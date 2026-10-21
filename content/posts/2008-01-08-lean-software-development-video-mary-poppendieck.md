---
title: "Lean Software Development Video Mary Poppendieck"
date: "2008-01-08T19:58:36"
slug: "lean-software-development-video-mary-poppendieck"
url: "/2008/01/08/lean-software-development-video-mary-poppendieck/"
wp_id: 848
categories: ["Agile", "Productivity", "Video"]
tags: []
author: "jesper"
---

Here are some great examples i jotted down when watching Mary Poppendieck's presentation at Google: "[Competing on the basis of speed](http://video.google.com/videoplay?docid=-5105910452864283694)". See my notes below.

Complexity kills speed: Windows 95 took 350 developers, Vista took 3500 developers

Make sure your project anticipates change:\
60-80% of all software is developed after first release to production

Defer commitment.Wait till the latest possible moment to make the commitment. This makes sure you base your decision on the best information available. Example: Toyota develops 10 parallel motors for a given project and only 9-10 months before production, they take the decision which one to use in the final car.

Make sure you can refactor and make decisions reversible. When you have irreversible decisions, make them as late as you possibly can.

Irreversible decisions scheduled to be made at the last responsible moment. Just like a pilot flying into a foggy airport. He makes the decision to pull up if he can't see the ground at a certain point. Not before or later.

Multiple decision must be available at the decision point. The paradox is that this is not a waste. (Toyota example approx 16:00 in video).

Printer example: poor or good red-eye reduction algorithm? The good will sell 100,000 printers more but not sure it will make it on time. Solution: **Do both**. Tell management. We will have red-eye reduction. After a few months we'll release a new version which can sell 100,000 extra. If we're lucky, we'll be able to have it built-in at first release.

You will be amazed how much faster you go when you make stuff where the defects are stopped the minute when they occur instead of later. (21:30).

Find defects immediately is essential to build test into development process. Test easy to automate.

Anything that makes code difficult to change is debt. (corresponds with 37Signals Getting Real definition of debt). complexity is potential. Regression deficit adds a little more until it dominates the release cycles. Solution is to automate acceptance testing.

Code branches: The longer they're apart, the harder it is to bring them together.

Example car paint booths (31:00).

If you're putting more and more stuff together because it's so hard to release to production, you are going the wrong way. The objective is "one piece flow".

Constantly focus on rapid deployment of small feature sets.

Deployment ready code: People doing anti-virus programs have a release cycle of about 48 hours from they start until it's on my computer.

It used to work. It worked 5 minutes ago. I checked in, now it doesn't work. Guess what caused the error. It's so much easier to figure out the moment the error occurs, just stop.

Software development cycle time. From customer problem to customer solution: Where are the delays?

Queing theory: How many have a list of things todo that are longer than you can possibly do? So, why bother to keep track of the things (waste)

Total cycle time = Number of things in process / average completion rate\
(Little's Law)

If you have large batches, You are going to start slowing down at around 50% utilization rate. If you have small batches, you start slowing down at around 80 or 85% utilization. (49:00)

This applies to both servers as well as people.

Have slack or spare time: Invented at 3M.

1.  Even out the arrival of work\
    Annual planning.. approval process (makes batches bigger).
2.  Minimize the number of things in process\
    Minnesota doctors. 60 days to 2 days. Stopped accepting appointments for patients.\
    Todo lists: Dealing with old problems.\
    Never ever accept more work than you do.
3.  Minimize the size of things in process\
    small rather than big
4.  Establish a recular cadence\
    2 or 4 week release cycles.
5.  Limit work to capacity\
    1 or 2 cycles in your queue (3 or 6 slots in your work queue)

You do not need long lists. You aren't gonna get to it, so why fool yourself? There is a bigger cost probably associated with them thinking it gets done and it doesn't.\
System measurements

1.  Average cycle time\
    from feature request to feature deployment (or similar)
2.  Business case\
    Are you making money? Are you delivering on that thing?
3.  Customer satisfaction\
    Sustainability on a long term.
