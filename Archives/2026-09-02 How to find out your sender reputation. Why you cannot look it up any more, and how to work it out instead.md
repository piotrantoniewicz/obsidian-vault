---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/how-to-know-your-sender-reputation.-why-you-cannot-look-it-up-any-more-and-how-to-work-it-out-instead?utm_medium=email&_hsenc=p2ANqtz-9xWT80QQ3JBJozT73QxNkFY8opjPRIhrH9NdZFNZ2cXu9LnyNc_6v1H52AmJsTI9kYoK0MFnXG5B6D_6WEPYMvDU6gZk7AcjpnZXmXpwdNGgIQYwQ&_hsmi=144797544&utm_content=144791947&utm_source=hs_email"
published: 2026-09-02
created: 2026-09-03
tags:
  - "digital-campaigning"
  - "fundraising"
---


“Where do I check my sender reputation?” is one of the questions I get asked most, and the answer disappoints people every single time.

Nowhere. You cannot check it. Not directly, not as a number, not ever.

There is no global sender score. There is no site you can put your domain into that will tell you the truth, and the sites offering to do exactly that are nonsense. Google Postmaster Tools used to show you a version of it, and that has gone too: the Domain and IP Reputation dashboards were retired along with the old interface at the end of October 2025, the new version went generally available in February 2026, and the coloured High, Medium, Low and Bad labels people used to screenshot for their monthly report do not exist any more.

So the position is that nobody, including me, can hand you your sender reputation as a figure. What you can do is work it out, and working it out is a proper discipline with a method behind it. That is what this post is about.

## The definition

## What sender reputation is

Sender reputation is a trust score that mailbox providers assign to your sending domain and your IP, and those are two separate scores.

- **The sending domain.** The bit after the @ in your from address. If you send from beth@astral-digital.co.uk, your sending domain is astral-digital.co.uk. The part you own, and the part that follows you around wherever you go.
- **The IP.** The actual server your email physically leaves from, a number like 192.168.x.x. Your ESP owns this, not you, unless you are on a dedicated IP.

Which matters more than it sounds, because domain reputation travels with you. Change platform and your history comes too, so switching ESP does not launder a bad record.

## The problem

## There is no single reputation; there are several, and they disagree

- No global sender score exists. Nobody maintains one, and there is no central authority scoring you as a sender.
- The lookup sites are nonsense. They exist, they will give you a number, and the number is not your reputation with anybody who matters.
- Google removed the closest thing we had. The Domain and IP Reputation dashboards went with Postmaster Tools v1 in October 2025. What remains in v2 is spam complaint rate, authentication status, delivery errors and compliance status, plus a Deliverability Analysis section added in June 2026 that gives you a verdict rather than a score.
- It changes daily. Whatever you establish today is a snapshot of a moving thing, which is why a single reading tells you far less than a trend.
- You have a separate reputation with every provider, and they do not talk to each other. Excellent with Yahoo and struggling with Microsoft is an entirely normal situation, and a blended figure would hide it completely.

### Different inboxes, different rules

- Gmail. Heavily engagement-driven and focused on the individual user. Do they want you, and what signals are they giving?
- Microsoft. User signals matter, but it is reputation-led. In B2B, corporate filters sit in front of the inbox before Microsoft even gets a say.
- Yahoo. The long game. Consistent, clean sending history wins over time.
- Corporate gateways. Mimecast, Proofpoint, Barracuda. A whole extra layer, more aggressive than the consumer providers, and offering you zero visibility.

## The mechanism

## What builds your reputation, and what decays it

Three things drive the whole picture: how you send, who you send to, and their reaction to your sending. Everything else is detail hanging off those.

The way I teach it is as a set of scales, weighed continuously by every provider you send to.

### Positive signals

- Opens, clicks and replies.
- Marking as not junk, or moving you into a folder.
- Stars, bookmarks and emoji reactions.
- Authentication set up correctly, meaning SPF, DKIM and DMARC.
- Consistent sending volume and cadence.

### Negative signals

- Spam complaints.
- Hard bounces.
- Deletes without opening, and ignored mail.
- Sudden volume spikes or changes to your sending pattern.
- Sending to spam traps.
- A new domain or IP sending at scale immediately.

Too many negatives over time and the providers trust you less, so you get pushed to spam more, which generates fewer positive signals, which pushes you further. Left alone, it becomes the vicious cycle where a team sends more to force results, generates more negative signals, watches placement fall further, and ends up having wasted the budget and needing months to recover.

### Signals and events are not the same thing

A distinction worth having, because it changes what you should worry about.

- A negative signal. One bounce, one spam complaint, one email deleted quickly after it arrived. On its own, close to harmless.
- A negative event. Lots of those negatives clustered into a short window. The clustering is what does the damage, and negative events are what you are trying to keep to a minimum.
- A positive signal. An open, a click, a reply, a move to folder, an emoji reaction. You want these consistently, over time.
- A positive event. Lots of positives clustered together. You want as many as you can get, and especially in the run-up to a big campaign, because they buy you headroom.

## Myths and facts

## What people worry about, and what deserves the worry

### Does not hurt your reputation

- Spam words like free and buy now.
- Unsubscribes. They are healthy and they protect you.
- One bounce or one complaint on its own.
- All-image emails, though they can reduce engagement and hurt you indirectly that way.
- Not having BIMI.

### Does hurt your reputation

- Spam complaints, particularly as events.
- Hard bounces and bad data.
- Sending patterns, both too little and too much.
- Poor email strategy and a poor sending approach.
- Your reputation with each provider, separately.

### Sending too little is a problem too

The one that surprises people. Gmail in particular starts to forget you, so go quiet for around four weeks and you cool off, with your reputation fading from disuse rather than from anything you did wrong.

Consistent, wanted, relevant sending keeps you warm, which is one of the quieter arguments for having good flows running underneath your campaigns. Too much, to the wrong people, and the negative events pile up instead.

## The method

## How to work out your reputation when you cannot see it

Since no number exists, what you are doing is closer to science than reporting. You gather every indicator available to you, look at how they move together, and build the most logical explanation for what you are seeing. A hypothesis, tested against evidence, revised when the evidence changes.

Which sounds harder than it is. The indicators are all obtainable, and once you know which ones matter the picture assembles itself fairly quickly.

### The core placement metrics

- Inbox Placement Rate (IPR%). The percentage of your email reaching the inbox, per provider.
- Spam Placement Rate (SPR%). The percentage landing in spam, per provider. Your single most important metric.
- Other or Promotions Placement Rate (OPR%). The percentage landing in tabs like Promotions, per provider.

### Reach and exposure

- Inbox reach. How many real people you reached this week, this month, or across ninety days. Dependent on your IPR and OPR.
- Inbox impressions. Total times you landed in front of somebody, so five emails to one person is five impressions. Also dependent on IPR and OPR.

### Complaints

- Spam Complaint Rate (SCR%). The percentage of recipients who marked you as spam. Providers set the thresholds, and Gmail calculates this daily.
- Spam Complaint Count (SCC). How many complaints, from how many people, in how short a window. The clustering is what hurts, which is why the count matters alongside the rate.

### Supporting signals your ESP does show you

- Bounce rate. Especially a spike in hard bounces, which is a list-quality signal.
- Open rate. Useful as a trend and distorted too much to be trusted as a number. Track big drops and spikes rather than the figure itself.
- Click rate. An engagement signal. Watch the trend, not the one-off.
- Unsubscribe rate. A health signal, not a deliverability harm.

### What normal looks like

Spam placement rate, per provider, is the number I would build your read around. Rough guidance on how many emails landing in spam is too many:

- 0 to 15 percent. Normal. Every business lands in spam to some degree and this is the ordinary state of things.
- 15 to 25 percent. Watch it.
- 26 to 50 percent. Real audience impact, and worth acting on now.
- Over 50 percent. Serious. Get help.

### One test is not a finding

The mistake that produces most of the wrong conclusions. A single placement test on a single tool is not enough and will mislead you, because the tools have limits and the providers are smart about seed lists.

What you want instead is multiple tools and rotating seed lists, capturing where you land each day across roughly thirty days, until you have a reliable inbox placement rate, spam placement rate and other or promotions rate for every provider. And crucially, the trend, because the trend answers the question that matters most.

### Reactive or consistent, which is the real diagnosis

- Reactive, which is most senders. Goes up and down. A big push or an email to disengaged people generates negative signals, placement dips for a week or two, then it bounces back because the underlying reputation is basically healthy. The fix is to be reactive with it and plan around it.
- Consistent, which is decayed. Never bounces back, or bounces back extremely slowly. Years of negative events have eroded your reputation to the point where it drags down even your most engaged people. The fix here is real intervention and a transformation, not a tweak.

Working out which of those two you have is the single most valuable thing your data can tell you, because the response to each is completely different and treating a decayed programme as a reactive one wastes months.

## The audit

## The six steps I use to build the hypothesis

When I audit an account, the reputation question sits inside a wider process, because you cannot interpret a placement number without knowing what produced it.

1. Situational analysis. Where are you today? Where has the list come from, who is on it, where are the negative signals coming from and how often, who in the business sends email, and what does your domain infrastructure look like. Everything captured here feeds the rest.
2. Technical checks. Confirm the plumbing is sound. Multiple tools and multiple methods to verify SPF, DKIM and DMARC are set up and running, plus blocklists: are you on any, and how do you get off.
3. Reputation and infrastructure. Work out how the providers see you. No real sender score exists, so you use your own data and signals to build a hypothesis per provider, and you map the domains and systems you send from along with the high-risk overlaps.
4. Data and sending hygiene. The big one, because your data is both your biggest blocker and your biggest opportunity. The make-up of your database by provider, list validation, bounces, complaints, acquisition sources, opt-in quality, spam-trap risk, corporate filters, and engagement analysis.
5. Inbox placement testing. The thirty day test rather than a one-off, using multiple tools and rotating seeds, producing your IPR, SPR and OPR per provider plus the trend.
6. Interpret and build the action plan. Weave it all into a root cause, then a prioritised plan. That plan lands in one of three modes: protect and monitor if you are healthy, transform and optimise if you are on the edge, or redeem if you are in real trouble.

## Your job

## Keep the scales tipped positive, consistently, over time

Which is the whole strategy in one line. You cannot control your reputation directly and you cannot look it up, so what you can do is keep generating more positive signals than negative ones, month after month, so that when something goes wrong you have the headroom to absorb it.

And something will go wrong. When it does, three moves:

1. Notice it. Which requires you to be watching the right indicators regularly rather than discovering the problem when somebody asks why revenue is down.
2. Understand it. Work out whether it is reactive or consistent, which provider it is affecting, and what changed in your sending around the same time.
3. Respond to it. Change the sending in response, rather than sending more in the hope of making the numbers up.

I call that a positive reactive strategy, and it is what separates the senders who recover in a fortnight from the ones who spend a year wondering what happened.

## The conclusion

You will never know your sender reputation the way you know your open rate, and the removal of the Postmaster reputation dashboards has made that more obviously true rather than newly true. It was always an inference. The dashboard just made it feel like a fact.

What you can do is build a hypothesis from the evidence available: placement per provider, complaints as both a rate and a count, bounce patterns, authentication health, and the trend across thirty days rather than the reading from one afternoon. Then keep the scales tipped positive and respond properly when they tip the other way.

Deliverability is the number one skills gap in our profession, according to my research across more than five thousand professionals globally, and this is precisely the part people were never taught. Not because it is difficult, but because nobody explained that the number they were looking for was never going to exist.

## Further reading from The Vault:

- [The State of Email Deliverability in 2026, and What I Think Happens in 2027](https://weareastral.co.uk/thevault/the-state-of-email-deliverability-in-2026.-and-what-i-think-happens-in-2027)
- [Email List Churn: What's Normal, and What Isn't](https://weareastral.co.uk/thevault/email-list-churn-whats-normal-and-what-isnt-and-when-should-you-stop-emailing-someone)
- [How to Prepare Your Email Deliverability for Black Friday and Peak Season](https://weareastral.co.uk/thevault/how-to-prepare-for-black-friday-and-peak-season-the-deliverability-version)
- [Not Sending Enough Email Is a Deliverability Problem Too](https://weareastral.co.uk/thevault/not-sending-enough-email-is-a-deliverability-problem-too)
- [Intentional vs Consequential Opt-Ins](https://weareastral.co.uk/thevault/intentional-vs-consequential-opt-ins)
- [The Ultimate Checklist for a Healthy Email Ecosystem](https://weareastral.co.uk/thevault/the-ultimate-checklist-for-a-healthy-email-ecosystem)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.