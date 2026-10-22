---
title: "Jef Raskin's First Law of Interface Design Explained"
date: "2009-03-19T15:01:20"
slug: "jef-raskins-first-law-of-interface-design-explained"
url: "/2009/03/19/jef-raskins-first-law-of-interface-design-explained/"
wp_id: 1055
categories: ["justaddwater.dk"]
tags: []
author: "jesper"
---

In variation of Isaac Asimov's first law of robotics, Jef Raskin writes the first law of interface design:

> "Any system shall not harm your content or, through inaction, allow your content to come to harm."

In other words:

Let's say you enter this in an email field: jesperrr#gmail.com

and you get this error message: "not a valid email address"

Then the page reloads and the interface removes all entered text in the email field.

Removing or changing the text (in a harmful way) adds frustration to the end user.

Another example from an old version of our internal Capgemini timereporting (CTR): If you accidentally type "7..5" hours worked on a project a given day, the system will give this error message:

> "You must enter the time as a valid number"
>
> [{{< img src=`/wp-content/uploads/2009/03/ctr-error-no-help-300x104.png` alt=`` title=`ctr-error-no-help` class=`aligncenter size-medium wp-image-1056` width=`300` height=`104` >}}](/wp-content/uploads/2009/03/ctr-error-no-help.png)

Then the application erases the field completely and lets you start over. That's a violation of the First Law of Interface Design. Instead the system should give a more appropriate error message like

> "7..5" is not a recognized time format. Please enter the time in the format "3", "4.0", "7.5" or similar.

Even better, if you can guess what the user actually meant. The new version of the system actually corrects anything like "7..5", "7,.25", "7a", etc to "7" (it truncates anything from the end it does not understand).

Not really perfect to change to "7" if I meant "7.5" or "7.25". So there is still a law violation, although it's smaller than just removing the field content.

## More examples

The worst kind of Interface Law violations are the ones that:

- says "username too short" and deletes the username completely
- says "error in your phone number" and deletes all the other fields so that you have to type everything again
- says "credit card information invalid. type again" and then deletes all entered credit card information
- says "wrong license code" and then deletes the license code field(s)
- says "incorrect captcha" and resets other fields I entered

All these examples fail in user experience because they do not take into account that you most of the time want to correct an accidental typo. The last thing you want is to re-type all the other fields, numbers, characters that were actually correct.

## Exceptions

I think this one is ok if it:

- says "passwords don't match" and deletes both passwords -- passwords are not shown on screen and system does not know if you made a typo in first field or second field

Thanks to Mathias Müller-Prove for giving me the correct quotation. Read more in his short memorial of Jef Raskin "[In Memoriam: Jef Raskin -- User Experience Newsletter \#5, March 2005](http://www.mprove.de/script/05/uxf/newsletter05.html)"

What's your favorite violation the First Law of Interface Design?
