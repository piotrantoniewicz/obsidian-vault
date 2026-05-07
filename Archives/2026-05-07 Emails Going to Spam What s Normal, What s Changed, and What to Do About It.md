---
type: Web
authors: '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/emails-going-to-spam-whats-normal-whats-changed-and-what-to-do-about-it?utm_medium=email&_hsenc=p2ANqtz-_1wJ78YlALfI420cuQKazfmXhm0ufCmCz1cqM3wqujhmabLcmvDSxMDu53WlR4jSSVyexyyF-U2J-0Xr6979WRxD4E8uTl-E03j0wa7j-x2zlgPps&_hsmi=135269154&utm_content=135270488&utm_source=hs_email
published: 2026-05-07T00:00:00.000Z
created: 2026-05-07T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
  - content-marketing
---


Let me start with something that will either reassure you or surprise you, depending on where you are right now.

Some of your emails are (and will be )going to spam, even if you are doing everything right.

Every time I send my newsletter, I know that a small portion of it is landing in spam folders.

Not because my programme is broken. Not because I have a deliverability problem. Because that is how email works. No sender — not one, not anywhere in the world — achieves 100% inbox placement across all providers for all recipients. It has never happened. It will never happen.

The question is not whether some of your emails go to spam.

The question is: how much, which providers, is it sustained, and does it represent a real problem or just the normal reality of operating in a complex email infrastructure?

That distinction matters enormously — because the response to "this is normal and manageable" is completely different from the response to "this is a structural deliverability problem that needs urgent intervention." And most email teams do not have the information they need to tell the difference.

This blog will give you that information. What spam placement actually is, what the numbers look like across providers, what has changed recently, what the thresholds are that should prompt action, and why your ESP dashboard is almost certainly not showing you any of this.

## What "going to spam" actually means — there are three different things

Before we talk about rates and thresholds, it is worth being clear on what going to spam actually means — because there are three distinct scenarios, and they are not equally serious.

### Type 1: Provider-decided spam placement

This is where a mailbox provider — Gmail, Microsoft, Yahoo, Apple — makes an algorithmic decision that your email belongs in the spam folder rather than the inbox. The recipient did not ask for this. Their spam filter made the call based on your sender reputation, your content, and the engagement history between your domain and that provider.

This is the most common type of spam placement and the one this blog is primarily about. It is measurable, manageable, and varies significantly by provider.

### Type 2: Subscriber-reported spam (spam complaints)

This is where a real human being looks at your email and clicks "this is spam," "mark as junk," or equivalent. This is fundamentally different from provider-decided placement — and significantly more serious.

When a subscriber marks you as spam, they are sending a direct, explicit signal to the mailbox provider that your email was unwanted. That signal directly damages your sender reputation. And unlike a quiet spam placement that affects only that recipient, a complaint contributes to reputation scoring that affects your deliverability for everyone.

Spam complaints are the metric I take most seriously in any audit. They should be yours too.

### Type 3: Delivery failures and rejections

This is where the receiving server actively rejects your email — it does not arrive at all, rather than arriving in spam. Rejection rates spiked significantly during the 2025 holiday season, according to Validity's 2026 benchmark data, as senders ramped volume aggressively and triggered provider-level blocks.

A rejection is different from spam placement. Spam placement means the email arrived but was filtered. A rejection means it was blocked before it even reached the recipient's mailbox.

## The number your ESP shows you is not telling you what you think it is

This is the single most important thing to understand about email deliverability — and the thing most marketers have never been told clearly.

When you look at your email service provider dashboard, you will see a delivery rate. It will probably say something like 98% or 99%. And you will probably think: great, almost all my emails are being delivered.

That number means something much more limited than you think.

Your ESP's delivery rate is calculated as sent emails minus bounced emails. That's it. It measures whether the receiving server accepted the email. It does not measure — and cannot measure — where that email went after it was accepted.

An email can be accepted by the receiving server and then immediately placed in the spam folder. Your ESP reports it as delivered. It was — to the spam folder, where the recipient will likely never see it.

Deliverability — genuine inbox placement — is a completely different metric from delivery. And it is one that your ESP almost certainly cannot show you without specialist testing tools sitting outside the platform.

This is why the question "why are my emails going to spam?" is so difficult to answer for most marketing teams. You cannot see the problem in your normal reporting. You need dedicated inbox placement monitoring to get an accurate picture — and most teams do not have it.

## What spam placement rates actually look like — and what's normal in 2026

Based on what I see across the programmes I audit and consult on, combined with Validity's 2026 benchmark data — which covers trillions of data points from global inboxes — here is an honest picture of what spam placement rates look like right now.

First: a zero to fifteen percent spam placement rate is not a cause for concern. That range — anywhere up to about 15% of your emails landing in spam — is broadly normal across the industry. If you ran a test tomorrow and found that number, I would not be alarmed.

Does that mean it is fine and you should do nothing? No. It means it is within the expected range of a functioning email programme operating in a complex infrastructure across multiple providers with different filtering approaches. Keep building your sender reputation. Keep monitoring. Keep your list clean. But do not treat it as a crisis.

Now let me be clear about what I mean by "spam placement rate" here. This is the rate at which provider algorithms are routing your emails to spam folders — not your complaint rate. Those are two different numbers requiring separate monitoring.

### The thresholds — what to watch for

Here are the ranges I use when auditing a programme. These are not industry benchmarks from a study. They are from my own practice, informed by the data I see across the programmes I work with:

| **Spam Placement Rate** | **Status** | **Explanation** | **Action Required** |
| --- | --- | --- | --- |
| 0% – 15% | Healthy | Normal. Even the best programmes land some emails in spam. Stay consistent, keep monitoring. | None — continue maintaining good sender reputation practices |
| 15% – 25% | Worth watching | Starting to creep. Could be a short-term event or the beginning of a trend. Do not panic yet. | Investigate: is this sustained or a one-off? Check for recent events — bounce spike, volume change, complaint uptick |
| 26% – 50% | Needs attention | A meaningful proportion of your audience is not seeing your emails. Revenue and relationship impact is real. | Audit your programme immediately. Look at list health, sender reputation, complaint rates, and sending patterns |
| 50%+ | Serious problem | Half or more of your emails are going to spam. This is a structural deliverability problem, not a one-off event. | Stop sending to unengaged segments. Full programme intervention required. Get specialist support. |

### The sustained vs. short-term distinction

One of the most important things when evaluating any spam placement figure is whether it is sustained or whether it is a short-term event.

A sustained problem is one that persists across a meaningful time window. I look at three periods: weekly, 30-day, and 90-day (quarterly). If a programme is seeing elevated spam placement across all three windows — week after week, across a full quarter — that is a sustained deliverability problem. It indicates structural issues with the programme that require a genuine intervention.

A short-term spike is different. A sudden jump in spam placement that then resolves itself within a week or two is almost always connected to a specific event: a large campaign to a stale segment, a sudden volume increase, a bounce spike, or a provider-level algorithm update that temporarily affected placement before normalising.

The appropriate response to a sustained problem is completely different from the appropriate response to a spike. Treating a spike like a structural crisis leads to overcorrection. Treating a structural problem like a spike leads to it continuing to compound while you wait for it to resolve on its own.

## How Gmail, Microsoft, and Yahoo decide your emails go to spam

The four major mailbox providers — Gmail, Microsoft, Yahoo, and Apple — do not share a single filtering system or a single set of rules. Each builds its own model. Your sender reputation at Gmail is separate from your reputation at Microsoft. You can have excellent placement at one and serious problems at another simultaneously.

Here is what each of the main providers looked like in 2025, based on Validity's benchmark data:

| **Provider** | **Market Share** | **2025 Inbox Rate** | **2025 Spam Rate** | **Key characteristic** |
| --- | --- | --- | --- | --- |
| Gmail | 42.9% | 89.8% | 6.4% | Most aggressive in enforcement. Fast to suppress, fast to recover. Engagement-weighted. |
| Yahoo | 15.7%\* | 87.3% | 6.4% | Mid-range performer. Deletes inactive accounts after 12 months — list hygiene critical. |
| Microsoft (Outlook/Hotmail) | 14.4% | 77.4% | 15.1% | Toughest to reach. Spam placement sustained longer — slower to recover. Double whammy for B2B. |
| Apple Mail | 3.6% | 82.0% | 10.8% | No official bulk sender requirements yet, but benefits from halo effect of other providers' standards. |

*\*Yahoo market share includes ATT and Comcast following acquisition. Source: Validity 2026 Email Deliverability Benchmark Report.*

### What they are all actually looking at

Despite the differences, all providers are fundamentally asking the same question: do the people receiving emails from this sender want them?

They assess this through a combination of signals and events.

Negative events are large-scale things that happen suddenly: a bounce spike (indicating list hygiene problems), a spam complaint surge (indicating subscriber rejection), or a dramatic volume increase overnight (a pattern associated with compromised accounts and spam operations). These cause sharp, immediate reputation damage.

Negative signals are the ongoing behavioural patterns that accumulate over time: consistent deletions without opening, emails being moved to junk by recipients, repeated non-engagement from large portions of the list. These erode reputation gradually rather than all at once.

Positive signals do the opposite: opens, clicks, replies, emails being moved from spam back to the inbox, subscribers filing your emails to folders they revisit. These build reputation over time.

The providers are not expecting everyone on your list to engage every time. They understand how the inbox works. What they are watching for primarily is the absence of negative signals, combined with a minimum baseline of positive engagement. When negative signals consistently outweigh positive ones — or when a negative event damages the balance sharply — spam placement follows.

### Gmail: fast to suppress, fast to recover

Gmail holds 42.9% of global mailbox market share according to Validity's 2026 report, making it the most important provider for most senders. Gmail achieved an average inbox placement rate of 89.8% in 2025 — up 2.6% from the previous year.

Gmail's filtering is engagement-weighted and responds quickly in both directions. A negative event can suppress you to spam relatively fast — but recovery, if you address the underlying causes, can also happen faster than with Microsoft.

In November 2025, Google enforced stricter guidelines around non-compliant bulk senders, causing widespread spam placement issues for programmes that had not kept pace with the requirements. And in January 2026, Google's spam checking and labelling system degraded for around five hours, causing significant disruption — Google later published a root cause analysis on this incident.

Gmail's 2026 outlook is worth noting: the integration of Google Gemini into Gmail means AI will increasingly sort emails by relevance and engagement, bringing high-priority messages to the top. Programmes with lower engagement will become progressively less visible, regardless of technical compliance.

### Microsoft: the hardest provider to reach

Microsoft — which includes Outlook and Hotmail — is consistently the toughest major provider for deliverability. Its average inbox placement rate in 2025 was 77.4%, meaning a spam placement rate of 15.1%. That is more than double Gmail's.

What makes Microsoft particularly challenging is the sustained nature of its spam placement. When Microsoft decides your emails belong in spam, it tends to stay that way for longer than Gmail. The recovery is slower. Which means problems that might be manageable at Gmail can become much more serious in programmes with a high Microsoft audience proportion.

Microsoft introduced new bulk sender requirements in 2025, leading to Q2 improvements for senders who were already compliant. But the overall picture for B2B senders — who have a high concentration of Microsoft addresses — remains significantly harder than consumer-facing programmes.

### The B2B double whammy

For B2B senders specifically, the deliverability challenge is even more complex than the provider-level picture suggests — because most corporate email environments sit behind two layers of filtering, not one.

The first layer is the hosting platform: Office 365 holds 60.3% market share, Google Apps 35.9%. These filter similarly to their consumer counterparts, applying engagement-based and reputation-based filtering to inbound email.

The second layer is the corporate security filter: Proofpoint (50.5% market share, with an even higher concentration at enterprise level), Mimecast (20.7%), and Cisco (11.8%). These are configured by IT administrators and can apply unique rules — blocked sender lists, enhanced spam thresholds, quarantine policies, and inbound gateway restrictions that are entirely separate from anything you can test or monitor through standard tools.

According to Validity's 2026 report, B2B inbox placement at filtering companies declined 5.8% in 2025. The true picture may be even worse, because emails held in corporate quarantine may not surface in any placement data — they simply disappear into an admin queue that nobody checks.

I covered the corporate security filter problem in more depth in the ABM and email strategy blog — specifically how simultaneous multi-stakeholder sends can trigger these filters in ways that look identical to a spam campaign. If you are sending to enterprise or corporate B2B audiences, that context is essential reading.

## What changed in 2025 — and what it means for 2026

2025 was a significant year for email deliverability, and the changes have permanent implications for how sender reputation is built and maintained going forward.

Bulk sender requirements became mandatory across all major providers

Gmail and Yahoo had already introduced mandatory bulk sender requirements in 2024. Microsoft followed in 2025. For the first time, the three largest mailbox providers in the world all require the same core set of standards from bulk email senders:

- DMARC authentication at a minimum of p=none, with p=quarantine or p=reject strongly recommended
- SPF and DKIM properly configured and passing
- One-click unsubscribe implemented and honoured promptly
- Spam complaint rates maintained below 0.1% for best performance (the old 0.3% threshold is now considered insufficient)

The good news: Validity's data shows that global inbox placement improved to 87.2% in 2025 — a 3.7% uplift year over year — partly because these requirements pushed the industry toward better practices. Senders who were already compliant saw their placement improve as providers recognised their DMARC status.

The bad news: programmes that were not compliant faced enforcement. November 2025 saw strengthened enforcement of non-compliant bulk senders across Gmail, with significant temporary and permanent reductions in inbox placement for programmes that had not kept pace.

Global sending volume decreased for the first time

For the first time in the history of Validity's benchmark reporting, global email sending volume decreased year over year in 2025. This reflects two things: the effect of mandatory compliance requirements causing some senders to send less indiscriminately, and the influence of AI-powered targeting helping marketers send smaller, more relevant campaigns.

This is directionally significant. The industry is — slowly, unevenly — moving away from volume-based email toward engagement-based email. The providers are pushing this through their filtering behaviour. The data is supporting it. And the programmes that adapt to this reality will consistently outperform those that do not.

Spam complaints reached a 2025 average of 0.06%

Validity's data shows that the average spam complaint rate across their network was 0.06% in 2025 — well below the 0.1% threshold. This improvement was driven by the same factors: mandatory requirements pushing better list hygiene, and AI-driven segmentation helping send more relevant content.

But 0.06% is a network average. Individual programmes vary enormously. And the expectation is clear: under 0.1% is now the baseline expectation. Under 0.3% used to be considered acceptable. It no longer is. Programmes operating in that range should treat it as an urgent signal, not a comfortable cushion.

## How to actually know if you have a spam placement problem

Here is the honest answer: you cannot know from your ESP dashboard alone. Your delivery rate tells you almost nothing about inbox placement. Even open rates — already unreliable for other reasons — cannot tell you whether the email landed in the inbox or the spam folder before someone opened it.

Knowing your spam placement rate requires dedicated inbox placement testing.

Inbox placement testing works by sending your email to a set of seed addresses — email addresses at real providers that monitoring tools control — and then checking where the email landed. Did it arrive in the inbox at Gmail? In the spam folder at Microsoft? Was it missing entirely at Yahoo?

These tests need to be run regularly — not as a one-off check before a major campaign, but as a consistent monitoring practice — because spam placement can change daily, hourly in some cases, based on recent sending behaviour and reputation signals. You need trend data, not a point-in-time snapshot.

Tools that provide this kind of monitoring include GlockApps, Mail Tester, and Validity's own platform. Google Postmaster Tools (for Gmail specifically) provides complaint rate and domain reputation data directly from the source. Yahoo Sender Hub and Microsoft's Smart Network Data Services (SNDS) provide equivalent visibility for their platforms.

The indicators you can see without specialist tools — sudden drops in open rates, unusual bounce patterns, campaign revenue unexpectedly underperforming — are proxy signals, not direct measurements. They tell you something may be wrong. They do not tell you what, where, or how serious.

### What to look for when you do test

When you run inbox placement tests and monitor reputation data, here is what to watch:

- Spam placement rate by provider — broken out separately for Gmail, Microsoft, Yahoo, and any other providers significant in your audience. A 10% overall spam placement could be 5% at Gmail and 20% at Microsoft — very different implications.
- Trend over time — a 15% spam placement rate that has been stable for three months is a different situation from 15% that was 5% three months ago. Direction matters as much as level.
- Complaint rate — ideally from Google Postmaster Tools directly, which shows you complaint rates as Google sees them rather than as your ESP estimates them
- Unknown user rate (hard bounces) — consistently above 2% is a serious list hygiene signal. The global average in 2025 was 1.46% according to Validity's data.
- Domain reputation in Google Postmaster Tools — Google rates your domain reputation as High, Medium, Low, or Bad. Low or Bad indicates active placement problems.

## What to do when your spam placement is a problem

This is where most blog posts end with a list of tips. I am going to be honest with you instead.

Understanding that emails go to spam, and knowing the thresholds, is one thing. Knowing what to do when you have a real problem — how to diagnose the root cause, how to build a recovery plan, how to implement that plan without making things worse, how to monitor progress — is a completely different and much harder thing.

Most marketers I work with who have a deliverability problem know something is wrong. They do not know where to start fixing it. And when they are under pressure from their boss to just keep sending, they do — often making the problem significantly worse.

The most common responses I see that compound the problem:

- Sending a large re-engagement campaign to the whole disengaged list — this generates exactly the kind of negative event that makes spam placement worse, not better
- Reducing send frequency without addressing the underlying list or reputation issues — this manages the symptom without treating the cause
- Assuming it will sort itself out — sometimes it does, for short-term spikes. For sustained problems, it almost never resolves without intervention
- Adding more people to the list to try to improve the engagement ratio — this imports more risk, not more engagement

What actually works is a structured approach: diagnosing the specific cause or causes, addressing list health first, rebuilding sender reputation through a deliberate warm-up plan, and monitoring through the recovery to make sure the trajectory is improving.

That process requires understanding deliverability deeply enough to make the right decisions at each stage. Not just knowing that sender reputation matters — knowing how to measure it, how to interpret it, what actions move it in the right direction, and what timeline to expect.

## The bottom line

Some of your emails are always going to spam. That is normal. What matters is:

- Whether it is within the normal healthy range (zero to 15%)
- Whether it is sustained or a short-term event
- Whether your complaint rate is well below 0.1%
- Whether you are actually measuring inbox placement — not just relying on your ESP delivery rate
- Whether you have a strategy for maintaining and improving sender reputation over time, not just reacting when problems surface

The email landscape in 2026 is more complex than it has ever been. Microsoft, Gmail, and Yahoo all have mandatory requirements. AI-driven filtering is making engagement more important than ever. Global sending volume is decreasing as providers push senders toward quality over quantity. And the corporate security infrastructure sitting in front of B2B inboxes adds an entire layer that most standard testing cannot even see.

Understanding all of this — properly, not just at the surface level — is what separates programmes that consistently reach the inbox from programmes that wonder why performance is declining while their dashboard shows a 98% delivery rate.

Deliverability is not a technical problem you solve once. It is a discipline you maintain.
