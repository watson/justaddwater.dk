---
title: "4 easy steps for documenting user interface"
date: "2006-11-22T11:51:04"
slug: "4-easy-steps-for-documenting-user-interface"
url: "/2006/11/22/4-easy-steps-for-documenting-user-interface/"
wp_id: 462
categories: ["Best of Justaddwater", "User Interface"]
tags: []
---

I was asked today on which best practices exist in documenting user interfaces. Especially with focus on documenting how and where the user interface (GUI) communicates with backend services.

The format I usually use is:

1.  Screenshot
2.  Description
3.  Preconditions
4.  Postconditions

Explanation:

1.  **Screenshot** of the entire page or content area
2.  **Description** of the page purpose. Primary action and possible secondary actions on page.
3.  **Preconditions**: What data must be available for the page to render. Where is data retrieved?
4.  **Postconditions**: Data that the user enters. Where is data saved? (Could also be data behavioural data: Example measuring if user completes a purchase)

Then repeat for each screen. Sometimes I also need to document variations of each screen. In that way, each page is repeated with the appropriate screenshots.

One big advantage for me is that documentation tend to become fairly brief and concise. My focus is **collaboration over documentation**, where the shorter is the better.

What are your experiences with documentation of GUI in a format that is short and concise and easy to maintain?
