---
title: "Extract HTML Structure From Page With Simple Script"
date: "2009-10-05T13:00:41"
slug: "tiny-script-to-extract-html-structure-from-page"
url: "/2009/10/05/tiny-script-to-extract-html-structure-from-page/"
wp_id: 1176
categories: ["Code"]
tags: ["Code", "nokogiri", "ruby", "script"]
---

I often want to extract parts of HTML page. Often I find myself parsing a doc with Nokogiri and extracting it with a CSS selector. It's pretty straight-forward from scratch.

To follow the Don't Repeat Yourself principle, I created a script to make it a one-liner. Just run `ruby parsepage.rb [url] [css_selector]`

Feel free to use and modify the code (which i put on GitHub so you can fork and pull from it): <http://gist.github.com/199558>

[View gist 199558 on GitHub](https://gist.github.com/199558)

I created the script because I wanted to extract headings from a recent article. You could also use it for creating table of contents or similar.

## Usage examples

    $ U=http://www.smashingmagazine.com/2009/09/24/10-useful-usability-findings-and-guidelines/
    $ parsepage.rb $U "h3" --html-list
    #=>
      <li>1. Form Labels Work Best Above The Field<li>
      <li>2. Users Focus On Faces<li>
      <li>3. Quality Of Design Is An Indicator Of Credibility<li>
      <li>4. Most Users Do Not Scroll<li>
      <li>5. Blue Is The Best Color For Links<li>
      <li>6. The Ideal Search Box Is 27-Characters Wide<li>
      <li>7. White Space Improves Comprehension<li>
      <li>8. Effective User Testing Doesn’t Have To Be Extensive<li>
      <li>9. Informative Product Pages Help You Stand Out<li>
      <li>10. Most Users Are Blind To Advertising<li>
      <li>Bonus: Findings From Our Case-Studies<li>
      <li>Other Resources<li>
      <li>Sponsors<li>
      <li>Smashing Links<li>
      <li>Stay in touch<li>
      <li>Popular Posts<li>
      <li>All Posts<li>
      <li>Blogroll<li>

    $ parsepage.rb $U "h1" --text-only
    #=>
      Smashing Magazine we smash you with the information that will make your life easier. really.
      10 Useful Usability Findings and Guidelines

    $ parsepage.rb $U "h1:first-child"
    #=>
    <h1 class="title"><a href="http://www.smashingmagazine.com/2009/09/24/10-useful-usability-findings-and-guidelines/" rel="bookmark" title="10 Useful Usability Findings and Guidelines">10 Useful Usability Findings and Guidelines</a></h1>

Let me know if you find it useful. I'll happily update script with any general contributions.
