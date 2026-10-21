---
title: "Introducing Tiny JavaScript Number Formatter"
date: "2008-08-18T10:50:25"
slug: "introducing-tiny-javascript-number-formatter"
url: "/2008/08/18/introducing-tiny-javascript-number-formatter/"
wp_id: 945
categories: ["JavaScript"]
tags: ["JavaScript", "library", "opensource", "project"]
author: "jesper"
---

For a current project, I created a tiny number formatter that inserts thousand delimiters in a string:

10000 to 10,000 etc.

Just add css class="numberformat currency" to a text field, and it will be formatted automatically.

It is based on the [Prototype JavaScript library](http://prototypejs.org). You can get it from it's GitHub repository page. Feel free to add or alter the functionality. Releasing under Creative Commons license.

[![Creative Commons License](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/)\
This work is licensed under a [Creative Commons Attribution-Share Alike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

Some quick notes:

I'm using this on a rather big HTML page, so the selection of DOM nodes must be as simple and quick as possible. So if you are considering moderations, please make sure that the DOM manipulations are as lightweight as possible.

The script is as simple as possible. It does not parse the string as a number. Instead it just strips any thousand delimiters in the string. Afterwards it sets its own. There may be some important logic here to add to make the code more robust.

I have also added a test page to the project... not a real test page, but a HTML page that shows examples that are modified. Please back up any added functionality with changes to that page as well.

Contact me for commit access if you would like to contribute. I do not expect to add any functionality to the code unless the work project requires it.

More info:\
[GitHub repository](http://github.com/jesperronn/numberformat-js/)
