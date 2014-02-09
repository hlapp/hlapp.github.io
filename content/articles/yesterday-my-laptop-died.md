Title: Computer failure without the agony - wishful thinking?
Tags: hardware, cloud
Slug: hardware-failure-and-productivity-loss
Date: 2014-02-08 23:57:57

Yesterday my laptop (a Macbook Pro) died. It showed the first signs of severe illness 2 days earlier, seemed to recover at first after a lot of agony, but then deteriorated rapidly yesterday morning. This post isn't about a story of data loss, even if that is sadly still more common than it needs to be. My laptop is backed up to the cloud almost continuously throughout the day. What I am worried about is not having lost any work;  it is the loss of productivity, which can be just as bad[^1].

More specifically, recommended practices and supporting technologies for preventing data loss in computer crashes have matured enormously to a point that anyone can implement them on their own, without the need for a technically sophisticated setup or IT department. However, based on what I've observed so far in my own quest to regain productivity, practices and technologies to limit productivity loss and disruptions seem to be still in their infancy. 

## Zero productivity loss: A dream, or a reality soon? 

A day later, I'm mostly up and running again, even if with lots of caveats. But a day of lost productivity is still an awful lot. Imagine a world in which recovering to full productivity after losing your laptop takes the same or less time than making a cappuccino. Hardware can and will fail. Imagine a world in which, just as we now keep a spare flashlight or a spare battery, we keep a spare laptop. If the one you use fails, you simply switch to the spare. No sweat, no anxiety, no panic, just an additional trip to the post office to ship the broken one to repair.

I will argue that we are as close as never before to having the technologies that allow us to strive for zero productivity loss from hardware failure not only for application servers but also for personal computing. But getting there will require rethinking from the ground up what a personal computer is. 

## The efficient restore problem

Due to the warning signs 2 days earlier, I had a freshly imaged loaner laptop already waiting for me. The question now was probably similar to what it is for most people in this situation: How efficiently and quickly can I get a sufficiently working environment up on the loaner to regain productivity, ideally in a way that will also limit the disruption from transitioning back to my own laptop once it is back from repair.

What do I need to get back up to running? As is probably fairly typical, I need a variety of more or less specialized software, where specialized means anything that isn't commonly installed on a freshly imaged system. For me this includes tools such as git, Emacs, a GNU C compiler, comprehensive Perl and Python installations, R, Protégé, and various productivity software. I also need access to a large variety of files, including the digital file drawer of administrative documents, presentations, manuscripts, data files, ontologies, and source code.

My initial, and as it turned out rather ill-advised approach to getting this all back was along the thought of _bulk restore_. That is, rather than wasting my time thinking about, picking, and choosing exactly what I will need (and in the course forgetting half of it), I checked the base directory for all code bases and all documents in Crashplan's backup archive and hit the "Restore" button. To my disappointment, after the restore commenced I soon found it occupied with lots and lots of expansive codebases and numerous voluminous documents that I had forgotten I even had lying around, and that for sure I wasn't going to need during this temporary period working off of a loaner.

So while the bulk document restore was chugging away, I abandoned my original plan to restore custom software by bulk restoring `/Applications` and `/usr/local`, and instead tried my hand at a different approach, which I'll call _project environment restore_. By project environment I mean the collection of tools, libraries, files, and configuration settings that are needed to do the work on one particular project. (As tasks in a project may change over time, so may the constituents of the project environment.) For the project I picked (due yesterday), I needed to operate on a git repository, make multi-way branch merges and resolve resulting conflicts. It took me less than 20 minutes to install git and TextWrangler from the web and to clone the repository. The vast majority of that time was spent installing the OSX developer tools, which git requires --- and helpfully prompts for.  

## Why efficient restore is very difficult today

How many projects do you work on at a given time? Perhaps a handful? Even if we assume up to a dozen, 3 hours to restore all of them to working order would still be a fraction of what any Time Machine or online restore from backup takes. While it sounds intriguing, in practice this extrapolation is invalid for a number of reasons, including (and not limited to) the following:

* In science and software engineering, projects often need software tools that need to be custom-built and/or configured, which can be very time-consuming.
* A project may involve data files that individually or together are far too big to be held on Dropbox or a git repository.
* Development and analysis tasks may require pre-populated databases and precomputed output from preceding steps that are time-consuming to recreate, or that even exceed the capacities of the temporary loaner equipment.
* A project may require browsing through an indeterminate number of documents, such as manuscripts, presentations, and the like.

On top of that, there is no 1:n relationship between projects and the tools and files that comprise their environment. This is most obviously true for general-purpose tools, but it also applies to data files, manuscripts, presentations, and even source code files. We don't want our files duplicated all over the place, so instead of by project, we organize them by type. "Documents" go into `~/Documents`, and if you're like me, you have one folder under which you have all your code repositories. This makes it yet more difficult to restore a project in a targeted way.

## Rethinking the personal computer

If you're like me, your personal computer, from the days they were all desktops to today's laptops, represents a lot of investment, time much more than money. It has numerous customizations, some of which required manual tweaks and anxious waiting whether some code builds or not. There are databases and other servers with carefully crafted machine-tailored configurations. If you're like me, you are not a sysadmin, and thus you didn't document let alone script how you did those customizations. You probably have data and analyses on your machine that you know work with the versions of the operating system, libraries, and software you have installed.

Even if everything is backed up well, there is a lot of time investment at stake when such a workhorse fails. What if we moved the workhorse into the cloud, and recast the personal computer at which we work as a vehicle for running a web browser on a high-quality screen, and for plugging in peripherals such as keyboard, mouse, camera, and speakers[^netbook]?

Virtual machines have numerous advantages to physical ones. For example, they can be cloned in minutes, shut down or spun up when needed, and their CPU and memory capacity can be elastically expanded or shrunk. Even though these advantages are well appreciated and widely applied for hosting machines that function as servers, the adoption of cloud hosting for personal computing is taking root only very slowly. 

Perhaps part of the reason is that it requires behavior change, and the technologies that minimize the required change or make it transparent are only now beginning to mature. We have grown accustomed to [personal computers becoming exponentially more powerful](http://en.wikipedia.org/wiki/Moore's_law), allowing them to run ever-more resource-hungry and sophisticated software. Seemingly reducing one's personal computer at its pinnacle of computational power to a machine that simply runs a web browser can easily strike as irrational in light of that trajectory.

## An example available today: Google's Chromebook

The sea change may have started. For example, Google and other vendors sell [Chromebooks](http://www.google.com/intl/en/chrome/devices/), for which from the perspective of an end-user [Google Chrome](https://www.google.com/intl/en/chrome/) is essentially the only software they'll run.

Locally, that is. Through Chrome, users have access to the Google Docs online office application suite, as well as all the other Google Apps.  I have used Google Docs regularly for a long time, and I suspect most of you have, too. With [Paperpile](http://paperpile.com) working as well as it does, managing citations and generating a bibliography is now possible, too. What about developing, debugging, and building software code, though? Although I suspect that most developers are still using local software for these tasks, increasingly sophisticated online code editors have been sprouting up[^code editors].

Manipulating, analyzing, and visualizing data, especially on a large scale, perhaps remains for now as the last frontier. However, even that frontier is crumbling. For data analysis in R, [RStudio can be run as a server](https://www.rstudio.com/ide/docs/server/getting_started) with a web-browser interface. For command-line tools, there are various [web-based SSH terminal clients](http://en.wikipedia.org/wiki/Web-based_SSH). [Open Refine](http://openrefine.org/) is already a web-application. 

## Zero productivity loss is all but one opportunity

Chromebooks sell for a lot less than ordinary laptops[^chromebook], yet I don't think that their main, or even a realistic promise is to make personal computing cheaper. Instead, these kinds of devices, and their underlying concept of ubiquitous personal computing, hold numerous opportunities for making computing flexibility, choices, and power available to everyone. And freedom from hardware failure-induced agony.

Some of the money saved one could use to keep a spare device. So that when one device gets sick, you switch to the other with zero loss of productivity. One could use some of the savings to occasionally spin up an AWS machine for the data crunching or code compilation that are difficult to achieve through dedicated web-applications.

If Chromebook-like devices become common, they may profoundly change IT on-boarding procedures at institutions. Today, such procedures are focused on procuring, configuring, imaging, and maintaining physical hardware.  In the future, the focus of on-boarding could instead consist of determining the best mix of online private and public cloud service subscriptions for a new employee, and then setting them all up automatically through APIs.

## Postscriptum: A birthday, and a disclosure

Tomorrow is the birthday of one of my daughters. She'll become 11 years old, and one of her presents will be a [Chromebook](http://www.google.com/intl/en/chrome/devices/hp-chromebook-11/). That decision is the result of a lot of agonizing over what's right for her yet affordable, and is entirely coincidental to my laptop's life event. Many of the thoughts written up here have, however, been prompted by the coincidence of having to think through what's right for her, and being forced to ask whether what I have myself is really as right for me as I've complacently taken it to be. One of the many blessings of having children.

[^1]: As is probably the case for many, my laptop is my single central workhorse. I am giving a [major talk](http://www.iscb.org/cshals2014-program/cshals2014-keynote-speakers/cshals2014-keynote-lapp) in just 3 weeks, and need all the time I can get to prepare for it, on top of a dense schedule of other deliverables I need to keep moving. Of course, if that wasn't enough, I also got ill myself. This or some other combination of aggravating factors is probably true for most who have been hit with computer failure.

    There is an all too human temptation to bemoan how such disrupting events seem to mysteriously occur at times we can least afford them. However, if we lead busy lives organized towards productivity, arguably the chances that a potentially productivity disrupting event falls in a time we aren't pressed for time is vanishingly small. That's possibly a problem in its own right, but outside the scope of this post.

[^netbook]: This idea is not exactly the same as, but was obviously preceded and precipitated by the invention of [Netbooks](http://en.wikipedia.org/wiki/Netbook).

[^code editors]: See for example [Cloud9 IDE](https://c9.io/), [CodeAnywhere](https://codeanywhere.net/), or [CodePen](http://codepen.io/), just from a simple Google search. I'm sure there are more.

[^chromebook]: For example, [Google quotes the 14'' HP Chromebook](http://www.google.com/intl/en/chrome/devices/hp-14-chromebook.html#hp-cb-14) as starting from $299.