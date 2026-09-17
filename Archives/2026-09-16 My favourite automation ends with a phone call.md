---
type: "Web"
authors: "[[Kyle Behrend]]"
url: "https://kylebehrend.substack.com/p/my-favourite-automation-ends-with"
published: 2026-09-16
created: 2026-09-17
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "organizacje-społeczne"
---


One of my favourite automations ends with someone picking up the phone.

I’ve set versions of it up for a few organisations. When a donation comes through their donation platform, the automation checks a couple of things.

Did the donor tick the box agreeing to receive marketing emails? If so, add them to the email list.

Was the donation above a threshold the organisation has chosen? If so, send a message to the fundraising team so someone can phone that donor and thank them.

The notification might arrive in Slack, by text or by email. What matters is that the team has the information they need to follow up.

It’s a useful example because you can understand the whole process without knowing anything about the tool behind it.

A donation happens. We check some conditions. We take the appropriate actions.

That’s how I want people to start thinking about automations.

**Trigger, conditions, actions**

Across the automation workshops I’ve been running, we keep returning to these three components.

The trigger tells the automation when to begin. That might be a donation arriving, a form being submitted, a scheduled time, or you manually pressing a button.

The conditions determine whether it should continue and which actions should happen. In the donation example, permission to join the email list is one condition. The size of the donation is another.

The actions are what happens next. Add a record, move information between systems, notify someone, or prepare a draft.

You can even sketch those three things on paper or a tool like [tldraw](https://tldraw.com/) before you open [Make](https://make.com/), [n8n](https://n8n.io/), Claude or ChatGPT.

Doing that forces you to explain the task. When should it happen? What information does it need? When should it leave something alone? What should the result look like?

Even if you never build the automation, answering those questions can help you understand your existing process. This is often termed process mapping.

**Start with something you hate doing**

People often ask me where to start. My favourite answer is to look for a task you hate doing.

Keep a little notepad next to your monitor. Each time you catch yourself copying the same information, chasing the same update or repeating the same set of steps, write it down.

A Post-it that says “Can I automate this? Can I use AI for this?” can be enough to help you notice.

You can also ask AI to interview you about your working day. Talk through what you do, what repeats and where you get frustrated. Sometimes explaining the task out loud is enough to spot an opportunity you’ve been overlooking. *Tip: use voice dictation!*

From that list, choose something small, repeatable and easy to verify.

I once had to create Google Drive folders for a cohort of organisations. Each organisation needed its own folder, subfolders and personalised copies of documents.

After making the first couple manually, I knew I didn’t want to repeat the process for every organisation.

I built an automation and kept it to use again with future cohorts. The result was straightforward to check: did each organisation have the right folders and documents?

A task doesn’t have to run every day to be worth automating. An occasional task can still be tedious enough to justify building something reusable.

**Where should you build it?**

A question coming up more often is whether Make and n8n are still worth using when you can create automations within AI tools like ChatGPT and Claude.

I still see plenty of value in both approaches.

For testing an idea or setting up a personal automation, I often suggest starting in the AI tool you already use. You can describe the outcome, work through the instructions and see whether the result is useful.

Researching grant opportunities or preparing a roundup of news on a particular topic can be good experiments using public information. You still need to check the sources, relevance and deadlines. But you can learn without immediately connecting sensitive organisational records or letting a system contact people on your behalf.

For an organisational workflow, I’m more likely to consider Make or n8n. Particularly when it needs several accounts, multiple systems, explicit routing rules or a clear view of what happened at each step.

The donation example fits that pattern. We already know the conditions and the actions. Checking a donation amount and passing information between systems doesn’t require AI to interpret anything.

An email triage automation combines the two approaches.

AI reads the email and categorises it. The workflow then uses that category to decide whether to file it, forward it or prepare a reply for review.

You can choose where AI contributes, which model handles that step and what information it receives. Ordinary data transfer can happen without calling a language model. There are still platform costs, and AI steps still consume tokens, but every step doesn’t need AI.

I find “structured versus AI-led” a useful way to think about how much of the process you define in advance. It’s a spectrum. You can put AI inside a structured workflow, and an AI-led task still needs clear conditions and boundaries.

Start with the job and the level of control you need. Then choose where to build it.

**Getting it running is often the beginning**

The mistake I see is assuming that once an automation is set up, the work is finished.

Things break. Models are discontinued. Prompts stop producing the results you expected because models change. Your organisation changes how it works. You realise there’s another step you’d like to add.

An automation can save time and still need maintenance.

Start by running a small number of examples and checking what actually happened. Include cases where it should take no action.

For the donation workflow, that means checking that someone who hasn’t opted in stays off the email list. It means checking donations above and below the notification threshold.

For grant research, a completed report doesn’t tell you whether the opportunities are current or suitable. You need to look at the sources and confirm the details.

As you get more comfortable, you can expand the workflow. That might mean handling more records, adding another action or connecting another system.

It also means having error handling, keeping backups of the workflow and reviewing whether it still does the job you intended.

I love the idea of people building their own solutions. They know the frustrations in their work better than anyone.

That needs to sit alongside organisational oversight. People should know which tools and data they can use, what needs approval and who can help when something goes wrong. IT may support that, but building useful things doesn’t have to be limited to IT.

For anything the organisation relies on, someone needs to know how it works and take responsibility for keeping it useful.

**Decide what the saved time is for**

In the donation example, there’s a specific answer: phone the donor.

Ask what connected them to the organisation. Thank them. Develop the relationship.

You might also use the time to try something you haven’t had room for. Build a small tool that solves another frustration. Experiment with a more personal way of sharing impact. Create an HTML thank-you experience that helps donors see what their support made possible.

This is what excites me about automation. It can make room for work we’ve been too busy to do and ideas we haven’t had time to explore.

Keep that notepad beside your monitor this week. Write down the tasks you’re tired of repeating. Pick one that’s manageable and easy to check, then map its trigger, conditions and actions.

Before you build it, decide what you’d like to do with the time it gives back.

**What’s next?**

Ready to try this with your own work? Use the [Plan your first automation guide at AI Impact Hub](https://hub.aiimpacthub.com/hub/guides/plan-your-first-automation) to choose a task and map its trigger, conditions and actions.

![](https://substackcdn.com/image/fetch/$s_!VZAx!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87c9459f-431e-491e-b9f5-7293326fbbcc_3420x1903.png)

*[Kyle Behrend](http://kylebehrend.com/) is an AI, Automations & Systems Specialist with 15 years in the nonprofit sector, based on the Central Coast of NSW, Australia. He is the founder of [AI Impact Hub](http://aiimpacthub.com/) and writes The Leverage Point on Substack — exploring how small shifts create transformative change for mission-driven organisations.*