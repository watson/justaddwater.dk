---
title: "Justaddwater.dk hacked"
date: "2007-11-15T00:28:38"
slug: "justaddwaterdk-hacked"
url: "/2007/11/15/justaddwaterdk-hacked/"
wp_id: 779
categories: ["justaddwater.dk", "WordPress"]
tags: []
author: "thomas"
---

### The non-technical version:

Last Thursday we unfortunately had an intruder on Justaddwater.dk. The cracker used a flaw in our blogging software to gain administrative access to it. With this access the cracker placed a secret backdoor on the server.

It seems that the intention of the cracker where to use our server to host illegal copies of movies as part of a larger pirate network. To our luck the technical skills of the cracker where very bad (*read: [script kiddie](http://en.wikipedia.org/wiki/Script_kiddie "Wikipedia: Script Kiddie")*) and the attempt to upload files to our server was not successful. The cracker therefore quickly gave up and did not try to access to backdoor afterwards.

We have now upgraded our blogging software to the newest version effectively closing the security hole and have reverted his (or hers?) changes and damage to the system.

We have tried to track his every move in our system, but cannot guarantee that he at some point didn't get a copy of all our commenter's e-mail addresses. We are pretty sure he was not after this information, and it does seem like he did not retrieve them, but we are not a 100% sure.

I know some of you use unique e-mail addresses when writing comments on our blog. If you are such a person and ever get any spam on this unique e-mail address, we would very much like to [hear from you](/contact-us/ "Contact Justaddwater.dk").

To those of you who subscribe to our newsletter, you can rest assure that your e-mail addresses where never in any danger. They are safely kept at our service-providers and the intruder have not had access to them.

For more information on how we store user information see our [Privacy Policy](/privacy/).

### Info to fellow WordPress users

The versions of WordPress affected by this security issue are:

- The entire version 2.1.x branch
- In the 2.0.x branch, every version below 2.0.11 is affected

If you are still running WordPress version 2.1.x we urge you to quickly upgrade to a newer version (2.2 or above). If you are running the older 2.0.x branch you can upgrade to version 2.0.11.

### All the technical goodies

[The bug in question](http://trac.wordpress.org/ticket/4322 "WordPress Trac: #4322 (Sql injection blind fishing exploit)") is a serious SQL injection bug affecting `/wp-admin/admin-ajax.php` where the attacker can perform any SQL command on your WordPress database (including wiping it out completely!).

In our case the cracker "only" used it to gain administrative WordPress access and updated the WordPress "upload_path" to point to the servers `/tmp` directory. He then uploaded a PHP script to this folder and added it as a WordPress plugin by manipulating the "active_plugins" option in WordPress. The purpose of this plugin was to lay dormant until a call to a specific URL was detected. This secret URL would then render a backdoor interface instead of the regular justaddwater.dk. You can see the backdoor interface by clicking the thumbnail below:

[![justaddwater-hacked.png](/wp-content/uploads/justaddwater-hacked.thumbnail.png)](/wp-content/uploads/justaddwater-hacked.png "justaddwater-hacked.png")

After looking at the Apache log files we can see what the cracker actually did to gain access and what he used that access to do.

First he made a very strange call:

    "GET /wp-includes/js/tinymce/wp-mce-help.php HTTP/1.0" 200 7411 "-" "-"

I have no idea why he called this URL first. My guess first was that this was a way of detecting which version of WordPress we where running, but after investigating I can see that this file exists also in versions not affected by the bug.

Secondly he called the URL affected by the SQL injection bug several times (actually 159!):

    "POST /wp-admin/admin-ajax.php HTTP/1.1" 200 2 "-" "Mozilla/4.0 (compatible; windows 5.1)"

Every call looks the same except for the size of the response in bytes following the 200 response code (in the above log entry it's 2, but sometimes it would be 298 or 299). It would have been during these calls that the cracker gained administrative access to WordPress. The cracker also created a new post that he would later use as a placeholder for the PHP script he where to upload.

Now followed 8 calls to options.php:

    "POST /wp-admin/options.php HTTP/1.0" 200 1248 "http://justaddwater.dk/wp-admin/options.php" "Opera"

Notice how the user-agent changes all the time. This could be different scripts running, set to identify them selfs differently. My guess is that he used these calls to change the "upload_path" option and the "active_plugins" option. He could have done this via SQL injection though.

Then came 10 calls to upload.php, the script used to upload pictures etc. to posts:

    "POST /wp-admin/upload.php?style=inline&amp;tab=upload&amp;post_id=-1 HTTP/1.0" 200 1150 "http://justaddwater.dk/upload.php?style=inline&amp;tab=upload&amp;post_id=-1" "Opera"

My guess is that he used these calls to upload the backdoor script to /tmp. Why he needed 10 I don't know.

Then came another 15 calls to options.php:

    "POST /wp-admin/options.php HTTP/1.0" 200 1230 "http://justaddwater.dk/wp-admin/options.php" "Opera"

It's not quite obvious why he made these last calls, except to maybe clean up something he made earlier.

Now came a very strange call to upgrade.php that I can't figure out why he made:

    "GET /wp-admin/upgrade.php?step=1 HTTP/1.0" 200 1172 "-" "-"

This script is used to upgrade the WordPress database after installing a new version of WordPress. He might have used some of the previous requests to prepare an "upgrade" script that he could then run this way, but why didn't he just use the SQL injection technique from before?

Finally he accessed his newly created backdoor, looked inside our `/wp-content` folder, did 3 POSTS (that I suspect where file-upload attempts) and then left never to be seen again.
