---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/email-behaving-badly-why-compliance-will-not-save-your-deliverability?utm_medium=email&_hsenc=p2ANqtz-9CB7S7Ma4HLy3iMIkP1bSK8Qdtl-nWa-a3Yq-K4e2gKoyiIwV6JPIJKQfHFqVQMP8f3R32nz2uKwvxachDFGE9qMIWkET35dil0E_cwC2VpRCLmrY&_hsmi=147661112&utm_content=147658469&utm_source=hs_email"
published: 2026-10-01
created: 2026-10-08
tags:
---


Something shifted this year, a BIG shift.

Mailbox providers spent 2024 and 2025 building a compliance floor. Authenticate properly, keep complaints below a threshold, put a one-click unsubscribe in your headers. Reasonable requirements, widely publicised, and by now most serious senders have done all of it.

Which is precisely the problem. When everybody complies, compliance stops being a signal, so the providers moved on to the thing that still separates good senders from bad ones. Behaviour!!

So you can pass every check on the list, have your SPF, DKIM and DMARC in perfect order, sit under the complaint threshold, and still watch your placement fall, because compliance was never the thing being measured. It was the ticket to be considered at all.

## The floor

## Everything on the checklist is table stakes

None of this is an argument against compliance. Skip any of it, and you will be rejected outright, and Gmail now issues hard rejections rather than routing you to junk.

- SPF, DKIM and DMARC, aligned and at enforcement. A DMARC record sitting at p=none is monitoring rather than protection, and Microsoft in particular will find that out before you do.
- One-click list-unsubscribe in the headers. Required for bulk senders, and unsubscribe friction is read as a negative signal whether or not the requirement technically applies to you.
- Complaint rate under the published ceiling. 0.3% is where enforcement starts, which makes it a limit rather than a target. I work to under 0.05%.
- Clean bounce handling and valid data. Hard bounces suppressed permanently, and a list you can account for.

Do all of that, and you have earned the right to be assessed. Nothing more. It is the equivalent of turning up to an interview in the correct clothes, and nobody gets the job for that.

## Behaving badly

## The things that pass every check and sink you anyway

Every behaviour below is technically compliant. Not one of them would fail an audit. All of them will cost you placement.

### Sending to people who consented and do not want it

The biggest one by a distance. Consent is a legal state and wanting is a behavioural one, and providers measure the second. Somebody who ticked a box in 2021 and has ignored you since is fully consented and is generating exactly the signal that says nobody wants this sender.

### Frequency without consequence

Sending four times a week is not a violation of anything. Sending four times a week when none of it matters teaches people to ignore you, and the resulting deletes and non-opens are read by providers as a verdict on you rather than on your schedule.

### Waking up dormant data because it is still on the list

A reactivation campaign to people who have shown nothing for two years is permissible and it is one of the fastest ways to generate a complaint event. Legally fine, reputationally expensive.

If you HAVE to do a re-engagement campaign, read these guides first:

- [How to Re-Engage Your Email List (Properly and Without Destroying Deliverability)](https://weareastral.co.uk/thevault/how-to-re-engage-your-email-list-properly-and-without-destroying-deliverability)
- [How to Run an Email Re-engagement Campaign](https://weareastral.co.uk/thevault/how-to-run-an-email-disengagement-campaign)

### Volume spikes that break your own pattern

Nothing in any provider's rules says your volume must be consistent. Consistency is a trust signal all the same, so tripling your sending for a promotion looks, from outside, indistinguishable from somebody who has just bought a list.

Example:

- For months you send to only 2,000 people then it jumps to 10,000 - RED FLAG

### The unsubscribe that technically exists

One-click header in place, tick. Visible link buried in nine point grey at the bottom, routed through a preference page with no exit option, requiring a login. Compliant, and it converts people who wanted to leave into people who press the spam button.

### Bundled and conditional consent

Marketing consent attached to a download, a purchase, a wifi login or a competition entry. Sometimes lawful, depending on jurisdiction and wording, and behaviourally it produces resentment, throwaway addresses and complaints. A forced opt-in list passes every technical check and behaves terribly.

### Marketing dressed as transactional

An order confirmation with four product recommendations and a promotion in it. The email gets sent on a transactional stream, gets opened at transactional rates, and carries marketing content. Clever, and providers have got considerably better at spotting it, and it risks the one stream you cannot afford to damage.

### Manufactured urgency and misleading subject lines

Re: in a subject line for an email that is not a reply. A deadline that resets every fortnight. Fwd: on something nobody forwarded. All perfectly legal, all trained your audience to distrust you, and distrust shows up as non-engagement.

### Buying data that came with a consent claim attached

The vendor says it is opted in. Possibly it was, for somebody else. The people receiving it have no recognition of you at all, which produces the exact engagement profile of a purchased list because that is what it is.

## How providers assess behaviour rather than configuration

They cannot inspect your intentions, so they read the traces your behaviour leaves on the people receiving it.

- Engagement, positive and negative. Opens, clicks, replies, moves to folder and not-junk on one side. Deletes without opening, ignored mail and complaints on the other.

I explain this in my [free deliverability training](https://weareastral.co.uk/free-email-deliverability-training) as the scale concept:

![FREE Email Deliverability Training Getting Email Deliverability Right](https://weareastral.co.uk/hs-fs/hubfs/FREE%20Email%20Deliverability%20Training%20Getting%20Email%20Deliverability%20Right.png?width=5760&height=3240&name=FREE%20Email%20Deliverability%20Training%20Getting%20Email%20Deliverability%20Right.png)

- Clustering. One complaint is noise. Forty complaints in an hour is an event, and events are what damage reputations rather than individual signals.
- Consistency of pattern. Volume, cadence, recipient mix. A sender whose shape stays stable looks established. One whose shape jumps looks like something automated and unwanted.
- Recipient-level history. Assessment is per user at Gmail in particular, so your reputation is partly a collection of individual verdicts rather than one global score.
- And the aggregate. Providers form a view of you from everybody you send to, which is why a block of people who never engage costs you placement with the people who do.

None of that appears on a compliance checklist, because none of it is configurable. It is the residue of decisions you make every week about who gets sent what.

## The test

## One question that catches almost all of it

When I am looking at a programme and trying to work out whether something is acceptable, I do not reach for the rules. I ask a version of this.

### The question:

If the person receiving this understood exactly why they were receiving it, and exactly what we did to get their address, would they be fine with it?

Not would it survive a legal review. Would the human be fine with it. Almost every bad behaviour in this post fails that question immediately, and it does not require you to memorise a single provider guideline.

Two useful follow-ups when you are unsure.

- Could you explain how you got this address, out loud, to the person you are sending to? If the answer involves a purchase, a scraper or a condition of access, you already know.
- Would a reasonable person be pleased to receive this, today, at this frequency? Not tolerant. Pleased. It is a higher bar and it is the one providers are effectively measuring through engagement.

## Behaving well

## What providers are looking for

1. Send to people who want it, and stop sending to people who do not. Exclusions and suppression, applied at system level rather than campaign by campaign. The highest-leverage thing available to almost every programme and the least glamorous.
2. Be consistent. Predictable volume, predictable cadence, predictable sender identity. Boring is a deliverability strategy.
3. Make something matter, regularly. Consequence is the only reliable defence against people learning to ignore you, and being ignored is what eventually moves you to spam.
4. Make leaving obvious and instant. You want the unsubscribe, not the complaint. One costs you a subscriber, the other costs you reputation with everybody.
5. Acquire people properly. How somebody joined your list is the strongest predictor of how your programme performs, and no amount of good sending fixes bad acquisition.
6. Separate your streams. Transactional away from marketing, outbound away from everything. So a bad month in one place cannot take down the rest.
7. Keep your promises. What you said at signup, at the frequency you said, about the subjects you said. Satisfaction is a comparison and you set the denominator.

## The trap

## Passing the audit and still not reaching anybody

The situation I get called into most often now, and it is a relatively new phenomenon.

A business has done the work. Authentication is immaculate. DMARC is at enforcement. One-click unsubscribe is in place. Somebody ran a compliance audit and it came back clean. And placement is still falling, engagement is still dropping, and nobody can explain it because every box on the list is ticked.

The list was the wrong list. It described the floor and they were failing at the ceiling, and no compliance audit ever asks whether the people receiving your email are pleased to get it.

Which is why I keep saying deliverability is the ongoing health of your sending reputation, a condition shaped by your behaviour over time. A condition, not a configuration. You can configure your way onto the pitch and you cannot configure your way to winning.

## The conclusion

The providers have been clear enough about the direction, and the industry keeps hearing it as a technical instruction. Enforcement moved from rejecting senders who fail the checks to demoting senders who pass every check and behave badly, and that shift is almost complete.

So do the compliance work, quickly and properly, and then stop treating it as the project. It is the entry requirement. The actual work is the unglamorous, repetitive business of sending things people want, to people who want them, at a rate they can live with.

There is no configuration for that, which is precisely why it still works as a differentiator.

### Further reading from The Vault:

- [How to Know Your Sender Reputation](https://weareastral.co.uk/thevault/how-to-know-your-sender-reputation.-why-you-cannot-look-it-up-any-more-and-how-to-work-it-out-instead)
- [The State of Email Deliverability in 2026, and What I Think Happens in 2027](https://weareastral.co.uk/thevault/the-state-of-email-deliverability-in-2026.-and-what-i-think-happens-in-2027)
- [Do You Have a Forced Opt-In List?](https://weareastral.co.uk/thevault/do-you-have-a-forced-opt-in-list-what-it-is-why-it-is-worse-than-a-consequential-opt-in-and-what-it-does-to-your-email-programme)
- [Email Exclusions and Sending Hierarchy](https://weareastral.co.uk/thevault/email-exclusions-and-sending-hierarchy.-how-to-decide-which-email-wins-when-three-of-them-could-go)
- [The Email Footer: Valuable Real Estate, and Why the Unsubscribe Belongs at the Top](https://weareastral.co.uk/thevault/the-email-footer-your-most-valuable-real-estate-and-why-the-unsubscribe-belongs-at-the-top)
- [Conversion to Trust: The Email Metric Nobody Is Measuring](https://weareastral.co.uk/thevault/conversion-to-trust-the-email-metric-nobody-is-measuring-and-how-to-improve-it)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.