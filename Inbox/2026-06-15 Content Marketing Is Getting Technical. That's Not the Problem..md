---
type: "Web"
authors: "[[Ina Toncheva]]"
url: "https://inatoncheva.substack.com/p/content-marketing-is-getting-technical?utm_source=multiple-personal-recommendations-email&utm_medium=email&triedRedirect=true"
published: 2026-06-15
created: 2026-06-20
tags:
---


![](https://substackcdn.com/image/fetch/$s_!f4_f!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F269ab7a8-284f-469e-a5da-dbf13c6ea6a9_1376x768.png)

Last week Ryan Law, Director of Content Marketing at Ahrefs, posted what he’d do on his first day as a new Head of Content.

It reads like a developer’s roadmap, but bear with me because that’s exactly why many people will skip it.

Here’s a summary (link to the post at the end of the article):

1. Build a new blog using a static site generator, host with GitHub, deploy with Netlify or Cloudflare Pages.
2. Get access to Gong/Intercom/Slack and extract common entities and n-grams.
3. Build key “source of truth” files in markdown I can reference throughout my workflows.
4. Crawl our sitemap and generate vector embeddings for every article. Use this to analyse topical authority (and topic “drift”) and automate internal linking.
5. Schedule a recurring, automated content audit: pull rankings and backlink data via the Ahrefs MCP.
6. Set up a daily cron job to refresh our highest priority articles.
7. Run a content gap analysis using the Ahrefs MCP.
8. Build my Content OS: a centralised dashboard that pulls all of these reports and workflows into one place.

Some of the points sound barely like a marketing job. But the technical parts are almost beside the point. Someone can build those functionalities for you in a few days if you understand the reasons you need them. Because it represents a real shift in what the content marketing job is becoming.

Let me translate the technical jargon.

### What Ryan said he’d do (in plain English)

**1\. Static site + GitHub + Netlify/Cloudflare Pages**

WordPress and similar CMSs are designed for humans clicking in a browser. An AI agent can’t easily “log into WordPress and update this article.” A static site stored as files in GitHub can be edited by a script, or an AI agent, because it’s just files. The point is to make the blog a codebase, not a GUI (graphic user interface) tool, so that AI can write to it directly.

**2\. Gong/Intercom/Slack for customer language**

Gong records sales calls. Intercom handles customer support conversations. Together they’re the rawest possible source of how customers describe their problems — before marketing has polished it into something cleaner and sterile. The goal is to find which phrases appear most frequently. Two and three-word combinations tell you how people actually think: “too expensive to scale,” “doesn’t integrate with Salesforce,” “takes too long to onboard.” Those phrases become your content angles, your headlines, your keyword clusters.

**3\. “Source of truth” markdown files**

This is prompt infrastructure. Every AI workflow he runs will reference these files. A features/use-cases list stops the AI from misrepresenting the product. A voice document with reference articles stops the AI from sounding generic. Strategic priorities stop the AI from optimizing for the wrong things.

**4\. Vector embeddings of every article**

This is the most technically dense one, so worth slowing down on. A vector embedding converts a piece of text into a set of numbers that represent its *meaning*. Articles about similar topics end up with similar numbers. Once you have embeddings for your whole blog:

- You can measure topical authority mathematically — which clusters are dense, which are thin
- “Topic drift” means: articles that were written to serve one topic have gradually drifted to cover something else, diluting both
- Internal linking becomes automated — find the most semantically similar articles to any new piece and suggest links

You don’t do this manually. You run it as a script. It tells you things about your content at scale that would take a human weeks to audit.

**5\. Automated content audit via Ahrefs MCP + Brand Radar + Site Audit + GSC**

Each tool covers a different failure mode:

- Ahrefs MCP: rankings + backlinks (is this still performing?)
- Brand Radar: AI search visibility (is this being cited in ChatGPT/Perplexity answers?)
- Site Audit: technical issues (broken links, slow pages, indexing problems)
- Google Search Console: traffic decay (was performing, now isn’t)

The output is a prioritized list of content to fix, not a pile of dashboards to interpret. The AI synthesizes the signals into a to-do list.

**6\. Daily cron job to refresh top articles**

A cron job is just a scheduled script. This one pulls the article, runs it through an AI tool to identify topic gaps (things competitors cover that this article doesn’t), updates outdated stats, and saves a draft for human review. The human doesn’t write the update, they approve or adjust it. This is the “manager” framing he mentions at the end: you’re reviewing AI work, not doing the work yourself.

**7\. Content gap analysis via Ahrefs MCP + Firehose**

The gap analysis is standard competitive SEO — find what competitors rank for that you don’t. The interesting addition is Firehose, which is an Ahrefs tool that monitors new content in your industry as it publishes, delivered as a daily email digest. This gives the content team real-time awareness of what’s being covered before it becomes a rankings gap.

**8\. Content OS / centralised dashboard (Agent A)**

Agent A is Ahrefs’ own AI agent platform. The “Content OS” is a single interface that surfaces all the above — audits, gaps, cron job drafts, topical authority maps — in one place. Without this, you have 8 separate scripts and reports. With it, you have a control panel. This is the layer that turns a collection of automations into a system.

### The strategy behind all of it

Put it all together and what Ryan is describing is this: a blog machines can write to, a strategy encoded somewhere AI can read it, a content archive that’s understood rather than just stored, and maintenance that largely runs itself.

The human role in this model is to set the vision, build the system, review the output and apply taste and judgment to course-correct. That's not a smaller job — it's a harder one.

He even names it explicitly at the end of the post: *“AI is truly putting the ‘manager’ into ‘Content Marketing Manager.’ We now operate at a higher level of abstraction.”*

### Is this realistic?

Ahrefs isn’t your average marketing team. The company lives and breathes search data at a scale most companies never touch. They have a deep, native understanding of how content, rankings, and the web actually work. Not as users of data, but as builders of the infrastructure. And they’ve built their own AI agent platform on top of that foundation.

More importantly, they employ people who sit at the intersection of marketing expertise, data fluency, and AI literacy — people who can form a clear vision of how AI can be used to get further ahead.

So yes, directionally right. Not universally applicable tomorrow.

But here’s what I’d push back on: the gap between “Ahrefs can do this” and “most companies can do this” is closing faster than people think. Six months ago, half the tools Ryan mentions either didn’t exist or weren’t accessible to non-developers. Now you can describe most of these systems in plain English to Claude Code or a similar agent and have a working version by end of day.

The limiting factor is rarely the technology. It is knowing what to build and why. It’s the person who can hold the vision of the whole system and knows enough to build each layer.

And when someone in that position is generous enough to share [the full blueprint in public, for free](https://www.linkedin.com/posts/thinkingslow_if-i-was-starting-my-first-day-as-a-new-head-activity-7469755485517271040-s-vH?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAcEiKEB1Ohvfo1W9awc5f6MsmeQk8zyoJo) — it’s worth paying attention.

Hit reply and tell me: is this realistic for where you work? And honestly — do you feel pressure to become more technical than you think you can be? I'd love to know.

Thanks for reading!  
Ina