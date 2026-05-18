---
type: Web
authors: '[[Grace Leung]]'
url: 'https://www.youtube.com/watch?v=yLXLHnD4fco'
published: 2026-03-28T00:00:00.000Z
created: 2026-05-08T00:00:00.000Z
tags:
  - automatyzacja
  - narzędzia-AI
  - content-marketing
---


![](https://www.youtube.com/watch?v=yLXLHnD4fco)

## Transcript

### What we’re covering today

**0:00** · Claude keeps getting succinctly powerful and unstoppable, and I really mean it as a claude power user.

**0:05** · So what if you could turn Claude into a full AI marketing team that research, writes, analyze and design all working together?

**0:13** · So in this video, I'll walk through step by step how to build this entire system from scratch, inside Claude Code, Even if you're not technical, let's go.

**0:23** · To design your first AI marketing team in Claude, follow these four step.

### Design Your AI Marketing Team

**0:27** · Step one, map your marketing function, what marketing tasks you actually do every week.

**0:32** · Step two, turn each repeatable into a skill, ideally one skill per workflow.

**0:38** · Step three, group similar skills into non-overlapping agent roles.

**0:43** · So you have dedicated and focused agent that produce better work.

**0:47** · Step four, connect agents and skills as a team, set up your project, so Claude knows who is on a team and when to use agents versus skills.

**0:56** · So today we are building exactly that for a travel brand called Go Travel, five Agents, 12 Skills.

**1:02** · And we are using Claude Code to build a whole thing.

### Popular Ways to use Claude Code

**1:05** · Of course, it might look different for your brand depending on your marketing focus, but same concept apply.

**1:11** · For now there are three popular ways to use cloud code.

**1:13** · Cloud code desktop, where you just switch to Claude code from the tab, an IDE like VS code or cursor or a terminal, which gives you the full power.

**1:21** · So for this video, I'll be using VS code so we can see the files and folders side by side.

**1:27** · So first download vs code and then on VS code go to extension, search for cloud code and install the one by Anthropic official.

### Install Claude Code (VS Code)

**1:36** · So once installed, click the Claude icon in your sidebar, log in with your Claude plan account.

**1:42** · It will open your browser for login in and you'll be good to go.

**1:45** · All right, so I already set up the brand folder called Go Travel.

### Project Folder Setup

**1:49** · And inside you can see we have got folders for different departments like sales ops and marketing.

**1:55** · So think of it like how a real business organized their work.

**1:58** · But today we are focused on the marketing folder.

**2:01** · So inside we'll set up two types of folder.

**2:03** · So one I call the system folders like context, SOP templates.

**2:08** · Those are reusable by your AI agents.

**2:11** · And then the working folders, like Ads, pages, presentations.

**2:15** · So when your agents produce work, everything goes here.

**2:19** · Now a really important step is we need to first load some context inside the context folder, like your brand voice guide, style guide, product offerings, marketing strategy.

**2:29** · So your agents are pre equipped things about your brand and it will make the whole difference.

**2:34** · So other useful file, like the templates or SOPs.

**2:37** · By the way, this is what we're covering in our AI growth system for marketing program inside our community, where you'll get all the templates and we go much deeper.

**2:45** · So if you're interested, you can find the link below to join.

**2:48** · Now open the project folder on VS Code.

**2:50** · The very first step is to initial this project by creating the Claude MD file.

**2:56** · So this is basically the custom instructions for your entire project, and you can let Claude to scan your folder and draft it for you.

**3:03** · And immediately, we have this CLAUDE.md file created, but note, we will keep updating this file.

**3:10** · So it is not like a one off process.

**3:13** · Now another thing is to install the official scale.

**3:15** · So these are the prebuilt Skills by anthropic, so you can use right away for your project.

**3:21** · So first type the slash command plugin.

**3:23** · We are gonna first add the official skills GitHub repository marketplace, and then go back to plugin search for document skills and click install.

**3:32** · Now if you type the slash command and see all those scales, and that means you have successfully installed official skills pack.

**3:39** · All right, let's build our first marketing team branded deck skills that every marketer needs.

### Build Skill 1: Branded Deck Skill

**3:44** · And for this one, we'll use what I call the reference based method.

**3:48** · So you give Claude examples or templates of what goods look like And it studies the patterns Now to build a great deck creation skill that really follows your branded template.

**3:57** · You need two things.

**3:59** · First is the branded deck template and a detailed understanding of how that template works.

**4:04** · So inside the templates folder, we already have an existing deck template.

**4:08** · So this is the style that we want Claude to follow exactly.

**4:11** · Then have clause analyze this template first and to generate the analysis report.

**4:16** · So it will come back with a really detailed analysis.

**4:19** · Now we are ready to create our first skill.

**4:21** · So we will ask it to extend the official PowerPoint creation skill and generate a new branded deck skill based on the template and analysis report.

**4:29** · And immediately we have our first skill.

**4:31** · So Claude creates a new folder, called "Skills", and underneath we have the branded deck scale containing the assets and references.

**4:39** · Now, whenever we want to create on-branded slide decks, we can just give it some background information and let Claude to create.

**4:46** · So in this case, we wanted to create a campaign strategy deck for an upcoming summer campaign.

**4:51** · So it will call the skill we just created and return a slide deck with 13 slide.

**4:56** · And you can see it is following exactly the same brand presentation template we just see.

**5:01** · Although some slides still need to fix like the margin, the charts, it is 90% done.

**5:07** · And using this method, you can include all the templates as well.

**5:11** · Perhaps one for strategy deck, one for client reporting, one for product launches, and Claude will follow exactly that.

**5:18** · Now that you build your first skills, but there are so many other marketing use cases, you could turn into skills.

**5:23** · So if you want more ideas on what to build next, then this resource I put together with HubSpot is exactly what you need.

**5:30** · It's called the AI toolkit I use every week.

**5:33** · I made this because most of us are either juggling too many tools with no real system or stuck using one tool for everything.

**5:41** · It covers my favorite use cases across popular AI tools like Claude, ChatGPT, Gemini, and Perplexity.

**5:48** · Based on my personal experience working with these tools, and when I use one tool over the other For Claude, you'll see how I use it for things like strategy, brainstorming, data visualization, content repurposing, and honestly, any of these could become the next skill you build in your own setup.

**6:05** · You can use them as a starting point, then adapt for your own market needs.

**6:09** · So grab it for free in the description.

**6:11** · Thank HubSpot for partnering with me on this resource and for sponsoring this video.

### Build Skill 2: Social Creative Designer

**6:15** · All right, so that was one way to create a scale using brand templates and references.

**6:20** · Now, this time, we are going to create a scale that connects to an external MCP tool for inmate generation.

**6:26** · We are going to create our social creative design skill.

**6:29** · So first, set up your creative style library.

**6:31** · Under the templates folder.

**6:33** · Create a sub folder called social creatives and then include all those on branded templates.

**6:38** · So these serve as visual inspiration for Claude and not the exact copy.

**6:43** · Then we also have the style guide, so Claude knows what style are available and when to use them.

**6:49** · Now since the skill used the nano banana model to generate images.

**6:53** · So we also need to set up the MCP connection first.

**6:56** · The most reliable way I found in VS Code is to create a .mcp.json file in your project root folder.

**7:04** · So simply this file tells Claude which external tools it can connect to for this project.

**7:11** · We will add the nano banana MCP server with the Gemini API key.

**7:15** · I will also include the GitHub repository link below so you can check it out.

**7:19** · Then restart VS Code type slash command MCP.

**7:22** · So you should see all your connected MCP servers for this project.

**7:26** · So now we are ready to create a second skill.

**7:28** · So this skill will design and create carousel or single social creative using the nano banana model.

**7:34** · So now it is scanning the style library we just create, and then pretty quickly we have our second skill created in the same skill folder.

**7:41** · So now whenever we need some social creatives, we can just give it a simple prompt like this and let it generate.

**7:47** · So like in this case, it is a five slide Instagram carousel and they are really nicely done.

**7:53** · So following one of the style from the library, and not just copying the design, but just the vibe.

**7:58** · And that is why setting up references matters so much for your skill output quality.

### Marketing Skills Library + Why moving beyond Skills?

**8:03** · So using similar methods, we have created 12 marketing skills in our skill library.

**8:08** · But the more skills you pile into one conversation, the less focused cloud become.

**8:13** · Just like one person trying to be your writer, analyst, and designer all at once.

**8:18** · And that is when you need dedicated agents or what the official call the sub-agents.

**8:23** · So agents are specialized team members with their own roles and tools, and then skills are the shared playbook your agents can use.

**8:31** · So let's build, our first agent a data analysts.

### Build Agent 1: Data Analyst

**8:34** · This is a great one to start with because it thinks completely different from the content skills we just built.

**8:40** · So to create our first custom agent, we have to use the built-in agent command inside the Claude code terminal.

**8:46** · So first type slash agents, and then click continue in terminal.

**8:51** · So where it will bring up the terminal view.

**8:53** · So here, click Create New Agents.

**8:55** · Then click for this project only, and let Claude to generate the Agent MD file for you.

**9:01** · And then tells it about what you want this agent to do.

**9:04** · So in this case, we want to create an agent called data analyst and what skill it should use and then pick the tools, the default model, color and agent memory, location.

**9:14** · And then immediately we create our first agent for this project.

**9:18** · And what it really does is you can see there is a new Agents folder.

**9:21** · And underneath we see there is a data analyst Agent markdown file, and there is a file defining the agent's role, its skills, and a core responsibility.

**9:31** · Now let's say we have this campaign data set for this project, so it contains eight different types of data sets.

**9:37** · Now, to use this agent, we can just use the @ tag and call this agent and ask it to create the campaign report and the performance dashboard that is ready to present.

**9:47** · So this agent will call the campaign report and data Visualization skill.

**9:51** · So for the campaign report, it looks quite comprehensive with all the channel performance breakdown summary and the analysis synthesized from all those dataset.

**9:59** · As for the data dashboard, summarizing the top line metrics with key takeaways, charts and diagrams that visualize different channel performance.

**10:07** · Week on week revenue trend and everything is interactive where you can hover or select.

**10:12** · So basically you can see this as a on-branded template.

**10:15** · And let Claude to update this tracker whenever there's a new campaign data.

**10:20** · And this will be an other huge time saver.

**10:22** · So our data analyst agents thinks in numbers, charts, and patterns.

### Build Agent 2: Content Creator

**10:27** · Now let's build another agent for content creation that thinks in stories and headlines.

**10:32** · Again, use the slash command agents to trigger the terminal view and use this prompt to create this content creator agent.

**10:39** · And so this agent, will produce marketing content across multiple formats and equip with the four content creation skills we just created.

**10:47** · And immediately we create this second agent.

**10:50** · Now we can just tag this content creator agent in a chat.

**10:53** · Ask it for a relevant task.

**10:55** · So in this case we want a blog post for an upcoming campaign that will also link to a lead magnet.

**11:00** · So Claude now delegate task to this agent, which it would call the blog writer skills for the blog creations that use the keyword research tool and then also use the lead magnet skills to generate the pdf guidebook so the blog post is following the structure we define with the table of content, bullet points and structure that is optimized for AI search.

**11:20** · And here it even added the link to our lead magnet resource guide.

**11:24** · So this resource guide contain 11 pages designed in a brand color tone.

**11:29** · So the design is intentionally simple to keep the focus on the content value, But you can always tweak the skills for your needs.

**11:36** · So you can see how powerful Claude can be to create all kinds of marketing content that you need for your campaign.

### Agent Routing with CLAUDE.md

**11:42** · So using similar methods, we can build three more agents, the market researcher, creative designer, and a campaign strategist.

**11:50** · And each of them equip with their own set of skills we created earlier.

**11:54** · But before running the AI marketing team, an important step is to update the CLAUDE.md file to add agent routing routes.

**12:01** · So Claude knows explicitly when to dedicate to this agent and it will make your system much more reliable.

**12:07** · All right, this is exciting time as we are gonna give our marketing team a complex task and see how they can work together on its own.

### Team Orchestration

**12:14** · For example, we are launching a new Japan Cherry Blossom season campaign, and we need a full marketing package from research campaign brief social posts of a landing page and ad creatives, since this is a complex task.

**12:28** · So you can see Claude will decide which step it needs, the agents versus using skill only.

**12:34** · So that is because we have add the rules in the CLAUDE.md file.

**12:38** · So not every step requires the use of agent, like research and campaign that requires synthesizing an agent can be beneficial, but for content creation that is really executional and straightforward skill should be enough.

**12:50** · So first is it's calling a research tool for market research.

**12:53** · And it moves on to campaign brief once finished and then generating images and building the landing page.

**13:00** · And after like 10 minutes, it got all the deliverables ready.

**13:03** · So first we got the market research.

**13:05** · This is perfectly done, including the target audience we should target.

**13:09** · And then it also translate to our campaign brief with more executional details like the messaging where it proposed the tagline, "Sakura like a Local", and then the social post for the campaign with all those trending conversation it have identified.

**13:25** · And finally, the creative.

**13:26** · So you can see they're all tied back to the same campaign theme, and particularly I like the last one.

**13:32** · Now for the offer landing page, it is also quite impressive.

**13:35** · So this is done using the landing page builder scale.

**13:38** · Everything is on the brand tone, aligned with a campaign theme, the images, style, all look professional with all important sections and call to action.

**13:48** · So even for complex tasks like this Claude can keep all the deliverables connected.

### Notion Task Board for Team Collaboration

**13:53** · Now we've built our first AI marketing team.

**13:55** · We have seen them work together on complex campaigns, but in real world, you also need to work with your real teammates too.

**14:01** · So let me show you how to set up a shared task board on Notion, where anyone on your team can drop a task and your AI agents can pick it up and get it done.

**14:11** · So here we have a simple Kanban board that tracks all the marketing tasks for the team.

**14:15** · So each task we have a priority, the task title and details and all pending tasks with the status of "To-Do".

**14:22** · And once they're done, they will be moved that to the complete status.

**14:25** · Now, the magic happens when we let the Claude agents to pick up these tasks.

**14:30** · By the way, shout out to David, a great marketer in my network who actually gave me this idea.

**14:35** · So on Claude we can use this prompt to ask it to scan the pending task on this notion board and assign an agent to do it and execute them according to priority.

**14:45** · So like this case, it will pick up the Europe campaign launch task and then according to tools to execute the research and design the carousel posts.

**14:53** · So you can see Claude updated tasks to complete status once done and include all the output file paths.

**14:58** · And we can double check all the results.

**15:00** · So the research is being done successfully as well as the set of carousel posts with a total seven slide that are informed by the research findings, which is also nicely done.

**15:10** · So that means now you can set up this task board, collaborate with the team, and let the AI agents to execute it.

**15:16** · But we can take it even further.

### Remote Control Team

**15:18** · You can actually talk to your AI team from your phone.

**15:20** · So claude code now lets you connect your mobile device to your local running session, so you can send tasks to your AI team from the cloud mobile app anywhere, even when you're away from your desk.

**15:32** · And if you’re familiar with the Dispatch function from Claude Cowork, they are essentially the same thing.

**15:38** · So for any conversation you want to connect remotely, we have to first activate the remote control.

**15:43** · So type the slash command remote control in the chat and you will see it now says remote control connected and with a remote control link.

**15:51** · So this is the link you will open in your mobile phone to chat with your agents, but don't share this link to anyone since it will give the full control of your session.

**16:00** · So once you open it, you immediately connect with your local Claude code session and now we can communicate with the team remotely.

**16:07** · So for example, I can just type check the task board and it will trigger the skills I have already set up and grab any pending task on notion and execute it as normal.

**16:16** · So basically everything you sent through your phone is immediately sync to your local Claude code session.

**16:22** · So for this case, it has identified the new task about building a landing page for a new campaign and get it done.

**16:28** · But the limitations for now is you can rely on this one single connected session for any task.

**16:34** · So if the context become full, you can type clear conversation to clear the context where you can start the chat again.

**16:41** · And whenever you want to disconnect, just click the three dots here and click archive.

**16:46** · And all the works are just saved locally, even if you are away.

**16:49** · So imagine you might have some urgent tasks.

**16:52** · You want your AI agent team to execute for you.

**16:54** · It can be useful and it really feels like a 24 7 teammate that works for you and get the work done.

**17:00** · So try this yourself and build your AI agent team.

**17:03** · If you find this video helpful, please give a thumbs up.

**17:06** · I really appreciate that.

**17:07** · I also invite you to join our growth community.

**17:10** · We are running the AI system for marketing program where we go much deeper from context, setup, research, workflow, all the way to building a complete system.

**17:19** · You can find the link below to join.

**17:21** · I hope to see you there and join all the AI native marketers.

**17:24** · And before you go, also watch this video if you want to get started with Cloud Skill first for building your marketing team.

**17:31** · I'll see you next time.
