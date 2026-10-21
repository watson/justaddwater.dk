---
title: "Why Web Standards Matter (Case Study)"
date: "2006-06-29T16:03:01"
slug: "webstandards-case-study"
url: "/2006/06/29/webstandards-case-study/"
wp_id: 319
categories: ["Browser", "Code", "Errors", "HTML", "JavaScript", "Performance", "Web Standards"]
tags: []
---

Project managers often have a hard time understanding web standards and why they matter. In this case, my arguments made a perfect business case for the managers of a particular project.

Recently I was called out to debug some javascript code that did not perform. There was really not a big problem in Firefox, but Internet Explorer hung using 20 seconds or more each time the script was activated by the user.

It was one of those applications where you click on a little plus to expand a list of units in a subgroup. The list that caused the trouble contained 1,416 rows.

The subgroup was invisible and already rendered. On click a display style property changed from `display:none` to `display:block`. **Unfolding the list took 19 seconds in IE**. WHAT?

### A first look

A brief investigation hinted something was wrong:

- \
- Content/markup ratio: 23%/77%
  \
- Page contained 27,000 elements in the DOM
  \
- W3C HTML Validator unable to validate
  \
- Firefox HTML validator gave 6 HTML errors and 15,700 warnings
  \
- No JavaScript errors, though
  

There were plenty of transparent spacer gifs, and **the spacer gifs were used in empty table cells**. A brief count in the DOM revealed that 5,400 of the 7,200 images were transparent gifs. Uh oh.

### Most important pitfall: TOO many elements in DOM

JavaScript really was not the problem here, because there was nothing but an innocent `display:block` statement. The problem had to be rendering related and I got suspicious as the hidden list contained:

- \
- One giant table element with `display:none`
  \
- Inside that 1,416 rows
  \
- Each of the rows had a table cell with one new table inside it.
  \
- Each nested table had 15 cells (four of which contained only transparent spacer.gifs)
  \
- Tables nested six levels deep on the page
  

All this equals **bloated HTML** and 27,000 total HTML elements on the page. Here's how we got down to 11,000 elements without removing any content:

### Strategy for reducing element count

These were my recommendations for reducing element count and thereby improving performance:

**Avoid JavaScript**. We found that in this situation, the javascript performance had big variations on different browsers (and on the same browser, with different people logged in). In this case, we were able to avoid JavaScript, which is not always the case.

**Remove validation errors and warnings**. Browsers are coded after the HTML specifications, HTML specifications tell browser vendors how their code should interpret valid HTML. If the code is not valid, sometimes browsers guess what they think the source code means. The only thing specified in the HTML standard is how valid code behaves. Invalid code is left for the browser to do whatever it pleases. If, for instance, a `form` element is nested directly in a `table` element, it's not allowed. But what will the browser do about it? Render the element? Or silently ignore it? Can you submit forms at all from the page? If your form cannot submit, it can be a big risk to use HTML that does not validate.

In this particular case, there were 6 errors and 15,700 warnings (all of which could be easily fixed).

**Remove elements without content**. Originally each of the 1416 rows had its own table element. Additionally, a lot of transparent images were placed in empty table cells. All of this clutter was removed. We ended up using six table columns in the parent table, compared to originally 15 columns in each of the 1416 child tables. This really adds up when you consider that in our baseline example we had 1416 rows. All in all we reduced HTML footprint with 40%.

### Result





Before


After




display:none on subgroup:


19 sec


\<0.5 sec




`document.getElementsByTagName('*').length`:


27,000


11,471




Number of image tags:


7,200


1,426




Number of tables:


1,416


11




HTML validation errors:


6


0




HTML validation warnings:


15,700


0




IE memory consumption (avg):


46MB


35MB




IE memory consumption (peak).


58MB


36MB




### Long-term findings


- \
- Don't use JavaScript for general page layout rendering. Think really really hard if it can be done without JavaScript. One example: Print should be done with CSS
  \
- If there is no way around it, use standard JavaScript libraries were browser bugs, etc are hidden for the programmer
  \
- Tables used for layout are evil. Use tables for table-based content ONLY
  \
- HTML code is really messy and hard to maintain. Should be cleaned up to avoid similar situations in the future. Clean up nested tables, table cells with transparent gifs. Use CSS where appropriate could shave up to 50-70% of HTML footprint
  \
- Many HTML validation errors. Code improperly nested, forgotten end-tags: Ideally, the pages should have no validation errors. It's an achievable work worth the effort and very educational way of working with the code
  


### Long-term benefits

In general, several benefits could be gained by raising the knowledge of HTML, CSS, Javascript, web standards, and browser issues.

- \
- Include easier maintenance
  \
- Lower risk of change
  \
- Lower risk of browser incompatibilities
  \
- Lower risk of browser crashes
  


### Browser tools

These tools I used for quick investigation of the HTML page:

- \
- [HTML validator Firefox extension](https://addons.mozilla.org/firefox/249/ "Firefox Add-ons: HTML validator") by [Marc Gueury](http://users.skynet.be/mgueury/mozilla/ "Marc Gueury Mozilla homepage")
  \
- [Firebug Firefox extension](https://addons.mozilla.org/firefox/1843/ "Firefox Add-ons: Firebug") by [Joe Hewitt](http://www.joehewitt.com/ "Joe Hewitt website")
  \
- Content/markup ratio with [pageinfo bookmarklet](http://slayeroffice.com/?c=/content/tools/pagenfo.html "Slayeroffice: Page Info Favelet") by Slayeroffice (Steve Chipman) who has a [cat named Javascript](http://slayeroffice.com/archives/?p=140 "Slayeroffice: Javascript the cat")!
  \
- Counting of HTML elements with [JavaScript shell bookmarklet](http://www.squarefree.com/shell/ "Squarefree: Javascript Shell") by Jesse Ruderman:\
  `document.getElementsByTagName('*').length`\
  could be done dicectly from the browser address bar by typing:\
  `javascript:alert(document.getElementsByTagName('*').length);`
  

More info on my firefox extensions in the article: [Web developer’s collection of browser tools](/2005/11/30/web-developers-collection-of-browser-tools/ "Permanent Link to Web developer’s collection of browser tools") (Nov 30th, 2005).
