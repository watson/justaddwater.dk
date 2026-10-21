---
title: "Captcha usability revisited: Google inaccessible to blind people"
date: "2006-01-30T16:42:24"
slug: "captcha-usability-revisited-google-inaccessible-to-blind-people"
url: "/2006/01/30/captcha-usability-revisited-google-inaccessible-to-blind-people/"
wp_id: 129
categories: ["Accessibility"]
tags: []
---

*An online petition is being circulated to all Internet users for the purpose of collecting signatures showing support for Google to make its word verification scheme accessible to the blind and visually impaired.*

I just signed up for the request to make Google more accessible. (I'm [number 2759 on the list](http://www.petitiononline.com/mod_perl/signed.cgi?captcha "Google Word Verification Accessibility: Petition signatures")), and [you can sign it too](http://www.petitiononline.com/captcha/ "Sign the Google Word Verification Accessibility Pertition").

> We, the undersigned, ask Google Inc. to "do no evil" and follow their mission statement to "organize the world's information and make it universally accessible and useful" by promptly adding accessibility to their visual word verification scheme so that the blind and visually impaired are allowed to fully participate in all products and services offered by the company on terms of equality with our sighted peers.Sincerely,
>
> [The Undersigned](http://www.petitiononline.com/mod_perl/signed.cgi?captcha)


### What Google does wrong

The problem is that it requires vision to see what's the word/text in the word verification (captcha). Purpose of captcha is to tell machines and humans apart, and can prevent machines from creating accounts that for instance spammers and phishers can abuse. [More about captcha Wikipedia](http://en.wikipedia.org/wiki/Captcha "Wikipedia.org: Captcha").

Here is what Google does in the sign-in process:

[![screenshot of the google account signup captcha](/wp-content/uploads/2006/01/screenshot-google-captcha.png)](/?attachment_id=124 "screenshot of the google account signup captcha")

Clicking on the wheelchair icon reveals a popup-window that shows the same image in a separate window.

The [press release from Blind Access Journal](http://www.prweb.com/releases/2006/1/prweb333502.htm "Press release: Google asked to make its visual word verification accessible") tell us that this is wrong and will block blind users, because it…

> …currently locks the blind and visually impaired out of participation in all the company's services. Google’s implementation of word verification currently denies us access to such important features as the ability to create accounts and blogs, change our passwords, and post comments to most blogs that use the Blogger service. Accessible solutions to visual verification have already been put in place by such companies as America Online, Microsoft, PayPal and SpamArrest.We ask Google to follow this lead with an audio playback implementation now, followed by the creation of new innovative approaches that meet the needs of all users, including the deaf-blind population.


### What Google should do

Recently, Peter Kranz of Standards Schmandards wrote a terrific overview different accessibility problems with captcha and came up with a [proposal for an accessible captcha](http://standards-schmandards.com/index.php?2005/01/01/11-captcha "Standards-schmandards: Proposal for an Accessible Captcha").

![standards-schmandards-captcha](/wp-content/uploads/2006/01/standards-schmandards-captcha2.gif)

> Some of the [solutions proposed in the W3C article](http://www.w3.org/TR/turingtest/#solutions) are:\
>
> 1.  \
> 2.  Use logic puzzles. This solution does not satisfy requirement 2. It would require someone to manually create these tests. Also, they would probably be difficult if you have a cognitive impairment.
>     \
> 3.  Use credit card validation. Brilliant idea. Everyone would be happy to submit their credit card number to unknown sites on the internet.
>     \
> 4.  Live operators. Fails on cost efficiency. Although it would be one of the best ways to provide support for your users, a lot of sites do not have the resources to provide this kind of service.
>     \
> 5.  Federated identity systems. Well, this does not exist yet so we can not use it.
>     \
> 6.  Sound output. If it could be possible to create a sound file that was difficult to decode for a machine, this may be the best option to use together with a regular captcha image. Let's move forward with this solution.
>     \
>
> \
> First of all I suggest that you thoroughly evaluate *why* you need a captcha. Is it really necessary? A lot of sites implement them because it "looks professional". If you can avoid captchas, please do so.
>
> My proposed solution is based on an ordinary captcha image in combination with an audio based test. Instead of providing the same information in the audio file as in the test image (like the [Hotmail registration form](http://www.hotmail.com/)) we will use a separate test. This test is based on the ability of the human brain to understand the meaning of information as well as discard unnecessary details.

An audio file as an alternative to the image. And this is exactly what Blind Access Journal proposes in the text for the petition. If you want to help, I think you can help both Google and blind internet users by [signing the petition](http://www.petitiononline.com/captcha/ "Sign the Google Word Verification Accessibility Pertition").
