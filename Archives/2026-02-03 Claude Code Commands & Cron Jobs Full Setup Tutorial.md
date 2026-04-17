---
type: Web
authors: '[[Allie K Miller]]'
url: 'https://www.youtube.com/watch?v=l6V0u3ZIgDI'
published: 2026-02-03T00:00:00.000Z
created: 2026-04-06T00:00:00.000Z
tags:
  - automatyzacja
  - narzędzia-AI
  - context-engineering
---


![](https://www.youtube.com/watch?v=l6V0u3ZIgDI)

In this video, I walk you through one of my favorite Claude Code use cases—building a custom slash command that checks my Gmail for urgent emails I haven't replied to, then scheduling it to run automatically every Friday morning.  
  
I'm terrible at email. Instead of paying for another tool, I built my own system in Claude Code using commands, arguments, and cron jobs. Now I'll show you exactly how to do it yourself.  
  
What you'll see in this video:  
✅ The /UE command—a custom urgent email tracker I built in Claude Code  
✅ How to pass arguments to commands (check last 3 days, 1 week, 1 month)  
✅ Setting up Google Workspace MCP to connect Gmail  
✅ How to schedule commands with cron jobs (run every Friday at 9am)  
✅ Stacking commands—triggering one command from inside another  
✅ Real example: building a /client-prep command that pulls from Gmail, Slack, Notion, and the web  
✅ How to brainstorm custom commands for your specific business  
  
  
\~~~~~~~~~~~~~~  
  
  
🔗 Get started with Claude Code:  
https://claude.ai/referral/6bgDpTbmjQ  
  
🔗 Claude Code for Absolute Beginners: STEP-BY-STEP TUTORIAL:  
https://www.youtube.com/watch?v=v1ynWeHhzXs  
  
🔗 Claude Cowork Lightning Demo for Business Users:  
https://www.youtube.com/watch?v=\_nH1fc9HBSA  
  
  
\~~~~~~~~~~~~~~  
  
  
📌 The AI Fast Track \[free email course\]: https://www.alliekmiller.com/the-ai-fast-track  
📌 AI-First Academy: https://www.alliekmiller.com/ai-first-academy  
📌 For Entrepreneurs, Solo-Founders, and SMBs: https://www.alliekmiller.com/ai-first-entrepreneur  
📌 AI with ALLIE Newsletter: https://aiwithallie.beehiiv.com/  
  
👀 Follow me here:  
https://www.linkedin.com/in/alliekmiller/  
https://www.instagram.com/alliekmiller/  
https://twitter.com/alliekmiller  
https://www.tiktok.com/@alliekmiller  
Business inquiries: contact@alliekmiller.com  
  
  
\~~~~~~~~~~~~~~  
  
⏰ Timestamps:  
0:00 Intro: Why I built this  
0:34 The /UE command explained  
2:43 Passing arguments to commands  
7:05 Setting up Google Workspace MCP  
9:12 Cron jobs: scheduling automated tasks  
15:00 Verifying your setup & safety checks  
20:19 Creating custom commands  
21:24 Brainstorming commands for your business  
25:21 Building /client-prep live  
27:37 Stacking commands together  
29:04 Wrap-up

## Transcript

### Wprowadzenie: Dlaczego to stworzyłem

**0:00** · I want to show you one of my favorite use cases for Claude Code. And this is pretty complex when you think about all the different integrations that I set up, but I'm going to make it very easy for you cuz I've already done the hard work. So, this is going to be the exact prompt that you can use. Essentially, what I found is that I'm terrible at email. And I know that there are platforms out there like Superhum or Poke that help you manage email, but I just wanted to quickly set something up on my own. So I decided to create a new command. That command is slashue.

### Wyjaśnienie polecenia /UE

**0:38** · UEe standing for urgent emails. So, essentially what I wanted is every single Friday at 9:00 a.m. I get a review of all the urgent emails that I need to reply to and whether or not I've replied to them. I also wanted to be able at any point to ask for my most recent urgent emails that I haven't replied to because maybe on a Tuesday night at 1:00 a.m. I also want to see what urgent emails I haven't replied to.

**1:06** · So I both set it up as a command that I can ask any point uh you know show me urgent emails for the last one day, one week, one month and also a repeated task something that is set up on a schedule which is very easy inside of chatbt and way more annoying inside of Claude. But here's how I set it up. So, um, the full prompt that it goes through is, and I love how it's, uh, formatted as well, right? We love structured prompts that use markdown. So, we've got urgent emails, check, check my Gmail, and I, you know, redacted my email so you guys can't see it, but presumably this would be your exact email address because the Google MCP requires that you pass it an email address. So even if you only have one email address that it is the only email address you use for every single thing and ever, you still have to pass in an email address. So check my Gmail blah blah blah for all emails read and unread. And this is because when I tested the original prompt that I was going back and forth with, it was only testing the read emails, uh, excuse me, the unread emails. And there were plenty of times that there was a red email that was urgent that I hadn't replied to. or maybe I sent a reply to someone saying, "Totally get it. Let me get back to you in 24 hours." So, there's a chance that I even replied to it and it is still not yet replied because the email is not yet answered. So, again, this went through a lot of testing. So, I wanted to show read and unread from arguments and I'll explain that in a second. Default last seven days that need responses. So if you give a command uh and I've showed this before where I had a command for uh passing a screenshot to the AI and I used slash SS to show screenshot. If you just say slash SS it'll just look at the most recent screenshot in the folder.

### Przekazywanie argumentów do poleceń

**3:04** · But I also gave it an argument so that you can pass it a value that it can then act on. So if I do slash SS2, it'll look at the two most recent screenshots.

**3:16** · SS17, it'll look at the 17 most recent screenshots. And maybe if I'm trying to compile, you know, let's say that someone was giving a presentation and I was taking screenshots of every single slide, I could say SS50 and pull that all together into a report or a PowerPoint. Don't do that with my presentations, but you can do it with with uh people who have said that you can share them. Um, so that is passing an argument for this email thing. I wanted to pass it an argument for how many days it should check. So if I said slueie, it's going to default to checking the last seven days of the email. And if I do slash UEIE 3 days or slue one week or SLUE 1 month, then it'll convert that into a day count and then run the actual search. Search for emails containing blah blah blah. It does do that search, but then it also just generally looks through my emails to see what it's looking for. So, response uh and by the way, if it didn't and if we felt that it was not catching enough, then I could edit that line. Uh then we've got response status tracking.

**4:20** · So, within each of those urgent emails, I was getting stuff back that, you know, I had replied to. And so, I would rather see all the emails and see which ones I've replied to than not to see all the emails and wonder what's missing. Uh, and I talked back and forth with claude code in planning mode to think through the best solution. So for each urgent email found, get the full thread, check if any of the replies are from me, categorize them still as needs, response or replied, and then the output format.

**4:49** · It sends me an email that is also from me. And the subject line is like, hey Ally, I've got hear this. Hey Ally, I've got all your email urgent urgent emails here. I can change it to whatever I want. I could put in the date, doesn't matter. And I get back this whole format. Needs responses do reply. Again, another edit that I gave it. It was giving me a summary of all the emails that I had to respond to um or not. And then I had to hunt down my own email.

**5:21** · Like, God, just make it faster. So, I asked for it to have the link to each of those emails that I have to respond to in the email because then it's just one click. And then I was like, what if I just want to open all of them? So then I have a summary of all the links at the top so I can just click through all.

**5:37** · Unfortunately, in Gmail, you can't just have it uh open like 20 different uh email links cuz they'll think it's spam.

**5:44** · Okay. Starts with the need response at the top. At the top, include the open all urgent emails link that combines all the thing. It doesn't do this. Uh then send an email to me with all those linked grouped above. Okay, here are the things that one would need to set up.

**6:01** · First, you need to title your shortcut.

**6:03** · Mine is urgent emails. If you're wanting to, you know, find all emails related to yellow school buses, you can do slash yellow, whatever. Um, I like to do short things because also you can do a slash and you can search through all of your slash commands inside of Cloud Code anyways. So, even if you kind of forgot which one was the right shortcut, you can go into it. You can also set up uh multiple shortcuts that open up the same one. So if you're like, I'm going to do slue, but just in case I forget that, I'm going to do slash urgent email and slurgent emails, and they'll all kick off the same thing. Um, where all of these are stored is going to be in a markdown file. The argument that I just mentioned is going to be the the window of time that it's going to check those emails. I always give it a default so that I don't always have to type in an argument. I give it uh examples. So last 3 days, last 24 hours. Again, I can pass it any unit of time and it'll do the conversion. And then the big thing that you will need to set up is a uh Google MCP. MCP is uh model context protocol.

### Konfigurowanie Google Workspace MCP

**7:12** · It is a way that your uh systems can talk to one another. It's a it's a unified way that they kind of decide to have like a shared key between them so that all of these systems uh can talk to one another in similar in the way that we have um like API keys that allow us to go into an application and grab some certain information. MCP is another way of setting it up. So the way to set this up, you can literally just ask cloud code, hey, I need to get into my Gmail.

**7:44** · How do I do that? you could give it a little bit more detail and say, "Hey, I need to set up this whole urgent email thing. Ally told me to set up some sort of Google MCP. Can you walk me through that?" Um, there are multiple Google MCP GitHub pages. Some are uh created by Anthropic themselves. Some are created by strangers on the internet. even if they have a lot of stars, if the GitHub page is very popular, I felt safest going with the anthropic version even if it doesn't have all the bells and whistles. Fine. So, I specifically picked the anthropic Google MCP setup and it'll walk you through all the steps. It'll take you to the Google link. It'll help you set up an OOTH.

**8:27** · It'll help you go through all the permissions that you have to kick off.

**8:31** · Um, if you didn't pass in an email address, it'll flag that that is an issue that you need to fix. And you can just go into claude code and say, "Hey, it's asking me for this error thing.

**8:39** · Like, how do I fix it? Um, you can check documentation manually if you'd like, but you can just keep feeding back to cloud code what the errors were." I would say that the Google uh workspace MCP took me longer than I was expecting to set up. I was kind of expecting it to be like 10 minutes and it was maybe more like an hour because of all of the uh permissions that I needed to go through and I was learning all this stuff for the first time. Um, okay. That is the actual command. That is if I wanted to type in /wi just as we did. If I instead want to have it set up uh to run every single morning at 7 a.m., then I can set up what is called a cron job. Spelled C R O N. Cron job. Uh and I I don't think it stands for anything unless I miss something in class. But um cron is like chronological. Uh it's uh the root of time. And so it just means setting up a script or a command to run on some sort of schedule um in the background. So it's not like taking over your whole screen every single morning at 7 a.m. to run a task. It's doing it in the background and then it's able to complete it. And in this case, it completes with an email that it sends to me. So, we're going to, you know, I could show you just like um set this command up to be on a cron job that kicks off every Tuesday at 7 a.m. And every Tuesday at 7 a.m., it just looks for the most urgent emails of the last 24 hours.

### Zadania cron: planowanie zadań automatycznych

**10:22** · That is the type of prompt that you can give it. It is in natural language. I didn't even need to know that it's called a crown job. I could have just said that kicks off a task every Tuesday at 7 a.m. And I could have asked, "Help me think through potential solutions.

**10:36** · Help me weigh through the trade-offs of each. You know, I'm I'm a non-technical mother of eight that only has 10 minutes free every day." Or I'm an extremely technical, you know, based in Finland, engineer of 40 years. Help me think through solutions. Giving the system that context is going to help you think through the best solution for you. So you can give it a little bit of that context for here. We're just going to say kickoff crown job. And I'm just going to hit enter. We'll see what it comes back with. But that is how you're going to set up the command. So you can use it whenever you're going to set up arguments, how you can go through and set up the Google M Google Workspace MCP. How you can select different GitHub uh repos depending on your level of uh wantedness for amazing features uh versus what I would consider security.

**11:27** · Um, and that is how you can set it up.

**11:30** · This whole process, including the Google Workspace MCP, might take you um, let's say 2 to three hours if it's your first one. Uh, and you haven't set up any sort of command on your own, but it is going to save you, I think, that amount of time in one to two weeks. So, very much worth it. So, I'm going to run this. If it comes back with a bunch of private data, I'm going to clip the video off here. If it comes back with redacted things, great. I can even say keep it redacted and don't show my email. This is just a demo. Let's see if that helps.

**12:06** · Either way, my name is Ally Miller. I'm the number one most followed voice in AI business. I've got tons of free AI resources and courses at the link in my bio, and you can follow along for more.

**12:16** · Cool. Okay, so it created the script. Do I want to create this? I'm just going to kind of look through this and make sure that nothing looks very off. Um, things that you might be looking for. Is it accessing uh something that it doesn't need to access? Is it accessing something that you don't recognize the name of? Um, do any words say like danger or security? Um, do any words say like public? Right? So, you're looking for kind of keywords that set you off.

**12:45** · Um, keywords that you might not recognize. And so, I'm looking at this.

**12:49** · It's just showing me directory names.

**12:51** · It's showing me logs. I've also already created one before, so that gives me a lot of confidence. And cron jobs are perfectly fine. Um, so we're just going to say yes. And I'm going to say yes, and allow Claude to make all edits during this session.

**13:11** · And then it might ask you to spin up.

**13:14** · Let me see if it does this.

**13:18** · Um, it might ask you to spin up like a new terminal window and run a couple bash commands to be able to permission this cron job. You can literally ask it for step by steps. It might even have you switch from something called Vim to nano if you're on a Mac. It's just like switching the interface of your terminal to be able to get permissions done a little bit faster. Um, but again, all those things take minutes and you just go back and forth with Cloud Code to be like, I don't know what the heck you're talking about. Give me step by step.

**13:50** · Talk to me like I'm a preschooler. Talk to me like I've never seen a computer in my life. Tell me exactly where to point my cursor. Like, those are things that you can type. So, I'm just going to say yes. Um, for this, because it has to run commands on its own, you are going to have to allow it. Um I just want to see uh the other thing this 07 um the seven is the time of day. So if I asked it to check it you know 7 p.m.

**14:21** · this would have said 19. Um and so if I say allow it is gonna continue to run its course.

**14:32** · Do I want to proceed? Yep.

**14:35** · And then this uh cron tab dashl, it looks like a one, but it's an l. This is uh a list function. So this allows you to get a list back of the cron jobs that you've set up. Uh we're going to say yes to this.

**14:58** · And so you can see the cron job that I set up before looks up. I want to scroll back just so I can show you. You can see the other one that I set up is 9 because I had it check every uh Friday at 9 a.m.

### Weryfikacja konfiguracji i kontroli bezpieczeństwa

**15:14** · And then the days of the week also get numbers. So two is Tuesday, five is Friday. Uh and then the actual command that it's running is this uh d the actual command. Um and then redacted for demo. Amazing.

**15:34** · command. I'm just checking through.

**15:37** · There's an email check.

**15:40** · Oh, see, and it already it gave you the whole explanation anyway. So, I didn't have to do this. So, the minute is going to be at minute zero of the hour of 7 a.m. So, again, if it was at 7:30, this would have said 30 space 7. um day of the month. If that was restricted to say, you know, any um third of the month, then you would get these instead of the day of the week. So, if it's the day of the month or maybe if it's every January 3rd, then you can set that up as well. Uh you can even set up, you know, reminders for all of your taxes. You could say, uh, I have folders for all my tax documents. I have folders for receipts. You can set up a crown job to say, "Hey, every single uh 15th of the month, go through my receipts folder for anything that was saved in the most recent two weeks, um create a spreadsheet summarizing all of my receipts and go and fill out my uh Concur expense report or whatever online based on all that. That is what you can do with a sort of cron job something on command." Okay, so it is going to do that. Boop boop. Great. So that is now set up. So I can even say something like, is it set up? Did we do it right? Should I be nervous of this command? Is it safe?

**17:07** · To the extent that you trust AI answering these questions, great. You can also go into Google itself and just look up um, you know, what would make a crown job not safe? Or you can ask multiple LLMs and compare their answers.

**17:22** · So yes, it's set up. Let me verify. Give you an honest safety assessment. Again, do I trust it 100%? No. But I trust this. So yes, it is set up and active. I always like just confirmations of things that I've set up. I also pretty often will run tests. So if I set up a cron job for the very first time in my life, maybe I want to set it up for like 2 minutes from now. Um, things to watch out for, authentication. If your Google Workspace MCP O token expires, then it will fail silently. I could even say if it fails, send me an email saying um your your Workspace O failed. Set it up again. So, a lot of these sort of fallback things uh might be something you want to set up. Weekly email to yourself. If you forget that you set this up, it might be confusing later.

**18:11** · Okay, one email, who cares? Your computer must be on. This is a big one, right? So, if I'm sitting here going, "Okay, every single 2 am while I'm sleeping, blah, blah, blah, do this."

**18:23** · But then every single night I turn off my computer, that crown job is worthless. And so instead, uh maybe you might get a Mac Mini so that it's running 24 hours even if your computer is turned off or out of batteries. Uh maybe you set up a VPS um so that you can have a different server running so that it can always be running. Um again, that wouldn't use your main device. Uh for now, I'm just going to trust that my computer is going to be on at 7:00 in the morning, usually working. Um it skips that run, doesn't catch up. And so again, maybe I say uh that anytime I open my computer for the first time, it's going to check which chronobs ran whatever. Uh to test it right now, you can run this. Bottom line, it's safe. It only sends an email to yourself. The worst cases, da da da.

**19:13** · I like to ask questions of the code that I am writing. Um I think claude code is an unbelievable tool to complete tasks, to build things. Same with codec, same with Google anti-gravity, any of these systems that allow you to code and talk to your actual device. But if you use it to replace all of your thinking and just code for you without looking at anything, you will not learn anything and you'll probably fall into uh disarray when it comes to security measures. If however, throughout the experience, not just at the end like I showed, throughout the experience, if you say um hey, did I set this up right?

**19:51** · Hey, what's the smartest way of setting this up? Um, hey, I'm I'm uh thinking through these three potential problems.

**19:58** · Can you help me in planning mode think through how to solve these? That is the type of learning and thinking you want to do. And if it means that a task takes three hours instead of two, so be it.

**20:10** · Particularly if you are non-technical and this is a means of learning for free. So that is it. That is the uh command tutorial and uh setting up a cron job. Again, you can just dictate to cloud code any sort of command that you want. I can say set up a brand new command that um allows me to scrape the internet for any new scientific element that has been discovered.

### Tworzenie niestandardowych poleceń

**20:45** · and later I'll maybe set it up on a routine, but I just want to be able to do like slashcience and then it'll run that entire search for me and it'll look at the research in the last month before I ask it. And so it should look up today's date as well. Um, and I want it specifically to look up uh material science.

**21:09** · Could I have thought of any more generic thing? Um, so again, you can come up with a couple of these uh commands.

**21:17** · Hopefully, they are a little bit more helpful for your day-to-day business.

**21:22** · What I would suggest, um, great. It's going to do this whole search. What I would suggest for figuring out commands is giving it a ton of context on your life, on your work, on your career, on your business. Um, one thing that I've suggested before is creating a context vault. I have a lengthy document detailing every single thing that an AI system if it was born with no brain or if it got amnesia what it would need to know about my business to be hyper specific with context for my business. I can literally give a system that one document and just say come up with a list of commands that I can use for my business. Right? I could also say uh I run a 50 person consulting company uh in the supply chain space. I'm constantly doing research reports. I'm constantly talking to clients. We use notion, Slack, Google workspace.

### Burza mózgów na temat poleceń dla Twojej firmy

**22:22** · Uh can you come up with a list of potential commands that could be really helpful for my work? The criteria should be that it saves at least one hour per week.

**22:33** · So this is a very short type of prompt.

**22:36** · Again, I am very often giving it a page or multiple pages of context for it to uh work on my behalf. But let's see what it comes back with for command ideas.

**22:48** · Commands again saves you time. You can use them for tiny little things like check this screenshot. You could use it for massive things like running an entire research report. Um, and note that I didn't really give it crazy detail of different sources to look up or how to return the results to me. I'm just trusting it, but I can always go back and forth. Okay, so what are the types of commands that it sets up?

**23:14** · Supply chain news does all the news research for me and gives it to me summarized. Amazing. Uh, it can look up competitors. It can look at tariffs for me. Maybe that's especially interesting for supply chain. It can look up ports.

**23:28** · Uh, it can prep me for certain client meetings. It can, um, look through Slack. I could give it a Slack MCP to review and summarize every single thing in Slack, key decisions, blockers, wins.

**23:42** · That means that you could literally look up in Slack and say, month over month for the last 12 months, tell me how my team has progressed in Slack. Um, you know, and you can point at a specific channel or whatever. um like if you have a hiring channel, how are we progressing in hiring? If you have a um wins channel, you can point it to that. But you can literally say compare January to February to March to April, etc. And compare how decisive we've been. Score us on a scale of 1 to 10. Score each individual employee on a scale of 1 to 10. Give specific feedback for every single employee. write it up as a script that I can read at my next uh presentation. Give it to me in a PowerPoint. We're a very open and honest company, so I'm going to present this in a public PowerPoint to everybody. Um, also pre-draft emails if you have a Google Workspace MCB setup. Also, go ahead and draft individual emails to each of those people on my team. If it has the email addresses for everyone on your team, you can just have a document that lists out every single member of your team, their title, and their email.

**24:51** · um and pre-draft all those emails with specific advice for every single person.

**24:55** · Don't send it out just yet. I want to be able to review it, save it in my drafts folder.

**25:00** · That is the type of thing that you can do. You would need for that a Slack MCP, a Google Workspace MCP. Um if you want to run it on an automated sort of scheduled fashion, you can set up a crown job for that. And you can do that for any of these commands. And also top five, I'd build first. Great. Um, let's go ahead and build the first one. I'm dictating via whisper flow. You can type if you feel like living in the stone age. I enjoy dictating constantly. It's also why my voice is like always shot and that I keep cough drops usually within reach, but I think they're too many steps away.

### Tworzenie /przygotowanie klienta na żywo

**25:44** · Cool. Okay, let's go ahead and do this.

**25:47** · So it is naming that command to be client prep. It is creating the markdown file that's going to include all the directions that it's going to take.

**25:58** · I can I always do like to expand to see what the full prompt is. It also just helps me learn to see how AI is prompting itself. So step one, gather communications for the last 14 days.

**26:14** · Okay. Search for emails. anyone from that client domain to that client domain mentioning the client in Slack look up mentioning the client's name channels that might be dedicated to that in notion search for this go online and search for this compile the brief and also in the output format always love me some good emojis we can do this I can also have it in you know blocky narrative form uh active documents etc suggested talking points you might even say um suggested talking points yeah but also So, um, give me three suggested talking points based on the most recent three days of pop culture news and search trending Tik Toks. I don't maybe you can't search Tik Tok because it's usually blocked, but you know, search uh the word Tik Tok on Google and see what news is being written about Tik Tok. Uh, priority order. Awesome. The command has been created. Let me show the user what was built and how to use it. Cool. So, it does all this. It looks through Gmail, Slack, notionotion, web. Again, you would need connections into those tools. It's not just going to randomly hunt on your computer. It cannot use apps uh with like a cursor in the way that you might see in chatbt Atlas um or in Claude Co-work using the Chrome extension that it can. And so, example, if you do SLC client prep Walmart, then it's going to go and spin off Walmart.

**27:34** · You could even connect it to your you could stack commands. And then I feel like Oh my god, this demo's been so long. I'm so sorry, but this is so important. Um, I like stacking commands.

### Łączenie poleceń

**27:45** · So, if you have a command like uh slash and we'll get out of this expanded one.

**27:51** · If you do like slash daily brief, right?

**27:53** · And it goes through your Gmail um or your Google calendar and it summarizes your day ahead. Maybe it even looks at two days ahead so that if you have a crazy day two days from now, it'll tell you to get some admin work done now. Um, you can say inside the daily briefing, look up every single client that I have meetings with and then spin off a separate agent to go and run the client prep command with that client passed as an argument.

**28:27** · That is the type of stacking that you can do. I know a lot of you have watched my GBT stacking video. You can now stack autonomous commands that are integrated into actual systems.

**28:40** · That is the type of power that we got today with Claude code. It is unbelievably powerful. You can also go nuts and build this out in Claudebot, Open Claw, Moltbot, whatever it's called by the time you watch this. Uh if you're looking for a more secure option, then I would go the Cloud Code route with MCP.

**29:01** · Um, but yeah, thus concludes your commands, cron jobs, stacked commands, and everything tutorial. I hope you guys enjoyed it. I've been spending hours of my day, every single day inside of Claude Code. Whether you're using anti-gravity, codeex, cloud code, it doesn't matter. They all have similar functionality to this. And I hope you have a wonderful week, month, year ahead in your business. I think I already mentioned this in the middle, but we're just going to interject the CTA one more time. My name is Ali Miller. I'm the number one most followed voice in AI business. I've got two million people that follow me for the latest in AI business and tools and how they should be structuring their organization, how they should be training their organization, what sort of products they should be building, how they should be going to market, and I advise Fortune 500 companies and executive teams on exactly that. Hope you follow along for more and I'll see you guys
