---
type: "Web"
authors: "[[Allie K Miller]]"
url: "https://www.youtube.com/watch?v=gVMAbiQYMh8"
published: 2026-06-24
created: 2026-06-26
tags:
  - strategia-AI
  - szkolenia-AI
  - context-engineering
---


![](https://www.youtube.com/watch?v=gVMAbiQYMh8)

In this video, I sit down with Dr. Andrea Jones-Rooy (@jonesrooy), Founder of Data Thinking Revolution and former NYU professor with a PhD in political science and a background in data science, to talk through how she actually uses AI day to day and where the hype falls apart. She went from prompt-engineering in ChatGPT to running Claude Code with MCP and an email research pipeline, and she explains what finally got her over the hump.  
  
This one is for anyone who advises companies on AI or is trying to figure out what separates real usage from theater. We get into layoffs, token maxing, measuring value, and the human skills that hold up no matter how good the tools get.  
  
What you'll see in this video:  
✅ Why the tech world overhypes AI to the point of intimidation, and how that keeps smart people out  
✅ How Andrea built an email research pipeline with Claude Code, MCP, and Gmail  
✅ Why coding with AI felt like cheating to her, and the moment that changed  
✅ How she handled two-thirds of a 200-person class using ChatGPT with no policy  
✅ "Urgency is poison": the cross-functional brainstorming work she did with a major fintech  
✅ The AI watchdog agent that catches two teams building the same thing  
✅ Why token maxing tells you who to interview, not who's doing good work  
✅ The layoffs data problem: why "we cut roles because of AI" rarely holds up  
✅ What China gets right on EVs, air pollution, and renewable energy  
✅ Why curiosity and critical thinking are the skills that survive every tool change  
  
\~~~~~~~~~~~~~~  
  
🔗 New to Claude Code? Start here — Claude Code for Absolute Beginners:  
https://www.youtube.com/watch?v=v1ynWeHhzXs  
  
🔗 Claude Code Commands & Cron Jobs: Full Setup Tutorial:  
https://www.youtube.com/watch?v=l6V0u3ZIgDI&t=1282s  
  
🔗 How I Use Claude Code: From Terminal Hacks to Agent Teams  
https://www.youtube.com/watch?v=0pd7PVTOaRw  
  
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
Business inquiries: support@alliekmiller.com  
  
\~~~~~~~~~~~~~~  
  
⏰ Timestamps:  
0:00 Intro: Meet Dr. Andrea Jones-Rooy  
2:55 Getting over the hump: hype and intimidation  
9:33 Her AI stack: Claude Code, MCP, research email pipeline  
14:08 Coding with AI and the cheating question  
19:34 Teaching through ChatGPT: students and policy  
26:28 Urgency is poison: enterprise brainstorming advice  
41:21 The AI watchdog agent  
45:42 What data shows about layoffs  
59:55 A players, B players, and token maxing  
1:10:21 China, EVs, and the environment  
1:20:12 Sensors, measuring problems, and human skills

## Transcript

### Wprowadzenie: Poznaj dr Andreę Jones-Rooy

**0:00** · Very excited to have the one and only Andrea Jones Roy, Dr. Andrea Jones Roy, excuse me, here and you are a former NYU professor. You've talked about data science, you've talked about reinforcement learning, natural language processing, all the things that are happening literally right now. And reinforcement learning is one of the biggest waves that's literally right now happening. Um you have a PhD in political science with a focus on complex systems. Your literal study was on looking at chaos and just going, "How can we make sense of this?"

**0:28** · And I assume that you have no stress any day of your life.

**0:34** · Right.

**0:34** · Cuz that cuz you have a PhD in de-stressing yourself. Um and then you've also just been using AI a lot in really interesting ways. You, like me, we both advise some of the biggest companies in the world. I know some of the companies that you work with, but it's like one of the largest fintech companies, actually two of the largest fintech companies in the world, one of the largest CPG companies in the world, and you work a lot with the government as well. So, to the extent that you are able to share, I'm really excited for you to take on a couple different topics.

**1:02** · My hope for this conversation is that we can kind of start talking about how you're using AI, how both of us are staying productive, increasing the quality of our work. Then I want to get into some hot topics. Maybe we talk about layoffs, maybe we're talking about the environment, and just again making sense of chaos.

**1:20** · All very upbeat, non-controversial topics.

**1:23** · This is going to be really light-hearted conversation.

**1:26** · Just laughs, \[laughter\] mostly.

**1:28** · And then toward the end, uh I want to talk about like forward-looking future predictions, um and maybe you can bring in some of your data science into to how you're thinking about that.

**1:37** · That sounds great.

**1:38** · sound?

**1:38** · That sounds wonderful. What What a plan.

**1:40** · \[clears throat\] \[laughter\] If I told you that AI helped me come up with that plan, would you be surprised or not?

**1:45** · I would be shocked. I just assume that your default is to not use AI unless you absolutely have to.

**1:51** · No, I have I only have like 45 questions to get through, so we'll start with the top and then explain someone, I don't know if you want to share this. We'll start with secrets. Uh \[laughter\] I had someone recently ask me if you used AI to send text messages.

**2:04** · If I used AI?

**2:05** · Yeah.

**2:05** · Or if If you use They were like, "Does Ally text If I'm If I'm texting with Ally, is it Ally or an AI agent?"

**2:10** · It's definitely Ally, but I am dictating Yeah.

**2:13** · and therefore transcribing Sure.

**2:15** · like 90% of my texts.

**2:16** · Right.

**2:17** · And so the number of times that I have texted, "Sorry, any typos, please blame it on AI."

**2:22** · Right.

**2:22** · is very high now. Because I am I've now had to tell my team, "When I send you a text like for the purpose of efficiency in getting things out, I need to be able to do things hands-free, and so I'm just going to send that first draft."

**2:34** · Right.

**2:35** · You're going to work it out.

**2:36** · Yeah.

**2:36** · Yeah.

**2:37** · And my team is smart enough they can figure out whether I mean this or that.

**2:41** · Right. Right.

**2:42** · Okay. So, the person you can tell them that they are texting with me, which is also why I'm really late on texting everyone.

**2:48** · That's right. I was \[laughter\] like, "We would be hearing from her right away if her agentic AI workflow was dealing with this." Yeah.

### Przełamanie barier: szum medialny i zastraszanie

**2:55** · Okay. So, how I mean, are you dictating to AI? How are you using AI? Like you've you've now jumped on the agentic AI bandwagon.

**3:04** · Yes.

**3:04** · I'm newer to the agentic AI bandwagon. So, I was the person who forever was just using ChatGPT and feeling like I was ahead of the curve until I looked up from my laptop one day and was like, "I am a thousand years old if I'm on here prompt engineering like a 200-year-old dinosaur." And so, I very quickly was like, "We got to understand what's going on here."

**3:25** · You took a You offered a workshop that I that I took, and really it was one of those where it's both agentic AI is both amazing and incredible, and maybe this is a credit to your teaching, but also is much more approachable than I thought.

**3:40** · And it reminded me a lot of when I teach data science to folks who are like, "I'm not a math person. I'm not a science person. I couldn't possibly." And it's like if you just open a spreadsheet and kind of start mucking around, it's more intuitive than you think. Yes, for Agent QA, you're doing more complicated things than just working with a spreadsheet, but I was pleasantly surprised at how readily the on-ramp was not as steep as I expected. Let me put it that way.

**4:03** · Here's my question. You are someone that knows that you've had to convince thousands of students to like actually move into math and science. You know that the answer was to open up your laptop. Why did it take you so long to open up your laptop for agents if you knew that that was the answer?

**4:17** · You know, I asked myself the same thing once I opened up my laptop and looked at it. I was like, "Oh, this is this again." And I think that it's it's two things. I think one, humans in general, I'm not a psychologist, but I have a working hypothesis that humans in general, we we have these ideas of what we're capable of and we think, "Oh, I can't go outside of that." If I tell myself, "I'm a bad singer. I'm a bad cook. I'm a bad math person." We just tend not to push that boundary. And so, I think a lot of it is self-imposed. And so, I grew up studying data science.

**4:45** · And so, I thought, "Well, I'm a data scientist." And yes, I've taught reinforcement learning. Yes, I use NLP and and all of these tools in my work, but I'm not I don't have a degree in AI, so I must not be for me. And so, I sort of was just anytime it came up, I was like, "Uh, I can't do it." It's the you know, you might as well have said brain surgery to me, right? And I think the other piece of it is that I'm going to speak in broad terms, but I think the tech world in general is guilty of over-hyping things to the point of intimidation.

**5:18** · say.

**5:18** · Dare I suggest? And I think there's a lot I mean, we saw this in the world of data science as well, where it was like, "We're using machine learning and deep learning and neural nets." And it just sounds much scarier than it is. And a lot of people are very unpleasantly surprised, at least my students, when I would say, "Okay, you've all heard of machine learning.

**5:37** · What do you think it is?" And they say all this complicated stuff. And you say, "Okay, we're going to now do it." And one of my co-instructors used to call it fancy counting. And you're like, "Yeah, a lot of this is really fancy counting. And and so so I think that the way that we talk about it is naturally exclusionary.

**5:55** · \[clears throat\] And I would I was I fell into that trap even though I consider myself roughly in that world and I literally say these things to other people, that's how quick the world it and because it's changing so quickly it's like you hear a term token maxing. I've never heard that term. I must not know anything. I can't be part of this. Oh, you can just learn it and you can keep going. Like we we artificially inflate the steepness of the curve.

**6:18** · Other than using more simplified language, which I hear you and I like it's not dummying things down by the way. It is just It is just bringing people into your little walled garden of the walled garden that they feel.

**6:32** · I think in general I'm okay with the use of jargon. There's a lot of talk in science communication you don't use jargon. I think jargon is okay if it serves a purpose, which it does. Deep learning is a thing, right? And so you can use the jargon. I think it's the way we talk about what we do with that stuff. Like we it almost everyone kind of sounds like an advertisement. Like we use deep learning to leverage insights from mountains of data that swoop beyond our wildest expectation and there's all these images of oceans and and hurricanes and things. You're like, what are we doing?

**7:01** · Okay, so maybe the So in addition to finding zones of more simplified language, maybe the second one is like don't go in places where there is marketing. Instead go in places where there is education.

**7:15** · Yes.

**7:15** · Yes. And I think you know, name a company or name a random product, there's probably some advertising campaign that says we leverage AI to blah blah blah blah blah. And it's like you probably aren't or you're doing it in a very you're using a chatbot, right?

**7:29** · like why I like going on YouTube and just watching actual demos. Like there's a very big difference between someone telling me what their product does and putting it on slides in font size 32 and then just being like screenshot the damn thing. What I have learned in working with like I literally coach CEOs on AI.

**7:47** · Fortune 500 CEOs.

**7:49** · And I show actual screenshot and it's like until they actually see the screen share, they're like this is what every single person talking about. I literally just have to type the words make me an agent and look into topic XYZ and it's in natural language and I just hit enter and I go yes.

**8:05** · Yes.

**8:05** · But then I hear you there's a lot of gatekeeping. Um in terms of how you're actually using it now that you've kind of come over that hump, can you like what are some fun maybe it's in productivity, maybe it's in just like you're also stand-up comedian. Do you use AI in that? Like Mhm.

**8:21** · Just how are you using AI?

**8:22** · I I do not use AI to write material.

**8:25** · Everyone note that down. We can talk about why I think that feels so strongly about that. I have written material about my interactions with AI and AI making my voice sound different from how it is and You feel like it does?

**8:40** · Uh well it's so the this is not going to be funny outside of context, but I used to use it to write emails to my students and for a while I couldn't get it to stop ending every email with thank you from the bottom of my heart.

**8:51** · \[laughter\] I WAS LIKE STOP SAYING THAT. Stop saying that. I've never said that in my life.

**8:56** · Where does this come \[laughter\] from?

**8:57** · bottom of my heart.

**8:58** · Doctor.

**8:59** · Yeah.

**8:59** · And it's like I'm sending emails that are like, you know, please be on time for the midterm. Thank you \[laughter\] from the bottom of my heart. You're like oh my god. Like I can't So so I've used it for material Welcome to probabilistic systems.

**9:11** · Right.

**9:11** · Exactly. And I think the harder I was like turn it off, the more it was like extra from the bottom \[laughter\] of my heart. And it's like I just leaned at some point I was like maybe this is the the world telling me to be more polite.

**9:22** · I mean exactly.

**9:23** · Thank you from the bottom of my \[laughter\] heart. So grateful for your attention to my emails.

**9:29** · But no so but I do use it for kind of two big things. One is for day-to-day productivity type stuff. So, uh you give a few examples?

### Jej stos narzędzi AI: Claude Code, MCP, research email pipeline

**9:38** · So, after leaving academia, I started my own company. And so, what that means is that I am constantly in need of content. I'm in need of articles to write about.

**9:46** · I'm in need of new I need to be on the cutting edge of things. And so, I basically use a mix of Claude and old-school ChatGPT uh to to very quickly keep up with the way people are using AI in my field. And so, one of my areas of expertise, as you said, is in political science. I'm super interested in both in how people in politics are using AI, and I'm interested in how we're using AI to further scientific discoveries. And so, I'll use AI myself to keep up rest of those things. And I also have ADHD, and so I can't remember to do anything.

**10:17** · So, I have all the calendar invites in in the What are we Oh, yes.

**10:23** · That's the ADHD.

**10:24** · Yes, \[laughter\] yes. I was like, she's touching me. Um \[clears throat\] but the calendar invite reminders are not enough. And so, I get emails, I get pings all the time that are like, "This isn't on your calendar, but make sure you respond to this guy and that person and these things."

**10:39** · AI-driven.

**10:40** · All AI-driven.

**10:40** · Okay, so the first one is that AI agents doing research for you? Like, what does that actually look like?

**10:46** · automated as I should be on that. I've sort of in in my while I need an AI agent to write an AI agent to That exists.

**10:54** · do those Okay, great. Perfect. That's what I need.

**10:56** · There's a lot of meta prompting uh happening. And so, that could be like {slash} skill creator inside of Claude that is the builder of other skills. And I literally, when I built out my whole digital workforce that I know you know about, but this is 34 agents that all work together as a team to help me just exist.

**11:15** · \[laughter\] Yeah, so I'm not at that level, just so that everyone you know the way that I built 34 of them and not one or two was that I first built an agent builder Ah.

**11:26** · who then created the prompts for all of them.

**11:29** · That's like the my wish for from a genie is more wishes. Like my wish for this AI agent is more AI agents.

**11:36** · So you're manually prompting you're just saying, "Run this research for me." Do you have a skill that's like do it in this way?

**11:42** · I have something that basically sends me an maybe this is very old school, just sends me a regular old email with any updates from that day or from that week in terms of things that I need to be aware of where we've either used AI in an interesting way Yeah.

**11:56** · or research has been going on about how AI is impacting political and social life. So those are the two branches.

**12:03** · But that's not old school at all. You're saying you've connected your like agent harness, Claude code, Codex, whatever. You've connected that into presumably like Gmail or something.

**12:11** · Okay.

**12:12** · So you're already using MCP, which is how we're connecting to tools. So you've already set up Google Workspace to set it up inside of Gmail. You've figured out agent harnesses. You've grabbed like are using Claude code or Codex or which one?

**12:25** · Claude code.

**12:25** · Okay. So you're using Claude code. You figured out how to bring it onto your computer.

**12:29** · Yeah.

**12:30** · So you're talking to an agent. You've connected it to the tools.

**12:32** · than it is.

**12:33** · But this is exactly what you were saying in the beginning of just like, "Oh my god." when you take a step back and you realize all the things that you've been able to accomplish.

**12:40** · Right.

**12:40** · It's actually a lot.

**12:41** · Right.

**12:41** · And it was really just born out of necessity. So I took your workshop and uh we can talk about how amazing that was. But just to sort of because I realized that this was something that I was feeling intimidated by Yeah.

**12:50** · and this was a way to sort of get over that hump and and get the lay of the land. But then it was all very needs-based. Like I didn't sit down and say, "I'm going to do these fancy sounding things." I said, "You know what I really need is to know there's so much work going on about whether AI is benefiting the practice of science and whether it's are we just generating a thousand, you know, LLM driven papers and not learning anything new or learning something new?" So like how can I keep up with this? And so I basically out of necessity because you can only what scroll the internet for so long?

**13:19** · And so so it was very piecemeal to be like, "Oh, this and then if it send it to me every day and then okay, what is it?"

**13:25** · There's a quote out there I'm going to butcher it. But, it's something like knowledge is free, but like learning is not. Like, like I can grab knowledge from 10,000 books or 50,000 articles or my entire X feed or whatever, and I can bring it back and I can have AI synthesize it. But, I still have to throw it into my own brain. I still have to look at it with critical eyes to be like, actually all of this is missing the much bigger pattern.

**13:53** · Or, this is missing this really hot take over here and it doesn't realize that it's happening in this corner of the internet because of maybe the way that I asked it or the sources that it looked at.

**14:04** · thinks I meant this because I said now I see why and I actually meant this and so then I'm going to Can I give you a very silly example?

### Kodowanie z AI i oszustwa Pytanie

**14:11** · Yeah.

**14:11** · Of of how I did this. So, when I first learned about when LLMs first came onto the scene, what, November 2022, 2023?

**14:19** · Um, LLMs came on like over 10 years ago.

**14:24** · Oh, sure.

**14:25** · Yeah, but like Transformers, 2017, and then ChatGPT, end of 2022.

**14:29** · End of 2022. I didn't sleep for days when I first used it cuz I was like, this is so much better than I thought it was going to be. And I until time, browsing didn't exist. You couldn't connect it to the internet.

**14:41** · Yeah.

**14:42** · Okay.

**14:42** · But, I still I was just like I had the this idea that I was very deep in the weeds on natural language processing and and extracting meaning from text and it was going well, the field, but it was really not anywhere near this this was such an ocean change in in terms of what it could do that I I started giving it my own data science problem sets and not only did it ace those, it suggested better questions for me and I was just like, oh my. Like, this is Frankenstein seeing or Frankenstein's monster seeing the monster come I I was freaked out.

**15:11** · It was so much better and I I was used to I had spent my career being like, data science is amazing. All of these tools are amazing, but they're not as good as you think, and if you think they're better than they are, that's dangerous.

**15:25** · And this was the first time that I used a tool that was worlds better than I thought. Okay, so I didn't use it for a long time. I was very resistant. So then I went a while. I was one of those people who was like, "I'm not going to use this. I'm not going to teach with it. I'm not going to do anything. This is not It's not I'm too intimidated."

**15:39** · And then I finally used it for programming cuz I was like in a rush to figure something out for a client and I'm there with my Python and I was like, "I don't have time to look up what's wrong with debug my code." So I went into some terrible little like Jupiter notebook add-on and the minute I started using interacting with the LLM to generate the code, it was like going from biking uphill on an old rusty bike to like motorcycling down the coast of California with \[laughter\] the breeze in my hair and I was like, "This is amazing."

**16:12** · And then, and the reason I go into all of this detail is because then I realized that it was because I wasn't in Stack Overflow arguing over whether I had some kind of bug somewhere and reading really mean comments from people who are like, "You didn't put your problem right." Okay. I was able to actually think about what I wanted to accomplish with the data and what I wanted to understand and I was able to do more interesting things and more creative things. And so having that tool allowed me to use my brain more than I would have used it had I been like, "Is this a period or a comma? Oh my god."

**16:45** · Because it was just such a narrow question before and now you can ask bigger ones?

**16:48** · Yeah, because before I was It's sort of This is going to be a terrible analogy, but it's sort of like before anytime I wanted to use Python to do an analysis, which was a lot, I often was in the weeds. It was sort of like a cobbler building a shoe. I was like, "Oh, what nail nail do I need for this? And should I make it look like that?" And then with this and it was not a good coding inter or a LLM interface, but I I felt like it was like just put on the shoes and start running. Like then who knows where you'll go, right?

**17:14** · And so I was very blown away by what I thought was going to be intellectual cheating actually engaged my brain more. Does that make sense?

**17:24** · Do you do you feel like it's intellectual cheating though?

**17:27** · In my in my head I did and I had internalized that it is a form of cheating and you should be doing the coding manually and all of that kind of stuff. And I in that moment and in the process of putting that together I was like, oh maybe I've been looking at this the wrong way.

**17:41** · And so just walk me through that cuz if AI is doing coding work and you used to do coding work or you were tasked to do the coding work or whatever, AI doing the coding work is that task being fully delegated out to AI. So why does it not feel like cheating to you?

**17:57** · It doesn't feel like cheating and this is an interesting distinction because I do still feel like using AI to write something is largely cheating especially if it's something that I'm really trying to communicate on my own and I'm open to being changed have my mind changed on that.

**18:11** · But coding has never been something that I was like, I'm interested in becoming just a the the beauty of code itself never spoke to me. The the the creativity around the architecture yeah, that's just sort of not I've always used coding as a tool to get to another end of making a discovery with data or whatever.

**18:29** · It's kind of like your soul is in one place of the work. Yeah, like in your comedy your soul is in the actual jokes that you're making and the way that you're delivering it constantly.

**18:37** · Not inventing a language with which to tell jokes. So I was sort of like, I'm an architect and I want to build a skyscraper but instead I'm hammering every floor and I don't want to be hammering every floor. And so if I could hire a bunch of people to I can sit and think about the most beautiful skyscraper in the world.

**18:55** · like there is then a level of abstraction away from the work that would then be considered cheating in your mind?

**19:02** · Like if I then built say an agent or a team of agents to say, okay, you tell me what's interesting in this data.

**19:09** · I would feel more uneasy about that or I would at least And this is just kind of a me personal subjective take. I would feel uneasy presenting that as though it were my own. I have used it to say, "Hey, here's a bunch of data. Here are some questions I have. Like, what's a thoughtful or you know, creative way into it? What's a Given that I only have time to look at it one way, which way should I look at it?"

**19:32** · Can I hear about the perspective of the students? So, you're a like professor while all this stuff was coming out.

### Nauczanie przez ChatGPT: studenci i polityka

**19:38** · Yes. Yes.

**19:39** · And I'm sure that none of your students used AI at all, and you never had to deal with this as any sort of open Why would anyone ever Yeah. I mean, I think back to my time as a student where I had, you know, 12 hours to write a 15-page paper. I would have never just pressed \[laughter\] a single button I I'm remembering of like one moment

**20:00** · where I had to write a 10-page paper overnight, and I got a Monster drink, and I drank the whole thing and like literally was like tachycardic and like couldn't go to class, and could only write one page and like could not complete it. And the guy that told me to drink this stupid Monster drink, that he I was like, "Dude, like that almost killed me." He goes, "You drank the whole thing?" So, even when I was trying to use things that could help me.

**20:25** · Yeah.

**20:25** · It It blew up in my face. Okay. So, the viewpoint from these students. So, early days, ChatGPT's coming out, and suddenly you have to decide for your classes what counts as cheating, what doesn't. Can I tell you a little bit about like, what were students kind of defaulting to?

**20:43** · What do you think students are doing now? What advice would you give to students today?

**20:47** · So, my I I was teaching So, at the end of 2022 when when ChatGPT became something everyone was using, we were far enough along in the semester that the only real exam We're only real assessment remaining was an in-person blue book exam, which we were still doing way before LLMs or anything. So, it didn't really affect us. And then spring 2023 semester was very interesting because we went in thinking, "Okay, I'm just going to teach it the same way." And I wasn't I wasn't I actually thought the students mostly wouldn't be using it. And then about halfway through the semester, I was like, "Hang on. Hey, students."

**21:17** · It was a class of about 200. I said, "Raise your hand if you've been using ChatGPT for your homeworks."

**21:25** · Know that I don't have a policy. There's nothing in the syllabus. Like I'm no and 2/3 raised their hand. And that's probably an underestimate because the others just didn't raise their hand. So everyone was using it. And so in that moment, I thought, "Okay, I have been telling these students from day one with regular programming, pre-ChatGPT, that they don't need to in my class, they don't need to memorize code. I'm interested again, I use code as a tool to do other things. So I care more that you know that if you want to create a scatter plot, you know how to go Google how to create a scatter plot and you make it and you do that."

**21:55** · And so I felt it was only consistent with my philosophy to say, "Why would I then say, but you can't use this other tool." Mhm. So I out of the gates was like, "Okay, we're going to use it, but know that you're still going to have these closed book exams."

**22:08** · Yeah.

**22:09** · And so on. But we had other professors who didn't allow it at all. And my view was we can't tell people what to do. My view was that was unfair. I understood where it was coming from, but that was unfair because you're going to go on to My goal as a teacher is to say, "You're about to go use these skills in the real world."

**22:24** · Yeah.

**22:25** · My goal is to make sure you can use them well. And not letting you use a bunch of tools that are out there that your employer is going to expect you to use or hire you because you can use them feels like a disservice. However, we had some professors who didn't allow it. It's like, "Okay, you can make that case especially for the intro levels maybe."

**22:43** · And And then we had a lot of hearings. I was the chair of the director of the undergraduate program. And so anytime there was a cheating scandal, I would come in and and preside over the hearing. And we had so many students caught using ChatGPT. And early on I thought, "Well, how are we going to tell tell difference?" Especially for code.

**23:01** · And you can tell pretty quickly. I mean, there's some selection bias, but cuz the code you're like, why did you do the same thing four times to create a single table? Like, doesn't make any sense, right? That's less obvious these days, but one of the ones we got, my favorite example, was the student turned in a problem set, and at the end of every answer, it said, "Here you go, Justin. I hope this answers your question. Let me know if there's anything else that you need Whatever, right?"

**23:25** · And so I was like, "Oh, And then you emailed him back and you're like, "You're kicked out of the school. Thank you from the bottom of my heart."

**23:31** · Exactly

**23:31** · \[laughter\] right. Exactly right.

**23:32** · He tried to defend it as And Justin is a made-up name. He tried to defend it as, "Oh, I always talk to myself when I'm doing work." And like, "Oh my He tried to defend it.

**23:40** · Yes.

**23:42** · So, there is, you know, and and again, I'm not teaching essay-based courses. I'm not, you know, you hear these horror stories about a professor's teaching memoir courses where you're using ChatGPT for a memoir, which seems Again, I'm drawing the line in in a somewhat arbitrary place, but um But a lot of what you're talking about is any student in any situation, they need to be able to explain their decisions. And their decision might be, "Why did you decide to use ChatGPT here or not?"

**24:09** · And how did you know it was doing what you thought it was doing? Why didn't you do it another way? And so So, for me, the same lessons that I always gave with data science, which is you are leading with your brain, you're deciding what data is interesting, you're evaluating whether it's any good, you're selecting what sorts of analyses Are you going to do a linear regression? Are you going to do a KNN? Are you going to do something else? And and you're interpreting it on the back end, that doesn't change even if you're using a chainsaw instead of scissors.

**24:35** · That's how I see it.

**24:36** · So, if I I'm having flashbacks to grad school when someone got yelled at for using a pie chart because like I do hate a pie chart.

**24:45** · like like at the core, a pie chart made no sense in that context.

**24:49** · Sure.

**24:49** · And it was like, "You just did it cuz it was the button that you knew where Yeah, there you go.

**24:54** · Yeah.

**24:54** · Okay, but the ability to explain and explain not only just the actual work, but maybe when you decide to use what tool and why and maintaining critical thinking throughout. Which I will say Yeah.

**25:06** · I have been a ghast to observe that in the quote-unquote real world people are not doing that. I mean people are that I'm seeing, right? And this people are not We are I'm seeing when I go to companies, one of the reasons I I went back I had left academia and then I went back was I was like, we need to train people to use these tools more responsibly is I go to companies who then are who are incentivized to use AI.

**25:31** · They have to turn around a deck tomorrow and I don't see nearly enough Why am I looking at this data this way? Why do I think that this is the interesting trend? Why am I make Why am I assuming that because I saw this trend, that's the actionable insight, right? Or And so the the kind of thought that I'm trying to instill in my students, it's not it's because I think the world needs more of it. It's not because I'm seeing it out there. I think there's there's a lot of ways to miss And and misusing AI is like misusing linear regression on triple steroids.

**25:59** · On it's on like I don't think the other person knows what that means, but Okay, \[laughter\] monster energy drinks. Uh, you know, the the misusing chart like lies, damn lies and statistics, right? I can make it look like something's going up like crazy by manipulating the Y axis. You add AI to that, you can tell any story you want to tell to anyone.

**26:17** · It's also going back to what you're saying and and I'm thinking about, you know, all roles, not just like a data scientist inside of a business. But one thing that I have found in my work with these companies and one thing that I advise them on is that urgency is poison. Yes. Like if you are if it is the night before a big shareholder call, you think the CEO is just last-minute running a couple numbers and doing some research? No.

### Pilność to trucizna: porady dotyczące burzy mózgów w przedsiębiorstwach

**26:41** · And so maybe even on a smaller scale, prepping for a client meeting 5 minutes before and it's the biggest client of your entire year. If it's a smaller client, if it's someone that you've known for 5 years, whatever, you can prep in a different way.

**26:56** · But, I think companies, because they're really dialing up the importance of productivity, or at least the internal pitch of productivity, they're setting up pretty horrible internal incentives. Because if your output has to be 10x, the number of hours you're working, let's assume that it has stayed constant. That means that you only have so much time before the next thing is due Right.

**27:20** · to be able to turn all around.

**27:21** · Right.

**27:21** · I was brought in for one of these large fintech companies we talked about to think about how we could use generative AI or or we weren't quite at a genetic level in this particular case, but to to better to improve inter Wait, let me restate that. To improve cross role and cross I was going to say discipline, but cross What's the word I'm looking for? Cross-function.

**27:43** · I was working with a company to figure out how we could use generative AI and LLMs to improve cross-function communication and like brainstorming between sales and marketing or marketing and finance and kind of overcome that silo problem.

**27:54** · Yeah.

**27:54** · Super interesting problem. Uh working with my PhD advisor, Scott Page, who does a lot of work on collective intelligence. And so we were really trying to think about how can we make it so that you have all these diverse perspectives in the room and really take the time to understand what each other are saying and then come up with solutions that are way outside the box that no one could ever think about.

**28:11** · And our biggest recommendation after all the look looking at all the tools and all the math and all the different things we could do, our biggest recommendation was the more ur I I guess urgent or higher stakes the thing that you're working on, the more you need to make sure to pause and carve out a decent chunk of time for everyone to throw in all the ideas they can think of and then to sift through them thoughtfully or have an LLM help you do that or whatever and then move.

**28:38** · After you've looked you generated all the ideas, you evaluate all the ideas, as a group you agree like this is the one we're going to do, even if it's just an hour before you then dive in and instead they said we can't do that because basically the workflow they have that I think a lot of companies have is boss says we need this thing you say I'm going to do this as fast as I possibly can as opposed to what we were recommending which is boss says we need this thing pause for a second and say is

**29:04** · this the thing that we need does this actually serve our customers is this going to be fast today but a huge problem a year from now and you don't need to do that for every problem but our major you know we research the company we did all of these interviews so it was this multi-pronged approach and our biggest recommendation was you are hurtling full speed ahead over a

**29:24** · cliff like you need to pause and make sure you're doing what you need to be doing and there's just no slack built in to people's work days to use to free up the creative thinking right we're using AI to be faster but we're just filling it with more crap that we have to do as opposed to saying because I have AI I could take 30 minutes to walk around the block and think about what a really big idea would be that no one is actually thinking about like we're not using it to actually generate big ideas in the way that we could I also I'm going to pull two things out of this one is actually how I use AI

**29:55** · agents and the other is enterprise advice I think it's really hard for an enterprise leader even though it's the right advice it's really hard for an enterprise leader who is gold on these crazy short-term things and has to hit certain revenue by the end of the quarter and has to pass something off to the next department whatever that thing is it's really hard to say no no let us take this extra hour because across multiple projects it's going to be an extra full work day if however you start to pull into that

**30:26** · success metric you say all the things that went wrong when they didn't Mhm.

**30:30** · then I have now realized that like the enterprises that have a longer-term view which means that they are able to bake in the screw-ups from a bad short-term play Yes.

**30:43** · they're in a much better position.

**30:44** · Yes.

**30:45** · Similar to how I work with AI agents. Like, what I have learned is that the boring bits of AI get you 10x farther than if you're only focused on like the whiz-bang, wow, let's make a quick deck.

**30:57** · Right.

**30:57** · And I spend literal hours on the prompt to make AI sound more like me or the entire SOP or skill or whatever. Like, one freaking file that is now, you know, a markdown file, whatever. But like, let's just call it like a Google Doc.

**31:13** · Yeah.

**31:14** · Where you're just like, "How do we pitch to clients?" Or, "How do we write proposals?" Or, "How do we give keynotes?" Or, "How do we structure like a workshop for tens of thousands of employees?" Whatever the thing is, at some point, I sat with my own thoughts, maybe a little bit of collaboration with AI, but I wanted to write out, "What is that perfect

**31:38** · guidebook, the employee handbook that I would pass over that says, 'If If I woke up with amnesia or if I had to train someone new, like, what is the thing that I'm telling that person?'"

**31:47** · Yes.

**31:47** · And that takes hours.

**31:50** · Yes.

**31:50** · And and maybe days or at least multiple times of that multi-hour iteration. And so, I'm looking at these two things going, clearly speed of iteration matters inside of a business, whether you're small, medium business, large enterprise, it doesn't matter. The ability to just like get more cycles, you're going to be in a better spot because you can experiment, whatever.

**32:06** · Mhm.

**32:07** · But also, if you lack that long-term view, you're going to make the wrong short-term play.

**32:12** · Right.

**32:12** · If I'm going to be super efficient every single day, I might just be super efficient in a direction that ultimately does not serve my organization or just serve me. And I will say, we So, we this was our recommendation to this company, and they said, "We can't work with that. We don't have time built into our schedule." And so, we just So, we said, "Okay, know that this is our recommendation, and I would like to, you know, insist that you float it to the the and you present the the summary of all of this, and okay, we'll give you our other recommendations given that.

**32:40** · And again, this isn't like every single day, every time you're asked to do something you need to say, "Wait a minute, what is the main nature of our work?" It's really when you have these big critical, whether it's, you know, quarterly meetings or one-on-ones about your own personal goals, is like, what if we just took a moment to to really think about, yeah, what if we learned about what doesn't work? What's the thing that you all do that you all know is a waste of time? Do we have to keep having this particular type of meeting?

**33:04** · Yeah.

**33:04** · And so on. I will also say, we haven't tested this, but and this is all credit to Scott Page on this, wrote a piece, I forget the I think it's the Journal of Collective Intelligence, where basically his recommendation, I'm curious what you think of this, is meetings are terrible.

**33:18** · Everyone hates meetings. You go into a meeting, it's an hour-long meeting, you have 10 people in the room, everyone speaks for a few minutes, like, here's what I'm working on, here's what I think we should do, and you know, and then the next person, the next person, and you're bored out of your mind, and then everyone gets an AI summary after the fact that nobody reads. His recommendation was for the first 10 minutes, everyone talks through Whisper Flow or not, you know, whatever.

**33:36** · Everyone talks their ideas, and then for 10 minutes you all chit-chat while AI summarizes all the ideas that everyone had, and then you spend the rest of the meeting reflecting on the ideas that were shared and aggregated. And so there are ways to build in that slack using AI or leveraging AI to do more out of the box thinking. Whereas I think what you're describing is still a lot of people are like, I'm just going to automate my emails, and I'm going to do this, and I'm going to do that, where you can really restructure how you do things.

**34:02** · \[snorts\] So I think AI as a teammate is one of the biggest hacks. Every single person is still using it as a little tiny productivity paper clip in the corner.

**34:09** · Yes. Like clip it yeah.

**34:12** · So I would I would I'll I'll I'll share my thoughts on that and what I would also be doing in that finance example. Um again, you're a genius and you shared probably 50 recommendations. This is just one other thing.

**34:26** · Um first, in that meeting example, and and by the way, this is this is all anecdotal. I don't have like a perfect set of data to prove this. But my team uses this every single time. So it's kind of like it's it's not it's like an Oreo with extra frosting on top.

**34:44** · Double stuff. Oh, on top.

**34:45** · Yeah, which like it I guess it or it's like a \[laughter\] a chicken club but then you take off the top bread. Whatever. It's ABAB. It's a sonnet or whatever. Okay. So it's you start with some sort of let's all get ideas out there and this is also part of crucial conversations that like the best meetings you are doing presumably you're doing some sort of internal thought right for brain writing anyways. So some sort of internal thought solo person you're getting things out there.

**35:15** · My team sometimes will just throw things into the zoom chat window just to queue up like all the topics before we look at it. And then you can have if it's really complex particularly you can have AI review that synthesize it and maybe even just re-prioritize how you should talk about it or group things or decide what to delegate or even create an interface that creates like a dynamic interface for that meeting. Sure. Then maybe 25 minutes you're actually doing talking on it very fast-paced AI's recording that whole thing.

**35:45** · Then there's another whisper flow break. And so what our team does particularly for like big brainstorm things we will still have an AI recording the meeting.

**35:56** · Then we take out usually our phones and we dictate back and forth to order or whisper flow or whatever the thing is that we're doing and we will get to one unlock for each of our parts. So if I was blocked on like I can't quite figure out the difference between these two or I wonder how much the average something rather is.

**36:16** · I will just fire off like midway research tasks and now there's like some ways of integrating live agents but like for the most part we're firing those up and then we reconvene one more time and go around the horn to say, "Here's what I unlocked. Here's what I unlocked. Here's what I unlocked." and then share action items.

**36:34** · And then the AI summarizes it and whatever. But for the most part, I agree no one's really reading the AI summaries. The reason that we have AI recording all of our meetings is because we're building up the open machine, which is the name of the company that I run. We're building up that open machine to function as a context layer for a whole company. So, like \[snorts\] recording meetings, I don't think you should read the summary anyways.

**36:54** · But having it as a record for future, whatever.

**36:56** · Building it up so that you have a folder of 3 months of meetings. So, you can go to it and ask, "How have my patterns changed? Am I a good seller? What is the number one or it's top five complaints that clients have given?

**37:09** · What are three mistakes I keep making?"

**37:11** · Whatever those questions are. But having that as a context layer was very, very important.

**37:16** · Well, and AI is only as good as the data you give it. And so, the more that you're able to invite it into the way you're living your life as opposed to just giving it access to a few select things.

**37:25** · Yeah, and I think that in 5 years ago world, I used to be very careful of like it has to be this image that I give to the AI model to train it because it's the perfect image or whatever. Like you'd have to curate the hell out of it because finding the needle in the haystack was actually really hard even in amazing enterprise search use cases.

**37:49** · I actually think now AI is much better at managing a massive amount of data. You kind of can boil the ocean a little bit and give AI wide access to your emails, your meeting transcripts, your trouble tickets, your customer support, you know, discussions. And you'll be able to parse out brand new things.

**38:14** · Like even if that's creating a new onboarding guide for a new employee or maybe that's creating FAQ for your website or maybe that's brainstorming back and forth with an AI system about like a new business offering you can have. But that's all just building up this mass context layer that other than keeping it in like a relatively organized file system, I'm not sitting there going, "Mm, that meeting wasn't high enough quality. Therefore, I will delete it."

**38:35** · No, no, no. You want the This is just like stand-up comedy where my friend and I always have to remind each other the bad shows is where you learn. You're like, "Why did that joke didn't work?

**38:43** · Wow, I didn't do well. No one liked me.

**38:46** · Why not?" If you were to only keep the good ones and you only rewatch the good material, you don't know what it is that you're doing that's not working. And so, I'm a huge proponent, AI or not, of tracking all the failures and all the times it didn't work and all the times it fell flat. Or you have a whole bunch of meetings where you're like, "None of us I felt like I walked away not feeling like we had any marching orders after that." Like, what was going on? And maybe you'll find something interesting. So, Yeah. This is it's so interesting.

**39:10** · So, going back to what I think is like the biggest moat of maybe the century, but like the biggest moat certainly of the next 5 years is speed of iteration. If you believe that speed of speed of iteration is the moat, then you have to build things that allow you to do things faster.

**39:28** · Right.

**39:29** · Clearly, a context layer is one of those. And what you just said, looking at the end to go, "Did that work or not?" And in your finance example, if they were to look at what happened when they rushed through a decision, they would know that that did not perform well.

**39:44** · Right.

**39:44** · And maybe then they would carve out that time to like better manage it.

**39:47** · Well, and one thing we did, and this is a very, very small scale, but it was a kind of a for instance for this particular company, is we did an experiment in the organization where we said, "Okay, half of the the whole team is going to come together and we're all going to talk about collective intelligence and all these practices."

**40:01** · And then we randomly selected half of the managers to say, "Okay, I want you to build in this kind of slack." Or like, you know, do it in the way that works best for you, but actually use these tools and report back to us and let's talk about it. And then the other half just went on and lived their lives.

**40:14** · And of Of you can't you're comparing apples to fax machines, but uh that modern example, let me \[laughter\] talk about AI and really it's it's my speed of faxing that I've picked up that I really thank Claude code for.

**40:27** · But we really did see some, you know, hey, we actually got ahead of it's anecdotal, but we got ahead of this issue or like we were all going to do this higher and then it turned out we actually didn't need to fill that role. Like pretty big questions or or kind of pivot moments that came up that we didn't see in the kind of more pro forma group.

**40:43** · Uh first if you have not yet seen season two of The Pit at some point they have to bring in a fax machine and they run out of toner and someone's like, no, we can't possibly send a fax and it's like, you can still send a fax without toner cuz you're not printing anything. You can just scan it through.

**40:56** · Yes, that's right. Like Yes, there's no ink in use and so like just watching the the new hires figure out what a fax machine is and can do, I was like, is this the moment that we all figure out how old we are?

**41:09** · No, I I remember hearing about a fax machine for the first time in the 90s and being like, you're using a phone, but it's printing something out on the other \[laughter\] end. I'm like, this is insane.

**41:20** · Imagine how people feel learning about agent harnesses. The second thing so going back however many minutes ago.

### Agent nadzorujący sztuczną inteligencję

**41:27** · Sure.

**41:27** · So, idea one was bringing in AI as a listener and that like back forth ping pong. There's a second one that I've brought into my digital workforce and I'm now in the process of building out more, but I haven't I have so I only have got one of these.

**41:42** · Mhm.

**41:42** · But basically I built out this whole digital workforce of 33 agents. I had a chief of staff, the chief of staff named Simon had six direct reports. The six direct reports are named after Friends characters. So I've got like Chandler's running marketing and then they all have direct report agents and they can spawn little temporary agents, whatever.

**42:01** · What I was realizing was that Simon was like so busy going, okay, you do this, you do this, you do this. It was acting as this like big orchestrator that we didn't have that extra little layer of going, is this even smart like is this the dumbest thing I've ever done? It's like you got to whip all these egg whites. It's like you're not making a meringue. Exactly.

**42:19** · And also is the meringue even tasting good or can we whip it faster or can we whip it real good?

**42:24** · \[laughter\] I think we can. I am really happy that you did that. Diva shout out. Wow. Okay. So the thing that I built that ended up being that 34th agent and that I'm building more of is like an AI watchdog and so you can use a scary word like watchdog. You can also use a more enterprise word like project manager.

**42:44** · And so there are we should call all human project managers watchdogs. I feel like that's \[laughter\] like what the stakes in a lot of organizations.

**42:54** · I think like so okay. So the way that I'm using AI watchdogs is that I'm picturing a little helper carrying a key clipboard and just witnessing what is happening and going like what patterns keep coming up that we need to fit. It's kind of like a McKinsey consultant sitting in the corner.

**43:14** · And so this this character this persona this avatar is witnessing all the work is involved in every single conversation not as a contributor but as a witness and is keeping tally of like how often certain problems come up.

**43:30** · Or maybe like these this team and this team or these group of agents and these are coming up with the exact same problem.

**43:36** · So the reason that I want more of these watchdogs is because I was talking to a founder who was like of a very very big company and he was basically saying I am so sick and tired of realizing that two teams are working on the exact same thing. Maybe they came up with slightly different ideas but that just ruined an entire team's worth of work and like we could have had some creative amazing output from that team if we had only told them this other team about it.

**44:04** · where the like if we had one conversation three months ago we could have all been like, "Oh, you're also doing this? Okay."

**44:09** · Or if an AI watchdog is going, "Why are these two teams doing the same thing?"

**44:15** · And they at least flag it to the human. Because there are going to be times where you bring together those people for an hour and the same output came out. I I kind of disagree with that thought, but like, you can imagine that maybe the the um the improvement on the ideas is whatever, 5%.

**44:31** · Right.

**44:31** · But I can also imagine that anytime that the watchdog would weigh in, it's like got some sort of threshold for how risky or high liability, whatever that problem is. And that the watchdog is going to say, "Hey, get some more eyeballs on this."

**44:47** · Right.

**44:48** · So, I want I want more AI as a teammate functionality and I don't just mean AI as a I like I want more AI as a teammate functionality and I don't just mean Ali got her own chief of staff and I have my fancy AI. No one can use my AI.

**45:06** · What I want is individual or groups of AI agents that are up-leveling my whole company, my whole team, this whole meeting, that whole project, like so many people. And and I see this also anecdotally, so many people are coming to me saying, "How can I use AI I I I?"

**45:23** · And I get it. Like, that is absolutely the first thing that you want to check off your list. But then no one's asking the bigger question of going, "What is my whole org need?" And then we're kind of running into some issues on like staffing questions or org structure questions cuz no one's looking at that bigger picture. I wanted to ask you about just like job layoffs.

### Co mówią dane o zwolnieniach

**45:45** · Um both from like a data perspective and anecdotal perspective, just like, what are you seeing among your clients? Where are the trends headed? Do you believe in what the, you know, headlines are saying?

**45:57** · Well, one of the things that I wanted to ask you I'm going to be a politician. I'm going to answer your question with a question. First, and then I'll answer your question.

**46:04** · \[laughter\] But But one thing that I'm struck by as you describe the various ways that you've used AI or your team or or you've worked with other companies to do so is that at no point did you say anything about using AI to figure out what human to hire or what human to promote or human to lay off or using it to make personnel decisions or even performance reviews or things like that. And my viewpoint, I am originally trained in the social sciences and so I'm Maybe this is old school or maybe this is just massively risk-averse because I know that data itself is biased and we use using AI codifies a lot of those biases.

**46:36** · I am very strongly against using AI for personnel decisions in the same way that I wouldn't use AI to assign a grade to my students, right? Like I would want to sit down and make sure that I'm doing that. Do you advise This is getting to layoffs. Like do you Where is your stance on say, "Hey, let's Why don't you just assign everyone on my team a performance score for the year and then I'll promote the top five?"

**46:57** · So there have already been tech systems that weed out bad resumes. And you can argue whether really good resumes get weeded out or whatever. But these like I think they're called ATS, whatever. They like look at these systems and they're going, "Oh my god, this person's resume is 18 pages long or this person's resume is one paragraph long or there's so many typos or whatever."

**47:17** · Right.

**47:17** · So there's a little bit of weeding out that was pre-checking resumes.

**47:21** · forever.

**47:22** · Yeah, which like Like I see both sides. Companies are very overwhelmed with job applicants. And also how rude to not have your resume actually seen by a human. Because maybe the system is against you. I I don't use AI for any hiring decisions. Also because if you look at like the EU AI Act pyramid, it's like in the crazy high-risk don't do it category.

**47:46** · Exactly.

**47:47** · Uh in the same way that I wouldn't use it to figure out like who gets a loan.

**47:50** · Right.

**47:51** · Um if you're using it for like underwriting loans or you're using it as a brainstorm buddy for you and writing underwriting loans.

**47:58** · Right.

**47:59** · Having AI at least make the final decisions sounds morally wrong right now. Um on the hiring side though, what I have found and I do think that AI could help on this. Um And we can argue on that.

**48:14** · Sure.

**48:15** · So we'll we'll post a new job description. We'll get 250 applicants and 120 of them are the exact same ChatGPT or Claude answer because they take the question and they go, "Here's the question. Look at my resume and respond."

**48:29** · Right.

**48:29** · And there are signs that I, as someone who uses AI hundreds of times a day for the last several years, can see, which is are all the paragraphs the same length?

**48:40** · Are there similar starting sentences like prepositional phrases like, "When it comes to blah blah blah," comma.

**48:47** · It's not this, it's that.

**48:49** · Yeah, and those are the more obvious sounds or like, "Honestly?" question mark. I get really Every time I talk to ChatGPT, every paragraph begins with, "Honestly?"

**48:59** · Yeah.

**49:00** · Yeah.

**49:00** · And so you could almost kind of flip it on its head and say, "Technically, I'm using AI to weed out applicants because I'm seeing who falls for AI traps and I'm removing all 120 of those applicants because they were not smart enough to know that they should stand out." I don't care that they used AI, they used it in a boring way.

**49:19** · poorly.

**49:19** · Right. If you're using AI to write something that doesn't sound like every other piece of AI you've ever read, that's probably the person you want.

**49:25** · And it's it's That's right.

**49:26** · You're you're right though, like I don't want to hire a boring person. So I think that's one. The second is that a lot of the companies that I work with aren't just figuring out, "Okay, I want to hire this person versus that person because this person has AI experience and that person doesn't." That might be one trade-off.

**49:42** · Right.

**49:42** · There are other layers to that like that means we have to retrain every single one of our hiring managers or the people who run these interview loops to find these new skills. It means we have to update all of the interview question banks that we have to redistribute them out. Uh it means that we might have to update the way that we schedule stuff with applicants if we think we're going to have more or fewer clients, whatever.

**50:03** · Applicants.

**50:04** · The other side though is that companies are changing the structure of teams. Yes. And so like I I don't think a lot of companies are using AI to figure out what the structure is.

**50:16** · A lot of them are kind of circling around the same thing, which is a lot of fast-moving enterprises right now, and I want to get back to layoffs, but a lot of fast-moving enterprises right now are thinking to themselves, "Mid managers don't make any sense anymore.

**50:31** · Right.

**50:32** · Or we should at least have a flatter org with fewer layers, where from CEO down to intern is only whatever, five layers instead of 10." That is one, so flatter org, probably uh uh higher number of reports to person, or a mass removal of mid managers, or a re-pivoting of mid managers into ICs, very, very high-performing, high-expertise ICs.

**50:56** · Right.

**50:57** · And having smaller teams is definitely another one. So like a lot of the best ideas that I see are coming out of teams that are two to eight people.

**51:06** · the uh a friend of mine who's a a consultant gave me the language of the the pizza theory, pizza box theory.

**51:11** · Two pizza team?

**51:12** · Yeah, which I had never heard before. I was like, "Wait, you're you're giving everyone pizza?" But then I understood. \[laughter\] And then I was like, "Oh, that's right.

**51:18** · Okay, great. Yeah."

**51:19** · I It It's this concept of like a two pizza team, which in my head I'm always like what if the project is really a hungry project and you you're not going to eat a whole pizza yourself?

**51:31** · \[laughter\] Is that part of the team? Like are we I get too hung up on the details."

**51:35** · two to eight sounds right for for a two pizza team.

**51:38** · Right.

**51:38** · Um I think the bigger thing, whether it's like this exact number, the bigger thing is like, "Does a team of 300 on one project make sense anymore.

**51:48** · Right.

**51:49** · Because you need fewer people holding context. You need like higher ownership per person. Each individual person is probably building out more processes or workflows or agents or whatever to be able to build up that scaffolding, that system to actually get that product project done. And if you have more people involved, it's just more complex.

**52:08** · Right.

**52:08** · Like that is the thing that I see people doing and that does have headcount implications. Are you Talk to me about just layoffs? Like what are you seeing?

**52:18** · So it's it's this is a case where the gap between the lived experience and the and I say anecdotes not as a dismissive dirty word, but as a what I'm seeing on the ground versus when you take a step back and say, well, what are the broader trends? Is that the word, you know, among colleagues of mine, among clients, among companies that I've worked with is there's massive layoffs, particularly in tech, there's massive layoffs and of course it must be because of AI. And once you step outside of that and say, well, okay, let's look at the labor data.

**52:49** · Let's look at the company turnover data. Let's look at who's getting hired, who's getting fired and what the job announcements are. It's a lot harder to purely tell that causal story. Not to say that that doesn't mean it's not there, but in general, yes, there are, you know, a number of layoffs at the time of our recording. They were on the heels of of a number of high-profile layoffs from tech companies.

**53:08** · They may even say, yeah, this is because of AI, but they might be just saying that as a cover for we needed to do some internal restructuring and and we're going to you know, make it look like we didn't make a huge mistake in our hiring two years ago and when we fix this. So So actually getting into the data and saying, okay, are people getting laid off and specifically replaced by AI? We just don't have that kind of granular information. It also of course is going to vary across sector.

**53:33** · So I tend to be of the view and this is kind of again the old school social science hat is that this may well be what's going on, but I have yet and I've been watching it for maybe a year, year and a half as we've really seen this ramp up. I have yet to see meaningful signals in data from employment data that this is actually what's happening.

**53:53** · So I I don't know if that's consistent with what your It doesn't mean that it's not, but it's because I and this was the same thing by the way. So I was, you know, head of AI for startups and VC at AWS. When we were looking at who is an AI startup and who is not, Mhm.

**54:08** · which now is 99% of all startups and at the time was literally 5% of the market.

**54:14** · When we were looking at who was an AI startup, the line that I kept getting back from like corporate venture capital teams or VC teams or whatever was like, well, 50% of startups say that they're using AI. And I'm like, that's actually still very important data. Like it is important to know that all the headlines say AI because that means that there is a positive incentive for that company to say that it is AI. Right? Whether it's AI washing or actually because of AI.

**54:40** · Right.

**54:40** · We're seeing signs that if you say it's AI, your stock price goes up and if you say whoopsie daisy, I hired too much in 2022 or that we hired the wrong people, your stock price goes down.

**54:52** · Or that we're switching from and I don't know what their stock price did, but switching from making shoes to cloud intelligence \[laughter\] or whatever it was. EVERYONE WAS LIKE, WHAT? YEAH.

**54:59** · Uh Allbirds, their stock went up 6x when they just waved the AI magic wand.

**55:04** · Yeah.

**55:05** · And This is an AI podcast, by the way.

**55:07** · \[laughter\] Yeah. It's just like I Well, I don't believe the shoe thing. But it is an important thing to know that those incentives are there because you should therefore be taking a much more critical eye to any headline that you see saying we laid these people off because of AI.

**55:24** · Right.

**55:25** · I think when I both the the literal clients that I have that are like retainer and then also just large enterprises that I just chat with at conferences who I don't consider to be clients, but I you know, we trade insights.

**55:37** · Anytime that I'm looking at that, one of the biggest, biggest things that I am feeling that I've shared with that mastermind team, that I've shared with my clients, is there's this deep feeling that the person who succeeds in the AI age is not the same person who succeeded at your company in 2017.

**55:56** · And that it is taking every single department lead, exact, whatever, the whole XCOM. They're looking inside their company going, "Do we even have the right people to be able to build this out?" And so I talked to a lot of these companies and they're like, "Listen, we just got to get rid of the B players in the AI age." And so that looks like people that don't have high ownership, people that don't have deep subject matter expertise, people that have refused to learn AI over the last several years. Not because they're standardizing their entire day on it, but because they can have a critical eye and start to use it in some places that make sense.

**56:28** · Uh people that have really good systems thinking, that can figure out all the things you were talking about before about just like cross-functional collaboration.

**56:36** · If someone is a full hermit, has not been tied to revenue, refuses to use AI, and is kind of acting as like a negative culture point on AI, and someone who waits to be told what to do, why would you want that person at your company in 2026, 2027 and beyond?

**56:57** · So that is I like I see I see org restructuring definitely happening toward those flatter orgs, toward smaller teams, spinning up frontier units. I see companies working to figure out what the right profile is for an employee in 2026 and beyond, and making their hiring process and firing process better reflect that. And then I also see a lot of headlines that I don't believe in at all.

**57:23** · Right. I mean, the other piece to know about all of this, and and and this isn't news, is that headlines exist to get us to click on them so that companies who are projecting are trying to trigger crazy deep layer of something.

**57:33** · And so you you want to trigger things like fear and anger and then you're going to get people to look at those things. I will say I I agree with you on all of that and I do think and there may be a fair amount of churn and we may be entering that churn in a big way now where we look like getting rid of a lot of people realizing that we're not actually a one-to-one replacement where it's like, "Oh, because I fired Rebecca or laid off Rebecca, I now have an agent named Rebecca and we're doing this one-to-one." Like that's I think companies are going to learn quickly that that's not what's going on. And so I think you're right that we're going to see, "Oh, we actually need people who can do the system thinking.

**58:03** · We actually need people who can oversee this." And maybe the whole organization roughly has the same number of people, but the way teams look is totally different. I will disagree with you slightly or or at least raise a a concern around the A players versus B players because a fair a lot of work I do with companies is specifically around performance management and and performance measurement and we are doing AI or not, we are bad at figuring out who contributes what to our team.

**58:32** · I am optimistic that AI could help us figure that out and particularly unearth the unsung heroes who don't speak up in meetings, but when they put something in the chat, it's so helpful and it just clarifies where the conversation goes and maybe over 3 months or many months of of looking, you know, having an AI go through your transcripts, they'd be like, "Actually, the presence of Susan every single time means that meeting ends with a with with a direction as opposed to wandering."

**58:59** · Like how many times have you been in a meeting where it's like the person who never speaks is actually really really valuable and the person who's talking all the time, I say as I'm talking loudly right now, has nothing useful to say, right? And so humans and our biases, we like the loudest voice in the room. We like the system thing. We like the guy who says, "I'm going to use AI to revolutionize everything." When in fact, if we really want a sustainable robust AI-driven organization, we want some AI skeptics.

**59:23** · Not not you know, necessarily like going to going to you know, unplug the computer when you're using it, BUT LIKE YOU WANT SOMEONE to be like, I don't know if we should rely on it for that. We should do this more analog. And you want people who are actually hermits who kind of put their head down and get things done. And you want people who occasionally have amazing ideas and do very little otherwise. And so so I'm less optimistic that we will correctly suss out A player versus B player. And I worry that we will amplify existing problems of A players all kind of look like the same Yeah.

### Gracze klasy A, gracze klasy B i maksymalizacja tokenów

**59:55** · So first definitely wasn't saying whether they do it correctly or not.

**59:58** · yeah, but in principle they could.

**59:59** · that's what they're trying to do. And by the way, you bring up an amazing point. And this is such a big tension point inside of businesses of all sizes right now, which is yes, I can look at AI usage.

**1:00:12** · Mhm.

**1:00:12** · Yes, I can look at token usage. That still doesn't tell me who is doing awesome stuff and who's doing dumb stuff.

**1:00:19** · And so whether you're figuring out an A player versus a B player, whether you're figuring out whether this person at this usage is contributing value or not, I think we're in a really difficult position to try and figure that out. And so companies maybe should should lean on the side of like let's let's do some more experience experiments to figure out who might be contributing well.

**1:00:43** · Um what I would be looking at though is like or what I give companies as advice is token maxing, which is just spending as much money as possible or using as many tokens as possible. And if you use open source, it's a lot cheaper, but whatever.

**1:01:01** · Using as many tokens as possible, having AI work 24/7, having AI work while you sleep, having hundreds of agents work while you sleep, and running up a bill potentially of thousands of dollars a day. Right? Which is nine figures over the course of the year. Okay. So if I am looking at all of the people who are token maxing. I then personally would in person interview these people. Yes.

**1:01:27** · And I would say, "What the heck are you building? Show me what you're building."

**1:01:30** · And you kind of need human as a judge combined with AI as a judge, fine, to look at the actual value that people are cranking out. I know of companies who are like, "We have an AI leaderboard based on token usage and just to move up, you're going to gamify the heck out of it and you're going to say, "Well, I'm just going to throw the Great Gatsby in every 3 and 1/2 milliseconds and I'm going to charge tens of thousands of dollars to my company, but man, I'm going to be at the top of that leaderboard."

**1:01:59** · Right. We're optimizing over something that's entirely unhelpful if not expensive and counterproductive.

**1:02:04** · Yeah.

**1:02:04** · And it And again, maybe it's a helpful indicator to figure out who you might want to start interviewing right because it is likely among those bigger AI users that the revolutionary work is happening.

**1:02:17** · not the case that just because they're using a ton of tokens doesn't mean they're doing Exactly. In order to find a square, I must start with rectangles.

**1:02:25** · And so like that is where Though, even then, and I realize we don't have infinite time to to do these things, even then, I would be sort of interested in the people who are barely using it because they might be doing something incredibly efficient or incredibly exciting. It's probably not where you would start, but even AI skeptics, like you were talking about do you want an AI skeptic on the team? I definitely want an AI skeptic on the team, but they better be one of the most AI literate skeptics ever.

**1:02:50** · Sure.

**1:02:51** · If they are a skeptic and they're like, "This doesn't work." I'm like, "Get off my team."

**1:02:55** · Right. So, they at least need to be at the middle level.

**1:02:57** · Yeah.

**1:02:57** · Like I I was at a board meeting and a CMO of a company that every single person has heard of said, "I don't like using AI for writing cuz it can't write well." And was said can't write good.

**1:03:12** · \[laughter\] Can't write well, okay?

**1:03:15** · And he was telling Yeah.

**1:03:18** · that therefore the entire marketing org is is is told, AI can't do that, so you shouldn't do that.

**1:03:26** · And I was like, how are you prompting this thing?

**1:03:27** · Right.

**1:03:28** · And he was like, well, I gave it examples of our ads and then asked it to write more. And I was like, did you give it 10 ads, ask it to make a brief, ask it to reverse engineer the work, ask it to loop on itself 10 times, to check itself, to bring in five other agents to then check that work?

**1:03:43** · it's the equivalent of hiring a brand new person out of college and saying, hey, create the greatest ad copy you've ever seen.

**1:03:49** · on these 10 examples.

**1:03:50** · Yeah. And then being like, well, they don't work.

**1:03:52** · Yeah.

**1:03:52** · Yeah.

**1:03:53** · And so I You're right. You want you want some level of proficiency.

**1:03:56** · I want I want AI critical thinking and sometimes that will look like a skeptic.

**1:04:01** · Right.

**1:04:02** · And I also But I know, I think and I think to be a skeptic, you need to have really used it. Like I think that if you're at zero, you're you're not informed anyway.

**1:04:10** · skeptic. Like in the same way that you asked your students, defend this decision, defend this decision.

**1:04:17** · Right.

**1:04:17** · I'm going to have a live debate. I don't care if it's in front of thousands of people. I want to hear why you have that opinion. Give me three examples. Tell me three things that you tried to fix and why it still failed. Tell me two other people you talked to and why it still failed. Tell me two YouTube videos you watched and why it still failed.

**1:04:32** · Right.

**1:04:32** · Then I'm on your side.

**1:04:33** · I think the analogy I I had in my head, and tell me if this is perhaps not appropriate for for AI, but around the token maxing piece of it, I it it's it's almost comforting because even with all this technological and computational change, we're still humans with the same problems. And one of the biggest problems we have is that in the workplace is that we are still measuring inputs, not outputs. And that was the case way before AI, right?

**1:04:57** · Yeah.

**1:04:57** · hours are you in front of your computer?

**1:04:58** · How often is your Slack thing green? How many who's staying latest in the office?

**1:05:02** · Not who's actually coming up with the ideas or delivering the thing or landing the client or doing whatever cuz it's just harder to measure.

**1:05:08** · Yeah.

**1:05:08** · So we're coming at all of these problems with a factory floor mentality, whether we have AI or not, right? But one of the things that I think about when I think about token maxing and why I'm like, I don't know, I would talk to the middle users, not the zero, but the middle users as well, is a company I was working with talked about how they measured productivity. And this was right before LLMs came on the scene and they said, "Okay, we reward whoever writes the most lines of code."

**1:05:32** · And I was like, "That's insane." Because the worst coders are going to write thousands of lines of code.

**1:05:37** · bloated code.

**1:05:38** · Genius coder is going to do something massive in three lines. And so that's where I bring that lens to the token maxing side of things and say, "If you're doing some really cool stuff or you're getting to these outputs that the CMO thinks they can't get to, but you're doing it with two agents and three incredible prompts as opposed to powering out 600 agents who are, you know, spawning more agents, then I'm interested in that."

**1:06:00** · Yeah, and maybe what we're kind of coming out of it, we're saying at all levels of AI usage, token usage, you might just want to chat with those people.

**1:06:08** · Yeah.

**1:06:08** · Like talk to your crazy token users.

**1:06:11** · Talk to the people who are around that 100, 200 dollar subscription level and they're starting to hit that cap.

**1:06:16** · Right.

**1:06:16** · And then look at the people who are like bopping in once a month.

**1:06:20** · Right.

**1:06:20** · And I want to talk to all three to start to get insights on why one is over here, why one's over here.

**1:06:24** · I even would want to know, and I would imagine this is the case that, you know, if someone is watching this and they say, "Well, I really only use ChatGPT for personal stuff."

**1:06:32** · Yeah.

**1:06:32** · even using it at work. I would be, you know, again, if infinite time, I'd say, "Well, how are you using it?" Because maybe they've, without realizing it, just like at the opening of this conversation, I described what I was using and you're like, "Well, you've done this, this, this." I'm like, "Oh."

**1:06:43** · Like maybe there's someone at home who's doing something with ChatGPT to summarize family recipes and turn them into a thing that no one ever thought of. So even the little ones could be very helpful.

**1:06:52** · share that.

**1:06:52** · This is also going back to headlines, AI washing, and having crazy hyperbolized headlines. But did you see the the news about the Pope? The big, like, okay.

**1:07:03** · So all the headlines, at at that I read, before I actually read the thing, all the headlines were like, "The Pope hates AI."

**1:07:08** · Yeah. And then I read this thing and I go, "Wait a second. He's just talking about how we want to make sure that this technological revolution benefits all."

**1:07:16** · Right.

**1:07:17** · And that a lot of enterprises again that I meet with or randomly, they're often prioritizing even in output land the wrong metric.

**1:07:25** · Mhm.

**1:07:26** · Like they're looking at how many PRs someone is closing or whatever or they're looking at how many blog posts someone writes. That's still output.

**1:07:34** · Right.

**1:07:35** · Is it good?

**1:07:36** · Right.

**1:07:37** · Is the conversion going up? Do we have happier customers?

**1:07:41** · Right.

**1:07:41** · Are we I don't know, is our revenue going up? Like is our risk rate going down? I want people to not just look at business success metrics. I want people to look at like morale Yes.

**1:07:53** · and and impact and fulfillment metrics.

**1:07:57** · Yes.

**1:07:58** · And if I maybe if I'm talking to all levels of token users, we start to get that. But I used to have a slide in my keynote that talked about people process product. So the three parts of an AI first business. And the description of people used to be about productivity and about getting, you know, repetitive digital tasks, manual tasks, whatever off your plate. And it was really productivity focused. And a couple years ago I was like, "Oh, productivity's a trap."

**1:08:26** · Mhm.

**1:08:27** · Like productivity is the story we're all going to hear nonstop from every single company and every single shareholder call. That is going to be how stocks go up and down. That is going to be how budget decisions are made. That is going to be what is lauded in public. And guess what? Productivity is one of the dumbest metrics to be focused on because you're going to miss the growth, the impact, the fulfillment, the empowerment that you could Yes.

**1:08:50** · get from AI if you only tried.

**1:08:51** · Yes. This is where I always think of the example if anyone watching is a Are you a Mad Men fan from back in the day?

**1:08:57** · Um I watched I think the first season, but I also just watched listened to Jon Hamm on Amy Poehler's Good Hang.

**1:09:03** · He's so great. Okay. Well, HE'S HERE NOW, NO?

**1:09:06** · \[laughter\] HE'S HIS WHOLE THING IS THAT HE'S IN THIS advertising agency and he's kind of a you know, he's he's not pulling his weight. He comes in drunk and he lies on the couch all day long, but every couple of weeks he walks up and he says, "I've got it." And he writes down a thing that lands the next amazing client, right?

**1:09:22** · Whereas everyone else who's super productive, quote unquote, is putting out, you know, storyboards and they're putting out slogans and they're doing all of this. And so I always think of that when I think about whether we're using AI or some other tool. It's like productivity is not just a volume game.

**1:09:36** · And you've got to make sure that you're incentivizing and recognizing the people who maybe most of the time look like they're not doing much. But if you had someone on your team who or an agent or a team of agents who every quarter came up with just the most brilliant way of thinking about something, that's so much more valuable than six people who can type the do the AI equivalent of type thousands and thousands of words.

**1:09:56** · And if they were a jerk the whole time, I still don't want them.

**1:09:59** · Well, of course.

**1:09:59** · \[laughter\] Of course. Also, Jon Hamm shared that in the pilot episode of Mad Men, they counted how many cigarettes he smoked.

**1:10:07** · Oh god.

**1:10:08** · Any guess?

**1:10:09** · 100?

**1:10:10** · You're so close. 80.

**1:10:12** · I thought you were going to guess like 15.

**1:10:13** · No.

**1:10:14** · Oh, you're so good at data.

**1:10:15** · Well, you know, that's the good I actually specialize in cigarette data \[laughter\] from television from 2010. Yeah. So, that's uh you really got in my sweet spot there.

### Chiny, pojazdy elektryczne i środowisko

**1:10:24** · I want to also touch on China and environment. And you have such a fascinating take on AI in both China and the US because how long did you live in China for?

**1:10:35** · I lived in China for 3 years um between 2013 and 16, but I also spent, you know, a bunch of time there before that and a bunch of time there since, but that was when I was there.

**1:10:43** · And you continue to visit and you speak Chinese and you go back and you have friends that Okay. So, talk to me a little bit just like give me your view.

**1:10:51** · And I And I mean this in like a general sense. Like just one interesting stat, Open Router, which is one of the more common like model marketplaces, just reported that 60% of their token usage on the platform is run through these open source models that are coming from China. So, it's things like Deep Seek, which I think every single person's heard of, but it's also like Quan and MiniMax. And just give me a little bit of a sense cuz this has really big implications on open source, on who is leading in the model race, on token maxing.

**1:11:22** · Give me your view.

**1:11:24** · This is going to be a very broad view.

**1:11:27** · Even pre-AI, pre-the last 5 years, I think that we have dismissed, we the general American public and maybe the American legacy media, have dismissed China as still this backwater developing country. Now, China is a massive country. There are many areas where people are very impoverished and there's barely running water and all of these things. And they are living in a much more, I would say, futuristic world than we are.

**1:11:54** · So, even when 2013, 2016, when I was there, in the United States, we weren't paying for things with our phones even. We weren't using, you know, a lot of social media beyond just kind of posting things. And I would go walk around and see, you know, ancient old people, 90 years old, pay for their dumplings by scanning their phone. And I was like, this is the future, right? And so, I think the fact that we continue to be surprised, when Deep Seek came out and this comes out, we every time Americans are like, what? China's doing something?

**1:12:26** · We for so long, and and for much of our our, you know, relative histories in in recent decades, this has been somewhat true, where we say, oh, China is there to be a couple decades behind us. They're going to do all the ugly manufacturing. They're going to make the iPhones or they're going to copy our Apple stores and they're not really being innovative.

**1:12:43** · I think that we have thought that for a long time and we've been wrong for decades, but we're seeing it even more now with AI, which is really in some ways, good because it's not like, oh, China was was doing nothing and then all of a sudden they caught up. They've been very advanced for a very long time. They have much better, you know, trains and and bullet You know, we think about Japan and bullet trains. China has bullet trains.

**1:13:06** · Like, we just we've been so dismissive culturally and politically that that's part of why we keep getting shocked. And so, I think that in general, I would encourage anyone when they think about technology coming out of China, think about EVs. When we think about innovation coming from China, assume they're on the cutting edge because they really are.

**1:13:23** · And, you know, there's a lot of conversations and I could talk about this for a long time about regulation of AI in the US and well, we can't do that because China's not regulating and are we in this kind of arms race cold war of AI and we are if we think that we are, but it's also a wonderful way for these two countries to cooperate is to say, "Hey, Do you think that'll happen?"

**1:13:45** · I'm hopeful. I'm kind of living as though it will happen in the hopes that I create a self-fulfilling prophecy, one hopeful opti- cockeyed optimist at a time.

**1:13:56** · \[laughter\] I think it's possible. I don't think it's a foregone conclusion. I think at the moment it's unlikely, but I think that our it's early enough on and this is really personal speculation, right?

**1:14:07** · It's early enough on in the process that I think that the right companies, I don't see it being government-led at the moment, the right companies who say, "Hey, I'm just trying to use AI in the most thoughtful, innovative, incredible way to cure diseases, to solve this problem, to reduce greenhouse gases, whatever it is, and be agnostic or be open to doing it in different countries, just like you're open to running manufacturing in in Mexico or Southeast Asia or whatever." So, I think there's a version of the world where we could have more interdependencies that foster cooperation between the two countries.

**1:14:40** · But, what I'm also hearing is only if it makes sense in the incentive structure.

**1:14:45** · Yes.

**1:14:46** · Which like Which is that where countries trying to aim for sovereign AI and trying to influence a lot of the rest of the world.

**1:14:53** · Right.

**1:14:54** · Working together is not quite aligned to those incentives.

**1:14:57** · it's an arms race if we all think it's an arms race.

**1:15:00** · Yeah.

**1:15:00** · But at the company level or even at the non-profit like you work with non-profits too. The ability to have a scientific research group here working with a university in China whatever the thing is.

**1:15:09** · Right.

**1:15:10** · That there's I mean we see those that collaboration now. Like you look at any ML research paper there's already collaborations.

**1:15:15** · Right.

**1:15:15** · Right. So there are pockets. Of course there's massive issues with you know the government and the government's relationship with Google and all of these sorts of things. Like there's very real barriers and I don't want to be Pollyannaish about it but I do think that it's not set in stone that we couldn't see more of that kind of collaborate. And maybe the side the world of science is where we'll see more of it. Maybe because we see less investment in science in the United States we're going to see more American scientists going to places like China to work on on some problems that we don't have the funding for say.

**1:15:41** · Out of curiosity in in your recent trips to China, what is today's version of paying by phone? Like what is the thing where you're like I can't believe the US doesn't have this. I know electric vehicles anytime I talk to someone that just came back from China EVs are the number one thing that they say. Like China's able to create an EV I think it's once every 56 seconds. Is that the 56 or 26? I'll have to look it up but Yeah.

**1:16:03** · it is an insane manufacturing powerhouse.

**1:16:07** · And renewable energy. Like that is Oh, if I if I had one magic wand wish I would want way more renewable energy sources in the US and for all the people who are thinking about the environment and we I want to talk about that too and hear your thoughts on that. Like one of the greatest things two of the greatest things I think that you can push for in the environment space. One would be regulation so that in areas that are getting brand new data centers that there are certain quality checks of water quality, air quality.

**1:16:37** · That is definitely one area that I'd be pushing for. And the second is more renewable energy. The fact that we're reducing investment in renewable energy as a country is very concerning to me.

**1:16:49** · So, this is a perfect segue. Uh applause all around from the future and China to exactly this topic, which is what I was going to say is that something that when I look around China now is air pollution was a massive problem when I lived there full-time. Like it was you would leave the house and you would check the AQI, the air quality index, before you would check the temperature or whether it was going to rain or anything like that. And I had N95 masks way before they were cool and then extremely uncool and then politically charged and all of this I mean it's I had them a long time ago.

**1:17:20** · And uh and I mean there were days you couldn't even see your hand. I mean these were extreme days, but really rough air pollution. And to the point where anything I've ever seen in the US is this is a sneeze. It's like a slightly off slightly overcast day compared to that. It's basically not an issue. And I'm not an environmental engineer and I can't speak to exactly what happened and as a lot of, you know, authoritarian governments are able to kind of get things done in a way that democratic governments, you know, there's trade-offs everywhere, but this is one area where they've really it's just really in the major cities, not the kind of issue that it used to be.

**1:17:49** · So, these are problems that are big, they affect a lot of people, they're unwieldy, they require collective action, they require coordination, and they are solvable. And so, I get excited when I see China solving things like that. Of course, you always want to think about trade-offs and people watching are like, "The human rights." You know, this I'm not saying this is perfect, but I'm saying this is a problem that has been really meaningfully improved at a very massive scale.

**1:18:15** · My hope is that we get so jealous of their climate work and renewable energy work that that spurs us more into action. And you're reminding me by the way, this is I think more than 10 years ago. \[laughter\] Um or no, about yeah, about 10 years ago I was uh working at a large AI company and there was something called a cognitive nose that literally Can you Do you picture You know the movie Richie Rich?

**1:18:42** · Where there's like the like the robot nose?

**1:18:47** · So you're thinking of Blank Check.

**1:18:48** · Yeah, okay. \[laughter\] Okay, they There's a scientist like living in the basement who's just doing interesting experiments and he has like a little bee and he has a nose that can smell things and whatever. So that you can smell food and be like, "Oop, there's peanuts. You're going to die. Don't eat that."

**1:19:02** · Okay. So at the time, 10 years ago, and again, I haven't seen any AI nose come out for like scent detection, but that technology has existed for at least 10 years.

**1:19:14** · Yeah.

**1:19:14** · And the big use case that they were saying was not food detection, although food security was definitely one of them. It was air pollution and Beijing was like one of the leading cities saying, "We care about this." This was 10 years ago.

**1:19:29** · Yeah.

**1:19:29** · No, and this is one of those things too where it's one of the one of the more humbling pieces of information I learned 10 years ago or so when I was like, "Why can't they solve this problem?" is that one issue is it's actually very It's non-trivial to measure air pollution in different places because unlike the weather where it's like if it's 60° in Midtown, it's probably 60° downtown. Air pollution doesn't travel like that and so you really You could have a you know a meter in the middle of the city and it's totally fine, but three other pockets. And so it actually was a was a serious technological challenge to even understand the nature of the problem.

**1:20:01** · Where is the air pollution worse? What's causing it to be worse?

**1:20:04** · Where is it going up and down? Where are we pretty much fine? What can we learn from that? Just getting those sensors in place, never mind coming up with a solution, was a huge issue.

### Czujniki, problemy z pomiarem i umiejętności ludzkie

**1:20:13** · You're tying back to So I want I want to wrap on two things. One is just like enterprise advice for the world that we're walking into for the rest of 2026 and beyond. And the other is just like humanness.

**1:20:25** · And I don't mean like humanity, like what is going to be for all of us. I mean more like human skills and what should we each be focused on? So, the word sensor is so interesting because when I'm talking to these clients and at conferences and to boards about a self-learning org or about an autonomous enterprise, a lot of what I'm describing is this sort of flywheel or Satya Nadella calls it like a hill-climbing machine. Um I call it like building out that open machine to build out that flywheel.

**1:20:55** · Anyways, a lot of where it starts with, you're going to see the word sensors popping up everywhere. Just as like info gathering and I think this ties back to so many other points we were making like token maxing. Okay, that is one signal, that is one sensor that we have set up in our org. What are others? Or inside of that meeting, we have AI kind of functioning as a sensor in that sensor like S E N S O R. Or It's not telling you to stop talking about certain \[laughter\] topics.

**1:21:23** · Or or the AI as a watchdog. It is sensing and so I just I get this sense \[laughter\] Put me on stage. Okay, I get the sense that like AI as a sensor understanding, whether it's air pollution or token maxing or interesting conversations or duplicative work. I there's such a big interesting space.

**1:21:46** · So like now assuming that you believe that this recursive learning and all the reinforcement learning work that you're talking about, assuming that we're setting up a world where a team and org or person can set a what is good goal point and do a whole bunch of experiments to be able to get that reward.

**1:22:09** · What advice are you giving to businesses now?

**1:22:11** · Well, I think you've tapped into I'm so excited about everything you just said about sensors. I don't know how to say it without making it sound like we're forbidding free speech. The the using AI and using technology to get more of what

**1:22:28** · we can call just observational data of the world is a massive massive opportunity that I think almost no one is thinking about apart from maybe you and a handful of other people which is to say we have all these ideas about you know you go to the doctor's office and they say we take your pulse we're going to take your heart rate we're going to take your blood pressure and your temperature and then that's kind of it.

**1:22:48** · What if there were 200 things that you could take or you see it a little bit with like older people like you Fitbit you can get a sense if your gait is a little bit off or like get get warning signs if your heart rate has been a little bit off you know what is the version of that for the

**1:23:04** · rest of our lives right even if it's something as silly as you know every time I go to leave the house it takes me this is true it takes me from the moment I say I'm ready to go it still takes me five to seven minutes to be like well where are my keys and what is my this and what are even though I think I put them in the same place and then I'm like ah I forgot to switch to the laundry and so if there were enough sensors around I could be like Andrea just get your keys and your wallet and always go in that order or whatever right Yeah.

**1:23:26** · And I don't want to make a picture of like oh we're just sounding in a world where it's like the Jetsons and we're optimizing everything and you never have to do anything in your life.

**1:23:32** · Yeah.

**1:23:32** · It's much more about if we want to solve any problem that matters to us whether it's are my employees happy are my customers going to tell their friends about me am I going to make it a future that my kids are excited to live in at scale health yeah.

**1:23:46** · Yeah.

**1:23:46** · You need to be able to understand the problem that you're dealing with and I can make it here's a very very concrete if depressing example is I was recently humbled as well when I was speaking with someone about I care a lot about a disease called ALS Lou Gehrig's disease and uh it's a disease where people lose the ability to move uh and they they usually die within 3 to 5 years of diagnosis. I was speaking with researchers about how they use AI and data to come up with cures for this disease there are no cures.

**1:24:14** · And they said well of course we use data for those things but one of the problems with ALS is we don't even have good measures for how it's progressing. So, we can't even really tell if the treatments are working because we don't know we don't have enough numbers around what what what does it look like? Is it your fingers are twitching? Is it they stop moving? Is it your grip strength goes down? Is it your ability to walk goes down? Is it your ability your speech is starting We don't have the numbers for that. So, until we can measure what we would call the dependent variable, we don't know anything about what would work to improve it.

**1:24:45** · So, if I say, "I want to be happier. I want to be healthier." Until we have numbers for what those things mean, we're just shooting in the dark and trying the light latest thing we saw on TikTok. So, my advice to anybody thinking about a a place where we could use AI thoughtfully and creatively to actually fix the world that we're in is use it to better measure the things we already want to fix to make sure we're actually fixing the right problems or fixing problems that we are actually fully understanding correctly.

**1:25:14** · You've also you've given so many other pieces of advice I'm going to try and call out a few, but like one was starting with the problem Yep.

**1:25:21** · and not starting with the tech Yep.

**1:25:22** · and also not flying into whatever you just saw on TikTok.

**1:25:25** · Mhm.

**1:25:25** · Um second is that you you and I both agree that urgency is poison and that the ability to take a beat, bring in AI as a teammate in part of that can be really helpful.

**1:25:37** · Um not underestimating people in general. You talked about not underestimating China and not underestimating the introvert in the corner who every single month has the most brilliant idea and really helps move the team forward.

**1:25:50** · So, there's a lot of advice that you you've shared and I really appreciate it. Um two things that I'd be focused on it sounds like we honestly agree. The first is really building up that context layer and making sure you're doing it in like a safe way and not a surveillance way, but making sure you're doing things like recording meetings.

**1:26:06** · I even have one exact that I coach every single day at the end of her day she records a 5 to 40-minute voice memo and just stores it in her notes app and it's the ability to say, wait a second, I've now kept track of all of my thoughts, decisions, fears, worries, strengths, ideas over the last multiple months. And now I'm going to run all of those notes through Claude code or Codex to be able to say, okay, now map out where we're headed in the next 6 months.

**1:26:37** · What habit do I have to kick? Where am I still having blind spots? Am I hitting my goals? Whatever the things are. So building up the context layer for sure. The second, which you just touched on, and I'll I'll use the jargon word, which is evals, it's just like knowing what is good.

**1:26:53** · Right.

**1:26:54** · And trying to do more of? How do we know we're doing it?

**1:26:57** · That's the big So at Amazon, there was a guy, I'm not going to say him by name, and I love this man. But every single time someone would be like, well, we increased whatever by 15% or like, well, we got 40 new startups, whatever.

**1:27:10** · Yeah.

**1:27:10** · He would always unmute and he would go, I don't care about the number, I care whether the number is good.

**1:27:17** · That's it.

**1:27:17** · And it was like of it.

**1:27:19** · Uh, I say that all the time on my team. But it's I I need it in context. I need it based, you know, compared to other companies. I need it benchmarked against the industry. If every single company in our space is plummeting because, you know, fuel prices are going up and so every single person is losing their their margins and yet we've been able to maintain. Right.

**1:27:41** · Or it's only went down a tiny bit or whatever. Yeah.

**1:27:44** · Exactly.

**1:27:44** · It could be It could be negative and still be unbelievable. Okay. So evals and context are the two things that I would definitely be focused on and making sure that you have those A players as you can hopefully find Mhm.

**1:27:58** · doing that work. And that might mean the introvert or that might mean the loud person. Um, I want to add just one one last thought. Um, you're someone who is so data driven, PhD, you've worked with hundreds, probably thousands of students, you are so numbers. And yet, you are one of the most people-oriented data leaders that I know. What are you thinking right now about just like human skills? When when students, when Gen Xers and everyone in between, when they're coming up to you saying, "How do I survive in the AI age?"

**1:28:28** · What do you tell them?

**1:28:31** · I go straight to the same thing I've really been saying this whole time, which is yes, the tools are getting better and better, and yes, they're changing hour to hour. By the time this conversation's over, there's going to be something new that we both need to catch up on. But, I think we will never ever run out of Let me rephrase that. I think we will always need critical thinking, creativity, imagination, curiosity. And if I had to pick one of those four, I would say probably curiosity.

**1:29:01** · You need some critical thinking afterwards, but start with curiosity. If you're not stopping and saying, kind of to your point, if you're not stopping saying, "What am I actually trying to do here? What am I actually trying to find out? Why do I actually think this is a problem? Why do I think this is the most important problem? Why do I think that this has to get better instead of stay the same or whatever it is?" If we're not leading with curiosity, we're just going to very efficiently dig ourselves into some random hole that isn't very important.

**1:29:29** · And so, as much as I am impressed by the things that AI can do and that, you know, using a a, you know, agents and and all kinds of amazing things and and really being awed by the capacity, at the end of the day, and maybe in 5 years someone will point out that we don't need this anymore, I still believe that we need the human to say, "Hey, this is how the world is.

**1:29:50** · But, what if it could be that way? Or why wouldn't it be that way?" You you need that forward-looking curiosity, and then you need that critical thinking to say, "This is how I'm going to figure it out. This is how I know my solution is actually getting towards the change that I want. This is how I know I'm not just leaning to my own bias. I've actually checked with other people and we agree this is a good goal. I think that the human the curious and critical human steering the ship will never go out of style no matter how many amazing tools we have.

**1:30:18** · It's also that's brilliant brilliant point and if we believe that teams are getting smaller and that individuals are getting more capable then your ability to build on your curiosity and take action, your ability to have creativity in that, your ability to imagine a better world and build toward that news all these resources it actually just became more important Right. to double down on all those skills.

**1:30:38** · I kind of think of it as and this goes back to where we started this conversation with the first time I used an LLM to help me with some coding. I thought oh this isn't dampening my critic critical thinking and creativity.

**1:30:48** · This is helping me do more of it cuz I'm spending less time in the weeds. It's kind of like okay we used to walk everywhere. Then we figured out wheels and then we had bikes. Then we had horses. Now we have cars and planes but we still decide where we're going, why we're going there, what route we take to get there and what happens once we get there. And so no matter how and that doesn't mean that we always take the fastest plane or I got here via horse.

**1:31:10** · Yeah. I I uh I was dragged here against my will but \[laughter\] but I did GET HERE NONETHELESS. YEAH IT doesn't mean you need the fastest every single time.

**1:31:19** · Yeah. I love that. Critical thinking in the age of AI.

**1:31:22** · There you go.

**1:31:22** · Okay.

**1:31:22** · Thank you so much for being here Dr. Andrea Jones Roy and where can people follow you? Where can people You can find me on the internet at jonesroy j o n e s r o o y. It's on the social media's YouTube jonesroy.com all the things.

**1:31:36** · I love it.

**1:31:37** · the most confusing name and decided to just lean into it.

**1:31:40** · \[laughter\] Well thank you.

**1:31:41** · Yeah thank you.