---
title: "Fixing the Keyboard Shortcut Problem"
date: "2006-01-09T19:15:47"
slug: "fixing-the-keyboard-shortcut-problem"
url: "/2006/01/09/fixing-the-keyboard-shortcut-problem/"
wp_id: 59
categories: ["Usability"]
tags: []
author: "thomas"
technorati: ["shortcuts", "keyboard shortcuts", "internationalization", "i18n", "usability", "Windows XP", "Microsoft Office", "Windows", "XP"]
---

I just read a post on "Jensen Harris: An Office User Interface Blog" called "[The 50/50 Rule](http://blogs.msdn.com/jensenh/archive/2006/01/09/510783.aspx)" which got me thinking...

As a citizen of a non-English speaking country - in my case Denmark - where the preferred language last time I checked was Danish, I often get annoyed when I work on a computer that runs a Danish version of Windows. You see since I’m a techie I prefer all my software in English and so far all my desktop computers run both an English Windows and an English Office Suite - Even the laptop I got from work is all English. But from time to time I find my self in front of a Danish speaking machine.

Besides the obvious language differences in the GUI, I find it a major problem that all the keyboard shortcuts have changed when I’m using a non-English piece of software. The reason is of cause obvious. But I’m an experienced Windows user and are used to the English shortcuts. In my world they make sense.

Ctrl+F usually stand for “Find” and Ctrl+B for “Bold”. But in Danish this of cause does not make sense. In Danish “Bold” is spelled “Fed” so to use Ctrl+B would suddenly not make that much sense anymore. “Find” in Danish and English is actually spelled the same so here you would expect the keyboard shortcut to remain the same, but no - as you can see in the table below they have switched place:

|      | English | Danish |
|------|---------|--------|
| Find | Ctrl+F  | Ctrl+B |
| Bold | Ctrl+B  | Ctrl+F |

Is this good or bad? Mostly good I would say. For the average Danish user it makes sence to use Ctrl+F, Ctrl+K and Ctrl+U to either make some text **bold (fed)**, *italic (kursiv)* or *underlined (understreget)*. But for a techie user like me that likes pure English GUI’s this is a huge annoyance. When working on a Danish Windows I find my self pressing Ctrl+F to open the Find-dialog all the time. It’s a constant topic for debate among my fellow developers. Usually we just blame Microsoft with phrases like “Why don’t they just make software that works the way we would expect it to?” or “Why would anybody wanna change the way the shortcuts work - I’m used to…” etc. etc…

But for once I actually agree with Microsoft. The majority of their Danish users uses only the Danish version of Windows and has never tried anything else. So they of cause expect the keyboard shortcuts to comply with the Danish language. Microsoft should instead provide the experienced users with a setting where the user can choose which Windows language the default Windows keyboard shortcuts should comply to. The experienced user - being experienced - should not need much guidance to find and change this setting as they saw fit.

Other software could then if they as well had different keyboard shortcuts for different language versions check this system property and act accordingly. An obvious example would be that the Microsoft Office Suite would comply to whatever this setting was set to.
