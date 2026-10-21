---
title: "Using Local File-based Git -- Server Laziness"
date: "2009-02-21T10:04:59"
slug: "using-local-file-based-git-server-laziness"
url: "/2009/02/21/using-local-file-based-git-server-laziness/"
wp_id: 1029
categories: ["Code", "justaddwater.dk", "Web Development"]
tags: ["Code", "git", "ssh", "svn", "Web Development"]
---

My problem this week: I wanted to share some work with a colleague. Unfortunately we have not yet setup our caplab environment with git server. Nor did i want to push this particular project to GitHub or Unfuddle. My alternative was a file-based setup:

1.  Each developer's machine has it's own Git repository.
2.  On my machine I had an extra 'master' repository that other developers could push into.
3.  In the example below the local developer repos is called 'local' and the master is called 'remote'
4.  The master repository could be on a network drive as well.

Developer's workflow: Push changes to 'remote':

``` bash
cd local #developer's local repository
git pull ../remote master #get the latest code from 'remote' repository
git push ../remote master #push the recent commits from here to the 'remote' folder
```

### Git remote makes it easier

In stead of using a path in "git pull ../remote master", it's even easier to add the path just like you would do on GitHub or similar:

``` bash
git remote add origin ../remote/ #one time for all
git pull origin master # pull from the 'remote' directory
git push origin master #push recent commits from here to the 'remote' folder
```

### Bonus tip: Using remote git to SSH server

It's real easy to make a remote backup copy of your Git repository even if you have not set up a git server. Here is an example of how I did it on a server where I have SSH access to:

``` bash
git remote add origin ssh://jesper@myserver.com/~/project.git/
```

Setup the repository on the remote server:

``` bash
$ ssh jesper@myserver.com
Welcome to myserver.com!
$ mkdir project.git && cd project.git/
$ git --bare init
Initialized empty Git repository in /home/jesper/project.git
$ exit
Bye!
```

### Related posts:

- [Howto Create a Temporary Local Subversion Repository (April 2007)](../2007/04/26/howto-create-a-temporary-local-subversion-repository/ "Justaddwater.dk: Howto Create a Temporary Local Subversion Repository")
- [Git Side Benefit: Reducing Disk Usage](../2009/01/17/git-side-benefit-reducing-disk-usage/ "Justaddwater.dk: Git Side Benefit: Reducing Disk Usage") (January 17)
