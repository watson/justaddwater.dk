---
title: "Fixed Outlook 2003 Corruption after Power Blackout"
date: "2011-04-05T09:20:34"
slug: "fixed-outlook-2003-corruption-after-power"
url: "/2011/04/05/fixed-outlook-2003-corruption-after-power/"
wp_id: 1457
categories: ["E-mails"]
tags: ["outlook"]
author: "jesper"
---

The power disappeared at our office, and killed outlook 2003. Suddently I got this error:\
[![Outlook 2003: Cannot start Microsoft Outlook. Unable to open the Outlook window. The set of folders could not be opened.](/wp-content/uploads/2011/04/unable-to-start-outlook-unable-to-open-the-outlook-window-the-set-of-folders-could-not-be-opened-300x56.png "unable-to-start-outlook-unable-to-open-the-outlook-window--the-set-of-folders-could-not-be-opened")](/wp-content/uploads/2011/04/unable-to-start-outlook-unable-to-open-the-outlook-window-the-set-of-folders-could-not-be-opened.png)

> Cannot start Microsoft Outlook. Unable to open the Outlook window. The set of folders could not be opened.

I followed advice from a [forum thread, that recommended to run "outlook.exe /resetnavpane"](http://social.technet.microsoft.com/Forums/en/outlook/thread/a111e6d8-491f-449e-9b57-1b77f99e9aad), but with no luck.

Then, from the command line, i tried all relevant flags found on "[outlook tips: using command line](http://www.outlook-tips.net/howto/commandlines.htm)".

> \
> C:\Program Files\Microsoft Office\Office11\>outlook /resetnavpane
>
> C:\Program Files\Microsoft Office\Office11\>outlook /safe
>
> C:\Program Files\Microsoft Office\Office11\>outlook /resetfoldernames
>
> C:\Program Files\Microsoft Office\Office11\>outlook /resetfolders
>
> C:\Program Files\Microsoft Office\Office11\>outlook /cleanprofile

At the end it turned out, that none of the above worked.. Until I shut down Microsoft Communicator!

Now, this worked like a charm:

> \
> `C:\Program Files\Microsoft Office\Office11>outlook.exe /resetfolders`

Lesson learned: Remember to shut down Microsoft office communicator, before trying to repair outlook
