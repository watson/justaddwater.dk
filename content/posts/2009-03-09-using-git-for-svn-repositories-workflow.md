---
title: "Using Git for SVN Repositories Workflow"
date: "2009-03-09T14:52:11"
slug: "using-git-for-svn-repositories-workflow"
url: "/2009/03/09/using-git-for-svn-repositories-workflow/"
wp_id: 1038
categories: ["Code", "git"]
tags: ["git", "svn", "workflow"]
author: "jesper"
---

For the last months I have been using Git to work with my Subversion repositories. Besides from [reducing disk usage](/2009/01/17/git-side-benefit-reducing-disk-usage/ "justaddwater.dk | Git Side Benefit: Reducing Disk Usage"), Git also makes my work slightly faster and independent of network access -- I can make commits to repository which is sync'ed later when I get online.

One challenge though: Using branches

I ran into some pitfalls when using branches in Subversion repository. Here is a quick guide to how I setup and work with svn branches in git-svn.

### Useful git-svn command cheatsheet

For the lazy reader, let's just start with the compressed cheatsheet :)

``` bash
git svn clone -s [url_to_svn_repository] [project_name]

git branch -a #show all branches local(git) and remote(svn)

git status

git svn info #show svn details (also URL)

#create local Git branch that mirrors remote svn branch

git checkout -b local/RELEASE-0.12 RELEASE-0.12 #will connect with a remote svn branch named 'RELEASE-0.12'

git svn dcommit --dry-run # -n will show which svn branch you will commit into:

#=&gt; Committing to http://svn.edgewall.org/repos/trac/branches/0.11-stable ...

git svn rebase # pull changes from svn repository

git svn dcommit # push your local git commits to svn repository
```

### Step 1: Clone your repository with trunk, branches and tags

``` bash
git svn clone -s [url_to_svn_repository] [project_name]
```

The -s flag is important: It tells git to clone a standard svn layout with /trunk, /tags, /branches. NOTE that you have to use this -s flag to work with branches! Very important :)

Example: The Trac code repository has this layout by default. To make a git clone we do:

``` bash
git clone -s http://svn.edgewall.org/repos/trac trac.git

Initialized empty Git repository in /Users/jesper/othercode/trac.git/.git/
A    svntrac/__init__.py

[...]

M    trac/admin/console.py
r7937 = 2aab87158be06edb1a1931240a453cac762c4615 (trunk)
Auto packing your repository for optimum performance. You may also
run "git gc" manually. See "git help gc" for more information.
Counting objects: 13630, done.
Compressing objects: 100% (13146/13146), done.
Writing objects: 100% (13630/13630), done.
Total 13630 (delta 10584), reused 0 (delta 0)
Removing duplicate objects: 100% (256/256), done.
Checked out HEAD:
http://svn.edgewall.org/repos/trac/trunk r7937
```

SVN info shows the remote svn url:

``` bash
cd trac.git/
git svn info

Path: .
URL: http://svn.edgewall.org/repos/trac/trunk
Repository Root: http://svn.edgewall.org/repos/trac
Repository UUID: af82e41b-90c4-0310-8c96-b1721e28e2e2
Revision: 7937
Node Kind: directory
Schedule: normal
Last Changed Author: rblank
Last Changed Rev: 7937
Last Changed Date: 2009-03-07 03:52:37 +0100 (Sat, 07 Mar 2009)
```

### Step 2: Create local branch to mirror svn branch

`git branch -a` shows all branches and tags (both local and remote ones)

Use `git branch -a` to see all remote branches:

``` bash
git branch -a

* master
0.10-stable
0.11-stable
cboos-dev
cmlenz-dev
debian
debian-dev
jonas-dev
tags/debian
tags/debian-dev
tags/trac-0.10
tags/trac-0.10.1
tags/trac-0.10.2
tags/trac-0.10.3
[...]
trunk
utopiste-dev
```

Create local branch with same name as remote branch:

``` bash
git checkout -b local/0.11-stable 0.11-stable

Switched to a new branch "local/0.11-stable"
```

### Step 3: verify you are on new branch

``` bash
git svn dcommit --dry-run

Committing to http://svn.edgewall.org/repos/trac/branches/0.11-stable ...
```

(or git svn info)

``` bash
git svn info

git svn info
Path: .
URL: http://svn.edgewall.org/repos/trac/branches/0.11-stable
Repository Root: http://svn.edgewall.org/repos/trac
Repository UUID: af82e41b-90c4-0310-8c96-b1721e28e2e2
Revision: 7930
Node Kind: directory
Schedule: normal
Last Changed Author: rblank
Last Changed Rev: 7930
Last Changed Date: 2009-03-03 00:41:48 +0100 (Tue, 03 Mar 2009)
```

### Step 4: work with code

now you are free to work on the local branch: 'local/0.11-stable'. Hack on and commit to git with commands like:

``` bash
git status

git add filename

git commit -m 'my commit comment'
```

Repeat as much as you like. There are two strategies: Work on the master branch and then commit to the svn branch later.

### Step 5: commit to svn

``` bash
git svn rebase #to pull changes from svn before commit

git svn dcommit
```

If you get an error like this:

``` bash
git svn dcommit
Cannot dcommit with a dirty index.  Commit your changes first, or stash them with `git stash'.
at /usr/local/libexec/git-core//git-svn line 431
```

Just do what it says:

``` bash
git stash

git svn dcommit

git stash apply
```

The last line gets your dirty files back in your working directory.\
Applying change to multiple branches

Assume your change now is applied to the branch '0.11-stable'.

``` bash
git checkout master
git log --1
#=&gt; shows log of your latest commit
#To apply these changes to Trunk, now you should change branch and merge:

git checkout local/0.11-stable
git merge master #will merge changes to the current branch (local/0.11-stable) from trunk/master.

git svn dcommit #to commit the merged changes into the svn repository
```

### Related posts:

\* [Using Local File-based Git — Server Laziness](/2009/02/21/using-local-file-based-git-server-laziness/ "justaddwater.dk | Using Local File-based Git — Server Laziness") (Feb 21st)\
\* [Git Side Benefit: Reducing Disk Usage](/2009/01/17/git-side-benefit-reducing-disk-usage/ "justaddwater.dk | Git Side Benefit: Reducing Disk Usage") (Jan 17th)\
\* Dr Nic's Gitify command: [Going offline without your favourite Subversion repository?](http://drnicwilliams.com/2007/11/22/going-offline-without-your-favourite-subversion-repository/) (Nov 2007)
