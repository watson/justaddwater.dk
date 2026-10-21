---
title: "Blog Usability: Spam Comments Irritate Subscribers"
date: "2007-07-10T14:16:26"
slug: "blog-usability-spam-comments-irritate-subscribers"
url: "/2007/07/10/blog-usability-spam-comments-irritate-subscribers/"
wp_id: 676
categories: ["Blogging", "justaddwater.dk", "spam", "WordPress"]
tags: []
---

I am back from vacation and saw that Akismet has caught more than 22,000 spam comments over a two week period. That is roughly one spam comment every minute (65 comments each hour). Since February when we passed 100,000 spam comments, we have now passed a quarter million spam comments. (277,421 when I made the screenshot below).

The number of daily spam comments has grown more than 400% over the last year.

![justaddwater-akismet-277421-spam-comments.png](/wp-content/uploads/2007/07/justaddwater-akismet-277421-spam-comments.png)

Though Thomas and I are thrilled with how well Akismet works, there are still one serious issue: Every day somewhere between 1 and 10 spam comments slip through. It's not a big deal for us, as we usually remove them within minutes if they slip though.

### Spam comments annoy subscribers

However, the comments that slip through actually annoys the most loyal readers. Our readers can subscribe to new comments on any article, and the spam that slips through actually generates an email to all subscribers.

![justaddwater-comment-subscription.png](/wp-content/uploads/2007/07/justaddwater-comment-subscription.png)

Furthermore, any spam comments slipping through Akismet will occur in the [comment feeds](http://feeds.justaddwater.dk/jaw/comments).

I feel really sorry for the subscribers because a subscription then eventually generates an email, and even though we remove the spam comments fast, people still gets irritating, irrelevant spam sent by us to the subscribers. And we really hate that.

I think that this problem is more widespread than it seems, as I myself have recieved some emails from blog articles I'm subscribing to:

[![justaddwater-comment-spam-example-email.png](/wp-content/uploads/2007/07/justaddwater-comment-spam-example-email-thumbnail.png)](/wp-content/uploads/2007/07/justaddwater-comment-spam-example-email.png "justaddwater-comment-spam-example-email.png")

As a consequence, Thomas and I will now look for ways to tightening things further than Akismet can do.

## Possible solutions


### Moderate all comments

We have previously talked about holding back all comments for moderation (or at least comments from unknown email adresses). This is very easy to do — just flip a switch in a Wordpress administration module. One disadvantage with this solution: It adds a time-delay to the blog, and we feel that a blog should be immediate, and a discussion should take place without us acting as gatekeepers for the discussion.

### Improve Akismet

We are not in a position to change or improve Akismet directly, but here is a suggestion: Comments should be evaluated better and not just based on if anybody else has marked a comment to spam. It would be cool if Akismet could sometimes "be in doubt" about a comment. What if Akismet could tell Wordpress to hold a comment for moderation if it was likely to be spam. For example some of the comments that slipped though the last month had a Russian or Polish email address or www.yahoo.com as homepage. Some others contained the word casinos, which is a very unlikely word to use on this blog. This is of course not true to any blog, so it would be great marking this as "I'm not sure. please moderate for me".

This suggestion is probably based on my lack of knowledge on how Akismet really works. But it would of course be ideal to add rules to Akismet in order to improve the program.

### Adding a bot-filter in the comment form

We talked about adding one or more form fields and hide them via css, to not disturb screen readers. Then name the field something innocent test that the field is blank when recieved. If not blank, then it is likely that a robot has filled out the field. Not a human, because the field is hidden.

This probably requires some work as we have to try out possibilities for confusing spam bots and see what works and whatnot. There are probably also some disadvantages for people browsing without CSS.

Actually we have already done some work including [renaming the wordpress standard form](/2006/06/24/blog-usability-avoid-spam-comments/). That worked great at the time, but after 6 months or so, it did not really reduce the spam (we could actually see that in the error log).

### Our preliminary conclusion

Eventually we will probably turn on comment moderation, as it is the only 100% guarantee that spam comments don't slip through to our subscribers and loyal readers. Before we do that (and to avoid the time-delay drawbacks), we will experiment on making a better bot-filter in the comment form.

More info

- \
- Justaddwater.dk: [100,000 Blog Spam Comments](/2007/02/06/100000-blog-spam-comments/ "Permanent Link: 100,000 Blog Spam Comments"), February 6, 2007
  \
- Justaddwater.dk: [Blog Usability: Avoid Spam Comments (Part 2)](/2006/06/28/blog-usability-avoid-spam-comments-part-2/ "Permanent Link: Blog Usability: Avoid Spam Comments (Part 2)"), June 2006
  \
- Justaddwater.dk: [Blog Usability: Avoid Spam Comments](/2006/06/24/blog-usability-avoid-spam-comments/ "Permanent Link: Blog Usability: Avoid Spam Comments"), June 2006
  

PS. We have previously claimed that we [won't use CAPTCHAs](/2006/06/28/blog-usability-avoid-spam-comments-part-2/#comment-7617) or [encode comment form with JavaScript](/2006/06/24/blog-usability-avoid-spam-comments/#comment-7654), and for now, we will stand by that decision, in order to avoid usability and accessibility issues.
