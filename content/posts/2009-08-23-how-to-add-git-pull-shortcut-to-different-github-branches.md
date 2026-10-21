---
title: "How to add Git Pull Shortcut to Different Github Branches"
date: "2009-08-23T23:42:45"
slug: "how-to-add-git-pull-shortcut-to-different-github-branches"
url: "/2009/08/23/how-to-add-git-pull-shortcut-to-different-github-branches/"
wp_id: 1117
categories: ["Code", "git", "Web Development"]
tags: ["Code", "git", "github"]
---

**UPDATE 9 hours later: Changed to "remote = origin" to the specific branch "remote = dean" which works!**

Short explanation on how to pull changes from different Git repositories into your local Git repository.

Last week I worked with three different Github forks of a project. Now for standard, when you clone a Github repository, the remote repository is automatically added so you can do a simple git pull (instead of the verbose version "git pull origin master")

Now, let's say you'd like to pull changes from another branch/fork on Github:

> git remote add dean git://github.com/dstrelau/webrat.git\
> git co -b dean\
> git pull dean master

Git pull dean master will work. but "git pull" gives the following message:

> \[~/othercode/webrat (master)\] ➔ git co dean\
> Switched to branch 'dean'\
> \[~/othercode/webrat (dean)\] ➔ git pull\
> You asked me to pull without telling me which branch you\
> want to merge with, and 'branch.dean.merge' in\
> your configuration file does not tell me either.    Please\
> specify which branch you want to merge on the command line and\
> try again (e.g. 'git pull \<repository\> \<refspec\>').\
> See git-pull(1) for details.
>
> If you often merge with the same branch, you may want to\
> configure the following variables in your configuration\
> file:
>
> branch.dean.remote = \<nickname\>\
> branch.dean.merge = \<remote-ref\>\
> remote.\<nickname\>.url = \<url\>\
> remote.\<nickname\>.fetch = \<refspec\>
>
> See git-config(1) for details.


## Solution to get the shorthand "git pull" to work:

Add the following section to \[project_dir\]/.git/config

> \[branch "dean"\]\
> remote = dean\
> merge = refs/heads/master

So my ./git/config file now looks like this:

> \[core\]\
> repositoryformatversion = 0\
> filemode = true\
> bare = false\
> logallrefupdates = true\
> ignorecase = true\
> \[remote "origin"\]\
> url = git://github.com/brynary/webrat.git\
> fetch = +refs/heads/\*:refs/remotes/origin/\*\
> \[branch "master"\]\
> remote = origin\
> merge = refs/heads/master\
> \[remote "jonas"\]\
> url = git://github.com/jnicklas/webrat.git\
> fetch = +refs/heads/\*:refs/remotes/jonas/\*\
> \[branch "jonas"\]\
> remote = jonas\
> merge = refs/heads/master\
> \[remote "dean"\]\
> url = git://github.com/dstrelau/webrat.git\
> fetch = +refs/heads/\*:refs/remotes/dean/\*\
> \[branch "dean"\]\
> remote = dean\
> merge = refs/heads/master\
> \[branch "orig"\]\
> remote = origin\
> merge = refs/heads/master
