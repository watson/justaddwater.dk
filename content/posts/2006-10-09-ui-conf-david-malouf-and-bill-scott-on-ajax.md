---
title: "UI Conf: David Malouf and Bill Scott on AJAX"
date: "2006-10-09T15:40:10"
slug: "ui-conf-david-malouf-and-bill-scott-on-ajax"
url: "/2006/10/09/ui-conf-david-malouf-and-bill-scott-on-ajax/"
wp_id: 398
categories: ["AJAX", "Events/seminars", "justaddwater.dk", "Prototyping", "ui11"]
tags: []
---

David Malouf and Bill Scott: Designing Powerful Web Apps with Ajax\
[![David Malouf and Bill Scott on UI Conf](http://static.flickr.com/79/265346636_c34ea54d3a_m.jpg)](http://www.flickr.com/photos/jesper/265346636/ "Photo Sharing")

From UI 11 Conference, Cambridge, Boston October 9, 2006. David's and Bills [presentation notes available](http://billwscott.com/share/presentations/ui11/).

Macromedia coined the term "Rich Internet Application" originally because they wanted to create buzz around Macromedia Flash MX.

Usability tests often raise the Q: "Why doesn't this work like my windows desktop". So emulation of desktop behaviours.\
\* trees\
\* panels\
\* drag and drop\
\* spinner\
\* slider\
\* form validation\
\* context menu

Example Google Spreadsheet.\
\* doesn't look like a desktop application.\
\* Also holding on to some web specific metaphors: underlined links

Cinematic effect. Animated effects like for minimize to show you where to find the minimized programs again.\
Amazon bookstore example from Lazlo Systems: Add to card button activates a cinematic effect that makes the "cart" column jump very subtle. That indicates where to find the info.

"There is no \[page\]" - Neo watching the spoon.\
David's formulation: "page is a metaphor of a moment of uninterrupted context". Another example: Kayak.com where results constantly flow to the browser.

What's all the fuss about Web 2.0? Marketing buzz, but really nothing new: All existed separately.

Technical side of it: Pure browser. Open standards. AJAX new info from server without refresh.\
\* A Javascript call makes a query to the server\
\* server returns XML\
\* Javascript reformats content and updates browser page\
This is visualized with JJG's visual explanation .

Flash\
Flash\
\* to add animation for web pages -- not for creating applications\
\* requires plugin (very common)\
\* uses vector graphics

Bill adds: Flash adds the graphical aspect for html pages.\
David demos Goowy (a Mac like desktop).\
Goowy Made in flash.\
\* Can do most of what javascript does\
\* good image manipulation\
\* good audio support

Firefox "I can't leave firefox because I'm addicted to it's extensions" - David Malouf

An example: Google Notebook (as a Firefox extension). Add your notes to any page. You can even share and publish notes.

Q to what point will you aim for "emulating" a desktop application? Too much desktop emulation? A: It depends \[on user expectations\]. Certain things that never get there no matter how hard you try.

Example: Back button on home-made application. Opens a seperate window to show that back button not working. One user comes in with a 5-button mouse. Uses thumb as user command for going "back".

Bill adds: Yahoo mail beta (looks like outlook). Didn't look like a web app, and therefore users didn't expect back button usage. Users also tried double click. So in all, there is an aspect here: It has to look EXACTLY like a desktop app.

David example for popup window that gets blocked by the standard browser behaviour. After a little while, page detects that new window is not open, and shows a message: (something like) "it seems a popup blocker prevented the window from opening. Click this button to open".

Backend frameworks\
\* DOJO\
\* Script.aculo.us\
\* Rico (on top of prototype)\
\* Ruby on Rails\
\* ASP.NET\
\* Yahoo! User INterface Library (YUI)\
\* Backbase

At Yahoo! Rails really doesn't fit well: We have a lot of JavaScript + HTML inventory that sticks around. Solution for Yahoo: Creating the open-source YUI library (public released Jan 2006)

Atlas renamed to Microsoft AJAX Framework.

Important note on Backend frameworks: The more you know about them, the better you can form your design.

What makes AJAX big now is that Netscape 4 went away.

In a b-to-b\
Banks has a locked image as an end-user, you have to go to IT dept to get anything special installed. AJAX sidesteps all that. As long you use AJAX, you're good to go.

I even tried to sneak flash in there (a bank) but the Flash player that is installed is an older version than the one thats most used on the web.

Q Flash accessibility: Can you navigate through your controls by using tab. A: Yahoo solved that problem (maybe on yahoo maps). It's doable, but you have to add some code. If you want more details on that, I can give you that later.

Q AJAX accessiblity, assistive technologies? Again, it's doable, but you have to do it on purpose.

The design. Could be

David: I'm a big advocate for every designer learning to code something. That will actually make your designs more code-able.\
Meetups and barcamps are free. You learn by contributing, that's the model.

Quick excercise: Meet your neighbours.

How many people have tried that technology is selected before you actually know what application to build.

Power of Patterns\
Style guidelines tend to be thick and tend to not being read.\
Recommend the non-designers design book ([amazon link](http://www.amazon.com/Non-Designers-Design-Book-Second/dp/0321193857/sr=8-1/qid=1160404204/ref=pd_bbs_1/104-1764610-2554333?ie=UTF8&s=books)).

Examples of patterns. Bill's role is not just AJAX evangelist, but more Rich patterns evangelist (lots of examples of terms).

The classic model: page, send to server, page went away. in fact this is a constant interruption of flow. Can be useful sometimes.

Affects wireframing applications. Because wireframes works best for page to page applications.

Affects payment models because is based on page views.

Desktop apps never worked for wireframing: It was better to prototype because the experience was so rich.

Principle: **Keep it direct**\
Alan Cooper whereever there's output there should be input.\
Patterns\
\* Inline editing\
\* Drag and drop\
\* in-context tools\
Guideline: Prefer interaction within the page.\
What about discoverability? Example from Flickr. On hover: yellow background and title tip: Click to edit. Sometimes works also with little small "edit" links.

Added note: Redundant is good for discoverabilities. So the more "invitations", the better. David: "when developers say 'this is redundant' I actually say 'Good' "

Use direct editing on page content.\
What about save/cancel? Example from Flickr.

37Signals Backpack uses an onhover approach shows an edit+delete link that's carved out of the background.

Provide in-context tools\
Only good for single atomic operations. Can actually slow you down: Example backpack where a list of todo-items are checked rapidly. Some of the items are resurrected from the dead, because of the technical implementation.

Use drag-and-drop appropriately. Not for simply setting an attribute. (bad example drag and drop movie rating)

Leave a light footprint. (makes more people creating content).\
Patterns: remembered collection (Gap shopping bag for checkout)\
Pattern: rating an object (recommend this story)\
Pattern: in page action (digg button)

Kevin Rose, Digg creator: When he added AJAX digg button, participation exploded exponentially. Source: [BayCHI meeting](http://www.baychi.org/calendar/20060411/)

Design for engaging moments.\
Use invitations "write a review", "vote". Keep it fun, engaging and light.

Use lightweight events: Hover, click.

Principle: \
Principle: **Cross borders reluctantly**\
Pattern: endless scrolling\
Pattern: in-context expand. (is sometimes misused, where you could have lazy loading instead)

Pattern: inline assistant (Gap store example)\
Pattern: Hover details (Y! news stody links onhover photo + blurb)\
Pattern: Lightweught popups (the lightbox effect)

Rethink process flows: Every page jump is a mental speed bump.\
Rethink paging (vs. floating). It's the users model not the paging model.

Scrolling vs. paging. For search it's not that useful, because for search results, users are mostly interested in first page. Also, what do you do at the end of the scrollbar??

Lazy load.\
My yahoo paging-like scrolling model, where you click and add more news items to the list, and UI sort of scrolls it down.\
Animate that transition, where you kind of scroll them in.

Plan for linking, crawling and back button.\
Not everything is a single page application.\
What will the user think the back button does?

Example: Users actually didn't expect back button to "remember" all the little micro-steps.

Use overlays. For momentary interruptions, can replace page tranistions.\
When editing an individual more complex item.

Example a lightweight popup where you need more space for editing content.\
Also where it's OK to overlay other content of the page.

Use in-context expands.\
Example Yahoo trip planner where you can expand details.\
Example netvibes expand edit options.

Principle: **Provide Live feedback**\
Pattern: live suggest\
Pattern: auto complete

Keep the goal in mind. Is it narrowing or distracting?

Example: Alltheweb.\
Combined the suggest with live search.\
autocomplete builds a list below search box. with linked keywords. Add live-search results in main content frame.

(didn't release as rebranded Yahoo search: Would triple the number of servers needed)

Keep the user engaged\
Time passes faster. Look for engaging moments.\
Example time\
For the user

Use live-previews.\
Look before you leap.\
Example Google's password stength validator.

Keep feedback focused.\
GMail "your message has been sent" is located according to heatmap near searchbox.

Principle: **Offer an invitation**\
shift-click doubleclick, even tripleclick for desktop apps.\
Pattern: Tooltip invitation + hover invitation\
Pattern: Drop invitation\
Example flickr, where a dropped photo actually ondrop is showing a bomb explosion.

Keep actions out of it.\
Don't make the user afraid to explore.

Use invitations to aid discoverability\
Two challenges: idiom & features\
Adding signposts, always-on clues doen't scale:\
Example from backpack todo list where delet/edit links are all over.

Example Y! homepage. Where all but searchfield is dimmed (lightbox effext). As a guided tour for discoverability.

Example Turbotax, where a flash movie talks about all the wonderful things

Example Y! Maps too slow animation and the really bad thing that map grows on hover of a link. Makes it work like advertising.

Principle: **Show Transitions**\
Pattern: Fade transition + selv-healing transition.\
Pattern: slide + animate\
Ex flicr where scroll is on horisontal arrows and content slides.

Speak to the BRAIN\
understanding attention processing. Book Mind hacks (tom stafford and matt webb). [Amazon link](http://www.amazon.com/Mind-Hacks-Tools-Using-Brain/dp/0596007795/ref=sr_11_1/104-1764610-2554333?ie=UTF8).

Example: Apple widgets on dashboard flies at you when dissappearing -- not down to it's icon.

Animations, transitions is actually important:\
\* speed up time\
\* slow down time\
\* show state change\
\* show relationships between objects\
\* focus attention

But remember to **keep it sane**.\
"cut in half" rule of thumb\
When you think you're done, cut that time in half.\
Example Y! mail time for object to snap into place, was cut in half.

Principle: **Think in Objects**\
Example Trip planner\
The power of sharing\
Bloggable, shareable, findable\
How to dial-in community\
Collections

Web 2.0 as a platform\
Rich objects fit the SOA model\
Creates a good separation of concerns, microformats\
Mashups

Easy way to geocode: Flickr example. Made it easy to geocode. Drag objects (images) onto map: 2 million photos geocoded the first 24 hours. Amazing participation.

\[Bill coughs again: "I almost made it through"\]

Engineering: We used to say no. Now we can actually say yes.

Yahoo homepage evolution\
\* old and clunky (2-3 multiple select boxes. Page reload)\
\* click on page: "move up/down, move to top/bottom"\
\* drag and drop new positions

Example Add to my stories, where the plus sign flies up to the "my stories" tab. Plus is too little.

Q shift of paradigm affects advertising model.\
A work tightly with comscore advertising bureau.

Q discoverability of autocomplete\
A autocomplete seems to be secondary functionality, so in that way it's not critical.

Invitation has to be subtle. Point to waste as little brainpower as possible before you start typing. With better discoverabililty, less brainpower is wasted before typing starts.

Reccomends Jen Tidwells book Desinging interfaces ([amazon link](http://www.amazon.com/Designing-Interfaces-Jenifer-Tidwell/dp/0596008031/sr=8-2/qid=1160409975/ref=pd_bbs_2/104-1764610-2554333?ie=UTF8&s=books)).

### Design

When you draw (apply ink to paper) there is actually synapses crossing in the brain, connecting the two brain halves.

So, sketching is important. Also, you can communicate quite a lot you sketch on 10 seconds. Sketching is rapid and rough.

When people see too much permanence, they stop giving feedback.\
\* rapid and rough\
\* multiplicity (multiple sketches)

Don't forget your digital camera when you work with whiteboards.

Next step: Framework and language\
\* create structure\
\* Navigation\
\* Language\
\- object\
\- action\
\- modifiers

Next step: Refinement\
When you cross a boundary on details, people start thinking it's the real thing.\
\* Details\
\* Behaviour (on a very deep level)

Next: Designing behaviour.\
\* User stories. Example: Kevin Chang using cartoon strips as design element early in the design process.\
\* Communicate "intra contextual moments". Very hard to communicate.

Sample process:\
\* sketch on paper/whiteboard\
\* Scan/photograpth into digital environment\
\* Trace or re-draw using computer tool\
\* Use "blocking" tool (like visio) to define framework\
\* As further detail is required to refine framework fills in blocks using a higher fidelity drawing tool.\
\* Add interactivity so that behaviour can be experienced, evaluated, tested, and reflected upon.\
Example: Add hotspots to your visio and export to html. OK, but\
One guy (Anders Ramsay?) advocated XHTML, CSS, JavaScript for wireframes\
Other tools mentioned: Axure, iRise, Serena, Macromedia Fireworks.

\[Jesper's note: Nobody mentions using [Ruby on Rails as Prototyping tool](/2006/04/12/rails-prototyping/).\]

Pain.

> Wireframing Ajax is a \[expletive\]... We have to determine all of the things a user might do, and wireframe the blessed moments of each possibility.

*- [Jeff Zeldman, Web 3.0](http://alistapart.com/articles/web3point0)*

### The shift \[from PIA to RIA\]

PIA = Page-based Internet Application (or Poor Internet Application)\
RIA = Rich Internet Application

Assumption\
\* All interaction is course-grained at page level\
\* Wireframes capture layout, priority, behaviour and content

Impact\
\* Full page refresh replaced by small content update\
\* hyperlink, submit are replaced by a full range of interactive elements\
\* Micro-interaction, micro-updates leading to micro-states\
How to express micro-patterns as wireframes. From

Prototyping is highly important. Must see to make it happen. Paper based prototyping is not able to capture these prototypes\
If you can't actually prototype it, you could find someone doing it similar, and then talk about what you would change on the presentation level/behavioural level.

Q: How high fidelity should prototype have?

Bill working with iterative prototypes. Getting users in one day, then refining it and presenting them to results the next day.

Back to comic strips: 90 % of the time, computer is turned away from reader. Comic strips can show movement, feedback, time passing, etc...

Nuances in the interface are multiplied\
\* invitation\
\* activation\
\* deactivation\
\* affordances\
\* constraints\
\* timing\
\* delays\
\* rate of feedback

Benefits from being as close as possible to real code.\
Example: Use css classes to indicate, drag-objects and drop-zones

Bill Scotts. Drag and drop interesting moments.\
Not just event states, but interesting moments where you can interact with the user.\
About a total of 15 different "interesting moments" for drag and drop.

Drag and drop objects\
\* cursor\
\* drag object\
\* drop target\
\* etc...

Drag & drop matrix (bills article [Interaction Matrix](http://looksgoodworkswell.blogspot.com/2005/11/interaction-matrix.html))

Engineering teams are thrilled about this level of detail, and can be created in an agile way

Y! did that for different patterns\
\* drag drop\
\* inline editing\
\* 6-8 different examples

Working overseas: You can't have enough detail when working overseas. In normal documentation there are so many assumptions in it.

Adaptive Path: Micro states. aka key frames\
Storyboard add timeframe.

Axure, PowerPoint, Sketchup, Ruby on Rails.\
Bill: Wish we would have a tool more like Sketchup. That you are just using without thinking about it.

It's really hard to find that rapid prototyping tool that works good.

Animation with visio: on [bill's blog](http://looksgoodworkswell.blogspot.com/2005/05/interactive-wireframes-documenting.html) and [boxes and arrows](http://www.boxesandarrows.com/view/storyboarding_rich_internet_applications_with_visio)\
Example: Inline editing with visio.

Example: Animation with Photoshop (Photoshop CS2).\
[Blog entry](http://looksgoodworkswell.blogspot.com/2005/11/animating-interactions-with-photoshop.html) (used 20 minutes or so to take existing video and update the timings)

Q: Reviewing wireframes and an actual web page is very different. How to overcome differences?\
A: (David) I try not to reflect so much about the background, but want my colleagues to explain my wireframes.

Good to project your wireframes on a whiteboard so you can start adding to it while discussing it.

Collaborative process. I tend to do all my presentations in front of all teams. Because I want everybody to hear everybody's reaction.

The designers role is really to be a facilitator.

After coffee / fruit break a talk about design.\
Design used in different ways. Design as noun/verb.\
\[Jespers note: I'm not blogging that part (it's a more philosophical discussion that's not directly relevant for my daily work)\].

Design exercise: Design a few screens for a bus ticket kiosk.\
[![Balázs and Mark dissussing details on the exercise](/wp-content/uploads/2006/10/img_9312_resize.thumbnail.JPG)](/2006/10/09/ui-conf-david-malouf-and-bill-scott-on-ajax/balazs-and-mark-dissussing-details-on-the-exercise/ "Balázs and Mark dissussing details on the exercise")

Tool for sketching/prototyping: [Denim](http://dub.washington.edu/projects/denim/).

Q and A closing questions

Q: Good way of debugging when working with Ajax.\
A: Firebug (firefox extension). Make sure any javascript libraries are scoped. Name spacing helps a whole lot.\
Comment: Google web toolkit (built in java) if you have the option to do that

Q: keyboard equivalents to hovering, clicking, doubleclicking, drag&drop\
A: keyboard commands like GMail and Y! mail.

Q: Talk tomorrow different from today?\
A: Some of it will be new.

Q: Accordion\
A: We wrote it for Rico, but never transferered over to YUI library

Why agile development continues to grow in popularity

Rare combination: Companies that are strong both on agile development and user experience.

Wrong assumption. Agile is just about finishing something faster\
It isn't just about finishing faster. It's about finishing faster. I'll explain some more about that later.

### Greedines, short-sightednes and blame

Common things go wrong when projects go wrong.

To software developers, people like you \[UXP people\] are just "the requirements people"

Business case:\
Consider a fictitious product:\
– our business people tell us it will earn us \$300K monthly after release\
– development costs are \$100K monthly\
– it will take 12 months to design, develop, test, and release\
– release costs are roughly \$100K\
this seems like a reasonable venture\
– looking at a 4 year time window - development + 3

Then suddenly\
\* add features (Mona Lisa with candy bar and opera house)\
\* cut scope\
\* delays and risks

Outside the process\
\* political\
\* financial\
\* loss of key talent

Political: "I've seen a lot of projects die when new management take over". Killing predecessors descendants

Once we release it, we may be off target.\
\* doesn't meet business goals\
\* may be unusable\
\* may be technical weak

Also there may be reducing financial return.

So this is our problem: We have got all these risks that may affect return of the project.

### Let's look at the opportunity

\* all released features is \$300 K\
\* 25% features might earn us \$120K

Business cases go from annual release go semi-annual to quarterly\
Even with the added cost of 100 K per release, were earning more money and have an annual busines casse.\
Overall we earn 9% better return on investment (actually IRR)

We can even contemplate to skip the 4th quarterly release and we'll still earn more money.

Book: Software by numbers ([amazon link](http://www.amazon.com/Software-Numbers-Low-Risk-High-Return-Development/dp/0131407287/sr=8-1/qid=1160505925/ref=pd_bbs_1/104-1764610-2554333?ie=UTF8))

### Multiple cycles to reduce risks

Multiple user stories wrapped into an iteration

Planning phase (synonym for design and vice versa)\
For agile people, testing usually means automated testing.

Different levels here:\
\* feature\
\* iteration\
\* incremental release\
\* project

In theory stakeholders feel more involved. More opportunities to adjust.

Agile

### Common things that go wrong with agile projects

1\. planning and releasing smaller releases often results in unusable releases\
2\. no one really understood where the value came from in the first place\
3\. keeping design simple now and worrying about usability later

Why prioritization go wrong is when noone really understands the value of the customers

Not involving design people. They are good at understanding who users are, what are their values. This is actually not an agile problem, but a software development problem.

I'm\
and i'm usually pulled in when things go really bad.

Q's like\
\* who's gonna use it\
\* what's the value for those people\
=\> lot of user reasearch debt

Conversation with stakeholder:\
\- We already did user research\
\- Let me get what you already researched\
\- Well, this was the requirements when we started

### Adding User Experience people

At least They don't use UML, so that's a big advantage.\
Top mistakes:\
1\. "reasonable" research period usually too long\
=\> Truth is: Often a small amount of research yields preliminary designs. Also known as assumptions\
=\> Engaged in research often means disconnected with rest of team

2\. Desing solution is too large\
=\> the "ideal" solution is often so big that it has to be broken down to match releases\
Results in ugly releases\
=\> Often diff between something optimal and something slightly sub optimal. Diff for development effort is sometimes enormous.

3\. not understaning impmlementation costs compared to user value.

### Agile strategies recommended

\* defer specific design until late\
\* keep scope task centric\
\* create useful releases to users\
\* grow design iteratively

**Latest responsible moment** borrowed from lean manufacturing.\
UXP people might translate to\
\* doing enough research to understand users, their problems and goals

### User story

User story\
\* able to write on a 3x5 card\
\* reminder for a conversation\
\* wikipedia is dead wrong

write user stories using this simple template (credited to Rachel Davies in Cohn’s [User Stories Applied](http://www.amazon.com/User-Stories-Applied-Development-Addison-Wesley/dp/0321205685/sr=8-1/qid=1160507778/ref=pd_bbs_1/104-1764610-2554333?ie=UTF8))

As a \[type of user\]\
I want to \[perform some task\]\
so that I can \[achieve some goal\]

As a \[harried shopper\]\
I want to \[locate a CD in the store\]\
so that I can \[purchase it quickly, leave, and continue with my day.

### The car metaphor

Agile question: Which feature do you want us to build first: The tires or the breaks?\
All features are equally important\
=\> adjust scale: Kia, Toyota, Mercedes-Benz

"The simplest thing that could possibly work"

In an agile context, its only works when you understand that you may add other things later.

All these elements have some of these things in it.\
\* Necessity\
\* Flexibility added later. Make feature useful in more situations\
\* Safety\
\* Comfort (usability), luxury (UXP) and performance (run faster, smoother)

If you're in a usecase driven approach, flexibility maps to alternative paths.

\[Changed slide\]\
Bar diagram when adding to user story or feature\
symbolizes discussion\
\* simplest task\
\* flexibility (what if)\
\* fair bit of safety\
\* usability is important

maps to\
\* necessity\
\* flexibility\
\* safety\
\* comfort, luxury, performance

Agile development needs help\
\* so much late decision making\
\* often end up building luxury, but forget necessities.

Agile softwaer development isn't called rapid, or cheap\
Agile because it's maneuverability.

Linn miller, Alias. Written a report, recommend to download.\
Good job at describing

Yahoo! has done a good job adopting Scrum, just didn't have time to report about it yet.

I have more failures to report than successes.

*\[My live notes from UI Conf. [All UI Conf notes](/category/eventsseminars/ui11/). Expect updates of thes rough notes, with references, images, etc. within the first few days – this footnote will stay, though. Feel free to add comments, links to similar notes, presentations, correct quotes and add where appropriate. thanks! Also I post my [pictures on Flickr](http://flickr.com/photos/jesper/sets/72157594320346883/) tagged [uiconf](http://flickr.com/photos/tags/uiconf/)\]*
