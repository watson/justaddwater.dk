---
title: "Explanation of Firebug Net Panel Findings"
date: "2010-04-22T14:07:11"
slug: "explanation-of-firebug-net-panel-findings"
url: "/2010/04/22/explanation-of-firebug-net-panel-findings/"
wp_id: 1311
categories: ["Web Development"]
tags: ["firebug", "http", "network", "Web Development"]
---

Jan Odvarko – one of the Firebug developers – posted some very good explanations on the information available from the Firebug net panel.

![](/wp-content/uploads/2010/04/firebug-1.5-netpanel-explained.png "firebug-1.5-netpanel-explained")

Here is the explanation of the detailed mouseover view when zooming in on each request:

![](/wp-content/uploads/2010/04/firebug-1.5-network-tooltip.png "firebug-1.5-network-tooltip")

> - The second request started **109ms** after the start of the first request (since the beginning of the waterfall graph).
> - There are two numbers for each **request phase** (5 phases). The first number on the left says when the phase started within the request. The second number on the right (closer to the phase label) says the time needed to complete each phase. In this case, the first three phases took zero time, and so the **Waiting** phase was the first real and it needed 32ms to complete. The **Receiving** phase started in **32nd ms** of the request and needed **15ms** to complete
> - ***DOMContenLoaded*** event was fired **7ms** after this request started. If this number is negative the event was fired before the request is started.
> - ***load*** event was fired **189ms** after this request started. If this number is negative the event was fired before the request is started.
>
> Here are some notes about each request phase.
>
> - **DNS Lookup**: DNS resolution time
> - **Connecting**: Elapsed time required to create a TCP connection.
> - **Blocking** (not on the screenshot): Elapsed time spent in a browser queue waiting for a network connection. Displayed only in the case where this situation happens (see also [this post](http://www.softwareishard.com/blog/firebug/page-load-analysis-using-firebug/)).
> - **Sending**: Time needed to send request data to the server.
> - **Waiting**: Waiting for the response (till the first byte is received from the server).
> - **Receiving**: Time necessary to download response body.

I found myself reading up on this because I did a HTML5 offline experiment, where the "[HTML5 .manifest files did not appear in Firebug net panel](http://groups.google.com/group/firebug/browse_thread/thread/e920884868df9555#)"

Jan Odvarko has two excellent posts explaining most functionality of the Firebug Net panel. The two posts are highly recommendable

- [Firebug Net Panel Timings](http://www.softwareishard.com/blog/firebug/firebug-net-panel-timings/) (March 2010)
- [Introduction to Firebug: Net Panel](http://www.softwareishard.com/blog/firebug/introduction-to-firebug-net-panel/) (May 2009)
