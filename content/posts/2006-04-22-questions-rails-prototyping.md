---
title: "Questions on Rails for prototyping"
date: "2006-04-22T01:37:08"
slug: "questions-rails-prototyping"
url: "/2006/04/22/questions-rails-prototyping/"
wp_id: 225
categories: ["justaddwater.dk", "Ruby on Rails"]
tags: []
---

I recieved some mails and comments on my recent article: [Ruby on Rails as rapid prototyping tool\
](/2006/04/12/rails-prototyping/ "Permanent Link: Ruby on Rails as rapid prototyping tool")

First of all: Thanks for all of your comments. Here are my answers some of the questions. Answers are from top of my head, since I'm about to go on vacation, but want to give feedback.

> *Question by Ramzi:* are there any psychological side-effects in using both RoR and Java/.Net in parallel? Do you have to keep RoR out of the reach of the developers to keep them motivated in working with other frameworks?

Not that I know of, and besides, I'm doing all that I can to spread out theknowledge about the "Rails"-way — the conventions, etc. My thought is that it can only make working in the other frameworks faster.

> *Question by Priisholm:* Nice thing is to see larger RoR adoption in my home country, Denmark. Do you know of any RoR knowledge groups in DK, and if so, could you post it here? I’d be very interested.

Let's keep in touch. We are some at Capgemini that definately want to meet up with others in Denmark (Copenhagen area). Please let me know of other people that you have in thought that might want to join us.

> *Question by Luis Villa:* If you show your client an almost ended product, he can put pressure on the development phase. The advantage of the RoR approach is that you almost don’t have functional specs… so… all the product design and development team has the same perspective about functions, look and feel of the final product… Just build it.

I think it's a minor problem. The prototype is never close to a finished product. Car makers know that when showing prototypes on car shows. Maybe no airbags are installed, maybe steering is not adjusted, windshield wipers don't work, etc.

The important factor here is **what to do first**: Start with the user interface that creates value. Jason Fried of 37Signals preaches this in practically every presentation I have heard. Then afterwards, move on with the validations, integrations, browser compatibility, accessibility, etc.

I usually make it look pretty in Firefox and look broken in IE (leaving the thorough CSS work till later).

> *Question by Luis Villa:* The HCI and Interface team need to be remodeled: I mean, you can’t only sketch the UI. You need more technical profiles. So maybe, from a pure UI Team perspective you are lacking “agility”, because you raise the client’s expectations: he expects to hace a very high fidelity pre-definition of the final product.

The colleagues with whom I'm working with this are highly technical. I totally agree with you here (even though your role is the devil's advocate). Uou really need technical experts in your UI team.

An example: Let's say you want to put a live search field for selecting road names in your country. A live search (or autocomplete field) really must by really fast to work intuitively.

A less skilled design team may think it would just work. But it really takes a technical person to dig into the dirty details. How much data are we looking into? (in Denmark it's roughly 106.000 road names). Can we search full text or start of road name? Do we need some kind of winnowing mechanism to narrow down in order to get fast response times? And so on and so forth...

> *Question by Luis Villa:* Are we degrading Rails to just a “nice prototyping platform” with this approach?

Rails have some sweet spots other than protyping, which I have focused on here. I leave that to a later post to go into details about those. My point is that prototyping is a sweet spot for Ruby on Rails. Of course it requires that your team has Rails skills :-)

Related reading - [A Designer's Guide to Prototyping Ajax](http://particletree.com/features/a-designers-guide-to-prototyping-ajax/) pointed me to these good resources:

> \
>
> - \
> - [Getting Creative With Specs: Usable Software Specifications](http://www.boxesandarrows.com/view/getting_creative_with_specs_usable_software_specifications) · An effective, usable spec serves two main purposes: First, it elicits feedback early, which helps to avoid problems and misunderstandings later on. Second, an effective spec ensures the software stays in line with the designer’s intentions.
>   \
> - [HTML Wireframes and Prototypes: All Gain and No Pain](http://www.boxesandarrows.com/view/html_wireframes_and_prototypes_all_gain_and_no_pain) · A great introduction to wireframes and a list of benefits they provide to the workflow process.
>   \
> - [How do we do HTML wireframes?](http://atomiq.org/archives/2005/09/how_do_we_do_html_wireframes.html "How do we do HTML wireframes?") · An outline of a conversation between a few intelligent and experienced developers on their wireframing tools and methods.
>   \
> - [Prototype Techniques in the Web Design Workflow](http://www.molly.com/2005/08/23/protoype-techniques-in-the-web-design-workflow/ "Prototype Techniques in the Web Design Workflow") · Molly briefly goes over a number links to various techniques that can be used to build wireframes and prototypes.
>   \
>
> \
