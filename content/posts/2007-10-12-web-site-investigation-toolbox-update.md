---
title: "Web Site Investigation Toolbox Update"
date: "2007-10-12T10:54:01"
slug: "web-site-investigation-toolbox-update"
url: "/2007/10/12/web-site-investigation-toolbox-update/"
wp_id: 725
categories: ["HTML", "JavaScript", "Web Development", "Web Standards"]
tags: []
---

I figured the original bookmarklet toolbox needed an update (i have updated and added a few bookmarklets since I first posted [Toolbox — locating problems in HTML](/2006/09/18/toolbox/ "Permanent Link: Toolbox — locating problems in HTML")). Quirksmode detection, Layout grid and more.

For example I added "quirks or !quirks" to determine whether a page runs standards mode or quirks mode. It pops up an alert that displays rendering mode for each frame.

- \
- "Document mode: CSS1 Compat" is standards mode
  \
- "Document mode: Back compat" is quirksmode
  

I forget where I found the code (please notify me and I'll give you credit).I also modified [Steve Chipman's excellent "PageInfo"](http://slayeroffice.com/?c=/content/tools/pagenfo.html) so that its usable with frames. If frames are found it asks you to enter a frame number (index from document.frames\[x\])

I also added Andy Budd's [CSS grid layout bookmarklet](www.andybudd.com/archives/2006/07/layout_grid_bookmarklet/) which I find useful on occasions to see if things line up.

In general I find that I use these less and less, because much functionality is built into Firebug. But on some occations the bookmarklets can prove very handy.

Import all at once (separate HTML page):

**[Web Standards Investigation Tools (WSIT) HTML page](/wp-content/uploads/2007/10/web-standards-investigation-tools.html)** (last updated 2007-10-12)

![bookmarlets.png](/wp-content/uploads/2007/10/bookmarlets.png)

Instruction:

1.  Save the linked HTML page locally
2.  Open Firefox Bookmark Manager (Bookmarks \> Manage Bookmarks)
3.  Choose File \> Import …
4.  Import bookmarks into “Bookmarks Toolbar Folder” for easy access to them.

More info:

- [Toolbox — locating problems in HTML](/2006/09/18/toolbox/ "Permanent Link: Toolbox — locating problems in HTML")
- Original [Web Standards Investigation Tools (WSIT) bookmarklets](/2006/06/29/webstandards-case-study/) (September 2006)
- [Technique for locating problems in HTML](/2006/09/18/technique) (September 2006)
- [Why web standards matter (case study) (June 2006)](/2006/06/29/webstandards-case-study/)
