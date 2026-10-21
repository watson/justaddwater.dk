---
title: "Batch Screenshots with webkit2png"
date: "2012-01-23T15:00:53"
slug: "batch-screenshots-with-webkit2png"
url: "/2012/01/23/batch-screenshots-with-webkit2png/"
wp_id: 1544
categories: ["Code"]
tags: ["automation", "Code", "screenshot", "webkit"]
author: "jesper"
---

For projects I sometimes have lots of screenshots which I have to repeat whenever I change subtle things in the CSS or HTML.

I ended up creating this little handy script based on webkit2png (download source)

```
#!/usr/bin/env sh
HOST="http://localhost:8080/myproject/viewer"
/usr/bin/python webkit2png -F -o "01dashboard" $HOST/dashboard
/usr/bin/python webkit2png -F -o "02showdetail" $HOST/detail
/usr/bin/python webkit2png -F -o "03listpage" $HOST/list
```

This created the following 3 files in my directory:

```
$ ls -1
01dashboard.png
02showdetail.png
03listpage.png
```

Really simple and easy to use.

It only requires you to download webkit2png script ([download on github](https://github.com/paulhammond/webkit2png)).
