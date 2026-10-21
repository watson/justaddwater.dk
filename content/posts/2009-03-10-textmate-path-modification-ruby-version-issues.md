---
title: "Textmate Path Modification -- Ruby Version Issues"
date: "2009-03-10T11:47:26"
slug: "textmate-path-modification-ruby-version-issues"
url: "/2009/03/10/textmate-path-modification-ruby-version-issues/"
wp_id: 1044
categories: ["justaddwater.dk"]
tags: []
---

I had some issues with Ruby on my macbook after upgrading Ruby from 1.8.6 to 1.8.7.

This was a problem in Textmate as it still picked up the old version and ignored \$PATH i set in my .profile.

Thanks to fast and excellent help from Allan Odgaard and others in the \##Textmate IRC channel.

The main point is that if you modify your \$PATH you should probably also set a variable in Textmate reflecting that change. Otherwise you may end up with Textmate running an old version of a program like I did.

![](/wp-content/uploads/2009/03/textmate-preferences-advanced-path.png "textmate-preferences-advanced-path")

Note also that there is some help on the Textmate Wiki: "[RubyVersionIssue](http://wiki.macromates.com/Troubleshooting/RubyVersionIssue)" with a link to the suggestion Alan mentions above ([setting path for Finder](http://manual.macromates.com/en/shell_commands#search_path) in environment.plist).

```
Pasted as Plain Text by peterhaza
Description: No description
URL: http://rafb.net/p/mlsekL34.html

March 6th 2009
11:25 jesperronn: Hi everybody (new to the IRC channel) I know this has been 
up millions of times: Ruby version issues!
11:26 jesperronn: My problem is basically the same as described: wrong (old) 
ruby version picked up by Textmate
11:26 jesperronn: I tried the suggestion that was linked (setting up 
~/.MacOSX/environment.plist and adding new ruby path)
11:27 jesperronn: Could somebody give me some troubleshooting help?
11:29 malesca: jesperronn: Did you reboot after changing environment.plist?
11:29 malesca: path?
11:29 inner_six: Your search path is incorrect. See 
http://manual.macromates.com/en/shell_commands#search_path and be sure to 
read the last paragraph about ~/.MacOSX/environment.plist (used for shebang 
scripts)
11:29 jesperronn: Yes I did reboot
11:30 jesperronn: (although it says logout/login in the wiki page)
11:30 jesperronn: After the reboot the test suggested actually changed result
11:30 jesperronn: #!/bin/sh echo "$PATH"
11:31 jesperronn: result was: /usr/bin:/bin:/usr/sbin:/sbin
11:31 jesperronn: sorry for the smilies...:(
11:31 jesperronn: it changed to /Users/jesper/Library/Application 
Support/TextMate/Pristine 
Copy/Support/bin/CocoaDialog.app/Contents/MacOS:/Library/Frameworks/Python.fra
mework/Versions/Current/bin:/usr/local/apache2/bin:/usr/local/mysql/bin:/Users
/jesper/bin:/usr/local/bin:/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/b
in:/usr/X11/bin:/Users/jesper/Library/Application Support/TextMate/Pristine 
Copy/Support/bin
11:31 jesperronn: which is the correct from .profile
11:32 jesperronn: And "ruby --version" now gives me the new correct version 
1.8.7
11:33 jesperronn: So it works when running snippets in plain text via CTRL-R
11:33 jesperronn: Now the issue is still there for my .rb file
11:34 jesperronn: The .rb file starts with #!/usr/bin/env ruby
11:35 jesperronn: and running Command-R tells me the version is the old 1.8.6 
(located at /usr/bin/ruby)
11:35 jesperronn: So how do I change this behaviour on Ruby files??????
11:37 jesperronn: inner_six: there is no difference in the ruby version 
picked up if I remove the shebang
11:37 jesperronn: inner_six: i already added the environment.plist on my 
machine
11:39 perdiy: jesperronn: Have you set TM_RUBY?
11:40 jesperronn: perdix: how do I check that? (i probably have not)
11:40 perdix: jesperronn: Check Preferences → Advanced → Shell Variables 
11:41 jesperronn: thanks perdix. No it's not set
11:41 jesperronn: perdix: what do you suggest I do?
11:42 perdix: jesperronn: Not sure…
11:44 perdix: Just so I understand you correctly: entering ‘ruby --version’ 
and hitting ⌃R says it’s ruby 1.8.7, but creating a Ruby file containing 
‘puts RUBY_VERSION’ and hitting ⌘R says it’s ruby 1.8.6?
11:46 jesperronn: perdix: Thats exactly what i did!
11:46 jesperronn: and the exact reults i got
11:48 perdix: Sorry, then I have no idea. You could set TM_RUBY to the full 
path to the ruby executable you want to run (in the mentioned prefpane), but 
that’s a workaround.
11:49 perdix: Or wait for someone more knowledgeable to come online…
11:52 jesperronn: perdix: hehe thanks for your suggestions.. I tried to set 
TM_RUBY to /usr/local/bin/ruby (no Textmate restart). That actually gave an 
extremely strange error. 
11:53 jesperronn: Blank white "run" window only with this text: 
/tmp/temp_textmate.azBvzx: line 6: : command not found
12:02 perdix: jesperronn: Huh. Does `$TM_RUBY --version`, ⌃R work?
12:12 allan: jesperronn: the test with #!/bin/sh gave another result because 
I think you forgot to select BOTH lines
12:12 allan: jesperronn: instead of editing environment.plist try set PATH in 
TM’s preferences
12:12 allan: TM_RUBY will not help you since it is your script (using ‘env’) 
that needs the correct ruby
12:13 allan: so only setting PATH properly can fix this
12:13 allan: your second error must be because you set TM_RUBY to something 
non-existing
12:39 jesperronn: allan: where do I set PATH in preferences? 
12:40 jesperronn: allan: do you mean set a shell variable "PATH" in the 
advanced preferences>shell variables?
12:45 allan: jesperronn: yes
12:45 jesperronn: allan: I can see that setting a shell variable PATH in 
advanced preferences actually works! 
12:45 jesperronn: Why is this not different 'out of the box' 
12:45 allan: jesperronn: what do you mean?
12:45 allan: that TextMate should know how you want PATH setup?
12:45 allan: because that is impossible
12:45 allan: and it _does_ work out of the box
12:45 jesperronn: yes
12:46 allan: it just does not work with custom ruby installs
12:46 allan: emphasis here on custom ;)
12:46 jesperronn: OK
12:46 jesperronn: I actually tried to remove the ruby 1.8.6 after upgrading 
but i had to undo because it gave me problems running ruby inside textmate...
12:47 jesperronn: Maybe it\s just my limitted knowledge of Textmate internals
12:47 jesperronn: Thanks a lot for help, allan, perdix and inner_six!
12:48 allan: jesperronn: essentially it’s pretty simple: PATH tells what 
locations programs should shell for commands (and what order)
12:49 allan: so if you want to install something new yet still keep the 
system version (recommended) then just install it wherever you want and put 
that location first in the PATH variable
12:49 allan: that environment.plist failed for you is likely due to a typo on 
your part
12:49 allan: that is the system-supported way to set environment variables 
for all apps launched by Finder though
12:50 allan: where Terminal runs a shell so it additionally has the profile 
files
12:50 allan: and TextMate has the Preferences → Advanced…
12:50 jesperronn: allan: what I do not understand is why to use 
environment.plist and not .profile or similar
12:51 jesperronn: So the error on my side is probably that I added path 
settings to .profile
12:51 allan: jesperronn: .profile is for your shell
12:51 allan: i.e. only bash etc. will execute .profile
12:51 allan: so it works when what you launch from TM goes via bash
12:51 allan: but not when it is run w/o a shell
12:52 allan: this is analogical to asking in #bash why you have to setup 
stuff in .profile when you have Preferences → Advanced → Shell Variables in 
TextMate ;)
12:52 jesperronn: So for me to learn a lesson here: I should always use 
environment.plist and remove all custom $PATH adjustments in .profile
12:52 allan: jesperronn: it doesn’t really matter
12:53 allan: really, only shell and TextMate care about PATH
12:53 allan: so whether you set it locally for each of the two apps or 
globally makes little difference
12:53 allan: and in a shell context editing .profile is probably easier
12:53 allan: plus does not require re-login to have changes take effect
12:53 allan: also, in .profile you can have “code”
12:54 allan: e.g. you can add to your PATH, conditionally set something etc.
12:54 allan: where environment.plist is 100% declarative
```

PS. Thanks to Peter Haza (phˆ) for digging up the archived conversation.

PPS. Note to self: Clean transscript from irrelevant status changes with: cat tmp.txt \|grep -v "has left"\|grep -v "has joined" \| grep -v "is now known as"
