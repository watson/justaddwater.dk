---
title: "Affordance of Autocomplete Text Fields"
date: "2007-05-05T15:45:38"
slug: "affordance-of-autocomplete-text-fields"
url: "/2007/05/05/affordance-of-autocomplete-text-fields/"
wp_id: 626
categories: ["Usability", "User Interface"]
tags: []
---

In my opinion, the autocomplete input boxes have a very low discoverability because they're basically just textfields with added JavaScript.

**Google Suggest's** interface has an added line of text trying to explain and to make it easier to discover the \_hidden\_ functionality: "As you type, Google will offer suggestions. Use the arrow keys to navigate the results. Learn more":

[![google-suggest-affordance-text.png](/wp-content/uploads/2007/05/google-suggest-affordance-text.png)](/wp-content/uploads/2007/05/google-suggest-affordance-text.png "google-suggest-affordance-text.png")

And as soon as you start typing, the results will appear as shown below:

[![google-suggest-thumbnail.png](/wp-content/uploads/2007/05/google-suggest-thumbnail.png)](/wp-content/uploads/2007/05/google-suggest.png "google-suggest.png")

**Another example is Amazon's "tag this product feature"**. As I wrote previously, it has affordance as to which keyboard shortcut can show the dialog. But as you type in the field, there is no hints to make it obvious that this field can magically help the user by autocompleting.[\
](/wp-content/uploads/2007/05/google-suggest-affordance-text.png "google-suggest-affordance-text.png")[![amazon-participation-tag-item-affordance.png](/wp-content/uploads/2007/05/amazon-participation-tag-item-affordance.png)](/wp-content/uploads/2007/05/amazon-participation-tag-item-affordance.png "amazon-participation-tag-item-affordance.png")

# [![amazon-participation-tag-autocomplete-without-affordance.png](/wp-content/uploads/2007/05/amazon-participation-tag-autocomplete-without-affordance.png)](/wp-content/uploads/2007/05/amazon-participation-tag-autocomplete-without-affordance.png "amazon-participation-tag-autocomplete-without-affordance.png")

(totally unrelated, i suddenly feel very curious about what products are tagged with "cannibalism"...)

**Kayak.com also has autocomplete fields** in case you foroget that airport code. Which is actually cool, but again not hints before you start.

[![kayak-com-autocomplete-without-affordance-or-hints-thumbnail.png](/wp-content/uploads/2007/05/kayak-com-autocomplete-without-affordance-or-hints-thumbnail.png)](/wp-content/uploads/2007/05/kayak-com-autocomplete-without-affordance-or-hints.png "kayak-com-autocomplete-without-affordance-or-hints.png")

**Yahoo!s Design Pattern Library** has [one autocomplete example](http://developer.yahoo.com/ypatterns/pattern.php?pattern=autocomplete) from the recent Yahoo! Mail beta:

[![Auto completion of contacts in Yahoo! Mail Beta](http://developer.yahoo.com/ypatterns/images/pattern_autocomplete_ani.gif)](http://developer.yahoo.com/ypatterns/pattern.php?pattern=autocomplete)

The screenshot used for example has no affordance to hint the hidden functionality. There is also nothing describing the availability of automplete functionality.

**Outlook and Excel** have sort of autocomplete as well. But compared to the examples above (where suggestions appear if you hesitate typically a second), then the suggestions appear immediately.

**Is it good enough to have no visual indication**? Hardly. I would like to see a general consensus around how to visually indicate autocomplete fields in a way that makes it intuitively clear what functionality is hidden in the field.

Back in January last year, I wrote about ["live search" in user interfaces](/2006/01/26/live-search-explained/ "Justaddwater.dk: Live search explained (2006-01-26)"), with examples from Google Suggest, GMail, Apple Spotlight, Windows Vista and more. But neither of the ones I looked at had any visual indication of the fields that could indicate that the field was different from an ordinary text field.

### Problems related to unhinted functionality

The problem with this approach where the functionality is not hinted is that I believe that it will change your behaviour and usage pattern. An ordinary text field is just a field and you need to fill it in exactly as it's needed. That usually requires that you stop and think before filling in the field.

The autocomplete field can help you — but only if you hesitate after writing something for a start. I would say that this behaviour requires less brain activity and perhaps a quicker fill in of the form fields.

But the efficiency can only be achieved after you have learned that this is an autocomplete field. In some of the above examples, users would typically discover the autocomplete functionality with some sort of surprise. Suddently the field gives you suggestions.

But surprise and confusion are closely related. So I'd guess that it might confuse less trained users. My point here, i guess, is that there is no reason to confuse people. Just make sure that the functionality is properly hinted.

So we need more than just text for the autocomplete fields to stand out.

### Next step

In a couple of days, I'll continue this post with some guidelines for autocomplete fields. (I wanted to write "tomorrow", but I'm afraid to make a promise I cannot keep — like I did in last post).\
Please post your comments about good and bad examples, as I desperately need more examples for how to make these. Any usability testing results that you heard of? Any other thoughts?

Related info:

- \
- IxDA Discuss: [Affordance on autocomplete input boxes](http://lists.interactiondesigners.com/htdig.cgi/discuss-interactiondesigners.com/2006-July/010573.html)
  \
- Justaddwater.dk: [Hidden Functionality — Hints And Affordance](/2007/05/03/hidden-functionality-hints-and-affordance/ "Justaddwater.dk: Hidden Functionality — Hints And Affordance")
  \
- Justaddwater.dk: [Live search explained](/2006/01/26/live-search-explained/ "Justaddwater.dk: Live search explained (2006-01-26)")
  \
- Wikipedia: [Hidden Find](http://en.wikipedia.org/wiki/Incremental_find)
  \
- Bill Scott: [D](/wp-admin/%20Distracting%20or%20Narrowing:%20Looking%20a%20Little%20More%20At%20Live%20Search)istracting or Narrowing: Looking a Little More At Live Search[D](/wp-admin/%20Distracting%20or%20Narrowing:%20Looking%20a%20Little%20More%20At%20Live%20Search)
  \
- Yahoo! Design Pattern Library: [Autocomplete pattern](http://developer.yahoo.com/ypatterns/pattern.php?pattern=autocomplete "Yahoo design pattern library: Autocomplete pattern")
  \
