---
title: "The Quick Way to Creating Disabled State Icon With Photoshop"
date: "2009-08-28T22:57:58"
slug: "the-quick-way-to-creating-disabled-state-icon-with-photoshop"
url: "/2009/08/28/the-quick-way-to-creating-disabled-state-icon-with-photoshop/"
wp_id: 1124
categories: ["Web Development"]
tags: []
---

For an internal demo, I had to make my own disabled and :hover states of some buttons.

In Photoshop (Elements) it was dead easy by adjusting the color in each layer.

I found that the following settings worked very well:

In Photoshop, create a new layer for each button state. Select the layer and choose "Enhance" \> "Adjust Color" \> "Hue/Saturation"

**Disabled state background-image:**

- Saturation: -80
- Lightness: +40

![photoshop-elements-saturation-for-disabled-buttons](/wp-content/uploads/2009/08/photoshop-elements-saturation-for-disabled-buttons-300x184.png "photoshop-elements-saturation-for-disabled-buttons")

**Hover state background-image:**

- Saturation: +15

You have each icon defined now with several states in the same file. Perfect for using the [CSS sprites technique](http://www.alistapart.com/articles/sprites "A List Apart: CSS Sprites (2004) by Dave Shea") for showing them as background images on the buttons.

The final result:

![buttons-rejected-normal-state](/wp-content/uploads/2009/08/buttons-rejected-normal-state.png "buttons-rejected-normal-state")

What are your best settings for this type of task?
