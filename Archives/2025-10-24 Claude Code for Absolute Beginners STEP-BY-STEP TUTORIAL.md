---
type: Web
authors: '[[Allie K Miller]]'
url: 'https://www.youtube.com/watch?v=v1ynWeHhzXs'
published: 2025-10-24T00:00:00.000Z
created: 2026-04-06T00:00:00.000Z
tags:
  - szkolenia-AI
  - narzędzia-AI
  - automatyzacja
---


![](https://www.youtube.com/watch?v=v1ynWeHhzXs)

In this video, I show you how to bring Claude Code directly to your computer—no engineering degree required. In this beginner-friendly tutorial, you'll see how this tool can automate tasks, organize files, and boost your productivity, even if you've never used a terminal before.  
  
What you'll learn in this video:  
✅ Simple installation walkthrough (I'll guide you step-by-step)  
✅ How to use Claude Code without memorizing complex commands  
✅ Creating and organizing files with plain English instructions  
✅ Finding and summarizing documents in seconds  
✅ Getting system information without digging through settings  
✅ Essential keyboard shortcuts that save you time  
✅ Privacy settings you should know about  
✅ Creating custom AI agents for your repetitive tasks  
✅ Managing multiple projects at once  
✅ How to queue up tasks and let AI handle them  
  
🔗 Get started with Claude Code:  
https://docs.claude.com/en/docs/claude-code  
  
Lenny’s post with more Claude Code use cases: https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code  
  
  
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
  
  
⏰Timestamps:  
0:00 Intro and who this is for  
1:09 What is Claude Code (local vs claude.ai)  
1:55 Install and setup  
8:46 Create and edit files  
13:45 CSV to dashboard  
22:44 Presentations from dashboard  
27:49 System utilities: Activity Monitor cleanup  
32:54 Power tips (modes, thinking, escape, permissions)  
36:24 Creating Agents  
43:06 Conclusion & final tips

## Transcript

### Intro and who this is for

**0:00** · Friends, this is going to be one of the messiest tutorials that I do, but it's so important that I didn't want to wait until my voice came back, which maybe will be in a week, who knows.

**0:11** · Uh, I wanted to show a tutorial on Claude Code.

**0:14** · Why? Because it's powerful and because really the majority of uh demos that I see are from engineers or from what I would consider very technical business people.

**0:26** · Um, I'll I'll link uh Lenny Rachitsky's newsletter. I think I think he did a wonderful job laying out non-technical uh or non-engineering use cases. And so this will be in addition to that. If anything, this will actually be a more basic tutorial than that for people who have never used Claude Code, don't really even know what it is, um have no idea how to set it up on their computer. And so I'm going to like walk through the docs.

**0:54** · Um, I'm going to explain how to set it up. It's already set up on my computer and I can't uninstall it, so there's going to be some steps that are going to be missing, but hopefully I can grab a friend who hasn't done it and record that as well.

**1:05** · Okay.

**1:06** · Claude Code.

**1:07** · Claude Code is something that is going to run actually on your computer. So this is not Claude.ai where you're chatting back and forth with a web-based chatbot or this is not like a mobile app. Though now you can access Claude Code on some of those things. Um, the thing that I want to show off is the fact that it can talk to your actual computer, talk to your file system, talk to your system settings, um analyze your activity monitor to be able to see your actual computer and not just things that happen to be on that website right in that moment that you happen to attach or that happen to be in the uh historical part of that conversation.

### What is Claude Code (local vs claude.ai)

**1:50** · So, you first have to install Claude Code.

**1:53** · Um, if you go to Claude docs, you can just copy this URL, docs.claude.com.

### Install and setup

**2:01** · Um, you can read this whole overview. I just want to jump us kind of to this quick start guide.

**2:07** · Um, there are two ways to install it.

**2:11** · There is a uh kind of older way and newer way.

**2:15** · So, this is an option. This is using Node.js. You just have to install a more recent version of Node.js. 18 is just the version. So, you can download this.

**2:27** · It takes like 2 minutes. You download it and then you would run this command, which we're not going to do.

**2:33** · What we are going to do is come down to, and I have a Mac, but if you have uh a PC, you'd use this one or this one.

**2:42** · Uh, for Mac OS, which is what I'm running, I'm going to copy this sort of statement and I'll explain at least the parts that I know.

**2:53** · Um, curl is client URL. So that's basically like, "Hey, you know, code, like I'm about to give you a URL. Get ready." And it's going to like point to something. And so this is kind of like you saying, "Hey, I'm about to link you to something."

**3:10** · Um, this like every single letter is a setting uh in how it manages that URL, so how it goes to the URL and kind of navigates.

**3:20** · Um, F is like fail silently. It's just a bunch of settings, honestly.

**3:27** · Uh this is never something that I really look into.

**3:29** · Uh cuz I'm also not an engineer. Okay. The this URL is where it's actually going to go.

**3:37** · And um this vertical line right here uh is called a pipe. So basically anything to the left of the pipe is like, "Go do this thing." And then anything to the right of the pipe is like, "And put it there." Uh so bash is is like a shell that can then do some processing. So, I'm basically saying, "Hey, I'm about to give you a URL, handle it in this specific way. Okay, great, here's the URL. Put it here."

**4:04** · Cool. So, I'm going to copy this.

**4:07** · The next thing that I want to do is I need to access a terminal. A terminal is where you can uh manage code, type in code, talk to your computer.

**4:17** · And so, um you can pull it up in a few ways. You can open up finder or if you're on a Mac, if you hit the little flowery command button to the right of the spacebar, you hit that, hold it down, and then hit space, you'll get a uh spotlight search that pops up. And so I'm just going to type in terminal.

**4:37** · If you're in uh if you're on a Mac, this terminal will already be in your Mac. You don't have to download anything. There are way fancier terminals like iTerm or WesTerm.

**4:51** · Uh for the most basic beginners, we're just going to start here with what Steve Jobs gave us.

**4:59** · Uh so you're just going to hit terminal and it is going to open up this blank terminal. Uh it looks scary cuz it's not that pretty, there's no buttons, uh there's no color. You can switch it to dark mode. I still prefer light mode.

**5:15** · Um, it's going to give you very little information. It's really just like the name of my MacBook Pro.

**5:21** · Okay.

**5:23** · If you have not yet installed it, you're going to paste in that thing that we just copied. You're going to paste in that curl command and then you're just going to hit enter on your keyboard.

**5:34** · What you'll see after you hit enter is that it'll actually go through the installation process. Um, if you have already installed it, uh then or excuse me, if you have not yet installed it, it'll ask you a bunch of questions, mostly in security and privacy. "Hey, do you want to enable this? Hey, is it okay if we do this? Do you promise that you trust us? Are we friends?" And you just have to decide whether you're going to say yes to all those questions or not use it. Uh so I said yes to everything.

**6:06** · Uh it is up to you. Evaluate at your own risk level, risk tolerance. Okay. So we see that with that native install option, literally all I did was copy, paste, enter.

**6:19** · And you can see that it is successfully installed. Installation complete.

**6:24** · And yet, we still don't really have uh information. This says like run Claude help and you're like, "How do I even run something?" All you're giving me is like a text box.

**6:34** · So, if I were to type in what that says and hit enter, that's what running is.

**6:43** · Run means type, enter.

**6:45** · Uh it's it's like texting. I feel like I'm like texting a laptop.

**6:50** · So, then I get this gobbledygook and you're like, "What am I supposed to do with that?"

**6:56** · We're going to skip over all that. I just wanted to show you that if you follow its own instructions, you're like, "Ah, this is not meant for me."

**7:02** · All we're going to do is just hit the word type the word Claude and hit enter.

**7:07** · And what you'll get back is um and I'm going to say that I trust it. You'll start to get back something that's very lightly visual. There's like a little uh robot dude uh and then you'll get um a prompt to log in.

**7:22** · You'll go through the login process. It will give you options to either go via Claude or Anthropic's API.

**7:31** · I would go with Claude, again for ease.

**7:33** · So I signed in with Claude. I It basically kicks you over to a website, you log in, it kicks you back. Takes 2 seconds.

**7:41** · Um and so you can see here that it says Claude Pro because the account that I connected it to is a Claude Pro account.

**7:50** · Okay. So, it's giving you one potential uh example, which is like, "How does file path work?"

**7:58** · We're not going to do that. Why on Earth would we point to that as the first question? Okay. I'm going to go to my handy-dandy uh tutorial plan that I have thrown together that I just want to show you what it can do.

**8:14** · So, as I said, it can help you with your actual computer.

**8:21** · And so what I'm going to do is drag over a window.

**8:26** · This is Sorry.

**8:29** · Um, this is my finder. So, this is where I can see all my files. I hid all my files so you can't see what clients I'm working with. Uh but I said hide it all.

**8:41** · I hid it all. So if I come here and I say uh create a new folder on my desktop called Oh my god, Ali.

### Create and edit files

**8:53** · \[laughter\] Uh what I love about Claude Code, which the team always thinks of like fun little ways to make it fun. Um, if you saw there was uh well, I'll call it out when I give it a longer task, but basically it comes up with these fun little like gerunds that's like canoodling, whispering, contemplating. And so it just has this like tiny little model that's coming up with that. It's just a moment of fun.

**9:17** · Uh great. So it's like, "I'm going to create a new folder. Are you good with that? Do you want to proceed?" Um, mkdir is make directory.

**9:28** · So this is basically saying, "Hey, go ahead and create, make it, a directory of users, me, desktop, that file." Just like when you're like trying to hunt down a file on your computer where you know where it's nested. So this is where it's basically saying, "Hey, do you want me to nest it like this? Do you want to create a folder?"

**9:48** · I can either say yes, yes and always I want you to do this forever and always this type of command without asking any permission, or no, you totally got that wrong and I'm going to fix it. Um for now, I'm just going to say yes. You can either hit the digit one or hit enter. Uh and so I just hit the digit one and you can see on the left it immediately created that folder.

**10:14** · And it then tells you back in your terminal, done. I've created the folder.

**10:20** · Awesome. You don't really have to talk to it. Uh it just makes me smile. Uh awesome. Uh go ahead and write a short story about an anxious anxious perfectionist robot and add that to the folder we just made. So, you'll note I'm not actually specifying and add it to this folder. I'm not providing the directory. I'm speaking to my computer management in natural language. And as it's doing this, here's the choreographing this that little model.

**10:58** · As it's doing this, I want you guys to feel, not like feel the AGI. I want you to feel this movement toward AI as an operating system. The fact that it can manage files on my computer. The fact that I can talk back and forth to it in not just language, but also actions.

**11:18** · The fact that I can approve actions immediately and it'll do it. So, if I were to open this right now, you can see there's no document yet because I haven't approved this plan. Um for now, I'm just going to say yes. The next one I'll do allow all edits.

**11:34** · But now immediately you can see that this .txt file is in here and we get the exact same thing. Except I need it in a Word So, you can go back and forth with file types um and then it will Let's see. Yep. Uh it added a second file that is in .docx and if we open that up, now the perfectly imperfect robot and it looks like a normal Word doc. Okay.

**12:09** · I might say, actually let's take a look at that story.

**12:13** · Unit 8891.

**12:15** · Let's go there.

**12:17** · Blah blah blah, Skinner's fine. Seven's are actually on page six. Okay, cool. So, if we say like change uh character name of this to Beatrice. Um and I do that, then it'll actually edit uh the file itself. So, I can ask for file edits. I could have said um do you want I want it as a new version, save it as version two, whatever.

**12:52** · And um you can see that the sort of pink color is the before, the green is the after, and the highlighted, the darker part, is the actual edit.

**13:06** · And so it's very transparent about the edit that it's making and so I'm going to say yes and actually I'm going to switch it to this yes, allow all edits during the session. And so I'm just uh going with the up down arrow to navigate between these options. I'm settling on two and I'm going to hit enter. So, now anytime that I ask for edits, it's just going to do it. So, it is going to update that document and then when we open it, we will see Beatrice instead.

**13:37** · I don't see any unit. I see Beatrice. Beatrice. Phenomenal. Okay. So, now that we have edited the story and saved it, I'm going to switch into some like data analysis. So, if I said um create a CSV in that same folder with fake like sales data. Shimmying. It's just like Claude, you guys are so fun. Um Okay. Also, you can kind of see that it's counting up. Hold on.

### CSV to dashboard

**14:19** · Sexy. Okay. It's counting up the amount of tokens that it's using. Um if you're trying to be very cost conscious and you're using API, um some people might um check in on token usage.

**14:36** · Honestly, it's a couple bucks. I wouldn't really worry about it. Um unless you're coding very large scale code bases, uh then it can quickly get into the thousands of dollars. But for little things like this, genuinely don't worry about that token count. Um if you see that it's running a muck, if you're like, I asked you to write two lines and you're already at 1,000 tokens, um you can just hit the escape button and it'll stop everything that's happening. And what I love about this uh Claude code is that I can already queue up my next prompt. So, I already know what I'm going to have it do.

**15:14** · Create an interactive dashboard to view the sales data in an awesome way. Uh we can go ahead and open that up just to double check that it made some nice fake data. Cool, cool. So funny, uh whenever you see these names in particular, like Sarah Johnson, Michael Chen, Emily Rodriguez, you know that someone asked Claude to come up with with characters. They always default to those. Um okay.

**15:46** · Create an interactive dashboard to view the sales data in an awesome way. While it is doing that, I'm going to show you what it looks like to queue up the next prompt. So, I'm going to hit enter on this.

**15:59** · Uh great.

**16:01** · Now turn that dashboard uh into a presentation style still in HTML, but allow me to click left and right to navigate between slides. So, I hit enter on that before the first ask was finished. So, you can see that because I already hit enter, it queued up that next prompt and it is already working on the second prompt that I gave it. It's already working on that like left right navigation sort of thing.

**16:45** · Um and you can see it right here. I'll transform the dashboard into a presentation style. I can queue up things, especially knowing you know, the order of operations that I might want to go in. Uh okay. So, it says, let's scroll back up. So, I said create that interactive dashboard.

**17:04** · It wrote all these lines. It wrote out the code to be able to build out that HTML page. And if I were to open this, it's going to open in a web browser and it opened on my other. Okay. It's missing all the data that we just gave it. So, I'm going to say the dashboard is pretty, but you forgot to include all the data from the CSV I want to visualize that CSV fake sales data.

**17:43** · And I don't like I wouldn't actually have to have said I want to visualize that CSV fake sales data. Um it kind of already knows because we're in the same conversation which ones I'm talking about. Oh, it is spazzing out. That terminal decided to spazz out. I'm not sure why that hasn't happened to me. Uh but what we're going to do is just start a new one. That's how you do it.

**18:09** · And we're going to say yes, we trust it. Okay. So, now because it doesn't really remember what we were talking about, you can either send it to that specific and I bet if I don't give it the full, let me just see this before I talk through what just happened. Yeah, I want to see if it finds it. Okay, so basically I I like tricked it.

**18:34** · Uh no.

**18:36** · Let's see. Okay, let me explain what I'm doing before I do this. Um CD is change directory. So, it means that you're like hanging out in some sort of folder \[snorts\] or uh area of your computer that's pointed at. And change directory is like, okay, leave this area, go to that area. Usually, if you're saying change directory, you have to provide the whole directory, that long thing of like users/alisonmiller/whatever.

**19:03** · Instead, I just wanted to see what would happen if I just gave it the actual folder name and it basically said like, I have no idea what you're talking about and it gave me an error. And then it said like, let me see what's available overall. And then it says, I don't see a directory, which makes sense.

**19:21** · And it says, do you want me to create it? Do you want me to search for it or check if it might have a different name. I'm going to say two and I want to see if it can find this uh folder that we had just created. And you can see right here that it found it on desktop and that it's creating the actual uh directory.

**19:40** · Um brilliant. So, I I can even point it generally at a file or a folder and I probably could have typed it in, you know, I probably could have said OMG GG Ali and it still would have found it. Uh okay, so now we are in the right folder where we're back to where we were. Um and just for Well, I don't have to control myself. I can say delete the HTML file in the folder.

**20:18** · do do do Found one file. Good. Deleting it. Yeah. Now it's gone. Perfect. Use the CSV file and create create an interactive dashboard um to visualize that bike sales data.

**20:45** · Cool.

**20:46** · So, hopefully this will um work. And then the goal after this Okay. I've got another one. But I'm actually going to queue up on my side. Uh do I want to Sure. A lot of these um All right, wrote Python. Hold on.

**21:24** · It's so funny. Like what I have found is that I just keep hitting enter. Like assuming that nothing really looks terrible. Like this is just in Well, it actually tells you what it's doing. Um it's installing two libraries. It like created code to be able to build the dashboard. And now it will use that code to create the dashboard.

**21:47** · Let's see.

**21:50** · Great.

**21:54** · Um you'll also see that like I'm only hanging out in one terminal. Uh I could have multiple terminals running. I could have six on my desktop. And if I'm not just assigning little like one-minute things here, uh if I'm assigning longer tasks or if I have automatically approved things, which I haven't done in these examples, then I could let six things run a muck and it's like having six interns.

**22:22** · Okay. So, if I open this, hopefully this HTML will look nice. Not sure why San Francisco's written diagonally. But cool. Okay, so electric glide 3 sale 3,000 I guess I sold a lot.

**22:37** · Uh awesome.

**22:40** · And so now I want to say um Uh what do I want to do?

### Presentations from dashboard

**22:48** · Uh turn that HTML dashboard into a presentation where I can navigate.

**23:05** · Okay.

**23:06** · Um I could have also given it like I want HTML JS CSS. Like I could have special um specified the format that I wanted in or where I want it to pop up. Um But you can see that it's walking me through the steps. Awesome. And again, if I'm like, "Oh my god, don't do that." And by the way, if I say now, "Make it version that looks totally like a McKinsey presentation."

**23:37** · So, I can queue up the next task. So, it is still working on that first presentation. I've then queued up the McKinsey one and you'll see I I had a typo on the word version. There we go. And it's going to handle it totally fine. Just like when you prompt with a typo, it's totally fine.

**23:56** · Okay. So, we're just going to keep saying yes to these things. Um again, I like it when it prompts me with each of these just as I'm showing people. When I'm working on my own, I just approve things. Especially if it's like create a presentation. Very low risk. Um And while it is uh figuring that out, hopefully we will then get this sort of new files. Make them HTML files.

**24:29** · So, I can immediately show them in this corner.

**24:36** · Okay.

**24:38** · Um Great.

**24:40** · So, let's give that a little bit of time uh to run through and then we can check back in on it. But I've chatted with you know, sales people where they are creating demos. This is even pre-Claude code that they were creating demos or presentations 5 minutes before a meeting.

**25:02** · The cool thing about Claude code is that you don't have to upload a bunch of documents into Claude. You could point it at an entire folder that you have for that one client. Like you if you if you're working with Home Depot or whatever, you have an entire folder with like Home Depot sales, Home Depot corporate values, Home Depot strategies, the the sales conversations that you had with them. Uh you could then just basically say, "Review all files in the Home Depot folder and make me a new presentation that blah blah blah."

**25:37** · Uh okay, how are we doing?

**25:41** · Still doing all the Python stuff. Hopefully open bike sales dashboard. I re it overrode it. Okay, whatever. I could have said make a new one, make a new one. But this is our McKinsey style bike \[laughter\] sales. Uh it's so good.

**26:00** · It's so good.

**26:02** · Um the HTML file blah blah blah. I wanted two versions.

**26:09** · Give me both.

**26:11** · Okay.

**26:12** · What I'm hoping that this will actually do is it'll go back to the code that it wrote for the first one and that it'll be um done very quickly.

**26:33** · Okay.

**26:34** · Um We're just going to keep hitting enter enter enter enter enter. All right, this presentation colorful one should be the non-McKinsey one. Uh and so you get the colorful one.

**26:46** · Awesome.

**26:47** · Uh and so now we have both of those saved into the folder. Um I just want to show one other um one other sort of task that you can do, which is like my computer is running super slow. Give me three files I could potentially remove. Tell me to remove them. Not that I think it would.

**27:16** · Okay.

**27:22** · Um and so He wants to hide my my father's photos from Africa, which I wouldn't ever. Uh okay, so it is going to kind of find those. Uh it's going to flag certain things. Sparkle project I think was a coding thing that I did forever ago. Uh CapCut makes sense because those are huge videos. And so I could say, "Okay, great. Delete those." Uh I could say uh review my activity monitor.

### System utilities: Activity Monitor cleanup

**27:53** · What is stealing the most RAM?

**28:21** · Cool. So, Microsoft Teams, which I always complain about. Uh Firefox, great. The biggest culprit is Firefox. It's so funny like the way that it yells back. I asked it some other question forever ago and it was like, "This is your problem." Uh cool. And so it gives you advice, which I also love. Um Maybe one more, which I moved a file to my desktop, which is just called no code one.

**28:48** · Do you see a JPEG uh on my desktop?

**28:54** · Like no code something. So again, you can kind of talk to it in fake-o language. Perfect. It found it. Just for fun, we're going to terminate that. Start a new one. Uh find We have to invoke Claude.

**29:16** · Yeah.

**29:18** · Uh find the no code JPEG on my desktop and down res it. Down res, down scale, compress, whatever. Uh if you Oh, that's funny. Just the way that it's searching is very funny.

**29:43** · It'll find it.

**29:46** · There.

**29:48** · Uh that's like that's the most magical part is when you like talk about file names in natural language. Uh the image is currently da da da.

**30:03** · 40%.

**30:08** · And again, you can always switch to option two.

**30:19** · Cool.

**30:21** · You can see this one is resized and it's tiny.

**30:24** · Yay!

**30:26** · So fun.

**30:27** · Um you could also like like I've seen people take um let's see photo of receipt. Uh that looks like a photo.

**30:41** · Real photo.

**30:44** · Save image as great turn my Walmart receipt on my desk on my desktop into an expense report.

**31:02** · And so you can imagine like all these things I'm pointing at at one file. You can imagine pointing it at an entire folder that is filled with receipt images or an entire folder filled with PowerPoints. You could point it to an entire folder and say review all of my you know sales presentations. What are they missing? Review all of my um client contracts in this folder. What risks are we not thinking about?

**31:28** · Okay, we are going to approve. And so what I'm actually testing here and I could have specified like what um um I could have specified what OCR technology like what is actually going to read the receipt itself but it created a markdown file. So I I didn't specify uh how to read it or what format to put it in. I just said make it an expense report. Uh and it looks really nice.

**32:04** · Great.

**32:05** · It took I just think like this is the more impressive bit. It took what is a uh technically an unstructured piece of data in the sense that it is an image um and it was able to apply OCR aka read the text that is on the receipt. It was able to pull out the vendor. It was able to pull out the address. Um and so it was able to turn unstructured unstructured with structured stuff written on it into structured. Uh and so I've seen people like hey go through this entire folder and turn it into a a an expense sheet.

**32:51** · Um okay.

**32:53** · So just to review a couple last tips. When we go to the terminal uh last tips. So if you go to um shift tab you can switch between different modes.

### Power tips (modes, thinking, escape, permissions)

**33:12** · So right now I'm holding down shift and hitting tab. You can switch between mode accept edits is um the the automatic like yeah I'm going to approve it no matter what. Plan mode is like don't do anything. Just think about it and tell me what you're going to do.

**33:32** · Um and then you can cycle to the to the help thing. If you do um Where's tab?

**33:39** · If you do tap if you see kind of in the bottom right I'm tabbing between thinking off and thinking on. Any sort of thing that's like write me this story and save it or um you know edit this file name to include the word final at the end you don't need thinking on. If you're doing really large code bases, if you're reviewing 15 documents and you wanted it to think really thoughtfully about contract reviews I would hit tab and toggle thinking on.

**34:09** · Uh I already showed you that hitting the escape button when something spazzes out um it'll stop it. And if it still is spazzing out which we did experience you're just going to hit the exit button, terminate that terminal and start over.

**34:24** · Um and then again my like favorite favorite thing that Claude.ai doesn't have is the ability to queue up all of these different prompts and you can literally queue up 10 different tasks whatever. It's so so cool. Um things to flag uh number one was the permission setting and data privacy. So you have to determine that for yourself.

**34:48** · I cannot tell you what to do there. Um I can tell you that some people are like I'm auto approving everything. I don't need to review. I'm not like that. I need to like see it do it once. I need to know like what it's fail rate is before I automatically bless it to do something.

**35:04** · Um it's moving through kind of progressive trust. You'll see even through the login process that it tells you like you sure if I have this access?

**35:13** · You sure if I get this access? Uh and so I love that. You can um point it to only have access to certain directories. So if you're like I don't want it to see my entire desktop I only want it to see this one little folder that I'm willing to play around with. And so you can do that. Uh basically you're adding a directory inside of of Claude code.

**35:37** · You can remove access. If you've gave it access to two directories and you want to take one away um mm-mm Think if we also there are a couple of these like backslash uh things. So again, all I did was just type in slash. And so you can see all of these um different commands that you can use. Uh clear is really nice especially if you are about to switch tasks and you don't want to delete the terminal or terminate the terminal and restart it.

**36:08** · Um where it just clears your whole conversation and doesn't have as much uh memory dragging it down.

**36:15** · Um you can also go and do agents which we didn't get into in this but what I love is that if you do backslash agents and create a new agent um you can basically create um like ready ready It's like a GPT. It's a ready-to-use prompt. Um but you can also give it tools. So if I say yes to create a new agent uh if I say that I want to do it at a project level let's say uh always generate with Claude unless you're like Andrej Karpathy.

### Creating Agents

**36:56** · Um cool. Create a new agent and then I'm going to say new agent that turns a Word doc into a PowerPoint.

**37:06** · Okay, so I gave it I gave it a very uh vague description and it is going to in the same way that we've seen it in Claude console um or GPT creation um where it's configuring itself that you can give it a very vague prompt and that it will generate its own prompt for that. Um and when needed also generate its own code. So one of them could have been uh like that image extraction sort of thing. Right?

**37:36** · That was a little mini script that it wrote to be able to read the receipt and do something with it. That could be an agent. Um mm-mm Auto selected. I mean this doesn't actually matter but okay.

**37:59** · Auto selected. Continue.

**38:03** · I did it. Oh there. Continue. Sorry. Um select model. Um Sonnet is fine. Um if you were working on something that was tiny I would use Haiku but I would actually default to Sonnet. Uh you can set it as a certain color. We're going to make it blue. And you can see that it wrote the description. It wrote a system prompt.

**38:27** · It gave access to all tools which again I could have um uh changed. And then press S or enter to save. We're just going to say yep. So now I have saved it. So you can see that in agents uh I just created this doc to PowerPoint converter. Boom. Great. Um so now I can hit escape. It'll show me that I've created that document. And then I can say like doc to PowerPoint converter.

**39:05** · And any document on my Cool. So it's looking at my desktop. Hopefully it'll find zero.

**39:32** · Ooh. Sure.

**39:35** · Let's turn a receipt into a PowerPoint.

**39:38** · Um yeah, so you can create a bunch of go-to agents. Um for the most part, it might be like a common prompt that you're running. So, if you're always doing something on top of like a um uh folder, like review this and come up with suggestions, then that might be um an interesting one or uh review this, you know, invoice and generate uh or review this SOW and generate an invoice.

**40:07** · Those sorts of of commonly used ones, you might want to start there and then be able to build up. Um okay, this was a 40-minute-ish tutorial on Claude Code.

**40:22** · Um just again to to show, if I hit Well, maybe I'll let this If I hit escape, um you'll see this interrupted, "What should Claude do instead?" It's like it thinks that it like got hit and it needs to fix its problems. Um so, if you want to terminate this, you're just going to hit this X button. Do you want to terminate it? Yes. And yeah, that is Claude Code.

**40:48** · Uh we went through so much in so little time. Uh we went through how to uh initialize it, how to like actually install it, how to kind of set it up and making sure that you are reading the permission requests, um the fact that you can point it at specific directories or your whole computer, that's at that stage. Uh we talked about how to open up the terminal. We talked about how to talk to Claude.

**41:16** · Um we talked about how to create new files, edit files, create versions, change file names, uh create different file types, create synthetic data like the bike sales thing, uh create dashboards, create PowerPoints. Um I gave some examples about reviewing entire folders for advice or for edits. We even showed how to create an agent. You could have agents that again take action and not just like turn this text into this text.

**41:47** · Um but that is Claude Code. I think that there are so many use cases out there for non-engineers. It's not the sexiest uh user interface that I've ever seen. Terminals can be very overwhelming and can feel very inaccessible. But the last hack that uh I I always end these tutorials on is, when in doubt, ask Claude.

**42:13** · Literally, you can just highlight the entire terminal conversation and just hit Apple A, grab that whole thing, Apple C, copy the whole thing, go into the Claude that you know and love, claude.ai, or even go into ChatGPT, whatever, paste it and go, "What the heck's going on?" \[laughter\] Or, "It's telling me this error, how do I fix it?" Or, "All I want it to do is do this agent, like how do I tell it to do that?"

**42:37** · Uh and you can also talk to it within the terminal, but again, if ever you're just like get me out of here, you can go to the safe place of the pretty webpage and ask for that help and go back into it. My hope is that every single one of you is going to be able to complete all of those tasks that we just showed.

**42:52** · When in doubt, hit escape, terminate the terminal, start it up again, and ask Claude or ChatGPT or a friend uh for help. My name is Ali K. Miller. I'm the number one most followed voice on AI business. Think I've probably been giving too many workshops the last month and maybe I should drink some more water, have some more cough drops, but talk to you guys later. Bye.
