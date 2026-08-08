---
type: "Web"
authors: "[[Bryan Neider]]"
url: "https://www.linkedin.com/pulse/pour-foundation-first-what-nonprofits-must-build-before-bryan-neider-ne3hc/"
published: 2026-08-05
created: 2026-08-05
tags:
  - "strategia-AI"
  - "organizacje-społeczne"
  - "szkolenia-AI"
---


### TEAMS! Newsletter | AI Edition | August 5, 2026

I spent more than twenty-five years in corporate leadership, watching technology rollouts succeed and fail. Ultimately, the pattern was never about the technology itself. It was about sequencing. The organizations that won built the foundation first. The ones who struggled skipped straight to the exciting part and spent the next two years quietly repairing what they should have built correctly the first time.

AI is following the same pattern across our sector right now, and the execution sequence matters most. Generative AI needs guardrails in place before it reaches a staff member's fingertips. Agentic AI, tools that don't just draft a document but actually take action on your behalf, needs something even more foundational: workflows and data you trust. Skip either step, and you haven't saved time; you’ve created more work in the future. You've just moved the mess downstream, where it costs more to find and fix, and you likely will have lost your team's trust in the process.

### Executive Summary

- **Policy comes before rollout, not after.** Staff will use AI whether or not you've set guardrails; the only question is whether you set them intentionally.
- **Nonprofit licensing has genuinely changed the math.** Every major provider now offers steep nonprofit discounts, and the gap between "cheap" and "free" is now much narrower than most organizations realize.
- **Agentic AI runs on the data and workflows you already have.** The old warning, “garbage in, garbage out,” is more consequential now because an agent will act on garbage and confidently claim accuracy, even when it is wrong.
- **Staff literacy is infrastructure, not a nice-to-have.** AI tools will underperform when used by a team that was never trained to use them well.

### Five Pillars of AI Readiness

### Pillar 1: Guardrails Before Go-Live.

Before any tool reaches a broad staff rollout, establish a written AI use policy: what data can and cannot be entered into a consumer AI tool, which platforms are approved, and who owns the decision when a new use case arises. A policy written after adoption is merely documentation of the mistakes you've already made.

- ***A practical starting point:*** Don't wait for a perfect, comprehensive policy; draft a one-page starter version in a single meeting. Gather three or four people who represent different parts of the organization, including a program lead, someone from IT or operations, and someone from finance or HR. Answer just three questions together: what data we are never willing to put into a consumer AI tool (client records, financial data, anything identifiable); which tools are approved for use right now; and who a staff member should ask when a new situation isn't covered. Write the answers down, share them with the full team, and treat it as version one, not a finished document. A short, honest policy in place this week beats a thorough one still being drafted in six months, while staff is already experimenting on their own. After this step, you will need to evaluate what data protection laws and regulations you ***must comply*** with, such as HIPAA-related data.

### Pillar 2: The AI Platforms

Every major provider now has a real nonprofit program, and the differences are worth understanding before you commit:

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQGWEnWrFNKBzw/article-inline_image-shrink_1000_1488/B56Z_SBaInJgAI-/0/1785935019033?e=1787788800&v=beta&t=4-OjTM5649TEVPfR_WgDzbcurofqQlPxaCqtkHbp2EA)

Pricing and terms in this space change quickly. Verify current rates directly with each provider before budgeting.

The larger point holds regardless: don't default to whatever tool a staff member already has open. Match the platform to the workflow, and use the nonprofit discount programs. They exist specifically so budget isn't the reason your team falls behind.

***Pricing is only half the licensing decision.*** For a nonprofit handling client, health, or family data, such as intake records, therapy notes, and financial assistance applications, the governance and data protection terms attached to each plan matter just as much:

- **Claude for Nonprofits:** On Enterprise plans, an organization's Primary Owner can activate HIPAA readiness and sign Anthropic's Business Associate Agreement (BAA) directly in account settings. Standard Team plans are not BAA-eligible. Enterprise plans include admin-level audit logs and data retention controls.
- **ChatGPT for Nonprofits:** OpenAI signs a BAA for sales-managed ChatGPT Enterprise and its API, not for self-serve Business accounts. By default, Enterprise data isn't used to train models, and admins receive an audit log via OpenAI's Enterprise Compliance API.
- **Gemini / Workspace for Nonprofits:** Gemini inherits the protections already configured in your Workspace domain, including data loss prevention, admin console controls, and (if signed) your organization's Workspace HIPAA BAA, rather than carrying its own separate terms.
- **Microsoft 365 Copilot:** Enterprise Copilot, used within your organization's Microsoft 365 tenant, is generally covered under Microsoft's standard HIPAA BAA for eligible plans; the free personal account version of Copilot is not, and staff using it with client data would fall outside your organization's protection entirely.
- **Perplexity Enterprise Pro:** A BAA is available only through custom enterprise contracting, not as a standard, publicly posted agreement; confirm it's actually executed before entering client data, since Perplexity's own terms prohibit processing health information on this plan without one. Currently, the free and Pro consumer tiers, and Perplexity's API, are not eligible for a BAA under any circumstances.

**None of this is legal advice**, and BAA terms, eligible features, and exclusions shift often; confirm current coverage with each vendor and with your own counsel before any client or health-related data touches these tools, and make the plan tier and configuration explicit in your written policy, not left to individual judgment.

### Pillar 3: Know Your Plumbing.

Agentic AI doesn't just answer questions; it takes action within your systems. Before you let it, map the workflow it will touch: where the data lives, who owns it, and where it's already inconsistent. This is unglamorous work, but it's exactly what determines whether automation helps you or multiplies your existing errors at machine speed.

- ***A practical starting point:*** Workflow mapping is a skill, and like any skill, it's best built on small, non-critical work before it's applied to something critical. Start with one recurring, moderately complex process- donor gift entry, volunteer scheduling, or intake follow-up- and sit down with the people who actually run it. Document every step in plain language: what triggers the process, which systems and spreadsheets it touches, who owns each handoff, and where people already work around a known gap or inconsistency. You'll likely find that the map on paper doesn't match what actually happens day to day, and that gap is the most valuable finding in the whole exercise. Do this manually, without AI, for two or three workflows before you ever connect an agent to one. The team that gets good at seeing its own workflow clearly is the team that will, months from now, know exactly where agentic AI is ready to help, and where it isn't yet.

### Pillar 4: Data Integrity as Infrastructure.

**“** Garbage in, garbage out” isn't a dated warning. It's more urgent than ever because an agent doesn't just process bad data; it acts on it. Clean donor records, accurate program data, and a single source of truth aren't administrative housekeeping. They're the infrastructure that determines whether agentic AI becomes a capability or a liability.

- ***A practical starting point:*** Pick one core dataset (your donor database, client records, or program outcomes tracker) and run a small, honest audit before touching anything else. Pull a sample of fifty to a hundred records and check for duplicates, outdated contact information, inconsistent field entries, and conflicting values across systems that should agree. Ask the simplest possible question of each record: if an agent acted on this today, would it do the right thing? You don't need a data team or new software to start; you need one afternoon, one spreadsheet, and someone who knows the data well enough to spot what's wrong. What you learn from that single sample will tell you more about your organization's actual AI readiness than any policy document will.

### Pillar 5: Training Your Crew.

None of this works without a team that knows how to use it. A staff AI literacy program, tiered from basic prompting to advanced use, is the human infrastructure that determines whether your investment in AI tools and a governance policy translates into your team’s daily work. The “gardener's approach” applies here as much as anywhere: you don't get a harvest by planting and walking away. You need to nurture and water growth.

- ***A practical starting point:*** Run a one-hour, hands-on workshop with a small, willing group of five to eight people, mixed across roles rather than all from one department. Skip the slide deck. Give everyone the same real task from their actual job, such as drafting a donor update, summarizing a meeting, or outlining an intake form, and let them work through it live with whatever AI tool your organization has approved. Compare results and share what worked. Close by asking two questions: what would you use this for again next week, and what felt uncomfortable or uncertain? Those answers are your actual training curriculum. A tiered literacy program built from what your own staff struggled with will land better than one built from a generic template, and it costs you one hour and no budget to find out where to start.

### The AI Readiness Playbook

- **Draft and ratify a written AI use policy** before any staff-wide rollout, define approved tools, prohibited data types, and clear ownership.
- **Compare nonprofit licensing** across Claude, ChatGPT, Gemini/NotebookLM, and Copilot against your actual workflows, not just headline pricing, and review their governance and data-related guardrails.
- **Map your core workflows and data sources** before considering any agentic automation; know where the data lives and who's accountable for it.
- **Audit data quality at the source.** Clean and consolidate your data before connecting anything to it; don't automate a mess and hope AI compensates.
- **Launch a tiered staff AI literacy program**, from foundational prompting skills to role-specific advanced use.
- **Name an AI governance owner,** a person, or small committee that revisits policy and licensing on a set cadence, because this landscape will look different again in six months.

### Closing Thoughts

Every organization I've seen succeed with new technology did the unglamorous work first, the thousand small adjustments that make everything that follows possible. AI is no different. The nonprofits who will look back on this moment and see real capability gained, rather than a tool that quietly created new problems, will be the ones who laid the foundation before they built the machine. This part of foundational work isn't exciting. However, it is necessary, and ultimately, mission-critical. It's the kind of work our sector has always been good at when we slow down long enough to do it right.

> ***Build the Foundation First. Then Build What's Possible.***

Subscribe on LinkedIn [https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7396000666046881792](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7396000666046881792)

#AbilityPath #AIReadiness #NonprofitTechnology #TEAMSNewsletter #GenerativeAI #AgenticAI #NonprofitLeadership