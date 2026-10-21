---
title: "Windows Vista Off Button Usability Issues"
date: "2006-11-26T20:28:09"
slug: "windows-vista-off-button-usability-issues"
url: "/2006/11/26/windows-vista-off-button-usability-issues/"
wp_id: 467
categories: ["Usability", "User Interface"]
tags: []
---

Below is my argument that some user interface widgets are introduced only because of buggy software. First let's have a look at Windows Vista. Joel Spolsky is picking on the 24 people that designed the Off button in Windows Vista: [Choices = Headaches](http://www.joelonsoftware.com/items/2006/11/21.html).

> I'm sure there's a whole *team* of UI designers, programmers, and testers who worked very hard on the OFF button in Windows Vista, but seriously, is this the best you could come up with?
>
> ![Image of the menu in Windows Vista for turning off the computer](http://www.joelonsoftware.com/items/2006/11/21vistaOff.PNG)
>
> Every time you want to leave your computer, you have to choose between nine, count them, nine options: two icons and seven menu items. The two icons, I think, are shortcuts to menu items. I'm guessing the lock icon does the same thing as the lock menu item, but I'm not sure which menu item the on/off icon corresponds to.
>
> On many laptops, there are also four FN+Key combinations to power off, hibernate, sleep, etc. That brings us up to 13 choices, and, oh, yeah, there's an on-off button, 14, and you can close the lid, 15. A total of fifteen different ways to shut down a laptop that you're expected to choose from.

Also, Joel references Barry Schwartz' Paradox of Choice (that I [wrote about yesterday](/2006/11/24/paradox-of-choice-barry-schwartz-video/)), as a great reminder that less choice is more valuable.

Joel shrinks the number of choices down to one option with the following rationale:

> The fact that you have to choose between nine different ways of turning off your computer every time just on the start menu, not to mention the choice of hitting the physical on/off button or closing the laptop lid, produces just a little bit of unhappiness every time.
>
> Can anything be done? It must be possible. iPods don't even have an on/off switch. Here are some ideas.
>
> If you've spoken to a non-geek recently, you may have noticed that they have no idea what the difference is between "sleep" and "hibernate." They could be trivially merged. One option down.
>
> Switch User and Lock can be combined by letting a second user log on when the system is locked. That would probably save a lot of forced-logouts anyway. Another option down.
>
> Once you've merged Switch User and Lock, do you really need Log Off? The only thing Log Off gets you is that it exits all running programs. But so does powering off, so if you're really concerned about exiting all running programs, just power off and on again. One more option gone.
>
> Restart can be eliminated. 95% of the time you need this it's because of an installation which prompted you to restart, anyway. For the other cases, you can just turn the power off and then turn it on again. Another option goes away. Less choice, less pain.
>
> Of course, you should eliminate the distinction between the icons and the menu. That eliminates two more choices. We are down to:
>
> Sleep/Hibernate\
> Switch User/Lock\
> Shut Down
>
> What if we combined Sleep, Hibernate, Switch User and Lock modes? When you go into this mode, the computer flips to the "Switch User" screen. If nobody logs on for about 30 seconds, it sleeps. A few minutes later, it hibernates. In all cases, it's locked. So now we've got two options left:
>
> \(1\) I am going away from my computer now\
> \(2\) I am going away from my computer now, but I'd like the power to be really off
>
> Why do you want the power off? If you're concerned about power usage, let the power management software worry about that. It's smarter than you are. If you're going to open the box and don't want to get shocked, well, just powering off the system doesn't really completely make it safe to open the box; you have to unplug it anyway. So, if Windows used RAM that was effectively nonvolatile, by swapping memory out to flash drives during idle time, effectively you would be able to remove power whenever you're in "away" mode without losing anything. Those new hybrid hard drives can make this super fast.
>
> So now we've got exactly one log off button left. Call it "b'bye". When you click b'bye, the screen is locked and any RAM that hasn't already been copied out to flash is written. You can log back on, or anyone else can log on and get their own session, or you can unplug the whole computer.

This is where I think Joel should revisit Paradox of Choice. What he gets right here is to reduce the overwhelming number of options, to make it easier to choose from. But reducing it to one option is the same as no choice. According to Barry Schwartz, no choice makes people feel worse. So in theory, the ideal here is to have a recommended choice and just a few options that are easy to distinct from each other.

I'd like to reduce it only to\
\* lock\
\* shut down

When you lock you can access other possibilities (leaving your computer on). That would be change user, log out, etc.

When you shut down, you can manually restart your computer. I see no problem in adding that little extra step when you restart that you must manually press the start button. Why? Well, ideally, restart should not be necessary for updating windows, right! Or Internet Explorer, or Word.

I'm guessing here, but **the Restart button in Windows probably appeared because of buggy software**. It was a frequent task that people used often, hence there was a value in combining the two steps (shut down, then start) into one Restart action.

My next post will discuss the save button. Any comments on other user interface functions that are introduced because of buggy software?
