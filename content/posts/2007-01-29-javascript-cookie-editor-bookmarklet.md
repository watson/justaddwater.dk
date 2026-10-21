---
title: "Handy JavaScript Cookie Editor"
date: "2007-01-29T23:50:49"
slug: "javascript-cookie-editor-bookmarklet"
url: "/2007/01/29/javascript-cookie-editor-bookmarklet/"
wp_id: 523
categories: ["Code", "JavaScript", "justaddwater.dk"]
tags: []
author: "jesper"
technorati: ["javascript", "bookmarklet", "favelet", "cookie editor", "cookies", "editor", "cookie"]
---

2 years ago I wrote a small javascript to view, edit and delete cookies.

The really cool thing about this user interface is the **inline editing of cookie names and values**. I really like the principle that you hover the value that you inspect, can see that it's editable. Then click directly and the text is converted to a text field that is automatically saved when you leave the field.

Andrei from New York wrote me and reminded me the handy little cookie editor, so after making some minor modifications, I decided to republish it.

Well, actually, I've spent some hours getting more and more puzzled on some bugs and limitations in the code.

I won't hesitate anymore, but rather give you the tool including some known issues. Please feel free to make suggestions or fix.

### Known issues:

All cookies set with the tool expires end-of-session. This could be easily fixed, but I'd like to implement it in a way so that it works elegantly and simple in the user interface.

Cookies with domain set differently cannot be edited or deleted. This is a problem on many big portal sites. For instance, all cookies on Yahoo! are set for `.yahoo.com`. But the front-page is located at `www.yahoo.com` (the www subdomain of yahoo.com), which means that my tool is not allowed to edit or remove the cookie.

**Goto next page and bookmark this link in your browser: [cookie editor page with bookmarklet](/wp-content/uploads/2007/01/cookieeditor.html "cookieeditor.html").**
