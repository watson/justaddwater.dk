---
title: "Git Side Benefit: Reducing Disk Usage"
date: "2009-01-17T14:28:52"
slug: "git-side-benefit-reducing-disk-usage"
url: "/2009/01/17/git-side-benefit-reducing-disk-usage/"
wp_id: 1014
categories: ["Code"]
tags: ["Code", "git", "gitify", "svn"]
---

A side benefit of switching from Subversion to Git for source control is that Git does not use shadow files and directories to find out what has changed.\
I created two checkouts of a svn project -- one using traditional svn and one using git (which can actually clone a svn repos -- see explanation below).

    [~/my-projects]  du -hd 0 \
    > berammelse berammelse.git \
    > dokboks dokboks.git       \
    > intrastat intrastat.git   \
    > kompetenceregister k2.git \
    > ourpeople ourpeople.git   \
    > let0004 let0004.git

    43M berammelse
    38M berammelse.git
    63M dokboks
    11M dokboks.git
    53M intrastat
    34M intrastat.git
    144M    kompetenceregister
    47M kompetenceregister.git
    118M    ourpeople
    151M    ourpeople.git
    163M    let0004
    98M let0004.git

For any project I tried this, Git uses significantly less disk space. It's just a side effect, I know. But more important: The git version has all the logfile history offline and that makes rolling forward/back much faster :)\
FYI i'm using my version of [Dr. Nic's "gitify"](http://drnicwilliams.com/2007/11/22/going-offline-without-your-favourite-subversion-repository/%20%20) command that wraps a "git svn" command. This way I can use git locally and then re-commit into svn when done.

    #!/usr/bin/env ruby -wKU
    # command from
    # http://drnicwilliams.com/2007/11/22/going-offline-without-your-favourite-subversion-repository/
    # Install with
    # sudo port install git-core +svn

    # get svn info location
    svnurl = `svn info | grep "^URL:"`.gsub('URL: ','').chomp

    # project = basename
    project = File.basename(Dir.pwd)

    puts cmd = "git svn clone #{svnurl} ../#{project}.git"

    `#{cmd}`

    puts "('git svn rebase' merges changes from svn.\n 'git svn dcommit' updates svn with your git commits)"
