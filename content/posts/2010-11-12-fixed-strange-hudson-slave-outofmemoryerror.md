---
title: "Fixed Strange Hudson Slave OutOfMemoryError"
date: "2010-11-12T11:19:43"
slug: "fixed-strange-hudson-slave-outofmemoryerror"
url: "/2010/11/12/fixed-strange-hudson-slave-outofmemoryerror/"
wp_id: 1373
categories: ["Continous integration", "Java"]
tags: ["continuous integration", "hudson", "Java", "setup", "slave"]
author: "jesper"
---

At a current project I am working on, we use Hudson and Maven to build our Java code. Strangely, one of the slaves constantly failed with an OutOfMemory error. We tried two obvious fixes. The first did not work:

Not working strategy: To append memory params on the job itself. We modified the job inside Hudson configuration and added `-Xmx512m -XX:MaxPermSize=256m` to the MAVEN_OPTS field in the "build" section of the job configuration.

[{{< img src=`/wp-content/uploads/2010/11/mavensettings-for-hudson-slave-job-300x161.png` alt=`` title=`mavensettings-for-hudson-slave-job` class=`alignright size-medium wp-image-1374` width=`300` height=`161` >}}](/wp-content/uploads/2010/11/mavensettings-for-hudson-slave-job.png)

Unfortunately this did not work. Still an OutOfMemoryError on the Hudson slave. Fortunately, another strategy actually worked: To modify the settings of the slave service/daemon itself.

So appending memory params to the `hudson-slave.xml`. Locate the xml section `service=>arguments`. Add the following code.\
From:

> \<executable\>C:\Program Files\Java\jre6\bin\java.exe\</executable\>
>
> \<arguments\>\
> -Xrs -jar "%BASE%\slave.jar"\
> -jnlpUrl http://hudsonMaster:8080/hudson/computer/JesperRonn/slave-agent.jnlp\
> \</arguments\>

To:

> \<executable\>C:\Program Files\Java\jre6\bin\java.exe\</executable\>
>
> \<arguments\>\
> **-Xmx512m -XX:MaxPermSize=256m**\
> -Xrs -jar "%BASE%\slave.jar"\
> -jnlpUrl http://hudsonMaster:8080/hudson/computer/JesperRonn/slave-agent.jnlp\
> \</arguments\>

That actually solved the problem. Remember to restart the hudson slave service/daemon\
append. For reference, here is the [hudson-slave-example.xml](http://justaddwater.dk/wp-content/uploads/2010/11/hudson-slave-example.xml_.txt).

Full stacktrace from the original error:

> \
> `Exception:`\
> `Stacktrace:`\
> `org.apache.commons.jelly.JellyTagException: jar:file:/C:/deployer/hudson/war/WEB-INF/lib/hudson-core-1.382.jar!/hudson/model/Run/console.jelly:67:27: Java heap space`\
> `at org.apache.commons.jelly.impl.TagScript.handleException(TagScript.java:728)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:290)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:161)`\
> `at org.apache.commons.jelly.tags.core.OtherwiseTag.doTag(OtherwiseTag.java:41)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:161)`\
> `at org.apache.commons.jelly.tags.core.ChooseTag.doTag(ChooseTag.java:38)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.CallTagLibScript$1.run(CallTagLibScript.java:75)`\
> `at org.apache.commons.jelly.tags.define.InvokeBodyTag.doTag(InvokeBodyTag.java:91)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.apache.commons.jelly.tags.core.CoreTagLibrary$1.run(CoreTagLibrary.java:98)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.apache.commons.jelly.tags.core.CoreTagLibrary$2.run(CoreTagLibrary.java:105)`\
> `at org.kohsuke.stapler.jelly.CallTagLibScript.run(CallTagLibScript.java:96)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.CallTagLibScript$1.run(CallTagLibScript.java:75)`\
> `at org.apache.commons.jelly.tags.define.InvokeBodyTag.doTag(InvokeBodyTag.java:91)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.apache.commons.jelly.tags.core.CoreTagLibrary$2.run(CoreTagLibrary.java:105)`\
> `at org.kohsuke.stapler.jelly.CallTagLibScript.run(CallTagLibScript.java:96)`\
> `at org.kohsuke.stapler.jelly.CompressTag.doTag(CompressTag.java:21)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.kohsuke.stapler.jelly.JellyViewScript.run(JellyViewScript.java:40)`\
> `at org.kohsuke.stapler.jelly.DefaultScriptInvoker.invokeScript(DefaultScriptInvoker.java:40)`\
> `at org.kohsuke.stapler.jelly.DefaultScriptInvoker.invokeScript(DefaultScriptInvoker.java:30)`\
> `at org.kohsuke.stapler.jelly.JellyFacet$1.dispatch(JellyFacet.java:67)`\
> `at org.kohsuke.stapler.Stapler.invoke(Stapler.java:537)`\
> `at org.kohsuke.stapler.MetaClass$13.dispatch(MetaClass.java:359)`\
> `at org.kohsuke.stapler.Stapler.invoke(Stapler.java:537)`\
> `at org.kohsuke.stapler.MetaClass$7.doDispatch(MetaClass.java:219)`\
> `at org.kohsuke.stapler.NameBasedDispatcher.dispatch(NameBasedDispatcher.java:30)`\
> `at org.kohsuke.stapler.Stapler.invoke(Stapler.java:537)`\
> `at org.kohsuke.stapler.Stapler.invoke(Stapler.java:453)`\
> `at org.kohsuke.stapler.Stapler.service(Stapler.java:135)`\
> `at javax.servlet.http.HttpServlet.service(HttpServlet.java:45)`\
> `at winstone.ServletConfiguration.execute(ServletConfiguration.java:249)`\
> `at winstone.RequestDispatcher.forward(RequestDispatcher.java:335)`\
> `at winstone.RequestDispatcher.doFilter(RequestDispatcher.java:378)`\
> `at hudson.util.PluginServletFilter$1.doFilter(PluginServletFilter.java:94)`\
> `at hudson.util.PluginServletFilter.doFilter(PluginServletFilter.java:86)`\
> `at winstone.FilterConfiguration.execute(FilterConfiguration.java:195)`\
> `at winstone.RequestDispatcher.doFilter(RequestDispatcher.java:368)`\
> `at hudson.security.csrf.CrumbFilter.doFilter(CrumbFilter.java:47)`\
> `at winstone.FilterConfiguration.execute(FilterConfiguration.java:195)`\
> `at winstone.RequestDispatcher.doFilter(RequestDispatcher.java:368)`\
> `at hudson.security.ChainedServletFilter$1.doFilter(ChainedServletFilter.java:84)`\
> `at hudson.security.ChainedServletFilter.doFilter(ChainedServletFilter.java:76)`\
> `at hudson.security.HudsonFilter.doFilter(HudsonFilter.java:164)`\
> `at winstone.FilterConfiguration.execute(FilterConfiguration.java:195)`\
> `at winstone.RequestDispatcher.doFilter(RequestDispatcher.java:368)`\
> `at winstone.RequestDispatcher.forward(RequestDispatcher.java:333)`\
> `at winstone.RequestHandlerThread.processRequest(RequestHandlerThread.java:244)`\
> `at winstone.RequestHandlerThread.run(RequestHandlerThread.java:150)`\
> `at java.lang.Thread.run(Unknown Source)`\
> `Caused by: java.lang.OutOfMemoryError: Java heap space`\
> `at hudson.console.ConsoleNote.readFrom(ConsoleNote.java:220)`\
> `at hudson.console.ConsoleAnnotationOutputStream.eol(ConsoleAnnotationOutputStream.java:109)`\
> `at hudson.console.LineTransformationOutputStream.eol(LineTransformationOutputStream.java:60)`\
> `at hudson.console.LineTransformationOutputStream.write(LineTransformationOutputStream.java:56)`\
> `at hudson.console.LineTransformationOutputStream.write(LineTransformationOutputStream.java:74)`\
> `at org.apache.commons.io.output.ProxyOutputStream.write(ProxyOutputStream.java:70)`\
> `at org.apache.commons.io.output.CountingOutputStream.write(CountingOutputStream.java:71)`\
> `at org.kohsuke.stapler.framework.io.LargeText.writeLogTo(LargeText.java:145)`\
> `at hudson.console.AnnotatedLargeText.writeHtmlTo(AnnotatedLargeText.java:154)`\
> `at hudson.model.Run.writeLogTo(Run.java:1038)`\
> `at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)`\
> `at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)`\
> `at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)`\
> `at java.lang.reflect.Method.invoke(Unknown Source)`\
> `at org.apache.commons.jexl.util.introspection.UberspectImpl$VelMethodImpl.invoke(UberspectImpl.java:258)`\
> `at org.apache.commons.jexl.parser.ASTMethod.execute(ASTMethod.java:104)`\
> `at org.apache.commons.jexl.parser.ASTReference.execute(ASTReference.java:83)`\
> `at org.apache.commons.jexl.parser.ASTReference.value(ASTReference.java:57)`\
> `at org.apache.commons.jexl.parser.ASTReferenceExpression.value(ASTReferenceExpression.java:51)`\
> `at org.apache.commons.jexl.ExpressionImpl.evaluate(ExpressionImpl.java:80)`\
> `at hudson.ExpressionFactory2$JexlExpression.evaluate(ExpressionFactory2.java:72)`\
> `at org.apache.commons.jelly.impl.ExpressionScript.run(ExpressionScript.java:66)`\
> `at org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:161)`\
> `at org.apache.commons.jelly.tags.core.WhitespaceTag.doTag(WhitespaceTag.java:48)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.kohsuke.stapler.jelly.ReallyStaticTagLibrary$1.run(ReallyStaticTagLibrary.java:76)`\
> `at org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:161)`\
> `at org.apache.commons.jelly.tags.core.OtherwiseTag.doTag(OtherwiseTag.java:41)`\
> `at org.apache.commons.jelly.impl.TagScript.run(TagScript.java:270)`\
> `at org.apache.commons.jelly.impl.ScriptBlock.run(ScriptBlock.java:95)`\
> `at org.apache.commons.jelly.TagSupport.invokeBody(TagSupport.java:161)`\
