---
title: "Wordpress Dashboard improvements: Five things I'd like my blog software to do"
date: "2006-01-12T22:39:45"
slug: "blog-software-usability"
url: "/2006/01/12/blog-software-usability/"
wp_id: 60
categories: ["AJAX", "Blogging", "Links", "Web Statistics", "WordPress"]
tags: []
author: "jesper"
technorati: ["wordpress", "blogging", "search", "usability", "google analytics", "ajax", "dashboard", "wordpress dashboard"]
---

*UPDATE: Owen's comment pointed me to [WordPress Admin Dashboard replacement](http://blog.taragana.com/index.php/archive/angsumans-wordpress-20-dashboard-replacement-how-to-trim-the-fat-resource-hogging-wordpress-admin-dashboard/) which apparently adresses some of the issues I'm pointing out.*

I like Wordpress Dashboard. The name suggests that it's an overview of whats relevant to your blog. What's happening. What's popular. Who comments. What important updates are available. The Dashboard should work like in a car. The **most important and relevant information should be visible at a glance**. Lets have a brief look at the dashboard.\
I suggest you only take a brief look to judge for your self whether you think the main objectives of the Dashboard page are met.

[{{< img src=`/wp-content/uploads/2006/01/screenshot%20WordPress%20dashboard%201137074448414.thumbnail.png` alt=`Wordpress Dashboard for Justaddwater.dk` width=`62` height=`96` >}}](/wp-content/uploads/2006/01/screenshot%20WordPress%20dashboard%201137074448414.png "Wordpress Dashboard for Justaddwater.dk")

Click on the screenshot above for and look for 5 seconds only. Then ask yourself what you could remember from the page. Yup you just tried a [5 second usability test](http://www.uie.com/articles/five_second_test/).

### What works

The top left section "Welcome to Wordpress" contains a brief overview for the most relevant actions to administer the weblog (write a post, update profile, etc.). This is added from version 2.0 and works well as an appetizer (especially for newbies).

"Latest activity" is a good headline that immediately gets my attention. I can see things happening: posts, comments, incoming links. Very good, as I think this sums up what I'd like to know from a dashboard-view. However, I don't think that "latest activity" contains what it should to give me the complete overview.

### What I think should improve

1.  **Incoming links should show ALL incoming links.** The dashboard already has a box labeled "incoming links", but it doesn't show any referring URLs. Referring URLs (or link referrals) are registered by a browser as the page that link to the current page. In my opinion, referring URLs are of great value, as we want to know who link to us and how users get to know our website. I recently wrote that even in [Google Analytics this feature is hard to find](/2006/01/08/google-analytics-trick-how-to-view-referring-urls/ "Google Analytics trick: How to view referring URLs"). "Incoming links" should show both trackbacks AND referring URLs. Most browsers send information as HTTP header "Referer" when they request the page.
2.  **Add recent searches to activity list**. What are people searching for on my blog. Luckily we have a web-server access log that can tell me, but it requires digging and parsing a file on a regular basis. The dashboard has information recent trackback links and comments. It would be appropriate to add a list with recent searches.
3.  **Update the Dashboard when something interesting happens.** Ajax calls to the web server could keep "Latest Activity" up-to-date whenever a comment is posted, searches and trackbacks are performed. Also the display could update when my partner posts a new article on the site.
4.  **Clean up the dashboard. Remove things that are not relevant to me.** In particular, i think "Other Wordpress News" are too dominant (although placed in the bottom below the fold). Only a few of the news are directly Wordpress related. Other Wordpress News could easily be replaced by a link to planet.wordpress.org (from which the news are taken). After all, this will lead to faster response times, and will probably make the Dashboard more relevant to users like myself that wonders what on earth "Owen Winkler: I didn't do it" has to do with my blog.
5.  **Add latest drafts to Dashboard**. Maybe it's just me. Usually I'm working on 2-3 stories that I save as drafts. I think that these should be on the dashboard as well.

Here's a quick mockup of the changes i propose.

[![screenshot wordpress dashboard with improvements](/wp-content/uploads/2006/01/screenshot%20WordPress%20dashboard%20modified%20halfsize.png "screenshot wordpress dashboard with improvements")](/wp-content/uploads/2006/01/screenshot%20WordPress%20dashboard%20modified%20halfsize.png "Wordpress dashboard modified. Click to view larger image")
