---
title: "Multiple versions of IE in one Windows PC - Prepare for IE7"
date: "2006-01-25T14:29:29"
slug: "multiple-versions-of-ie-in-one-windows-pc-prepare-for-ie7"
url: "/2006/01/25/multiple-versions-of-ie-in-one-windows-pc-prepare-for-ie7/"
wp_id: 109
categories: ["Browser"]
tags: []
---

**Update 2006-09-28: [All IE Browsers Standalone On Same PC](/2006/09/28/all-ie-browsers-standalone-on-same-pc/ "Justaddwater.dk: All IE Browsers Standalone On Same PC") (September 28, 2006) solves the problem.**

**UPDATE 2006-02-03: The method described below will sometimes not work. To run IE7 and IE6 side-by-side, see the new post "[IE7 beta running side by side with IE6](/2006/02/03/ie7-beta-running-side-by-side-with-ie6/ "Justaddwater.dk: IE7 beta running side by side with IE6")". For older versions of IE, this still works and you could safely continue as described below**, (but you should acknowledge that this is still "unsupported", and is likely to make Internet Explorer less stable).

For some time I've used a trick from Quirksmode.org (Peter Paul Koch) to test webpages with different versions if Microsoft Internet Explorer (IE) on the same machine. This trick can come in handy if you want to run usability tests with old versions of IE.

How would you test a webpage in IE 6 when IE 7 is released? Here's a simple way that does not require multiple machines or complicated setups of multiple operating systems.

Usually IE upgrades and removes the old version of the browser. This is OK for most web users, but when I test and develop pages, its often convenient to have an old IE version available.

The method has been known for quite some years, and today I found information on how to transform Internet Explorer 6 to a standalone version. In that way, you're prepared when IE7 is released.\
The following is a [comment from IE blog](http://blogs.msdn.com/ie/archive/2006/01/23/516393.aspx#516872 "IE blog: comment on how to run IE 6 as a standalone application") (comment by [NocturnDragon](http://blogs.msdn.com/utility/Redirect.aspx?U=http%3a%2f%2fwww.nocturndragon.net "NocturnDragon")):

> \
>
> Make IE6 standalone and then upgrade to IE7 when you'll get it.you just need to copy this files to a folder of your choice (almost all of them are in the system32 folder)browseui.dll\
> dispex.dll\
> iexplore.exe\
> inetcpl.cpl\
> jscript.dll\
> mshtml.dll\
> mshtml.tlb\
> shdocvw.dll\
> urlmon.dll\
> vbscript.dll\
> xpsp2res.dlland do not forget to create a empty file inside that folder called: iexplore.exe.localI wonder why MS is so reluctant to let you do this with a simple checkbox during the install!I've been running IE5.0, IE5.5 and IE6.0 standalone for some time now. That's the simplest way to test your webpages on all of them.
>
> 

Just for the record, here is a reference to [Peter Paul Koch's original article](http://www.quirksmode.org/browsers/multipleie.html "Quirksmode.org: Browsers - multiple Explorers"), which I'm confident that he'll update when IE7 is released.

> A solution [has been found](http://www.insert-title.com/web_design/?page=articles/dev/multi_IE) however, by web developer Joe Maddalone who deserves eternal fame. Read his page for the technical details.
>
> Web developer Ryan Parman [made the customized browsers files available](http://www.skyzyx.com/archives/000094.php) on his site. I copied them to my server to make sure this valuable resource doesn't disappear. Subsequently I found similarly doctored Explorer 3 and 4 versions on [nachtarchiv.de](http://www.nachtarchiv.de/Webdesign.html?reportage=25).
>
> Here's how it works:\
>
> 1.  \
> 2.  Start with a Windows XP box with Explorer 6 installed on it. I have heard, but not tested, that this will also work on Windows 2000.
>     \
> 3.  Download the browsers of your choice:\
>     - \
>     - [Explorer 3](http://www.quirksmode.org/browsers/IE30.zip) (828K)
>       \
>     - [Explorer 4](http://www.quirksmode.org/browsers/IE4.zip) (2417K)
>       \
>     - [Explorer 5.01](http://www.quirksmode.org/browsers/ie501sp2_nt.zip) (3004K)
>       \
>     - [Explorer 5.5 sp2](http://www.quirksmode.org/browsers/ie55sp2_nt.zip) (3597K)
>       \
>
>     \
>     \
> 4.  Unzip the zip files and put them somewhere in a directory.
>     \
> 5.  To run the browsers, execute the `IEXPLORE.EXE` files in each directory. This works. Nonetheless, keeping the versions apart is not simple.
>     \
> 6.  I verified that this were in fact working copies of 5.01 and 5.5 by some simple CSS tests you can do right here on this site. See below.
>     \
> 7.  Nonetheless you'll find problems. The Help -\> Info screen, for instance, always shows the Explorer 6.0 version number, even though the image above it says "Explorer 4" in 4.0, "Explorer 5" in 5.0, but "Explorer 6.0" in 5.5.
>     \
> 8.  The user agent string seems to work fine, though. To help you keep these versions apart I wrote a simple [script](http://www.quirksmode.org/js/keepieapart.html) that precedes the document title by the IE version.
>     \
>
> 

I've been using this trick on several occations, and even on Windows XP it introduces some stability problems in Internet Explorer.

- \
- It sometimes crash when you choose bookmarks.
  \
- It also shows IE6 information in the "about" box in all the installed versions
  \
- Internet Explorer 4 address bar does not work (instead press CTRL+L to load a page)
  

Decide for your self if you can use this trick. I can live with the crashes becaus it has a huge advantage for me that I can test HTML and CSS early in the development.
