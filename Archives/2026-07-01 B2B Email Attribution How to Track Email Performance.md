---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/b2b-email-attribution-why-its-mostly-garbage-and-how-to-track-performance-properly-anyway?utm_medium=email&_hsenc=p2ANqtz--ZnBZiDKNkeoy9gyfOe_B6aFUraxJSszU-hPXO6TbE0G6PT6uPaC5x8vAp5PE2c199eMK2-skIsbWp2WFpWsGWnB7RC7HzGQFt_gXdnj_YQiyq3KM&_hsmi=139798729&utm_content=139799049&utm_source=hs_email"
published: 2026-07-01
created: 2026-07-09
tags:
  - "content-marketing"
---


Let me start with the uncomfortable truth that most attribution conversations try to skip past: B2B email attribution is, in large part, a fiction.

Not entirely. Not always. But the idea that you can look at your CRM, your ESP, and your revenue data and produce a clean, defensible number for "what email generated" is, in most B2B businesses, somewhere between an oversimplification and an outright lie. And the models most marketers use to produce that number make the problem worse, not better.

First touch, last touch, linear multi-touch, U-shaped, W-shape, time decay. These models all share the same fundamental flaw: they assume that commercial outcomes can be causally attributed to specific touchpoints in a way that is both measurable and meaningful. In B2B, where sales cycles run for months, multiple stakeholders are involved, and the relationship between any single email and any specific deal is almost always indirect and partial, that assumption falls apart.

This blog is not going to give you a perfect attribution model. There is not one. What it is going to give you is an honest framework for understanding what the models actually measure, why they each fail in different ways, and how to build a performance picture for B2B email that is genuinely defensible — not because it captures everything, but because it is honest about what it captures and what it does not.

## Why B2B email attribution is fundamentally broken

Attribution works reasonably well in environments where the path from marketing touchpoint to commercial outcome is short, direct, and involves one person. Someone clicks a Google Shopping ad and buys a product in the same session. The click caused the sale — or at least, it caused enough of the sale that crediting it makes practical sense.

B2B is almost never that environment. Here is what actually happens in a typical B2B email journey:

- A prospect downloads a white paper via a paid LinkedIn ad. They are added to a nurture sequence.
- Over the next three months, they receive twelve nurture emails. They open four of them.
- One of those emails includes a blog link about a topic they happen to be researching that week. They click through, spend twenty minutes on the site, and visit the pricing page.
- Three weeks later, a colleague mentions your company to them in a Slack message.
- The prospect Googles your company name, lands on the homepage, and fills in a contact form.
- A sales rep follows up, has three calls over six weeks, and closes the deal.

Which touchpoint gets the credit? The LinkedIn ad that started the journey? The fourth nurture email that drove the pricing page visit? The blog post? The colleague mention that does not exist in any system? The Google search? The sales calls?

The answer, honestly, is all of them and none of them. All of them contributed to the outcome. None of them caused it in isolation. And any model that assigns 100% of the credit to one of them — or even divides it cleanly between them — is producing a number that is convenient, not accurate.

## The attribution models — what each one measures and why each one fails

Before you can choose the least-bad model for your situation, you need to understand what each one is actually measuring — not what the name implies it measures, but what the underlying logic produces when applied to real B2B data.

## What to do instead — building a contribution model that actually holds up

Given that all standard attribution models fail in different ways for B2B email, the most defensible approach is to stop trying to attribute and start trying to demonstrate contribution. These sound similar but they produce completely different frameworks.

Attribution says: this specific touchpoint caused this specific outcome, and here is how much of the credit it deserves. Contribution says: email was present in the journey of contacts who converted, and the contacts with email in their journey behaved differently from those without it. Here is the evidence.

Contribution is provable. Attribution is usually not. And a provable contribution argument, made with the right data and the right framing, is often more convincing to a senior audience than a precise-looking attribution number that anyone with commercial experience will immediately question.

### The five contribution questions to answer

These are the questions that, if you can answer them with data, build a defensible commercial case for email in B2B — without relying on attribution models that will not stand up to scrutiny.

Question 1: Do email-active contacts convert at a higher rate than non-email contacts?

Pull two cohorts from your CRM: contacts who received at least three email touches during their journey, and contacts who went through the same pipeline stage without email involvement. Compare their conversion rates.

If email-active contacts convert at a meaningfully higher rate — and they almost always do — that rate difference is your contribution argument. You are not saying email caused the conversion. You are saying that contacts with email in their journey converted at X% higher rates than those without it, which is a correlation that demands explanation and investment.

Question 2: Do email-active contacts move through the pipeline faster?

Compare average time-to-close for contacts with email nurture versus those without. Also compare time between pipeline stages: are email-active contacts moving from MQL to SQL faster? From SQL to opportunity faster?

Pipeline velocity is one of the most commercially credible metrics you can present to a senior audience. A 15% reduction in average sales cycle length for email-nurtured contacts has a concrete financial value that can be calculated from your average deal size and your sales team's capacity.

Question 3: Does meaningful email engagement correlate with pipeline movement?

Look at contacts who took a meaningful email action — clicked a specific link, downloaded a resource, visited the pricing page after an email click — and track what happened to their pipeline status in the following 30 and 90 days.

This is intent signal tracking rather than attribution. You are not saying the email caused the pipeline movement. You are saying that specific email behaviours predict pipeline movement, which justifies investing in the email content and flows that generate those behaviours.

Question 4: Does brand search volume correlate with email activity periods?

Pull your brand search data from Google Search Console or your analytics platform. Overlay it with your email send volume and frequency over the same period. Is there a consistent correlation between active email periods and brand search uplift?

Brand search is one of the clearest measurable signals of email's awareness contribution. When you are consistently in subscribers' inboxes, they search for you more often. That search behaviour — and the direct traffic that accompanies it — is email's awareness value made visible in data.

Question 5: What is the email-assisted pipeline value?

In your CRM, identify every deal that closed in a given period. For each deal, look at whether the contact or any contact at the same company received email communications during the sales cycle — regardless of whether email was the first or last touch.

The total pipeline value of deals where email was present at any stage is your email-assisted pipeline number. It is not an attribution claim. It is a presence claim: email was in the room when these deals were won. That is a contribution argument that is both honest and commercially significant.

## How to build this in HubSpot or any CRM with contact activity tracking

The contribution model above requires two things from your CRM: contact-level email activity data, and contact-level pipeline outcome data. In HubSpot and most comparable platforms, both exist — the challenge is connecting them in a way that produces the analysis you need.

### The minimum viable data setup

Before you can build any meaningful email contribution analysis, you need clean data in three areas:

- Email activity at the contact level — which contacts received which emails, when, and what they did with them. Most ESPs including HubSpot Marketing Hub log this by default, but it needs to be accessible at the contact record level, not just in campaign reports.
- Pipeline stage and date stamps — when each contact entered each pipeline stage, and when they moved between stages. If your pipeline stage dates are inconsistently logged, your velocity analysis will be meaningless. Clean this up before you try to report on it.
- Contact source and first touch data — how each contact originally entered your CRM. This is what allows you to build the email-active versus non-email cohort comparison, because you need to be able to segment contacts by whether email was part of their journey.

### The reports to build

With clean data in those three areas, you can build the following reports in HubSpot or equivalent:

- Email-active contacts vs non-email contacts conversion rate comparison — a contact list filtered by "has received at least N emails" versus "has received zero emails," each measured against conversion rate to customer. This is your highest-impact contribution argument.
- Average deal close time by email engagement level — segment closed deals by the email engagement level of the primary contact (high engagement, low engagement, no email). Compare average days to close across segments.
- Pipeline stage velocity by email activity — track average time in each pipeline stage for contacts with email touches in that stage versus those without. This shows where in the funnel email is accelerating movement.
- Email-assisted closed revenue — a deal report filtered by "associated contact has at least one email activity in the deal timeline." The total closed revenue from these deals is your email-assisted pipeline number.
- Intent signal to pipeline movement correlation — a custom report tracking contacts who took high-intent email actions (pricing page click, specific content download, product page visit from email) and their pipeline status 30 and 90 days later.

### What to do when the data is not clean enough

Most B2B CRMs are not clean enough to run these reports without some preparation work. If that is where you are, here is the order to fix things:

- First: Audit pipeline stage date stamps. Are they being logged consistently? If not, establish the process to log them correctly going forward. You will not have historical clean data, but you can start building it.
- Second: Ensure email activity is being synced to contact records at the individual level, not just sitting in campaign reports. In HubSpot, this requires the Marketing Hub and CRM to be connected with activity logging turned on.
- Third: Define what "email-active" means for your programme specifically. Is it a contact who received at least three emails? Who opened at least one? Who clicked at least once? Set the threshold that reflects genuine engagement for your programme, not a generic definition.
- Fourth: Run the simplest version of the contribution analysis first — conversion rate comparison between email-active and non-email contacts. This requires the least data infrastructure and produces the most commercially legible argument.

## How to present email performance to a senior audience — without getting caught out

The most common mistake in email performance reporting is presenting attribution numbers with more confidence than they deserve. Senior leaders — particularly those with commercial experience — are often more sceptical of precise-looking attribution figures than most marketers assume. A CFO who has seen attribution models fail before will push back on "email generated £400,000 in pipeline" a lot harder than on "contacts with email in their journey converted at 23% higher rates than those without."

The first statement makes a causal claim that cannot be substantiated. The second makes a correlation observation that can be verified from the data. Both are making a case for email's commercial value, but one of them is honest about what the data actually shows.

### The framing that works

Build your email performance story around three layers, presented in this order:

- What email is doing that we can see directly — email-assisted pipeline value, conversion rate comparison, pipeline velocity differences. Specific numbers, clearly sourced, with the methodology explained.
- What email is contributing that we cannot directly attribute — brand search uplift correlation, inbox impression volume, awareness and familiarity built through consistent presence. Be explicit that this is contribution evidence, not attribution.
- What the combination of both tells us about the programme's commercial value — and what the cost of removing email from the marketing mix would likely be, based on the conversion rate differential.

This three-layer structure is more persuasive than a single attribution number because it is honest. It acknowledges the limits of what can be measured while making the strongest possible case from what can be. And it is much harder to challenge in a board meeting than a model number that an experienced CFO can immediately identify as oversimplified.

## Summary

Attribution in B2B is mostly garbage. Not completely, contribution analysis using the right CRM data produces genuinely useful commercial arguments, but the clean, defensible "email generated X in revenue" number that most attribution models promise is, in most B2B businesses, an oversimplification that will not survive serious scrutiny.

The more defensible position is this: email was present in the journeys of contacts who converted at significantly higher rates, moved through the pipeline significantly faster, and generated significantly more pipeline value than contacts without email in their journey. The causal mechanism is not fully attributable. The correlation is clear, consistent, and commercially significant.

That is a different kind of argument from "email generated £X." It is a harder argument to make because it requires clean data, careful analysis, and honest framing. But it is an argument that holds up — in a board meeting, in a budget conversation, in a performance review — in a way that a single attribution number rarely does.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.