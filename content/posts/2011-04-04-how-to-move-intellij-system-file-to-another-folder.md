---
title: "How to move IntelliJ system file to another folder"
date: "2011-04-04T09:23:57"
slug: "how-to-move-intellij-system-file-to-another-folder"
url: "/2011/04/04/how-to-move-intellij-system-file-to-another-folder/"
wp_id: 1444
categories: ["Web Development"]
tags: ["editor", "ide", "intellij"]
---

For work, I use IntelliJ IDEA, when working in Java world. For my current client, there is a quota on my user directory, which means I have to move IDEA system files to another folders.

1.  \
2.  Locate the file `idea.properties` in your IntelliJ Idea\bin folder
    \
3.  Edit `idea.config.path`
    \
4.  Restart
    

I changed it from

`idea.config.path=${user.home}/.IntelliJIdea10/config`

to

`idea.config.path=${idea.home}/.IntelliJIdea10/config`

It is very easy to do, but it was hard for me to google the result.
