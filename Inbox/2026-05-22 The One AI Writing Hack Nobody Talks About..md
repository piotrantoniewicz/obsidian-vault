---
type: "Web"
authors: "[[Nate B Jones]]"
url: "https://www.youtube.com/watch?v=ltbzgzZZmgI"
published: 2026-05-22
created: 2026-06-17
tags:
---


![](https://www.youtube.com/watch?v=ltbzgzZZmgI)

## Transcript

### Historia halucynacji Sullivana i Cromwella

**0:00** · A few weeks ago, Sullivan and Cromwell, one of the most prestigious law firms on the planet, had to write an apology letter about AI to a federal bankruptcy judge. Their emergency motion in a chapter 15 case had been filed with dozens of fabricated or misqued citations. AI hallucinations. The other side's lawyers caught them. Sullivan and Cromwell's own review did not. The partner who signed the apology letter is the co-head of the firm's restructuring practice. This is the failure mode I want you to think about with me for the next few minutes.

**0:29** · I'm not talking about 2024 hallucinations where a solo practitioner uses chat GPT and tries to tell it not to hallucinate. I'm talking about organizational and structural hallucinations at the top of aic workflows. In this case, the motion looked legitimate. The structure of the motion was correct. The citations were professionally formatted. Dozens of them were pointing at the wrong things and nobody on the team caught it before the filing. The model is not the problem here.

**0:57** · The working environment around the model is the problem and it's the source for most of our 2026 hallucinations. I know what some of you are thinking, Nate, the answer is a better prompt. We talked about this. Just tell the model not to hallucinate. And by the way, the Mark Andrees screenshot has been all over the timeline for a few days now. It doesn't work. You cannot tell a language model not to hallucinate any more than you can tell autocomplete not to autocomplete.

**1:23** · There is no separate truth check pass inside the model that the instruction can hook into and have some purchase and meaning. Sullivan and Cromwell had access to the best AI tooling that money can buy. The wrong detail still made it into court. The fix is not a sharper prompt. It just isn't.

### Dlaczego lepszy monit nie rozwiąże tego problemu

**1:43** · In the last month with 4.7 Opus and 5.5 from OpenAI, agents have picked up a capability that changes the way we think about this. And I don't think law firms or most other people have realized it yet. There is a fix. It is not a prompt fix. And that's what I want to talk about today. So what is it about 4.7 and 5.5 that's special? They do longunning agentic tasks, as I've said a lot, but they do it on your file system. And that's such an unsexy thing to talk about. Oh, files. That's all the way back to 1982, right?

**2:14** · Like that's a long time ago we handled files. Longer ago than that. Why do we care about files now? Why do we care that agents that are long running are now very good at taking and manipulating files? And how does all of that connect to the hallucination story? I will tell you these new agents do not just read what you paste. They can walk a folder tree. They can open files. They can compare dates across documents. They can inspect metadata.

**2:39** · The workflow around hallucinations has flipped, but most people haven't caught that yet because the first useful prompt in a serious project is now like it's not write the document, right? It's much more boring than that. It is build me the folder in the file room. Build me the room to do the work in. And I want to talk to you about three key takeaways in this video.

### Co zmieniło się w Opus 4.7 i GPT-5.5

**3:02** · And if you follow them, you are not going to end up in the same hallucination place because you will have set up a process that is structurally antagonistic to hallucinations. I'm not saying they never happen. I am saying that you are building a structure that makes them much less likely to occur at scale and it keeps you and the work you do much more accurate and much less likely to lead to the kind of corporate liability that this prestigious law firm generated for itself because it did not think through its agentic pipeline correctly.

**3:35** · It all comes back to file. So here we go. Three things. One, why your first AI prompt is never do the thing. And I talked about that just above. We're going to get into why that is. Two, what to ask the agent for when you want to go deeper and how you do that intelligently. And three, why this approach actually works with 5.5 in particular. 5.5 is really good at this and also with 4.7 as well. Look, the thing that sold me on this workflow was a real moment that I had multiple real moments over the last couple of weeks with codeex.

**4:06** · I have been in situations where the AI agent has now been able to do incredibly powerful simultaneous drafting of up to eight different documents. I haven't gone past eight yet. I think I could. And the only way I could get eight documents drafting at once in codeex is because I prepared the data room first and I knew my outputs and I could then execute really cleanly and consistently. And it saved me so much time.

### Trzy wnioski dla poważnej pracy opartej na wiedzy

**4:37** · It was an incredible speed up. It felt like the hair was blowing back on my face and I was living in the future. And I think that that's one of the things that we need to pay attention to is that we get these aha moments when we think about the boring primitives when we think about the files. And that's why we're going to talk about look because of chat GPT. Back in 2022, most people think the AI workflow starts with doing a job. Does the model write for me? Does the model code for me? Does the model make the Excel file? that's where the value is, right? It starts when the agent walks in and does something.

**5:10** · But I don't think that's true. I think a serious project almost never has its source material organized.

**5:16** · And we have had to be the human organizers for most of the prompting era in the last couple of years. We've had to find the strategy docs and the meeting transcripts and the spreadsheets and the half-finish notes and the follow-up emails and the old deck and the PDF you forgot about and the Slack thread where the actual decision was made. Can you tell I've actually had to do this? Some of it is current. Some of it is stale. Some of it contradicts itself. A few files may be helpful.

**5:38** · You're not sure which one is the source of truth. You're often wrong. When you ask an AI to write from that general mess, you're asking it to do two jobs at once. Job one, figure out what this is.

**5:49** · And job two, produce this beautiful artifact for me. That is a recipe for a really mediocre result. And it's one of the situations in which it's likely that you will have a hallucination problem in the way that this law firm did. The model didn't have a clean working environment. So, the dirt got into the dock. It didn't know which sources mattered. It didn't know what was stale.

### Dlaczego pierwszym monitem nigdy nie jest „zrób to”

**6:11** · It didn't know what was missing. It didn't know which file was authoritative. You cannot patch that with a better opening sentence. And you really can't patch it by reading the doc and hand editing anymore because we're working at a different kind of scale.

**6:23** · You have to patch it and prevent it from the beginning by cleaning up your data room first. So your first instruction should not be do the thing like write the memo, make the Excel etc. Instead, your first instruction needs to be find the relevant materials on the internet on my local computer in my files in the tools that I have connected to you. And by the way, Claude and Codeex both have a ton of connectors now. And so you can actually tell them to look in their connectors and they will.

**6:49** · And so the first instruction is find the relevant materials, preserve the originals, build me a data inventory, put it in a folder, tell me which files seem authoritative, which are duplicates, which are old, which are missing. Summarize every source before you synthesize anything.

**7:04** · And do not write the deliverable yet.

**7:06** · We're just learning. That is so powerful. And it's possible because these tools can do complex longunning file manipulation tasks successfully and with very high accuracy. So let's use them to do that. Let me give the workflow a name so we can talk about it very very clearly. I'm calling it a project room or a data room. A project room is a bounded workspace for one serious job. It's a project, a deliverable, a source set. Now, this is much smaller than a whole second brain.

### Problem z chaotycznym materiałem źródłowym

**7:36** · It's much more specific than a knowledge management system. It is a workspace set up so an agent can do useful work inside it. And in most cases, it is a local workspace. This is different than a lot of the published cloud solutions that claude and chatgpt and codeex have had where they say here start up a project and sort of a shared context window that people can all chat into and all work with. I have found those have been much less useful than the flexibility of a local file system.

**8:04** · And there is a whole 2026 conversation to be had around the idea that we are going back to files and going back to simple primitives. And those tend to work really really well because LLMs are being taught to use computers at their most primitive and root level in order to successfully do anything on computers. And when we go back to files, we are going back to what they know really, really well. Why not, right? Why not lean into it? So, let me give you an example. For a consulting project, this could look like client decks, interview transcripts, data exports, prior proposals, meeting notes.

**8:36** · For a house purchase, it's inspection reports, disclosures, contractor estimates, mortgage documents, email threads. For a Substack, article you're writing, it could be uh sources you're researching, transcripts, draft notes, screenshots, prior related posts. For a board doc, it's a financial model, an operating plan, an old board deck, the current KPI exports, and the notes from the last three review meetings. The point here is that you don't have to build a perfect archive to gain a tremendous amount of advantage in the task you're setting the model.

### Wprowadzenie do przepływu pracy w pokoju projektowym

**9:03** · The point is just to give the agent a usable work surface, just enough room for it to operate. Where you build your room, of course, will depend on your preference on your source set. Look, you can do this in cloud projects. It's solid when you need a bounded workspace with uploaded docs. Chat GPT projects handle smaller sort sets and spreadsheets.

**9:24** · Cursor or clawed code is the right tool in the room. Includes a code or folder tree. Codeex works for that too.

**9:30** · Notebook LM works when it's very sort of research heavy and sourcebounded. And like I said, my personal preference, just go to local files, have it create a folder, and you can stick literally anything in there. And that's what I love about it because there's no like file type limitations that you get with some of the tools I mentioned. If it's a file, it goes in there. And if Codex can read it or Claude can read it, you're in good shape. So, if you want to dive deeper on different options to organize your files from the all those different tools and how you want to think about making that choice, I put that on Substack.

**10:00** · You can dig into strategies for local file organization because imagine doing 20 projects. You're going to need to have some thinking around that. Uh you're going to want to dig into strategies if you want to use other tools too like uh projects on claude or on notebook LM looking at the sort of the folder structure, how you think about project breakdown. I've got all of that in detail there. We're going to stick in this video with how we think about this as an archetype, how we think about this as a larger pattern that works across many tools. So let's keep moving. So, you have your folder. You have stuff in it.

### Gdzie zbudować pokój w różnych narzędziach

**10:30** · The most important artifact in this whole folder I haven't talked about yet. It's a table. It's just a table. Hear me out. It's called the source inventory. And once the room exists, it's the first thing you ask the agent to produce. For every file in the room, the agent records the path, the type, the date, the apparent authority, whether the file is current or superseded, what claims it supports, what its limitations are, and how it should be used in the final work. Yeah, that does sound boring. It's also the artifact that determines whether everything downstream is any good.

**11:00** · And by the way, it's an artifact that makes it really, really helpful when another LLM checks your current LLM's work. It makes it easy to pass. The inventory tells you what the agent thinks the project consists of, which is critical, and that gives you a chance to correct the working set of docs and and current set of data before the final draft is going to like inherit a bunch of mistakes and lead to hallucinations, frankly. And so yes, I do recommend checking what is in your inventory and making sure you're aligned with it and nothing is missing.

**11:31** · And when in doubt, just say, "Hey, you know, codeex, I think this transcript may not be in here. Can you check and if need be, create a file for it?" And we'll do that. And the beautiful thing is these agents are strong enough to sort this out. Right? They can tell that an approved deck represents the story even when the underlying data lives elsewhere.

**11:47** · That the old PDF might be useful background but not a source for current claims. and the the agents really can sort that out at the at the opus 4.7 at the Chad GPT 5.5 level and and the inventory artifact that you you create that table I'm talking about what you're really doing is you're making the agents judgment visible and legible so

### Tabela inwentaryzacji źródeł

**12:08** · you can see it really really clearly because if you review the inventory and you can't tell why one file outranks another you can just like focus on getting the inventory right focus on making sure all the data is there before you have to go farther it's a really clean gate Now, I have been testing different knowledge systems for AI and the the organization framework that I landed on for large projects is something I'm writing up in a lot of detail on Substack.

**12:31** · So, if you're serious about AI work, if you're trying to figure out how you organize these files at a 10, 20, 30 project scale so you're clean and you understand what you're working with, that's what you want to get to. Like, I have it all written up over there. Let's get into a couple of more artifacts to illustrate the principles because remember that's what we're doing. So, we talked about the table. Let's talk about two more artifacts. The first is the conflict log. When the agent reads a serious source set, it will find disagreements.

**12:59** · The old PDF says one thing, the current plan says another. The transcript uses a different name for a person who's a key stakeholder versus a doc. The spreadsheet has a number with no visible assumptions behind it. Two documents that look adjacent are actually three months apart. A weak workflow lets the agent synthesize and smooth those conflicts over. The output will read confidently, but you don't know what you can trust. you get into the same hallucination problem that the law firm did at the beginning of this video.

**13:23** · A strong workflow surfaces that disagreement without necessarily resolving it or at least without resolving it, without you being able to tell. The conflict log allows your agent to surface conflicts that I've just described and recommended responses and allows you to have opinions and edit, adjust, tell the agent it's wrong, etc.

**13:45** · before you get into building the doc.

**13:48** · The second artifact I want to talk about on top of the conflict log is the missing context list. One of the best signs that an agent is helping properly is that it tells you what it doesn't have to do the job well. The missing decision, the number with no source, the current version of a file that that's nowhere to be found. The completely absent data file that is referred to in only one document. All that matters because the missing material is often more important than the material you have.

### Artefakt dziennika konfliktów

**14:15** · Your file can say as discussed and the actual discussion can be somewhere else. The deck can include a chart in the data source ends up being way far away and maybe not in your data room at all. Ask for the final memo or the final output or whatever you're writing too quickly and all of those gaps become effectively hallucination traps. The model invents its way around them to get your job done and the pros looks fine and you may ship something with a very soft spot underneath and someone will find it.

**14:42** · So ask for the missing context list first and those gaps become transparent and legible and you can review them. You can see them. You can decide whether they matter, whether you can find the source, whether you have to phrase the claim more carefully. So the full sevenfolder structure that I use inside projects, every folder name, the purposes, and all of that, I link that in the substack. It's all laid out. You can see it really cleanly there. Uh we're going to go on from here to talk about duplicates. And and I want to be really honest about this because a lot of people miss this.

**15:12** · People think duplicate detection in files is housekeeping. But in AI work, duplicates can be a reasoning problem. If the agent sees three versions of a plan and doesn't know which one is current, it might blend them. The same transcript exported twice can get overweighted in the synthesis if you're not careful. An old deck and a new deck with similar titles can become a source for wrong claims. a revised budget sitting next to an earlier copy. It produces averaged assumptions, right?

### Lista brakujących kontekstów

**15:38** · You do not want your agent deleting duplicates, but you do want it to produce a duplicates report and probably a separate folder with suspected duplicates and hand that back to you. Let the agent find the mess. Let the agent name the duplicates, name the likely duplicates, name the level of confidence, name the version families.

**15:58** · Do not let it silently resolve the mess, especially when you care about the work.

**16:03** · the agent finds you decide that is a really healthy way to have good clean agentic pipeline work for very complicated highv value critical knowledge work. So why does all of this matter? One more thing before I get to like how we write the prompt to get actually going into stuff. There's a reason this matters now. The agents have just gotten so much better at the details of the file manipulation I'm talking about. They really do walk folder trees cleanly. They open files well. They inspect metadata.

**16:32** · They're good at actually doing the nitty-gritty work of file comparison at high fidelity across hundreds of documents for a long period of time. And so file organization used to be something we had to do to housekeep for ourselves. Increasingly, I think of it as a canvas that we have to work with the agent to create so that the final work reflects the underlying data. In that sense, the data underneath is the substrate for the canvas.

### Dlaczego duplikaty stanowią problem z rozumowaniem

**17:00** · It's that white gesso that's on the surface of the canvas and then you paint across it the work you want to create with your agent. But if you don't get the canvas right, you're never going to get the final work to look right. And that's what we're doing with a data room.

**17:14** · You're framing the work. Literally, you're framing the work. And because we are now doing harder work because the agents are more capable, our traditional ways of compensating don't work. You used to be able to compensate for a messy folder with a sharp prompt. It's too big now. You can't now. The mess is becoming structural and entangled and it's becoming something that you can't clean up with a single prompt. The mess is sitting inside the agent's context window and it's something that the agent will disentangle in the best way it knows how.

**17:42** · And the risk is actually higher because the agent will find you know no matter what come hell or high water and a way to disentangle it because that's its job and it's trained to go after that task aggressively. You may just not have ever seen that way of disentangling it. you may not be aligned. And that's exactly where you get the kinds of hallucinations that we saw in the law firm at the top of this video. That's that's the structural reason those sorts of things start to surface in final materials. Now, the good news is we're finally at the prompt part. I know you guys are waiting for it.

**18:13** · Once the room is in shape, once you have inventory, conflict log, missing context list, duplicates report, the writing prompt actually gets really short. It's not long and the output gets much better. Before the room, the prompt was like, "Write me a strategy memo.

**18:29** · Here are a bunch of files." And then if you're doing prompt engineering, it's a very detailed like, "Here's what I want you to write." After the room, after you have your data together, the prompt is very simple. Use the reviewed source inventory in the project room in the working brief. Treat the current operating plan as authoritative for numbers, the transcript as source material for decision context, and the older deck as background only. Draft the memo, site claims, flag anything not supported. The key here is that all I'm doing in that prompt is I am saying this is what matters to me.

### Pliki jako kanwa dla pracy agenta

**18:59** · This is what I care about from a conflict perspective.

**19:04** · This is what I think the authoritative true line is for this piece of work that we're working on together. And then you go do the rest. And this makes the AI's work inspectable. It's not that I'm saying if you do this the AI's work will be perfect. But it is the difference between using AI as a colleague and using AI as a gopher. And we are really underusing these agents if we treat them like gophers and say just go deal with stuff and we don't give them any any ability to think about their structure and their context with us. They are more senior than that.

**19:36** · Now our AI agents deserve to be able to shape their context windows and their data rooms together with us if we want to get the most out of them. and they are capable of doing so. Now, a word on calibration before I close. I am talking specifically about agents for serious knowledge work. Right? If you are working with codecs for a 30, 40, 50 hour, two-hour run, this makes sense. It makes sense for coding. It makes sense for heavy knowledge work like I've been discussing with projects and reports. Do not run this workflow on every casual interaction with AI. It's way overkill.

### Krótki monit pisemny, który w końcu działa

**20:10** · Also obviously I am not talking about using this approach to produce agentic pipelines that take care of back office operations. You still need a data strategy. You need to think about how you input data. That's important and I cover it in other videos, but it's not this problem. And yes, I have more prompts on the Substack. I know that not everyone has the exact prompt situation that I gave you. If you want more sample prompts that kind of cover a wider variety of use cases for this kind of knowledge work, it's on the Substack.

**20:37** · you can grab them and apply it to your messiest folder this week. It'll help.

**20:40** · So, in closing, here's the mental model shift that I want you to walk away with.

**20:45** · I'm really passionate about this. I think this is one of the most slept on implications of AI in the last 40 days and and we're not talking about it enough because it's files and it's boring. The old AI question was whether the model could do the thing, right?

**20:56** · Could it write the memo? Could it make the spreadsheet? Could it write the code? Those questions still matter.

**21:01** · They're just not the most powerful questions anymore because the models have gotten so good. The new question is whether the agent can help prepare the conditions under which good work happens. Can it shape the canvas? Can it find the right sources? Can it tell which ones are current? Can it identify what's missing before it invents around the missing thing? That's where agents start to feel really useful as colleagues for real work. Because an agent can walk into a messy room, it can turn on the lights. It can label what's in all of the folders. And it can get the entire desk area organized for serious work. That is an AI worth using.

**21:35** · Please use your AI that way. And I'm talking specifically about Chad GPT 5.5 and Opus 4.7. I would not do this with earlier models. I hope this has been helpful. There will be more practical tips coming on this channel shortly, so subscribe for more. Cheers.