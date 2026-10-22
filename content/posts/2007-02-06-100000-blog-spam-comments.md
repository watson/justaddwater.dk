---
title: "100,000 Blog Spam Comments"
date: "2007-02-06T12:44:47"
slug: "100000-blog-spam-comments"
url: "/2007/02/06/100000-blog-spam-comments/"
wp_id: 531
categories: ["Blogging", "justaddwater.dk", "spam", "Usability", "WordPress"]
tags: []
author: "thomas"
technorati: ["WordPress", "Apache", "httpd", "htaccess", "filter", "spam", "blogging", "Akismet", "usability", "comments", "trackbacks", "justaddwater.dk"]
---

**Today justaddwater.dk got spam comment number 100,000.** But actually the real number is much higher since we have incorporated a couple of measures to catch the spam even before it reaches WordPress or [Akismet](http://akismet.com/ "Tool for stopping comment and trackback spam").

![Akisment Caught Spam Comments on justaddwater.dk](/wp-content/uploads/2007/02/jaw-caught-spam-2007-02-06.png)

We have for example been [blocking certain keywords](/2006/06/24/blog-usability-avoid-spam-comments/ "justaddwater.dk - Blog Usability: Avoid Spam Comments") that we found where common in spam that slipped through Akismet, or we have been [changing the standard WordPress URL for posting comments](/2006/06/28/blog-usability-avoid-spam-comments-part-2/ "justaddwater.dk - Blog Usability: Avoid Spam Comments (Part 2)"). Finally we have incorporated a little htaccess hack that validates the posters referral URL. This should of cause be our own domain justaddwater.dk, but many spammers actually put some garbage into this header field - and we can then easily block it directly in the Apache web server before it even reaches WordPress. <ins>UPDATE: We also allow empty referrals (thanks Håvard, for pointing this out)</ins>

8 months ago we had over a period of also 8 months received 6,517 comments totally. Of them only 348 where legit comments! Since then we have received approximately 100,800 comments. 389 where new legit comments and 7,317 was caught in the htaccess filter we applied in July 2006. **This translates to 99.6% spam comments.**
