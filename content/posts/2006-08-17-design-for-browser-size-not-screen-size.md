---
title: "Design for Browser Size — Not Screen Size"
date: "2006-08-17T09:52:09"
slug: "design-for-browser-size-not-screen-size"
url: "/2006/08/17/design-for-browser-size-not-screen-size/"
wp_id: 367
categories: ["Best of Justaddwater", "Browser", "Usability", "User Interface"]
tags: []
author: "jesper"
technorati: ["usability", "screen size", "screen resolution", "browser", "web design", "liquid layout", "window size", "jakob nielsen", "web statistics"]
---

***Update 2006-11-08:** Baekdal has published numbers (hard evidence) on browser size. And a fun research video too. See "[Actual Browser Sizes (final)](/2006/10/31/actual-browser-sizes-final/)*

Jakob Nielsen discusses screen resolution and page layout in a [recent Alertbox article](http://www.useit.com/alertbox/screen_resolution.html "Useit.com, Alertbox: Screen Resolution and Page Layout (July 31, 2006)").

> Optimize Web pages for 1024x768, but use a liquid layout that stretches well for any resolution, from 800x600 to 1280x1024.

As usual, Jakob offers some decent facts and clear guidelines on which screen resolution to design for. I have the deepest respect for Jakob Nielsen and the work he does to make usability easier to understand and use for everybody. **There is just one problem: Findings should focus on browser window size and not screen size.** (More precisely, browser content area, which we'll get back to shortly)

> Currently, about **60%** of all monitors are set at **1024x768** pixels. In comparison, only about **17%** use **800x600** so it's obviously less important to aim at perfection for these small-display users. What's equally obvious, however, is that you can't simply ignore 17% of your customer segment by providing a frozen layout that requires more screen space than they have available.

People working professionally with web know the difference between screen size and browser content area, but to make it clear I wanted to illustrate that screen size is irrelevant in comparison to other more important metrics.

To illustrate the difference, look at these examples that show the difference between screen size and browser content area.

![Screen size 1024x768](/wp-content/uploads/2006/08/outerwindow-10241.png)\
1024x768 screen resolution gives 1004x598 usable content\
area (maximized Internet Explorer window, Windows XP)

![Screen size 800x600](/wp-content/uploads/2006/08/outerwindow-800.png) 800x600 screen resolution gives only 778x430 usable content area (maximized Internet Explorer window, Windows XP) The figures show that the "browser real estate" available for actual content is smaller. This is what I call "content area". You might notice that browser window height in the screenshots above is smaller than screen size. This is because of the Windows XP task bar that is 30 pixels high in the standard configuration. Likewise, the standard browser toolbar, statusbar, scrollbar subtracts an additional 22x140 pixels. (That's what sometimes is referred to as "browser chrome". So, in general operating system and browser window consumes 22x170 pixels. Does this mean that we're safe if we optimize for 1004x598? Well, not entirely. Jakob mentions that

> screen sizes vary among users. Window size variability is even greater, since users don't always maximize their browsers (especially if they have large screens).

I wanted to take this quote and the other facts from the article and show it in a tabular format:

| Percentage | Screen size       | Maximized window | Max available content area |
|------------|-------------------|------------------|----------------------------|
|            | 640x480           |                  |                            |
| 17%        | 800x600           |                  |                            |
| 60%        | 1024x768          |                  |                            |
| 18%        | 1200x1024 or more | Not always       |                            |
| Total: 97% |                   |                  |                            |

Screen real-estate available for browser. Source: Jacob Nielsen's article *"[Screen resolution and page layout](http://www.useit.com/alertbox/screen_resolution.html)"*. The blank fields show what is not mentioned explicitly in the article.

- Percentage is the users that have the given screen size.
- Maximized window is how likely users are to run browser maximized (no other programs visible)
- Max available content area is the absolute largest area for content visible (when reserved pixels for operating system and browser is subtracted).

My problem is that often people are not using a maximized browser, but a browser window that's actually smaller than the entire screen. An that's why speaking of screen size is irrelevant to other metrics, such as browser content area.

### Browser rarely maximized

18% of all web users who use big screens (above 1200x1024), including me (and most of my web developer colleagues). I also fit perfect on the other finding: I never surf with my browser maximized. Here is what my laptop screen looks like:

<div style="text-align: center">

![Screen size 1400x1050](/wp-content/uploads/2006/08/outerwindow-14001.png)

</div>

1400x1050 screen resolution with a normal Internet Explorer window gives 941x1017 usable content area

Notice that even though I have a wider screen, the actual browser window is smaller than a maximized browser on 1024x768. So to sum this up and fill in the missing data from Jakob's article:

|             | Screen size       | Maximized window | Max available content area |
|-------------|-------------------|------------------|----------------------------|
| 3%          | 640x480           | Always           | 618x310                    |
| 17%         | 800x600           | Always           | 778x430                    |
| 60%         | 1024x768          | Often            | 1004x598                   |
| 18%         | 1200x1024 or more | Rarely           | 1259x853 or more           |
| Total: 100% |                   |                  |                            |

Screen real-estate available for browser, based on findings by Jakob Nielsen with added data by me.

### No stats on browser window size

Unfortunately, I know of no statistics on browser window size. Every major stat company and analytics tool measure screen size. My own experience (by watching people's browsing behavior) follow what Jakob has found. On smaller screens, people tend to maximize browser window. Jakob, I really hope that you update your findings with this adjustment, because it only adds to comfusion especially when working with clients that have not spent their entire working life on the web.

### Proposed update of text

Therefore I decided to update all figures in the article so that it reflects browser content area in stead of window size.

> - **Optimize for *1004x598***, which is currently the most widely used *browser window size*. Of course, the general guideline is to optimize for your target audience's most common resolution, so the size will change in the future. It might even be a different size now, if, say, you're designing an intranet for a company that gives all employees big monitors.
> - **Do *not* design solely for a specific monitor size** because screen sizes vary among users. *Browser* window size variability is even greater, since users don't always maximize their browsers (especially if they have large screens).
> - **Use a liquid layout** that stretches to the current user's *browser* window size (that is, avoid frozen layouts that are always the same size).
>
> *My modified version of Jakob Nielsen's Alertbox "[Screen resolution and page layout](http://www.useit.com/alertbox/screen_resolution.html)", July 31, 2006. My modifications: browser window size instead of screen size.*

I really wanted to put in a smaller number than 1004x598 in order to take the big-screen users into account. However, I really don't know any enough metrics to make a well-argumented decision.

### Conclusion

Web designs should optimize for a maximum available browser window of 1000x600 pixels. As screens get better and bigger, users rarely maximize browser windows, which is why we're probably better off optimizing for a smaller window, such as 900x600. Still, the layout should be liquid so that content fill the users current browser content area, regardless of the size. Also, do not design for a specific browser window size, as it varies between users, especially users with large screens. I'd like to hear your comments on this. Do you know of any metrics or study on browser window size? Any stat tools that actually measure the browser window size? What are your own experience with regards to browser window size that's used? For the user test I have been involved in, every test leader started by maximizing the browser window. That off course would bias any findings with regards to browser window size, so any observations from field studies and similar are welcome.
