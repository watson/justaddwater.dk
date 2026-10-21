---
title: "PhantomJS 1.7 build for Linux 64 bit"
date: "2012-09-28T09:54:39"
slug: "phantomjs-1-7-build-for-linux-64-bit"
url: "/2012/09/28/phantomjs-1-7-build-for-linux-64-bit/"
wp_id: 1663
categories: ["Code", "Continous integration", "Testing"]
tags: ["phantomjs", "testing"]
---

At a project I work on, we needed PhantomJS to run from a Redhat Fedora 64 bit machine.

Since phantomJs is just released this week, I needed to build it myself.

 

I post this link to the binary in case it can benefit others.

 

[PhantomJs 1.7.0 built on Linux Redhat Fedora 64 bit](http://dl.dropbox.com/u/54307969/phantomjs-1.7.0-linux-x86_64.tar.gz)

 

 

PhantomJS is a fantastic tool for automating tests, since it is a headless browser which we wrapped in our automation framework to run javascript based tests very fast and easily.

 

I followed the [build instructions](http://phantomjs.org/build.html "Phantomjs 1.7.0 official build instructions") (the instructions described for Amazon EC2 also worked on the fedora I am running).

```
sudo yum install gcc gcc-c++ make git openssl-devel freetype-devel fontconfig-devel
git clone git://github.com/ariya/phantomjs.git
cd phantomjs
git checkout 1.7
./build.sh --jobs 1

#(added step below by me)
sudo yum install upx
After finishing the build, run deploy/package.sh which creates PhantomJS binary tarball that can be moved around and/or extracted to a different location. This is the correct way to install the built binary into an arbitrary directory, i.e. do not simply copy the executable as it won't work.
```

The link I posted is the actual outcome of ./deploy/package.sh

 

For other operating systems, you could probably just get the binary at the official [PhantomJs download page](http://phantomjs.org/download.html).
