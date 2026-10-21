---
title: "Replacement for Standard Windows Console"
date: "2007-04-30T11:48:28"
slug: "replacement-for-standard-windows-console"
url: "/2007/04/30/replacement-for-standard-windows-console/"
wp_id: 609
categories: ["Productivity", "Web Development"]
tags: []
---

The standard windows command window (console) sucks for several usability reasons:

- \
- Standard windows keyboard shortcuts don't work. It's not possible to copy/paste without using a special menu.
  \
- This special menu is best accessible with the mouse (or a long range of shortcuts)
  

Compare how it should be

> CTRL + V

With how it is in the standard console:

> ALT + SHIFT + space
>
> E (for edit)
>
> P (for paste)

Which means that my everyday work becomes very tedious than it has to be. Copy is even worse because you first have to put the editor into "mark" mode to make a selection before you do the ALT+SHIFT+space, then E, then C = even more time-consuming.

### Looking for a replacement

I have been using Console 2 for a while as it provides decent support for the basic shortcuts and tabs (to avoid clutter the task bar with multiple windows).

Console 2 has one major error in my environment: It freezes occationally when I use it for Ruby on Rails development (where I typically run 3 windows per application: one window for the webserver, one for the log-file, and one for commands).

So I'm ready to shift to a new console replacement

Microsoft PowerShell seems not to have tabs. At least it's not mentioned either on the product homepage or in Wikipedia.

"PowerCmd". On the paper, it looks very promising: Multiple windows in tabs, usual keyboard shortcuts are there. But also more advanced features that I have been missing, like line numbers, search and result highlighting, word wrap on/off, and to choose between block selection and line selection.

I'm sure that these features will help me speed up development further (if implemented properly), and look forward to try out the program.

More info:

- \
- [PowerCmd homepage\
  ](http://www.powercmd.com/)
  \
- [Console 2](http://sourceforge.net/projects/console/) on SourceForge
  \
- [Microsoft Powershell](http://www.microsoft.com/windowsserver2003/technologies/management/powershell/default.mspx) (and [team blog](http://blogs.msdn.com/powershell/ "Microsoft blog: Powershell"), found via [John Ericsson](http://john.se/blog/2006/07/01/searching-for-a-good-replacement-for-the-old-console-in-windows/ "John's Blog: Searching for a good replacement for the old console in Windows"))
  \
