---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/what-email-deliverability-actually-is-and-the-3-metrics-that-really-matter?utm_medium=email&_hsenc=p2ANqtz-85f_r5yM4attOCqRRFLLeCO37qOY0WgyGuEsRUw13UAnAiFMpjDGyQUU26Ls0zVSeLnwTyOowrv4qhjTEsjHNB6CFFKdPw9E69n4RGzV4BlqBUN2A&_hsmi=137963204&utm_content=137755486&utm_source=hs_email"
published: 2026-03-04
created: 2026-06-10
tags:
  - digital-campaigning
  - fundraising
---


Let me start with something that might make you question your own approach.

If your ESP says 98% delivered, that tells you almost nothing about whether your emails are being seen.

Delivery and deliverability are not the same thing.

Delivery simply means the receiving server accepted the message, it does not mean the message reached the inbox. It does not mean the user saw it. It does not mean it wasn’t filtered, quarantined, rate-limited, or silently placed into spam.

Deliverability is about placement. It is about trust! It is about how mailbox providers view your domain over time.

And this is where the industry has created a huge amount of confusion.

## What Deliverability actually is:

At its core, deliverability is a trust score that mailbox providers build about your sending behaviour.

- It is not a single score.
- It is not universal
- It is not visible to you in full.

Gmail builds its own model. Microsoft builds its own model. Yahoo builds its own model. Corporate gateways layer their own filtering on top. They do not share data with one another, and they do not publish the exact mechanics of how they score you.

That is intentional.

Providers rely on combinations of:

- Authentication (SPF, DKIM, DMARC)
- Historical sender reputation (domain and sometimes IP)
- Per-recipient engagement signals
- Spam complaint behaviour
- Volume consistency and cadence
- Data quality (bounces, stale records, spam traps)
- Content and link analysis
- Infrastructure changes (new ESP, new domain, sudden spikes)

Authentication proves you are who you say you are.

It does not prove you are wanted.

Reputation is built from behaviour, and behaviour is built from patterns.

Deliverability is dynamic. It can change week to week, campaign to campaign, even segment to segment. It is influenced by context and consistency.

Which is why simplistic advice does more harm than good.

## You Can’t Trust Your Dashboards

This is the part that frustrates me the most (like SO much). Most marketers are operating entirely inside their ESP dashboard. They are looking at:

- Delivered %
- Open rate
- Click rate
- Bounce rate
- Unsubscribes

And they believe they are seeing the full picture, they are not.

Your ESP cannot see inside Gmail’s inbox classification system. It cannot see Outlook’s SCL scoring decisions. It cannot see when a corporate gateway quarantines your email before the user ever sees it. It cannot see tenant-level suppression at enterprise level.

What it can show you is whether the receiving server accepted the message.

That’s it.

As covered in my deliverability training, ESP health scores are not true inbox placement metrics. They are product-layer diagnostics, not provider-layer truth.

Let’s be really clear:

- Your ESP is a sending platform
- It is not a deliverability monitoring system (yet anyways)

Even spam complaint data inside ESPs is often incomplete, especially for Gmail, because feedback loops differ by provider.

So when marketers say:

“Our deliverability is fine.”

What they usually mean is:

“We have a high delivered rate.”

That is not the same thing.

## Why there is SO much misinformation out there

Deliverability advice online often falls into three traps:

1. Over-simplified percentage rules
2. Technical obsession without behavioural context
3. Generic benchmarks without provider nuance

The famous “keep your spam complaint rate under 0.1%” rule is a perfect example.

It sounds safe and it sounds measurable.

But it ignores volume context, pattern shifts, and complaint velocity.

Mailbox providers do not look at a percentage in isolation. They look at complaint counts, historical trends, spikes, and cross-campaign patterns.

If you suddenly generate a cluster of complaints in a short period, that pattern matters more than a static percentage!!

Deliverability is pattern based, not so much rule based.

## How Gmail, Microsoft & Yahoo actually see uou

Let’s zoom out and look at how the major mailbox providers assess you at a high level.

Gmail

Gmail places significant weight on per-recipient engagement signals.

They analyse:

- Whether users open
- Whether they click
- Whether they reply
- Whether they delete without opening
- Whether they mark as spam
- Whether they mark as “Not Spam”

They also monitor authentication and historical sending behaviour. New senders are often evaluated conservatively. Gmail may “trial” you in spam before gradually moving you to inbox if engagement signals improve.

Google Postmaster provides partial insight into spam rates and authentication health, but it no longer exposes full domain reputation scoring.

So you are inferring reputation indirectly.

Microsoft (Outlook / Office 365)

Microsoft operates with layered filtering.

They assign Spam Confidence Level (SCL) scores based on authentication, content, sender history, engagement, and machine learning signals. Emails scoring high on SCL are routed to junk or blocked.

Enterprise tenants add another layer.

Corporate gateways can:

- Rewrite links
- Sandbox attachments
- Quarantine messages
- Suppress domains tenant-wide

One employee marking your email as junk can influence filtering at organisation level.

And your ESP will still show “Delivered.”

This is especially critical in B2B environments where enterprise filtering is aggressive.

Yahoo

Yahoo leans heavily on historical reputation and consistency.

Sudden volume spikes or erratic behaviour can trigger filtering.

User feedback still matters significantly.

Long-term stability wins.

## The 3 Deliverability Metrics that you must track

Inside my framework, I reduce deliverability measurement down to three core metrics:

1. Inbox Placement Rate (IPR %)
2. Spam Placement Rate (SPR %)
3. Spam Complaint Count (SCC #)

Let’s unpack these properly.

## 1\. Inbox Placement Rate (IPR %)

Inbox Placement Rate is the percentage of emails that land in the inbox.

This is the only metric that tells you whether your emails are visible.

You cannot see this inside your ESP. You need seeded inbox testing across providers (Gmail, Outlook, Yahoo, corporate mailboxes), monitored consistently over time.

If inbox placement drops, performance drops — even if your “delivered rate” remains stable.

And many teams never notice until revenue declines.

## 2\. Spam Placement Rate (SPR %)

Spam Placement Rate is the percentage of emails landing in spam folders.

Inbox Placement Rate and Spam Placement Rate move together.

As negative signals increase or sending behaviour changes abruptly, spam placement rises. As spam placement rises, inbox placement falls.

You can be:

- 99% delivered
- Seeing “stable” open rates (distorted by privacy protections)
- And still have a significant portion of your emails landing in spam

Open rates, particularly in B2B environments, are unreliable due to image blocking, reading panes, and privacy features.

Relying on opens to diagnose deliverability is SO flawed.

## 3\. Spam Complaint Count (SCC #)

This is the metric most misunderstood.

What matters is not simply a percentage threshold.

What matters is:

- How many complaints are you generating per send?
- Over what time period?
- Is the pattern accelerating?
- Is there a spike tied to a specific campaign?
- Are complaints clustering by provider?

Mailbox providers feed complaint behaviour directly into their reputation systems in real time.

Even small numbers can trigger filtering changes if patterns shift.

And because Gmail complaint data visibility is limited, many teams underestimate their true complaint footprint.

Complaint count and complaint velocity are far more powerful signals than a static percentage.  

## Commercially if you don't know...

- Your Inbox Placement Rate
- Your Spam Placement Rate
- Your Spam Complaint Count by provider
- Your engagement thresholds
- Your infrastructure map

Then you are optimising creative inside a system that may already be filtering you.

You can improve subject lines all day long, but if you’re landing in spam, it doesn’t matter.

## Learn deliverability with me

If you want to become certified in deliverability, understand how audit your own deliverability, how to monitor, redeem, improve and everything in between - you can with me.

My live Deliverability Masterclasses (B2B + B2C) walk you through the full diagnostic framework.