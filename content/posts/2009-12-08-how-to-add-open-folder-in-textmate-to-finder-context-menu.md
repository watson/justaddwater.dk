---
title: "How To add \"Open folder in Textmate\" to Finder Context Menu"
date: "2009-12-08T10:44:43"
slug: "how-to-add-open-folder-in-textmate-to-finder-context-menu"
url: "/2009/12/08/how-to-add-open-folder-in-textmate-to-finder-context-menu/"
wp_id: 1252
categories: ["OS X"]
tags: ["automator", "mac", "osx", "textmate"]
author: "jesper"
---

I wanted to add a menu item in Finder's context menu that would open the selected folder in Textmate.\
[![Textmate context menu item: Open selected folder in Textmate](/wp-content/uploads/2009/12/Screen-shot-2009-12-08-at-10.24.20-AM-289x300.png "Textmate context menu item: Open selected folder in  Textmate")](/wp-content/uploads/2009/12/Screen-shot-2009-12-08-at-10.24.20-AM.png)

A google search suggested the method described by K. Adam Christensen on his blog: "[Opening a directory in TextMate from Finder](http://shifteleven.com/articles/2006/09/17/opening-a-directory-in-textmate-from-finder)". However, from the documentation, I learned that that method is now outdated. Snow Leopard users should use "Services" and not "workflow" for setting this up.

Here is what I did:

Open Automator.app.

From the menu item "File" \> "New" choose "Services"

[![Automator-File-New-Service](/wp-content/uploads/2009/12/Screen-shot-2009-12-08-at-10.22.00-AM-300x280.png "Automator-File-New-Service")](/wp-content/uploads/2009/12/Screen-shot-2009-12-08-at-10.22.00-AM.png)

Now there are 3 steps to be filled out like so:

[![Automator final setup for "open in textmate" Finder.app context menu itm](/wp-content/uploads/2009/12/Screen-shot-2009-12-08-at-10.23.23-AM-300x152.png "Automator final setup for "open in textmate" Finder.app context menu itm")](/wp-content/uploads/2009/12/Screen-shot-2009-12-08-at-10.23.23-AM.png)\
First, edit the top so that "Service recieves selected: **files or folders** in **Finder.app**".

Second, add the action "Get Selected Finder Items" from the left column (use the search field to find, then drag selected into the right work area).

Third, add the action "Run Shell Script" to your service. Fill in the following command:

cat \| xargs mate

Finally, choose "File" \> "Save..." and give it a name like "Open in Textmate"
