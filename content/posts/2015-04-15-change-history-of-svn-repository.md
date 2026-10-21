---
title: "Change history of SVN repository"
date: "2015-04-15T23:06:48"
slug: "change-history-of-svn-repository"
url: "/2015/04/15/change-history-of-svn-repository/"
wp_id: 1759
categories: ["Code", "git"]
tags: []
---

Somebody asked me if it's possible to change history of an SVN repository like you can do in Git.

The easiest parts to change are:

- \
- commit date
  \
- commit log message
  

With this, you can easily modify time stamps if, for instance, your svn server clock is wrong.

## Step 1: Modify repository to accept property changes

Make sure your svn repository accepts property changes. (commit dates and messages are just properties which are basically unversioned).

For your repository, you need to make sure the hook file \`pre-revprop-change\` exists, is executable and has exit code 0. An easy way is to write a file which always exists with code 0:

\# write this file to \`repository_directory/hooks/pre-revprop-change\`

> \#!/usr/bin/env sh
>
> exit 0

##  Step 2: change date on the revision you want:

In this example I will set the date for revision 1 to May 1st, 1981.

> svn propset --revprop -r 1 svn:date "1981-05-01T10:00:00.000000Z"

\`svn propset\` command will set certain properties. You can set many properties, and in this example we manipulate \`svn:date\`. If we want to change the log message, we can use \`svn:log\`.

I deliberately chose a date from before SVN was made. Subversion is from 2001, so this commit is now made 20 years before SVN was out.

## All combined

I created a combined script, which has has the steps mentioned above, and also iterates to change all dates in a repository:

 

 

The result

The result is a fine modified commit history which could look like this

> \$ svn log\
> \
> \
>
> r10 \| jesper \| 1990-05-01 12:00:00 +0200 (Tue, 01 May 1990) \| 1 line commit number 10 (originally created 2015-04-15 22:21:35) ------------------------------------------------------------------------ r9 \| jesper \| 1989-05-01 12:00:00 +0200 (Mon, 01 May 1989) \| 1 line commit number 9 (originally created 2015-04-15 22:21:34) ------------------------------------------------------------------------ r8 \| jesper \| 1988-05-01 12:00:00 +0200 (Sun, 01 May 1988) \| 1 line commit number 8 (originally created 2015-04-15 22:21:33) ------------------------------------------------------------------------ r7 \| jesper \| 1987-05-01 12:00:00 +0200 (Fri, 01 May 1987) \| 1 line commit number 7 (originally created 2015-04-15 22:21:32) ------------------------------------------------------------------------ r6 \| jesper \| 1986-05-01 12:00:00 +0200 (Thu, 01 May 1986) \| 1 line commit number 6 (originally created 2015-04-15 22:21:31) ------------------------------------------------------------------------ r5 \| jesper \| 1985-05-01 12:00:00 +0200 (Wed, 01 May 1985) \| 1 line commit number 5 (originally created 2015-04-15 22:21:30) ------------------------------------------------------------------------ r4 \| jesper \| 1984-05-01 12:00:00 +0200 (Tue, 01 May 1984) \| 1 line commit number 4 (originally created 2015-04-15 22:21:29) ------------------------------------------------------------------------ r3 \| jesper \| 1983-05-01 12:00:00 +0200 (Sun, 01 May 1983) \| 1 line commit number 3 (originally created 2015-04-15 22:21:28) ------------------------------------------------------------------------ r2 \| jesper \| 1982-05-01 12:00:00 +0200 (Sat, 01 May 1982) \| 1 line commit number 2 (originally created 2015-04-15 22:21:27) ------------------------------------------------------------------------ r1 \| jesper \| 1981-05-01 12:00:00 +0200 (Fri, 01 May 1981) \| 1 line commit number 1 (originally created 2015-04-15 22:21:26) ------------------------------------------------------------------------

## More info

- SVN book [chapter on "pre-revprop-change"](http://svnbook.red-bean.com/en/1.7/svn.ref.reposhooks.pre-revprop-change.html)
- Rooot.net "[Change a SVN commit log message or date](http://www.rooot.net/en/development/code/16-change-svn-commit-log-date.html)"
- Stackoverflow: [Can I go back and edit comments on an SVN checkin?](http://stackoverflow.com/questions/692851/can-i-go-back-and-edit-comments-on-an-svn-checkin)
- Stackoverflow: [Change the timestamp of a SVN revision](http://stackoverflow.com/questions/633353/change-the-timestamp-of-a-svn-revision)
