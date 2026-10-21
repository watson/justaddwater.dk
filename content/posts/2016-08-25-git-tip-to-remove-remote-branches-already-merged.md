---
title: "Git tip to remove remote branches already merged"
date: "2016-08-25T10:54:43"
slug: "git-tip-to-remove-remote-branches-already-merged"
url: "/2016/08/25/git-tip-to-remove-remote-branches-already-merged/"
wp_id: 1798
categories: ["git"]
tags: []
---

Let's talk about source control and an efficient way of using Git.

I like the projects where you have a `master` branch and a few feature branches, which are actively being worked upon. Only a few branches are present at a given time, and this is less confusing for the contributors in the repository.

A couple of times I have been on a project where old branches were not cleaned up.

I found that it's really easy to list these branches and clean them up.

Step 1: List all branches that are already merged:

`$ git branch -r --merged`

Lists all remote branches which are already merged. In case you want to find the old ones, you can sort them by commit date with the flag `--sort=committerdate`

Example:

`$ git branch -r --sort committerdate`

Committerdate flag will put the most recent branches last (you can reverse with minus: \``--sort=-committerdate`\`.

Step 2: List only relevant branches.

The list returned from above will also contain origin/HEAD and origin/master with we have to filter out:

`$ git branch -r --merged | cut -d / -f 2 | grep -v master | grep -v origin`

we simply remove them with `grep -v`

Step 3: Feed list into a delete command

The above command will give you a list of branches to remove. Review the list carefully by printing each line:

`$ git branch -r --merged | cut -d / -f 2 | grep -v master | grep -v origin | xargs -n 1 echo`

When you are satisfied, you can remove each branch with a git push command. Example

`$ git push --delete origin merged_branch1`

You can simply repeat this for as many times as you have branches with the above expression. So, in total your final command will be:

`$ git branch -r --merged | cut -d / -f 2 | grep -v master | grep -v origin | xargs -n 1 git push --delete origin`

And done :)

This post is following my series of blog posts with [useful Git Tips](/2011/09/30/collection-of-useful-git-tips-to-get-started/)
