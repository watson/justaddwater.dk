---
title: ".NET tips for my development environment"
date: "2008-10-09T13:21:43"
slug: "net-tips-for-my-development-environment"
url: "/2008/10/09/net-tips-for-my-development-environment/"
wp_id: 958
categories: ["Web Development"]
tags: ["development", "iis", "microsoft", "visual studio", "Web Development"]
---

At a recent project I had to work in a full-blown .NET environment. Here are some of the tips I collected from my colleagues.

Visual Studio\
I added the methods below in the Macro editor (Tools \> Macros \> Macros IDE)

Stop the build on error. When an error occurs I am notified instantly and able to fix faster.

        REM Stop the build process when the first error is encountered
        Private Sub BuildEvents_OnBuildProjConfigDone(ByVal Project As String, ByVal ProjectConfig As String, ByVal Platform As String, ByVal SolutionConfig As String, ByVal Success As Boolean) Handles BuildEvents.OnBuildProjConfigDone
            If Success = False Then
                'The build failed...cancel any further builds.
                DTE.ExecuteCommand("Build.Cancel")
            End If
        End Sub

Timestamp on build complete. This is a great helper because I usually don't waste braincycles on keeping track on when I last build the code. The timestamp occurs below the output which makes it instantly clear if it is necessary to rebuild. This usually saves 10-20 daily rebuilds each wasting one to four minutes.

        REM Output timestamp in build panel on build complete
        Private Sub BuildEvents_OnBuildDone(ByVal Scope As EnvDTE.vsBuildScope, ByVal Action As EnvDTE.vsBuildAction) Handles BuildEvents.OnBuildDone
            Dim win As Window = DTE.Windows.Item(EnvDTE.Constants.vsWindowKindOutput)
            Dim ow As OutputWindow = win.Object
            Dim owPane As OutputWindowPane
            For i As Integer = 1 To ow.OutputWindowPanes.Count
                owPane = ow.OutputWindowPanes.Item(i)
                If owPane.Name = "Build" Then
                    owPane.Activate()
                    owPane.OutputString(DateTime.Now.ToString)
                    owPane.OutputString(Environment.NewLine)
                End If
            Next
        End Sub

Creating/copying websites in IIS. (Local Windows XP development). In our project we had to add a handful of different websites. Using the helper tool called "adsutil.vbs" in Inetpub/AdminScripts can help:

    cd C:\Inetpub\AdminScripts\
    CScript adsutil.vbs enum w3svc /p

This gives you a list of each website with an index, that you can use for copying websites. This way, you add only one website, and then copy it. Much easier.\
`CScript adsutil.vbs copy W3SVC/1 W3SVC/2`

Now you have added a new site and all you have to do is go into the IIS Manager and configure it. You can configure the site from the command prompt as well, but usually it's a one-time effort and it's faster to do that from the manager.
