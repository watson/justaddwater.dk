---
title: "Watir: Another sweetspot for Enterprise Ruby"
date: "2006-07-14T11:18:12"
slug: "watir-sweetspot-enterprise-ruby"
url: "/2006/07/14/watir-sweetspot-enterprise-ruby/"
wp_id: 362
categories: ["Businesscase"]
tags: []
---

There are many speculations regarding Ruby (the programming language) and it's ready-ness for enterprise use. The other day, a colleague of mine found an absolutely sweet spot: Automated testing via the browser interface.

[Watir](http://wtr.rubyforge.org/ "Watir: ") stands for "Web Application Testing in Ruby", you write a few lines of Ruby that fires up Internet Explorer, and then clicks around, fills in form fields, submits, etc.

My colleague used a couple of hours to write a few lines to integration test a complex system for a financial customer. He modified it to repeat the same test in three different environments and via timers found out that one of the environments performed very badly.

I saw my colleague demo it yesterday, and both testers and developers present were absolutely impressed by the jar-dropping demo. Comments: "We could have used this much earlier", "Despite that I don't know Ruby, It's easy to understand what it does". Everybody in the project room went around smiling ([David Heinemeier](http://loudthinking.com/ "Loudthinking: David Heinemeier Hansson") would probably say "happy")

It's nothing new that automated browser testing can be done, but when I ask about the alternatives, I'm told that they're too complex to get started with, and sometimes take forever to set up.

Watir gets started with just four lines of code:

    require 'watir'
    require 'watir/WindowHelper'
    include Watir

    ie = IE.new
    ie.goto(test_site) 

In my opinion, Watir + Ruby is a winnner. So easy to get started. So great payoff for a small amount of time invested. Jaw-dropping reactions on developers and testers that don't even know Ruby. It's a definite winner.
