---
type: Web
authors: "[[Iseunife The First]]"
url: 'https://x.com/Shawnife/status/2027652088163922184'
published: 2026-02-28T00:00:00.000Z
created: 2026-03-07T00:00:00.000Z
tags:
  - narzędzia-AI
  - strategia-AI
  - automatyzacja
---


Last week I was in Nairobi preparing for a talk. I had the ideas, the research, and a rough outline in my head. What I did not have was time. So I opened Claude Cowork, described the presentation I needed, pointed it at my notes folder, and stepped away.

I came back to a fully structured slide deck, with sections, speaker notes, and a flow that actually made sense for the audience I was presenting to. That presentation went down really well. People were genuinely wowed. And the honest truth is that it would have taken me most of a day to build that from scratch the traditional way.

That was the moment it clicked for me. Not what Cowork could theoretically do, but what it actually delivered when I needed it under real pressure.

I have been in AI and product long enough to spot when something is genuinely different versus when something is just marketed as different. Cowork is unique. It is not a chatbot with extra features. It is a completely different category of tool, and most people who have heard of it still do not fully understand what it actually does or how to get the most out of it.

That is what this guide is for.

Most people who use Claude use it as a chatbot. You type a question, it gives you an answer, you copy the answer somewhere and go do the actual work yourself. That is useful. But that is not what Claude Cowork is.

Cowork does not answer questions. It does the work. It reads your files, makes a plan, executes the steps, and delivers finished outputs directly to your computer while you step away. Picture the difference between asking a colleague for advice and actually handing them the task. Cowork is the second one.

What surprised me most when I first used it properly was not just the speed. It was how comprehensive the output was. It did not give me a starting point to build from. It gave me something close to finished. That combination of speed and depth is what makes it feel genuinely different from anything else I have used.

This guide covers everything from setup to plugins to use cases to prompting. By the end, you will have a complete picture of what Cowork can do and exactly how to make it work for you.

## What Is Claude Cowork, Really?

Before getting into setup and use cases, it helps to understand what kind of tool Cowork actually is, because it is a different category from what most people are used to.

The difference between a chatbot and an agent

When you use regular Claude, ChatGPT, or any standard AI chatbot, the interaction looks like this:

- You type something
- The AI responds with text
- You read the text and decide what to do with it
- You go do the actual task yourself

This is called a conversational AI or a chat interface. It is helpful but you are still the one doing the work. The AI is your advisor.

Cowork is what is called an **agentic AI**. The interaction looks completely different:

- You describe an outcome you want
- Cowork makes a plan and shows it to you
- You approve the plan
- Cowork executes every step on its own, working directly with your files
- You come back to finished work

The AI is no longer your advisor. It is your executor. You become the director instead of the doer.

**Where Cowork came from**

Cowork was built by Anthropic using the same technology that powers Claude Code, which is Anthropic's tool for software developers. Claude Code lets developers hand off complex coding tasks to an AI agent that writes, tests, and edits code autonomously.

Cowork is essentially Claude Code for everyone who is not a developer. It applies that same autonomous, multi-step execution to everyday knowledge work: documents, spreadsheets, research, presentations, file organization, email drafts, reports, and more.

## How Cowork runs on your computer

Cowork lives inside the Claude Desktop app, not the web version. It runs directly on your device, in a folder you choose and give it access to. Your files never leave your computer to be stored somewhere else. Claude reads them locally, does its work in an isolated virtual machine on your device, and writes the outputs back to your folder.

You control what it can see. You pick the folder. You approve actions before they happen. And for anything that could delete or permanently change files, it asks for your explicit permission before proceeding.

## What You Need to Get Started

Requirements

- **The Claude Desktop app** for macOS or Windows (not the web version at [claude.ai](https://claude.ai/))
- **A paid Claude subscription**: Pro ($20/month), Max ($100 to $200/month), Team ($30/user/month), or Enterprise
- **An active internet connection** throughout your session
- **The latest version of the app** (Cowork requires the most recent update)

A note on Windows: Cowork launched on Windows on February 10, 2026 with full feature parity with macOS. Windows ARM64 is not currently supported.

A note on usage: Cowork uses significantly more of your usage allocation than regular chat because it is running complex, multi-step tasks. A single involved Cowork session can consume what would normally be dozens of regular conversations. This is worth knowing before you start, especially on the Pro plan.

## Step-by-Step Setup Guide

- Step 1: Download and install the Claude Desktop app

Go to [claude.com/download](https://claude.com/download) and download the Claude Desktop app for your operating system. If you already have it installed, make sure it is updated to the latest version. Cowork will not appear on older versions.

- Step 2: Sign in with your paid account

Open the app and sign in. You need to be on a paid plan. Free accounts do not have access to Cowork.

- Step 3: Find the Cowork tab

At the top of the Claude app window, you will see tabs. Look for **Chat**, **Cowork**, and possibly **Code**. Click the **Cowork**tab to switch into the Cowork workspace. If you do not see it, check that your app is fully updated.

- Step 4: Set up your workspace folder

This is the most important setup step. Cowork works inside a folder you choose on your computer. It can read, edit, create, and organize files within that folder.

**Best practice:** Do not point Cowork at your entire Documents folder or desktop. Create a dedicated folder specifically for Claude to work in, for example a folder called "Claude Work" or "Cowork Projects." You can create subfolders inside it for different projects. This keeps things organized and limits what the AI has access to.

To add your folder, click **Add Folder** and select the folder you want Claude to work in.

- Step 5: Give your first task

Once your folder is set up, you are ready to give Cowork a task. Type a clear description of what you want done in plain language. You do not need to write code or use special commands. Just describe the outcome you want.

A good first task is something low stakes so you can see how Cowork works without worrying about anything going wrong. For example:

1. "Organize the files in this folder by type and create subfolders for documents, images, and spreadsheets"
2. "Look at these meeting notes files and create a summary document that pulls out all the action items"
- Step 6: Review the plan and let it run

After you submit your task, Cowork will show you its plan before doing anything. Read it. If it looks right, let it run. If something seems off, you can adjust or clarify before it starts.

While Cowork is running, you can see its progress in real time on the right side of the screen. It shows you what it is doing at each step. You can watch it, or step away and come back when it is done.

The app must stay open while Cowork is working. If you close it, your session will end.

## Understanding Plugins: What They Are and Why They Matter

Plugins are one of the most powerful features in Cowork. Once you understand them, you start to see why Cowork is not just a productivity tool but a genuine shift in how entire departments can work.

**What a plugin actually is**

A plugin is a pre-built package that turns Claude into a specialist for a specific job or workflow. Instead of starting from scratch every time, a plugin bundles together:

- **Skills**: specific things Claude knows how to do for that role
- **Slash commands**: shortcuts that launch pre-built workflows with a simple command
- **Connectors**: connections to the tools you already use (Google Drive, Slack, Salesforce, etc.)
- **Sub-agents**: smaller specialized agents that handle specific parts of a task

When you install a finance plugin, for example, Claude does not just become slightly better at finance tasks. It becomes configured specifically for financial work, with the right terminology, the right workflow structure, and the right connections to financial tools.

Without a plugin, asking Cowork to help with investment banking work is like asking a smart generalist. It will do okay. With the investment banking plugin installed, Claude understands how to review transaction documents, analyze comparable companies, and format pitch materials the way people in that field actually do it. The output quality and the accuracy of the workflow both improve significantly.

## How to Install and Use Plugins

Installing a plugin

1. Open the Claude Desktop app and switch to the **Cowork** tab
2. Click the **Customize** menu in the left sidebar
3. Click **Browse plugins** to open the plugin library
4. Find the plugin you want and click **Install**
5. The plugin is now saved locally on your machine and ready to use

You can also upload a custom plugin file if you have built one yourself or received one from a colleague. Plugins are portable files, so they can be shared directly between team members.

**Using a plugin once installed**

After installation, your plugin adds commands you can use inside Cowork. To access them:

- Type **/** in the task input or click the **+** button
- You will see a list of available commands from all your installed plugins
- Click a command to open a structured form
- Fill in the details and click to run

For example, if you have the marketing plugin installed and you type /content-brief, a form will pop up asking for details like the topic, audience, tone, and length. Fill it in and Claude handles the rest. This structured approach makes complex workflows feel as simple as filling out a short form.

**Customizing a plugin**

Every plugin can be tailored to fit your specific workflow:

1. While viewing an installed plugin, click **Customize** in the upper right corner
2. This opens a Cowork task where Claude walks you through adjusting the plugin
3. You can change the skills, tweak the commands, and update which connectors it uses
4. Claude asks you questions to understand your preferences and adjusts the plugin accordingly

**Building a custom plugin from scratch**

If none of the existing plugins fit your workflow, you can build your own using the **Plugin Create** tool, which is itself a built-in plugin in Cowork. It walks you through the process step by step. You can also start from one of Anthropic's published templates on GitHub and modify it to suit your needs.

## The Full List of Available Plugins

General productivity and business plugins (available to all paid users)

These were part of the original launch:

- **Productivity**: Manages tasks, calendars, workflows, and personal context. Good for anyone who wants a general assistant to handle scheduling, task tracking, and daily workflow management
- **Enterprise search**: Finds information across your company tools and documents. Useful when you need to pull together information scattered across different systems
- **Marketing**: Drafts content, plans campaigns, manages launches, and handles content calendars. Covers everything from social posts to full campaign briefs
- **Sales**: Researches prospects, prepares deal materials, and helps follow sales processes. Useful for account executives and business development teams
- **Finance**: Handles market and competitor research, financial modeling tasks, and analysis reports
- **Legal**: Reviews documents, drafts contracts, and summarizes legal material. This plugin was significant enough that when it launched, shares of legal software companies dropped sharply
- **Data analysis**: Processes datasets, identifies patterns, and builds reports from raw data
- **Customer support**: Handles support ticket drafting, knowledge base management, and response templates
- **Engineering**: Writes standup summaries, coordinates incident response, builds deploy checklists, and drafts postmortems
- **Research**: Synthesizes information from multiple sources into structured reports and summaries
- **Recruiting**: Helps with sourcing, candidate outreach, and evaluation workflows

**Department-specific enterprise plugins (added February 24, 2026)**

These more specialized plugins were designed with practitioners in each field:

- **HR**: Generates customized job descriptions, offer letters, onboarding materials, performance summaries, and compensation analyses. Covers the full employee lifecycle
- **Design**: Generates critique frameworks, drafts UX copy, runs accessibility audits, and structures user research plans. Built for designers who spend time on documentation and briefs alongside the creative work
- **Investment banking**: Reviews transaction documents, analyzes comparable companies, and prepares pitch materials. Built with investment banking workflows in mind
- **Equity research**: Parses earnings transcripts, updates financial models, and drafts research notes
- **Private equity**: Reviews and extracts financial data from large document sets, models scenarios, and scores opportunities against investment criteria
- **Wealth management**: Analyzes investment portfolios and generates asset rebalancing recommendations customized to a firm's voice and approach
- **Operations**: Manages process documentation, vendor evaluations, change request tracking, and runbook creation. Useful for operations teams handling complex logistics and process management

## The Full List of Available Connectors

Connectors are the links between Cowork and the tools you already use. They allow Claude to pull data from, and act within, your existing software without you having to copy and paste information between apps.

Communication and collaboration

- **Gmail**: Read, draft, and send emails
- **Google Calendar**: View, create, and update calendar events
- **Slack**: Send messages, read channel updates, surface relevant conversations
- **Google Drive**: Access and edit documents, spreadsheets, and presentations stored in Drive

Sales and marketing

- **Apollo**: Prospect research and contact data
- **Clay**: Data enrichment and workflow automation for sales teams
- **Outreach**: Sales engagement platform integration
- **SimilarWeb**: Competitor web traffic and market research data
- **WordPress**: Draft, edit, and publish content directly to WordPress sites

Finance and legal

- **FactSet**: Financial data and analytics
- **MSCI**: Investment research and risk analytics
- **LegalZoom**: Legal document creation and review
- **Harvey**: AI-powered legal research and drafting
- **DocuSign**: Send, track, and manage documents for signature

Developer tools

- **GitHub**: Access repositories, review pull requests, and manage code-related documentation (available through MCP)

Additional integrations (available through MCP)

The Model Context Protocol (MCP) is the underlying standard that makes connectors work, and it is open, meaning the ecosystem continues to grow. Earlier MCP integrations that are also available include Zapier, Atlassian (Jira and Confluence), PayPal, Asana, and Snowflake.

## What Cowork Actually Does in Practice

Here is where things get concrete. These are genuine use cases, organized by the type of work involved.

1. Document and file work
- **Organizing a chaotic folder** You point Cowork at a messy folder, possibly your Downloads folder or a shared project drive, and tell it to organize everything. Cowork does not just sort by file type. It reads the contents of documents and organizes them semantically. A PDF that is an invoice goes into an Accounting folder. A PDF that is a contract goes into Legal. Images get grouped by project or theme. File names get standardized to a format you specify. What would take you a full afternoon happens in minutes.
- **Processing receipts and expenses** Drop a folder of receipt screenshots, scanned PDFs, and bank statement exports and ask Cowork to create an expense report. It opens each file, reads the merchant name, date, amount, and category, categorizes expenses intelligently (an Uber charge becomes "Travel"), and builds a formatted Excel spreadsheet with totals and formulas. The file is ready to open and submit. One user reported this saved them a full afternoon every month.
- **Updating the same information across multiple documents** If your company details, pricing, or standard terms change and those details appear across dozens of proposals, contracts, or templates, Cowork can open every file, find the relevant sections, and update them consistently. This is the kind of task that takes hours to do carefully by hand and is prone to human error. Cowork handles it systematically.
- **Creating a branded slide deck from raw materials** Give Cowork access to a folder with brand assets, a content outline, data files, and existing presentation templates. Ask it to build a complete presentation. It pulls from all those sources, structures the slides, drops in relevant data, and applies consistent formatting. A financial analyst at one company used this to pull data from an Excel analysis and automatically generate a PowerPoint presentation without having to re-explain the underlying numbers, thanks to the new cross-app Excel to PowerPoint workflow introduced in February 2026.

2\. Research and analysis

- **Synthesizing research from multiple sources** If you have a folder with academic papers, interview transcripts, internal research notes, and competitor reports, you can ask Cowork to synthesize the key themes, compare findings across sources, and produce a structured report. It reads across all the files at once, identifies relationships, and assembles a coherent narrative. One well-known example: podcast host Lenny Rachitsky used Claude to analyze transcripts from 320 podcast episodes, extracting the 10 most important themes and 10 counterintuitive truths for product builders. That took 15 minutes.
- **Competitor research and pricing analysis** With the Claude in Chrome extension, you can ask Cowork to research five competitors, visit their websites, pull pricing and feature information, and combine that with your own internal data from a spreadsheet. It opens each website, scrolls through the relevant pages, extracts the data, and builds a comparison document. A task that would normally take a full research day can be done in under an hour.
- **Meta-analysis of multiple reports** If you receive ten departmental reports and need to extract a global trend without reading all 200 pages, Cowork reads all of them and produces a structured meta-analysis showing what patterns appear across the set, what the outliers are, and what the overall direction suggests.

3\. Writing and content

- **Batch updating evergreen content** For content creators who have a library of older articles that are still relevant but need fresh references, updated statistics, or new examples, Cowork can go through the entire library, identify which articles need updating, pull in fresh information from the web, and create updated versions. What would normally be a week-long project becomes a single Cowork session.
- **Drafting personalized outreach at scale** Give Cowork a list of prospects, some background information about each one, and your messaging guidelines. It researches each person using available data, drafts personalized outreach messages, and saves them as a ready-to-review batch. You review and send. The personal touch is there because each message is written specifically based on real research, not a template with blanks filled in.
- **Generating reports from meeting transcripts** Drop a set of meeting recordings or transcripts into your folder and ask Cowork to extract action items, organize them by person responsible, create a tracking spreadsheet, and draft follow-up emails. In regular chat that is five separate prompts. In Cowork you describe the outcome, walk away, and come back to all five outputs ready and waiting.

4\. Finance and legal (with plugins)

- **Financial reconciliation** With your bank statements and invoices in a folder, Cowork can run a full reconciliation: analyze the statement, clean up vendor names, categorize each expense, match invoices to transactions, flag anything missing, generate a formatted Excel file, and rename the invoice files to a consistent format. All in one go.
- **Contract review and comparison** The legal plugin lets you point Cowork at a folder of contracts and ask it to identify standard clauses, flag anything unusual or potentially problematic, and create a summary document comparing terms across multiple agreements. Legal teams at Thomson Reuters noted the disruption this kind of capability creates for traditional legal software products.
- **Portfolio analysis and rebalancing recommendations** The wealth management plugin can analyze a client's investment portfolio, pull in current market data through connected financial tools like FactSet, and generate a rebalancing recommendation written in the firm's own voice and format. What used to require an analyst's full attention for hours can be produced in minutes and then reviewed and refined by the human advisor.

5\. HR and operations (with plugins)

- **Building the full hiring workflow** The HR plugin can take a job title and a few notes about the role and generate a complete job description, an offer letter template, an onboarding plan for the first 30 and 90 days, and an initial performance review framework. All formatted to your company's standards if you provide them.
- **Vendor evaluation and documentation** The operations plugin handles process documentation, vendor comparison matrices, change request tracking, and runbook creation. If you are evaluating three vendors for a software contract, you can drop their proposals into a folder and ask Cowork to produce a structured comparison document that summarizes each vendor's offer, highlights the key differences, and flags the questions you need to ask before deciding.

## How to Write Good Prompts for Cowork

This is the section I wish someone had given me when I started. Because I made every mistake here before I figured out what actually works.

The quality of your results depends heavily on how clearly you describe the task. Cowork is powerful, but vague instructions produce vague results. Early on I gave it loose prompts and got loose results. Once I started treating it more like briefing a capable colleague who needs the full picture, the quality jumped significantly.

Here is everything I have learned about what makes prompts work.

1. **The core principle: describe the outcome, not the process**

This was the biggest difference for me. When I was building that presentation in Nairobi, I did not tell Cowork which slides to create first or how to structure each section. I described what the finished presentation needed to accomplish, who the audience was, and what I wanted them to walk away feeling. Cowork handled the rest.

Instead of telling Cowork every step, describe what you want the finished work to look like. Cowork figures out the steps. You specify the destination.

**Less effective:** "Help me make a presentation about AI adoption for a business audience"

**More effective:** "I am presenting to a room of 50 business professionals in Nairobi who are familiar with AI but have not yet started using it in their daily work. Build me a 12-slide presentation that opens with why this matters now, walks through three practical use cases with real examples, and closes with a clear call to action. Use a professional but conversational tone. Save the file as AI-Adoption-Talk.pptx in the Presentations folder."

The second version tells Cowork exactly what done looks like. That specificity is what produces something close to finished rather than something that needs significant rework.

2\. **Be specific about the output format**

Tell Cowork exactly what you want the finished output to look like. If you want an Excel file, say Excel. If you want a Word document with specific headings, describe the structure. If you want files renamed in a specific format, write out the exact format.

I learned this the hard way when I asked Cowork to create "a summary" of a set of research documents and got back a plain text file when I wanted a formatted Word document with sections. One extra sentence in the prompt fixes that entirely.

**3\. Tell it what not to do**

If there are files it should not touch, folders it should stay out of, or actions it should avoid, state them explicitly. This is especially important for anything involving deletion or moving files.

**Example:** "Do not delete any original files. Do not modify anything in the Archive subfolder."

I include a line like this in almost every prompt now. It takes five seconds and removes a lot of uncertainty.

**4\. Use constraints to keep it focused**

If you have a large folder and only want Cowork to work with specific file types or files from a certain date range, say so upfront. This saves time and avoids accidental changes to files you did not intend to include.

For example: "Only work with files created after January 1, 2026. Ignore any files with Draft in the name."

5\. **Give it context about who you are and what you are trying to achieve**

This one made a noticeable difference for me. When I told Cowork who the audience for my Nairobi talk was, not just what the topic was, the output was calibrated to that audience in a way that felt genuinely thoughtful. The examples it chose, the language it used, the level of technical depth, all of it adjusted based on that context.

A sentence or two of context at the start of your prompt often produces a meaningfully better result than jumping straight into the task.

6\. **The trick that saves the most time**

If you are not sure how to phrase a complex task clearly, open regular Claude chat first and describe what you want in plain language. Ask Claude to turn that description into a detailed Cowork prompt. You can also ask it to flag edge cases you might have missed. Then take that polished prompt into Cowork and run it.

I use this regularly. It sounds like an extra step but it saves time overall because you are far less likely to get halfway through a Cowork session and realize the instructions were ambiguous.

## What Cowork Cannot Do (Yet): Honest Limitations

Cowork is impressive and genuinely useful, but it is still in research preview and has real limitations worth knowing about.

- **It can make mistakes on complex or ambiguous tasks.** Always review outputs before using them, especially for anything important. It works best with clear, specific instructions.
- **It uses a lot of your usage allocation.** A single complex task can consume what would normally be many regular conversations worth of quota. If you are on the Pro plan, you will notice this. Batch your work into efficient sessions and use regular chat for simpler tasks.
- **It can sometimes be overly cautious with permissions.** It will ask for confirmation frequently, which is good for safety but can interrupt flow if you are doing many small steps. Learning to give it well-scoped tasks up front reduces unnecessary interruptions.
- **It struggles with scanned PDFs and heavily formatted documents.** If your PDFs are images of text rather than actual text documents, Cowork may not read them accurately. Clear, text-based documents work best.
- **It is not the right tool for simple one-off tasks.** If you just need to rewrite a paragraph or get a quick answer, regular Claude chat is faster and uses less of your allocation. Cowork is for complex, multi-step, multi-file work.
- **It does not build memory over time.** Cowork treats each session as a fresh task. It does not accumulate ongoing knowledge about your work the way a human assistant would. You need to provide relevant context for each session.
- **Always have backups for important files.** File operations can be difficult to undo if something goes wrong. Before running Cowork on important documents, make sure you have a backup copy somewhere safe.

## Safety: What to Know Before You Start

Because Cowork runs directly on your computer and can make real changes to real files, it is worth understanding the safety mechanisms that are built in.

- **Deletion protection**: Claude always asks for your explicit permission before permanently deleting any files. You will see a clear permission prompt and must click Allow before any deletion happens.
- **You control file access**: Cowork only has access to the folder you specify. It cannot reach files outside that folder unless you grant additional access.
- **Data stays local**: Your files do not get uploaded to Anthropic's servers for storage. Conversation history is stored locally on your machine.
- **Do not use for regulated workloads**: Cowork is currently not suitable for work that is subject to compliance regulations like HIPAA, GDPR, or similar frameworks. Cowork activity is not captured in audit logs or compliance exports.
- **Be careful with web content**: If you are using Cowork with the Claude in Chrome extension to browse and pull data from websites, only allow access to sites you trust. Web content can sometimes carry malicious instructions intended to interfere with AI agents, a vulnerability known as prompt injection.

## Conclusion

Cowork is not another AI chatbot with a slightly better interface. It is a genuine change in how the relationship between people and AI tools works.

The standard model has always been: you think, you plan, you execute, and AI assists at specific moments when you ask it to. Cowork changes that. You think and direct. AI plans and executes. You step away and come back to finished work.

For professionals who spend hours on tasks that are important but not strategically interesting, like organizing files, processing receipts, synthesizing research from a dozen sources, or updating the same information across twenty documents, Cowork gives that time back. And for teams using the department-specific plugins, it changes what a small group of people can produce in a day.

It is still in research preview. It has rough edges. It uses your quota quickly and sometimes asks for confirmation more than you want it to. But even in its current state, it is one of the most practically useful AI tools that has been released this year.

The best way to understand it is to try it. Pick a task you have been putting off because it is tedious and multi-step. Drop it into Cowork with a clear description of what you want. Watch what happens. That experience will tell you more than any guide can.
