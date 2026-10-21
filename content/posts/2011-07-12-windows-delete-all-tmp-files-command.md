---
title: "Windows delete all tmp files command"
date: "2011-07-12T21:34:10"
slug: "windows-delete-all-tmp-files-command"
url: "/2011/07/12/windows-delete-all-tmp-files-command/"
wp_id: 1419
categories: ["Code"]
tags: ["command-line", "windows"]
author: "jesper"
---

Just a quick note to self about this tip i found. It is a Windows (XP) helpful command line snippet that removes all your temporary files.

Delete all files in temp folder:

```
DEL /F /S /Q %TEMP%
```

Taken from the "[A-Z Index of the Windows CMD command line](http://ss64.com/nt/del.htm)"
