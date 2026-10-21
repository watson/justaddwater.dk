---
title: "Forgotten Subversion Commands, Undo, Merge Branches and More"
date: "2012-06-28T20:42:46"
slug: "forgotten-subversion-commands-undo-merge-branches-and-more"
url: "/2012/06/28/forgotten-subversion-commands-undo-merge-branches-and-more/"
wp_id: 1587
categories: ["Code", "Web Development"]
tags: ["Code", "git", "subversion", "svn"]
---

In a current project I use a lot of Subversion (svn) from the command-line.

Subversion recently has lost terrain to Git for several reasons. But actually, svn is capable of doing many of the things I love from Git.

Here are some less known commands I find extremely helpful.

 

### Undo last commit

svn merge -r HEAD:PREV .

This commands merges in the changes required to go from latest version (HEAD) and back to the previous (PREV).

It also makes sense to view latest commit comment, and possibly include the revision number/description in your new commit message.

svn log --limit 1

After this, you should to an `svn status` and (if you are satisfied with the result), then commit:

svn commit -m "reverted accidentally committed previous version"

More info: [http://stackoverflow.com/questions/747713/subversion-retract-accidental-checkin/](http://stackoverflow.com/questions/747713/subversion-retract-accidental-checkin/747758#747758)

### View files changed since last update

svn st -u

The -u flag gives  an overview of **what has been updated on the server.** This is what IDEs like Eclipse and IntelliJ do behind the scenes.

I have seen much confusion caused when `svn log` will not show what changed on the server. In case you need more info, then investigate the changes with

svn log -r BASE:HEAD

As opposed to `svn log`, this command actually shows log messages on the server.

and if you need the list of files changed:

svn diff -r xxx:HEAD --summarize

Where xxx represents the version number of BASE (and you can get it with `svn info`)

More info: <http://stackoverflow.com/questions/1444005/displaying-a-list-of-files-that-have-changed-since-last-changeset-in-svn>

### Merge to branch from trunk

After branching, it's easy to keep up-to-date with changes of the trunk. Just go to the branch, and merge all from trunk, like this:

```
cd branch
svn merge ^/trunk
```

 

where as of Subversion 1.6, the  caret "^" is a handy annotation for the base repository url.

After this merge, you can just commit the changes with a standard comment that changes have been merge.

 

 

### Merge from trunk to current branch

In this case I want to merge all changes from trunk to a specific branch. (I am doing this daily to keep my branch updated). First step is to find the branch split point:

```
$ svn log --stop-on-copy | tail -n 4
r1769 | jesper | 2012-05-09 11:07:45 +0200 (Wed, 09 May 2012) | 1 line
Adding the new branch in subversion
------------------------------------------------------------------------
```

So, the revision number is "1769", which marks the first split point of the branch.

We now have a way to target all trunk changes with a higher revision number than "1769".

The merge command is then:

```
 svn merge -r 1769:HEAD ^/trunk .
```

 

 

 

If that matters I am using svn 1.6.
