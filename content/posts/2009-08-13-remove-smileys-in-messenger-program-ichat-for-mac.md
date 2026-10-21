---
title: "Remove smileys in messenger program (iChat for mac)"
date: "2009-08-13T14:17:55"
slug: "remove-smileys-in-messenger-program-ichat-for-mac"
url: "/2009/08/13/remove-smileys-in-messenger-program-ichat-for-mac/"
wp_id: 1106
categories: ["OS X", "Software", "Usability"]
tags: []
author: "jesper"
---

It has long annoyed me that there is no intuitive, straightforward way to disable smileys in chat programs.

Today I found that these two commands can do it for iChat for mac:

> \$ cd /Applications/iChat.app/Contents/Resources/English.lproj/\
> \$ mv SmileyTable.plist SmileyTable.plist.bak

Restart iChat. (tip from MacOSXhints.com: [Disable graphical smileys in iChat 3.0](http://www.macosxhints.com/article.php?story=20050522145205539) but it works for me on Mac OS X 10.5.8 with iChat 4.0.8 (619).

Now my conversations look like this:\
![ichat-messenger-with-smileys-disabled](/wp-content/uploads/2009/08/ichat-messenger-with-smileys-disabled-218x300.png "ichat-messenger-with-smileys-disabled")

Which reminds me that I better soon write a short article on the problem of having the wrong and obtrusive defaults in your applications.
