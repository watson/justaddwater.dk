---
title: "IE7 beta running side by side with IE6"
date: "2006-02-03T21:05:31"
slug: "ie7-beta-running-side-by-side-with-ie6"
url: "/2006/02/03/ie7-beta-running-side-by-side-with-ie6/"
wp_id: 131
categories: ["Browser"]
tags: []
---

**Update: [All IE Browsers Standalone On Same PC](/2006/09/28/all-ie-browsers-standalone-on-same-pc/ "Justaddwater.dk: All IE Browsers Standalone On Same PC") (September 28, 2006) solves the problem.**

In the comments of "[Multiple versions of IE in one Windows PC](/2006/01/25/multiple-versions-of-ie-in-one-windows-pc-prepare-for-ie7/ "Justaddwater.dk: Multiple versions of IE in one Windows PC - Prepare for IE7")" I could see that other people also had problems with the suggestion to make IE6 standalone.

Jon Galloway has the solution: Run IE7 as standalone and keep IE6 as the default browser. I have tried it out for a couple of days and could not get it to work until he posted a followup, [IE7 Standalone Launch Script](http://weblogs.asp.net/jgalloway/archive/2005/12/28/434132.aspx "Jon Galloway: IE7 Standalone Launch Script"):

> **How to use the IE7 Launch Script**:\
>
> 1.  \
> 2.  If you already have IE7 set up for standalone mode, skip to step 4.
>     \
> 3.  Download the [IE7 Beta Install from MSDN](http://www.microsoft.com/windows/ie/ie7/ie7betaredirect.mspx "Microsoft.com: Download Internet Explorer 7 beta"). \[...\]
>     \
> 4.  Open the install file with a decompression program like [WinRAR](http://www.rarlab.com/download.htm) (yep, it's an EXE, but it's a self extracting EXE) and extract them to a folder. \[...\]
>     \
> 5.  Copy the text below to notepad and save it as **IE7.bat** in the same folder you're setting up the standalone IE7 copy.
>     \
> 6.  When you want to run IE7, double click **IE7.bat** - it pops up a DOS window that will hang around as long as IE7 is running so it can clean up after it (by deleting that pesky registry key) when you close IE7. Don't close the DOS window down or your pancreas will implode.
>     \
> 7.  When you're done with IE7, just shut it down. The DOS window will clean up that pesky registry key and delete the standalone files, then disappear. If you shut IE7 down and the DOS window hangs around, just close it and run it again.
>     \
>
> 

Here is the script that should be saved as IE7.bat:

> @ECHO OFF\
> TITLE IE7 Launcher 1.3
>
> ECHO IE7 STANDALONE LAUNCHER 1.3\
> ECHO Updated for IE7 Beta 2 Preview - 2/2/2006\
> ECHO.\
> ECHO Do not close this window or it will not clean up after itself properly.\
> ECHO You can pass a URL into this batch file, like this:\
> ECHO ie7.bat www.microsoft.com\
> ECHO More info here: http://blogs.msdn.com/ie/archive/2005/12/16/504864.aspx\
> ECHO.\
> ECHO When you close IE7, this will remove the registry key and shut itself down.\
> ECHO.\
> ECHO Setting up IE7 for standalone mode...\
> PUSHD %~dp0
>
> ECHO Removing IE7 registry key.\
> \> %TEMP%.\IE7Fix.reg ECHO REGEDIT4\
> \>\>%TEMP%.\IE7Fix.reg ECHO.\
> \>\>%TEMP%.\IE7Fix.reg ECHO \[-HKEY_CLASSES_ROOT\CLSID\\{C90250F3-4D7D-4991-9B69-A5C5BC1C2AE6}\]\
> \>\>%TEMP%.\IE7Fix.reg ECHO \[-HKEY_CLASSES_ROOT\Interface\\{000214E5-0000-0000-C000-000000000046}\]\
> \>\>%TEMP%.\IE7Fix.reg ECHO.\
> :: Merge the REG file to delete the IE7 standalone entry\
> REGEDIT /S %TEMP%.\IE7Fix.reg
>
> REN SHLWAPI.DLL SHLWAPI.DLL.BAK\
> TYPE NUL \> IEXPLORE.exe.local\
> ECHO Running IE7...\
> iexplore.exe "%1"
>
> :: Merge the REG file to delete the IE7 standalone entry\
> REGEDIT /S %TEMP%.\IE7Fix.reg\
> :: Delete the temporary REG file\
> DEL %TEMP%.\IE7Fix.reg
>
> ECHO Removing IE7 standalone files...\
> REN SHLWAPI.DLL.BAK SHLWAPI.DLL\
> DEL IEXPLORE.exe.local\
> POPD\
> ECHO Complete, closing...

**One problem** with this: If I start IE6 before IE7, I cannot use the address bar in IE6 (as this loads the page in Firefox which is my default browser). The workaround for me is to start IE7, and then start IE6. Now I can see a web page in IE7 and IE6 side-by side.

I'm really glad Jon updated the script. The previous script worked with IE7 beta 1, but with beta 2 it could only run once once, then it would not work for me. Eli on [Jon Galloway's comment page](http://weblogs.asp.net/jgalloway/archive/2005/12/28/434132.aspx#436422) has exacly the same problem.

So, if you want to install IE7 and keep a working version of IE6, then I could only recommend the Jon Galloway method described above. He has an updated article: [Runing IE7 Beta 2 Preview next to IE6 (the right way).](http://weblogs.asp.net/jgalloway/archive/2006/02/02/437196.aspx)
