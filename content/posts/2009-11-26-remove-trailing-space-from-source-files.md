---
title: "How to Remove Trailing Space from source files"
date: "2009-11-26T15:10:40"
slug: "remove-trailing-space-from-source-files"
url: "/2009/11/26/remove-trailing-space-from-source-files/"
wp_id: 1241
categories: ["Code"]
tags: ["Code", "find", "sed", "shell", "trailing", "whitespace"]
---

When it comes to source code, i am a perfectionist. I cant stand to see trailing whitespace, interchanged tabs/spaces, etc.

This Stackoverflow user asked [How To Remove Trailing Whitespace Of All Files Recursively](http://stackoverflow.com/questions/149057/how-to-removing-trailing-whitespace-of-all-files-recursively).

This reply helped me to work around the fact that \s and \t are not supported in the mac version of sed:

> find dir -type f -print0 \| xargs -0 sed -i .bak -E "s/\[\[:space:\]\]\*\$//"

So using \[:space:\] can actually work for both tabs and spaces.

However, I ended up not using 'find' for the files, and then passing the files to sed directly:

> sed -i '' 's/\[\[:space:\]\]\*\$//g' \*\*/\*.\*
