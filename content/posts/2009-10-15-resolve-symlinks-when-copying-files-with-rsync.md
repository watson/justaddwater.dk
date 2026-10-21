---
title: "Resolve Symlinks When Copying Files With Rsync"
date: "2009-10-15T10:58:49"
slug: "resolve-symlinks-when-copying-files-with-rsync"
url: "/2009/10/15/resolve-symlinks-when-copying-files-with-rsync/"
wp_id: 1207
categories: ["Code"]
tags: []
author: "jesper"
---

In a project I'm working on there is a structure where images and css are common for some of the subprojects. One folder has static pages for testing HTML + CSS layout. This folder has some symlinks to the /css folder and /images folder.

Now, on my Mac during normal development, this works perfectly. But I also wanted to access the static HTML files via my virtual windows machine. And I cannot follow the unix symlinks from my virtual windows machine!

My solution was to copy the files to another folder with rsync, which can then resolve the symlink into real files.

    #!/bin/sh
    # set -x
    # Script will copy contents of current dir (except the files defined in _exclude_list)
    # into it's own separate folder. It will also expand symlinks so that windows users
    # can use the script directly
    # Created 2009-10-14 by Jesper Rønn-Jensen
    echo ".*
    _*" > _exclude_list.txt

    cd `dirname $0`
    BASE=`pwd -P`
    DEST=`dirname ~/src/htmlguide` #remember trailing slash of parent
    FLAGS=' -av --exclude-from _exclude_list.txt --delete'

    rsync $FLAGS --copy-dirlinks $BASE $DEST/ #remember trailing slash at destination

The rsync flag `--copy-dirlinks` does the magic by expanding all symlinks and copying the files. Besides from that, I make sure to `--delete` files no longer present in the source folder.

I decided to use rsync in stead of for example a webserver, as this approach is more portable, and I can then zip the static files or deploy them elsewhere.

If you want to improve on the script, feel free to [fork it on github gist 210796](http://gist.github.com/210796).
