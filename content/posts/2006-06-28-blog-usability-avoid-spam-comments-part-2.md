---
title: "Blog Usability: Avoid Spam Comments (Part 2)"
date: "2006-06-28T19:26:09"
slug: "blog-usability-avoid-spam-comments-part-2"
url: "/2006/06/28/blog-usability-avoid-spam-comments-part-2/"
wp_id: 344
categories: ["Blogging", "justaddwater.dk", "WordPress"]
tags: []
---

![Can of SPAM](/wp-content/uploads/2006/06/spamcan-small2_resize.jpg)In our previous article [Blog usability: Avoid spam comments](/2006/06/24/blog-usability-avoid-spam-comments/ "justaddwater.dk: Blog usability: Avoid spam comments") we discussed the two ways we currently where fighting spam comments on our blog:

1.  Use Akismet for Wordpress
2.  Make a spam filter against BBCode like "\[/url\]"

The latter being a quick and dirty solution we had to implemented to deal with a lot of spam comments that for some reason where slipping though Akismet.

Today we then implemented one of the possible future protection mechanisms that we also discussed: **Remove standard URLs for posting comments**.

WordPress uses `/wp-comments-post.php` as the receiving URL when posting new comments. Some spammers exploit this and automatically send their spam directly to that URL (without actually filling out the comment form on the blog). The popular solution has therefore been to rename the file `wp-comments-post.php` and update the comment form to use the new filename.

**But there are two drawbacks to this solution:**

1.  When updating your WordPress installation to a newer version the renamed file is of course deleted and replaced with a new version with the old name. If you forget to rename the new file nobody will be able to leave a comment on your site since your theme still points to the renamed version of the file (which is now deleted).
2.  If you publish your WordPress theme or move it to another WordPress installation chances are that the comment form will break because the file hasn't been renamed on other systems.

The solution we implemented today doesn't actually rename the `wp-comments-post.php` file. Instead we deny all access to it via htaccess and point to it via a symbolic link we create in our theme directory. We then make our comment form point to this symbolic link instead.

Since the symbolic link is located in our theme directory it is never deleted when we upgrade to a newer version of WordPress and if the theme is copied to another server the symbolic link will be copied as well — hence the comment form is not in risk of breaking.

### Simple 3-Step Implementation Guide

If you don't have shell access you must ask your host provider to do this for you

1.  **Create Symbolic Link** Create a symbolic link from your theme directory to the `wp-comments-post.php` file:Go to the directory of your current theme (in our case `wp-content/themes/jaw/`) and execute the following command: ln -s ../../../wp-comments-post.php my-comments-post.php In this example we name the symbolic link `my-comments-post.php`, but you can choose any name.

2.  **Update Comment Form** Still in your theme directory you need to find which files that contain links to the `wp-comments-post.php` file. To do this execute the following command: grep -l wp-comments-post.php \* You will then get a list of the files you need to edit. Now update each file so that the link to `wp-comments-post.php` instead point to the symbolic link. This is usually done by changing the following:

        &lt;form action="&lt;?php <span style="color: #ff0000">echo get_option('siteurl');</span> ?&gt;/<span style="color: #ff0000">wp-comments-post.php</span>" method="post" id="commentform"&gt;

    To this:

        &lt;form action="&lt;?php <span style="color: #ff0000">bloginfo('template_directory');</span> ?&gt;/<span style="color: #ff0000">my-comments-post.php</span>" method="post" id="commentform"&gt;

3.  **Deny Access To Old File** To make sure that the old `wp-comments-post.php` file cannot be accessed from the internet, edit your `.htaccess` file in the root of your website and add the following to the top of the file:

        &lt;Files wp-comments-post.php&gt;
        &nbsp; &nbsp; Deny from all
        &lt;/Files&gt;

    To verify that the update to the htaccess file works, try to open the `wp-comments-post.php` file in a browser (i.e. http://www.yourblog.com/wp-comments-post.php) and see if you get a "403 Forbidden" page telling you that you do not have permission to access the document.

**Remember:** Make sure to test that your comment form still works when you are done with the modifications.
