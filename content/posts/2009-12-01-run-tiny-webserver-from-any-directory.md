---
title: "Run Tiny Webserver From Any Directory"
date: "2009-12-01T20:56:13"
slug: "run-tiny-webserver-from-any-directory"
url: "/2009/12/01/run-tiny-webserver-from-any-directory/"
wp_id: 1245
categories: ["Code"]
tags: []
---

There are alternatives to [Resolve Symlinks When Copying Files With Rsync .](../2009/10/15/resolve-symlinks-when-copying-files-with-rsync/ "Permanent Link to Resolve Symlinks When Copying Files With Rsync")

How about firing up a (tiny) webserver that starts up quickly. Yehuda Katz suggested this some years ago:

Just drop this file in any directory, run the script, and it serves the files. I use this frequently for instance when I need to browser test static files on different virtual machines. (I modified the script shebang to work on my Mac).

I prefer to use this server.rb script in stead of accessing the files from a shared folder from the virtual machine. It's faster to write the address for `http://172.16.244.1:2000/accordion.html` than for `\\.host\Shared Folders\jesper On My Mac\src\htmlguide\accordion.html` – and easier to remember.

Tip from Yehuda Katz' "[Webrick Anywhere](http://yehudakatz.com/2007/08/06/webrick-anywhere/)"
