---
title: "Just added Google Analytics as tracker tool"
date: "2005-11-14T11:17:32"
slug: "google-analytics"
url: "/2005/11/14/google-analytics/"
wp_id: 16
categories: ["justaddwater.dk", "Usability", "Web Standards", "Web Statistics"]
tags: []
author: "jesper"
---

We just signed up for testing the new [Google Analytics](http://www.google.com/analytics) statistics software. It gives us an idea of who is browsing our website. On the humorous side, the signup process is missing something. It seems that the license agreement is not found. Hilarious. Of course I accepted (but I'm still wondering what that means). We're looking forward to try this out.

[{{< img src=`http://static.flickr.com/26/63155510_d2335c263a_m.jpg` alt=`screenshot google analytics agreement` width=`240` height=`225` >}}](http://www.flickr.com/photos/jesper/63155510/ "screenshot google analytics: license agreement not found")

Photo Matt writes that this is the first [online stat tool that actuallly validates XHTML strict](http://photomatt.net/2005/11/14/google-analytics/). Previously, it's been a problem with major sites that use online stats, that the JavaScript messes up an otherwise XHTML compliant page:

> People love stats so this will get huge uptake, and probably provide Google really invaluable information. A year or so ago I hoped Technorati would do this for blogs, but they probably saw it as outside their core business. Interesting note: this is the first stat tracking javascript I’ve seen that validates as XHTML Strict. Good job, guys. (Most examples leave the language attribute.)

Well, it seems that other web analytics tools also get it right. I had a brief look at our [Capgemini](http://www.capgemini.com/) corporate frontpage. It [validates XHTML](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.capgemini.com%2F) (transitional) and includes this bit of tracker JavaScript:

`<script type="text/javascript">`\
`<!-- //`\
`pageLoaded = true;`\
`// -->`\
`</script>`\
`<!-- END #page -->`\
`<!-- SiteCatalyst code version: G.7.`\
`Copyright 1997-2004 Omniture, Inc. More info available at`\
`http://www.omniture.com --><script language="JavaScript" type="text/JavaScript"><!--`\
`var s_pageName="Collaborative Business Experience"`\
`var s_channel="home"`\
`//--></script><script language="JavaScript" src="/js/s_code_remote.js" type="text/JavaScript"></script><!-- End SiteCatalyst code version: G.7. -->`

**UPDATE 2005-11-16:** Since we signed up two days ago, the service has not really been working. People have been complaining about Google Analytics all over the net (examples from [Techcrunch](http://www.techcrunch.com/2005/11/14/google-analytics-swings-at-measure-map/), [Ethan Stock](http://onotech.blogspot.com/2005_11_01_onotech_archive.html#113200904055483341), [TDavid](http://www.makeyougohmm.com/?p=2614)). We're still looking forward to see some data from our website....

**UPDATE 2005-11-17:** Finally, we get data. Google Analytics seem to have solved their problems so now we can use the statistics module. It looks good. Fairly easy to use. I'm now wondering how often data will be updated. I saw the first data 16 hours ago (56 unique users in total). Now 16 hours later, it still says 56 unique users. It's a pretty unlikely event that nobody has visited the page in the meantime. Both Thomas an I have visited the site. So how often will data be updated? Hopefully more often than once a day.

Technorati tags: [google](http://technorati.com/tag/google) [analytics](http://technorati.com/tag/analytics) [stat](http://technorati.com/tag/stat) [screenshot](http://technorati.com/tag/screenshot) [license](http://technorati.com/tag/license)
