---
title: "Blog Usability: Avoid Spam Comments"
date: "2006-06-24T23:58:49"
slug: "blog-usability-avoid-spam-comments"
url: "/2006/06/24/blog-usability-avoid-spam-comments/"
wp_id: 325
categories: ["Accessibility", "Blogging", "justaddwater.dk", "Usability", "WordPress"]
tags: []
author: "jesper"
technorati: ["blog", "usability", "spam", "comments", "akismet", "bbcode", "dom scripting", "javascript", "captcha"]
---

Since yesterday, the volume of spam comments has gone up even more. Now we get 150 spam comments every 12 hours. ([Yesterday it was 21 hours](/2006/06/23/spam-comments-just-got-worse/ "Justaddwater.dk: Spam comments just got worse")). I promised to tell about what countermeasures we have taken against spam comments.

What has that to do with usability? Well, in my opinion, irrelevant comments removes focus from the relevant content on the page, and makes your article less useful because of the irrelevant content.

In the last 8 months we had 348 real comments out of 6517 (with the 6,169 being spam comments we removed). Imagine what this blog would be like with 95% spam comments: Each relevant comment buried in 20 spam comments.

In my opinion, spam comments in that amount makes all comments unusable. Currently we're only using two countermeasures to avoid spam:

## What we have done

### 1. Use Akismet for wordpress

[Akismet](http://akismet.com/ "Akismet home page") is a plugin for the blog software justaddwater.dk runs on. The plugin checks all comments and trackbacks collaboratively on a lot of blogs. If the comment is already known as spam, it's never published. Here's what other people are saying about it:

> Before Akismet I was spending more time deleting spam than creating content. Now I can focus on actually blogging!
>
> — [Sarah King](http://sarahk.pcpropertymanager.com/blog/)
>
> I think Akismet is the best automated spam killer that actually gets better as it learns from the whole community marking new spam comments as spam. It just WORKS.
>
> — [Vinny Carpenter](http://www.j2eegeek.com/blog/)

As i mentioned yesterday, an occational spam comment slips through the Akismet filter. Then we mark it as spam, and this way Akismet learns from us so that other users can benefit from this.

### 2. Make a spam filter against BBCode like "\[/url\]"

We noticed recently that almost all of the comments that slipped through Akismet contained weird formed codes like:

> \[url=spam.domain.com\]Spam comment\[/url\]

This has been noted by many other bloggers including [Sam Ruby](http://www.intertwingly.net/blog/2006/05/30/Captcha-this "Sam Ruby: Captcha this") (via [Jeremy Voorhis](http://www.jvoorhis.com/articles/2006/06/09/open-discussion-fighting-spam-in-the-new-world#comments "Jeremy Voorhis: Open Discussion: Fighting Spam in the New World")) and [Mike Haugland](http://haugland.ca/notebook/316/ "Mike Haugland: Comment Spam"). To avoid this we've added another filter that holds comment for moderation if it contains \[/url\]. We put that into the "comment moderation" field as seen on the screenshot below:\
[![Wordpress spam settings](/wp-content/uploads/2006/06/screenshot-wordpress-spam-settings.png)](/2006/06/24/blog-usability-avoid-spam-comments/wordpress-spam-settings/ "Wordpress spam settings")\
This is the two things, we've done and it's caught all our spam comments the last days.

## What we might do

We feel it's not necessary at the moment but at some point that'll obviously not be enough. So we might do the following:

### Remove standard URLs for posting comments

Recently, Thomas and I met with François Nonnenmacher, a French Capgemini employee blogging at [padawan.info](http://padawan.info). He told that he had been very successful by renaming the files that receive comments — in our case `wp-comments-post.php`` `. From his webserver log he saw that many spam comments still hit on the standard comment file names.

### Encode forms with JavaScript

[Thomas Baekdal](http://www.baekdal.com/ "Baekdal.com") recommended this trick in a [comment yesterday](/2006/06/23/spam-comments-just-got-worse/#comment-6171 "Comment on justaddwater.dk: Spam comments just got worse"): Remove the comment form in the HTML source code and replace it with JavaScript that generates the same HTML. Can be done with online tools like [http://automaticlabs.com/products/enkoderform](http://automaticlabs.com/products/enkoderform).

A variation of this would be to use DOM scripting to change the URL the form posts to via JavaScript. Example:

``` html
<form id="postform" method="post" action="illegal.url">
```

And then via DOM scripting change form.action to the proper URL (`wp-comments-post.php`).

``` javascript
var obj = document.getElementById('postform')

if(obj)

obj.action = "wp-comments-post.php"
```

### Moderate all comments before publishing

It's also likely that we might toggle that setting in Wordpress, to moderate all comments before they're published. It's of course a disadvantage to our readers that they can't read what other people are saying until we approve it. But we might toggle this setting if it's necessary and comment spam gets out of our hands.

## What we won't do

### Captcha

A non-machine readable image or similar. We probably won't use that, because most implementations have accessibility issues to disabled users. See our ealier "[Captcha usability revisited: Google inaccessible to blind people](/2006/01/30/captcha-usability-revisited-google-inaccessible-to-blind-people/ "Permanent Link to Captcha usability revisited: Google inaccessible to blind people")"

## More info:

- Wordpress article: [Combating Comment Spam](http://codex.wordpress.org/Combating_Comment_Spam)
- Six Apart [guide to comment spam](http://www.sixapart.com/pronet/comment_spam "Six Apart: Six Apart guide to comment spam")
- [WeblogToolsCollection - WordPress comment spam stoppage techniques](http://weblogtoolscollection.com/archives/2004/09/15/wordpress-comment-spam-stoppage-techniques/ "http://weblogtoolscollection.com/archives/2004/09/15/wordpress-comment-spam-stoppage-techniques/")
