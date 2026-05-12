---
type: "Web"
authors: "[[How I AI]]"
url: "https://www.youtube.com/watch?v=ZKnASs_d7aE"
published: 2026-01-05
created: 2026-05-12
tags:
---


![](https://www.youtube.com/watch?v=ZKnASs_d7aE)

Wade Foster is the co-founder and CEO of Zapier. In this episode, Wade shows how he uses meeting transcripts, Zapier agents, and even Grok to analyze company culture, evaluate interview candidates, and source talent from unexpected places. He explains why CEOs need to lead by example when it comes to AI adoption and shares practical workflows that any executive can implement to make hiring more effective and efficient.  
  
\*What you’ll learn:\*  
1\. How to use meeting transcripts to extract your company’s “unspoken culture” and compare it against your stated values  
2\. A workflow for creating AI interview evaluators that assess candidates against your job descriptions and company values  
3\. How to use Zapier agents to provide objective feedback on candidate interviews while checking your own biases  
4\. Why CEOs should participate in AI “hackathons” and “show and tells” rather than just delegating AI adoption  
5\. A surprising technique for using Grok to find “diamonds in the rough” talent outside traditional recruiting channels  
6\. How AI enables companies to complete tasks that were previously not economically viable  
  
\*This entire episode is brought to you by:\*  
Brex—The intelligent finance platform built for founders: https://brex.com/howiai  
  
\*In this episode, we cover:\*  
(00:00) Introduction to Wade Foster  
(02:32) Zapier’s AI adoption  
(06:50) Creating AI fluency rubrics  
(08:37) Using Granola to extract company culture from meeting transcripts  
(10:49) Practical use cases for company culture rubrics  
(13:38) Building an AI interview evaluation agent in Zapier  
(16:50) Using Copilot to improve agent prompts  
(18:49) Ideas for enhancing the interview agent  
(22:31) Mistakes people make when using agents  
(25:11) Using Grok to find talent on social media platforms  
(33:39) Recap of AI workflows for recruiting and hiring  
(34:40) Lightning round and final thoughts  
  
\*Tools referenced:\*  
• Zapier: https://zapier.com/  
• Zapier Agents: https://zapier.com/agents  
• Granola: https://granola.ai/  
• Grok: https://grok.x.ai/  
• ChatGPT: https://chat.openai.com/  
• Copilot: https://copilot.microsoft.com/  
  
\*Other references:\*  
• Zapier values: https://zapier.com/about  
• How Zapier’s EA built an army of AI interns to automate meeting prep, strengthen team culture, and scale internal alignment | Cortney Hickey: https://www.lennysnewsletter.com/p/how-zapiers-ea-built-an-army-of-ai  
• How this CEO turned 25,000 hours of sales calls into a self-learning go-to-market engine | Matt Britton (Suzy): https://www.lennysnewsletter.com/p/how-this-ceo-turned-25000-hours-of  
  
\*Where to find Wade Foster:\*  
Zapier: https://zapier.com/  
LinkedIn: https://www.linkedin.com/in/wadefoster/  
X: https://twitter.com/wadefoster  
  
\*Where to find Claire Vo:\*  
ChatPRD: https://www.chatprd.ai/  
Website: https://clairevo.com/  
LinkedIn: https://www.linkedin.com/in/clairevo/  
X: https://x.com/clairevo  
  
\_Production and marketing by https://penname.co/.\_  
\_For inquiries about sponsoring the podcast, email jordan@penname.co.\_

## Transcript

### Wprowadzenie do Wade'a Fostera

**0:00** · So many CEOs sending these memos. We want you to do 10 times more work using these magical tools. You go figure it out.

**0:07** · I see a lot of CEOs fall to the delegation trap. They write the AI memo.

**0:11** · They say, "Hey, we're going to go do this." And then they don't do anything else. They ask their exec team, who ask a director on their team, who ask a manager on their team, who ask an IC on the team, and then that poor IC is like, "Am I figuring this out for the whole company?" It's like, "Do you think that's going to go well for that person or for your or no, not really." And so I think it's really important for leaders to do hackathons, to do showand tells, whatever you want to call them, whatever you want to do, but you do need to provide a little bit of play space for the organization to get comfortable with it. And then once people put their hands on the tools, I find that some of the fear goes away.

**0:42** · You've actually put these rubrics together that allow you to identify how do you build AI fluency as a PM at these different levels. And I think that exercise is so effective because people change around what gets rewarded and what gets measured.

**0:57** · There is so many tasks that are not economically valuable right now. And these are the areas where AI and agents really thrive. Welcome back to How I AI. I'm Claire, product leader and AI obsessive here on a mission to help you build better with these new tools. Today we have a very special episode with Wade Foster, co-founder \[music\] and CEO of Zapier.

**1:22** · Wade's going to show us how CEOs can do more than send emails \[music\] to their teams about how they should adopt AI. Instead, he's going to pop open his screen and show us how he uses meeting notes, Zapier, and believe it or not, Grock to find, hire, and inspire talent across the company. Let's get to it. This episode is brought to you by Brex.

**1:44** · \[music\] If you're listening to this show, you already know AI is changing how we work in real practical \[music\] ways. Brex is bringing that same power to finance. BR is \[music\] the intelligent finance platform built for founders. With autonomous agents running in the background, your finance \[music\] stack basically runs itself. Cards are issued, expenses are filed, and fraud is stopped in real time without you having to think about it.

**2:11** · \[music\] Add Brex's banking solution with a high yield treasury account and you've got a system that helps you spend smarter, move faster, and scale with confidence. One in three startups in the \[music\] US already runs on Brex. You can too at bre.com/howi AI. Wade, thanks for joining how I AI.

### Wdrażanie AI w Zapier

**2:36** · Why I am so excited to have you here is I think Zapier has done one of the most exceptional jobs. Not just leaning into adding AI into their product, but really thinking about how AI transforms a company and how people do work there.

**2:54** · And today we have a really exciting show where we're going to show how you think about AI talent, AI fluency, interviewing for AI, and even finding some um AI pill talent out there that you can pull into the org. So before we get into it, why have you leaned in so hard into changing how your team works, who you hire, and what you reward inside the company?

**3:19** · Couple reasons, I think. one for the same reason that everybody's doing it, which it feels like this is a transformative technology that allows us to ship and deliver just like a whole bunch more value to our customers. So that's first and foremost. Second, our product does a lot of this stuff and I would be embarrassed if we're out there evangelizing how this stuff can change how you work and internally we're doing none of it.

**3:49** · And so when I talk to our team, I'm like, I want us to be on the forefront of using this stuff. And that should mean that we're going to try things and we're going to make mistakes.

**4:02** · But even when we make mistakes, that's really good because we can now go out and share those mistakes and say, "Hey, we tried this thing that everybody was, you know, talking was so great and, you know, either it was great for us or actually it didn't really work for us, like we couldn't figure it out." And I think that has helped people feel a little bit more comfortable, you know, just pushing on these things.

**4:24** · It also helps that one of our core values is don't be a robot, build a robot. So like we're just we're probably just like more predisposed uh compared to most companies to to get into these things.

**4:33** · Well, and one of the things that I hear a lot from people is they get a lot of anxiety sometimes when they're hearing these messages from their leaders about how they need to change how they do work or how they think about their job. and they say, "I'm so busy. I don't have time or I just don't know where to get started. It doesn't practically apply."

**4:52** · And where I've been able to crack kind of people is I think you are doing your teammates a huge service by investing in them getting these skills because every challenge the challenge I give to most people is I say okay let's say you've had a wonderful run at whatever company you're at and I know you're going to be here forever but maybe in a couple years you decide you're up for a new adventure. What do you think that interview is going to look like? What do you think they're going to scream for in two or three years? and do you think this is going to be part of how you're evaluated?

**5:23** · And they almost consistently say absolutely yes. And then I say then you're very lucky to be at a company who wants you to be on the leading edge in terms of adopting these tools and technologies and processes in your work. So I think it's um not only the right thing to do for a business, but I actually think it's the right thing to do for employees and people as part of a team.

**5:44** · I 100% agree. I see a lot of CEOs fall to like the delegation trap. They write the AI memo. They say, "Hey, we're going to go do this." And then they don't do anything else. They they ask their exec team, who asks a director on their team, who ask a manager on their team, who ask an IC on the team. And then that poor IC is like, "Am I figuring this out for the whole company?" It's like, "Do you think that's going to go well for that person or for your org?" And it's like, "No, not really."

**6:07** · And so I think it's really important for leaders to do hackathons, to do showand tells, to do Friday afternoon, you know, mess around, whatever you want to call them, whatever you want to do. But you do need to provide a little bit of play space for the organization to get comfortable with it. And then once people put their hands on the tools, I find that some of the fear goes away. It's so natural because the media would have you believe that this stuff is terrifying. But for those of us who are messing around with it, you see how awesome it is, but you also see the flaws.

**6:38** · You're like, "Oh, it's not so good at this. It's really good at this. I'm going to lean into it over here, and then my role is actually doing these other tasks now." And so it becomes a lot more pragmatic versus this like boogeyman in the closet that's going to come for your job.

### Tworzenie AI Rubryki oceny płynności

**6:51** · I agree. And then the last thing I'll give you a little kudos on is you've made this very tangible for your team.

**6:57** · So we have a lot of for example product managers in the how AI audience and you've actually put these rubrics together that allow you to identify how do you build AI fluency as a PM at these different levels. And I think that exercise is so effective because people chain around what gets rewarded and what gets measured. And by making it very specific, people can invest in specific skills and tools and know where, you know, the goalposts are. And so you've actually used AI to both like make those and make them better.

**7:27** · And I think that's where we're going to start with our first workflow.

**7:31** · So the first thing I want to show, we're going to talk about recruiting day. I spent a lot of time on recruiting. I've got this dock here which is you know probably most of your companies have like something like this which is you know like a values um document. Um most of them I don't think put like a ton of effort into it but I think it's really helpful when you start to have a document that's like written well for an AI to understand like what is good and bad behavior. I think you actually had an episode with um Hillary doing yeah Hillary like man that did a version of this where it was like you know uh default action. Okay.

**8:02** · But what does that actually mean? Like here's examples of do this, not this. And it helps the AI sort of get really good at these types of things. So we had a document like this for forever that helps us with our rubrics. And so when you think about hiring somebody, you want to have clear evaluation criteria.

**8:23** · Now, this we put together long long ago, but I have a hack for how you can do this even if you haven't thought about this. Um, and so the hack that I have for this one is if you use Granola, Granola launched this feature called recipes, which are just fancy prompts basically.

### Wykorzystanie Granoli do wyodrębniania kultury firmy z transkrypcji spotkań

**8:47** · And I did not think of this idea. This is something that was just in their library, which was genius. I've been using Granola for I don't most of the year, I think, almost a year now. And one of the prompts they have is, yeah, build the unspoken company culture. uh handbook. So you can see it actually starts to say how the organization works at least according to my meetings and I have it on in every single meeting so people really know at least how Wade works and the meetings in and around Wade works.

**9:15** · Um and you get this like pretty rich example of what your company's doing.

**9:23** · And so if you're using a tool like Granola, if you're using any of these meeting recorders, I think you can run a prompt like this to actually extract the real culture of the company. Uh, and so you can see what it rewards, you can see what it doesn't reward. Um, and it it it the first time I ran this, I was like I I was shocked. I was like, we spend a lot of time thinking about our culture, writing about our culture, and I think we do a better job than most.

**9:48** · But as I read through it, I was like, "Wow, this actually gets at the specifics in a way that even I hadn't figured out quite how to do." And so, I think this is kind of the magic of AI, especially if you're using a tool like Granola or something to collect data over long periods of time. Then AI gets really powerful because you can just like slap a prompt on the top of it and it can generate something like this that now becomes really practical for a whole host of reasons.

**10:20** · You can now put it into job descriptions. You can now use it as part of hiring and firing. You can set expectations really well. So this is a tool I would use. I I would take the output of this now and I would go give it to a tool like chat GPT and say hey can you take this like unspoken culture and actually generate a set of like scoring prompts for how to

**10:45** · evaluate somebody in an interview against these traits that um match zappier well and what I want to call out for the CEOs or other executives here are is you know a lot of CEOs talk about culture and our operating principles and how you know who we want to hire for and how we want to hire. But you do have this rich unstructured data. Most of us do just bunch of granola which is how your team actually speaks to each other and operates in the day-to-day and taking this this data and not using it for functional purposes.

### Praktyczne przypadki użycia rubryk kultury firmy

**11:17** · Although we've seen lots of functional purposes of this, taking sales calls and giving salespeople coaching, you know, taking product, you know, debates and turning them to documents, but actually taking the aggregate of all your company communications and stress testing it against your stated values is really interesting because then you can see well where are we aligned with our values?

**11:38** · Where do things show up that we haven't actually clearly articulated that we want to reinforce and document and do all these things and like where are we actually off like we say we XYZ but then if we really look at how we speak to each other we do a lot of ABC and I just think so many CEOs again are

**11:59** · like sending these memos like we want you to do 10 times more work using these magical tools um you go figure it out but aren't spending the time to figure out how to maybe even do the CEO job better. And I'm sure you think of yourself as the carrier of culture at your company. And so why not use these tools that weren't available before to do that?

**12:21** · And then and then you can use, you know, AI to turn these into all sorts of assets as you said, job descriptions, um, performance rubrics, all hands content, all that kind of stuff that I think is really interesting. And we have, not to spoil it, we have an episode coming either before or after. We'll see when it gets scheduled with your EA Courtney who holds your executive team's feet to the fire on how they perform in meetings relative to your uh values. So it's not just about, you know, eye of Sauron from across the organization.

**12:52** · You do turn it upon yourself as well.

**12:58** · Yeah.

**12:58** · I think so. So, I think what you're talking about is we have uh like coaching bots in a lot of meetings and stuff like this and I I love it honestly because I I as a CEO I want to get lots of feedback because of power dynamics and stuff. You don't always get like just the honest truth and AI is this infinitely patient coach and so it's just fantastic and be like hey here's some things I think you're doing great good job and like here's three things that candidly you're not doing a great job of you know you don't always have to agree with it but it's really helpful at just making me better at my job. Uh, and I think most people want that.

**13:28** · Like most people want more feedback than your their their manager or their peers or whoever have time to give them. And AI has all the time in the world to give you feedback.

### Tworzenie agenta AI do oceny rozmów kwalifikacyjnych w Zapier

**13:39** · Okay.

**13:39** · So you have your um values document. You shown us how we could create maybe or infer some values from some sources of data that weren't available before. But then let's talk a little bit about hiring. So again, CEO job, carry carry values, culture, you know, drive pace in the organization, hire great people. So you spent a lot of time on hiring and how has AI come into how you manage some parts of the hiring process that were maybe a little bit more tedious or um harder to scale before?

**14:13** · One of the places that I really like to use it is as like an assistant for interviews. So uh I again I use granola a lot. Um so I have built an agent that will help will will basically evaluate my transcripts and my notes and will help me make a yes no decision on how to hire this person. So what we're looking at here is Zapier agents. This is a pretty simple agent here. So you can see over here it triggers when there's a note added to a folder in granola.

**14:45** · In this case if we look in it it's a interview agent. whenever it adds uh an interview to my new interviews um folder. And the way Zap year agents work is you can give them a set of instructions to follow. And so in this case, you know, the instructions are you're an expert hiring evaluator at Zapier. Your task is to review the interview transcript and notes provided by Granola. You're reviewing the job description provided at the knowledge source and Zapier's company values provided as a knowledge source to determine whether a candidate should advance in the hiring process.

**15:16** · You want to evaluate the candidates's functional expertise, their values alignment, so on and so forth. So you run through all the things that you want this agent to do and then ultimately I give it a goal.

**15:27** · And the goal here is, hey, I want you to recommend yes, no, or maybe to this candidate, and then I want you to provide your reasoning. Give me three to five sentences on why you think you should do what you uh why you are recommending this. Then I want you to go ahead and email me the uh evaluation.

**15:44** · And inside Zapier agents, you can upload those knowledge sources. So you can see down here I have two Google Docs, the Zapier values rubric, and in this case, we're looking at a social media job description. So we're in the process of hiring someone to help out with our social, and so there's a job description uh associated with this. So this is a very simple agent now that for any uh of these interviews I'm doing with this, I will get in addition to my own opinion, I will get an AI opinion alongside of this. And I I I really like this because it acts as um like a bias check.

**16:14** · It acts as a thought partner. You know, especially for me who's interviewing people across all sorts of disciplines, all sorts of areas. You know, I usually know a little bit about a lot of things, but it's nice to have another tool kind of gut-ing me on some of these things and giving me extra little tips and tricks and nuggets to go, "Oh, that that that actually was interesting. I should pay more attention to that." So, um, we should actually see what this looks like for a candidate, but I want to do one thing real quick.

**16:46** · So, let me show you how co-pilot works if you want to go change this. So, in this case, I actually just got off an interview with a candidate and I want to show the output of it, but I don't want to uh have any PII leak while we're demoing this. So, we're going to have chat uh we're going to have co-pilot get rid of that. So, um, let's say change the prompt to remove any identifiable information about the candidate.

### Wykorzystanie Copilota do ulepszania komunikatów dla agentów

**17:12** · And so, the nice thing about how Zapier agents co-pilot works is it'll help you write these instructions. You don't have to sit down and write all these come up with all these instructions yourself. you can give it kind of just hey basic guidelines and then copilot will go generate all of that stuff for you uh and then you can just edit the the instructions directly if you if you want to.

**17:39** · Yeah.

**17:39** · And I'm going to go ahead and give I'm going to give your team's product folks or whoever design folks uh a lot of kudos because I use both co-pilot and a lot of the improve my prompt little mini features inside Zapier. And I also love how you score how strong some of my prompts are in some parts of the app.

**17:58** · And so it is it is helpful just to have a co-pilot for prompting because no matter how much people say it's it doesn't matter. It definitely matters.

**18:07** · Totally. Uh all righty. So it's made the change. I am going to go ahead. We're going to just I didn't actually check exactly what I did. So we're just going to do this vibe style. So you can see we've got uh interview evaluation for a senior social media specialist. Look, it's stripped out and that's nice. So recommendation for this candidate is yes. Hey, job well done candidate. Uh you know strong functional expertise all in alignment with Zapier's value. Uh they have a deep understanding of social media strategy particularly shift from product focused marketing to story building and community building.

**18:36** · So you can see it kind of works through the job description then it works through the values here um and ultimately tries to like support the recommendation.

**18:48** · Now, uh, one thing that I would do to make this better then is to look at the feedback here and go, okay, how can I update the prompt to give me even more actionable recommendations like if I felt like, you know, hey, this um, evaluator is like being too easy on candidates or too hard on candidates, I would um, basically go through the same system that Hillary shows off with her GPTs, which is like provide more suggestions, more details on this is a good answer, this is a bad answer.

### Pomysły na usprawnienie pracy agenta rekrutacyjnego

**19:17** · And over time, uh, you'll find that your, uh, interview agent starts to get really good at assessing candidates.

**19:27** · So, I'm going to give you two enhancements that I think you should make.

**19:30** · Oh, I love it.

**19:31** · One is one that um, Zach Davis at Launch Darkly showed in his interview flow, which is he actually evaluates the quality of the interviewer during the session against the rubric. And so there could be a feedback for interviewer section at the end that says hey you actually forgot to ask about XYZ or when going into topic you didn't really reinforce this and so next time you interview remember to do ABC.

**19:56** · We did this for um engineering interviews at launch because you know humans get into conversations and we forget exactly what we're going to ask and it becomes a very natural flow. So give yourself a interview coach in your feedback channel. The other thing is man, I just want that yes, no, maybe in the subject line.

**20:19** · If you want like interview candidate, yes, move forward because the most important thing I say, you know, how I win good talent is I just I want to hire them harder than every than everybody else. That's one of my secret paths. So like the sooner you're like this is a yes, let's prioritize reading that.

**20:35** · Let's get the candidate to the next stage. You can get um a little aggressive on talent acquisition. So those are my two pieces of feedback and we are seeing right here Wade is live using co-pilot to add those um suggestions into the overall prompt. And what I like about agents is I think this concept of agents has been very opaque to a lot of people in terms of like what can they even do? What does this mean?

**21:03** · Do I have to like do these you know fancy flow connectors which are available um in your your product? But really what I say is just like if you were to explain to somebody how to do this job in steps and what they would need to get that job done. Write it down and that is that is the definition of your agent. And then these these AI tools can execute them. And then of course you know features like co-pilot or like enhance my prompt can then go make it a little bit more structured for how the AI models would read those instructions. But it's basically like just describe what you want to get done.

**21:36** · Yeah. I think uh a a way I often describe it is if you've ever seen standard operating procedures, you've seen an agent.

**21:46** · And you know, the folks that are great at writing standard operating procedures are fantastic at building agents. But even if you're not great at writing standard operating procedures, this is where Copilot helps you out so much because you can just blab in, can you do this thing for me? and it starts to go, okay, I get your idea, but here's what standard operating procedure for that should actually look like. And then it's awesome to, you know, sit down and talk to someone like Claire who goes, here's two other ideas to make this better. And then you can just go tell CPI to make it better.

**22:14** · I find the real challenge with AI, at least at this point in time, is less about the tools and more about just coming up with ideas for like how do you make this stuff better? And once you have the ideas, it's crazy fast to implement it. Like those two suggestions took literally 60 seconds to add to this and they're great suggestions.

### Błędy popełniane przez ludzi podczas korzystania z agentów

**22:32** · Yeah.

**22:32** · So how if you want them to know the Clarvo magic secret to suggestions on what your AI can do. One of the mistakes I see people make when they do agents is they think what do I do and let's just do what I do. And I say that's a great place to start what I do and how I do it. But then I say but then ask yourself if I had more time what would I do next? And what would I do after that? And if I had three interns on this, what would they do?

**22:55** · And I say like pull that thread a little further along and imagine doing this task, you would do it to the nth degree and you would have maybe interns or additional resources and sort of infinite time to to take it to the next level.

**23:12** · And I think Matt at Suzie showed us this on a very similar flow granola to a more structured workflows app where he said, "Okay, if I had a sales call and my marketing team operated perfectly off that sales call, what are the 15 things that they would do? Not the three things they have capacity to do now, but the 15 things that we have great ideas for." And that can really open up your creativity for what what an agent can do for you.

**23:37** · 100%. I think this is what's lost in the discussion is there is so many tasks that are not economically valuable right now because it's too expensive to pay a person to do that thing or it's too annoying and too tedious for a human to actually follow through consistently on those things. And these are the areas where AI and agents like really thrive because you can put something that will happily do that task for very low budget and do it very very consistently against those things.

**24:05** · Um, and so there's so many tasks inside of a company that simply do not happen, even though they probably would if you could do it. Um, and so it's that that's where I think a lot of the value is. Um, not just in like, hey, do the stuff I already do.

**24:22** · This episode is brought to you by Brex. \[music\] If you're listening to this show, you already know AI is changing how we work in real practical ways. \[music\] Brex is bringing that same power to finance. Rex is the intelligent finance platform built for founders.

**24:38** · With autonomous agents running in the \[music\] background, your finance stack basically runs itself. Cards are issues, expenses are filed, and \[music\] fraud is stopped in real time without you having to think about it. Add Brex's banking solution with a high yield treasury account, and you've got a system that helps you spend smarter, move faster, and scale with confidence. One in three startups in the \[music\] US already runs on BS. You can too at bre.com/howi AI.

### Wykorzystanie Groka do wyszukiwania talentów w mediach społecznościowych

**25:11** · Speaking of um what you would do if you had infinite time and capacity, I have an eagle eye on the the the rubric you just showed and it said that whoever runs your social media needs to be chronically online and you have figured out a way to use AI and probably one of our most chronically online model to identify talent.

**25:35** · So, do you want to show us a little bit about your your trick that I have never literally never heard anybody say before on how to source some talent?

**25:45** · So, uh one of the tools I like to use to help source um under the radar talent is Grock. Um you heard it here first. This is a how I AI first you all.

**26:00** · Okay.

**26:00** · So, uh what we are looking for here is we're trying to find some good social media uh candidates. And so let's say help me find uh posters on X that are fans of Zapier, no code, agent building, automation and related topics. Uh, I want posters that share tutorials and education related ideas, you know. Um, let's see. Uh, what else do we want? Um, these posters should have modest followings.

**26:50** · Um, not too much, but not too little. Um, I'm looking for diamonds in the rough.

**27:07** · Let's see. Uh, what else might we want?

**27:09** · Uh, let's say we're on a budget. So, um, we're on a budget, so look for folks outside the Bay Area. We don't want Zuck to get his hands on these people. Um let's um you know g give me let's just say like give me 10 ideas. So we'll just start with this uh and see what comes up with here.

**27:32** · Um I will like when we're looking for folks I will do this um to just do tons of revs for it because sourcing candidates is crazy times like you have recruiters like they do this stuff all the time. Um but they all love LinkedIn and they use like LinkedIn stuff. I find Grock like helps you find just a different slice of the market that people are not looking for. And because you can ask it um through natural language, you can do these kind of odd searches that are like really hard to do in kind of like LinkedIn's like boolean search um tools.

**28:03** · Uh and so you end up finding people that you're like, "Oh, it's kind of interesting." And it's great for other stuff, too.

**28:13** · Like if you're looking for um like a lot of folks do uh influencer marketing these days. Well, if you want like this would be a very simple way for me to source uh potential like folks to do influencer marketing or you know if I wanted to find people who just might have product feedback for me. Say you're like a new startup and you want to go find people who have a certain problem you could do the same way. So um you know Grock is like a people finder uh is a really helpful tool. Um, all right.

**28:40** · So, you can see here we've got a handful of um folks that they sent over. So, you've got automation king uh who's sharing tutorials. You've got uh uh Ritz talks. Um we've got a lot of folks from India, Nigeria, etc. So, there must be like a hot bed of um no code talent going on in there. Interesting. So, you could click through to these and you know start to check out uh different profiles here. Actually, I'm not sharing I'm sharing just a tab. Let's just hover and see what we get here. Um, all right.

**29:11** · That's kind of interesting. Um, a thousand day challenge. That's kind of interesting. Um, someone's maybe like building out like a whole education curriculum. Um, so that's interesting.

**29:23** · We've got one here that's um, uh, I don't know, that's like kind of pretty standard, I feel like. Uh, interesting. See, a lot of the one challenge you have with this is you start to find folks who like I can't always tell if they're bots or that's the one challenge with the Gro stuff.

**29:41** · Not a bot.

**29:43** · I know, right? So, let's say let's do not a bot. And uh let's say uh give me people with real faces as avatars. Um is that what they're called?

**29:56** · For profile for profile.

**29:58** · Avatar would be not a ring.

**30:00** · Yeah.

**30:00** · And let's do let's just do um we only let's say we only hire in the United States. So let's do United States located folks. Um give me uh you know 10 more ideas or something like that. So you can kind of just do this back and forth with Grock and you'll just find like like we're looking for diamonds in the rough here. So it's not that they're all winners. Um it's just to help you unsurface folks that you may never come across um otherwise.

**30:25** · Well, and what's interesting about what I was thinking as it gave you this list is, you know, maybe not all those candidates would be great, but as you said, there must be something no code happening in Bangalore, like should we do more community events there? Like could these be so so it can give you ideas of kind of sub sub segments of your market that maybe maybe not for an employment perspective, but maybe for a customer engagement, community engagement perspective could be really great.

**30:56** · Now, let's see. Here's interesting. This one didn't do a good job on the, you know, only 16 followers. That's tricky to learn tricky.

**31:02** · You need to say it cannot have numbers more than two digits in their username.

**31:09** · Cuz that's the trick.

**31:10** · There you go. Um, here's a couple that look pretty good, though. Uh, I liked I liked Nathan. Nathan seems kind of interesting. So, you know, again, with recruiting, it's an interesting The thing I tell my team is there's there's no there's no shortcuts in recruiting is what it boils down to. It really is a numbers game.

**31:31** · And so, you're just trying to like increase the surface area of your ability to find interesting, talented people. Uh, and you kind of just got to sift through a lot of lot of stuff to find them uh at the end of the day. So, um, Brock, also, by the way, we're looking at just X posts, but you can ask it. um you know how uh how about finding you know 10 YouTubers um so you can do kind of the same thing and YouTubers might actually be a better fit for us because these people are posting content and videos. So um you know you can do that as well.

**32:02** · Uh, so I do like it for um yeah, finding finding diamonds in the rough.

**32:09** · And so why Grock? Not just because you have this access to X, which is just a different slice of the market than something like um LinkedIn or or even like parsing YouTube, but also because it has this like pretty broad um sources of data that it can pull in. I also love the reasoning we just saw here, which is Grock got frustrated.

**32:32** · Oh goodness.

**32:33** · Okay, here is here are promising YouTubers.

**32:38** · Interesting.

**32:39** · So, there we go. Uh, Zapier's Brigade Guide 2025. Like, oh, that's nice.

**32:44** · Somebody built that. I like that. I'd have to go the The thing that's annoying is it gives me their their X profile, but what I really want to go see is the YouTube channel. So, I go back and say like, "Hey, can you include the YouTube handle uh channel link in the um table here?" Um, Doc Williams, I happen to know this guy is quite good. So that's that's a nice find. Um we got a competitor in here. So that's interesting.

**33:08** · They're probably not gonna go there.

**33:10** · Uh yeah. So I don't know. It's uh I think it I don't see a lot of people using Grock in this way. So uh I think it is an interesting tool to share. It is especially helpful for communities that are heavily on Gro. Um yeah, like another area we've used it before in the past is finding um technical AI talent because there a lot of discussion about AI happens on um X and so it is really helpful at surfacing those folks.

### Podsumowanie przepływów pracy AI w rekrutacji i zatrudnianiu

**33:40** · Well, this was our first I think our first Grock walkthrough on how I AI and I did not expect it to be around recruiting. So a very very first for for our show and thanks for showing it. So just to recap what we looked at today, we saw your meetings to values workflow via granola. We also talked a little bit about how you have sort of always feedback and coaching even for yourself as a CEO.

**34:06** · We looked at a Zapier agent for giving interview feedback to make yes or no hiring, you know, kind of early calls and give you some meta analysis on your interview style. And then we are going to find terminally online YouTubers to she'll know on the internet via Grock. So this was a end to end how to AI native CEO endto end how to do recruiting and hiring and culture values alignment with AI.

**34:36** · I'm going to do a couple lightning round questions and then we are going to get you out of here. So the first one that I have to ask is this has been a lot around talent and the conversation on AI has been a lot of like what roles are changing, what roles are going away and what roles are durable and you just said

### Krótkie podsumowanie i końcowe przemyślenia

**34:59** · something which is a lot of tasks that were just not economically viable for companies now can get done and I think that's a whole set of work that can get done in an organization but you're still hunting for talent. So I have to ask you what roles you still feel are like highly competitive uh right now even in the middle of all this AI transformation.

**35:24** · So we're insatiable for engineering talent engineering engineering leadership like that we're hiring very very consistently.

**35:33** · There's an interesting way you phrase the question though which was um where is there still demand for top talent? And I think the answer is for top talent everywhere. everywhere.

**35:42** · Everywhere where I see question marks is very hyper specialized roles that focus on a very particular task where that task is now almost entirely done by AI.

**35:58** · So you think like your classic like analyst roles where it's like hey I'm going to go uh do like competitive research on a bunch of it's like that's a prompt now. Uh and so there are ways in which you can elevate that job. You can build agents that help orchestrate this stuff and then you can sort of redeploy yourself in other areas. And so I look at most knowledge work and say hey there is a version of your job that can be elevated and allow you to have much much higher impact but it requires you to invest in the tools and requires you to learn these things.

**36:29** · And the places I worry most are in organizations that have fleets of these people doing these jobs. That's the place that's really tough because you definitely don't need fleets of those folks anymore. And so that's where I feel like, you know, if you're in that situation, you got to find a way to elevate yourself. Um because that's going to be tough. Um but most most jobs I feel like there is like top talent. I I I need top designers. I need top recruiters. I need top PMs. I need top marketers. I need top sales reps.

**36:58** · Like all of these things, I'm not done hiring them. Um, it's just what it means to be top has has changed quite a bit.

**37:06** · Yeah, I completely agree. And what I like about what you're doing inside the company is you've just leaned in to not only hiring people who fit this new profile, but again, as we talked about at the beginning, investing in time and development for your team to build these skills. And so I'm curious as someone who has leaned in very hard and probably changed how a lot of people do their job probably by by practical nature of how your product has evolved over the past two years and allowed them to do their job little very differently. How has that changed the company if if at all?

**37:38** · What feels different? What feels the same?

**37:40** · You know there like there's feedback bots everywhere. So you're like constantly getting coaching and feedback on things. Um, you know, we've always had a lot of automation, so that doesn't feel all that new. Like our Slack is pretty unhinged with like, um, you know, emoji reactions trigger all sorts of stuff. Um, and it's not too uncommon of a scenario inside of Zapier for like a new person to come in and like, "Oh, that's a cool emoji. I'll react with this." And not realize that like that is actually attached to something. And they'll they'll, you know, trigger a suite of automations.

**38:11** · Most of the time it's like pretty benign stuff. Uh, and so it mostly gets a chuckle. It's not hooked up to anything like crazy critical. Um, but that has always been the case inside of Zavier. Um, you know, I think the the next chapter for us where I see opportunity is how do we start to like break down more of these silos?

**38:32** · We've already started doing this in parts of parts of the organization, but this feels like one of the harder culture tasks where you're taking, you know, two job families and saying, "Actually, these need to become one now." And um we're starting to see that in pockets. Uh you know, I wouldn't sit up here and say like, you know, there's uh you know, we we only have builders now. There's no such thing as like a product manager, a designer, an engineer. We're not that far. Um I I think, you know, some of that stuff feels a little overstated in 2025, but in 2030, I don't know.

**39:03** · I I famously said it in 2023, so I'm just waiting for it to become true. I'm just either I get to every year I get to say I'm wrong for now, but as soon as it happens, I'm going to say, "Look, look at me. I have I have the receipts."

**39:18** · I think you're directionally correct.

**39:20** · It's the time horizon that's tricking.

**39:21** · Horizon. Exactly. That's exactly right.

**39:24** · Well, okay. My last question I ask everybody. You seem like a really nice person, but when AI is just not giving you what you want, when Grock is being sassy, what is your prompting strategy? How do you handle it? How do you deal?

**39:39** · Yeah.

**39:39** · I I basically have two bows. One is like pretty pleasant, you know, hey, please do this, please do that, thank you, etc., and then if I'm really really not getting it, I get pretty curt, no, try again. No, do this different. Uh, so that that's my my go-to.

**39:55** · Good. Do you um do you feel like any of those strategies actually work in prompting zap your agents? Like I see a lot of markdown. Should we put all caps in there? Should we say I'll give you a dollar if you do this right in in our agent prompt? Have you tested any of that?

**40:11** · I I I have. I can't tell if it makes a difference or not. I I think it doesn't.

**40:16** · I think how we how we prompt is more of a reflection of us than it is of our AI overlords. Well, Wade, this has been fabulous. Where can I know a little bit of where we can find you, but where can we find you and then how can we be helpful to you?

**40:30** · Yeah.

**40:30** · Uh I am, you know, Wade Foster on X on LinkedIn. Uh you should check out Zappier. check out Zapper agents. Like agents are a way different way to build automations than folks maybe are familiar with with Zapier. Uh so definitely check those out. And uh you know if you're I mean shoot you're watching how I AI like you want to work at a company that's AI pilled so to say like check out we're hiring top talent everywhere. So we'd love to have you build crazy stuff inside of Zap here.

**40:54** · Well thanks for joining us. I appreciate it.

**40:56** · Love it. Thanks Claire.

**40:59** · Thanks so much for watching. If you enjoyed this show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. \[music\] Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiipod.com. See you next time.