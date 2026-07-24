---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/not-sending-enough-email-is-a-deliverability-problem-too?utm_medium=email&_hsenc=p2ANqtz-_W6KKu30DR0HBXpUJjytu0UZbBhpQ1q_QTgh7t-rF0Z-rUu6mOxxJIMlGRSFTo7UBxuUnbVLzxtvOfipO12g3-gP1zAMhu0aAd5yItFn5hc_zEt9M&_hsmi=141442980&utm_content=141381565&utm_source=hs_email"
published: 2026-07-22
created: 2026-07-24
tags:
---


Deliverability conversations almost always focus on over-sending. Too many emails, too frequently, to too many unengaged people. The advice that follows is almost always the same: clean your list, suppress your inactives, reduce your volume.

That advice is not wrong, exactly (if you want to learn email deliverability, you need to [do this first](https://weareastral.co.uk/emaildeliverability/training)). But it is incomplete, and the way it gets applie, in particular the way platforms like Klaviyo present it through their Deliverability Hub, can lead marketers into a trap that makes their deliverability worse, not better.

I think about deliverability as a set of scales:

![Screenshot 2026-07-22 074807](https://weareastral.co.uk/hs-fs/hubfs/Screenshot%202026-07-22%20074807.png?width=3768&height=2112&name=Screenshot%202026-07-22%20074807.png)

Image taken from my FREE Email Deliverability training - [book on here](https://weareastral.co.uk/webinar/getting-email-deliverability-right)

On one side: positive engagement signals, opens (unreliable, but still counted), clicks, replies, email moves from spam to inbox, website visits from email traffic.

On the other side: negative signals — spam complaints, hard bounces, deletions without opening, ignored sends piling up from unengaged contacts. Your inbox placement is determined by which side is heavier. It is not a pass/fail gate. It is a continuous balance of trying to get the scales not tipping onto the negative side!

The problem with almost all mainstream deliverability advice is that it focuses almost entirely on reducing the negative side of the scales. What it ignores is that you can also lose the balance by failing to generate enough positive signals — which is exactly what happens when you do not send enough email, when you stop and start, and when you suppress large portions of your list based on a metric that has not been reliable for years.

## What Gmail actually does when you go quiet

Most email marketers know that sending to unengaged contacts damages deliverability. Fewer know that going quiet for too long damages it too, and the mechanism is more immediate than most people realise.

Gmail can sometimes actively prompt users to unsubscribe from promotional emails they have not opened in approximately 30 days or EVEN start diverting you to the spam folder to see what you do. This is an automated feature that fires without the sender knowing it is happening. Your subscriber has not made any active decision to leave. Gmail has decided, based on their behaviour, that they are not interested in your emails, and has offered them a one-click exit — without them having to go through your unsubscribe flow.

The effect of this is that infrequent senders, those sending a monthly newsletter, for example, or those who go quiet for several weeks between campaigns are systematically generating Gmail-prompted unsubscribes before their next send even arrives. By the time your email lands, a proportion of your subscribers who were technically still on your list have been nudged out of it.

Beyond the unsubscribe prompts: inbox providers build a picture of your sending behaviour over time. They expect consistent patterns. When you send regularly, they have months of signal about who engages with your emails, how quickly, and how positively. When you disappear for four, six, or eight weeks and then come back with a significant send, the pattern looks suspicious. Erratic volume is a classic behaviour pattern associated with spam operations, and inbox providers treat it accordingly. Your emails after a gap are more likely to be filtered or deprioritised than your emails during a period of consistent sending.

And then there is the human psychology dimension.

- When someone has not heard from you in two months, and your email suddenly appears in their inbox, the first reaction is often confusion
- Who are these people?
- Did I sign up for this?

That confusion translates into deletions, ignores, and in some cases spam complaints — all of which are negative signals that compound the deliverability problem you are already facing from the inconsistent sending pattern.

## The stop-start problem

The most damaging version of infrequent sending is not consistent low frequency. It is the pattern of stopping entirely and then restarting at volume, which is exactly what happens when teams run re-engagement campaigns after a period of reduced sending, or when seasonal businesses come back after their quiet period, or when a marketing team has been under-resourced and suddenly ramps back up.

When you stop sending to a significant portion of your list for a prolonged period and then come back with a large send, you are effectively doing a cold send to a warm list. The inbox providers have seen your domain go quiet. They do not have recent engagement signals to draw on. And you are asking them to deliver high volume from a domain that has been inconsistent, which is precisely the pattern that triggers filtering and throttling.

The contacts themselves are also in a different place than when you last sent. Some have changed email addresses. Some have addresses that have gone dormant or been deleted. Gmail purges inactive personal accounts after two years, meaning your list from 18 months ago contains a meaningful proportion of addresses that no longer exist, which now generate hard bounces. Others are simply less warm than they were, they signed up for a reason that may no longer be relevant, and a long gap has eroded whatever familiarity existed.

The bounce rate on a restart send is almost always higher than normal. The spam complaint rate is almost always higher than normal. The engagement rate is almost always lower than normal. All of these signals hit your domain reputation simultaneously, at the worst possible moment.

## The problem with platform suppression advice — specifically Klaviyo’s Deliverability Hub

I just want to say that I am mad with most Email Service Providers right now; they do not know enough about email deliverability and then they create features and tools that MAKE IT WORSE.

Klaviyo’s Deliverability Hub presents what looks like helpful, data-driven deliverability guidance. It shows you engagement scores, flags contacts who have never engaged, and recommends suppressing them. On the surface, this seems sensible — remove the unengaged, improve your list health, protect your reputation.

![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/d26a3a47db317f77938ef3876075af5bfc5cb41e-1160x1168.jpg?w=558)

The problem is not the principle, it's suppressing contacts who have genuinely never engaged and never will is a legitimate list hygiene practice. The problem is what the platform uses to define “never engaged” and the downstream effects of acting on that definition at scale.

Klaviyo’s engagement scoring is primarily based on opens and clicks. But opens have been unreliable as a measure of human engagement since Apple Mail Privacy Protection in 2021, which pre-fetches emails and registers machine opens. Gmail’s Gemini integration in 2026 auto-opens emails to generate AI summaries, inflating open rates further. A contact who is reading every email subject line in their inbox preview and clicking through to your website regularly might show as "never engaged" in Klaviyo’s deliverability hub because their email client does not register opens. A contact who has Apple Mail set up will have every email pre-fetched and counted as an open, so they look engaged regardless of whether they ever read anything. And then we have human behaviour in the inbox...but that's another day!

When you follow the platform’s advice and suppress large segments of your list based on this broken data, several things happen:

- You remove people who may actually be engaged with your brand through channels or signals the platform cannot see — website visits, social media, purchases, the billboard effect of seeing your sender name regularly
- You reduce your total sending volume significantly, which means your positive engagement signals are now a smaller absolute number even if the rate looks better
- You change the ratio of your list composition in ways that can be difficult to reverse — once suppressed, contacts stop receiving emails and cannot generate engagement signals that might have brought them back
- If you then run a re-engagement campaign to try to recover some of those suppressed contacts, you are sending email to people who have not heard from you in months, into exactly the cold-restart scenario described above

The Deliverability Hub also does not account for the fact that some of the contacts it recommends suppressing are likely engaged consumers who are just not clicking in ways the platform can track. Suppressing them does not clean your list. It removes real relationships from your sendable audience based on incomplete data.  

PSA: Any platform that gives you an engagement score, or email health score - ignore it please!!

## Disengagement is normal human behaviour — not a list hygiene failure

Before we talk about what to do, it is worth naming something that gets missed in most deliverability conversations: disengagement is a completely normal part of the subscriber lifecycle, and treating it as a programme failure that needs to be corrected through suppression misunderstands what is actually happening.

When someone signs up for your emails, they are in a particular moment — a specific context, a specific need, a specific level of interest in what you offer.

Over time, contexts change, jobs change, life circumstances change, behaviour changes, mood changes and you know the rest of it...the problem you solve may become less urgent for them. They may find another solution. They may simply have more going on in their inbox and their life than they had when they signed up.

This is not a failure of your email programme. It is the natural lifecycle of a contact database operating in the real world. Every list loses a meaningful proportion of its effective engaged audience every year through a combination of unsubscribes, address changes, and gradual disengagement.

The question is not how to stop this from happening, you cannot, but how to manage it intelligently without damaging your deliverability in the process.

The answer is not to keep emailing people who are genuinely no longer interested. That damages the scales on the negative side. But it is also not to suppress large chunks of your list based on open data that does not accurately reflect engagement. That reduces your positive signal-generating capacity without necessarily removing the contacts who are actually hurting you.

The most sophisticated version of this is segmentation by meaningful actions, website visits, purchases, content downloads, replies, clicks, rather than by opens. Contacts who have taken no meaningful action in 12 months across any channel are more likely to be genuinely inactive than contacts who have not opened an email but have visited your website three times in the last month.

## Why intent-based flows are the answer — not re-engagement campaigns

The most important thing I want to leave you with from this blog is the role that automated, intent-based flows play in maintaining deliverability. Because this is the part of the conversation that most platforms and most deliverability guides miss entirely.

My newsletter, like any newsletter, sees drops in engagement over time. People sign up, they are engaged, and then life happens, and they drift. That is inevitable, and I accept it.

What I do not accept is that my total email programme lives or dies on the engagement signals from that newsletter.

The majority of my best engagement signals come from intent-based flows — the emails that fire when someone does something.

Signs up for a resource, attends a webinar, downloads a checklist, visits a specific page, fills in a contact form.

These emails land at a moment of very real interest, which means they generate high-quality engagement signals: people click, reply, forward, move emails to folders. They generate positive signals that counterbalance the lower engagement on broadcast sends.

This is the fundamental shift in how to think about maintaining deliverability. It is not about cutting your list back far enough that only the most engaged people remain. It is about building a programme architecture that continuously generates strong positive engagement signals from the people who are in an active moment of interest. Those signals protect your domain reputation, which protects the deliverability of everything else you send — including the newsletter that inevitably generates lower engagement than the flows.

### Intent-based flows maintain your deliverability because:

*They send at the moment of highest subscriber interest, generating the strongest possible engagement signals*

Welcome and orientation flows send when someone is at peak engagement — the moment they joined your list. This is the highest open and click rate you will ever generate from any email. A well-built welcome flow that runs for the first two to three weeks of a subscriber’s relationship with you creates a strong initial engagement record for that contact that continues to influence their deliverability tier.

Lead nurture and conversion flows fire based on specific behavioural signals — content downloads, website page visits, form fills. The subscribers receiving these emails have demonstrated intent. Their engagement with these emails is higher than with broadcast sends, and the positive signals they generate are stronger.

Post-purchase and onboarding flows send to people who have just made a purchase or taken a significant action — another high-engagement moment. These emails often see the highest click-through rates in the entire programme because the subscriber is actively invested in what comes next.

Transactional and notification emails — order confirmations, account updates, appointment reminders — are opened at extremely high rates because they are expected and immediately relevant. These may come from a separate sending domain, but they still contribute to the overall sending health of your organisation.

The point is: a programme that generates consistent, high-quality engagement from flows is in a much better deliverability position than a programme that relies entirely on broadcast campaigns and then suppresses its way to better metrics. The flows protect the campaigns.

## What to do — maintaining healthy deliverability through consistent sending

The principles below are not complicated, but they require discipline to apply consistently.

Send consistently, even at low volume

Consistent sending — even if that means one shorter email per week rather than one long one per month — is better for your domain reputation than sporadic high-volume sends. Inbox providers build trust through pattern recognition. A predictable, consistent sender is a trusted sender. An erratic one is a suspicious one. If resource constraints mean you cannot maintain a weekly newsletter, consider a fortnightly cadence rather than monthly — it keeps you inside Gmail’s 30-day window and maintains the consistency signal.

Build your flows before you need them

Flows should not be a deliverability rescue tactic. They should be the foundation of your programme architecture from the start. If you have no flows at all, start with the welcome flow. It is the single highest-leverage automation any email programme can have, and it starts generating positive engagement signals from the first day someone joins your list.

Suppress on meaningful actions, not opens

Before suppressing any contact, cross-reference open inactivity against website visits, purchases, content downloads, email clicks (not just opens), and any other engagement signals your CRM can see. A contact who has not opened an email in six months but purchased three times in that period is not disengaged. A contact who has had no meaningful interaction of any kind in twelve months is a better candidate for suppression. The distinction matters enormously.

If you need to restart after a gap, treat it like a warm-up

If your programme has gone quiet for a significant period and you need to restart, do not fire your full list on day one. Start with your most engaged contacts — people who clicked something recently, people who purchased recently, people who are most likely to engage positively. Build from there over several weeks, monitoring your inbox placement, complaint rates, and bounce rates as you increase volume. Treat the restart like an IP warm-up, even if you are on a shared IP. The principle is the same: build reputation gradually rather than asking inbox providers to trust a sudden volume spike from a domain that has been quiet.

Stop measuring deliverability through your ESP dashboard alone

Your ESP shows you delivered, opened, clicked. What it does not show you is inbox placement — whether your delivered emails are landing in the Primary inbox, the Promotions tab, or the spam folder. These are fundamentally different outcomes that look identical in your delivery metrics. Use inbox placement testing tools (GlockApps, Litmus, Email on Acid, or your ESP’s built-in placement testing if available) to understand where your emails are actually landing. This is the metric that tells you whether your deliverability is actually healthy — not your open rate, and not your Klaviyo deliverability score.

Deliverability is a balance, not a threshold. You do not cross a line and suddenly land in the inbox or suddenly land in spam. You are continuously earning or eroding inbox placement through the aggregate of every signal your programme generates — positive and negative. Stopping and starting, aggressive suppression on broken metrics, and neglecting the flow architecture that generates consistent positive signals are all ways of tipping that balance in the wrong direction. Building a consistent, well-structured programme that sends regularly and earns engagement through relevance is the only sustainable path to inbox placement.