---
title: "Rewrite author/email in git history"
date: "2015-01-21T15:25:38"
slug: "rewrite-authoremail-in-git-history"
url: "/2015/01/21/rewrite-authoremail-in-git-history/"
wp_id: 1733
categories: ["git"]
tags: []
author: "jesper"
---

After my harddisk crashed and I reinstalled the machine recently, I misconfigured my Git to set EMAIL as email address.

This made Git history look horrible, with incorrect email, image. By accident I even wrote an incorrect name at one point.

[![git history github](/wp-content/uploads/2015/01/Screen-Shot-2015-01-21-at-15.16.09-300x265.png)](/wp-content/uploads/2015/01/Screen-Shot-2015-01-21-at-15.16.09.png)

 

Note the missing image.

 

Now it turns out my git repository was full of EMAIL instead of my correct email address.

\$git log --pretty=fuller -1 9461d8b\
commit 9461d8b\
Author:     Jesper Rønn-Jensen \<EMAIL\>\
AuthorDate: Tue Jan 13 09:56:13 2015 +0100\
Commit:     Jesper Rønn-Jensen \<EMAIL\>\
CommitDate: Tue Jan 13 09:56:13 2015 +0100\
    adding install of hipchat and sourcetree

 

I had to rewrite the history in order to fix the email addresses. Turns out `git filter-branch` could help:

 

NEW_MAIL="jesp....@gmail.com"\
git filter-branch --env-filter '\
\> if \[\[ "\$GIT_AUTHOR_EMAIL" = "EMAIL" \|\| "\$GIT_AUTHOR_EMAIL" = "\$NEW_MAIL" \]\]\
\> then\
\> if \[\[ "\$GIT_AUTHOR_NAME" = "Ben Alman" \]\]\
\> then\
\> GIT_AUTHOR_NAME="Jesper Rønn-Jensen"\
\> GIT_COMMITTER_NAME="Jesper Rønn-Jensen"\
\> export GIT_AUTHOR_NAME\
\> export GIT_COMMITTER_NAME\
\> fi\
\>\
\> GIT_AUTHOR_EMAIL="\$NEW_MAIL"\
\> GIT_COMMITTER_EMAIL="\$NEW_MAIL"\
\> export GIT_AUTHOR_EMAIL\
\> export GIT_COMMITTER_EMAIL\
\> fi\
\> ' -- --all

10 seconds later, I could push the changed repository up back on the server. The result was much better:

[![github log images fixed](/wp-content/uploads/2015/01/Screen-Shot-2015-01-21-at-15.24.24-203x300.png)](/wp-content/uploads/2015/01/Screen-Shot-2015-01-21-at-15.24.24.png)

 

Nice result :) All of this trouble was because I wanted to script the setup of a new machine. I used [my clone of Ben Alman's dotfiles](https://github.com/jesperronn/cowboy-dotfiles/commits/master "Github.com: jesperronn/cowboy-dotfiles"), and this way his name slipped in before I figured out how to configure the .gitconfig file.

I really like that Git enables you to do almost anything. Especially that you can make mistakes and fix them later :)
