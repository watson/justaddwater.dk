---
title: "Git extract folder from project with history and tags"
date: "2016-11-02T20:40:32"
slug: "git-extract-folder-from-project-with-history-and-tags"
url: "/2016/11/02/git-extract-folder-from-project-with-history-and-tags/"
wp_id: 1809
categories: ["Code", "git"]
tags: []
author: "jesper"
---

This is a short note regarding the use of `git filter-branch` when you want to split a git repository and preserve the history.

I had some issues in finding the correct parameters. In case this also can help others, you can find the command here.

In case you are not yet familiar with the possibilities of `git filter-branch`, I suggest you look into the  [Git book: Rewriting history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#The-Nuclear-Option:-filter-branch), which has a good introduction to the command.

Now, to start you should clone the repository you want to change (since you will completely rewrite history in the new repos).

 

In short, without further explanation:

ORIG=path_to_original_repos\
DEST=destination_of_rewritten_repos\
DIR=directory_you_want_to_extract_from_ORIG

git clone \$ORIG \$DEST && \\\
cd \$DEST && \\\
git filter-branch --prune-empty --tag-name-filter cat --subdirectory-filter \$DIR -- --all

A few notes:

- `--prune-empty` will remove all commits that has no relation to the folder you extract
- `--tag-name-filter cat` will also rewrite any tags you put on the commits that are rewritten
- `--subdirectory-filter` takes a foldername as parameter, but I needed to add `-- --all` to make it work
