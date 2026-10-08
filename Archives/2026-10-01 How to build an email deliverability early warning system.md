---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/how-to-build-an-email-early-warning-system-so-you-find-out-before-it-costs-you?utm_medium=email&_hsenc=p2ANqtz-9hMfq3a2HfgX_VsM32MnwLCd2umM7MDCGqcW7gfJnJ6vAYNfOIFOCiXexgidFKT98L-JaTpK9BnojFPBpBFLQtLCJX6WgI5sIlbmR-dMsufA2DbSw&_hsmi=147661112&utm_content=147658469&utm_source=hs_email"
published: 2026-10-01
created: 2026-10-08
tags:
  - "digital-campaigning"
---


Most businesses find out they have a deliverability problem when something dramatic happens OR when results drop so much over time that people conclude that "the channel just doesn't work anymore" (shocker it still does or I wouldn't be in a job).

Somebody notices email is down last quarter, a meeting gets called, somebody goes looking and discovers open rates started sliding four months ago, complaints crept up in March, and placement at one provider has been falling since before that. By then the problem is not a wobble; it is a condition, and recovery takes months (and sometimes years) rather than weeks.

Every one of those signals was available at the time. Nobody was watching for them, because watching requires knowing what to watch, what normal looks like, and what should make you stop.

Which is what an early warning system is. Not a tool you buy, a handful of numbers with thresholds against them and somebody whose job it is to look.

## The cost

## Why finding out late is so much worse than it used to be

- Recovery got slower. What used to take a few weeks of clean sending now routinely takes months, because providers have longer memories and less patience than they did.
- Enforcement became mechanical. Gmail now issues hard rejections rather than quietly junking, so the consequences arrive faster and with less warning.
- Damage compounds. Reduced placement means fewer positive signals, which means worse reputation, which means less placement. Left alone it accelerates.
- And the cheap window is at the start. A problem caught in week one is a conversation. The same problem caught in month five is a project with a budget.

## What to watch

## Leading indicators move first, lagging ones confirm it later

The mistake almost everybody makes is watching only the lagging indicators, which are the ones on the dashboard by default.

### Leading indicators, which move first

- Spam complaint rate, per send and per provider. The single most important number you have, because it is the one with an enforced ceiling behind it and it moves before anything else.
- Complaint count, not just rate. Particularly if your list is small, where percentages behave strangely and three annoyed people can put you over a threshold.
- Hard bounce rate, and any sudden change in it. A spike is a data quality signal and it is usually telling you something arrived in your list that should not have.
- Soft bounce and deferral patterns. Repeated deferrals from one provider are that provider throttling you, which is an early sign of a reputation problem rather than a technical one.
- Authentication pass rates. A drop means something changed in your DNS or your sending setup, frequently without anybody telling you.
- Placement by provider. Inbox, spam and other or promotions, tracked as a trend. The most direct measure and the one fewest people have.
- First-email engagement on new subscribers. A leading indicator of acquisition quality, and it moves long before list-wide engagement does.

### Lagging indicators, which confirm it afterwards

- Open rate. Unreliable as a number, useful as a trend, and by the time it has visibly fallen the cause is weeks old.
- Click rate. More reliable than opens and still a lagging measure of something that already happened.
- Revenue and conversion. The number that gets everybody's attention and the last one to move.

Nothing wrong with the lagging set. The problem is a monitoring regime built entirely from it, which by definition cannot warn you about anything.

## The thresholds

## Green, amber, red, stop

An alert needs a number attached or it is a feeling. Mine are more conservative than the published ceilings, because the published ceilings are the point at which you get punished rather than the point at which you should be worried.

### Spam complaint rate

- Under 0.02% is fine. Carry on.
- 0.02% to 0.1% is amber. Look at it this week. Which segment, which send, what changed.
- 0.1% to 0.3% is red. Stop broad sending and investigate properly. You are in the zone where providers are paying attention.
- Above 0.3% is a stop. Pause everything non-essential. You are in active enforcement territory and every further send makes it worse.

### Hard bounce rate

- Low and stable is fine. The absolute number matters less than the stability of it.
- Any sudden increase is amber, whatever the level. A jump means something entered your list or something changed in your data. Find out which before the next send.
- Sustained elevation is red. You are telling providers you do not know who is on your list.

### Spam placement rate, per provider

- Up to around 15% is normal. Every business lands in spam to some degree and this is the ordinary state of the channel.
- 15% to 25% is amber. Watch it and look for the cause.
- 26% to 50% is red. Real audience impact. A meaningful proportion of your list is not seeing you.
- Over 50% is a stop. Get help.

### Everything else

- Authentication pass rate below 100% is amber immediately. There is no acceptable level of authentication failure, so any reading other than clean means something to investigate.
- Unsubscribe rate compared only against the same email type. A deliberate clear-out is supposed to have a high rate. A newsletter doubling its usual rate is a signal.
- Engagement on a cohort falling faster than previous cohorts. Amber, because it says something changed in acquisition or in the onboarding experience.

## Building it

## Without buying anything

1. Set up Google Postmaster Tools and verify your domain. Free, twenty minutes, and it gives you spam complaint rate, authentication pass rates, delivery errors and compliance status for the provider handling most of your consumer list.
2. Set up Microsoft SNDS. Less generous with data and worth having, particularly if any part of your audience is B2B.
3. Export the same handful of metrics from your ESP every week. Complaint rate and count, bounce rate, unsubscribe rate, by campaign type and by segment. Same day each week so the series is comparable.
4. Put it in one sheet with conditional formatting. Green, amber, red against your thresholds. Unsophisticated, free, and it will catch almost everything a paid tool would.
5. Add a placement reading on a regular cadence. Seed testing or inbox placement tooling, run consistently rather than occasionally, because the value is in the trend.
6. Name the person who looks, and when. Fifteen minutes a week in somebody’s calendar. A system nobody is accountable for checking is a spreadsheet, not a warning system.

### And take the baseline now

The part people skip and then regret. An alert is a comparison, so you need to know what your normal looks like before anything goes wrong.

Take your readings during an ordinary month, write them down with the date next to them, and keep them somewhere you will find them in November. Without that, a wobble becomes a fortnight of argument about whether it is even unusual. With it, you can answer in ten minutes.

## The response

## An alert with no plan attached is just anxiety

Decide in advance what happens when each level fires, because deciding in the moment produces panic sending or paralysis, and both are worse than the original problem.

Amber: look at it this week

- Which segment, which send, which provider.
- What changed in the last fortnight: volume, audience, content, acquisition source, any technical change.
- Is it one send or a trend across several.
- No action required yet beyond understanding it.

Red: change the sending

- Pause broad sends to the affected group.
- Tighten exclusions, particularly the dormant and low-engagement segments.
- Reduce volume and hold it there until it settles.
- Check authentication and blocklists before assuming it is behavioural.

Stop: everything non-essential pauses

- Transactional continues. Marketing does not.
- Named person makes the call, as agreed in advance.
- Investigate properly rather than trying things.
- Expect weeks, not days, and plan communication accordingly.

## False alarms

## What not to react to

- A single data point. One send is not a trend. Look at three before you conclude anything.
- Seasonal variation. August and late December behave differently everywhere. Compare against the same period last year as well as against last month.
- Percentage noise on small volumes. Which is why the absolute count matters for smaller senders.
- A deliberate clear-out. If you sent an email designed to remove people, a high unsubscribe rate is the email working.
- One provider moving while the others hold. Worth investigating and frequently a provider-specific change rather than a problem with you.

The discipline is to watch everything and react to patterns. A monitoring system that fires constantly gets ignored, which leaves you worse off than having no system at all.

## The conclusion

Deliverability problems almost never arrive suddenly. They build, quietly, across weeks, leaving signals the whole time, and the reason businesses get caught out is not that the signals were hidden. It is that nobody had decided which numbers mattered or what would count as worrying.

Fifteen minutes a week, six numbers, a set of thresholds you agreed while nothing was wrong, and a plan for what happens when one of them fires.

Not sophisticated, and it is the difference between a conversation in week one and a recovery project in month five.

### Further reading from The Vault:

- [How to Know Your Sender Reputation](https://weareastral.co.uk/thevault/how-to-know-your-sender-reputation.-why-you-cannot-look-it-up-any-more-and-how-to-work-it-out-instead)
- [Email Contingency Planning](https://weareastral.co.uk/thevault/email-contingency-planning-what-to-do-when-you-get-it-wrong-and-the-emails-you-should-have-written-before-you-needed-them)
- [Who Owns Email Deliverability? Not IT](https://weareastral.co.uk/thevault/who-owns-email-deliverability-not-it)
- Email Operations: The Processes That Turn a Pile of Campaigns Into a Programme
- [Email List Churn: What's Normal, and What Isn't](https://weareastral.co.uk/thevault/email-list-churn-whats-normal-and-what-isnt-and-when-should-you-stop-emailing-someone)
- [The State of Email Deliverability in 2026](https://weareastral.co.uk/thevault/the-state-of-email-deliverability-in-2026.-and-what-i-think-happens-in-2027)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.