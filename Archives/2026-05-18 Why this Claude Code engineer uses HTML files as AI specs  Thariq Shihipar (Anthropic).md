---
type: Web
authors: '[[How I AI]]'
url: 'https://www.youtube.com/watch?v=Qrpm7E80wQ0'
published: 2026-05-18T00:00:00.000Z
created: 2026-05-18T00:00:00.000Z
tags:
  - narzędzia-AI
  - strategia-AI
  - prompt-engineering
---


![](https://www.youtube.com/watch?v=Qrpm7E80wQ0)

## Transcript

### Wprowadzenie

**0:00** · Markdown became a really popular way of interacting with agents, but the plans are so long, I honestly have stopped reading them. And this was honestly a mistake. I think that you still need to be really in the loop.

**0:10** · Plans matter, PRDs matter, spec matters.

**0:13** · When you say, okay, cloud can run for 8 hours. What you're really saying is cloud can spend 500 bucks. All of us are becoming these compute allocators now, right? And so you have to decide what is worthwhile spending the compute on.

**0:25** · People ask me all the time, Claire, you said product management is dead. What's next?

**0:28** · \[music\] I'm going to say you're a compute allocator babe that's the job now HTML is a lot easier to read and so it's just a richer communication medium between you and quant instead of saying here's a markdown document it was like what's the best way to convey this information so you can actually engage with it and pick something this is the plan it's purely in HTML this is something that I will actually read this is not even personal software it's like micro software on top of micro software where \[music\] welcome back to how I AI.

**1:00** · I'm Claraveo, product leader and AI obsessive here on a mission to help you build better with these new tools. Recently, I was able to attend Code with Claude, Anthropic's first developer conference. And as part of that, I got to spend a little time with Thoric, who works on Claude Code, and taught me something that has blown my mind ever since I heard it. \[music\] HTML is the new markdown. He's going to show us how to use cloud code to generate rich artifacts that both you and the agents can enjoy working on.

**1:32** · Let's \[music\] get to it. This episode is brought to you by Celiggo. Every company today wants AI to improve how work gets done. \[music\] The fastest way is building it directly into everyday business processes. \[music\] Automating employee onboarding, keeping customer data accurate, managing orders and inventory, or resolving finance and operations issues. When AI lives inside the flow of work, it can update records, \[music\] trigger approvals, route work, and kick off the next step across systems. That's \[music\] how teams operationalize AI, and deliver measurable results.

**2:03** · Celigo makes this possible. And now \[music\] with Celigo Aura, it's never been easier. Celigo Aura gives you \[music\] access to the entire platform through natural language, connecting your systems and turning intent into action. All of it under your control. Companies like databicks, PayPal, and Ollipop rely on Celiggo to run critical business operations at scale. \[music\] Ready to operationalize AI? Visit celigo.com/howi aai. That's cel.com/howi aai. Welcome to How I AI.

### HTML jako nowy Markdown

**2:42** · Thanks for having me.

**2:43** · I am so excited to be here at Codewith Claude in San Francisco. There's a lot of exciting things that were announced and we'll get to that in a little bit.

**2:50** · But you told me something I was not expecting to hear today which is you heard it here first. HTML is the new markdown. Tell us more. I mean I think markdown became a really popular way of interacting with agents especially like you know Opus 4 and cloud 3.5 where you

**3:09** · know they have a plan and the plan is like how to do this feature and maybe it's like 50 lines of code and you can edit it right like I think back then you were still like reading all the outputs and editing the the markdown and making it right but you know as the agents have gotten longer and longer running when you have Opus 4.5 and 4.7 they're running for like an hour or something and the plans are so long I honestly have stopped reading them and this was honestly a mistake. Like I think that you still need to be really in the loop.

**3:37** · You really need to understand what the agents are doing. Uh but like a thousandline markdown file, you know, I don't even edit them anymore. I just ask Claude to edit them instead.

**3:46** · And so I think one of the things that I've been seeing emergently in the cloud code team is that like they that we're using HTML files instead. And so HTML is like the models are still very good at it. They have a lot of more context now. So you can spend the more extra tokens and they like it's a lot easier to read like they can uh have a lot more information.

**4:06** · They're a lot scrollable more scrollable. And when you're talking about implementation like you know sometimes you see claude make these like little asky markdown things where you're like oh like here's a little you know little mockup and it's trying really hard. in HTML it doesn't need to try nearly as hard right like there uh it can actually draw like things that you

**4:26** · can look at and so it's just a richer communication medium between you and quad and before we go further into HTML specifically I do have to pause because I do have a vested interest in this which is you are saying for the people who are not listening listen up yes plans matter PRDS matter spec matters even as these models get more intelligent you still feel like that's a really important part of the process oh 100% yeah I I think that you know everyone has different views on how it'll go but I I think that this will just forever be the thing because when I

### Mentalność alokatora zasobów

**4:57** · you say okay cloud can run for eight hours what you're really saying is cloud can spend like 500 bucks you know what I mean and and so if you're spending 500 bucks or like I think all of us are becoming these compute allocators now right and so you have to decide like what is worthwhile spending the compute on y and I think that is happens in the spec and planning phase right you have to really understand like what do you want?

**5:21** · And sometimes you don't know. Sometimes you have to like pull it out of yourself by chatting with Claude. Uh sometimes you have like unknown unknowns you need to figure out. Uh but yeah, I think this is like the whole thing now is just like really getting in in sync with Cloud about what it's building.

**5:35** · I love what you said because people ask me all the time, Claire, you said product management is dead. What's next?

**5:40** · I'm going to say you're a compute allocator, babe. Like that's \[laughter\] that's the job now. You're still doing the same thing, though. You're writing documents to decide whether or not something else should do do work in the shape of that work. Okay. So, you've convinced me HTML is the future. And I I like how you said this. It's not that it is necessarily harder or easier for the agents to read. They're very smart. They can read all sorts of code.

### Jak HTML sprawia, że ​​specyfikacje są bardziej angażujące

**6:04** · But in fact, what you're finding is that HTML makes it easier for you to engage with the content, which then uplevels the quality overall because you're not your eyes aren't crossing looking at a bunch of raw markdown, being like whatever, it's probably good. Instead, you're actually getting pulled into the spec or the document or the plan and then interacting it with a way that upgrades the the quality and then you can ultimately build something better.

**6:30** · Yeah, that's right.

**6:31** · Okay.

**6:31** · So, you're building something with the agent so the agent can manage you. You know, I'm not sure if manage me is the right word exactly, but you know, I just I care a lot about being in sync with the agent. This is sort of like the features that I built in Cloud Code have been like that, you know, like how can I get to know you better? So, yeah. Yeah.

**6:47** · Yeah.

### Demo: Burza mózgów w HTML z Claude Code

**6:48** · Okay, great. Well, we have we have Claude Code up. So, let's walk through how that how that works.

**6:52** · Yeah.

**6:52** · So, I I did like uh a little bit before we started uh and so I like to talk with Claude just as a human, you know, and like I always start with brainstorming. It's so much easier to brainstorm once you like, you know, uh once you have a partner. So, I was literally like, "Look, I'm on a Claro podcast. Um I want to do a demo, you know, and can you brainstorm some ideas in the HTML file, right?" And this is literally the prompt I gave it, right?

**7:17** · Like there's not it's not complicated.

**7:20** · And so here you can see the eight visual demos that it made for me. And uh it has these little mockups as well, right? So like purity to working prototype, right?

**7:30** · Like it it searched you up, right? You saw that with a web search, right? Uh whiteboard sketch to working UI, which I thought was really cool. This is such a cute like little thing.

**7:40** · Extremely cute. And I It's what's really funny is just this morning a chat purd user messaged me and they're like, I love the mockups in chat purity and I'm like, what in the world? What are you What are you talking about? Because I have something very similar to this in code review right now and haven't shipped it. And I'm like, did I like did I act Did Claude accidentally do this? And it was that like cute little a little asy, you know, wireframe. Um, so this is definitely the dream.

**8:08** · Yes.

**8:08** · But not but but now you're telling me I'm going to build it. So So it's giving you basically instead of saying here's a markdown document of kind of like what you should talk to Claire about and some descriptions of things you could do. Instead, it was like, what's the best way to convey this information so you can actually engage with it and pick something? And it used HTML to make this visual guide of a potential agenda or a set of demos and you just get like a much richer expression.

**8:40** · Yeah, exactly. Like I I think like another like for brainstorming, one of my like sort of rules of thumb is that I'm not going to read a longer output than the screen on cloud code, you know?

**8:49** · So like if I if you gave me eight ideas, I'm just not going to see all of them. And but with HTML, I'm definitely I scroll through all of these, you know, and uh yeah, the the the diagrams just make it so much more evocative for me to like sort of understand what's happening, right? The slash command starter pack, vibe code of feature flag dashboard.

**9:08** · \[laughter\] Yeah. Yeah. PRD diet. And the the one I ended up liking the most was the CSV to interactive dashboards.

**9:15** · We love a dashboard. Uh I used to say when I was in enterprise, I guess I still am in enterprise software, dashboards equals dollars. So, I like this one.

### Od burzy mózgów do pełnego planu wdrożenia

**9:24** · Um, okay. So, you use clog code. You said brainstorm, but brainstorm in HTML. Give me a couple things that I can talk about. It gave you eight ideas, including visuals and this lovely like why her, what the visual is, and then the I like the risk. It's like it could go sideways as all good demos Yeah.

**9:42** · can.

**9:43** · Um, and so you're going to pick one and then you're going to show us how you pull this through to a full plan on on on this idea.

**9:51** · That's right. Yeah. So I I think the what I like about HTML is like really Claude really understands this. And so my next prompt here was really like okay uh I asked it to make some mockups in in the follow-up prompt and then I was like I asked it to interview me about number eight, right? And so this is something that like you know similar to specs and PRDs, right? Like uh finding out my unknown unknowns. What do I want it to do?

**10:13** · I answered a bunch of questions and uh now I'm like okay create a HTML file as a plan that helps me visualize what the implementation plan is include excerpts, mockups, code when whatever is needed to give me like maximum context, right? Um and so then it made me this HTML file here. Yeah, you can see now this is this is the plan. Uh but it's it's purely in HTML.

**10:34** · It's got like it started scripting out the podcast itself which you know maybe I I didn't need all of that but like you know we're making a skill and so it it you know fleshed out the the file system. It gave me like an exerpt of the skill.md um it put together like a a mood board as well some example components.

**10:58** · um some of the logic here um yeah insights and templates helper scripts right and like helping me get a sense of like what's the important things for me to know here um yeah this is this is something that like I will actually read you know yeah and I want to go back to claude code really quickly if you don't mind which is you know people are going to ask how did it know exactly what to put into the spec and I just I want to go back to Your prompt was very simple. And it's so funny.

### Filozofia narzucania: Zaufaj Claude, ale nałóż na niego ograniczenia

**11:30** · I've done I don't know 75 of these how I AI episodes and they get incredible outputs and everybody's prompts like make the thing. Hopefully it's good. Yeah. Kind of nice. And so I love that this prompt is literally just create an HTML file with a plan. Help me visualize. You misspelled excerpts. \[laughter\] And you're like excerpts, mockups, code, etc. Whatever is is needed. Yeah. And so I do want to encourage people, you know, don't stress so much about what should go in the thing. And in fact, it might change initiative to initiative.

**12:01** · It might be slightly different to engage you with the work, but like identifying what you want to get and then letting claw let letting letting the model do what it needs to do will do a very high quality job.

**12:18** · Yeah.

**12:18** · I I think with prompting it's like this fine balance of like I think you want to give enough information that you get what you want but you don't want to over constrain claude you know and so sometimes when I see people with a lot of like overbuilt skills kind of like you know you're an expert planner or something right like that is usually like outsourcing too much and constraining it um but in this case for example like I really did wanted to make sure it gave me code exerpts and I wasn't sure if I did uh whether it would do that you So this was really important.

**12:49** · But then I always need to give Claude an out, you know, I always needed to be like, "Okay, like you asked me for this, but you know, like there's something else I want to give you." And so whatever is needed to give me maximum context is like my way of saying like, "Hey, Claude, like I I trust you here. I want to just like be in the loop with you."

**13:07** · Yeah.

**13:07** · I I love what you say, which is I trust you because my new ending prompt is not make no mistakes. Love make no mistakes, but that's not it. I I literally like I believe in you and trust you.

**13:21** · Exclamation. I'm like truly I know you are capable and I believe in you to make these decisions. And so I I think leaving that open-ended sort of like whatever you got to do, I trust your judgment. Um at least it makes me feel like I get better outcomes.

**13:35** · Yeah.

**13:35** · Yeah. I I mean I've loved the like recent twist on this where it's like make mistakes Claude, you know, like fall in love, you know, like you know, make some bad decisions \[laughter\] like we need uh we need more happen stance in in our life. Okay, so you built this thing. Another thing that I want to walk people through if you pull up the plan because I think about this a lot and I get people ask that ask me this a lot which is like what's the future of the PRD? What's the future of the tech spec?

### Przyszłość PRD i specyfikacji technicznych

**14:00** · Are these things separate? Are they together? And I think what's nice is they whatever you want, right? And whatever you want for the audience. So you are a single builder in the instance of this demo. Y you want it all in one piece. You want the product idea. You want the I guess you want a 12minute walkthrough of how you're going to demo it. Exactly. You want code snippets. You want style guide. You want that allin-one thing because this is a self-contained little project that's easier to have it all at once.

**14:29** · But what I can imagine in larger organizations is like be like put the PRD in one tab and put the tech spec in the second tab because maybe separate people would be reviewing that information. And so you can really kind of like craft a ideal spec package.

**14:47** · That's right.

**14:48** · To whatever you want with HTML in a way that markdown is a little bit more constrained. It has to either be like one megapile or like separate files. And I think this is just nicer from that perspective.

**14:58** · Yeah, I think that's right. you have a lot more interactivity. I haven't asked it to make tabs here or something, but it can easily do that. It's like all the same to Claude, right?

**15:06** · Um I think one of the things on like the specs and PRDs is like I think you're trying to find like the boundary of like what you need to know with Claude.

**15:14** · And for example, if you're doing something very technical, I like to do the type interfaces. So this is like you know just like understanding what the types are so that I don't often care about the actual implementation of it but just like okay like the types help me understand what we're building and then I might edit those right and that's like the boundary I want to interface at and yeah like across the problem right like from yeah the the arc of the podcast to to mockups where where do you want to interface?

**15:42** · Yeah, one one other thing on this types as sort of a an important input is I think types are really great and then really a validation criteria and set of tests or other ways to see if you can get what you intended to get and I know you all like just announced outcomes which is really focused on this like kind of goal oriented you need to achieve this thing do whatever you need to do and I think that is a piece that most product managers at least are not used to writing like the technical success criteria of a feature.

**16:14** · Um, and then how to test your way into it. I do those two things as well. It's like I care about the data model and the shape, the pipes, like what's going in and then this is how you would test that you did it correctly. And with those two bookends, you can like everything in the middle is kind of kind of gravy. So that's what I think about.

**16:32** · I think that's right. We could have a whole podcast on testing. I think there's like Okay, round two. We're going to get it scheduled.

**16:39** · Yes. Yes. Yes. Yeah. My my tagline there is like uh test verification is not testing. Yeah.

**16:45** · And so I think there's a lot of like there used to be like unit test and things like that but now yeah verification can be like a rubric like with managed agents and outcomes. It can be like have cloud record a video of what it did for you, you know. Um so there's a lot of depth there.

**17:00** · Yeah.

**17:00** · I keep a set of like synthetic data and I like run a CLI through this synthetic data cuz I'm like these are all the things that have broken in the past and if you get better at like resolving these broken things then we have moved forward. So I think there's just a lot of interesting verification and testing mechanisms you can do now. We are going to part two pressure him to do it um in the in the comments please please tell us. This episode is brought to you by Persona.

**17:26** · You're learning to build with AI, but there's an important question you need to ask. Who is actually using your product? Is it a legitimate user, a bot, or a fraudster? Brex, Figma, Etsy, and Twilio trust Persona to answer that question. With \[music\] Persona's identity verification platform, you can create branded experiences, automate fraud prevention, and know who is human

**17:50** · online. \[music\] that makes it easy to give good users an experience that makes them feel welcome and to stop bad actors from causing damage. \[music\] And for those of you building in the AI agent space, Persona helps you verify the identities of people, businesses, and developers behind agents. It's how companies like Lithic and Skyfire are pushing the frontier of agentic commerce. Learn more at \[music\] withpersona.com.

### Edytowalność specyfikacji HTML

**18:16** · Okay. So, you have have built this, but here's here's the objection I'm gonna get, which is Markdown is accessible, right? I can like go into Markdown, type in it. Yes.

**18:30** · And make edits. And so, I think that is one reason is it has been so popular. It's bridged this gap between machine writable and readable, human writable and readable at a very low level of sophistication. Right? As soon as you understand, okay, these like hash signs mean headers, you're good to go on on markdown.

**18:48** · Yes.

**18:49** · How like I want to fix this. How do I how do I touch this? How do I edit this?

**18:53** · Yeah.

**18:53** · Yeah. So, I I think that this is like a great point, right? And I think one thing I felt with Markdown was that one I because I had stopped reading them, I had stopped editing them as well, you know, and so I would end up asking Claude to edit them. And so like that is like the most basic form is just to be like, "Hey Claude, I didn't like this part of the plan. Can you edit it?

**19:13** · Uh, but let's say you want to get really in the loop, right, and like really get in depth with it. Claude can also do that for you. So, the next prompt I had and I forgot if it was here or no, it was here. Okay, I want to create an editable HTML artifact to help me define the the decision rules. So, these are the rules that it's defined here on like okay, how do you take data and turn it into, you know, a visualization? And I think some of these are kind of arbitrary. Um, and so I asked it like, uh, you know, to create an HTML artifact. Uh, I don't like the ones we have right now.

**19:43** · Make this a custom UI that helps me with structure but gives me flexibility. Design the ideal interface for this problem. Yeah, u, I really wasn't quite sure what it would give me. And this is one of the fun parts of HTML 2. It's just like I just want to see what what cloud like cooks up here. And um, yeah, this is what it gave me, right? So it's like a my own beautiful custom interface. Um, I can sort of like, you know, edit any of these fields. Uh, I can, you know, like hide them. I can copy. I can, you know, add new fields here. Um, and it gives me a markdown to to copy back.

**20:16** · And so once I'm like, okay, I have this, I can copy it back into the um the output.

### Mentalność obfitości

**20:23** · Okay. I want to pause because people are going to totally miss what you just did. So, I'm going to repeat it, which is you have this HTML plan.

**20:30** · Yep. And there's a section in the HTML plan that is a pretty like specific table of rendering and visualization rules. Yes.

**20:40** · Per data type that you could predict would be in a CSV.

**20:42** · Yep.

**20:43** · And you're like, I don't like it.

**20:44** · Yep.

**20:45** · And instead of going back into cloud code and being like, I don't like it. Let's go back and forth and edit it in like the terminal, you said, there's probably a way for me to interact with this p particular problem that's ideal from a user perspective. So basically build a throwaway UI.

**21:02** · Yes.

**21:02** · For this very it's like this is not even personal software. This is like sub it's like micro software on top of micro software which is like I've made this very personalized plan and then I'm taking a module in the personalized plan and zooming into it using a very custom UI.

**21:19** · Yes.

**21:20** · That's going to engage me with the the content to get to a higher quality. Um, I also like that it's like kind of gamified. It's like very consumerry.

**21:30** · Yeah. Yeah.

**21:31** · Very consumey. And you said in the prompt, give me the ideal UI for this to like help me engage with this. You built this, then you get the the data, right, and then you're just going to bop it back into the into the file.

**21:44** · Yeah, exactly.

**21:45** · So fun. Is this how you're building now?

**21:47** · Actually, it is.

**21:48** · Yeah.

**21:48** · And do you have any challenges with like how are you passing this around from a collaboration perspective or is it just like this is the way a singlethreaded product or engineering leader can get something done? It's you're engaging with yourself and with the model and so you feel like you can own things full stack or do you hit friction points with collaboration like when somebody needs to give input on this?

**22:09** · Yeah.

**22:09** · Or you want input?

**22:10** · Sure.

**22:10** · Yeah. Yeah. I mean I think uh on the scale of an implementation plan it's way better, right? And I think that this is cuz you just like can upload it to like you know whatever AWS or something and then you just share the link around and so definitely the likelihood of like I don't know cat or Boris like reading this is like a hund times better right um and so I think that really helps me like present this. I also just you know somewhat related I use it a lot in like collaborating overall.

**22:42** · So, for example, uh you know, I report to cat and so like every week I send her a weekly status update in HTML of everything I've done. I get Claude to read my Slack and just like create this message and and like she actually gets to read it and I don't have to spend that much time on it, you know?

**23:00** · Oh my gosh. New compet new internal competition is showing up. It's not just who is building the best product. It's who's building the best product that goes into building the best product and like who is building the best product to represent themselves to the manager. But I I mean I think why you do that is not artificially for fun.

**23:18** · It is that it is just much a much more effective way to communicate across a company is with content that is engaging and at the right level of detail and consumable and we're all pretty good at reading websites.

**23:35** · Yeah, exactly. I think this is like when I think of like abundance, you know, and like you know, we talk about like Javon's offer software like, oh, like you software gets cheaper. What do you do? I'd say like the amount of tokens I produce that go into production code like extremely small. It's like 1% or something, you know, but like I'm generating so many more tokens like this, like my dashboards, my custom interfaces, like really trying to get a sense of like what do I want to do? And yeah, it's like I have everything I'm interacting with is so beautiful.

**24:04** · And I think my hope is that it also like translates into what I produce in the end, right?

**24:09** · It's like more in the loop. It's more beautiful. It's more like, you know, like what me and Claude working together.

**24:16** · Yeah.

**24:16** · And I I like this because I've been in the in the product game for quite some some time, many decades. And people used to get so wrapped around the axle on like what's our source of truth for specs and what's our source of truth for PRDs and you know is all this information in some centralized place that we can all access it and is it all in the same format? Is it all in the same template? And there were these arbitrary rules because creating this content was relatively expensive.

### Dokumentacja just-in-time i oprogramowanie jednorazowe

**24:42** · Consuming it was certainly expensive.

**24:44** · finding it was really hard. And I think when all of that cost goes to like functionally zero, although we're all paying our I call them \[laughter\] our our claude chits. We're paying our claits, but you can kind of put stuff wherever in whatever format because we know these models are very good at using tools to discover the context that they need. And so I do think there's this fun moment where you could really up you like uplevel the things that you should care about which is like what is the content of the plan? Is it a good idea?

**25:14** · Do we feel like it's going to be executed well as opposed to like I can't put a interactive markdown document in our you know blessed document repository and so I have to have like another asset somewhere else. And so I just I like this idea of just in time documentation very very high quality some throwaway software. which is nice. Like it's cheap so you can toss it.

### Wykorzystanie planów jako artefaktów do wdrożenia

**25:39** · Um and then I like you know the executive me is like what if we can't ever find this again? I'm like oh Claude can find it for us it's fine.

**25:46** · Definitely.

**25:47** · Um and then do you feel like this results in better products? Like would you how would you build off of this?

**25:52** · Would you say plan's good, let's go?

**25:54** · Yeah, I I think so. I I didn't uh hit implement on this but yeah, I would basically use this as an artifact. And so, um, I would clear context and I would say like here's a plan.

**26:07** · Um, you know, implement it.

**26:10** · Uh, you could also have like you can also use this as a source of checking the truth, right? And so again, a benefit of HTML is like I've got a little mockup here as well. So, right, I can have the verification a or I can have the verification agent check like, hey, what did I intend to do, right? And what actually came out in the output, right? Um, so yeah, I think this is like really uh helps cloud be more in the loop. Um, I've got some other examples of like plans here that we can let's see it.

### Demo: Żywe systemy projektowe w HTML

**26:39** · Yeah, this is like a a post I'm working on. So like uh it's just like different ways I'm I'm using uh cloud code or sorry using HTML with cloud code. And one of my favorites is this living design system. And so it's this idea that like you know oftent times when I am making let's say a new app in the entropic design system, right? Like Cloud Design does this very well. You link a GitHub repo and you uh like it will extract the design system from it. Yeah.

**27:08** · Right.

**27:09** · And uh yeah, I saw Nate did that. I'm like so smart. Uh what this does is like basically I have an HTML file that represents my design system.

**27:18** · Yep.

**27:19** · You can see the colors here, typography, spacing, radius, core components, right?

**27:24** · It's a fairly small one. Um, but once I have this, I can basically start passing this around. Yeah. So, I go to a new project. I'm like design system.html, right? Instead of like design.md or something.

**27:36** · And it's got this like compressed understanding. And you can literally just point pod at a folder in your thing and be like, hey, find the design system here, create a HTML artifact, and pass it around. So, I I love this. I do this as well. I will give you my um like advanced mode version of this, which is I use claw design. I pull in my both my marketing site repo and my app repo which have like some expressions of the same design system in I say make the design system.

**28:05** · Then I actually make it ask ask it to make a design system or a style guide but I want it at the component level. And so we have like colors and all this stuff but we also have components because there's some tweaks in how you want the design system implemented in particular components. and then I drop that into the repo and then yes I say exactly this um reference the design system.

**28:29** · The advanced thing that I do that I think is really useful for people who have to interface with marketers is I um have a like what I call a god what do I call it like it's like a component visualization page which is like the 25 components of our app in action and interactable y in a page. So a marketer can go in and like get the get the component in the form factor it needs to look quote unquote real.

**28:59** · Yes.

**29:00** · And then you can download a transparent PNG.

**29:02** · Yeah.

**29:03** · And like drop it in a deck or drop it in a video. And I know you or or we use that as a source of truth for like videos. And so I love this idea of like this living design system and this living design repository. It's great for code, but it's also great for marketers, for designers, because one of the hardest things is is getting versions of your app that look real.

**29:26** · Yeah.

**29:26** · And you can use HTML to do that.

**29:29** · Yeah. Exactly. I I think there's also something here around like component variations, which I thought was um Exactly.

**29:36** · Uh fun where it's like Yeah. like you you create a component, you want to see like, oh, like what if I change the padding or what if I change the border, you know, solid things like that. like these are like a pretty simple like you know uh way of just playing with this. This is also claw design like right like where you create these little components and or these little knobs and sliders.

**29:56** · Um but yeah you you can imagine one this is like the abstract of like oh like what's the interface for this thing that you're trying to do and how can you visualize it and yeah there's not a trade-off between like being nice pretty for you and understand being nice for Claude you know like they're They're really the same, right? So, and you're making me think of one thing that I love in claw design that I think you could bring into your plans.

### Dodawanie komentarzy i Adnotacje do planów HTML

**30:20** · Again, it's one of these features that like sounds truly cuckoo bananas to build, but is totally possible and easy to do, which is I love in claw design once you have your design going. You can like comment, you can circle things, and there's no reason you can't do that in a plan, right? I was like, "Oh, how would you interact with this?" And it's like, "Oh, just build an arbitrary like comment thing into it and say people are going to leave comments on any aspect of this."

**30:43** · And when they do and then they submit like fix it fixes the core thing. And so I think people getting really creative with what interaction models you can do between content Yes.

**30:55** · and code.

**30:55** · Yeah.

**30:56** · Is really fun.

**30:57** · Yes.

**30:57** · Yeah. I mean you could easily imagine that you did this plan as like a like almost a lightweight Figma dashboard or something where you just ask it to like hey make a canvas make a bunch of things. let me comment on it and then give me a place to copy out my comments into something that I can paste back into cloud code.

**31:15** · Yeah.

**31:15** · And we did an episode recently um with the Stripe team and they built their own vibe coding platform and they said what they loved about it which I think really applies here is they have just a particular way they want to review products and they have a particular way they want to run design review and a particular way they want to run spec review and by building it in HTML they can actually shape the tool to how they want the team to run which I think is really compelling to people.

### Podsumowanie: Przepływ pracy w HTML

**31:42** · Yes, I love this. So, just to wrap for people, pull up Cloud Code, ask it to make you give you some ideas. Brainstorm ideas, but brainstorm them in HTML. That's right.

**31:54** · Pick an idea. Yep.

**31:55** · Plan it in HTML. Pick a part of that idea you don't like, have it create a micro app to edit it in HTML, and then some like bonus things is use cloud design, make a design system, but not only that, use HTML to encode that design system in your repo so it can be referenced at any time.

**32:13** · design.mmd is dead. Long lived design.html. Did I get it right?

**32:18** · Yeah, I think that's right. I think that's right.

**32:20** · Throw it. I'm pretty good. Okay. Well, this was so fun. Before we get you out of here and back to this amazing event, couple lightning round questions. One, I have to I ask everybody there's three tabs in Claude desktop app.

### Krótkie podsumowanie i ostatnie przemyślenia

**32:34** · Yeah.

**32:34** · What is your favorite tab?

**32:36** · It's got to be code, you know. Yeah. Yeah. I love the team as well. I'm really close friends with them. So, yeah.

**32:41** · Okay.

**32:41** · So, so, so code that I I thought it would be on brand. Okay. Second thing, we were at this amazing event.

**32:46** · What is the thing that you're most excited about or that you saw or heard today?

**32:49** · I think obviously we had a big announcement at the start of the day, uh, our partnership with SpaceX, bringing more compute online. I think, uh, yeah, I'm excited for, you know, we also said we are thinking about orbital data centers and that's just I love it.

**33:04** · Yeah.

**33:04** · You know, incredibly sci-fi and but could, you know, it could actually happen. So yeah, I know. We were watching this moon mission with my kids who are like kind of elementary school and I'm like, would you want to work in the moon? Would you want to work in the moon mines? Cuz I think it's coming. Yeah. Orbital.

**33:21** · Orbital. That's That'll be next year's demo, right? You and I will come back and we'll do this. We'll do HTML. We'll do testing and then lunar data model modules.

**33:31** · That's right.

**33:32** · Perfect. Okay. And then my last question, very important. I love that you just talked to CL Claude like a person.

**33:37** · Yeah. When Claude is not listening, not giving you what you want.

**33:42** · Yeah.

**33:43** · What's your prompting technique? Do you yell? No one in anthropic yells. That has been my experience so far. So, you'd be the first to admit it.

**33:49** · Yeah.

**33:49** · Yeah. No, I I definitely don't. Um I think that like there are a couple things here. I I do sometimes message people and I'm like, "Hey, like seems like you have a bug. Can you send me your transcript?" And they're like, "That's not the best side of me." Yeah. Yeah. You know, um I think that like Yeah. I don't I I don't yell at Claude.

**34:06** · I think that like we've also done some interesting research recently about like emotions in in in Claude and just sort of like this idea that like once you when you say things with a certain emotional charge, it also like activates different features inside of Cloud Code.

**34:19** · I don't think anyone's done this like AB test of like which like you know if you're mean to Claude, does it better than without it or not? But I'm just like, let's airer on the side of like, you know, just not or like what's the thing I'd prefer to exist, you know, and I'd prefer if you're like nice and, you know, friendly to Claude that you got better output. So, all I've seen is if you sort of border on stern to any of these models, their reasoning gets really sad. It's like, oh, the the user is right to be so disappointed in me. I'm like, oh, I don't want I don't want to read that. I don't want to see that.

**34:51** · Yeah, thinking traces are tough. I I usually give the model some privacy. I'm like, I'm not going to read the none of your business. Yeah, I had somebody else on. I feel like it was Hillary who was like, "Just like an employee. How do you get your work done is none of my business. I don't even want to know. We just collapse those things." Well, this has been so fun. Thank you for showing us the way. Where can we find you and how can we be helpful?

**35:12** · Uh extremely online at X. Yeah, I'm uh tr12 and uh yeah, just tag me if you have, you know, anything with cloud code. I'm happy to help.

**35:21** · Perfect. I am living proof. This this man is happy to help. Well, thank you for joining how I Thank you. Thanks for having me.

**35:30** · Thanks so much for watching. If you enjoyed this show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your \[music\] favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you \[music\] next time.
