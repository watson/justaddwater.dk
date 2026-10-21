---
title: "Importing Existing Git repository into SVN"
date: "2009-07-08T10:59:58"
slug: "importing-existing-git-repository-into-svn"
url: "/2009/07/08/importing-existing-git-repository-into-svn/"
wp_id: 1104
categories: ["Code"]
tags: ["Code", "git", "subversion", "svn", "Web Development"]
author: "jesper"
---

Many of my colleagues know svn but are in general not (yet) ready jump over to using Git for bigger projects.

Today I had to import my existing Git repository into SVN. I had been working locally with a Git repos and wanted to keep my history before giving access to my colleagues.

The guide from Google Code is really easy, and the commands are just to follow (although several of them I don't understand). Set the following variables to fit your needs

USERNAME=jesper\
SVN_REPOS=https://project.caplab.dk/svn/\
\#NOTE in my example I expect standard /trunk, /tags, /branches layout\
EXISTING_GIT_REPO=~/src/expensereport.git\
NEW_GIT_SVN_REPO=~/src/expensereport

     $ git svn clone --username $USERNAME $SVN_REPOS $NEW_GIT_SVN_REPO
     $ cd $NEW_GIT_SVN_REPO
     $ git fetch $EXISTING_GIT_REPO

     $ git branch tmp $(cut -b-40 .git/FETCH_HEAD)
     $ git tag -a -m "Last fetch" last tmp

     $ INIT_COMMIT=$(git log tmp --pretty=format:%H | tail -1)
     $ git checkout $INIT_COMMIT .
     $ git commit -C $INIT_COMMIT

     $ git rebase master tmp
     $ git branch -M tmp master

    $ git svn dcommit

Later, export Git repository updates to SVN as follows:

     $ git fetch $EXISTING_GIT_REPO
     $ git branch tmp $(cut -b-40 .git/FETCH_HEAD)
     $ git tag -a -m "Last fetch" newlast tmp
     $ git rebase --onto master last tmp
     $ git branch -M tmp master
     $ git svn dcommit
     $ mv .git/refs/tags/newlast .git/refs/tags/last

Find the full explanation from the Google Code wiki: [ImportingFromGit\
Import a Git repository to Google Code.\
](http://code.google.com/p/support/wiki/ImportingFromGit)

Found via Stackoverflow: [Pushing an existing git repository to SVN](http://stackoverflow.com/questions/661018/pushing-an-existing-git-repository-to-svn)
