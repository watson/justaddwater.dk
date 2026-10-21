---
title: "Windows SVN pre-commit-hook"
date: "2010-06-10T09:23:32"
slug: "windows-svn-pre-commit-hook"
url: "/2010/06/10/windows-svn-pre-commit-hook/"
wp_id: 1354
categories: ["Code"]
tags: ["Code", "subversion", "svn", "windows"]
---

At a current project I work on, we use a Windows server to run our subversion repository.

I wanted to set up the pre-commit hook so that commits with empty comment are automatically rejected.

All commit-hook example files that go with Subversion are written in bash (as unix servers tend to be the normal).

Here is a the pre-commit hook rewritten as a windows .bat file.

*pre-commit.bat — [gist on GitHub](https://gist.github.com/432704)*

``` bat
REM Subversion pre-commit hook for Windows machine
REM put this in your SVN repository folder /hooks/pre-commit.bat
REM we use it with svn version 
REM http://stackoverflow.com/questions/869248/windows-pre-commit-hook-for-comment-length-subversion

@echo off  
:: Stops commits that have empty log messages.        
@echo off  

setlocal  

rem Subversion sends through the path to the repository and transaction id  
set REPOS=%1  
set TXN=%2           

rem line below ensures at least one character ".", 5 characters require change to "....."
svnlook log %REPOS% -t %TXN% | findstr . > nul  
if %errorlevel% gtr 0 (goto err) else exit 0  

:err  
echo. 1>&2  
echo Your commit has been blocked because you didn't enter a comment. 1>&2  
echo Write a log message describing the changes made and try again. 1>&2
echo Thanks 1>&2
exit 1
```
