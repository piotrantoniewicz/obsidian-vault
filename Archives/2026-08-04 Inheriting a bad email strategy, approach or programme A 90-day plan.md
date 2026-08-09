---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/inheriting-a-bad-email-strategy-approach-or-programme-a-90-day-plan?utm_medium=email&_hsenc=p2ANqtz-_ALY-D1AStot01thB8ykvv8odDcxQG2xkel8rm29-wXkFpmxbuOJYI_HXZD_OxUdhLZ7ufS-wdQTFw22B_b4tnvvIXnNBKchkDn4f7PvvOuPy51n4&_hsmi=142599401&utm_content=142598984&utm_source=hs_email"
published: 2026-08-04
created: 2026-08-08
tags:
  - "strategia-organizacji"
  - "digital-campaigning"
  - "fundraising"
---


You've walked into something (hopefully not a wall just a terrible, awful email sending strategy). Maybe you started a new job three weeks ago, and email came with the desk. Maybe you're a consultant or an agency who has just been handed the login. Maybe you've been sitting here for two years and only recently worked out that the thing you've been dutifully maintaining was never designed in the first place.

Whichever version it is, the situation is identical. You own an email function you didn't build, you can't yet see how it was built, and somebody is already asking when the numbers are going to improve.

So let's start with the line that will annoy whoever hired you: the best thing you can do in your first 30 days is not send a good email.

That sounds wrong, and it sounds especially wrong when the instinct on both sides is to demonstrate value quickly. But the quick win you'll be steered towards is nearly always some version of 'let's wake up the disengaged half of the list', and that is the fastest known method for converting an inherited problem into your problem. You do not want your name on the send that tanked deliverability in week three.

Your job in this 90 day window is not to fix email. It's to establish what fixed would even mean for this business, and to build enough evidence that the decisions you make in month four can be defended by somebody who wasn't in the room when you made them.

## Two versions of this job

This plan applies whether you're in-house or external, but the constraints are different and pretending otherwise makes the advice useless, so I'll flag the split where it matters.

- In-house, your constraint is people (and time potentially). You have time, you have relationships you inherited along with the platform, and you will personally live with every consequence. The politics are the hard part.
- External, your constraint is access and information. You have a scope, a contract, and a client who has usually decided what the problem is before you arrived. The archaeology is the hard part, and you're being paid by the day to do it.

## DAYS 1 - 30

## Archaeology, not action

The first month is for looking. That's it, and the discipline required to do only that is the reason most inherited emails never actually get fixed.

### What's live?

This is the hardest part of inheriting an email function, and almost nobody writes about it, because it isn't strategic or interesting and it makes for terrible LinkedIn content. Nobody documented anything. The person who built it has gone. There are forty automations switched on and no map of what triggers them, what exits them, or whether any of them still make sense.

You need to be able to answer, on paper:

- What is switched on right now, and what triggers each one.
- What exits somebody from each flow, if anything does.
- Which flows overlap, so a single person can sit inside three at once.
- What is excluded from what, and whether anyone knows why.
- Which automations are still emailing people who bought, unsubscribed, complained or, and I am not being flippant here, died.
- What is scheduled that nobody has looked at since it was scheduled.

Do this by observation rather than by asking. Ask what's running and you will be told what somebody believes is running, which is a different document entirely. Go into the platform, list what is actually firing, then compare the two, because the gap between them is your first real finding and it's usually the most persuasive thing you will have to show anybody for a month.

### Where did these people come from?

Acquisition source, consent basis, and opt-in type for every entry point you can identify. If nobody can tell you how somebody ended up on the list, you have a permission problem sitting underneath what everyone is calling a performance problem, and no amount of better subject lines will touch it.

The distinction I'd apply here is consequential versus intentional. Somebody who ticked a box at checkout to get 10% off did not sign up for a relationship; they signed up for a discount. If the inherited programme has been treating those people the same as newsletter subscribers, you have found a large part of your answer in week one.

### What does the data say?

Look at ALL the data, what you collect, how it's being used, how it's segmented, how it's reported, how it's integrated, and then all the stuff that is missing.

### The technical picture

Authentication, domains and subdomains, which streams are sharing a reputation that they shouldn't be sharing, and where your mail is actually landing rather than what your ESP's delivered rate claims. This is proper deliverability audit territory and it has a methodology to it, which I teach in full in the [certification programme](https://weareastral.co.uk/emaildeliverability/training). What matters for the 90-day plan is that you do it now, before you change anything, because it's your only clean baseline.

### You have inherited somebody else's numbers (uh oh)

The baseline you'll be measured against was probably never real. It's contaminated by privacy changes that broke open tracking, by tab and category placement, by a list full of people who never properly opted in, and by an ESP that counts spam-foldered mail as delivered. Somebody will hand you a slide showing a 42% open rate in 2021 and ask, reasonably, why it's 19% now.

Correct the record in month one. If you don't, you spend the rest of the year defending somebody else's fiction, and by month six it has quietly become your fiction, because you were the one who didn't challenge it.

### What is on fire

Two lists, and the difference between them is the most useful thing in this whole post. Fix what creates risk. Leave what creates questions until you can answer them.

![images (1)](https://weareastral.co.uk/hs-fs/hubfs/images%20(1).jpg?width=1980&height=1392&name=images%20(1).jpg)

This is me when the email strategy is NOT fine 👆

Fix in week one, regardless of your lovely plan:

- Missing or broken authentication. SPF, DKIM and DMARC. Not optional, not a project, not next quarter.
- Anything sending to a purchased, scraped or rented list. Stop it today and worry about the conversation afterwards.
- Consent problems. No lawful basis, no record of how consent was obtained, or opt-outs that aren't being honoured properly.
- Automations still emailing people who unsubscribed, complained or already bought/recently bought This is more common than anyone admits and it is actively costing you reputation every single day it runs.
- A broken unsubscribe. Including one that technically exists but doesn't actually work, or takes four clicks and a login.
- A spam complaint rate sitting at or near the threshold. That's not a metric, that's an alarm.

None of these are optimisation. Also, you can [quickly build an exclusion strategy](https://weareastral.co.uk/thevault/stop-sending-the-wrong-emails-step-by-step-exclusion-strategies) too & this will massively help.  

Looks broken, don't touch it yet:

- Don't clean the list. Not yet. You don't know who's on it, how they got there, or why they look inactive, and some of them will be perfectly healthy customers who buy once a year and ignore you the other eleven months.
- Don't change the from name or sending domain. You'll break the pattern recipients already recognise and you'll destroy your ability to compare before and after, which is the only evidence you're going to have.
- Don't switch automations off. Not until you've mapped who is currently inside them and where those people would land if the flow stopped underneath them.
- Don't migrate ESP. Everybody wants to, it's rarely the actual problem, and it will eat your entire first year and most of your goodwill.
- **Don't redesign the template.** It feels productive, it's very visible, and it fixes nothing. It is the email equivalent of tidying your desk instead of doing the work.

## DAYS 31 - 60

## Stabilise and define

Month two is where you stop the bleeding and replace inherited assumptions with definitions somebody can actually argue with. An arguable definition beats a borrowed one every time.

### Stop the leaks with exclusions

Exclusions are the highest-leverage thing available to you in month two, because they don't need budget, they don't need a redesign, and they improve results by subtraction rather than addition. They're also almost entirely absent from inherited programmes, which is usually why those programmes are collapsing.

Start with these:

- New subscribers excluded from general broadcasts while they're in onboarding/ [orientation](https://weareastral.co.uk/thevault/welcome-flows-are-dead.-orientation-flows-are-thriving)
- Anyone in an active sales conversation excluded from promotional sends.
- Anyone with an open service or support issue excluded from marketing entirely.
- Overlapping automations prevented from firing at the same person in the same week.
- Consequential opt-ins protected from hard commercial asks until you've earned that invisible second opt-in.

### Define what engagement actually means here

Not 30, 60 or 90 days lifted off the internet. That number needs to reflect this business, this buying cycle and this product, and it needs to account for meaningful actions that happen outside the inbox entirely. Somebody who never opens a newsletter but attends every webinar, reads the blog directly and renews annually is not disengaged, they're just not an opener, and treating them as dead weight is how you delete your best customers.

This is also the month where you'll discover that nobody has ever written this definition down, which means every report anyone has produced was measuring something nobody agreed on.

### Agree what you'll be measured on, and get it in writing

The moment results start moving, somebody will move the goalposts, usually sincerely and usually because they've read something. Fix the measures now, while you still have the credibility of being new.

- Revenue or pipeline per thousand emails sent, rather than total volume.
- Spam complaint rate, tracked as a headline number and not buried.
- Time from signup to first meaningful action.
- Placement by cohort, so new subscribers and legacy data are never reported as one blended figure.

If you're external, your 60-day report should be about the definition you've established and the risk you've removed, not about opens. Set that expectation in the proposal rather than in the report, because by report stage it reads as an excuse.

## DAYS 61 - 90

## Rebuild the entry point

Notice what we still haven't done. We haven't rebuilt the campaign calendar, redesigned the template, or launched a big re-engagement push at the dead half of the database. That's deliberate, and it's the part most 90-day plans get backwards.

You fix the front door first, because everything you repair upstream stops generating the problem downstream. Re-engagement is what you do when you've run out of upstream fixes, and you have not run out. You've barely started.

### What month three looks like

- Every entry point mapped, and each one labelled consequential or intentional.
- A proper orientation flow live for your highest-volume entry point, delivering the promise immediately, setting expectations, and giving people control.
- Data collection at entry that changes what happens next, rather than fields that get stored and never used.
- Exclusions wired around that flow so new subscribers aren't dragged into everything else on day two.

### Pick one thing and do it properly

One flow, designed from scratch, with the thinking visible. Not because one flow transforms a programme, but because it becomes your reference point, your internal proof, and the thing you point at when somebody asks what good looks like here. It's much easier to argue for a standard that already exists somewhere in the building than for one that exists only in your head.

### The 90-day narrative

What you say, and when, matters as much as what you did. Here's the shape I'd aim for.

| **The milestone** | **What you should be able to say** |
| --- | --- |
| **Day 30** | Here is what is actually running, here is what was creating risk, and here is what I have already stopped. |
| **Day 60** | Here is what engagement means for this business, here is what we're now excluding and why, and here is the baseline I want to be measured against. |
| **Day 90** | Here is the first properly designed part of the programme, here is what it does differently, and here is the plan for next quarter. |

## THE HARD HALF (LOL)

## The politics, which is always half the job

Everything above is the easy part. What follows determines whether any of it survives contact with the organisation, and it's the reason competent people fail at this while less competent, more politically fluent people succeed.

### The person who built it may still be in the room

They might be your colleague, your client's most trusted operator, or the loveliest person on the team who did their absolute best with no budget, no training and no time. Critique the system, never the person, and not because it's polite. Because it's accurate. Most broken programmes were built under pressure, with the wrong tools, by somebody who was never given the chance to do it properly.

Language that works, because all of it is true:

- “This was built for a different volume.”
- “This made complete sense when the list was eight thousand people.”
- “This is what happens to every programme that grows faster than its infrastructure.”

None of those is an accusation, all of them are defensible, and each one gives the person who built it a route to agreeing with you without losing face.

### Your boss may have built the broken thing

Considerably harder. You cannot tell the person who wrote the strategy that the strategy is wrong and expect the following nine months to be enjoyable.

What works is making the inbox the antagonist rather than the person. Mailbox providers changed the rules. Privacy changes broke the measurement. Rising volume changed the economics of the channel. All of that is genuinely true, none of it is anybody's fault, and it hands everyone a dignified route to the same conclusion you'd reached anyway. You're not being manipulative, you're choosing which true thing to lead with.

### Somebody wants a campaign in week two

You will almost never get 30 clean days to look. This is the single biggest flaw in every 90-day plan ever published, including this one if I'm not careful about it, so let's deal with it honestly.

Three things that buy you the time:

- Say yes to a narrower version. Send to your engaged segment only. It's small, it's safe, it keeps everyone calm, and it doubles as a diagnostic because you'll learn something from how it performs.
- Give a date, not a refusal. “The first proper campaign goes out on the 14th, and here's what I need to check before then so it doesn't cost us.” Nobody argues with a date. Plenty of people argue with a no.
- Show something in week two anyway. Not results, findings. A one-page list of what's live, what's leaking and what you've already switched off is enormously persuasive, and it buys more patience than any campaign would have.

The trick isn't resisting the pressure, it's redirecting it. People asking for a campaign are usually asking for evidence that something is happening. So give them evidence that something is happening.

### If you’re external, a few extra ones

- You'll be told what the problem is before you look. The brief is a hypothesis, not a diagnosis, and quite often the stated problem is the symptom that annoyed somebody most recently.
- Scope the archaeology explicitly and charge for it. If discovery is buried inside “strategy”, you'll be doing it for free and resenting it by week three.
- Choose one visible, genuinely safe fix early. You are being judged on whether anything appears to be happening. Pick something real that also happens to be visible.
- Work out which internal argument you were hired to win. Somebody wanted an external voice for a reason. Knowing whose position you're expected to validate is not cynicism, it's context, and it changes how you write the report.

## What 90 days gets you

Not a fixed or new shiny strategy (you wish). That isn't available in 90 days, and I'd be suspicious of anyone selling it to you, particularly if they're selling it to your boss.

What it gets you is this:

- You know what you've actually got, which almost nobody in the business currently does.
- The things creating genuine risk have stopped.
- There's a definition of engagement that reflects this business rather than a blog post.
- Exclusions are doing quiet, unglamorous work in the background.
- One part of the programme has been designed rather than inherited, and it's your reference point for everything that follows.

Most importantly, you've stopped inheriting. From day 91 onwards the decisions are yours, they're documented, and you can defend them to anybody who asks.

## What to read next in the Vault

- [Stop Sending the Wrong Emails: Step-By-Step Exclusion Strategies](https://weareastral.co.uk/thevault/stop-sending-the-wrong-emails-step-by-step-exclusion-strategies)
- [Email Welcome Flows Are Dead and Orientation Flows Are In](https://weareastral.co.uk/thevault/welcome-flows-are-dead.-orientation-flows-are-thriving)
- [How to Run an Email Re-engagement Campaign](https://weareastral.co.uk/thevault/how-to-run-an-email-disengagement-campaign)
- [The Data-Powered Email Playbook](https://weareastral.co.uk/thevault/the-data-powered-email-playbook-collect-model-and-use-data-to-make-email-performance-grow)
- [The Ultimate Checklist for a Healthy Email Ecosystem](https://weareastral.co.uk/thevault/the-ultimate-checklist-for-a-healthy-email-ecosystem)
- [Email Is an Impact Channel, Not a Conversion One](https://weareastral.co.uk/thevault/email-is-an-impact-channel-not-a-conversion-one-and-thats-a-good-thing)
- [How to Successfully Migrate ESPs (and What Your Boss Needs to Know)](https://weareastral.co.uk/thevault/how-to-successfully-migrate-esps-and-what-your-boss-needs-to-know)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.