---
type: Web
authors: '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/the-three-new-email-metrics-for-2026?utm_medium=email&_hsenc=p2ANqtz--3RwIVvrI5jGFoSQj0GF9pQVtTyGUvFcKmHyFN79tqgAcOUx9WNMWCAx96V6qxUzTi3hC5q4DadvTQBN7wNfvxV0scbhHyutZ8N5aDymmgUtZ57n0&_hsmi=135789897&utm_content=135788518&utm_source=hs_email
published: 2026-05-13T00:00:00.000Z
created: 2026-05-18T00:00:00.000Z
tags:
  - fundraising
  - digital-campaigning
  - content-marketing
---


In March 2026, [MarTech published a piece on three emerging email metrics](https://martech.org/3-new-email-metrics-that-you-need-in-2026/) that are likely to go mainstream this year — disaffection rate, reply rate, and trustworthiness. The piece drew on [Validity's 2026 Email Deliverability Benchmark Report](https://www.validity.com/resource-center/2026-email-deliverability-benchmark-report/), which I have read in full and referenced extensively in other work.

I want to talk about these three metrics. Because I think the direction of travel is right, moving away from opens and clicks toward signals that actually reflect the health of the subscriber relationship, but the specific definitions and formulas need interrogating properly. MarTech is a huge publication with a massive readership. People will take this as gospel. And some of it needs a closer look!

## Metric 1: The Disaffection Index

### What MarTech & Validty says

![Screenshot-2026-03-26-at-1.38.39-PM-800x176.png](https://weareastral.co.uk/hs-fs/hubfs/Screenshot-2026-03-26-at-1.38.39-PM-800x176.png.webp?width=2400&height=528&name=Screenshot-2026-03-26-at-1.38.39-PM-800x176.png.webp)

*Graphic from Validity 2026 Email Benchmark Report*

The disaffection index is positioned as a way to measure negative engagement rather than positive. Instead of asking how many people opened or clicked, it asks: how quickly are you burning through your audience?

The formula combines unsubscribes, complaints, and bounces — divided by clicks, multiplied by 100. The idea being that this single number captures all the signals indicating an audience is losing interest.

MarTech references Validity's benchmark report, which makes the specific point that inbox providers increasingly treat negative signals as stronger indicators than positive ones. And that is genuinely true. Gmail, Microsoft, and Yahoo are all moving toward engagement-weighted filtering — the programmes that generate consistent positive signals win, and the ones generating sustained negative signals lose inbox placement.

### Where I push back

My issues are with the definition and the formula. Let me pull them apart...

Bounces are not a signal of disaffection.

This is the first problem. The disaffection index combines unsubscribes, complaints, and bounces as though they are equivalent expressions of the same thing — an audience losing interest.

They are not!

A bounce is almost never a signal of disinterest. A soft bounce is a temporary delivery failure — the inbox was full, the server was unavailable. A hard bounce means the email address is no longer valid, usually because someone left a job, changed provider, or their mailbox was closed. In a B2B context specifically, that person did not decide to disengage from you. They left a role. Their mailbox expired. They never took any action indicating disinterest — they just stopped existing at that address.

Bounces damage deliverability, yes. They need monitoring and managing. But conflating them with unsubscribes and complaints — where a human being has made an explicit decision about their relationship with your emails — muddies what disaffection is supposed to measure.

A spam complaint is not disaffection — it is something worse.

The formula also combines spam complaints with unsubscribes. Again, these are not the same thing. An unsubscribe is someone saying: I no longer want to receive these. A spam complaint is someone saying: this email was unwanted and offensive enough that I am flagging it to the provider.

Disaffection implies fading interest. A spam complaint implies something far more active and far more damaging to your programme. The two should not be averaged together into a single metric — they require different responses and carry completely different weights.

Dividing by clicks is the wrong denominator.

The formula uses clicks as the denominator. But clicks are not a reliable measure of positive engagement for many businesses. There are plenty of programmes — particularly in B2B content marketing and thought leadership — where almost nobody clicks the email directly, but where meaningful commercial value is being generated through brand awareness, pipeline influence, and direct search. Using clicks as the positive baseline for a disaffection calculation would make those programmes look catastrophically disaffected when they are actually performing well.

### My reframe: what a meaningful disaffection metric would look like

The concept is sound, the formula needs work.

Here is how I would approach measuring what this is actually trying to measure — which is, at its core: are people leaving my list or turning against it, and at what rate relative to the engaged portion?

Rather than combining different signals of different severities into one number, I would track them separately as indicators and then look at their relationship over time:

- Unsubscribe rate by segment and by send type — tracked over time, not as a blended average
- Spam complaint rate — tracked separately from unsubscribes, with zero-tolerance thresholds because of its deliverability implications
- Bounce rate — tracked separately as a data quality and deliverability signal, not an engagement signal
- Meaningful action rate — what proportion of the list took a meaningful action (not an open or a click, but a real engagement signal: website visit, content download, event registration, purchase, inquiry) in the measurement period

The disaffection question I would actually want to answer is: of the people who received my emails in this period, what percentage showed any meaningful engagement signal and what percentage showed an explicit exit or rejection signal? The gap between those two numbers tells you more than any combined formula.

It is also worth naming what this is really measuring: list churn rate, measured through negative signals. That framing is clearer, more accurate, and easier to act on than the term "disaffection index."

## Metric 2: Reply Rate

### What MarTech & Validty says

![](https://martech.org/wp-content/uploads/2026/03/Screenshot-2026-03-26-at-1.40.21-PM-800x227.png.webp)

*Graphic from Validity 2026 Email Benchmark Report*

The reply rate metric positions replies as the real measure of engagement. The argument: clicks can be accidental, opens are unreliable, but replies require genuine intent. Someone replying to your email is telling you — and telling inbox providers — that this communication is real and wanted.

MarTech and the Validity report also make the point that Microsoft's new sender requirements specifically mention ensuring the reply-to address is valid and can receive replies — suggesting that replies are becoming a formal signal in provider reputation models.

### Where I push back

My concern with reply rate as a headline metric is the expectation it sets — and the reality of consumer behaviour it somewhat ignores.

When was the last time you replied to a marketing email from a brand? Not a customer service email — those are a different category entirely. A marketing email. A newsletter. A promotional send.

Most people never do. Not because they are disengaged or because the email was bad — but because the habit has not been built. We have spent thirty years training consumers that marketing emails are one-directional. You receive them, you read or scan or delete them, and you move on. The idea of replying to a brand email simply does not occur to most people, even when they find the content genuinely interesting.

Building reply rate as a primary KPI, in consumer contexts especially, is setting yourself up to measure extremely small numbers and potentially draw misleading conclusions from them.

There is also the question of what a reply actually indicates. An automatic out-of-office is a reply. A negative complaint reply — "please stop emailing me" — is a reply. A spam filter auto-response is a reply. High reply rate from the wrong cause is not a positive signal.

And there is the operational reality. Who picks up those replies? If you have a proper reply-to address and you are actively encouraging people to respond, you need a system for handling what comes back. For small businesses and solo operators, that is manageable. For teams sending to hundreds of thousands of people, it is an operational challenge that the metric does not address.

Reply rate is not new. It has always been tracked in B2B email marketing, in sales outreach, in one-to-one relationship email. Validity and MarTech are not introducing a new concept — they are reframing an existing one for a different context. That reframing is valuable, but it should be named as such.

## My reframe: when reply rate makes sense, and when it does not

Reply rate is worth tracking if:

- You actively invite replies in your emails with a specific, low-friction ask
- You operate in B2B where conversational email is more normalised
- You have a system for responding to and logging what comes back
- You are sending from a genuine reply-to address, not a no-reply

Reply rate is less useful if:

- You are sending high-volume consumer email where replying is not a behaviour your audience has ever been encouraged to do
- You have no operational capacity to handle or learn from what comes back
- You are measuring it as an average across all email types, including transactional and automated, which will skew the data in both directions

The deeper point here is a good one, even if the metric is imperfectly framed: design your emails to invite a response rather than demand a click. Even if not many people reply, the posture of "I want to hear from you" changes the tone of the relationship. And the handful who do reply will tell you more about what your programme is doing than a thousand opens.

## Metric 3: Trustworthiness

### What MarTech & Validty says

![](https://martech.org/wp-content/uploads/2026/03/Screenshot-2026-03-26-at-2.56.20-PM-800x138.png.webp)

*Graphic from Validity 2026 Email Benchmark Report*

The trustworthiness metric proposes measuring trust as a quantifiable KPI using the formula: credibility plus reliability plus intimacy, divided by self-orientation.

The definitions: credibility is believability and competence, reliability is consistency of follow-through, intimacy is the feeling of safety subscribers have sharing their data with you, and self-orientation measures how focused the sender is on their own interests versus the subscriber's needs.

MarTech acknowledges that "variables like these are highly subjective" and suggests starting with customer feedback, replies, and complaint rate monitoring as practical proxies.

### Where I push back

The formula is the problem here, and I am going to be direct about it!

Credibility plus reliability plus intimacy divided by self-orientation is not a metric.

It is a framework for thinking about trust that has been dressed up as an equation.

None of those four variables are independently measurable in any consistent or objective way. Credibility as a subscriber perceives it is entirely subjective. Reliability is directionally trackable but not in the precision the formula implies. Intimacy and self-orientation cannot be quantified from your ESP dashboard or your CRM — they exist entirely in the subscriber's perception, which you cannot access directly.

Presenting this as a KPI that marketers should be tracking implies there is a way to produce a number. There is not — at least not without extensive qualitative research that most email teams neither have the time nor budget to conduct.

There is also a category error in calling this an email metric specifically. Trust is not an email metric — it is a brand and relationship metric that email contributes to, alongside every other touchpoint. If your customer service is terrible, no amount of excellent email will build trust. If your product consistently underdelivers, your newsletter cannot compensate. Trust is an organisational outcome, not an email programme output.

### My reframe: how I would actually track trust through signals

Here is the thing about trust: you cannot measure it directly, but you can measure its effects. And measuring its effects is actually more useful than measuring the abstract concept anyway, because the effects tell you what to do about it.

The signals that indicate a subscriber trusts you:

- Time from sign-up to first meaningful action — a subscriber who purchases, registers for an event, or books a call within days of signing up is demonstrating a level of pre-existing trust or very fast trust-building. Track this by acquisition source and email programme to understand which channels and flows build trust fastest.
- Time from lead to customer — how long does it take someone on your email list to convert? Email programmes that build trust shorten this timeline. Track the conversion timeline for email-active contacts versus those who are not in the programme.
- Repeat engagement over time — a subscriber who has been on your list for two years and still occasionally opens, clicks, or takes meaningful actions is demonstrating sustained trust. Track longevity and continued low-level engagement as a trust indicator.
- Referral behaviour — do your email subscribers refer others? People who trust you enough to put their own reputation behind a recommendation are demonstrating the deepest form of trust. If your CRM can capture referral source, this is worth tracking.
- Complaint rate as an inverse trust signal — a rising complaint rate is one of the clearest signals that trust is eroding. Not the only one, but a direct, measurable, and highly consequential one.

None of these replace the qualitative, relationship-level understanding of trust that comes from actually talking to your subscribers. But they are real signals, measurable in real systems, that tell you something genuine about whether trust is building or eroding over time.

## The bigger point that the article gets right

I want to be clear: despite my pushback on the specifics, the broader argument in the MarTech piece is one I have been making for years.

Opens and clicks — as provided out of the box by your ESP, measured per campaign, reported in isolation — are indicators at best and misleading at worst. They are not proof that your email programme is working. They are not proof that it is not working either. They are data points that need to be contextualised, combined with other signals, and evaluated against meaningful outcomes rather than arbitrary benchmarks.

The email industry has known this for a long time. Apple's Mail Privacy Protection accelerated the conversation in 2021. The proliferation of AI-sorted inboxes has continued it. What Validity and MarTech are doing is correctly identifying that the next stage of this conversation needs to be about what we measure instead.

Where I think they have not quite got there yet is in the specificity of the alternatives. Disaffection rate, as formulated, combines signals of different severity and different nature into a single number. Reply rate is meaningful but not universally applicable. Trustworthiness as an equation is aspirational rather than practical.

The framework I use — and that I have written about in depth in the metrics blog and the meaningful actions blog — is simpler and more actionable:

- Track opens and clicks as indicators — not performance metrics. Use them to spot patterns, spikes, and drops, not to declare success or failure.
- Define your meaningful actions — the things that tell you a subscriber is genuinely engaged with your brand, not just interacting with an email. These are different for every business.
- Measure email's influence on meaningful actions over time — not last-click attribution, but genuine correlation between email engagement and commercial outcomes
- Track the negative signals separately — unsubscribe rate, complaint rate, and bounce rate are three different things requiring three different responses
- Monitor trust through behaviour — conversion timelines, longevity, referral, complaint trajectory

All of the metrics that Validity and MarTech are trying to point toward are real and important. The formulas just need refining — and the context needs expanding beyond what any email dashboard can show you.

## What to do with all of this

If you read the MarTech article and thought "this sounds interesting but I'm not sure what to do with it" — here is the practical answer.

Do not try to implement all three metrics simultaneously. Start with the one that is most relevant to your current situation.

If your list is shrinking or your engagement is declining: focus on tracking negative signals properly. Separate your unsubscribe rate, complaint rate, and bounce rate. Track each one by segment and over time. Look for the pattern — is it sustained, or a short-term spike? Is it concentrated in a specific segment or universal?

If you want to improve the quality of your subscriber relationships: think about reply rate in the context of your specific audience. Are your emails the type that invite a response? Do you have a system for handling replies? If yes — actively invite them and track what comes back. If no — start there before you start measuring.

If you are trying to demonstrate the commercial value of email to stakeholders: trust-building is the hardest to measure directly, but conversion timelines, pipeline influence, and referral data are real numbers you can extract from your CRM. Track email-active contacts through the funnel and compare their behaviour to non-email contacts. The difference is your programme's commercial contribution.

And in all cases: go and read the metrics blog linked below, which goes deeper on meaningful actions and how to build a reporting framework that actually reflects what email is doing for your business.

### Further reading from The Vault:

- [Stop Relying on Email Opens and Clicks](https://weareastral.co.uk/thevault/stop-relying-on-email-opens-clicks-better-metrics-for-email-marketing)
- [Stop Reporting on Opens and Clicks. Here's What to Measure Instead](https://weareastral.co.uk/thevault/stop-reporting-on-opens-and-clicks.-heres-what-to-measure-instead)
- [The Billboard Effect: How Email Builds Awareness Without a Single Click](https://weareastral.co.uk/thevault/the-billboard-effect)
- [Email Is an Impact Channel, Not a Conversion One](https://weareastral.co.uk/thevault/email-is-an-impact-channel-not-a-conversion-one-and-thats-a-good-thing)
- [The Laws of the Inbox](https://weareastral.co.uk/thevault/the-laws-of-the-inbox)
- [Validity 2026 Email Deliverability Benchmark Report](https://www.validity.com/resource-center/2026-email-deliverability-benchmark-report/)
- [MarTech: 3 New Email Metrics That You Need in 2026](http://martech.org/3-new-email-metrics-that-you-need-in-2026/)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.
