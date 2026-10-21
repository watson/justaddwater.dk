---
title: "Dilemma -- Updated Numbers or Long Response Times"
date: "2008-01-11T13:05:12"
slug: "dilemma-updated-numbers-or-long-response-times"
url: "/2008/01/11/dilemma-updated-numbers-or-long-response-times/"
wp_id: 853
categories: ["Performance", "Usability", "User experience"]
tags: []
author: "jesper"
technorati: ["usability", "performance", "user experience", "paypal", "response time"]
---

Paypal showed me this splash screen when logging in:

[![paypal-account-unsync-notice-thumb.png](/wp-content/uploads/2008/01/paypal-account-unsync-notice-thumb.png)](/wp-content/uploads/2008/01/paypal-account-unsync-notice.png "paypal-account-unsync-notice.png")

I think this is a useful design pattern that can be valuable to most of our clients dealing with time-sensitive data.

It is time-consuming for an application to check if there are new payments on every request. This check is better off being uncoupled from the actual user request. Then, the check should be handled backend by a cron job or similar every second, minute, hour or whatever suits the data in the system.

The Paypal example has these advantages:

- Faster response times -- does not wait for a backend account check
- Server less sensitive for extreme load because each request uses less cpu power
- Server can handle more users because each request ends faster

Any other pros or cons you like to add?
