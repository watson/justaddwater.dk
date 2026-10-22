---
title: "On-Site Searching Still Stinks"
date: "2005-12-04T01:04:53"
slug: "on-site-searching-still-stinks"
url: "/2005/12/04/on-site-searching-still-stinks/"
wp_id: 28
categories: ["Search Engines", "Usability"]
tags: []
author: "thomas"
---

It has been said many times before. Jared Spool [said it in 1997](http://www.uie.com/articles/search_stinks/). Today 8 years later little have been done to improve them: Site-specific search engines.

If you browse a website chances are that it has its own build-in search engine where you can search its content. But chances also are that you never get any good results when using them. How come? What can be done to improve them?

When referring to a study about site navigation and whether or not users found what they where looking for Jared Spool writes:

> Using an on-site search engine actually reduced the chances of success, and the difference was significant. Overall, users found the correct answer in 42% of the tests. When they used an on-site search engine (we did not study Internet search engines), their success rate was only 30%. In tasks where they used only links, however, users succeeded 53% of the time.

### Ranking

The main difference between an on-site search engine and search engines for the web is the way they rank the results. Google is very silent about their own ranking algorithm (PageRank) - but it's no secret that the corner stone of the web (hyperlinks) is quite a big factor in the equation. Google themselves [explain it](http://www.google.com/technology/) this way:

> PageRank relies on the uniquely democratic nature of the web by using its vast link structure as an indicator of an individual page's value. In essence, Google interprets a link from page A to page B as a vote, by page A, for page B. But, Google looks at more than the sheer volume of votes, or links a page receives; it also analyzes the page that casts the vote. Votes cast by pages that are themselves "important" weigh more heavily and help to make other pages "important."

If you could just do the same with links between the pages locally on your website, you would be on your way. But the reason this works for Google is because the web is so enormous. This is the same reason why a survey covering 10.000+ people gives a clearer and better image of the reality than one that only covers 10. Of course you could just make your own indexing bot whose sole purpose was to traverse the net and log all links pointing to your website. But why waste time, bandwidth and money on this when you can just ask Google?

#### Asking Google

Google have what they call [Google Web API](http://www.google.com/apis/). This is a semi-free Web Service (a thousand free queries allowed per day) you can use in your on-site search engine to tap into Google's huge databases and use it to search your own site. You can easily limit the Google search to only cover a specific domain by using the ["site:" operator](http://www.google.com/help/operators.html#site). In [this example](http://www.google.com/search?q=Google+site%3Ajustaddwater.dk) I'm searching the domain justaddwater.dk for the word "Google".

When doing a search through the API, you can either use the retuned results as they are and just display them (properly formatted of cause). Or you can use the ranking and apply this to your own algorithm.

Of course to be able to use Google like this, all the corners of your site must be reachable to Google's indexing bot. So you can't ask Google to find stuff on your intranet or even a password protected forum on your public website - In that case you have to host the indexing and searching technology in-house. If you are a Google fan this is possible to do with their [enterprise solutions](http://www.google.com/enterprise/) (we at Capgemini Denmark are currently implementing this solution on [www.dk.capgemini.com](http://www.dk.capgemini.com/) - so hopefully we can review this later when we have gathered some experience).

#### Asking MSN Search and Yahoo!

After Microsoft have woken from their great slumber and entered the search engine market they as well have developed a Web Service you can use to access and query MSN Search. I haven't tested it yet, but you can find more information about it on [MSDN](http://msdn.microsoft.com/msn/msnsearch/).

MSN Search has learned from Google and has also implemented search operators which are an important factor if you want to use it for searching your own site. Even the format is the same - so the "site:" operator can easily be used.

I haven't been able to find out if Yahoo! supports search operators (it doesn't seem like it!), but they do have an impressive collection of Web Services. Of interest here is of course their [Search Web Service](http://developer.yahoo.net/search/).

### What to do?

The message is clear enough. If your search engine is not working, don't let your users use it. In that case it can do more damage than good. If you want to have an on-site search engine please implement it properly. This means:

1.  **Rank the results** with the most important once at the top of the page.
2.  **Make all your content searchable**. Many on-site search engines does not search for example a product catalog because this in many situations is implemented via 3rd party software.
3.  **Show matching text snippets with highlighted keywords**. If the user can't see the relevance of the results he or she can't judge how well a given one matches the query. So do like all the major search engines and show two or three lines of text where the keywords match.
4.  **Remember the title-tag**. Make sure each page on your website has a proper title! This is the headline that will show up in search results and the first thing the users sees in a result set - very important!
5.  **Group the results by category**. This is hard (if not impossible) to do by the big internet-wide search engies since they don't have control over the content. But surveys show that this actually works very well on site specific search engines. One of these is detailed in this PDF by Microsoft Research: [Optimizing Search by Showing Results In Context](http://research.microsoft.com/~sdumais/chi2001.pdf).

Of other important points could be the use of proper **meta keywords** and maybe also a **meta description**. But Google does not use any of these when indexing or ranking results though. David Callan from akamarketing.com [explains](http://www.akamarketing.com/google-ranking-tips.html):

> I imagine many of you know this already but Google does not use meta tags such as the keywords meta tag or the description meta tag. This is because the text within these tags can't be seen by visitors to a website. Therefore Google feels these tags will be abused by webmasters placing lots of unrelated words in them in order to get more visitors.

In a controlled environment like a single website you could of cause argue that the level of self discipline is so good that this is not an issue - so maybe you should also consider this?

### Final words...

This post does not at all do the subject justice. It even leaves some unanswered questions. This is both because *one* post is simply too small to cover this subject in depth and also because I want to hear your opinions. So feel free to comment. But just remember this: When developing a new website, you should never let your users depend on a search engine. This is just a sign of bad usability. Make sure that your users **easily** can find what they are looking for via the normal navigation. If they have to use your search engine it just means that your navigation is flawed.

<small>Technorati tags: [search engine](http://technorati.com/tag/search+engine) [usability](http://technorati.com/tag/usability) [jared spool](http://technorati.com/tag/jared+spool) [search ranking](http://technorati.com/tag/search+ranking) [google](http://technorati.com/tag/google) [google api](http://technorati.com/tag/google+api) [msn search](http://technorati.com/tag/msn+search) [yahoo search](http://technorati.com/tag/yahoo+search)</small>
