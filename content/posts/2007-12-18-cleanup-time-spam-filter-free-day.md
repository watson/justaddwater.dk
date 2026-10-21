---
title: "Cleanup Time -- Spam Filter Free Day"
date: "2007-12-18T10:55:58"
slug: "cleanup-time-spam-filter-free-day"
url: "/2007/12/18/cleanup-time-spam-filter-free-day/"
wp_id: 807
categories: ["justaddwater.dk", "spam", "WordPress"]
tags: []
author: "jesper"
---

1111 spam comments in the last 24 hours have been published on Justaddwater.dk. Just for the record, all of them are now deleted. The many spam comments has had no effect whatsoever with respect to Google PageRank or similar, since we kept \<code\>rel="nofollow"\</code\> on all links. Besides, we quickly removed all spam comments at the end of Spam Filter Free Day.

137 new conversations in my mailbox telling me that 137 articles I wrote were hit by spam comments the last 24 hours.

[![spam-filter-free-day-gmail-inbox-tiny.png](/wp-content/uploads/2007/12/spam-filter-free-day-gmail-inbox-tiny.png)](/wp-content/uploads/2007/12/spam-filter-free-day-gmail-inbox.png "spam-filter-free-day-gmail-inbox.png")

## **Important lesson: Almost none of the recent posts have spam comments**

The screenshot below shows that only 2 of the latest 20 posts have recieved spam comments. So it seems the logic behind it is that spammers need time to harvest links for potential targets.

[![spam-filter-free-day-frontpage-spam-count-thumb.png](/wp-content/uploads/2007/12/spam-filter-free-day-frontpage-spam-count-thumb.png)](/wp-content/uploads/2007/12/spam-filter-free-day-frontpage-spam-count.png "spam-filter-free-day-frontpage-spam-count.png")\
(click to view entire count on first 40 articles)

No posts newer than 11 days are hit by spam comments. 2 comments on "[Spam Comments Dropped 95% Overnight](/2007/12/04/spam-comments-dropped-95-overnight/ "Permanent Link to Spam Comments Dropped 95% Overnight")" from December 4th.

So on this particular day, spam comments only hit in after 11 days and should be used to our advantage. There are currently these different strategies to consider:

1.  Close old posts for comments
2.  Close old posts for comments but keep active posts open
3.  Hold back comments on old posts for moderation
4.  Hold back comments on old posts for moderation unless posted by a user that has a previously approved comment

Thomas and I talked this over yesterday, and would really prefer number 4, and we can live with number 3. Number 1 and 2 are implemented by a wordpress plugin (i forget the name).

The real difference is in the user experience. 1 and 2 are unacceptable for us, since it will block our users' valid comments if, say, somebody has an update to an old article or wants to send a trackback from a related post. This really works against the [wisdom of crowds](/2006/04/07/the-wisdom-of-crowds/) principle, that works best if everybody is allowed to comment right away.

Does anybody know a plugin that can do number 3 or 4?.

## Wordpress flaws and bugs:

- Three comments were incorrectly held for moderation by Wordpress even though the link limit were set to 99 and the comments clearly did not contain 99 links.[![spam-filter-free-day-awaiting-moderation-thumb.png](/wp-content/uploads/2007/12/spam-filter-free-day-awaiting-moderationthumb.png)](/wp-content/uploads/2007/12/spam-filter-free-day-awaiting-moderation.png "spam-filter-free-day-awaiting-moderation.png")
- The interface for marking comments as spam is unproductive. It took me two hours to mark 1111 comments as spam (and de-spamming 6 valid comments). I used "mass edit" screen and checked all. Pressed "mark checked comments as spam". Then pressed OK to the JavaScript confirmation. [![spam-filter-free-day-deleting-confirmation-thumb.png](/wp-content/uploads/2007/12/spam-filter-free-day-deleting-confirmation-thumb.png)](/wp-content/uploads/2007/12/spam-filter-free-day-deleting-confirmation-thumb.png "spam-filter-free-day-deleting-confirmation.png")I don't know the internal procedures here -- but it seems as if wordpress sends the 20 spam marked comments directly to Akismet. And waits for the response before showing me the next page. My workaround here was to first open page 1-20 in 20 different tabs. Then for each of them check all and press "mark checked comments as spam".
- Recheck Queue for spam is a brilliant feature -- but works on the wrong data. The feature should be copied to the "comments" tab. This way, you could force a rerun if your spam filter is out of order for a period of time. Also that would be the usecase of people trying out a spam filter. "wow I got more spam comments than I can handle. Let me try and install a spam filter and see what it can do for me". In this case, the spam filter not only works forward in time after activation, but also backwards. (obviously there must be a feature to review the past comments marked as spam). ![spam-filter-free-day-recheck-que-for-spam.png](/wp-content/uploads/2007/12/spam-filter-free-day-recheck-que-for-spam.png)
- Blank email posts slip through even when the setting does not allow it. I have suspected this to happen also in previous versions of Wordpress. Several of the 1111 comments we recieved during Spam Filter Free Day were with blank email. And that should not be possible because of the setting in Wordpress "Comment author must fill out name and e-mail" (found at Admin\>Options\>Discussion). ![spam-filter-free-day-blank-emails.png](/wp-content/uploads/2007/12/spam-filter-free-day-blank-emails.png) I would expect these comments to be rejected and not even show up at the administrators' panels. But for some reasons they still appear. Perhaps a tiny bug in Wordpress? Or maybe spammers found a hole? Or are these trackbacks/pingbacks that just look like comments? Or maybe the [updated Akismet version 2.1.2](http://blog.akismet.com/2007/12/17/new-plugin-version-21/) actually deals with this because they added separate tabs for trackbacks and pingbacks?

All in all, we learned a few lessons and found some areas, where wordpress could improve in order to deal with comments that slips through. Total time consumption for removing these comments were 2 hours, which actually surprised us to be very low. But note also that this was not "just" a day without Akismet. In that case, we would probably had to keep comments under surveillance, and remove them during the day. In that case, time consumption would perhaps have been something like 6 hours during a 24 hour period.

As to whether we would do it again as a reoccuring event? Most likely not. We don't want our regular readers to suffer, so we prefer to keep our blog safe and sound and in good shape, by keeping the guards up. On the other hand, it has been a learning experience to do the Spam Filter Free Day. Not only has our daily spam count decreased (perhaps because spammers have understood that comments that momentarily slip through have no effect on PageRank or similar). Also, we wanted to raise awareness of the bandwith and processing power (machine and human) that spam comments waste every day. And last also do this day as a thank to spamfilters such as Akismet. (heck, comments on other blogs even alledge that the Spam Filter Day is a publicity trick from Akismet... I can strongly deny that as we -- thomas and jesper -- can take full responsibility for inventing this event. And we are in no way affiliated with Akismet).

I would really appreciate comments with respect to plugins that do not close articles for comments -- but in stead holds comments back for moderation. I will subsequently update this article with links.
