---
title: "Usability of Pagination Links"
date: "2008-01-03T15:04:05"
slug: "usability-of-pagination-links"
url: "/2008/01/03/usability-of-pagination-links/"
wp_id: 841
categories: ["Usability"]
tags: []
author: "jesper"
---

In case you missed the thorough pagination gallery that was published in November: [Pagination Gallery: Examples And Good Practices](http://www.smashingmagazine.com/2007/11/16/pagination-gallery-examples-and-good-practices/ "Pagination Gallery: Examples And Good Practices")

There are really some good (and bad) examples collected at the page, including these written "best practices":

> 1.  Provide large clickable areas
> 2.  Don’t use underlines
> 3.  Identify the current page
> 4.  Space out page links
> 5.  Provide Previous and Next links
> 6.  Use First and Last links (where applicable)
> 7.  Put First and Last links on the outside

I am missing a few important points in that article.

### Think twice before adding link to "last"

First, i will in some cases disagree with the advice to use a "last" link as mentioned in \#6. For big search results it will mostly be irrellevant to jump to the last page. Often a search resulting in lots' of hits will lead to another more specific search. Who cares what the last of 24,000,000 results on [a Google search for "usability"](http://www.google.com/search?hl=en&q=usability "Usability - Google search result page 1")? I think it's correct of Google not to show a "last" link. Jakob Nielsen notes that 42% use the top link, 8% the second link, and the other links are even less likely to get attention. (see end note for details).

The anatomy of searching is usually to keep narrowing your search until the result you were looking for is in the first page.

Also Amazon uses that technique. Here is a screenshot from the German Amazon.de:

![amazon-search-result-paging.png](/wp-content/uploads/2007/12/amazon-search-result-paging.png)

As you see, there the paging only covers the first 3 pages (or 75 items of 168 found in the query). In my opinion (and backed by the Google and Amazon examples), this should be the default. However, in rare cases there could be an idea in providing a "last" link.

For instance in a netbank, when searching for payments or elsewhere when returning a limited, known resultset you are likely not to narrow down further.

So I would reformulate \#6

> ~~6. Use First and Last links (where applicable)~~
>
> 6\. Provide a link back to first page. Don't use a link to last page, unless there really is a value for the end user on the last result page.

### Number of pagination links

Also I am missing a guideline regarding to how many pagination numbers to show. Here is my suggestion:

> 8\. Provide a reasonable number of pagination links. Usually, the 3 first pages are enough.

The last sentence follows the Amazon example from above. For the record, i have gathered the different states here in case i am missing something

![amazon-search-result-paging-all-states.png](/wp-content/uploads/2007/12/amazon-search-result-paging-all-states.png)

### Consider "endless" scroll and avoid pagination

One other point that I want to add is that pagination add a lot of controls that don't necessarily add value to your content. By adding more links, the content gradually gets hidden more and more. In article, there are som example where pages actually implement so many paging controls that it will eventually confuse some people. So, before adding pagination, consider the alternatives.

For instance, does it really, really add value that you are able to jump directly to any of the 28 pages in this example:

![pagination jump to any page in result set](/wp-content/uploads/2007/12/erweiterungen.gif)

One alternative is the "endless scroll" model. Bill Scott originally wrote about this and implemented it for Rico (javascript framework). Bill's [Death to Paging! - Rico LiveGrid Released](http://looksgoodworkswell.blogspot.com/2005/06/death-to-paging-rico-livegrid-released.html)

Currently, Google Reader also uses this, and it's very intuitively implemented. You scroll the feed list and when the scrollbar approaches the bottom, suddently, more items are loaded in the background.

Important pros and cons of "endless scroll":

- Very intuitive. No need to learn new navigation, just scroll.
- No need to clutter interface with additional controls that require braincycles to understand
- Watch out: Can be surprising to new users that the scrollbar itself shrinks as new results are loaded

Because of the last bullet, I would not recommend using "endless scroll" in any situation. But at least I would recommend you seriously consider it. (Btw, if you know of any other easy-to-implement of endless scroll, please let me know and I'll add it to the article).

## Alternative: No pagination

One final option also deserves a mention here. Using no pagination, "endless scroll" or similar is actually the easiest to implement and the easiest to comprehend.

Actually, we recently decided not to implement pagination in a project. Instead we took a principal decision and showed maximum 30 results. The question "what if there are 31 results?" -- the classic N+1 question that you would have to face regardless of you pagination strategy or a fixed number of results.

The biggest advantage of this is that it's the fastest to implement. Just limit the number of search results to a fixed number. But this also puts a burden on you shoulders: You as the application designer must make an informed decision about how many results it would be appropriate to show. In the case of a Google-like search dataset, there are data that suggest that most people choose from the first 10 search results (or else they narrow searching). So 10 results may be appropriate. In other cases you may want to adjust that number to either side.

In any case, make sure you ask your project team the question: **Did you seriously consider no pagination?** Seriously? Are there features we should spend time on that add more value than pagination?

Making informed design decisions on behalf of the users is one of the things I admire in "getting real" by 37Signals. If anything can be done to reduce the number of braincycles used to understand a user interface, make sure you seriously consider it. [Start With No](http://gettingreal.37signals.com/ch05_Start_With_No.php) \[pagination\]. [Epicenter Design](http://gettingreal.37signals.com/ch09_Epicenter_Design.php) \[to focus on the most important features\]. [Build less](http://gettingreal.37signals.com/ch10_Less_Software.php). [Beware the bloat monster](http://gettingreal.37signals.com/ch15_Beware_the_Bloat_Monster.php).

End note:

Jakob Nielsen: "[The power of default values](http://www.useit.com/alertbox/defaults.html)" (September 2005), Thorsten Joachims et al.: [Accurately Interpreting Clickthrough Data as Implicit Feedback](http://www.cs.cornell.edu/People/tj/publications/joachims_etal_05a.pdf "Cornell University: PDF file")"(178KB pdf file). Nielsen notes that 8% follow link number 2, but I can't find that result in the publication. This graph I'm reading as follows:

[![search-result-rank-click-rates.png](/wp-content/uploads/2007/12/search-result-rank-click-rates-small.png)](/wp-content/uploads/2007/12/search-result-rank-click-rates.png "search-result-rank-click-rates.png")

1.  42%
2.  16%
3.  12%
4.  6%
5.  5%
6.  7%
7.  3%
8.  4%
9.  1%
10. 4%

Regardless of the accurate numbers, it does not alter the conclusions that users focus on first results. Furthermore, there is nothing in the materials that backs up my theory that people narrow their search until what they look for are in the top results. Please let me know if you are aware of any numbers that can confirm that.
