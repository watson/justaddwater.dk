---
title: "Letting Spam In For A Day Questions and Answers"
date: "2007-11-29T10:33:10"
slug: "letting-spam-in-for-a-day-questions-and-answers"
url: "/2007/11/29/letting-spam-in-for-a-day-questions-and-answers/"
wp_id: 790
categories: ["Blogging", "justaddwater.dk", "spam", "WordPress"]
tags: []
author: "jesper"
---

Note that our [spam experiment](/2007/11/27/announcement-spam-filter-free-day/) scheduled for December 15th got mentioned by the Akismet Blog, Blogherald, and many other blogs.

- Akismet Blog: [Letting Spam In For A Day](http://blog.akismet.com/2007/11/28/letting-spam-in-for-a-day/)
- Blogherald: [Will you turn off Akismet](http://www.blogherald.com/2007/11/29/wordpress-wednesday-news-will-you-turn-off-akismet-wordpress-24-delayed-and-more-wordpress-news/)?
- Follow along in Technorati blog reactions for Justaddwater.dk

Also to answer some of the comments we got:

> **[Binh Nguyen](http://binh.name/):**\
> How about a bigger challenge? Keep everything else active and shut down only the spam protection.

That's a big challenge. But we actually tried that recently when [Justaddwater.dk got hacked](/2007/11/15/justaddwaterdk-hacked/). The hacker used a security hole in an old version of Wordpress and to upload his malicious code, he disabled all plugins. I discovered that by discovering that Akismet (and all other plugins) was turned off.

> **[Olysses](http://ulyssesonline.com/):**\
> You are nuts. I might join you, but let me think about it. I don’t want to spend the whole day deleting spam. Maybe, a quick database backup and restore as if December 15 never happened. That might do the trick.

Thanks for the tip. That might be what we end up doing if the cleanup task will get too big.

> **[Thomas Baekdal](http://baekdal.com):**\
> I don’t understand why you don’t try to mask your comment form, or prevent the spammers from running their scripts.

Purely for accessibility reasons. We discussed that previously And Thomas Watson and I totally agree that it must be possible to fill in a valid comment without using JavaScript in the browser, cellphone, Iphone, whatever. We also discussed that with the previous corporate webmaster at Capgemini (Francois Nonnenmacher), that used a similar technique to get virtually no spam.

Furthermore, we really really want our blog's spam comments to go back into Akismet, so that Akismet learns and other blogs can benefit. If we reject spam comments at the door, so to speak, Akismet will never learn about it and it won't get better at rejecting spam. If somebody has a method for rejecting spam (in .htaccess or by looking at 404's), and at the same time let Akismet know about it, then please let us know.

> **[Thomas Baekdal](http://baekdal.com):**\
> BTW: Just out of curiosity – how much time do you spend on handling spam emails now? That is, the time it takes to look through the spam being filtered + the time spend deleting spam that missed the filter, Whitelisting and blacklisting people etc.?

At the most 30 minutes per day for both Thomas and me. It's primarily an ad hoc task. I'm looking at what is new, and get an email when a new comment is posted (or slips through the spam filter). Based on that information I either take action to delete it immediately (if it's spam) or take other actions such as answering real comments, etc.

> **[Michael Clark](http://www.planetmike.com/):**\
> I’m curious: on December 16th, after you reactivate all of your systems, are you going to submit to Akismet the spam that accumulated on the 15th? And are you using a “professional” Akismet account, or a free one?

Free account. We aim at submitting all spam comments to Akismet and apologies to anybody posting a real comment on December 15th. **By the way, is there a way to let Akismet traverse comments back in time to see if it can find any spam once we turn it back on? We really could need that to save time :)**

> **[JMorris](http://jmorris.name/):**\
> Pardon me if I misinterpreted your post, but it read as though you were going to allow automatic approval of comments. If this is the case, do you intend to put into effect some sort of indexing block in place so that search engines don’t pick up the comments and display them in your SERPs?

You understand correctly that we use automatic approval of comments. We have actually discussed pros and cons of this approach. The worst thing about it is that we offend email subscribers once in a while when a spam comment slips through. However, since we manually remove these comments within 10 minutes or so, we consider the most important thing that a discussion can take place instantly without us approving the discussion.

At a later point, if we find it necessary, we might take the step to change the settings, so that a comment from a new mail address is held for moderation, but a known person can comment with automatic approval.

With respect to SERP (search engine result pages), all links by default have the `rel="nofollow"` tag. This means that no spam comments will benefit at all from posting on our blog.

More comments in the original article: [Announcement: Spam Filter Free Day](/2007/11/27/announcement-spam-filter-free-day/)
