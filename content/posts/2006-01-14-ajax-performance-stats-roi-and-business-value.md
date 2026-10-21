---
title: "AJAX performance stats, ROI, and business value"
date: "2006-01-14T00:10:30"
slug: "ajax-performance-stats-roi-and-business-value"
url: "/2006/01/14/ajax-performance-stats-roi-and-business-value/"
wp_id: 71
categories: ["AJAX", "Best of Justaddwater", "Businesscase", "Performance", "Usability", "Web Standards", "Web Statistics"]
tags: []
---

How do you build a system that can deliver and update content to 100,000 people simultaneously? Via [Ajaxian.com](http://ajaxian.com/?p=735 "Ajax Reduces Load on MacRumors.com Servers") I saw this article from MacRumors on what traffic they got when Steve Jobs delivered his keynote on MacWorld a few days ago.

> On January 10th, 2006, [MacRumors.com](http://www.macrumors.com/) successfully delivered live updates of the Macworld San Francisco Keynote speech to over 100,000 people simultaneously using the latest web technologies.
>
> *"By far the best mac keynote coverage I have ever seen. No constant page refreshing. No 'page will update every three minutes' even though they never do. I just let the page update every minute like it was supposed to. It was actually weird to get coverage without some sort of connection failure." - MacRumors member, war*

The live coverage web solution is basically a transscript updated frequently during the keynote. One article is about the [traffic they experienced](http://www.macrumors.com/events/mwsf2006-stats.php "MacRumors.com's Webcast Stats during the Macworld San Francisco 2006 Keynote"):

> Our site was linked to widely across the web, including prominent links from [Digg](http://www.digg.com/) and [Slashdot](http://www.slashdot.org/) -- two popular technology sites. These links caused no noticable "spike" in our number of visitors, illustrating the magnitude of traffic that *MacRumorsLive* was already receiving.
>
> We peaked at approximately **103,000** simultaneous web visitors and **6,000** IRC viewers during the Keynote speech and transmited over **32 GB** of data in a three hour period. If not for the efficiency of the *MacRumorsLive* AJAX update system, the same webcast would have required approximately twice as many servers and would have had to transfer almost 6 times as much data (196 GB).

With peak loads that reaches insane levels of almost 4,000 hits per second:

> |                       |                    |
> |-----------------------|--------------------|
> | Hits/second ⁽²⁾       | 3,812              |
> | IRC users             | 6,079              |
> | Simultaneous visitors | 109,000            |
> | Bandwidth ⁽³⁾         | approx. 77Mbit/sec |

[![MacWorld keynote hits graph (from macrumors.com)](/wp-content/uploads/2006/01/hits-20060110.gif)](http://www.macrumors.com/events/mwsf2006-stats.php "MacWorld keynote hits graph (from macrumors.com)")

Hits per second from ~8am to ~12:30pm. Average over each minute.

They also posted an article about [how they built the system](http://www.macrumorslive.com/about/ "MacRumorsLive.com: EQX Webcast System") which is insanely interesting

> Traditionally, websites have coped with visitors during the keynotes by swapping to text-only pages, using HTML Meta Refresh to reload the page at set intervals, usually every three minutes, for example, [MacRumors' coverage from MacWorld in January 2005](http://www.macrumors.com/events/mwsf2005.html). As a result, the sites lose their identity and branding, and cannot make best use of the additional traffic for site promotion.
>
> Even with all this simplification the sheer number of visitors can still take the server down. To provide the best coverage during live events an improved system is required.

> As this system is retaining the normal layout of the site, all the necessary objects (CSS, images & Javascript) also need to be loaded. This increases the load placed on the web servers considerably in comparison to the old system, which only had a single text file to display. Even with the ability to use multiple servers, the web server software needs to be improved.
>
> By using [PHP](http://www.php.net/) to generate the necessary HTML & XML files every ten seconds, rather than each time the file is requested, it is possible to use small & simple web servers to deliver the public site, without the overhead of database usage. Two web server software packages are employed - [lighttpd](http://www.lighttpd.net/) and [thttpd](http://www.acme.com/software/thttpd/) - with [Apache](http://httpd.apache.org/) still being used for the administration interface.
>
> The efficiency of these packages over Apache is considerable and allows quite modest hardware to be used to serve a large number of visitors. Benchmarks of lighttpd compared to various other packages can be found on [their website](http://www.lighttpd.net/benchmark/). In our tests, thttpd was able to sustain in excess of 3,300 hits per second, whereas Apache managed only 600 hits per second for 20 seconds, before overloading the server due to memory usage. \[1\]
>
> The use of these more specialised web servers allows a vast number of simultaneous visitors to be supported - as the system stands at the moment, in excess of 200,000.

This reminds me of Ajaxinfo (the guys behind [AJAX usability metrics](http://blogs.ebusiness-apps.com/andre/?p=52)), **[AJAX ROI faceoff](http://www.ajaxinfo.com/default~viewart~18.htm),** where a traditional webapp is compared to an AJAX webapp. For the visually oriented, there is a video comparing the two applications at the end of the article.

> Recently on Developer.com, I looked at ways for developers to [communicate the value of Ajax](http://www.developer.com/xml/article.php/3554271) in dollars and cents. Arguing for or against a technology usually creates some stress for developers, who tend to speak a different language from business decision makers.
>
> [TABLE]

Right at the point. Performance website or not, the metrics he mentions above are almost like something Jakob Nielsen could have done. Conclusions:

> Although every new technology should be greeted with a healthy amount of skepticism, there are clearly demonstrable, quantifiable advantages to using an Ajax architecture in a Web application. These cost savings originate primarily from time savings, but also from reductions in bandwidth requirements.
>
> A representative test case showed that a business can save between 500 and 2,800 man hours per year on a 10-step hypothetical process, saving roughly 4 seconds per step (a between 30% and 70% reduction in labor costs).
>
> Although the benefits of improved application architecture extend beyond mere time savings, when included in the decision making process, an ROI approach such as this can help make a solid business case for Ajax.

![Total time taken (AJAX vs traditional webapp)](/wp-content/uploads/2006/01/totaltimetaken.gif)![Total bytes transferred (AJAX vs traditional webapp)](/wp-content/uploads/2006/01/bytestransferred.gif)

The benefits listed here are very similar to benefits when we're arguing for web-standards: Reduced bandwith, training costs, cost of ownership, and increased return on investment. But for the time being I still believe that AJAX has increased learning costs for developers. (Although most developers are really keen on using AJAX and webstandards it still requires expert knowledge regarding libraries, backend integration and browser compatibility — to name a few).\
I'd be happy to hear your comments on this. Please share more info here. Also check out Ajaxinfo's [Call for AJAX Studies](http://www.ajaxinfo.com/default~viewart~22.htm).

**UPDATE:** Just saw Jonathan Boutelle's [Bandwidth Savings with AJAX](http://www.jonathanboutelle.com/mt/archives/2006/01/bandwidth_savin.html "Jonathan Boutelle: Bandwith Savings with AJAX") blog post, that covers the same story and has a good point on AJAX fit frequently used applications:

> The old-school RIA technology vendors always made the claim that using the RIA paradigm saves you bandwidth. Numbers on this were always hard to get, and hard to trust.
>
> Theoretically it always made sense that an RIA would consume less bandwidth (in exchange for a larger initial download). The longer a user continues to use the application, the greater this benefit (so an RIA word processor might make more sense than an RIA news site).
>
> Now, watching a keynote presentation takes at least an hour, so it's definitely long enough to provide benefit. What we see in this case is really different though: AJAX is basically being used as a *broadcast technique*, grabbing new data every minute so that the user doesn't have to refresh the entire page. For covering live events that have a large audience, this makes a ton of sense. Expect to see more content sites "pushing" content out to their users this way.
