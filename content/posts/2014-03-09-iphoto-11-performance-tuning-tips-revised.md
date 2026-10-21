---
title: "iPhoto 11 performance tuning tips, revised"
date: "2014-03-09T20:41:07"
slug: "iphoto-11-performance-tuning-tips-revised"
url: "/2014/03/09/iphoto-11-performance-tuning-tips-revised/"
wp_id: 1709
categories: ["justaddwater.dk"]
tags: []
---

My iPhoto library with 6000+ family photos was running slow on my macbook. So I looked for performance tuning tips on the net.

Here are the adjusted tip, which works for me.

 

This [Apple support  thread](https://discussions.apple.com/thread/3012995?start=60&tstart=0) mentioned 3 tips:

1.  Upgrade RAM
2.  Turn off visual bling in overview pages
3.  Vacuum iPhoto database file 

Could not do anything with tip 1 today (and I presume I cannot update the RAM on this 2012 macbook air)

Tip2 works: Go into settings \> "appearance" and turn off "Outline" and "Drop shadow" in the overviews.

Tip3 needs adjustment. Originally \*.db files were only in top folder ' ~/Pictures/iPhoto\\ Library/'

 

Adjusted command to vacuum iPhoto database files:

 

```
cd ~/Pictures/iPhoto\ Library/ &&  for dbase in `find . -name '*.db'`; do sqlite3 $dbase "vacuum;"; done
```
