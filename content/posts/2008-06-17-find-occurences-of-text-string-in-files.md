---
title: "Find Occurences of Text String in Files"
date: "2008-06-17T14:54:11"
slug: "find-occurences-of-text-string-in-files"
url: "/2008/06/17/find-occurences-of-text-string-in-files/"
wp_id: 934
categories: ["Software", "Unix"]
tags: []
author: "jesper"
---

I had to search for occurences of string in particular files, and using Cygwin i did the following:

find all files that ends on .js, .html or .ascx:\
`$ find -regextype posix-extended -regex ".+\.(js|html?|ascx)$"`

Then search for lines that contain the following javascript construction `for( var x in object)`

I ended up with this regular expression to match the javascript: `/for\s?\(.+?\bin\b.+?\)/`. Although not strictly necessary, i test for word-boundaries around `"in"` -- it would be sufficient just to use spaces like this `" in "`. For grep to eat this its pack with parameters that show filename (-H), line number (-n), only matching part of line (-o), and use Pearl compatible regexps (-P):

` grep -nHoP "for\s?\(.+?\bin\b.+?\)" `

Set this into a find expression where the -exec flag allows you to run the grep command on each file found:

`$ find -regextype posix-extended -regex ".+\.(js|html?|ascx)$" -exec grep -nHoP "for\s?\(.+?\bin\b.+?\)" '{}' \;`

**Choosing a -regextype for find**\
The regextype had to be changed and I found that these work with the chosen regexp:\
\* posix-extended, posix-awk, and posix-egrep\
but posix-basic did not work.
