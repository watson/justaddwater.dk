---
title: "CAPTCHA usability: Humane alternative to CAPTCHA"
date: "2006-10-23T15:25:06"
slug: "captcha-usability-humane-alternative-to-captcha"
url: "/2006/10/23/captcha-usability-humane-alternative-to-captcha/"
wp_id: 428
categories: ["Accessibility", "Usability", "Web Standards"]
tags: []
---

Revisiting CAPTCHA: Since W3C wrote about "[inaccessibility of CAPTCHA](http://www.w3.org/TR/turingtest/)" almost a year ago, a new technique has emerged:

Using technology, to make it easier for humans, and challenging for robots to fill out a form, and using a more traditional fall-back method in the rare cases where the system cannot detect if a human is filling in the form.

CAPTCHA is for instance showing an image with distorted text in order to make it impossible for computers to read. The side effect has been problems for people using assistive technology such as blind people using screenreaders.

The problem from an accessibility point of view, is that most CAPTCHAs challenge people just as much as they challenge machines. Sam Ruby [described an alternative](http://www.intertwingly.net/blog/2006/05/30/Captcha-this "Sam Ruby: Captcha this!") back in June:

> I’ve implemented an unusual captcha system.
>
> First, the images are not distorted. In fact, if you have posted to my weblog in the past 90 days, or have visited it within the past week (but more than an hour ago), and aren’t running afoul of the throttle, the display of the image will be entirely suppressed; furthermore, the input field will be pre-filled in for you and hidden.
>
> If you are not recognized, but have JavaScript turned on, DHTML will be used to fill in that input field for you, and that portion of the form will be set to display:none.
>
> In fact, even if you are new, have both JavaScript and images turned off, you will find that the alt attribute of the image will contain the necessary text.
>
> I’m really not targetting humans with this.

So, much of this is learning from usability: **Stop hurting the users!** There are so many problems with traditional CAPTCHAs described already by [me](/2006/01/30/captcha-usability-revisited-google-inaccessible-to-blind-people/), [Roger Johannson](http://www.456bereastreet.com/archive/200512/captcha_is_bad_for_accessibility/), [Peter Krantz](http://standards-schmandards.com/2005/captcha "Standards Schmandards: Proposal for an Accessible Captcha"), [Michael Mahemoff](http://softwareas.com/captcha-impossibillis "Software As She’s Developed: Captcha Impossibillis"), [Bob Easton](http://www.access-matters.com/2005/05/22/quiz-115-did-a-captcha-catch-ya/ "Access Matters: Did a CAPTCHA catch ya"), [Christian Heilmann](http://www.wait-till-i.com/index.php?p=203).

I really like the new and far more usable approach as it still makes it hard for machines, but this time easier for humans.

I just saw that in Microsofts AJAX toolkit for .NET, there is a "NoBot" widget: http://ajax.asp.net/ajaxtoolkit/NoBot/NoBot.aspx

> NoBot is a control that attempts to provide CAPTCHA-like bot/spam prevention without requiring any user interaction. This approach is easier to bypass than an implementation that requires actual human intervention, but NoBot has the benefit of being completely invisible. NoBot is probably most relevant for low-traffic sites where blog/comment spam is a problem and 100% effectiveness is not required.
>
> NoBot employs a few different anti-bot techniques:
>
> \* Forcing the client's browser to perform a configurable JavaScript calculation and verifying the result as part of the postback. (Ex: the calculation may be a simple numeric one, or may also involve the DOM for added assurance that a browser is involved)\
> \* Enforcing a configurable delay between when a form is requested and when it can be posted back. (Ex: a human is unlikely to complete a form in less than two seconds)\
> \* Enforcing a configurable limit to the number of acceptable requests per IP address per unit of time. (Ex: a human is unlikely to submit the same form more than five times in one minute)
>
> NoBot can be tested by violating any of the above techniques: posting back quickly, posting back many times, or disabling JavaScript in the browser.

Very nice work, Microsoft! I'd really like this approach ported to Wordpress (our justaddwater.dk blog software).

Last week we had 1,334 spam comments that were all caught by the Akismet plugin (except for a dozen that we had to remove manually).

Related reading:

- [Blog usability: Avoid spam comments](/2006/06/24/blog-usability-avoid-spam-comments/ "Permanent Link: Blog usability: Avoid spam comments")
- [Blog usability: Avoid spam comments (part 2)](/2006/06/28/blog-usability-avoid-spam-comments-part-2/ "Permanent Link: Blog usability: Avoid spam comments (part 2)")
- [Captcha usability revisited: Google inaccessible to blind people](/2006/01/30/captcha-usability-revisited-google-inaccessible-to-blind-people/ "Permanent Link: Captcha usability revisited: Google inaccessible to blind people")
- Microsoft ASP.NET AJAX controls Toolkit: [NoBot example](http://ajax.asp.net/ajaxtoolkit/NoBot/NoBot.aspx)
