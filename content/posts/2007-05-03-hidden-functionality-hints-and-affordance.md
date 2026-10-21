---
title: "Hidden Functionality — Hints And Affordance"
date: "2007-05-03T13:29:20"
slug: "hidden-functionality-hints-and-affordance"
url: "/2007/05/03/hidden-functionality-hints-and-affordance/"
wp_id: 618
categories: ["Usability", "User Interface"]
tags: []
author: "jesper"
technorati: ["usability", "progressive disclosure", "affordance", "hints", "hidden functionality", "examples"]
---

Many of today have extremely advanced features and functionality. But the trend towards simpler, slicker user interfaces points towards hiding some of the functionality. Hiding functionality is — in my point of view — a very good thing for usability.

A usable website (or application) is:

- easy to use
- easy to learn
- hard to make errors in

Jakob Nielsen wrote about how hiding functionality is actually good for usability. The principle is called **progressive disclosure**, and presumes that you hide stuff that you don't use often, which makes it easier to find stuff that you use all the time.

Another interesting term is **affordance which means "an aspect of an object which makes it obvious how the object is to be used"** (definition from the HCI dictionary).

So making functionality scream to the user is one thing. The most frequently used functions on the website must be the easiest to find.

Let's see some real life examples of how affordances are shown for functionality that is hidden or less discoverable.

### Google mail hidden functionality

[![screenshot-gmail-callout.png](/wp-content/uploads/2007/05/screenshot-gmail-callout.png)](/wp-content/uploads/2007/05/screenshot-gmail-callout.png "screenshot-gmail-callout.png")

Here, functions to reply, forward, delete, print and more are put in a dropdown (actually an element designed to look like a dropdown).

### Amazon.com add tags to a product

Tagging is one of amazons initiatives to [add interactive features](http://bokardo.com/archives/how-social-is-amazon/) on the product pages. The interesting part in this context is the little help text below the tagging field.

[![amazon-participation-tag-item-affordance.png](/wp-content/uploads/2007/05/amazon-participation-tag-item-affordance.png)](/wp-content/uploads/2007/05/amazon-participation-tag-item-affordance.png "amazon-participation-tag-item-affordance.png")

The text hinting the functionality is visually less significant below the tag field:

> (press the 'T' key twice to quickly access the "tag this product" window)

This opens the tag dialog with "advanced" features as seen below. Note that the primary functionality here is to add one or more tags. That's actually already accessible from the main page (screenshot above). But to edit existing tags is only available in the dialog (that is if you press 'T' twice).

[![amazon-participation-tag-item-dialog.png](/wp-content/uploads/2007/05/amazon-participation-tag-item-dialog.png)](/wp-content/uploads/2007/05/amazon-participation-tag-item-dialog.png "amazon-participation-tag-item-dialog.png")

Amazons product page is extremely long ( 6,500 pixels for this product). It can be hard to locate the "tag this product" feature on the page. In this case, users that want to add tags can now easily use that functionality just by pressing 'T' twice.

Of course, this requires learning the keyboard shortcuts. But it's an interesting tradeoff between hiding advanced features, yet making it instantly available to expert users.

### Google Personalized Homepage drag and drop

[![google-ig-dragrop-affordance-thumbnail.png](/wp-content/uploads/2007/05/google-ig-dragrop-affordance-thumbnail.png)](/wp-content/uploads/2007/05/google-ig-dragrop-affordance.png "google-ig-dragrop-affordance.png")

At first visit on the personalized homepage, there is a hint that it's possible to rearrange the boxes. The screenshot shows the text that is only shown as long as you have not dragged anything. As soon as you have demonstrated that you can use drag and drop, the text hint will disappear.

### Google mail autosave

GMail has an example on functionality that is hidden but nevertheless very useful. All emails get autosaved while editing. The only visual indication of the functionality appears after (and during) the autosave:

[![google-mail-autosave-thumbnail.png](/wp-content/uploads/2007/05/google-mail-autosave-thumbnail.png)](/wp-content/uploads/2007/05/google-mail-autosave.png "google-mail-autosave.png")

In this situation, there is actually no affordance of the functionality, it just appears. The key to this is to **make sure the action is unobtrusive** and does not get in the way of the user. Actually, GMail has many examples of hidden actions with no visual clue: **CTRL+S** saves the text, and I use the shortcut all the time.

Tomorrow, I'll dig into more examples about affordances of autocomplete text boxes.

### More related info:

- Justaddwater.dk: Affordance in autocomplete fields (will be published tomorrow)
- Jakob Nielsen: Progressive Disclosure
- Google search on [definition of affordance](http://www.google.com/search?q=define%3Aaffordance): [Wikipedia:Affordance](http://en.wikipedia.org/wiki/Affordance), [HCI dictionary: affordance](http://ei.cs.vt.edu/~cs5714/glossary.html)
- Andy Ruthledge: [No instruction necessary part 1](http://www.andyrutledge.com/no-instruction-necessary-part1.php) (about affordance)
- Interaction design encyclopedia: [Affordances](http://www.interaction-design.org/encyclopedia/affordances.html)
