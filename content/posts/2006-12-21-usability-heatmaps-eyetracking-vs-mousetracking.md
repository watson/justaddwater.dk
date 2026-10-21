---
title: "Usability Heatmaps, Eyetracking vs Mousetracking"
date: "2006-12-21T11:28:53"
slug: "usability-heatmaps-eyetracking-vs-mousetracking"
url: "/2006/12/21/usability-heatmaps-eyetracking-vs-mousetracking/"
wp_id: 494
categories: ["justaddwater.dk", "Usability", "User Interface"]
tags: []
author: "jesper"
---

Recently I was recommended taking a look at [CrazyEgg](http://crazyegg.com) which could be a possible candidate for creating heatmaps of user navigation. Rather than to be specific to CrazyEgg, I would like to comment on the general principles and pitfalls when using the methodology that CrazyEgg uses.

[![crazyegg heatmap](/wp-content/uploads/2006/12/crazyegg-heatmap.thumbnail.png)](/2006/12/21/usability-heatmaps-eyetracking-vs-mousetracking/crazyegg-heatmap/ "crazyegg heatmap")\
*Heatmap (from CrazyEgg demo site)*

As I understand, it works by injecting a javascript on the page, then tracking mouse movement and clicks. Here are my immediate comments for the concept:

- Sounds like a good idea for "poor mans tests". You can do tests with low effort, no test lead, and on all your users. It can't get more quantitative :)
- Tracks mouse movement not eye movement. Results will be skewed compared to "traditional" eyetracking tests
- Results depend on how users use the mouse. Results will be skewed by users that don't use mouse, users that use a laptop with trackpad or another device for moving the cursor around on screen. More on that later.
- However, if logfiles or your current statistics tool fail to give you the answers, or if traditional eyetracking is not possible, the CrazyEgg method could give you some valuable insight.
- Also, there could be more niche-like usage scenarios: For instance, are there any elements in the user interface that users think are clickable but are not?

### Mouse vs. trackpad

In my opinion, there is a difference in the results collected by mouse-tracking because it's skewed by the mouse (or "pointing device" to put it in academic terms).

![Trackpad on a laptop and mouse next to it](/wp-content/uploads/2006/12/trackpad-and-mouse.jpg)

Some pointing devices are simple and natural to use and others are not. For instance, I move my mouse around with the hand, sometimes I "read" or "look for information" with my mouse.

When I use my trackpad on the laptop, however, it's more when I *really need to*: When I've found where to click (and it's too far away for using the TAB key), I use my index finger to move the cursor. A trackpad gives me more tensions and strain in the underarm and it's harder and more time-consuming to target the right spot.

### Your opinion

I'd love to hear your comments on this. What are your opinions? Any testing data to back it up? Any other considerations to put into the equation?
