---
title: "Lenovo Thinkpad Silent Fan"
date: "2007-11-06T00:26:39"
slug: "lenovo-thinkpad-silent-fan"
url: "/2007/11/06/lenovo-thinkpad-silent-fan/"
wp_id: 761
categories: ["Hardware"]
tags: []
---

Since I got my Lenovo Thinkpad T60p I have always wondered why the fan kept running away (even just after booting).

Turns out there is a program to manipulate the speed of the fan: tpfancontrol

[![thinkpad-fancontrol-for-t60p-small.png](/wp-content/uploads/2007/11/thinkpad-fancontrol-for-t60p-small.png)](/wp-content/uploads/2007/11/thinkpad-fancontrol-for-t60p.png "thinkpad-fancontrol-for-t60p.png")

With this, you can tune your fan speed and follow the temparature readings at the right.

Using this program permanently is probably a bad idea to do since Lenovo will probably void any guarantee on your computer. To spare you from the inconvenience of testing I did a brief test run of the program:

\* The two most interesting temperatures are CPU (apparently combined for the two cores), and GPU (the graphical processor).

\* Setting the speed to max had no effect on the GPU -- it is apparently not close to the fan.

\* Setting the speed down for some moments to 2 or 1 had no effect on the GPU either. And the CPU stayed at 48 degrees C.

## Graphical processor not cooled by fan

So probably the worst thing for my poor windows machine is that no matter how fast the fan goes, it will never be able to cool the Ati GPU in the laptop.

![thinkpad-fancontrol-for-t60p-ati-gpu-graphical-processor-not-cooled-by-fan.png](/wp-content/uploads/2007/11/thinkpad-fancontrol-for-t60p-ati-gpu-graphical-processor-not-cooled-by-fan.png)

This also may explain why I previously have had problems where the graphics card is probably involved:\
\* The computer has problems setting the right screen size for my new 22" Dell E228wfp monitor even though it has exactly the same screen dimensions as the built in laptop screen (1680x1050).

\* Installing Ubuntu 7.10 crashes when starting up the install program: It tries to start the graphical user interface, but fails to. The error below was when attempting to install the final release candidate, and some similar thing happened when I tried installing the final 7.10 release (desktop).

![thinkpad-t60p-ubuntu-install-fails-graphics.jpg](/wp-content/uploads/2007/11/thinkpad-t60p-ubuntu-install-fails-graphics.jpg)

As I see it, there are two possibilities: Either this machine has been delivered with a bad quality graphics card. I have no previous experience with ATI, but having big problems connecting a standard screen with the same screen-size should be easy.

The other possibility is that the graphics card has been damaged by the high temperature when the laptop is running.

Either way, it's obviously some kind of construction error that GPU is placed so that the fan is not able to cool it.

UPDATE (8 hours later): Maybe there is something with that ATI graphics processor. From this model comparison on the Lenovo site, you can see that they change to NVIDIA GPUs going from T60p to T61p

It also says that\
Maybe there is something with that ATI graphics processor. From this model comparison on the Lenovo site, you can see that they change to NVIDIA GPUs going from T60p to T61p

It also says that

> The new ThinkPad T61 is the most secure, strongest, coolest and quietest T Series ever

(which doesnt surprise me: With a red hot ATI chip that makes the fan go at fastest speed constantly, there is definitely room for improvement)\
Source: [Lenovo ThinkPad T Series homepage](http://www.pc.ibm.com/europe/thinkpad/why/en/tseries.html?dk&cc=dk)

Previous info[](/2007/05/17/new-laptop-with-better-defaults/ "Permanent Link to New Laptop With Better Defaults")

- [New Laptop With Better Defaults](/2007/05/17/new-laptop-with-better-defaults/ "Permanent Link to New Laptop With Better Defaults") (May 2007) -- there is a section about "fan always running"
- [Lenovo Problem: No Wireless Reconnect After Standby](/2007/07/25/lenovo-problem-no-wireless-reconnect-after-standby/ "Permanent Link to Lenovo Problem: No Wireless Reconnect After Standby") (July 2007)
- [Lenovo Power Supply Almost Caught Fire](/2007/10/08/lenovo-power-supply-almost-caught-fire/ "Permanent Link to Lenovo Power Supply Almost Caught Fire") (October 2007)
- [TPfancontrol on SourceForge](http://sourceforge.net/projects/tp4xfancontrol/) [(found via this forum "Lenovo T60 fan constantly running")](http://forum.notebookreview.com/showthread.php?p=2638398 "Notebook Review.com: T60 Fan constantly running")
