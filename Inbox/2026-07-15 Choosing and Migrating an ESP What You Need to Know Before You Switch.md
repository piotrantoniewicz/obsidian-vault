---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/choosing-and-migrating-an-esp-what-nobody-tells-you-before-you-switch?utm_medium=email&_hsenc=p2ANqtz-9YgpuyBa6VFLsE2qr3UxvW_r0pG0KRrdBNkQNBdSx1F9iscXXCxFMa928mb0Xnd4A2STS1rPzaPXuruBbotOqDtKjdyydIFVzLDc7tc5SWbx5qK1Y&_hsmi=140873362&utm_content=140822143&utm_source=hs_email"
published: 2026-07-15
created: 2026-07-16
tags:
---


I want to start with a conversation I have had WAY too many times.

An organisation switches email platforms, the sales process was smooth, the demo looked great, the onboarding team were helpful. They go live. And then, a few weeks later, the cracks start showing. Automations that were running fine are not firing. Contacts who should be excluded are getting emails. The forms are not routing correctly. The deliverability has taken a hit nobody warned them about. And the engagement metrics in the new platform look completely different from the old ones, in ways nobody can explain!

They are not back to square one — they are further back than square one, because now they have a broken programme, a team under pressure, and a platform contract they have committed to.

This happens constantly (all the flipping time). And almost all of it is preventable — not by choosing the right platform, but by understanding what choosing a platform actually involves and doing the right things in the right order before, during, and after the switch.

This blog covers all of it. How people get the selection wrong. The questions to ask before you sign anything. What "plug and play" actually means versus what people assume it means. What a migration actually involves. And the ten things most likely to go wrong — because I have watched them go wrong, repeatedly, and the pattern is almost always the same.

## How people choose the wrong ESP and why the sales process is designed to let them

The first mistake happens before anyone has touched a new platform. It happens in the selection process and it is almost entirely driven by how ESP sales and demos are designed to work.

The demo shows you the best version of the platform. Features are demonstrated in ideal conditions, with clean data, perfect integrations, and a presenter who knows exactly which buttons to press. The platform looks simple. Powerful. Exactly what you need.

What the demo does not show you: how it performs when your actual data is imported with all its inconsistencies. How it behaves when your specific integrations are connected. What the experience is when something breaks and you need support. What the platform looks like six months after you go live and the onboarding team has handed you over.

Most buyers walk out of a demo thinking about features. The right question is not whether it has the feature you need. The right question is whether it handles your specific situation, with your data, your integration dependencies, and your team capability level.

### The feature trap

*Buying based on what a platform can do rather than what it can do for you*  
  
Every mainstream ESP can do most of what you need. The features are not the differentiator. What differentiates them is how those features work in your context, with your CRM/CDP, your forms, your contact fields, your automation logic, your team's technical comfort, and your commercial calendar.

I have seen companies choose platforms because they have a feature they were excited about in the demo, then discover that feature requires a plan tier they cannot afford, or depends on a data structure they do not have, or works completely differently in practice from how it worked in the presentation. The feature existed. It just did not exist for them, in the way they needed.

### "Plug and play" — what it means

*The phrase that causes more problems than any other in ESP sales*  
  
"Plug and play" in ESP sales language means: this integration exists and has been built. It does not mean: this integration will work seamlessly with your specific data setup, in real time, without configuration, for your specific use case.

There is a world of difference between a static integration — one that syncs data on a schedule, or requires a manual export/import, or only pushes data in one direction — and a real-time, bidirectional, dynamic integration that reflects live CRM data in your email platform at the moment an automation fires.

The distinction matters enormously for how you design automations. If your integration is a sync rather than real-time, any flow that depends on a contact's current CRM status — deal stage, lifecycle stage, a field that changes when someone does something — may not work the way you expect. The data it is checking may be hours old. The conditional logic fires against a snapshot, not live reality.

Most teams only discover this after they have built their automations and started testing. At which point the flow needs to be redesigned, sometimes fundamentally.

## The questions to ask before you sign, that most people do not ask

The questions that matter are not in the feature list. They are in the operational detail. Here is what to ask every ESP before you commit.

On your specific integrations

- Does this integration with \[our CRM / our forms / our ecommerce platform\] work natively or does it require Zapier, a middleware tool, or a custom API connection?
- Can you show me the technical documentation for this integration — not the sales page, the actual integration docs?
- Have you spoken to any of your current customers who use this specific integration with this specific CRM version? Can we speak to one?
- What data does not sync through this integration — what are the known limitations?
- If the integration breaks, whose responsibility is it to fix it — yours, ours, or the other platform?
- Do unsubscribes in your platform automatically update our CRM, and vice versa? Show me exactly how.

On data and contacts

- Can we import our historical performance data — original list creation date, historical engagement — or does that all reset to zero?
- Can we override your native "date added" field with our existing contact creation dates, or do we need custom fields to preserve historical records?
- How do we import suppression lists — unsubscribes, hard bounces, spam complainants — so they are flagged correctly in your system and not just imported as contacts?
- What happens to a contact who unsubscribes in your platform — how does that feed back to our CRM?

On deliverability and IP setup

- Are new customers put on a shared IP pool? Is it a separate IP pool for new customers, or the same one used by established senders?
- What is the reputation of your shared IP pool? Can I see recent deliverability data?
- What warm-up support do you provide — do you give us a warm-up plan, or are we on our own?
- What monitoring do you provide during the warm-up period?
- What is your policy if our deliverability deteriorates after migration?

On support

- What does onboarding include, and when does it end? What happens on day sixty when we have a technical problem?
- What is your average support response time on \[our plan tier\]? Not your SLA target — your actual average.
- Is there a dedicated account manager, or do we go into a general support queue after onboarding?
- Who do we contact if we have a deliverability emergency — something we need resolved in hours, not days?

What a migration actually involves and why it takes longer than you think

A migration is not moving your email list from one place to another. That is the smallest part of it.

What you are actually moving is an entire email infrastructure: every contact, every field, every suppression list, every form connection, every automation, every template, every integration, every Zapier connection, every trigger, every piece of conditional logic, plus setting up authentication on a new domain, warming up a new IP, rebuilding benchmarks, and monitoring everything daily for weeks after go-live.

When I scope a migration with a client, the work falls into six phases. Each one has to be done before the next one starts. Skipping ahead, building automations before you know your integration is real-time, for example, or importing contacts before you have imported suppressions — is where the expensive mistakes happen.

### Phase 1: Pre-migration audit

*Before you touch the new platform, understand exactly what you have*  
  
The first thing to do is not open the new platform. It is document everything about your current one. Export all your campaign performance data now — because once you lose access, it is gone. Note your current open rate, click rate, unsubscribe rate, and complaint rate by email type. These are your benchmarks — you cannot know whether the new platform is performing well or badly unless you know what "normal" looked like on the old one.

Run an inbox placement test before you move. If you have an active deliverability problem, migrating will make it worse, not better. Moving to a new IP while your sending reputation is damaged is like moving house to escape a bad credit score — the debt comes with you. Resolve spam issues before you switch, not after.

Check your SPF, DKIM, and DMARC records. If they are not correctly set up now, you are starting the migration from a weaker position than you should be.

### Phase 2: Understanding the integration before building anything

*The step most teams skip and the one that causes the most problems*  
  
Before you build a single automation in the new platform, you need to know exactly how your integration works. Get the technical documentation — not the sales page, the actual integration docs — and read it.

The critical question is whether your integration is real-time or a sync. If a contact's CRM deal stage changes, when is that reflected in the ESP? Immediately? In an hour? At the next daily sync? The answer determines what kinds of automations are possible and what kinds need redesigning.

Map every form on your website that captures email addresses. For each one: how does it currently connect to the ESP? Will that connection still work with the new platform? If you are using Zapier to connect forms to your current ESP, those Zaps point to the old platform — they will need to be cloned and updated. Clone them, do not edit them. You need the originals running until go-live day.

### Phase 3: Data migration — in the right order

*The order is not optional!*  
  
When you import your contacts, the order matters more than almost anything else. The first thing you import into the new platform is not your active subscribers. It is your suppression lists.

Your unsubscribes must be imported as suppressed contacts before any active contacts go in. Your hard bounces must be imported as suppressed. Your spam complainants must be imported as suppressed. If you import active contacts first and then your suppressions, there is a window — even a brief one — where the platform does not know those people are suppressed. If an automation fires in that window, you risk sending a marketing email to someone who previously unsubscribed, which is a compliance problem and a legal risk under PECR and UK GDPR.

Build your field mapping document before you import anything. Go through every contact field in your current ESP — every native field, every custom field — and map it to the equivalent in the new platform. Fields that do not have a direct equivalent need to be created in the new platform before import. You cannot map data to fields that do not exist yet.

### Phase 4: The warm-up — the thing everyone underestimates

*You are not just moving lists. You are rebuilding an IP reputation from zero.*  
  
When you move ESP, you almost certainly move to a new sending IP — or a new IP pool. Inbox providers have seen behaviour from your old IP over months or years. They have no history of your new IP at all. Suddenly sending your full list volume from a brand new IP, with no sending history, looks from the outside exactly like the pattern associated with spam operations. Even if every contact is legitimate and permissioned, the providers do not know that yet.

The warm-up plan is the process of building that reputation gradually. You start by sending only to your most engaged subscribers — the people who open and click reliably, from the new platform, while continuing to send to the rest of your list from the old platform. Week by week, you increase the proportion sent from the new platform, monitoring deliverability as you go. If placement stays healthy, you increase. If it drops, you pause and investigate.

A standard warm-up takes eight to twelve weeks to reach full volume safely. During that period, you need to keep your old ESP active. This surprises people, they expect to switch cleanly on day one. But the overlap is essential. You cannot safely send your full programme from the new platform on week one without risking your deliverability.

The thing that most often derails a warm-up plan is the commercial calendar. If you have a major campaign, a peak period, or a high-volume appeal coming up within twelve weeks of your go-live date, either delay the go-live or plan to send that campaign from the old platform. Sending high volume from an unwarmed IP during a critical commercial period is a deliverability risk that can take months to recover from.

## The ten things most likely to go wrong and how to avoid them

These are not hypothetical. Every one of these is something I have seen happen, more than once, in real migrations.

1\. The integration was a sync, not real-time — and nobody checked

Conditional automations were built assuming the CRM data would be live. The sync runs once every four hours. Flows fire against stale data. Contacts who should be excluded are included. Contacts who have moved past a certain stage get emails that are no longer relevant. The rebuild takes weeks.

2\. Suppression lists were not imported before active contacts

A re-engagement automation fires for a contact who unsubscribed eighteen months ago. The compliance team finds out. The platform did not flag the issue because the contact was imported as active before the unsubscribe list was processed. A preventable PECR problem.

3\. The warm-up was skipped or rushed

The team cancelled the old ESP on go-live day and sent the full list from the new platform in week one. Inbox placement at Outlook dropped to below 60% within ten days. The recovery took three months of reduced sending and careful list management. The peak campaign they were gearing up for had to be delayed.

4\. Forms were not remapped — new contacts stopped flowing

The Zap that connected the website contact form to the ESP was pointing at the old platform. Nobody noticed for three weeks because the old platform was still receiving submissions and nobody was checking the new one. Three weeks of new contacts went into a system the team had moved away from.

5\. Historical performance data was not exported before losing access

The old platform contract was cancelled before the performance export was done. The team had no benchmarks for the new platform — no way to tell whether open rates were normal, low, or indicating a problem. Twelve months of performance data, gone.

6\. Dynamic flows were rebuilt without confirming the data was available

An onboarding flow was built with conditional logic that checked a custom field. The field had not been mapped correctly in the data import and was blank for most contacts. Every contact hit the same branch of the flow, regardless of their actual status. The team did not notice for weeks because the flow appeared to be working.

7\. Go-live landed during a peak period

A retailer scheduled their migration go-live in September with a peak campaign in November. The eight-week warm-up period was not complete when the November send needed to happen. They were forced to split the peak campaign between two platforms at the worst possible time, with double the complexity and half the monitoring attention.

8\. Metrics were compared directly between platforms without understanding the differences

Open rates on the new platform looked significantly higher than on the old one. The team assumed performance had improved. It had not — the new platform was counting bot opens from preview panes as opens, while the old platform was filtering them out. They were not measuring the same thing. Benchmarks were set wrong, and performance problems that emerged later were missed because the baseline was inaccurate.

9\. The integration architecture was not documented

Six months after the migration, the person who ran it left. Nobody else knew how the forms were connected, which Zaps were running, what the field mapping had been, or how the conditional flows worked. The programme ran on institutional knowledge that walked out the door. The next migration — or the next problem — required starting from scratch.

10\. The old platform was cancelled too soon

Cancel it too early and you lose access to historical data, you lose your fallback if the new platform has problems, and you lose the ability to run campaigns from a warmed-up sending infrastructure during the overlap period. Eight weeks minimum of clean deliverability data from the new platform before you cancel. Ideally twelve.

## Summary

Platform migrations go wrong because they are treated as technical projects with a go-live date, rather than as programme transitions that require planning, sequencing, monitoring, and patience.

The checklist I have built for this, linked above, covers everything in the right order. But the mindset matters as much as the sequence. The questions to ask before you sign. The integration audit before you build. The suppressions before the active contacts. The warm-up before the full volume. The old platform kept running until you have proof the new one is working properly.

Every shortcut in a migration becomes a problem later. Sometimes a small one, sometimes a large one. The teams that navigate migrations cleanly are not the ones with the best ESP — they are the ones who took the process seriously enough to do it in sequence, ask the uncomfortable questions early, and resist the pressure to go live before they were ready.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.