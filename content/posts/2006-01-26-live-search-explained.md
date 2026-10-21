---
title: "Live search explained"
date: "2006-01-26T12:04:15"
slug: "live-search-explained"
url: "/2006/01/26/live-search-explained/"
wp_id: 115
categories: ["Best of Justaddwater", "Usability"]
tags: []
---

Trend: Live search will gradually replace traditional search in web applications. As mainstream programs such as Windows Vista matures up to release, and live search is deeply integrated, we can expect more web pages implementing live search. Apple's Spotlight and MSN Desktop Search uses the same Live search paradigm that we'll probably see a lot more in the year to come.

My post from yesterday has more on different examples of [live search usage](/2006/01/25/windows-vista-setting-new-standards-for-find-as-you-type-searching/ "Justaddwater.dk: Windows Vista setting new standards for Find-as-You-Type searching"). Let me just explain the difference between live search and traditional search.

**Traditional search**: A search user interface component consists of a text field and a "search" button. User types and when finished typing, he presses "search". Then the results are displayed. If user misspells a word or does not find any useful results, then user must correct search term in input field and press "search" button again.

Problems here involve that people often misspells words. Google registered [593 ways of spelling Britney Spears](http://www.google.com/jobs/britney.html "Google.com: Britney Spears spelling correction"), and a study (that we [mentioned earlier](/2005/12/04/on-site-searching-still-stinks/ "Justaddwater.dk: On-Site Searching Still Stinks")) showed that [3% of all searches are misspelled](http://www.uie.com/articles/search_stinks/ "UIE.com: Why On-Site Searching Still Stinks"). (I wonder if that number has raised since 1997). Jakob Nielsen found that only [51% find what they're looking for in the first search](http://www.useit.com/alertbox/20010513.html "Useit.com: Search, Visible and Simple (Alertbox May 13, 2001)").

That concludes that users are likely to refine results when searching. Refining results multiple times can be tedious using traditional search.

**Live search**: The search user interface is identical to traditional search. But results are fetched whenever the user "hesitates" — for instance stop typing for a brief moment. An example of this is [Google Suggest](http://www.google.com/webhp?hl=en&complete=1 "Google labs: Google suggest") where the most popular results are presented as-you-type.

[![Google suggest autocomplete feature](/wp-content/uploads/2006/01/screenshot%20google%20suggest.thumbnail.png)](/2006/01/25/windows-vista-setting-new-standards-for-find-as-you-type-searching/google-suggest-autocomplete-feature/ "Google suggest autocomplete feature")

The user experience is very different that traditional search: Here you type, hesitate, and get results. This has some benefits:

- Relevant alternatives are presented as you type, so the best match can be picked immediately.
- Its easy to refine your search: Just continue typing
- If the search typed is too narrow its easy to press backspace and remove characters.
- In the better implementations (like Google Suggest above), the best match is highlighted in the input field. In this way, the user can press "enter" and immediately go to the content page. Traditional search involves an extra click on the results page.

**Live search can be a big time saver for a user**, especially considering that at 49% of all searches will be refined. Furthermore, misspellings can be corrected immediately (there is no need to wait until the results show up.

Any system designer should consider it, given the performance advantages it can give for the end user. On the downside, live search requires more processing power as multiple searches are performed every second (depending on setup of course).

Bill Scott of Yahoo has described Kayak.com (travel site) autocomplete:

> Kayak.com is a good example of live auto complete. Say the user is wanting to fly into New York city. They seem to remember that the airport they want is called LaGuardia (not sure how to spell it or what the airport code is). When I type 'New Y' I get the following results:
>
> ![kayak-auto-complete-LGA.png](http://static.flickr.com/34/71871872_e922cab3cc_o.png)
>
> Ok, this is nice. I hate remembering the airport code. And I hate having to go to another page to find out that the site could not figure out what I meant. Jakob Nielsen states as one of his ten usability principles, Error Prevention. Providing the feedback instantaneously to cue me to what the system thinks is great. Saves me time and makes me feel like I am narrowing in on the right thing. This probably ties in with Jared Spool's research on [The Confidence Game](http://www.uie.com/brainsparks/2005/10/20/brain-sparks-live-the-confidence-game-102705) which shows that users are happy to click and click as long as they feel confident they are reaching their goal. Here I have the best of both worlds. Raise my confidence and do it with the minimal effort!
>
> \[...\]
>
> Without a question this helped me narrow to my result and did not distract me.

More good examples from his brilliant article "[Distracting or Narrowing: Looking a Little More At Live Search](http://looksgoodworkswell.blogspot.com/2005/12/distracting-or-narrowing-looking.html "Looks Good Works Well:Distracting or Narrowing: Looking a Little More At Live Search")".

Christopher Allen wrote [Google Suggest Dissected](http://www.lifewithalacrity.com/2004/12/google_suggest_.html "Live with Alacrity: Google Suggest Dissected") with references and links to more technical information:[\
](http://www.lifewithalacrity.com/2004/12/google_suggest_.html "Live with Alacrity: Google Suggest Dissected")

> This specific technique is probably not useful for all web sites -- the amount of load that even a small number of users can place on a database using this technique requires a large server infrastructure, as basically every time you type a letter a database is being hit. Google can do this as they understand server farms and how to scale large loads. However, as inspiration for other ideas, I think it is marvelous.

**To build on my conclusion** from yesterday, Live search will definately reach broader appeal as more and more mainstream applications occur with this feature. Also — from a user perspective — Live search is unobtrusive and reveals itself without intimidating users that are not aware about it (this is what usability people call discoverability).

There are clear indications that autocomplete save time, reduces errors and form resubmissions. The missing point right now is probably some real usability data to back it up. Recently, uxmatters had a good article on traditional search forms (evaluating ebay, amazon, flickr and more). Findings are available in the article "[Evaluating the Usability of Search Forms](http://dev.uxmatters.com/MT/archives/000068.php "Evaluating the Usability of Search Forms Using Eyetracking: A Practical Approach")". And this type of findings is needed to back up my assumptions with user test data.\
Examples

- [Windows Vista](http://www.microsoft.com/windowsvista/features/default.mspx "Microsoft.com: Windows Vista User Experience") has [live search is deeply integrated](/2006/01/25/windows-vista-setting-new-standards-for-find-as-you-type-searching/ "Justaddwater.dk: Windows Vista setting new standards for Find-as-You-Type searching"),
- [Apple's Spotlight](http://www.apple.com/macosx/features/spotlight/ "Apple.com: Mac OS X - Spotlight (find as you type)") user interface from OS X
- [MSN Desktop Search](http://toolbar.msn.com/tour_desktop/start.aspx "Microsoft.com: MSN Search Toolbar Tour")
- [Google Suggest](http://www.google.com/webhp?hl=en&complete=1 "Google labs: Google suggest")
- [Google GMail](http://mail.google.com "Google GMail") autocompletes contacts
- [Kayak.com](http://kayak.com "Kayak.com travel booking") autocompletes to and from locations

[](http://www.madmanweb.com/links/archives/000459.html) [](http://www.madmanweb.com/links/archives/000459.html)
