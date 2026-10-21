---
title: "Textmate Snippet: Convert HTML entities for viewing code"
date: "2008-01-01T12:44:49"
slug: "e-texteditor-snippet-convert-html-entities-for-viewing-code"
url: "/2008/01/01/e-texteditor-snippet-convert-html-entities-for-viewing-code/"
wp_id: 755
categories: ["Software", "Web Development"]
tags: []
---

Happy New Year everybody. Here is a tiny Textmate or E-Texteditor Snippet: Convert HTML entities for viewing code. I created this recently for a HTML cookbook on a project, where we made HTML pages showing HTML example code. It converts

- & to \&amp;
- \< to \&lt;
- \> to \&gt;

[![e-texteditor-bundle-editor-convert-html-entities-thumb.png](/wp-content/uploads/2007/12/e-texteditor-bundle-editor-convert-html-entities-thumb.png)](/wp-content/uploads/2007/12/e-texteditor-bundle-editor-convert-html-entities.png "e-texteditor-bundle-editor-convert-html-entities.png")

That's it. Basically, I made a copy of one of the more complex snippets and simplified it. Recently, it has been a real time-saver for me despite it's simplicity.

In text here is the snippet:

Save:  
Nothing

Environment:  
Cygwin (generic)

Input:  
\[Selected Text\] or \[Document\]

Output:  
Replace Selected Text

Activation:  
\[Key Equivalent\] Ctrl-Shift-6

Scope Selector:  
text.html

Code:  
    #!/usr/bin/env ruby
    # By Jesper Rønn-Jensen, 2007-12-19 (Last update: 2007-12-19)
    # escape &amp;,&lt;,&gt; to show in HTML pages
    $KCODE = &#039;U&#039;

    $char_to_entity = { }
    File.open(&quot;#{ENV[&#039;TM_BUNDLE_SUPPORT&#039;]}/entities.txt&quot;).read.scan(/^(\d+)\t(.+)$/) do |key, value|
      $char_to_entity[[key.to_i].pack(&#039;U&#039;)] = value
    end

    def encode (text)
      text.gsub(/[&lt;&gt;&amp;]/) do |ch|
        ent = $char_to_entity[ch]
        ent ? &quot;&amp;#{ent};&quot; : sprintf(&quot;%02X;&quot;, ch.unpack(&quot;U&quot;)[0])
      end
    end

    print encode(STDIN.read)

The blog software messes up single/double quotes, so here is a link to the raw snippet file which I put in `/Bundles/HTML.tmbundle/Commands`. On my E-texteditor/Windows install that is `C:\Documents and Settings\[username]\Application Data\e`\
`\Bundles\HTML.tmbundle\Commands . `

**Here it is for you to download:**\
[entities-convert-html-for-html-output.tmCommand](/wp-content/uploads/2007/12/entities-convert-html-for-html-output.tmCommand "entities-convert-html-for-html-output.tmCommand")\
(last update: 2007-01-01)

I was very close to modify it further to wrap selection in \<pre\>\</pre\> element, (because I always use the code that way). But decided not to: It's only a keyboard shortcut more to wrap the selection:

Alt-Shift-W: Wrap selection in Open/Close Tag

PS. The editor usually messes up on some of the escaped HTML characters. Please refer to the attached file for the correct version. And please let me know if you find errors in the markup.
