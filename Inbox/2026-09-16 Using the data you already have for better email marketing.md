---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/using-the-data-you-already-have-derived-properties-predictive-insights-and-where-ai-really-helps?utm_medium=email&_hsenc=p2ANqtz-8iubLJTbEYvn-ShbH6atWDwsFR9fbmst0Vk0IxtG1LmU4aZgoa2pQJxF1ABFDhaSsMjDRsyQnxiYUe8zxNqLtvuyVg9p6cTHUx72kp6irF63V3xCI&_hsmi=145913605&utm_content=145862482&utm_source=hs_email"
published: 2026-09-16
created: 2026-09-17
tags:
---


Most businesses do not have a data collection problem. They have a data derivation problem, and the two look identical from the outside.

The symptom is always the same; somebody says we need better data before we can personalise properly (or more advanced), a project gets scoped to add fields to forms, and eighteen months later there is more raw data sitting in the CRM and still nothing useful being done with it.

Meanwhile the company has years of purchase history, support tickets, click behaviour, sales calls, survey responses, reply text and form answers that nobody has ever turned into anything you could segment on.

The problem was never collection. It was that turning raw data into something usable took either a lot of manual work or a data team, so most businesses stopped at the raw layer and called it a data strategy.

That constraint has now changed. Not AI as a way to write more emails faster, which is a bad use of it, but AI as a way to derive meaning from data you already own and have never been able to use.

## The three tiers

## Collected, derived, and predicted

### Tier one: collected data

What somebody told you, or what happened. A purchase. A form field. A click. A page view. An email address and a signup date.

Factual, verifiable, and on its own close to useless. Knowing that somebody bought a thing on the fourteenth of March tells you almost nothing about what to send them, which is why programmes built entirely on collected data end up segmenting by product category and wondering why it underperforms.

### Tier two: derived data

What you worked out from the raw. Computed rather than stated, and where all the useful segmentation lives.

- Average order value, and whether it is rising or falling.
- Days since last purchase, and how that compares to their own normal rather than to everybody else's.
- Category affinity, built from repeated behaviour rather than one order.
- Discount dependency, meaning what proportion of their purchases came with a code attached.
- Engagement tier, using your own definition rather than an inherited ninety days.
- Purchase cadence, meaning their personal rhythm rather than a blanket replenishment window.
- Lifecycle stage, meaning never purchased, first purchase, repeat, lapsed, dormant.
- Channel preference, based on where they respond rather than what they ticked.
- SO MUCH MORE (and if you have HubSpot you know what I mean - all their calculated fields is where it's at)

None of that was collected. All of it was calculated from things that were, and every single one is more useful for deciding what to send than the raw data underneath it.

### Tier three: predicted data

What is likely to happen next or NOT happen next. Propensity to buy in the next thirty days, likelihood of churn, likelihood to close, the specific window in which this individual is due rather than the average for their category, probability of complaint if you send to them this week.

Historically this needed a data science function, which is why most businesses never had any of it, and why the ones that did kept it locked inside a model nobody in marketing could interrogate.

## What changed

## Where AI really helps, and it is not writing your emails

The obvious use of AI in email is generating copy, and it is the worst one. Heavily automated writing sees engagement decay over time, because humans recognise the patterns and disengage, and declining engagement is what eventually pushes you into spam.

The useful applications are all upstream of the writing and doing your copy (side note, I NEVER ever thought of myself as a writer, but since forcing myself to write every single piece of content - with some AI help but mainly me, I LOVE it)

### One: turning free text into structured properties

Every business is sitting on a large volume of text that contains exactly the information they claim to need, in a format nothing can segment on.

- Why did you sign up answers. Hundreds or thousands of free text responses telling you precisely what people came for, sitting in a field nobody has opened.
- Support tickets and their resolutions. What people struggle with, at the moment they were struggling.
- Replies to your emails. The highest quality feedback you get, and typically stored in a shared inbox rather than anywhere connected to the contact record.
- Cancellation and refund reasons. What you failed to explain or over-promised, written in their words.
- Sales call notes. Objections, context and timing, usually locked in a CRM field that reporting cannot touch.

Classifying that text into consistent categories used to be a manual job nobody had time for. It is now a perfectly reasonable afternoon's work, and the output is a set of structured properties you can build audiences from.

### Two: clustering, which finds segments you did not think of

Conventional segmentation starts with a hypothesis. You decide the groups, then sort people into them, which means you can only ever find the segments you already imagined.

Clustering works the other way round. It groups customers by how similarly they behave, then you look at what came out and work out what each group has in common. Frequently it surfaces something nobody would have proposed, such as a set of customers who buy rarely, at high value, always after a long browsing period, and who need a completely different treatment from everybody else in their product category.

The caveat is that a cluster is a mathematical grouping, not a person. If you cannot look at one and describe who these people are in a sentence, you have found a pattern rather than a segment, and acting on it will not go well.

### Three: propensity scoring per person

Rather than a blanket rule that everybody who has not purchased in ninety days gets a win-back, a score per contact for how likely they are to buy, to lapse, or to complain.

Which changes exclusions more than it changes campaigns. A high complaint propensity is a reason to leave somebody out of a broad send, and that single application is worth more to most programmes than any amount of clever targeting.

### Four: timing predicted individually

Replenishment is the clearest example. Most businesses apply one interval to a whole category, so everybody who bought coffee gets the reminder at six weeks, when the actual range across customers runs from two weeks to five months.

A per-person prediction, built from that individual's own history and people who behave like them, turns a blunt reminder into something that arrives when it is useful. And relevance is what breaks through habituation, so the deliverability benefit is real rather than incidental.

## The caveats

## Why this goes wrong, and how to keep it grounded

### A prediction is a hypothesis wearing a confident face with a BIG fat smile

The single biggest risk, and it is a presentation problem rather than a technical one. A propensity score arrives as a number, numbers look like facts, and within a month somebody in a meeting is describing a model output as though it were something the customer said.

Every predicted property needs a confidence level attached, and it needs to be visible to the people making decisions with it. High confidence, medium, and unknown are three different treatments, and unknown is a legitimate answer rather than a failure.

### Bad data in, authoritative-looking bad data out (or as I like to say Shit in Shit out)

AI does not clean your data, it processes whatever you give it. A derived affinity score built on a database full of duplicates, gift purchases and addresses collected through a forced opt-in will produce confident, specific, wrong answers, and they will be harder to challenge than a gut feeling would have been because they came out of a system.

Which makes the unglamorous work a prerequisite rather than an alternative. Deduplicate, verify, understand where your data came from, and only then derive anything from it.

### Label the provenance or nobody downstream can tell

A derived property sits in a contact record looking identical to a stated one. Six months later, somebody in another team builds a campaign on a field called preferred category with no idea whether the customer chose it or a model inferred it, and no way of finding out.

Naming conventions solve most of this. Make it obvious in the property name whether something was stated, derived or predicted, and future you will be extremely grateful.

### Do not predict what you could simply ask

The most common overreach. Building a model to infer something that one well-placed question would establish as fact is expensive, less accurate, and it misses the relationship benefit of asking.

Ask where asking is reasonable and the answer would change what you send. Derive where asking would be intrusive or where behaviour tells you more than a self-report would. Predict only where neither is available, which is a much smaller category than most vendors would like you to believe.

### Acting on a weak prediction is a deliverability decision

Worth spelling out because it rarely gets connected. A wrong prediction sends the wrong email to the wrong person, which produces a non-open, a delete, or a complaint. Those are negative signals, and enough of them clustered together is a negative event.

So a model operating at low confidence across a large audience is not a neutral experiment. It is a slow degradation of your sender reputation, carried out with the best intentions and reported as a personalisation initiative.

## How to start

## An order of work that produces something usable

1. Inventory what you already hold. Every field, every free text store, every behavioural log. Most people are surprised by how much exists and how little of it is in use.
2. Mark each field as stated, derived, predicted, or dead. Dead means collected and never used for anything, which is usually the largest category and the most revealing.
3. Fix the underlying data before you derive from it. Duplicates, role addresses, verification, acquisition source tagging. Boring, and everything downstream depends on it.
4. Build three derived properties, not thirty. Lifecycle stage, engagement tier and one affinity measure will carry more value than a comprehensive model nobody maintains. Prove the value, then expand.
5. Put your free text through a classifier. Signup reasons first, because that one turns directly into content planning and segmentation at the same time.
6. Add one prediction, and use it for an exclusion. Complaint propensity or churn risk, applied to who you leave out rather than who you target. Lower risk, immediate deliverability benefit, and easy to measure.
7. Label everything and write down who owns it. A derived property with no owner becomes a mystery field within a year, and mystery fields get used by people who do not know what they mean.
8. Review the predictions against what happened. A model nobody checks is a belief. Compare predicted to actual quarterly and adjust, or stop using it.

## The conclusion

The businesses getting value from their data are rarely the ones collecting the most of it. They are the ones who took what they already had and worked something out from it, which is a completely different activity and a far cheaper one.

AI has made the derivation layer accessible to businesses that were never going to hire a data team, and it has made the prediction layer available to businesses that could not previously dream of it. Both are useful and both are dangerous in exactly the same way, which is that they produce outputs that look more certain than they are.

So derive before you predict, label what came from where, keep confidence visible, and remember that a wrong guess acted on at scale is not a neutral mistake. It is a negative signal with a spreadsheet behind it.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.