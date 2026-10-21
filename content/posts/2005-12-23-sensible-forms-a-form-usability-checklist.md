---
title: "Sensible Forms: A Form Usability Checklist"
date: "2005-12-23T00:37:12"
slug: "sensible-forms-a-form-usability-checklist"
url: "/2005/12/23/sensible-forms-a-form-usability-checklist/"
wp_id: 49
categories: ["Forms", "Usability"]
tags: []
---

I heard [via WebWord](http://www.webword.com/2005/12/22/sensible-forms-a-form-usability-checklist/) that A List Apart had [an interesting article on form usability](http://www.alistapart.com/articles/sensibleforms). It is a very good article that's definitely worth a read. Below is just my comment to the article and my own thoughts on the subject form usability.

### Give them room to type

First want to say that I especially relate to the point on giving the users room to type:

> Just because your name is Joe Tod doesn’t mean other users won’t need more space to enter their names.

I have been filling out many forms just to find out that the e-mail address that I type in is longer then the maximum size of the e-mail field. Ok, yes - I know that I sometimes use long e-mail addresses, but since I don't like getting spam I bought a domain which I fitted with a catch-all e-mail address. Then when I visit a site that requires me to leave an e-mail address that I don't plan to visit ever again, I just type in something like\
*www.somestupidwebsite.com-2005.22.12@my-spam-domain.com*\
Anyway... my point is that some people have long names. And why should you not want the French Hélie Denoix de Saint Marc form Wales with the e-mail address\
*helie.denoix.de.saint.marc@llanfairpwllgwyngyllgogerychwyrndrobwyll-llantysiliogogogoch.com*\
as your costumer?

### Validation

Which bring me to the second issue on my I-hate-stupid-form-designers list - wrong validation:\
\<rant\>I've seen a few forms where the developer though he had all the facts on valid characters in a domain-name (or the whole e-mail address for that fact). I don't want a form telling me that my e-mail address isn't valid because it doesn't like the hyphens in my domain name!\</rant\>

### Borders (not the graphical, but the physical ones)

Besides all the great points that this article makes, there is one that it misses completely (and I'm probably gonna get some bad comments on this one):\
**USA ≠ The Internet**

As a non-US citizen I can't make this point often enough. Some US websites whose audience extends the physical borders of USA forget that it can be very difficult for a user that doesn't live inside the US to fill out the required choose-your-state select-box. Either provide the user with a country select-box and use some JavaScript to make the state select-box dimmed when the user chooses another country than USA or provide a "I live outside the USA" option as part of the state select-box (I personally like the first option).

The article also mentions asking for the user's telephone number (e.g. 800 555-1212) and that one possible option is to split the telephone number input into three fields. But what about me? Danish telephone numbers is just 8 plain digits following each other without any fancy spaces or hyphens. Of cause I would probably also like to provide a county code (+45 for Denmark), but I've seen countless examples of websites that either:

- Does not allow for a + (plus) in the telephone number and gives me an error when I try to submit (I can fix this by writing 0045 instead).
- Strips the + of the beginning of the telephone number just before it saves it into its internal database without giving me the chance to change the + to 00 (two zeros). This in turn leaves owners of the website with an invalid telephone number.
