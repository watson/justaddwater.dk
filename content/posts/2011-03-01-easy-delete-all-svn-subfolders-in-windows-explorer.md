---
title: "Easy delete all .svn Subfolders in Windows Explorer"
date: "2011-03-01T11:08:51"
slug: "easy-delete-all-svn-subfolders-in-windows-explorer"
url: "/2011/03/01/easy-delete-all-svn-subfolders-in-windows-explorer/"
wp_id: 1414
categories: ["justaddwater.dk"]
tags: ["subversion", "svn", "Web Development", "windows"]
author: "jesper"
---

I had to repair a flawed Subversion repository recently (not all files were committed). I had my local repository checked out. This was the flawed part, containing only parts of the folders and files it should.

Then, I got a zip file from the machine where it was working. Problem: It contained .svn folders from the other developer. So to merge these i did the following workflow:

1.  Delete all .svn folders from other developer's zip
2.  Move other developers folder over on top of my local install.
3.  Commit all missing files

Of course this will only work if there are no .svn folders in other developer's file, because then svn authentication, paths, etc. will be messed up, and commit will fail.

Luckily, Sanil S (IamTechie blog) wrote a nice little script that actually adds a context menu in Windows explorer:\
[![](/wp-content/uploads/2011/03/delete-svn.jpg "delete-svn")](/wp-content/uploads/2011/03/delete-svn.jpg)

*delete_svn_subfolders.reg — [gist on GitHub](https://gist.github.com/848907)*

``` ini
Windows Registry Editor Version 5.00
;
; Running this file will give you an extra context menu item in Windows Explorer
; "Delete SVN folders"
;
; For the selected folder, it will remove all subfolders named ".svn" and their content
; Tip from http://www.iamatechie.com/remove-all-svn-folders-in-windows-xp-vista/
;
; Enrichened with comments by Jesper Rønn-Jensen ( http://justaddwater.dk/ )
;
;
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN]
@="Delete SVN Folders"
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN\command]
@="cmd.exe /c \"TITLE Removing SVN Folders in %1 && FOR /r \"%1\" %%f IN (.svn) DO RD /s /q \"%%f\" \""
```

Just save this file as "delete_svn_subfolders.reg". When you run it, then you will have the new windows explorer context menu item shown in the image.

The full script (repeated for the ones with javascript disabled:)

```
Windows Registry Editor Version 5.00
;
; Running this file will give you an extra context menu item in Windows Explorer
; "Delete SVN folders"
;
; For the selected folder, it will remove all subfolders named ".svn" and their content
; Tip from http://www.iamatechie.com/remove-all-svn-folders-in-windows-xp-vista/
;
; Enrichened with comments by Jesper Rønn-Jensen ( http://justaddwater.dk/ )
;
;
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN]
@="Delete SVN Folders"
[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Folder\shell\DeleteSVN\command]
@="cmd.exe /c \"TITLE Removing SVN Folders in %1 && FOR /r \"%1\" %%f IN (.svn) DO RD /s /q \"%%f\" \""
```

More info:

IamTechie: [How to remove all “.svn” folders in Windows XP & Vista?](http://www.iamatechie.com/remove-all-svn-folders-in-windows-xp-vista/)
