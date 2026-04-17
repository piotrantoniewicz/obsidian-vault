---
type: Web
authors: '[[Claire Vo]]'
url: >-
  https://www.chatprd.ai/how-i-ai/jj-englerts-guide-to-a-daily-operating-system-with-claude-cowork
published: 2026-04-13T00:00:00.000Z
created: 2026-04-13T00:00:00.000Z
tags:
  - strategia-AI
  - narzędzia-AI
  - automatyzacja
---


![How I AI: JJ Englert's Guide to a 'Daily Operating System' with Claude Cowork](https://www.chatprd.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fng65ow1q%2Fproduction%2F7ecadd6947775e36fe803ead35deb722ad555a19-960x540.png&w=3840&q=75)

When [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork) first launched, I was a bit of a skeptic. I even wrote a [tweet](https://x.com/clairevo/status/2010835704931369379) about it that got some attention, asking who this tool was really for. It seemed stuck in a strange middle ground between a simple chatbot and the full power of a terminal-based tool like [Claude Code](https://claude.ai/code). It felt like a UI slapped on top of code, and I wasn't sure who the target user was.

Well, I’m happy to say that the Anthropic team has been cooking. Week after week, the product has evolved, and I kept hearing from my non-technical friends how Cowork was becoming indispensable to their daily jobs. The UI has improved, the capabilities have expanded, and it’s become a seriously powerful tool for getting things done. That’s why I was so excited to have [JJ Englert](https://www.linkedin.com/in/jj-englert-a08836a6/) on the show. As a Community Enablement Lead at [Tenex](https://www.youtube.com/channel/UCv2ovDhYVtlJw4QMidLFP8Q), he's a true power user who has mastered the art of using Cowork as a central hub for his professional life.

In this episode, JJ walks us through the complete zero-to-one process of setting up a 'Daily Operating System' in Cowork. He showed me how to move beyond simple chat prompts and build a connected system of skills, agents, and automated tasks that work for you. We cover everything from creating a foundational 'brain' file to building personalized writing skills and even setting up a multi-persona 'sub-advisory board' for instant feedback. This is your guide to making Cowork actually *do work* for you.

## Workflow 1: Building Your 'Daily Operating System' Project

The biggest mental leap from using a standard chatbot to using Cowork is the concept of a 'Project.' It’s the foundation for everything else we’re going to build. A project isn't some complex developer concept; as JJ explains, it's just a folder on your computer that acts as a dedicated workspace for a specific goal. This allows Cowork to have persistent context and memory for everything related to that goal.

### Step 1: Create Your Project Folder

First things first, you need a home for your project. Simply go to your computer's file system and create a new, empty folder. For this demo, JJ created a folder named `Daily Operating System`.

> "This is the start of everything, and then it's an empty folder. Now I'm gonna go back into Cowork here, and I'm going to load up this folder." - JJ Englert

### Step 2: Establish Your 'Brain' File

This is a brilliant strategy from JJ. Inside your project folder, you create a simple markdown file, maybe called `brain.md`, that acts as your personal instruction manual for Cowork. This file contains all your working preferences, the team members you frequently interact with, your communication style, and any other standing instructions. Every time you work within this project, Cowork reads this file to get up to speed on who you are and how you like to work.

\>"My brain goes into very detail of like, what are my working preferences? Who are the team members that I work with?... This is a very specific series of instructions that we, you know, also known as a prompt that Claude can read to get up to speed very quickly of who you are, how you like to work." - JJ Englert

### Step 3: Connect the Folder to a Cowork Project

Back in the Claude Desktop app, you navigate to the 'Projects' tab and create a new project from an existing folder. Select the `Daily Operating System` folder you just made. You’ll also give the project high-level instructions that define its overall purpose. This connects the physical folder on your computer to the persistent, memory-enabled project workspace inside Cowork.

`I'm gonna use this folder and operating system to help me navigate the day-to-day life of a busy professional. You're gonna help me with some superpowers by applying some AI magic to it all.`

![The Cowork Project interface, showing the chat list, the 'Context' panel with folder and memory, and the 'Instructions' panel](https://cdn.sanity.io/images/ng65ow1q/production/c4e1917e6a6d44236fd182089cdeb3c9a55dee7d-1920x1080.jpg)

The Cowork Project interface, showing the chat list, the 'Context' panel with folder and memory, and the 'Instructions' panel

Once this is set up, you have a foundational workspace. All the tasks, skills, and memory you create within this project will be interconnected, allowing Cowork to build a deep understanding of your work over time.

## Workflow 2: Creating a Personalized Email Writing Skill

One of the most common complaints about AI-generated text is that it sounds robotic and generic. This workflow solves that by training Cowork on your own writing style to create emails that actually sound like you. The key is using Cowork's connectors to analyze your past work.

### Step 1: Enable Connectors

Connectors are the one-click integrations that give Cowork access to your other apps. JJ has his connected to [Gmail](https://www.google.com/gmail/), [Slack](https://slack.com/), [Notion](https://notion.so/), and Google Calendar. You can browse and add connectors easily, and for each one, you can configure specific permissions. For instance, you can allow Cowork to *read* your emails but require approval before it *sends* anything.

![The Connectors settings page, showing the list of enabled connectors like Gmail and Slack](https://cdn.sanity.io/images/ng65ow1q/production/724623ae63d6009dfa3a5359cf085920e4497e5b-1920x1080.jpg)

The Connectors settings page, showing the list of enabled connectors like Gmail and Slack

### Step 2: Prompt the Skill Creation

With the Gmail connector active, you can now ask Cowork to build a skill based on your writing. JJ used a simple voice prompt to kick this off. I love this because it’s not just drafting an email; it’s creating a reusable asset.

\>"Hey, analyze my Gmail specifically the emails that I have sent in the last 30 days, and use this to create a writing skill specifically for emails that I write using, uh, my emails as an example of my writing structure. So whenever I want you to write an email in the future, you know exactly how I write my emails, and you'll use this skill."

### Step 3: Review and Refine the Outcome

Cowork will go to work, accessing your Gmail via the connector, analyzing your sent messages, and then generating a detailed style guide and voice profile. It saves this as a skill within your project's memory. Now, any time you ask Cowork to draft an email in this project, it will automatically apply this skill, matching your tone, structure, and vocabulary.

![The chat window showing the confirmation that Cowork has created an 'email style guide' and 'voice profile'](https://cdn.sanity.io/images/ng65ow1q/production/3edc779c75c39cacf23b2e5ea95a109d73554bb2-1920x1080.jpg)

The chat window showing the confirmation that Cowork has created an 'email style guide' and 'voice profile'

To be safe, JJ adds a global instruction to his project: `never send emails on my behalf. Only write them as drafts for me to review.` This is a great example of setting clear boundaries and maintaining human oversight.

## Workflow 3: Building a 'Sub-Advisory Board' for Instant Feedback

This was one of my favorite takeaways from the episode. We all know how expensive and time-consuming it can be to get collaborative feedback, especially in a remote-first world. JJ's 'sub-advisory board' technique uses AI to create a virtual roundtable of reviewers, allowing you to pressure-test your work before sharing it with your team.

### Step 1: Define the Multi-Persona Review Agent

The idea is to create a skill that, when invoked, spins up several 'sub-agents'—each with its own unique persona and perspective. This avoids the single-minded feedback a normal chatbot might give you.

### Step 2: Prompt the Skill Creation

JJ prompts Cowork to build a 'review agent' skill. The key is to specify that this agent should launch its own sub-agents representing different viewpoints. This is a powerful pattern you can customize for any task.

\>"I want you to build another uh, skill, and this is gonna be a review agent. For this skill, you're gonna launch a series of subagents that have each their own persona. And this can differ per the task, but an example is if we're launching a newsletter, we want to have subagents that represent our ICP. Maybe for me it would be AI builders, AI executives, and AI interested people."

### Step 3: Apply the Skill to Your Work

Once the skill is created, you can apply it to anything you're working on. Writing a product requirements document (PRD)? Have it reviewed by sub-agents acting as your boss, an engineering lead, and a customer. Crafting a marketing email? Get feedback from three different Ideal Customer Profiles (ICPs). This gives you a rich, multi-faceted critique that helps you identify blind spots and improve the quality of your work dramatically.

I find this especially useful as a solo founder. It's tough to work in a vacuum, and having this on-demand feedback mechanism is like having an instant brainstorming session with a team of experts.

## Workflow 4: Automating Your Day with a Scheduled 'Morning Debrief'

This final workflow brings everything together, moving Cowork from a reactive tool to a proactive assistant. Instead of you having to ask for things, Cowork will prepare information for you on a schedule.

### Step 1: Create a Scheduled Task

Within your project, you can create a 'Scheduled Task.' This feature allows you to run a specific prompt on a recurring basis—hourly, daily, or weekly.

![The 'Create a scheduled task' interface, showing fields for name, schedule, and prompt](https://cdn.sanity.io/images/ng65ow1q/production/9e72595029e80d34e6068d92fdf522f77922e463-1920x1080.jpg)

The 'Create a scheduled task' interface, showing fields for name, schedule, and prompt

### Step 2: Write the Morning Debrief Prompt

JJ sets up a 'Morning Debrief' task to run every weekday at 7:30 AM. The prompt instructs Cowork to synthesize information from all his connected tools to prepare him for the day.

\>"I want you every single morning to look at my email, my Slack and my calendar, and check it to help organize a plan of action for the day. So that way when I get into the office, I'm aware of any kind of messages that need my attention. You can start preparing me for my day by looking through my calendar and looking through my events, and if I need any kind of meeting prep, helping me do that."

### Step 3: Let the Automation Work for You

Once saved, this task will run automatically. Every morning, JJ gets a consolidated plan of action that takes into account his emails, messages, and schedule. Because it runs within the 'Daily Operating System' project, it has all the context of his skills and preferences. This could be a debrief for a specific work project, or as I mentioned in the episode, it could be something personal—like a curated list of interesting news or a reminder to go for a walk.

\---

These workflows demonstrate a powerful progression: from organizing your context in a project, to building personalized skills, to finally automating proactive assistance. JJ’s approach shows that with a bit of setup, you can transform Cowork from a simple chat interface into a true digital partner that understands you and helps you get your most important work done. It's a great on-ramp to more advanced AI usage and teaches the foundational skills you'll need as these tools become even more capable.

If you’ve been sitting on the sidelines with Cowork, I hope this gives you the playbook you need to get started. Pick one small project—work-related or personal—and give it a try. The potential to offload cognitive overhead and streamline your day is immense.

### Thank You to Our Sponsors

- [**Tines**](https://www.tines.com/) —Start building intelligent workflows today
- [**Cursor**](https://www.cursor.com/) —The best way to code with AI

### Episode Links

- JJ's YouTube: [10x Builder](https://www.youtube.com/channel/UCv2ovDhYVtlJw4QMidLFP8Q)
- JJ on X: [@jjenglert](https://twitter.com/jjenglert)
- JJ on [LinkedIn](https://www.linkedin.com/in/jj-englert-a08836a6/)

**Tools Referenced:**

- [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork)
- [Claude Code](https://claude.ai/code)
- [Wispr Flow](https://whisperflow.ai/)
- [Monologue](https://www.monologue.to/)
- [Domo](https://www.domo.com/)
- [Pencil.dev](https://pencil.dev/)
- [Remotion](https://www.remotion.dev/)
- [Obsidian](https://obsidian.md/)
- [OpenClaw](https://openclaw.com/)
- [Notion](https://notion.so/)

**Other References:**

- [Hilary's "Plan My Day" episode](https://www.lennysnewsletter.com/p/how-to-turn-claude-code-into-your)
