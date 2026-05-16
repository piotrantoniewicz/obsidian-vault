---
type: "Web"
authors: "[[How I AI]]"
url: "https://www.youtube.com/watch?v=BTcG59ZR9sg"
published: 2025-12-29
created: 2026-05-12
tags:
---


![](https://www.youtube.com/watch?v=BTcG59ZR9sg)

Rachel Wolan, the chief product officer at Webflow, has embraced AI not just as a product leader but as a hands-on builder. A coder since age 16, Rachel has returned to her technical roots by creating a custom AI chief-of-staff application that helps manage her executive workload. In this episode, she demonstrates how she uses personal AI software to prep for meetings, triage her calendar, manage emails, and even get brutally honest feedback about how she’s spending her time.  
  
\*What you’ll learn:\*  
1\. How Rachel built a custom AI chief-of-staff application that integrates with her calendar, email, and more  
2\. Why building personal software can be a gateway to understanding AI’s capabilities for executives  
3\. How her AI agents help her prep for podcasts, dinners, and meetings with just-in-time information  
4\. The technical approach to building personal AI software using markdown files, API tokens, and multiple LLM interfaces  
5\. How Rachel organized company-wide “builder days” that dramatically increased AI tool adoption across her organization  
6\. Why she believes executives must lead by example in AI adoption to authentically drive organizational change  
  
\*Brought to you by:\*  
Graphite—Your AI code review platform: https://graphitedev.link/howiai  
Atlassian for Startups—From MVP to IPO: https://atlassian.com/startups/howiai  
  
\*In this episode, we cover:\*  
(00:00) Introduction to Rachel Wolan  
(02:26) Why Rachel started leaning into AI  
(06:26) Building an AI chief of staff  
(08:17) Prepping for the podcast  
(10:00) Rachel’s morning flow with her AI chief of staff  
(14:14) Designing a personalized interface with custom note cards  
(16:34) Getting “brutal truth” feedback from your AI assistant  
(19:34) Email triage and management workflows  
(23:31) Prepping for networking dinners and events  
(28:18) The result of building an AI chief of staff  
(30:09) Organizing “builder days” to drive AI adoption  
(35:38) Measuring the impact of AI adoption initiatives  
(38:00) Lightning round and final thoughts  
  
\*Tools referenced:\*  
• Claude: https://claude.ai/  
• Claude Code: https://claude.ai/code  
• Cursor: https://cursor.com/  
• Google Calendar API: https://developers.google.com/calendar  
• Gmail API: https://developers.google.com/gmail  
• Webflow: https://webflow.com/  
• Figma: https://www.figma.com/  
• Make: https://www.make.com/  
• Hex: https://hex.tech/  
  
\*Other references:\*  
• The complete beginner’s guide to coding with AI: from PRD to generating your very first lines of code: https://www.lennysnewsletter.com/p/the-complete-beginners-guide-to-coding  
  
\*Where to find Rachel Wolan:\*  
LinkedIn: https://www.linkedin.com/in/rachelwolan/  
X: https://x.com/rachelwolan  
Webflow: https://webflow.com  
  
\*Where to find Claire Vo:\*  
ChatPRD: https://www.chatprd.ai/  
Website: https://clairevo.com/  
LinkedIn: https://www.linkedin.com/in/clairevo/  
X: https://x.com/clairevo  
  
\_Production and marketing by https://penname.co/.\_  
\_For inquiries about sponsoring the podcast, email jordan@penname.co.\_

## Transcript

### Introduction to Rachel Wolan

**0:00** · So, you've built yourself an AI chief of staff.

**0:03** · The AI chief of staff is actually something that I have been trying to build since I started vibe coding. There's a lot of repetitive things that I have to do. For example, like prepping for podcasts and speaking engagements and stuff like that. And so, I've built out an agent that preps me.

**0:18** · Let's go into a specific workflow of how this chief of staff actually helps you with do something. And I think you did a little prep for this podcast.

**0:25** · I basically prompted and said, "Hey, let's generate a how AI flow." And so I was trying to get it to tell me what should I actually demo that is going to be part of this chief of staff app. And then what actually ends up getting output is this. It gives me an executive summary. Here are three different ways you could tell me about yourself and web flow.

**0:43** · Just the ability to be prepped even in a few minutes ahead of these things can really make your life better.

**0:51** · \[music\] Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive here on a mission to help you build better with these new tools. Today's episode is all about the AI native executive. We have Rachel Woolen, CPO at Webflow, who's going to show us how she uses AI, cla \[music\] day using AI as an executive.

**1:16** · She's also going to show us her formula for teaching teams how to use AI, drive adoption, and get them in those new tools with excitement. Let's get to it.

**1:30** · This episode is brought to you by Graphite, the AI powered code review platform helping engineering teams ship higher quality software faster. As developers adopt AI tools, code generation \[music\] is accelerating. But code review hasn't caught up. PRs are getting larger, noisier, and teams are spending more time blocked on review than building.

**1:52** · Graphite \[music\] fixes this. Graphite brings all your code review essentials into one streamlined workflow. Stacked diffs, a cleaner, more intuitive PR page, AI powered reviews, \[music\] and an automated merge queue. All designed to help you move through review cycles faster. \[music\] Thousands of developers rely on Graphite to move through review faster so you \[music\] can focus on building, not waiting. Check it out at graphite dev.link/howi ai to get started.

**2:20** · That's graphite.link/howi aai. Rachel, welcome to how I AI. The reason why we are doing this podcast together is we were sitting at a very recent San Francisco based AI event and we were talking about how so much of the discourse is around the AI native PM the

### Why Rachel started leaning into AI

**2:44** · AI native engineer basically like the AI native IC and we spent a lot of time on that topic here at how I AI but you and I have been chief product officers and we want to talk about the AI native executive and I think your workflow and the tools that you have built yourself are such a great example of somebody with, you know, as I say, a very fancy se-level title who is actually leaning into not only getting hands-on with these tools, but building things that help them do their job better with AI.

**3:18** · So, how did you get here? Because I will tell you, not every executive is as into this as maybe you and I are. So, what kind of clicked in your mind to get you thinking like my job's going to change. I really got to figure this stuff out.

**3:31** · I started coding when I was 16 and, you know, it's obviously been kind of a lifelong journey of building and tinkering and, you know, making mistakes. And so, I I feel like I I kind of built that resiliency pretty early in life. And now, uh, in my my current role, you know, I probably hadn't coded in about, you know, six or seven years.

**3:54** · And then when all of the new appgen tools came out, I think lovable is like one year old now, um I was like, "Hey, I'm going to try this out." And you know, it was it felt magical, right? And I'd kind of played around with some of the earlier versions of GPT. Uh but you know when it was so when kind of like vibe coding started coming on the scene I actually built an app uh to capture my kids memories and that was the first vibe coded app that I built and I built it in a weekend and it was it just felt like something completely different than anything I had ever built before.

**4:24** · And you know here we are a year later and this is you know now I'm like sitting in clawed code all day and I you know this is an app that I kind of like I'm continually maintaining. You can see I'm running it on local host and you know I've probably have built dozens of apps this year. We just launched our appg gen product. So I feel like a lot of times when you're building AI native products you also have to be just in the weeds a lot and making mistakes. And I'll show you like this product is not perfect.

**4:56** · This is a product for one person right now. And so that's that's really you know kind of how I got started. And I think it's it's something that now is just part of my day-to-day. This is how this is my daily driver.

**5:09** · This is a story I hear a lot. It mirrors my own story. This is probably why you and I get along so well, which is, you know, started coding very early, a lot of self-taught stuff, and then, you know, get into these jobs where coding hands- on keyboard wasn't my job. And then in 2023, 2024, it just became easier to go 0ero to one on stuff. It wasn't that I didn't have technical skills. It was just I didn't have time to do things.

**5:38** · And so the ability to, you know, do AI assisted engineering or vibe coding was it just brought me back to the love of coding and building things.

**5:49** · And so I hear that a lot. I certainly feel that a lot. The second thing I hear a lot that I tell people who are like trying to motivate themselves to learn some AI skills is find something personal to work on. you said like this memory app for your kids and do it in a weekend. You will get hooked. I think these vibe coding platforms are some of the most addictive games on the market right now. And so again, you don't have to start with something at work. You can start with something that's personal.

**6:18** · And I think once you get hands-on and realize what's possible, it's hard to think that your day-to-day job is going to be the same. So, let's get into what you built because I feel like I need this. So, you've built yourself an AI chief of staff. Tell us more and how you're using it in your everyday life.

### Building an AI chief of staff

**6:40** · Yeah, so the AI chief of staff is actually something that I have been trying to build since I started vibe coding. This is actually the first app that I tried and then it didn't work the first time that I tried it and then I've just been kind of continually trying to build it. And what you'll see here is like kind of rotating uh agents. I've just kind of been, you know, ticking away different use cases. And then a big part of this is also, you know, I I really want to help my team level up.

**7:13** · And so it it would be inauthentic for me to tell them, hey, you need to prototype with AI if this isn't something that I'm doing every single day.

**7:22** · I completely agree. And one of the things I want to call out about how you're talking about building this software is one, you're building it for an N of one. You're building it for yourself, so it can be really hyper customized. two, you're building sort of a a multimodal interface to this in which it can be a web app or it could be something just like a little bit more close to the metal in terms of in the terminal or in cursor. And then I love this idea of being able to build ephemeral widgets that are useful that you can just toss away.

**7:53** · Like you may never look at this Q4 road map after Q4 again and you may want to do it completely differently the next time.

**8:03** · you can build these like little personal ephemeral apps and then toss them away when they're not useful to you. And so I think software has become as accessible as documents have if you can lean into some of these tools. And so let's go into a specific workflow of how this chief of staff actually helps you with do something. I think you did a little prep for this podcast. I did. So I will actually run different terminals that are all running Claude.

### Prepping for the podcast

**8:27** · I do this partially because, you know, I I want to make sure that I'm like not using too much context and then I find that when I when I'm asking questions that are of a similar ilk, I get better answers back um in that same terminal window. But I basically prompted and said, "Hey, let's generate um a how AI flow." And so I was trying to get it to tell me like what should I actually demo that is going to be part of this chief of staff app, right?

**8:56** · So it knows this structure and then what actually ends up getting output is this. So this is it gives me like an executive summary. You know if we were to vamp it would be like hey here are three different ways you could tell tell me about yourself and web flow.

**9:14** · I just love that you can do this on an ad hoc basis get a structured output feel very prepared. I don't know if you're like me and don't don't tell my my teams that work for me. I am a just in time executive which means like the 2 seconds before I'm walking into a meeting that's the time I have to prep for that meeting with very rare exceptions because you are just back to back to back to backto back things.

**9:36** · I I say sometimes to people the number one skill you need to learn as an executive is improv because you are just dropped into a wide variety of context. you need to be able to think on your toes. And so just the abil I had a chief of staff and just the ability to be prepped even in a few minutes ahead of these things can really make your life better. So let's go through Okay, this is a very specific example.

### Rachel’s morning flow with her AI chief of staff

**10:00** · It's sort of our meta example.

**10:02** · Yeah.

**10:02** · On how we're going to go through the show, but let's talk about your morning triage and how you start your day every day using this AI chief of staff.

**10:11** · That sounds good. So in this case, what I actually gave it was a question. I said, "Hey, how can I make my week, my last week better? What what could I have done?" Because I I think that I don't have a chief of staff anymore. I used to have a chief of staff at another company. And so I knew that this was something that they would be like kind of combing through my calendar and like, "Hey, you're not blocking your energy, right? Um and you're you're not like kind of taking care of yourself."

**10:35** · And so, you know, the other the the main thing that they kind of called called me out on, which I thought was really funny. Um, so we just had our customer conference about a month and a half ago, and you know, I haven't taken quite as many customer calls. And it's basically calling me out and saying, you know what, you're not spending enough time with customers, and that's where you get energy from. And so, it's basically like doing a time analysis on my external calls. I'm like, how is that possible?

**11:03** · And again, it did pick up. it wasn't like 100% correct. And so I think that but but it was kind of like a signal to me. I'm like, "Oh, this is a place where I need to go and like reinvest, right?"

**11:14** · And it's like, "You're a CPO with like no regular visible cause for contact. Fatal flaw." And I'm like, "Oh gosh."

**11:19** · Um, it's very like dramatic, right? Uh, well, how does this actually access your calendar? How have you technically built?

**11:26** · Good question. Um, so I went and I got a token from Google Cloud and I basically I'm not going to show it, but I I basically have it like in my uhv file and so but I didn't really like set that up myself. I mean I knew that this was the way that I was going to need to construct it because I had built other apps before. But let's see if I can find it. So this is like myv file.

**11:50** · I'm not going to show it to you because I'll have to like burn all the the tokens I have in there. but it's basically has a bunch of variables and so one of those variables is my Gmail. Um, and then it walks you through how to actually go and set that up. One of those variables is my uh Google calendar. And you know, then I give it certain authorizations.

**12:12** · So in the case with Google calendar, it can only read my calendar. In the case with Gmail, it can only create drafts.

**12:19** · It can read, it can uh archive, and it can create drafts and label. And so a lot of this is like thinking about how do I, you know, put the right guardrails in place. It's kind of like thinking about software, right? How do I put the right guardrails in place so that I don't make mistakes or the agent doesn't make mistakes? Um it's kind of janky software, right? Because I I mean I because I'm like, "Oh, this is like pretty powerful."

**12:43** · And then a lot of times I'll like go and kind of take some of the power away um when I realize I've given it like too much uh you know too much authority to act on my behalf. And so I think that's you know part of it is also like me populating my own you know kind of intuition about what feels good in working with agents um and what feels like it's kind of like overstepping.

**13:08** · Yep.

**13:08** · And so, are you coming to this every morning? And this is sort of a metaanalysis of your calendar, which again, I've had a chief of staff we did every Friday where we're like, what what are you doing, girl? Like, let's let's fix this. But tell me how you would use this on a daily basis.

**13:23** · So, tell me about my day tomorrow. What can I delegate?

**13:28** · And so, this will run for a couple of minutes. And when it comes back, it'll tell me this is what's coming up tomorrow. uh this is what I think you can actually you can do something else.

**13:39** · This is you know I think the the way that I would like to make this smarter is this is who you should delegate to and then you know I'm still kind of working on my my Slack agent so I I can't show you but what I want to do is basically like send notes to my admin and be like hey could we go do this and is this fetching the calendar events through an MCP? Is it is it some custom code that you wrote? This is fetching it through an API token.

**14:06** · Um, I don't think that there's an MCP that is like a a official official MCP. But what you can kind of see, this is why sometimes I like looking at my briefing. So, other things that I do here, you know, I actually have like a little um, you know, like a little like note card that I like to make for myself. I'm like, I did prep for you. That's good. And then, you know, I'm basically kind of looking at this.

### Designing a personalized interface with custom note cards

**14:34** · It the thing that I like about it is it like makes it just very easy for me to get a snapshot and and view it, but I'm still kind of like iterating on what do I want this um to be like.

**14:44** · Let's just take a pause really quickly on your web app while this is running in the background. And what I love about what you've designed is look, we're all running on Google Calendar or whatever, but you want it to look a certain way.

**15:02** · You want it to be designed a specific way. You want to have a Can you show us that little note card really quickly?

**15:08** · I I got this idea from Mark and Dreason about like what are my top priorities for the day and then did I actually accomplish it?

**15:19** · and hold your horses real quick. It's also extremely cute. So, for people that are not on YouTube and are listening, it is actually designed like a blue lined note card and it does this little flip.

**15:32** · Look at you product person. I I mean, this is one of those other things where when people talk about personalized software, they don't get to talk about the little like pieces of that you get to put in the app that just make you really happy. Okay. So, sorry. Sidecar on design. So, you have your top priorities.

**15:51** · Yeah.

**15:51** · I I just as a side note, like I almost redesigned the app last night because I was like, I wish it kind of felt more like Apple Notes. And I think that's like part of what is fun is like, okay, what would that actually be like if I translated this app and I had like a theme for it? And so, there's something there's something really fun about like actually getting to design again, but not actually I mean, it takes the amount of time.

**16:13** · It's not it's it's not at like the pixel level perfection of the incredible designers on my team, but it does at least convey like you know there there's a certain um Jennaqua of this like app that I'm trying to to capture to make myself happy.

**16:32** · Yeah, I love it. It's so great. Um okay, so here we go. Here we go.

### Getting “brutal truth” feedback from your AI assistant

**16:37** · Yep.

**16:38** · Okay.

**16:39** · Your your chief staff is very mean.

**16:43** · I tell it to be mean to me. That's why \[laughter\] I want it to like keep me in line. You know, I'm I'm one of those people who likes to try to take on too much, I think, sometimes.

**16:54** · Um, okay. So, it's basically telling me to make certain meetings async. That's a great idea. It's telling me to delegate a couple of these. This is also probably a great idea. I don't think I can delegate this one, but good call. Um, it's telling me there's too much clutter on my calendar. This is one of those things where somebody's just like, "Put something in my calendar. I don't know this person." Um, so that's definitely optional and I haven't accepted. And then it's like, can whatever director cover this and send me a summary. Can Right. And this is really helpful.

**17:23** · This is like forcing me to think about, okay, do I actually need to attend all these things that I've signed up for? And can I give myself a break during the day to do some work and, you know, maybe get home to my family at like a reasonable hour? I love these delegation messages because just as a human, it is very easy to identify meetings that you don't need

**17:46** · to go to and then you're like, "Oh god, how do I say I don't want to go to this meeting?" \[laughter\] So even getting that draft where you could just find I could just copy paste that into Slack is such a useful friction reducer in managing your own time. And again, we're talking about the AI native exec just too busy, over booked, under prepped, really just wanting to spend our time vibe coding if we're being honest. So, I think this is really, really useful.

**18:12** · And again, I I like this because it's very conversational as a chief of staff might be and really helps you sort of figure out what you can do with your calendar. And then I like how it's mean to you. What's the brutal truth? Let's look truth. Is that \[laughter\] I'm like, yep.

**18:37** · It's because being a senior PM sometimes sounds more fun than I know. I'm like, is that bad? Is that a bad thing? Um, \[laughter\] so for those again who are not watching, the brutal truth is you're operating as a senior PM, not a CPO. You're reviewing PRDs, approving scripts, and recording marketing videos. I mean, they're calling a spade a spade.

**19:00** · This is the behind the curtain stuff.

**19:02** · And I tell everybody this about the origin story of chat purity, which is they're like, "Why did you build chat purity?" And I was like, "Man, because no matter how fancy of a title I got, I still was writing PRDs all the time."

**19:13** · And so this is this is really really great. And then I love this idea of like the only thing that will matter in six months are is this conversation. What an amazing way to level up. So, chiefs of staff that are watching here, you need to end every meeting with your exec with the brutal truth. Um, and and build this for yourself. Okay. So, this gives you a really good prep for your day. I'm presuming you do a very similar workflow for email as well. What is outstanding?

### Email triage and management workflows

**19:42** · Can you just walk us through maybe just some of the problems that your email um chief of staff solves? Yeah, I mean I think that my biggest problem is that I'm I have like five I'm like 500 emails deep in my email, but it's basically archiving a bunch of stuff that I don't need um to it's keeping a few things in the inbox and then it's drafting a few responses and you know a lot of this is like I've been kind of like continually updating this particular agent to know where to draft responses.

**20:11** · Um, sometimes it draft responses, you know, like some random SDR inbounds to me and I'm like, "No, no, no. You don't need to like draft responses to this person, but a lot of times it'll be like, you know, somebody from like a like a partnership type of email will send me an email and it'll tell me, hey, you need to pay attention to this email." So, a lot of it is like trying to also know like when somebody's waiting on me and asking for some document to get shared, right?

**20:38** · And so, you know, this is like kind of a cursor view. and then I can go through my inbox like very very quickly. Um I'm I think the Slack version of this is going to be like an absolute game changer since we operate almost internally in Slack 100%. Um but that one has been a lot harder to digest even with like the where the models are at. It's like almost too much data to triage.

**21:02** · Yeah.

**21:03** · Um so I I feel like that's like my next that's my next hill to climb. What does that say about what we expect of humans?

**21:10** · That we are expected to triage a vast amount of very disperate information with a lot of disconnected context. So disconnected that fancy pants large language models cannot make sense of it.

**21:27** · But for some reason, us with our meat brains are expected to be able to do this. And I just think that is such an indictment of how we're expected to navigate the massive amounts of information as as people that are working on teams in these asynchronous or semi-synchronous ways.

**21:46** · Yeah, it I mean I think it's also become so different during you know like post pandemic and especially if you're working for a remote organization and you know I I think that that you know that we're obviously only what you know four years five years into that experiment and so I think that we haven't like the tools haven't quite caught up with what we need to kind of declutter our our brains um in through that kind of transition.

**22:13** · And so I I still think we're in like the early days of of how to effectively do remote work, but that's like a different topic for another podcast.

**22:22** · The early story of Atlassian is probably very similar to your own. At Lassian knows firsthand the challenges that startups \[music\] face every day and that the right tools are essential to go from MVP to IPO. That's why Atlassian \[music\] for startups gives eligible companies up to 50 seats free on the premium edition for products like Jira, Confluence, Loom, Jira \[music\] product discovery, Compass, and Bitbucket. So your team can use the best-in-class tools to plan, track, and collaborate on work, whatever that work might be.

**22:53** · Many of today's most \[music\] successful startups like Cloudflare, Canva, and Rivian relied on Atlassian \[music\] for their growth trajectory. And Atlassian wants to give that same opportunity to the next generation \[music\] of builders. They know how important it is to focus on building the right things \[music\] early. Whether you're in the sticky note stage or well on your journey, teams \[music\] at any stage can work smarter together. It's never too early to start with Atlassian.

**23:22** · Head to atassian.com/startups/howi for more details and eligibility. Okay, I want to do one more fun chief of staff example before we go on to our next workflow, which is how do you prep for dinners? Tell me I just this little tab is calling my name. I must know.

### Prepping for networking dinners and events

**23:44** · All right, so I'm going to a dinner tonight. Um it is called the CXO Collective. And what I did was I took a screenshot of this guest list. And so, you know, I'll show you. Uh, it's, you know, I basically literally just took a screenshot of this guest list and then I dropped it in here. So, you \[snorts\] can see the image that I dropped in here.

**24:09** · And then it it read each of them. And it I haven't looked at this yet, so I can't tell you if this is good or not. Um, buyer beware. Uh, it's free. So, um, and then it went and did search on every single person on that list. And then I have an agent that is basically kind of like going and like doing more analysis on like this happens to be one of my colleagues who's going to the dinner guy leaf and so you know like he was acquired. So it looks like they're like actually identifying the right person.

**24:40** · So it what it does is it goes and it does a search on the web then it does a search in LinkedIn then it goes and tries to do like more web search and you know it's like hey this is your colleague that pretty good and it it also has like the the other thing that I would say that I have given this is a lot of context about me. So let me see if I can just show you a couple of examples.

**25:02** · Yeah. So I have like some general about me documents like this is from like some communication workshops that I went to where this is like kind of how I want to communicate. This is like personal resources about me and they're all I try to do everything in markdown just so it's easier for the models to understand it. And then this I actually generated like a I try to generate this maybe once a month of like what are the new Web Flow products um off of our release notes so that it kind of like knows everything that we've released in the last couple of years.

**25:31** · Um, and so then it kind of knows a lot about me and then it's telling me about the venue. Uh, and then it's like what are hot discussion topics. Um, and you know I'm going to like an AI marketer kind of AEO answer engine optimization uh, dinner and you know then it's like created this full prep doc. So I'm like okay that's great. And then what you can see is I'm like can you add it to my dinner research tab? So the everything that's in dinner research is actually a markdown file.

**26:01** · So that's the other way that this has like worked really well. Um I could go and open this up in cursor if I could find that file and then but really I just find it easier for something like this to go into my chief of staff and then let's see pretty oh it's going to be a nice dinner and you know it's like these are my priority connections like conversation starters. Um, you know, I'm like this is like kind of the introvert in me or maybe the ambivert trying to like uh be prepped.

**26:29** · Um, just I love this because I am an introvert. I get invited to these dinners all the time. Um, and this is this is really great. One of the things I want to call out for how I AI um watchers and listeners is I recently did a mini episode on how to generate a markdown powered personal app.

**26:52** · And so, you know, instead of having to toss these files into a database or into a file store, you can just store them as markdown files inside your repo and then display them on the front end using a markdown renderer and then it looks really nice. So I think again when you're building sort of a personal um app for you know your own research or context just use markdown files as a source of truthful content and display those markdown files in a nice way on the front end. Simplifies things.

**27:23** · You don't have to think about a database.

**27:27** · And the benefit is then any of those markdown files can be referenced by any of the agents that you use for other things. So, you could go to Cloud Code and say something like, "Hey, um, grab the dinner prep from that steakhouse dinner I went to last month and remind me of who that person was at Twitter that I was supposed to talk to. I never got to talk to her and I want to send her an email."

**27:50** · Like, that kind of stuff can really help just make not only the the software, the personal software better, but also just your use of overall um, Aentic tools a lot better. Yeah, I I feel like it's been a game changer to start using markdown files.

**28:06** · Um, and then also start using markdown for even like PRDs. So, a lot of times I'm like updating this app and I have like kind of an ongoing PRD that's like self-documenting this app.

### The result of building an AI chief of staff

**28:18** · I love it. And so, what do you think the result of you building this chief of staff has been? Um, how has it helped you? Are you saving time? Do you feel like your life is a little bit better?

**28:28** · Obviously, you've learned more about AI.

**28:29** · kind of what is the outcome you've gotten here?

**28:32** · Yeah, I think that the biggest outcome for me has number one been really being like close to the metal in terms of like building out AI products and I am the one that is like you know able to have very very detailed conversations like for example I didn't get a chance to this morning but I'm going to go and start using Gemini 3 um as part of this app and there's certain types of um it's gotten me very close to our code base as Well, um, so for example, I, you know, I have like I I use codeex a lot.

**29:05** · Right now I'm only using it on this particular app, but I could like go and be like, tell me about uh this app. How is it built? And I think that that's really important to be able. So I also obviously have access to our rep our monor repo. And so a lot of times like this happens to be for telling me about this repository, right?

**29:33** · But this is like a really good starting point um for anybody who's going to go build something because then you can start to understand well how is this app that we build actually built and I think that that it was almost something that was inaccessible unless you were sitting there and like reading code which you know sometimes I do but I I think that this is like very accessible to anybody.

**29:56** · This is awesome. And again, you can just add modules, you can spin up new quad code interfaces, and then you can design whatever you want on the front end. It can look however exactly however you want, which I love. Well, I want to flip this to another use case in the second half of our episode, which is a little bit less about how you personally use AI, even though we've we've shown that a little bit. I do want to talk about how you get AI into your team.

### Organizing “builder days” to drive AI adoption

**30:23** · And so I want to talk about your builder days because I think you know what you're setting a really great example of is I'm a CPO. You say you think of yourself as an IC CPO. I I do as well which is like we're going to do the work. We're going to get into it.

**30:40** · Part of it is setting an example of how the work gets done. And then part of it is you have no credibility if you don't actually know what you're talking about to convince other people to do something in their job. And so this is a little bit of a different how I AI which is how I AI into an organization and you've done these builder days. So tell us a little bit more about this.

**31:03** · Yeah, so we did a builder day last Wednesday. Um so this is pretty fresh and that's the second builder day that we did in this particular way. So maybe first I'll talk about the results because I think that it's actually helpful to see that. So this is a screenshot from Hex that was a dashboard um that shows all of the roles under my team and then after builder day one which was just design we had maybe half

**31:31** · the team using cursor and you what what I think is really cool is like very few people were using it before that and then it became this like kind of sustained use because we helped people get over that hump and you know not everybody and then we just did a builder day part two And I'll talk about a little bit about how we actually ran that builder day, but we had design product uh data science, user research, analytics, engineering, you know, lots of different functions um build for builder day.

**31:58** · And what we realized in order to get more people over that hump, and by the way, I don't think this is everyone. I think we actually had something like 80 plus prototypes that were actually built that day. Not all in cursor. Um but you know, this is like I'm excited to see like does this continue to be sustained? um is this something that people start to use as part of their day-to-day?

**32:19** · And you know, I I really think about um an organization kind of similar to any normal distribution curve um where you're going to have, you know, it's the innovator's dilemma where you have like the early adopters, right? And you know, we've we identified a lot of these early adopters here back in like March, let's say. And then those people actually built out the scaffolding for May for our first builder day.

**32:44** · And then as we had more and more people working, we actually had like a bigger user group um that was inside our organization that were maybe the early majority.

**32:54** · And now we're starting to, you know, build into the kind of like middle part of that distribution or even maybe some of the lagards um that are by just trying to reduce the friction and then trying to lean into the people who are really embracing that technology. Um, and and I think it needs to be both, you know, a top- down mandate. Like I tell my team, hey, you can't get into a meeting with me without a prototype. So there's a mandate, but then it's also a bottoms up. So I think it kind of has to go both directions.

**33:26** · So this is the outcome you're trying to drive, which is like we want to use these tools. We want to feel like not just during this spike, but overall in our day-to-day, those tools are useful to my team. And so explain to us what a builder day is and how it drives you towards that outcome.

**33:42** · Yeah, so we're builder day is when our entire organization stopped doing what they're doing and they built a prototype for whatever they wanted it to be. Um, and the goal was really to boost confidence, um, spark adoption. And so we had a couple of different types of tools. Um, we lit up cursor, figma make, and web flow. Um, and I'll talk about how we actually enabled the organization around that. And then we actually had like different tracks for different types of teams. So we had different assignments for product.

**34:13** · We had, you know, you can explore a new product idea. um you can validate user interactions, you can test product concepts, you can build a full-end workflow, you know, we so we we also had them do like a a warm-up assignment and then we basically had like support channels. So we had a couple of engineers that were on call for this. We ran like a judging panel. So like me and the CEO and a couple of other crossunctional leaders were the actual judging panel. We had prizes, recognition, different categories.

**34:38** · Um and then we we you know really focus on like how do we measure success and do this again and so you know this is something that is like evolving for us. This isn't we we we definitely aren't like we've we've nailed every single part of this but I was really encouraged to see so many people actually like taking one step outside of their comfort zone.

**35:00** · Amazing. And so this is something that for the leaders out there that are just looking to like how can I accelerate adoption? how can I up, you know, upgrade our learning and development in the org, not in this ad hoc way. This is 100% the advice I give them. Um, a builder day, a hackathon, and it has to be a combination of tools, access, education, real prototypes, and prizes. People love the prizes.

**35:26** · And so if you can make this something really fun, I think it's a super effective way to engage the whole organization and just becoming more AI AI native. And I would I would just ask you, you know, what's the feedback from the team?

### Measuring the impact of AI adoption initiatives

**35:43** · What's the kind of before and after you're seeing from the team before and after these builder days?

**35:49** · Yeah, I mean, so I actually like copy and pasted literally the feedback that we got from our survey, so you can go and see it. Um, most people were not frustrated, which made me really happy, which meant that we had like gotten around of the a lot of the technical issues. I think people found it fun, empowering, motivating, and eye-opening. I don't think people understood what was possible.

**36:09** · Yeah.

**36:10** · And that to me was like the most heartwarming thing I could possibly imagine. Um, is all these people I I call it getting bluepilled, right? like all these people all of a sudden like stepped into a a new part of their professional journey and that that just made me really happy.

**36:28** · So to recap this for any of the CPOS or executives or aspiring CPOS or executives out there, you know, a couple takeaways from this episode is one, there is just no substitute for getting your hands on to these tools, especially coding things. I think is very important in almost any role. I've been saying over and over and over again, this is the era of the hard skill. And one of the hard skills I just think is going to become more table stakes is at least being able to use code to get things done.

**36:58** · Even if you can't be an exceptional software engineer, that you can build yourself custom software, especially markdown based um that has both sort of agentic access properties where cloud code could use it and web UI. You could run it locally if you don't want to deploy anything. it's not a big deal and it also helps you kind of bypass some of the um security concerns around using thirdparty tools because you're running things locally, you're using, you know, internally approved API keys.

**37:28** · All those sorts of things kind of help you um stay sandboxed in your environment. And then organizationally and culturally, these builder days can have a very repeatable structure. And so if people want this, I think you're going to share this repo and this resource with us so you can look at it.

**37:46** · there's a repeatable process for onboarding, educating, engaging, and driving sustained adoption of AI in your org through um these sort of spikes in builder days. And then you're just having fun. Are you having fun? Because I am having so much fun right now. And that's one of one of the reasons why I'm spending so much time on AI is it's just it's it's better than it used to be for my job. I think it's the most amazing time to ever be doing this job in the entire time that I've been doing it. Um, it's it's a hard job.

### Lightning round and final thoughts

**38:17** · I think it's just building products is hard, but it's never been more fun and the possibilities have never been, you know, quite so unlimited.

**38:26** · I completely agree. Okay, let's do some lightning round questions and then let's get you back to um I just have to call it out. Your two cursor windows down at \[laughter\] the bottom, one of us, as we say. Okay, so first lightning round question. This is hyper hyper hyper personalized software.

**38:46** · Is this a product or do you think that just every CPO needs to go out there and build their you know as I say artisal farmtotable chief of staff for your app? You know where where do you fall on this like personal software versus small market SAS for for something like this?

**39:04** · I think that parts of this are probably a product. Like I'd imagine that, you know, maybe Anthropic tries to build this themselves, right? Where it's like everybody's chief of staff, not just for a product leader. Um, that may not kind of get it everything that people want.

**39:22** · And so you may end up having kind of extensions off of that or right but I think there's going to be a whole ecosystem around how to actually like kind of get work done and what people are doing with MCPS is just the beginning. It's still like let me tell you like the very early days of being able to access company data. Um but I do think that this is an app. I just don't know if it's going to be exactly this form factor.

**39:47** · Yeah.

**39:47** · And then my second question for you, which is a little bit more on the people side, which is you clearly care about AI fluency, how are you hiring for that? How is your team reacting to it?

**40:01** · How are you evaluating and promoting kind of what's your framework for talent around this?

**40:06** · Yeah, I I actually tried to share a little bit of that in this um in this app so that you can kind of see that.

**40:13** · But I think that AI is almost like you have to look at each of the different dimensions of your team. Whether it's data and insights, whether it's tool fluency, you know, like builder culture, career ladder, interviewing, like you have to look at every single aspect of how you, you know, your operating system for your team and kind of like grade yourself and be like, how far have we moved um down this spectrum? And you know, in our case, like we're in the middle of redoing our career ladder.

**40:40** · Um, because I wanted it to be really clear to people that it's not just fluency, it's like I expect people to like lead and own and understand what is possible and push the limits of our product. Um, and you know, it's not just for themselves, it's for our customers. Um, and then I think you have to kind of like reinvent so many different parts of your your practice as a leader. Um, and so that's that's the skill that you kind of need to lead into as a leader is just like reinvention at all times.

**41:10** · Okay.

**41:10** · And then my final question for you, I ask everybody. You have dueling claws open too. So this is an interesting question, but when you are prompting and he's just not listening, he's just not giving you what you want or your chief of staff is too mean. This is really funny because usually I see so many AI agents be too nice, but yours is actually really mean. \[gasps\] What is your prompting technique? Are you an all cap? Your your AI is an all caps AI. So I'm curious if you go you hit hard right back at it.

**41:42** · What's your prompting technique?

**41:45** · My prompting technique is first when I don't like what it's giving me, I will clear cloud code. So, a lot of times I'll like clear it and then I'll try again and if I'm still not getting what I want, I'll be like be a 100x more this thing that I want or, you know, be 10x.

**42:02** · And so, it's like I almost use like 10x as like a little bit more and 100x as like go and just like rip it apart and do something else. So, this is a repeated tip. We heard this from Hillary at Whoop in one of our early Howi AI episodes, which is these models like numbers. So say be like 20%, you know, nicer or be 100x more harsh or make this three times as purple. Whatever it is, you can quantify it. It can calibrate um how it's working for you.

**42:33** · So great, great tip. Well, Rachel, thank you for joining us on how aai. How can we find you and how can we be helpful to you?

**42:40** · Yeah.

**42:40** · Uh thanks again, Claire. This is amazing. Um, I'mrachel woolen on Twitter and you can also find me on LinkedIn to follow me. Um, and I also recommend checking out uh webflow.com. We have a brand new appgen product that we just released last week. Uh, it's really for your marketing team to be able to do vibe marketing which is a whole new wave that we're riding. So amazing to be here.

**43:10** · Awesome. Thanks. And I appreciate you sharing all your tips on how I AI.

**43:16** · Thanks so much for watching. If you enjoyed this show, please like and subscribe here on YouTube. Or even better, leave us a comment with your thoughts. You can also find this podcast \[music\] on Apple Podcasts, Spotify, or your favorite podcast app. \[music\] Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. \[music\] See you next time.