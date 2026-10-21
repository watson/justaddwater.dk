---
title: "Spoken Git Commit Log — Another Annoyance at the Office"
date: "2009-09-30T10:23:26"
slug: "spoken-git-commit-log-%e2%80%94-another-annoyance-at-the-office"
url: "/2009/09/30/spoken-git-commit-log-%e2%80%94-another-annoyance-at-the-office/"
wp_id: 1161
categories: ["Code", "git", "Humor", "Web Development"]
tags: ["Code", "git", "Humor", "logging"]
---

Here is a short one-liner that really annoyed my colleagues today.\
I set my mac to read aloud all changes in the repository since yesterday:

     git  log --pretty=format:"%an commit %s, %ad." --date=relative --since=yesterday |say

if you remove the "say" command in the end it's actually pretty readable:

    pagerbak commit VA17, 34 minutes ago.
    pagerbak commit VA17 - Not used, 35 minutes ago.
    therikss commit , 48 minutes ago.
    pagerbak commit Checkstyle configuration, 56 minutes ago.
    pagerbak commit Checkstyle configuration, 56 minutes ago.
    pagerbak commit Checkstyle configuration, 57 minutes ago.
    pagerbak commit Checkstyle configuration, 57 minutes ago.
    pagerbak commit Checkstyle configuration, 57 minutes ago.
    pagerbak commit Checkstyle configuration, 57 minutes ago.
    pagerbak commit Checkstyle configuration, 58 minutes ago.
    pagerbak commit Library update. Axis2 updated, 58 minutes ago.
    pagerbak commit Checkstyle configuration, 59 minutes ago.
    pagerbak commit New certificates, VA17, Library update, Checkstyle, 60 minutes ago.
    pagerbak commit Checkstyle configuration, 61 minutes ago.
    pagerbak commit Checkstyle configuration, 62 minutes ago.
    pagerbak commit ?, 63 minutes ago.
    pagerbak commit Checkstyle configuration, 63 minutes ago.
    pagerbak commit Added a few extra SAML2 related methods for VA17, 64 minutes ago.
    nstrandb commit fixes, 75 minutes ago.
    nstrandb commit fixes, 75 minutes ago.
    pagerbak commit VA17 Login for existing user work., 76 minutes ago.

While reading it aloud seems pretty evil and intriguing, it was actually bit of a laugh at the office.

PS. Time to look for a better hobby :)
