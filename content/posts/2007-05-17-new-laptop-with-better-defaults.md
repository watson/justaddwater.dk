---
title: "New Laptop With Better Defaults"
date: "2007-05-17T00:40:27"
slug: "new-laptop-with-better-defaults"
url: "/2007/05/17/new-laptop-with-better-defaults/"
wp_id: 646
categories: ["Hardware", "Usability"]
tags: []
---

***Update: CPU fan speed can be controlled. See updated notes below...(2007-11-06)***\
I got a new laptop from work last week. Swapped the old Dell D600 in for a sparkling new (IBM) Lenovo Thinkpad T60p. I really like the new one. Things I have noted for now:

- \
- Much brighter and better screen
  \
- Lovely keyboard which is a pleasure to use
  \
- Funky gestures for the Touchpad
  \
- ~~CPU fan always running~~
  


### Lovely Keyboard ... but...

In general, the keyboard is really a pleasure to use. The keys have perfect weight and just right feedback. It makes a tiny clicking sound but not too clicky like the old Dell. In general the keys are good positioned and not too close (although there is an inch of unused space on each side of the keyboard. This space had been better used if it were used to put more space between essential groups of characters. (some of the buttons I hit Here are some of the buttons I hit in error occationally (which indicates that keys are too tight in that area):

1.  \
2.  I hit Fn when I want to hit CTRL
    \
3.  I turn on keyboard light when I want to page back between tabs in Firefox (variant of \#1)
    \
4.  I hit F3 when I want to hit F2 (to rename a file)
    \
5.  I hit F1 when I want to hit Esc
    \
6.  I hit the windows button when I want to hit CTRL
    \
7.  I hit the "page back" button when I want to hit arrow left
    

These are sorted from my memory of, which buttons I mistakenly press most often. Some of these errors can be solved with a keyboard customization program that is preinstalled with the computer. Screenshot below shows that I was able to adjust sensitivity of F1, back and forward buttons (all of which I use very rarely).

[![thinkpad-keyboard-configurations.png](/wp-content/uploads/2007/05/thinkpad-keyboard-configurations-thumbnail.png)](/wp-content/uploads/2007/05/thinkpad-keyboard-configurations.png "thinkpad-keyboard-configurations-thumbnail.png")

### Big mistake: Fn and CTRL buttons have swapped place

[![thinkpad-t60p-keyboard-10902.jpg](/wp-content/uploads/2007/05/thinkpad-t60p-keyboard-10902-thumbnail.jpg)](/wp-content/uploads/2007/05/thinkpad-t60p-keyboard-10902.jpg "thinkpad-t60p-keyboard-10902.jpg")

I really feared that and my fears turned out to be true. IBM/Lenovo laptops have swapped positioning of the Fn and left CTRL button. This is really annoying. And I'm [not the only one saying this.](http://blogoff.dk/2007/04/24/keyboard-design/ "Andreas Mailand: Keyboard Design") Mostly because I'm used to hitting CTRL a lot. I have a dedicated goal to use keyboard shortcuts as much as possible to increase productivity. But also for another reason.

This is simply less productive. No keyboard shortcuts with the Fn button involves pressing more than one key, but CTRL keyboard shortcuts often involve the Shift key as well. The principle of bringing closely related items together is simply broken here: **CTRL and Shift should be close together — as close as possible** .

In general, the keys at the edge of the keyboard are the easiest to locate. Therefore, a high productivity keyboard should have keys that are used often at the edge/corners and putting Fn at the lower left is a disaster for keypresses like CTRL + Shift + Arrow keys to select text in word chunks. Try that followed by CTRL + X for cutting the text to clipboard. I just can't get used to it.

Lenovo really should change this, in order for keyboard shortcuts to be as productive as possible. The danger is that if they change, probably some of their loyal customers that have burnt their fingers so many times that any change will be a challenge. But it has to be done, or my hand might grow in a strange angle...

If you don't believe me, try this with your left hand: Pressing Shift with your 4th finger while the little finger presses CTRL so that the little finger is twisted under and to the right of the index finger. Now, with your hand twisted to the left, try hitting T (as I do with CTRL+Shift+T for opening the file menu in my favorite editor). This is barely possible withing the physical limits of ordinary people. Concert Pianists have a vague chance of getting it right, but it's still a challenge with your and mind eyes focused on getting actual work done.

Here are some of the keyboard shortcuts I'm used to but are difficult (or non-productive) to use on my Lenovo keyboard:

1.  \
2.  CTRL + Shift + Arrow keys (selecting text in chunks of words)
    \
3.  CTRL + Shift + Esc (open task manager)
    \
4.  CTRL + Shift + F (find in files in some editors)
    \
5.  CTRL + Shift + T (intelligent file open in my favorite editor)
    

Because of the awkward placement of CTRL, I'm learning to use the right CTRL when pressing PgUp or PgDn — I use that a lot in Firefox. (For some reason, CTRL + Shift + S and CTRL + Shift + P works out OK because its some of the keys where I can use a more natural hand position to hit the keys).

I remember hearing [Tog Tognazzini](http://www.asktog.com/tog.html) once speaking about Fitt's law and their work at Apple on sizes of targets like the Windows Start button. He noted that in the first Windows versions, there was a tiny 1 pixel border all the way around the button, which meant that you could only hit it if you precisely moved the cursor to the placement. In recent versions of Windows (and on a Mac), you can simply slash your mouse out to the edge, and the cursor will just stay there at the most left pixel. With these edge pixels activated it's much easier to hit. I think a similar thing proves true on my keyboard: Esc, left CTRL and arrow keys are easy to locate and hit because they're in the corners. (of course, they would be even easier to hit if they were at the default positions of my fingers, but that's a different story...)

(Is there a textual reference to any written explanation of Tog's story? I was not able to find it. Please update me and drop a comment below.)

### Funky gestures for the touchpad

This is a nice one, that I really missed on the old Dell: Scrolling and advanced use of the touchpad. Recently, when Thomas Watson showed me his new Mac, I was impressed with the way to scroll. (Two fingers on the touchpad on a Mac scrolls). This is almost as good: Just move your finger along the right or lower edge of the screen will scroll. I'm really happy with this setting.

[![thinkpad-touchpad-configuration.png](/wp-content/uploads/2007/05/thinkpad-touchpad-configuration-thumbnail.png)](/wp-content/uploads/2007/05/thinkpad-touchpad-configuration.png "thinkpad-touchpad-configuration.png")

The best thing about it: It works this way out of the box. **Settings are nothing. Having good default settings are everything!**

### Problems with hibernation and standby

![windows-system-hibernate-system-error.png](/wp-content/uploads/2007/05/windows-system-hibernate-system-error.png)

Microsoft hotfix to solve it: [Hotfix 909095](http://support.microsoft.com/?kbid=909095) ("The computer occasionally does not hibernate and you receive an "Insufficient System Resources Exist to Complete the API" error message").

Running ThinkVantage System Updater told me to update a few essential programs: BIOS, graphics card driver, and add a program to manage keyboard shortcuts

### *Solved issue*: Fan always running (updated!)

Fan is always running. Even at low CPU usage (usually 2-7%), the CPU fan is always running. This is very annoying. Especially when running on batteries, as I presume it drains the battery faster. Here is a screenshot during typical usage:

[![speedfan-cpu-harddisk-temperature-thumbnail.png](/wp-content/uploads/2007/05/speedfan-cpu-harddisk-temperature-thumbnail.png)](/wp-content/uploads/2007/05/speedfan-cpu-harddisk-temperature.png "speedfan-cpu-harddisk-temperature.png")

Is this hot? Is this high CPU usage? What if CPU usage goes to 100%? It should really handle the fan control better. So I guess the question is: How do I turn the fan off or lower the CPU frequency in order to silence the fan? My big driver here is off course saving battery.

**Update: Fan speed is caused by graphics processor (GPU) running hot. This is apparently a design issue because GPU is not cooled by the fan:** See "[Lenovo Thinkpad Silent Fan](/2007/11/06/lenovo-thinkpad-silent-fan/ "Permanent Link to Lenovo Thinkpad Silent Fan")" (November 2007) [](/2007/11/06/lenovo-thinkpad-silent-fan/ "Permanent Link to Lenovo Thinkpad Silent Fan")

### Non solved issue: Swap Fn and CTRL buttons

Is there software to swap these buttons around? Putting Fn bottom left and CTRL to the right of it puts my hand in awkward position when I use some of my usual shortcuts. This is simply less productive. **No keyboard shortcuts with the Fn button involves pressing more than one key, but CTRL keyboard shortcuts often involve the Shift key** as well. The principle of bringing closely related items together is simply broken here: CTRL and Shift should be close together.

In general, the keys at the edge of the keyboard are the easiest to locate. Therefore, a high productivity keyboard should have keys that are used often at the edge/corners and putting Fn at the lower left is a disaster for most keypresses that involve the CTRL and Shift keys.

Lenovo really should change this, in order for keyboard shortcuts to be as productive as possible. The danger is that if they change, probably some of their loyal customers that have burnt their fingers so many times that any change will be a challenge. But it has to be done, or my hand might grow in a strange angle...

### Other minor issues

Another funny thing: Occasionally, the wireless network stops working. It's suddenly not possible to connect even though, sometimes networks are visible. Only cure is to restart computer.

**In summary,** still with these usability issues that affect my productivity or battery consumption, the new laptop is much better configured out of the box than the old one. However, some settings should not be changed, and I urge Lenovo to swap around Fn and CTRL for the next release... If they dare.

Update 2007-05-15: I got my first dreaded "blue screen of death" this morning.. Have absolutely no clue what happened.
