---
title: "ASP.Net 1.1 and web standards support"
date: "2005-11-21T06:30:55"
slug: "aspnet-11-and-web-standards-support-20"
url: "/2005/11/21/aspnet-11-and-web-standards-support-20/"
wp_id: 19
categories: ["Code", "CSS", "Web Standards"]
tags: []
---

At the moment, I'm working on a project where we develop ASP.Net components to a Microsoft Sharepoint Portal Server. I'm working on the user interface, other developers take care of the backend ASP.Net functionality, integration and business logic.

Lately Microsoft ASP.Net has been giving me some headaches. It's breaking my principles for a decent web-based application. On this project we're using ASP.Net 1.1 and Vsual Studio 2003.

Principles for a decent web-based application

- \
- Validate HTML
  \
- Validate CSS
  \
- Accessibility principles
  \
- Avoid bloated HTML code
  

Here are some of the ASP usercontrols that are causing me trouble

[\<asp:checkbox /\>](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/cpgenref/html/cpconcheckboxwebservercontrol.asp)

\<asp:CheckBox id="CheckBox1"\
Text="Label"\
Checked="True\|False"\
CssClass="checkbox"\
runat="server"/\>

Will result in this HTML\
\<span class="checkbox" onclick="..."\>\
\<input type="checkbox" name="" id="" CHECKED /\>\
\<label for=""\>Label\</label\>\
\</span\>

WHAT? I get a span when I want a checkbox? The span carries the CSS class? How can I put a class on my checkbox element? I figure out that Microsoft did not care about CSS on a checkbox because in Internet Explorer its probably the element that can be styled the least. Why would Microsoft care about putting a CSS class on the checkbox when you can't change color, you can't change margins, you can't change padding, you can't change size, you can't change anything?

Before I get carried away: One good thing about the \<asp:checkbox /\> though: I get the `label` element. Very good!

Labels are important. They enlarge the clickable area so that the user can hit the target with less accuracy. They are used by screenreaders and other assistive tools to identify fields. They must be present on form elements in order for a webpage to validate.

Back to ASP.Net, does that mean that we can expect `<label> `on other user controls? Unfortunately not. I looked at the `<asp:TextBox>`. Here there's no label. Neither can I get one.

...

Then there's the [`<asp:Label>`](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/cpgenref/html/cpconTextBoxWebServerControl.asp). The name insinuates something we could use for labeling. Not much help here. asp:Label translates into `<span id="..">Labeltext</span>`

Its too bad that ASP.Net has absolutely no focus on The HTML creation seems random, confusing and a complete nightmare for implementing a website in valid HTML, CSS and following accessibility standards.

### Until now

Last week's release of ASP.NET 2.0 has allegedly put an end to all this. In the next article I take a closer look on the improvements of ASP.NET 2.0 as I see it from a web standards point of view.

Technorati tags: [usability](http://technorati.com/tag/usability) [css](http://technorati.com/tag/css) [](http://technorati.com/tag/microsoft) [](http://technorati.com/tag/microsoft) [ASP.NET](http://technorati.com/tag/asp.net)
