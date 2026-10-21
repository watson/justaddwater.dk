---
title: "Windows SVN pre-commit-hook"
date: "2010-06-10T09:23:32"
slug: "windows-svn-pre-commit-hook"
url: "/2010/06/10/windows-svn-pre-commit-hook/"
wp_id: 1354
categories: ["Code"]
tags: ["Code", "subversion", "svn", "windows"]
---

At a current project I work on, we use a Windows server to run our subversion repository.

I wanted to set up the pre-commit hook so that commits with empty comment are automatically rejected.

All commit-hook example files that go with Subversion are written in bash (as unix servers tend to be the normal).

Here is a the pre-commit hook rewritten as a windows .bat file.

[View gist 432704 on GitHub](https://gist.github.com/432704)
