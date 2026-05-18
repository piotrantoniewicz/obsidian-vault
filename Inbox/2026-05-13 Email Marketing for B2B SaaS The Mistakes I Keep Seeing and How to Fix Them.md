---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/email-marketing-for-b2b-saas-the-mistakes-i-keep-seeing-and-how-to-fix-them?utm_medium=email&_hsenc=p2ANqtz-8h-1Vv4ez-aWwYZ9mNf3oiSWTA9wu9ku9HeVDmtCqS6SouT5junaAp7OyYXlKr6S4B7nmmVy5jENoZjOJqxDuzEKd_WLDo2fFvmvXtp8VxUA1aThU&_hsmi=135789897&utm_content=135788518&utm_source=hs_email"
published: 2026-05-13
created: 2026-05-18
tags:
---


I work with a LOT of B2B SaaS businesses. And across all of them — regardless of product or software, price point, market, or team size — I see the same mistakes playing out in remarkably consistent ways.

The product team thinks the product sells itself. The marketing team is running email flows that fire based on time elapsed rather than user behaviour. The sales team is doing their own outreach in parallel, with no visibility into what marketing has already said. And the product data — the actual signals from inside the platform that would tell everyone exactly where a user is and what they need — is sitting in one system while the emails are being written in another, with no connection between them.

Email in a SaaS context is one of the most powerful levers available. It sits at the intersection of acquisition, activation, retention, and expansion. Done properly, it shortens the path from free trial to paid customer, reduces churn, drives upsell, and maintains relationships with leads who are not ready yet but will be.

Done the way most SaaS companies do it — generic, disconnected from product data, misaligned with sales, and built around the wrong understanding of who the user actually is — it does almost none of those things.

This blog covers the biggest mistakes I see in B2B SaaS email, why they happen, and what to do differently. It is specific, it is direct, and it is based on real programmes I have worked with.

## Mistake 1: You don't know why someone signed up — and you're not asking

This is where everything else goes wrong.

Most SaaS businesses treat the free trial sign-up as a single event. Someone signed up, put them in the trial flow on product & in email, send the onboarding sequence. and push them toward conversion.

But people sign up to free trials for completely different reasons. And those reasons determine everything about what email they should receive, what message makes sense, what pace is appropriate, and whether sales should be involved at all.

In my experience, there are four primary motivations behind a free trial sign-up. Understanding which one you are dealing with is the most important single piece of data you can collect.

The biggest mistake here is treating all four of these people identically. The same onboarding email, the same drip sequence, the same sales handoff criteria. They are not the same person. They did not come for the same reason. They do not need the same next step.

## Mistake 2: Your product and your email system are not talking to each other

This is the email glass ceiling in SaaS, and it is the most limiting structural problem I encounter.

The scenario: you are using HubSpot (or a similar CRM and marketing platform) for your email automation. Your product is running on its own infrastructure with its own database tracking what users actually do inside it. These two systems do not share data in real time.

What this means in practice: your email programme is flying blind. It knows someone signed up for a trial. It knows their name and email address. It does not know that they logged in once, spent forty-five seconds on the onboarding screen, closed the tab and never came back. It does not know that another user has logged in every day for two weeks, used three core features, and has invited a colleague. To your email system, both of those people are "trial users." They receive the same emails.

Those are not the same person, they are not in the same place, and they do not need the same message.

### What product events should be feeding into your email system

The product data that changes the email journey falls into two categories: positive events (things that happened) and negative events (things that should have happened but did not).

Both matter enormously. Most SaaS email programmes only track positive events.

Positive events worth capturing:

- First login after sign-up — time elapsed, device used, entry point
- Key feature activation — the first time a user completes the core action your product is built around
- Team invitation sent — a strong signal of adoption intent and expansion potential
- Integration connected — a user who connects your tool to their existing stack is significantly more likely to convert and retain
- File/project/output created — evidence that the product delivered value for a specific task
- Return visits — frequency and recency of logins is one of the strongest retention predictors available

Negative events (non-actions) worth capturing:

- Signed up but never logged in — a significant and common drop-off point
- Logged in but left within sixty seconds — could not find where to start, onboarding failed
- Started a core action but did not complete it — hit friction somewhere in the key workflow
- Was active, then went quiet — has not logged in for X days after a period of regular use
- Trial expiry approaching with low or no meaningful usage — window closing without value being delivered

### The non-action is the signal

Most SaaS email automation is built to trigger on things that happen: a user completed X, so send email Y. That is useful. But it misses half the picture.

When a user signed up, logged in once for under a minute, and has not been back in four days — that is a signal. When a user started the core workflow three times but has not completed it — that is a signal. When a trial is five days from expiry and a user has never invited a team member despite being on a team plan — that is a signal.

These non-actions are telling you something specific: that something has not worked for this person. Not that they have lost interest. That there is an unresolved obstacle between them and the value your product delivers.

An email that responds to a non-action is not a reminder email. It is a diagnostic email. It should name the specific thing they have not done, acknowledge that this might mean something was confusing or unclear, and offer a genuinely easy path forward. Not "don't forget to upgrade." Not "your trial is running out." A real, human acknowledgement that they tried something and it did not quite work, and here is what might help.

## Mistake 3: Wrong message at the wrong time — and no idea what normal looks like

Even when SaaS companies have product data feeding in, the email sequencing is often off. Either the pace is wrong — too fast, too slow, too uniformly scheduled — or the message does not match where the user actually is.

The most common version of this I see: every trial user gets the same thirteen-email sequence over fourteen days, regardless of their behaviour in the product. User A has logged in every day and connected three integrations. User B has never logged back in after sign-up. Same emails. Same timing. Completely different situations.

The fix for this is intent-triggered sequencing rather than time-triggered sequencing.

### Build your email logic around what users do — not how many days have passed

Time-triggered emails have a place — particularly for deadline communications like trial expiry reminders, where the time itself is the relevant signal. But the core email logic for a SaaS trial journey should be built around events and non-events, not calendars.

A user who activated a key feature on day two does not need the "getting started" email on day three. A user who has never logged back in does not need the "here are five advanced features you'll love" email on day seven. Both of those emails, sent at the wrong time to the wrong person, build a negative association. The product does not feel like it understands them. It feels like it is talking at them.

The intent-based approach:

- When a user activates the core feature → send a "you just did the important thing" acknowledgement, then move to the next relevant step based on what comes next in a successful user journey
- When a user does not log back in within 48 hours → send a low-friction "can we help?" email that addresses the most common reasons new users do not come back
- When a user invites a team member → trigger the team onboarding sequence, not the individual onboarding sequence they were on
- When a user goes quiet after an active period → a re-engagement that names the change in pattern, not a generic win-back
- When a trial is approaching expiry with meaningful usage → a conversion email that references their specific usage, not a generic "trial ending soon"
- When a trial is approaching expiry with minimal usage → not a conversion email at all, but an "is everything okay?" email that acknowledges the low usage and tries to understand why

### Know what normal looks like for your product

One of the most useful exercises you can do before building any email logic is to look at your historical data and understand what an engaged trial user looks like for your specific product.

How many logins in the first week is typical for users who go on to convert? Which features do converting users activate that churned users do not? How long does it typically take from sign-up to first meaningful value moment? What does the activity pattern of a user who is about to churn look like versus one who is about to convert?

These benchmarks — your own data, not generic industry figures — are what allow you to build email logic that responds to meaningful deviations rather than firing based on arbitrary time triggers.

A user who has logged in twice in the first week when your typical converting user logs in five times is showing a pattern worth responding to. A user who has not activated the core feature when 80% of converting users do so within the first three days is showing a pattern worth responding to. Without your own benchmarks, you are guessing. With them, you are responding to evidence.

## Mistake 4: Sales and marketing operating in parallel universes

This one costs more than any other mistake in SaaS, and it is almost universal.

Marketing has a free trial nurture sequence running. Sales has a list of trial users they want to reach out to. Both are contacting the same person. Neither knows what the other has said. The user receives a marketing email at 9am about the product's enterprise features, and a sales email at 2pm asking if they have had a chance to try the product.

This is the message collision problem. And in the context of a free trial, where the user's impression of how sophisticated and customer-centric your company is forms very quickly, it is damaging.

But the deeper problem is not the duplication. It is that sales and marketing are making handoff decisions based on different, disconnected information.

Sales is often given a list of trial users based on crude criteria: they signed up in the last seven days, they are in the right company size range. That is it. No information about what motivated them to sign up, no information about their product behaviour, no information about what marketing has already communicated.

A user who signed up because they needed a specific tool for a one-off project is not a sales lead. They were never looking to buy. Assigning them to a sales rep who calls and asks "what are you hoping to achieve with the platform?" is wasting everyone's time and potentially souring a relationship that could have been nurtured toward a genuine need later.

A user who signed up because their team is actively evaluating solutions and they spent forty minutes inside the product on their first login, activated three features, and has already started inviting colleagues is an extremely warm sales lead who probably wants a conversation. Leaving them purely in the marketing drip sequence for two weeks is a missed opportunity.

### How sales and marketing handoffs should actually work in SaaS

The handoff criteria need to be based on a combination of motivation data and product behaviour data — not just time elapsed or demographic fit.

A user is ready for sales engagement when:

- Their sign-up motivation indicates they are actively evaluating solutions (Type 2 in the framework above)
- Their product behaviour shows meaningful engagement — multiple logins, key feature activation, team invitation sent
- There are signals of evaluation intent — they have visited the pricing page, they have viewed the integration directory, they have watched a demo video

A user is not ready for sales when:

- They signed up with a specific one-off need and their product usage was narrow and task-specific
- They signed up with research intent and their product usage was brief and exploratory
- They have shown minimal product engagement — regardless of how warm their profile looks on paper

Sales and marketing need to agree on these criteria together, review them regularly as product and market evolve, and document them clearly so that both teams are operating from the same understanding of what a sales-ready lead looks like in this specific product.

The other critical element: sales must have visibility into what marketing has already sent before they reach out. A sales rep who calls and asks "did you get our email about the enterprise features?" when they have not checked whether that email was actually sent — and whether it bounced or was never opened — is starting the conversation on the wrong foot.

## Mistake 5: Ignoring the biggest opportunity sitting in your database

Most SaaS marketing teams are focused on acquisition. Getting new people into the trial. Running ads, producing content, growing the top of funnel.

Meanwhile, sitting in the CRM is a database full of people who already know about the product, already signed up, already tried it — and did not convert. Some of them churned. Some of them expired their trial and just did not come back. Some of them were enthusiastic early on and then went quiet.

These people are your warmest possible re-engagement audience. They do not need to be educated about what the product is or why it might be useful. They already know. What they need is either the right trigger — a new feature that addresses the friction point that stopped them, a change in their circumstances that makes the problem more urgent, a conversation that resolves an objection — or simply to be reminded that you are still there.

The re-engagement email for a lapsed trial is not the same as the original trial email. It should acknowledge the gap explicitly. It should reference something specific about their behaviour — not in a creepy way, but in a way that shows the product has been paying attention. And it should make coming back easy.

Before you run another acquisition campaign, run a lapsed trial analysis. Who in your database signed up within the last twelve months, showed meaningful early engagement, but did not convert? What was their motivation at sign-up? What did they do in the product? Why might they have left?

That analysis will almost always reveal an audience worth re-engaging — and it will cost a fraction of what it costs to acquire the same number of new trial users from scratch.

## What a properly integrated SaaS email strategy looks like

Pulling all of this together, here is the structure of a SaaS email programme that actually works.

Layer 1: Motivation data at sign-up

One question at the point of trial registration: why are you signing up? Map the answer to a segment. Use that segment to personalise the entire downstream journey — both the email content and the sales handoff criteria.

Layer 2: Product data feeding the CRM in real time

Key product events — both positive actions and meaningful non-actions — feeding into the email system and triggering the right communication at the right moment. Not time-based. Event-based.

Layer 3: Intent-triggered email sequences, not calendar sequences

Different journeys for different motivation types. Sequences that branch based on product behaviour. Emails that respond to what the user has actually done — or not done — rather than firing on a schedule.

The core journeys to build:

- **Engaged trial** — actively using the product, progressing through the value journey, nudges toward the next natural step
- **Struggling trial** — signed up but not activating, emails focused on reducing friction and resolving specific obstacles
- **High-intent prospect** — strong motivation and strong product engagement, coordinated with sales for a consultative conversation
- **One-off need user** — task-specific engagement, low conversion priority, long-term nurture and awareness focus
- **Trial expiry — high usage** — clear, specific conversion email referencing their actual usage
- **Trial expiry — low usage** — not a conversion email, a genuine "what happened and can we help?" conversation
- **Post-trial lapsed** — re-engagement sequence built around what has changed, what is new, and why now might be different

Layer 4: Clear sales and marketing handoff criteria

Documented, agreed, and regularly reviewed. Based on motivation plus product behaviour. With full marketing email history visible to sales before they reach out.

Layer 5: Ongoing customer email — not just acquisition

Email does not stop at conversion. For SaaS businesses, the post-conversion email programme is often where the biggest commercial value sits — driving feature adoption, reducing churn, driving upsell and expansion.

The principles are the same: product behaviour data should be feeding into the programme, communications should respond to what customers are actually doing in the product, and the goal is always to move them toward the next meaningful value milestone.

## The summary

Email in a SaaS business is not a marketing channel that runs separately from the product. It is an extension of the product experience — a way to reach users when they are not in the platform and guide them toward the moments where the product delivers value.

When it is built that way — grounded in motivation data, connected to product events, timed to user behaviour rather than calendar schedules, and aligned with how sales operates — it is one of the most powerful tools available for converting trials, reducing churn, and driving expansion.

When it is built as a generic drip sequence that fires based on days elapsed and treats every user identically — it is noise. And noise, in a SaaS trial context where the user's impression of your company forms very quickly, is expensive.

The good news: most of what needs changing is structural, not creative. Better data integration. Clearer motivation segmentation. Intent-based triggers. Sales and marketing alignment. None of it requires you to become a better copywriter. It requires you to build the foundations that make the right message possible.

### Further reading from The Vault:

- [Customer Journey Mapping for Email](https://weareastral.co.uk/thevault/customer-journey-mapping-for-email-how-to-actually-do-it)
- [Intent Over Personalisation](https://weareastral.co.uk/thevault/intent-over-personalisation-what-personal-actually-means-in-email-and-how-to-build-it)
- [How to Diagnose Why Your Email Journey Isn't Converting](https://weareastral.co.uk/thevault/how-to-diagnose-why-your-email-journey-isnt-converting)
- [Designing Email Journeys Using TFDS](https://weareastral.co.uk/thevault/designing-email-journeys-using-tfds)
- [ABM Is Showing Its Age — How Email Fits Into Modern B2B Account Strategy](https://weareastral.co.uk/thevault/abm-is-showing-its-age-heres-how-email-actually-fits-into-modern-b2b-account-strategy)
- [Stop Reporting on Opens and Clicks](https://weareastral.co.uk/thevault/stop-reporting-on-opens-and-clicks.-heres-what-to-measure-instead)
- [The Science of Sending the Right Email at the Right Time](https://weareastral.co.uk/thevault/the-science-of-sending-the-right-email-at-the-right-time)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.