---
title: "How to make Git ignore files that already exist in your project"
date: "2009-12-07T13:28:34"
slug: "how-to-make-git-ignore-files-that-already-exist-in-your-project"
url: "/2009/12/07/how-to-make-git-ignore-files-that-already-exist-in-your-project/"
wp_id: 1247
categories: ["Code", "git", "Web Development"]
tags: ["Code", "git", "ignore"]
author: "jesper"
---

For a project I'm working on, I had to change some files with personal settings, and the files kept showing up with a `git status`.

Adding files to .gitignore that are already tracked does not work. (and it's actually pretty well documented in the documentation). In stead, it's possible to use this command:

git update-index --assume-unchanged \[filename(s)\]

From [git-update-index manual page](http://www.kernel.org/pub/software/scm/git/docs/git-update-index.html):

>     --assume-unchanged
>     --no-assume-unchanged
>
> When these flags are specified, the object names recorded for the paths are not updated. Instead, these options set and unset the "assume unchanged" bit for the paths.
>
> When the "assume unchanged" bit is on, git stops checking the working tree files for possible modifications, so you need to manually unset the bit to tell git when you change the working tree file. This is sometimes helpful when working with a big project on a filesystem that has very slow lstat(2) system call (e.g. cifs).

Fantastic! my system files are now ignored by git :)

It's an incredibly useful tip for example if you have files that MUST live in the repository and that servers/editors change. In this particular project, Tomcat keeps changing two files. Furthermore I have changed the log-level from INFO to WARN which I should not commit into the repository.

`git update-index --assume-unchanged` lets me do exactly that.
