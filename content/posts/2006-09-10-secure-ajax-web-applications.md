---
title: "Secure AJAX Web Applications"
date: "2006-09-10T21:49:02"
slug: "secure-ajax-web-applications"
url: "/2006/09/10/secure-ajax-web-applications/"
wp_id: 386
categories: ["AJAX", "Security", "Web Development"]
tags: []
---

Scott Dietzen of Zimbra posted a decent article about [security issues in AJAX web applications](http://www.zimbra.com/blog/archives/2006/09/securing_ajax.html "Zimbra blog: Securing Ajax").

> **Ajax security considerations.** Subject to the additional precautions enumerated below, Ajax applications can be made as highly-secure as the web technologies upon which the Ajax model is based.

The article mentions several issues and Scott has put some thoughts in how to secure their enterprise Outlook replacement, Zimbra.

- \
- Use SSL/TLS (i.e., HTTPS)
  \
- No server-side interpretation of JavaScript or other client-submitted code
  \
- Limited or no client-side interpretation of JavaScript within user data
  \
- RESTful URLs: No HTTP GET requests modify data (only POST or PUT requests)
  

[Zimbra blog: Securing Ajax](http://www.zimbra.com/blog/archives/2006/09/securing_ajax.html "Zimbra blog: Securing Ajax").
