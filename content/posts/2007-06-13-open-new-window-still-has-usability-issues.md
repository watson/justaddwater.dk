---
title: "Open New Window Still Has Usability Issues"
date: "2007-06-13T10:34:04"
slug: "open-new-window-still-has-usability-issues"
url: "/2007/06/13/open-new-window-still-has-usability-issues/"
wp_id: 673
categories: ["Usability"]
tags: []
author: "jesper"
technorati: ["popup", "popup window", "usability", "jakob nielsen", "sitepoint", "neil turner", "thickbox", "flickr", "organizer"]
---

Open new windows is a no-no for several reasons. Frequently readers probably know this already, but since I'm often seeing this on Danish web pages, I think it's time to reopen the discussion with new considerations.

> - Unless you warn them, Web users are likely to expect the new page to load in the current window. Unexpected surprises can be fun, but not when you're browsing the Web.
> - The act of opening a new browser window resets the back button in that window. The back button is the second most used navigation function (after hyperlinks, source: [useit.com](http://www.useit.com/alertbox/990530.html)), so resetting it is a big no-no.
> - To open a new browser window can disorient very novice Web users and the visually impaired. They might not realise that a new window has opened and might struggle to switch between windows.
> - Opening a new browser window disrespects the desires of your users. If they want a new window, they'll ask for one. Don't force a new window upon users unless there's a very good reason to do so.

Source: Neil Turner, Sitepoint "[Beware of Opening Links in a New Window](http://www.sitepoint.com/article/beware-opening-links-new-window)"

I would add two reasons to this list.

- Current browsers handle new windows differently than just a few years ago. This means that you may not clutter the task bar with new items. In stead, most windows that users don't explicitly request are opened in tabs. Just a blink with the eyes or a head turn is enough to miss the fact that a new tab was opened, the browser history is reset, and back button does not work.
- Browser toolbars with popup blockers tend to become widespread and used as default installations by some corporations (I have seen a few examples of this recently).

Web developers can overcome this latter obstacle by avoiding certain constructs in the code, but overall, using popups on your website increases the risk of having users not able to use your application.

Nevertheless I have often found myself recommending popups in some web applications. But recently, I found that so-called lightbox dialogs can replace the popup.

I see one place for using popup windows or lightboxes: You want to make a page less cluttered and hide away advanced functionality that's related to that one page. The advanced functionality could fit in a separate dialog so you can fill that in and then return to the main page. An example of this is the [Flickr Organizer](http://www.flickr.com/organizer/) where most of the detailed manipulation of photos is done in lighboxes.

Popups: Think hard \&mdash; very hard \&mdash; before you decide to use it. Resist any urge, and use a lightbox window in stead. Users can open their own windows, and [current browsers let users decide whether to open in same window, new window or new tab](/2007/06/13/same-new-window-or-tab-let-users-decide-themselves/ "Justaddwater.dk: Same, New Window, Or Tab? Let Users Decide Themselves").

More info:

- Sitepoint: [Beware of Opening Links in a New Window](http://www.sitepoint.com/article/beware-opening-links-new-window) (2004)
- Jakob Nielsen: [Open New Windows for PDF and other Non-Web Document](http://www.useit.com/alertbox/open_new_windows.html) (2005)
- [Thickbox](http://jquery.com/demo/thickbox/) (a lightbox add-on JavaScript library)
- Justaddwater.dk (sidebar): [Same, New Window, Or Tab? Let Users Decide Themselves](/2007/06/13/same-new-window-or-tab-let-users-decide-themselves/ "Justaddwater.dk: Same, New Window, Or Tab? Let Users Decide Themselves")
