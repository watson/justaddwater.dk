---
title: "Setting Up Subversion Externals With TortoiseSVN"
date: "2007-10-23T09:23:03"
slug: "setting-up-subversion-externals-with-tortoisesvn"
url: "/2007/10/23/setting-up-subversion-externals-with-tortoisesvn/"
wp_id: 750
categories: ["Web Development"]
tags: []
---

Just a tip I spent some time on figuring out: Found information today on how to use TortoiseSVN to manage svn:externals. I'm working on a big project where we need many different branches and parts to use the same css and images libraries throughout all subprojects.

I had to Google to get the information on how to set it up Here is how to do it with TortoiseSVN (i'm using windows XP):

1.  Right click on the project folder. Select "TortoiseSVN"\>"Properties" ![tortoisesvn-properties.png](/wp-content/uploads/2007/10/tortoisesvn-properties.png)
2.  Now add the property to the dialog. Press add and fill in the following: Property name: "svn:externals" css http://project_name/master/css images http://project_name/master/images ![tortoisesvn-properties-add-svn-externals.png](/wp-content/uploads/2007/10/tortoisesvn-properties-add-svn-externals.png) Any number of spaces will do between folder name and url. Remember line break between each project folder that needs to be checked out here.
3.  Press OK in both dialogs. The properties are now set. ![tortoisesvn-properties-svn-externals-added.png](/wp-content/uploads/2007/10/tortoisesvn-properties-svn-externals-added.png)
4.  On next "svn update", the external folders will be added and continuously updated.

Originally I wanted to do this for quite some time ago, and found info on how to do it with "svn propedit". For some strange reason, it fails (can't open external editor from command line).

More info: SVN book [section on svn:external](http://svnbook.red-bean.com/en/1.0/ch07s02.html#svn-ch-7-sect-2.3.6)
