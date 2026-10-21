---
title: "Groovy for Hudson console"
date: "2010-04-20T12:25:23"
slug: "groovy-for-hudson-console"
url: "/2010/04/20/groovy-for-hudson-console/"
wp_id: 1305
categories: ["Code"]
tags: ["Code", "groovy"]
author: "jesper"
---

Hudson continuous integration server has a console which is good for testing scripts and access to commands that your Hudson jobs need.

The hudson console only let's you run Groovy script. To run commands on the machine, Groovy has the method `"string".execute()`. So now I can use this snippet to test versions of Ruby, JRuby, etc:

    def commands = ["ruby --version", "gem environment", "which ruby", "which gem", "jruby --version"]

    commands.each{
      run(it)
    }

    def run(cmd) {
      //def proc = commands[1].execute()
      def proc = cmd.execute()
      proc.waitFor()

      // Obtain status and output
      println "return code: ${ proc.exitValue()}"
      println "stderr: ${proc.err.text}"
      println "stdout: ${proc.in.text}" // *out* from the external program is *in* for groovy

    }

Example borrowed from and shrinkwrapped from [groovy.codehaus.org/JN1015-Collections](http://groovy.codehaus.org/JN1015-Collections)
