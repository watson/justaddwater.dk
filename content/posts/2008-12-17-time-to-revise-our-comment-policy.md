---
title: "Time To Revise Our Comment Policy"
date: "2008-12-17T00:10:35"
slug: "time-to-revise-our-comment-policy"
url: "/2008/12/17/time-to-revise-our-comment-policy/"
wp_id: 982
categories: ["justaddwater.dk"]
tags: []
author: "jesper"
---

Our experiment [Spam Filter Free Day](/2007/12/15/today-is-spam-filter-free-day/) had one year anniversary yesterday. We won't repeat the experiment as it gave us a tremendous amount of comments to administer.

Since then we decided to remove the "nofollow" constraint on all comment links. At that time we wanted to give credit to our friends and other people that put effort in posting comments on our site.

Removing nofollow would result in higher search ranking for the webpages of our active community. We wanted to reward and encourage comments that way.

## The drawback of removing "nofollow"

Recently, justaddwater.dk has been added to spammers' search engines -- for instance the "[Search DoFollow](http://www.dofollow.radpixels.com/)" search engine where "you can find relevant posts where your comment will earn you a backlink". We also appeared on discussion forums like [here](http://forums.digitalpoint.com/showthread.php?t=864579) and [here](http://forums.digitalpoint.com/showthread.php?p=9666008).

The result is that we get many comments from people that are more interested in adding a link to their site than adding positively to the discussion. As a consequence, the article from last year ([Spam Filter Free Day](/2007/12/15/today-is-spam-filter-free-day/)) is totally bloated with comments. And you see only the comments that are actually approved. The majority of comments are still caught by our spam comment guards (akismet, and other comment filters).

Many of the comments are apparently not automated and address a specific thing in the actual blog post. But what should we do with the following situations:

### A: Author name and URL is a product name

The most common situation we see is like this:\
[![](/wp-content/uploads/2008/12/comment-spam-name-and-url.png "comment-spam-name-and-url")](/wp-content/uploads/2008/12/comment-spam-name-and-url.png)\
Until now, we have manually assessed the content of each of these. If it's relevant for the blog post, we have been approving it.

### B: Author name seems personal but URL is a product name

A seemingly valid name but apparently the URL points on a product (or may be a site that sells a product). Example:\
[![](/wp-content/uploads/2008/12/comment-spam-valid-name-product-url.png "comment-spam-valid-name-product-url")](/wp-content/uploads/2008/12/comment-spam-valid-name-product-url.png)

This type of comments have been approved if we decided the content to be valid. In this case it's actually an invalid comment as the CSS is included inside the example file. But I approved the comment as the author may not have known that.

### C: Author has a gravatar but URL is a product name

In rare cases, people post a comment where there is a valid gravatar but something smells about the URL. Example:\
[![](/wp-content/uploads/2008/12/comment-spam-valid-gravatar.png "comment-spam-valid-gravatar")](/wp-content/uploads/2008/12/comment-spam-valid-gravatar.png)\
This type of comments have been marked as spam if the content was not adding any real value.

### D: A personal gravatar but name is a product name

We have very rarely seen people that use a product name instead of their actual name. Example:\
[![](/wp-content/uploads/2008/12/comment-spam-valid-gravatar-invalid-name.png "comment-spam-valid-gravatar-invalid-name")](/wp-content/uploads/2008/12/comment-spam-valid-gravatar-invalid-name.png)\
In this case, Taylor Thompson would be better off by using his real name. He obviously put effort into commenting. In this case we have previously approved comments.

### E: Comments in other languages

To my surprise we see a lot of comments in Russian and Turkish. Our target group will not understand this, so we assume per default it's spam. Trackbacks could be valid here but we also assess these individually (and approve most trackbacks).

## New comment policy

In the future we will probably **mark all of the above comment types as spam**. Yes, some of the comments actually add value, but most of the comments actually are just made to improve ranking.

**We will continue to manually approve** the comments we mean will add value.

**We will continue to hold comments for manual moderation**. (so if your valid comment does not show up within a few hours, please contact us).

## Strategy for making a valid comment on this blog

- Use your real name -- not a product or service name
- Use a gravatar (improves the likeliness that your comment won't drown when we moderate comments)
- Write your comment in English. (of course, trackbacks from your site in other languages are OK)
- If your site is about SEO or traffic optimization, we'll probably remove your comment, or your link.
- Write comments on topic (this is of course not new)

In general, expect us to mark more comments as spam.

Note to self: We should look more into setting up the "[Nofollow case by case"](http://www.fob-marketing.de/marketing-seo-blog/wordpress-nofollow-seo-plugin-nofollow-case-by-case.html) and "[Auto moderate comments](http://planetozh.com/blog/2005/02/wordpress-plugin-auto-moderate-comments/)" plugins...

**See also**

- [Blog Usability: Spam Comments Irritate Subscribers](/2007/07/10/blog-usability-spam-comments-irritate-subscribers/) (July 2007)
- [Today is Spam Filter Free Day](/2007/12/15/today-is-spam-filter-free-day/) (December 2007)
