---
title: "How to indicate required or optional form fields"
date: "2006-03-29T17:50:33"
slug: "how-to-indicate-required-or-optional-form-fields"
url: "/2006/03/29/how-to-indicate-required-or-optional-form-fields/"
wp_id: 199
categories: ["Accessibility", "Best of Justaddwater", "Forms", "Usability"]
tags: []
author: "thomas"
---

I got [a question from Kimberly](/2005/12/23/sensible-forms-a-form-usability-checklist/#comment-2039), one of our reader, in the [Sensible Forms: A Form Usability Checklist](/2005/12/23/sensible-forms-a-form-usability-checklist/) post where she asks where the best place to display the asterisk indicating a required field in af form is:

> \[...\] I’d like to see the askterick appear before the label so that a user isn’t forced to read every label or field and can simply look for the askterick. What do you think?

The short answer is: **It depends on the graphical design as long as you remember the disabled users.**

I would like to say that there is generally two ways of showing required and optional fields:

1.  Grouping required and optional fields in different groups (fieldsets)
2.  Indicating next to each field or label if this field is required or not

There can be many design reasons why one of the above ways can't be used in a given situation. So I will not say that one should always be used instead of another (even though design should never out-rule usability!), but there is still drawbacks and benefits with both versions.

The general rule should of cause be that whatever version is used, disabled users should have just as fair a chance as normal users to see which fields that are required and which that isn't. This is a highly difficult subject with lots of ifs, buts' and maybes and you have to take the different groups of people into account:

1.  People using a screen reader (mostly blind people)
2.  People using a magnifying glass (electronic or IRL)
3.  Non-disabled people (the rest of us)

On this subject I find the guide "[Required Form Fields](http://simplyaccessible.org/examples/required-form-fields "Simply Accessible: Required Form Fields")" from Simply Accessible very useful. Remark: If you use the trick with showing the asterisk to the right of the field even though it is physically located inside the label, you just have to remember that this doesn't help people that depend on a magnifying glass, since they won’t necessarily see what's located all the way to the right.

Another point could be that if you use actual words like "required" or "optional" a screen reader would say these out loud giving a clear indication to the blind user. Using an image of an asterisk with the word "required" inside the "alt" attribute could also be a solution since I would imagine that most screen readers read "alt" attributes out loud as well. On the other hand **using bold to indicate a required field might create issues with screen readers** since there is no textual indication that a given field is required.

### Examples: Grouping required and optional fields

Many popular websites take this approach. Of a few can be mentioned:

- [The New York Times](http://www.nytimes.com/gst/regi.html "The New York Times: Free Registration") [![The New York Times - Grouping required and optional fields into groups](/wp-content/uploads/2006/03/nytimes-grouping-fields.thumbnail.png "The New York Times - Grouping required and optional fields into groups")](/wp-content/uploads/2006/03/nytimes-grouping-fields.png "The New York Times - Grouping required and optional fields into groups") Click on thumbnail to see larger image
- [All phpBB forums](http://www.phpbb.com/phpBB/profile.php?mode=register&agreed=true "phpBB.com: Register")
- [LinkedIn](https://www.linkedin.com/register "LinkedIn: Join LinkedIn")
- [Basecamp](https://secure.basecamphq.com/signup/Free "Basecamp: Sign up") by 37signals
- [Freshmeat](http://freshmeat.net/register/ "freshmeat.net: User Registration")

Some even have different pages for each group of fields creating a wizard like effect ([Amazon](https://www.amazon.com/gp/flex/sign-in/select.html/103-6445861-7965411?%5Fencoding=UTF8&protocol=https "Amazon: Sign In/Up") for one)

### Examples: Indicating next to field or label if required

This category is a bit more diverse. You can imagine an endless amount of different ways to indicate that a specific field is required, or you can turn the tables around and indicate that a field is optional. There generally is 3 popular ways of doing this:

1.  Asterisk next to either label or field marking the field as required: [Yahoo](https://edit.yahoo.com/config/eval_register "Yahoo! Registration") ![Yahoo! Registration - Asterisk before label](/wp-content/uploads/2006/03/yahoo-form-asterisk-before-label.png) [IBM](https://www-132.ibm.com/webapp/wcs/stores/servlet/UserRegistrationForm "IBM: Create an account") ![IBM Create Account - Asterisk before label](/wp-content/uploads/2006/03/ibm-form-asterisk-before-label.png) [The Washington Post](http://www.washingtonpost.com/ac2/wp-dyn?node=admin/registration/register&destination=register&nextstep=gather&application=reg30-globalnav "The Washington Post: Register") ![The Washington Post Register - Asterisk before label](/wp-content/uploads/2006/03/washingtonpost-form-asterisk-before-label.png) [Spread Firefox](http://www.spreadfirefox.com/user/register "Spread Firefox: Register") ![Spread Firefox Create Account - Asterisk after label](/wp-content/uploads/2006/03/spreadfirefox-form-asterisk-after-label.png)
2.  Bold label marking the field as required: [Technorati](http://technorati.com/signup/ "Technorati: Sign Up") ![Technorati - Bold is required](/wp-content/uploads/2006/03/bold-is-required2.png)
3.  The word "optional" or "required" in brackets next to either the field or the label: [Bugzilla](https://bugzilla.mozilla.org/createaccount.cgi "Bugzilla: Create account") ![Bugzilla Create Account - The word optional after the field](/wp-content/uploads/2006/03/bugzilla-form-optional-after-field.png) Here all labels are bold and does not mean that the field is required! [Wikipedia](http://en.wikipedia.org/w/index.php?title=Special:Userlogin&type=signup&returnto=Main_Page "Wikipedia: Create account") ![Wikipedia Create Account - The word optional after label](/wp-content/uploads/2006/03/wikipedia-form-optional-word-after-label.png) Here the asterisk actually means something else than "required"!

### Conclusion

Looking at the examples that use an asterisk to indicate a required field it's clear that common practice is to **color the asterisk in a different color than the text in the label**. All of my examples above use a shade of red to do this. The color red has a special effect on the human brain so that it is noticed before other colors and given a stronger weight. As a non-disabled user I prefer to quickly skim a form to get an idea of which fields I am required to fill out. Using the red color helps me do this. *UPDATE: Brian Crescimanno has brought an important fact to my attention which he also wrote about in [his A List Part article](http://www.alistapart.com/articles/sensibleforms "A List Part: Sensible Forms - A Form Usability Checklist"):*

> *I advise against using the color red to denote required fields, because red most often indicates an error or warning. \[...\] so pick a color that will not be confused with error messages.*

I would **always try to group form fields into fieldsets** so required and optional fields are separated - remember to clearly state if a group is required or not. If this isn't possible due to design or logical issues I would use the word "optional" (or "required" - whatever makes the most sense) in brackets next to the label. My last option would be to use asterisks if using actual words would be a design issue.

I would **never use bold to indicate required fields** since this potentially could cause misunderstandings with people using screen readers. I would **never show a required/optional indication to the right of the field** - always next to the label.
