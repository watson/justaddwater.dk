---
title: "Howto Create a Temporary Local Subversion Repository"
date: "2007-04-26T21:30:08"
slug: "howto-create-a-temporary-local-subversion-repository"
url: "/2007/04/26/howto-create-a-temporary-local-subversion-repository/"
wp_id: 600
categories: ["Code", "Productivity", "Prototyping", "Web Development"]
tags: []
---

UPDATE May 1st, 2007 (forgot the two final steps 8 and 9).

I've run into the situation a couple of times where I get started on a client's office, but due to delays and politics it takes time to get a proper versioning control server set up.

It turned out to be easy when I figured out the where to find the details on it. I'm running windows XP, don't know how this differs on other operating systems.

1.  \
2.  Install TortoiseSVN, find the latest .exe in the [binaries folder](http://subversion.tigris.org/servlets/ProjectDocumentList?folderID=91 "TortoiseSVN Download Windows Binaries")
    \
3.  In windows explorer find the root folder for where you want your repository (this should be different than where your code workspace is).
    \
4.  Create a new folder. In this example, I choose "\<code\>C:\svn-repo\<code\>"
    \
5.  In windows explorer, right click and select "TortoiseSVN" \> "Create repository here..."\
    ![svn-create-local-repository-with-subversion-tortoisesvn.png](/wp-content/uploads/2007/04/svn-create-local-repository-with-subversion-tortoisesvn.png)
    \
6.  Select "native filesystem (FSFS)"\
    [![svn-create-local-repository-native-filesystem.png](/wp-content/uploads/2007/04/svn-create-local-repository-native-filesystem.png)\
    ](/wp-content/uploads/2007/04/svn-create-local-repository-native-filesystem.png "Direct link to file")
    \
7.  Check in your code. Go to your workspace folder, right click it an select "TortoiseSVN" \> "Import..."\
    ![svn-import-workspace-folder-into-subversion.png](/wp-content/uploads/2007/04/svn-import-workspace-folder-into-subversion.png)
    \
8.  Now write the url of you file repository. In my case, "`file:///C:/svn-repo/projectname`"\
    ![svn-import-initial-commit-message.png](/wp-content/uploads/2007/04/svn-import-initial-commit-message.png)\
    Also remember to put in a commit message
    \
9.  UPDATE (forgot to write these very important steps below):\
    Now, delete your source files. You just comitted them to the repository. Don't worry, they will be back in a moment. (If you are the cautious type like me, you probably just move the files to somewhere else...)
    \
10. Now it's time to check out the files from subversion. Right click and choose "Check out..." in the context menu. Then select your repository, in my case "`file:///C:/svn-repo/projectname`". And you're done!
    

From now on, your code is versioned, and can later be ported to the real subversion repository (any comments on how this is done would be greatly appreciated). Now, you can commit changes, view and diff changes, merge and roll back. Just like you would do in a normal code repository.

## Advanced use

For user and access control it's possible to modify the config files in the subversion /conf directory. The files in `/svn-repo/conf/` has the info (although it's not very self-explanatory).

The repository is only set up for file access, so you will need to share your repository in order for more developers to use it.

A better (and slightly more complicated) strategy is to use Apache as a frontend webserver and set it up to serve your subversion repository via that. If you want details on that I suggest reading:

- \
- Svn.spears.at: [**Subversion** for **Windows** with **Apache** server HOWTO](http://svn.spears.at/)
  \
- Joe White: [Mere-Moments Guide to installing a Subversion server on Windows](http://excastle.com/blog/archive/2005/05/31/1048.aspx)
  

All in all, this can be a great benefit and speed things up in enterprise environments, where many chefs are involved in the most basic tasks. Please feel free to add your own advice and tips in the comments.
