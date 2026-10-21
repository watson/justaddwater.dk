---
title: "3 Simple Usability Tips For Developers"
date: "2008-02-11T12:37:38"
slug: "3-simple-usability-tips-for-developers"
url: "/2008/02/11/3-simple-usability-tips-for-developers/"
wp_id: 890
categories: ["Usability"]
tags: []
---

It takes a lifetime to become an expert on the usability field. Many developers may be interested in creating usable, successful applications. But the entry barrier is sometimes too high -- it's easier to rely on the usability experts than to know about usable applications themselves.

Although I'm really passionate about usability, I really understand that approach: Many of the developers in our company are not judged upon their ability to make usable solutions. They are measured on their skills in Java, .NET or whatever.  Also the current Wikipedia page on usability is hard to understand for anyone just faintly interested in the area.

However, basic knowledge of usability can often be of big benefit to most developers. So have simplified and boiled down  to these 3 simple statements:

## Usability definition

In a simplified form, a usable system is

1\) Easy to use

2\) Easy to learn

3\) Difficult to make mistakes

**Easy to use:** This is quite subjective scale to an ordinary system. Almost anybody -- expert or not -- have an intuition about system: Is it easy for me to use.

**Easy to learn:** You only have one chance to make a good first impression. For relations between people this is common knowledge. But when building user interfaces we often forget that first impression of the system.Was it really easy to use without prior knowledge? Did first-time use of the system require intense training? Do first time users ask questions or look for information the wrong places?

**Difficult to make mistakes:** Often overseen in the projects I see. There is a tendency to think that users always do the right thing (Push the correct button, do things in the correct workflow order, etc.). Do you remember back when there was no or limited undo in word-processing? First we had the mechanic typewriter. And after some years, Liquid Paper was invented. Today's common desktop programs all have unlimited undo. Also a few web apps have (GMail is one), but most applications we build for clients still don't have it.

Developers tend to think that undo functionality will be too complicated. What about transactions that have to be reversed, etc? I couldn't agree more. Building simple interfaces is a very complex thing.

Consider this example: A missing person is declared "dead" by the authorities. A few years ago I spoke to a person maintaining the Danish Social security database. Sometimes, a person is declared dead by accident.Either the person shows up, or it turns out that the authorities  by accident have declared the wrong person dead. To undo that action, I was told, is 100 times more expensive.

### All in all

Consider these simple rules and you're on the right way. This is by no means a replacement for dedicated usability work in the projects. However, it's a good supplement and can be used instead of exposing non-usability resources in projects to complex words that has value to experts.

Forget using words such as affordance, error-rate, click-through-rate, task-efficiency, contextual inquiry, quantitative and qualitative analysis. Start using the simpler easy-to-use, easy-to-learn, difficult-to-make-mistakes.

More info:

- Wikipedia: [Usability](http://en.wikipedia.org/wiki/Usability)
- Justaddwater: [Undo — Not Confirmation — End of Discussion](/2007/09/27/undo-not-confirmation-end-of-discussion/ "Permanent Link: Undo — Not Confirmation — End of Discussion") (Sep 2007)
- Justaddwater: [Save Button Usability Issues](/2006/11/27/save-button-usability-issues/ "Permanent Link: Save Button Usability Issues") (Nov. 2006)
- 37Signals: [Google's Gmail Undo](http://www.37signals.com/svn/archives2/googles_gmail_undo.php) (Sep 2005)
- Wikipedia: [Liquid Paper](http://en.wikipedia.org/wiki/Liquid_Paper)
