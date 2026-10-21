---
title: "Maven mirrorOf * in settings.xml breaks the build"
date: "2012-01-20T22:37:59"
slug: "maven-mirrorof-in-settings-xml-breaks-the-build"
url: "/2012/01/20/maven-mirrorof-in-settings-xml-breaks-the-build/"
wp_id: 1550
categories: ["Code"]
tags: ["Code", "maven", "nexus"]
---

In our maven3 pom.xml files for a particular project, we have defined a reference to an internal Nexus repository. Since we are behind a firewall, the Nexus repository also has to be mirror of the outside world. I discovered that this **generic \<mirrorOf\> from my settings.xml is actually evil**:

```
<!-- settings.xml -->
<mirrors>
  <mirror>
    <id>insideFirewallRepo</id>
    <mirrorOf>*</mirrorOf>
    <name>Mirror of the world outside.</name>
    <url>http://nexus_url/nexus/content/groups/public/</url>
  </mirror>
</mirrors>
```

The reason for this being evil was our project pom files which had the following references

```
<properties>
  <nexus.url>http://nexus_url/nexus</nexus.url>
  <subversion.url>http://svn_url/svn</subversion.url>
</properties>

  <scm>
    <connection>scm:svn:${subversion.url}/common-gwt-gui/trunk</connection>
</scm>

<repositories>
    <repository>
        <id>nexus-repo-releases</id>
        <name>Nexus Repo</name>
        <url>${nexus.url}/content/groups/public/</url>
        <releases> <enabled>true</enabled> </releases>
        <snapshots> <enabled>false</enabled> </snapshots>
    </repository>
    <repository>
        <id>nexus-repo-snapshots</id>
        <name>Nexus Repo</name>
        <url>${nexus.url}/content/groups/public-snapshots/</url>
        <releases> <enabled>false</enabled> </releases>
        <snapshots> <enabled>true</enabled> </snapshots>
    </repository>
 </repositories>
[repeat the <repositories> section for <pluginRepositories>]
```

And the same pom file contains the following \<distributionManagement\> section:

```
<distributionManagement>
    <repository>
        <id>company.releases</id>
        <url>${nexus.url}/content/repositories/company/</url>
    </repository>
    <snapshotRepository>
        <id>company.snapshots</id>
        <url>${nexus.url}/content/repositories/company-snapshots/</url>
    </snapshotRepository>
</distributionManagement>
```

Finally we have the maven release-plugin, but this irrelevant for now:

```
<build>
    <plugins>
        <plugin>
            <artifactId>maven-release-plugin</artifactId>
            <configuration>
                <tagBase>${subversion.url}/project_name/releases</tagBase>
            </configuration>
        </plugin>
    </plugins>
 </build>
```

## Error message: Using the wrong repository for snapshots

Now, the generic mirrorOf \* in settings.xml actually overrides the specific repository information we set in the pom.xml. Because of that setting, the pom.xml \<repository\> is not used. And the result is an error message like this. (error message enhanced in bold)

```
Downloading: http://nexus_url/nexus/content/groups/public/com/company/dependency_project/1.18-SNAPSHOT/maven-metadata
.xml
Downloading: http://nexus_url/nexus/content/groups/public/com/company/dependency_project/1.18-SNAPSHOT/maven-metadata
.xml
Downloading: http://nexus_url/nexus/content/groups/public/com/company/dependency_project/1.18-SNAPSHOT/dependency_project
-1.18-SNAPSHOT.pom
[WARNING] The POM for com.company:dependency_project:jar:1.18-SNAPSHOT is missing, no dependency information available
Downloading: http://nexus_url/nexus/content/groups/public/com/company/dependency_project/1.18-SNAPSHOT/dependency_project
-1.18-SNAPSHOT.jar
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary:
[INFO]
[INFO] project_name ...................................... FAILURE [1.108s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.364s
[INFO] Finished at: Fri Jan 20 12:28:04 CET 2012
[INFO] Final Memory: 5M/15M
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal on project project_name: Could not resolve dependencies for project com.company:project_name:jar:2.1.1
3-SNAPSHOT: Could not find artifact com.company:dependency_project:jar:1.18-SNAPSHOT in insideFirewallRepo (http://nexus_url
/nexus/content/groups/public/) -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/DependencyResolutionException
[ERROR]
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <goals> -rf :project_name
```

```
Notice that the errormessage actually gave the ID of our <mirror> from settings.xml:
<!-- settings.xml -->
 <mirrors>
   <mirror>
     <id>insideFirewallRepo</id>
```

So problem is that maven actually does not use the pom.xml settings, but we can easily fix this.

Solution: Exclude local repositories from mirrorOf \*

We need to force Maven to use the \<repository\> values from the project pom.xml. And  maven can do just that, since we need to take the \<repository\> ids and exclude them from mirrorOf \*.

Take the repository ids from the pom file:

```
<repositories>
<repository><id>nexus-repo-releases</id><repository>
<repository><id>nexus-repo-snapshots</id><repository>
```

And exclude them to mirrorOf in settings.xml (add an exclamation mark in front of them). Line added enhanced in bold:

```
<!-- settings.xml -->
<mirrors>
  <mirror>
    <id>insideFirewallRepo</id>
    <mirrorOf>!nexus-repo-releases,!nexus-repo-snapshots,*</mirrorOf>
    <name>Mirror of the world outside.</name>
    <url>http://nexus_url/nexus/content/groups/public/</url>
  </mirror>
</mirrors>
```

Most users could probably just remove the \<mirrors\> block from settings.xml, but in this particular project, that is not possible since firewall blocks for access to maven central. So, in order for us to use external dependencies, we must use the \<mirror\> in settings.xml

Then, you could argue, to use \<proxy\> instead of \<mirrors\> in settings.xml. This may be a decent solution as well, but in my case i wanted to avoid that, since the company proxy required user/password. Our jenkins build machines would then have my username/password, and it would lock my account whenever my password expires.

Within those constraints, the \<mirror\> block with excluded internal repositories seems like a decent fit.

For the issues described in this article, I have been using Maven 3.0.3 and Sonatype Nexus 1.9.2
