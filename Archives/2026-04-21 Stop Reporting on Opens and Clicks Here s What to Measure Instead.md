---
type: Web
authors: '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/stop-reporting-on-opens-and-clicks.-heres-what-to-measure-instead?utm_medium=email&_hsenc=p2ANqtz-8DH3Sao32f7rL-2SbdVv8vE_EPx5McRY_GdZ6DD967KFbGlIBZWvUq27Hr7nNC3B8U2TxogyYZkai3wqzGbH3ybNR_aLi7eDOyYuNzA0bMvdwlVd0&_hsmi=134083242&utm_content=133965696&utm_source=hs_email
published: 2026-04-21T00:00:00.000Z
created: 2026-04-23T00:00:00.000Z
tags:
  - digital-campaigning
  - strategia-organizacji
  - fundraising
---


The email industry has been measuring success with the wrong tools for YEARS.

Not because people are bad at their jobs, but because email service providers handed us a dashboard, which showed opens and clicks, and so opens and clicks became the definition of whether email was working. We didn't choose them. We inherited them!

And the world has moved on considerably since those metrics made sense — but the dashboards haven't changed, the stakeholder reports haven't changed, and the conversations in most email teams haven't changed either.

So this blog does two things. First, it explains what is actually happening when your ESP reports an open — because understanding why opens are unreliable as a success metric is the thing that will give you the confidence to explain it to your boss, your stakeholders, and anyone else who still thinks a 40% open rate means the email worked. Second, it gives you the framework I actually use for reporting: what meaningful actions are, how to track them, and what good email measurement looks like when you stop defaulting to what the platform gives you.

Let's start with the metric itself.

## What is an open rate, really?

Before we talk about why opens are unreliable, it's worth being precise about what an open actually is — because most marketers have never thought about the mechanics underneath the number.

An open is recorded when a tracking pixel fires. That's it. A tracking pixel is a tiny, invisible image embedded in the code of your email. When someone opens your email and their device downloads the images, that pixel fires, sends a signal back to your ESP, and your platform records it as an open.

What the open does not tell you:

- - Who opened it — the pixel just knows it fired
		- Whether they read it
		- Whether they cared
		- Whether they took any action at all

What it does tell you:

- - A device downloaded your images
		- That device was associated with a contact on your list

That is a much more limited piece of information than most reporting treats it as. And it gets more complicated from there — because of everything that has happened to email infrastructure since opens became the default metric.

## Why opens are unreliable — the actual reasons

You've probably heard that opens aren't reliable. What you may not have is a clear explanation of why, in enough detail to actually be useful in a conversation. Here it is.

Apple Mail Privacy Protection (AMPP)

This landed on 20 September 2021 and changed email measurement permanently. Apple's Mail Privacy Protection feature — which operates across the Apple Mail app on iPhone, iPad, and Mac — pre-loads email content, including tracking pixels, before the recipient actually opens the email.

What this means in practice: if any portion of your audience uses Apple Mail as their default email app, those emails are being recorded as opened whether they opened them or not. Apple pre-fetches everything. The pixel fires. Your ESP reports the open. The person may never have looked at the email.

For most consumer-facing programmes, Apple Mail users are a significant portion of the list. Which means a meaningful slice of your open rate is technically fictional — those emails appeared opened, but whether anyone saw them is a completely separate question.

**The reality:**

Apple Mail over-reports. Your open rate is inflated for every Apple Mail user on your list. You have no way of knowing by how much.

Outlook's reading pane — the opposite problem

While Apple Mail inflates your opens, Outlook suppresses them.

The default view in the Outlook desktop and web app is the reading pane — where you see your email list on the left and the email content on the right. In this view, images are off by default. Because the tracking pixel lives inside the images, it doesn't fire unless the person explicitly downloads the images.

So in B2B environments, where Outlook is dominant, a huge portion of your audience could be reading every word of your email in the reading pane and never triggering an open. Your open rate is underreported for this audience — sometimes significantly.

The net result: for many B2B programmes, Apple Mail is inflating opens on the consumer side and Outlook is suppressing them on the professional side. The number you see in your dashboard is being pulled in two directions simultaneously. It tells you almost nothing useful about actual behaviour.

Gmail clipping

If your email is long enough that Gmail clips it — showing a 'view entire message' link at the bottom — the tracking pixel may not fire even if the person opens and reads the whole thing in Gmail. The pixel is in the part of the email that didn't load.

This is a real issue for newsletters and longer-form emails. Your opens are being underreported for everyone reading on Gmail who hits the clip threshold.

Corporate bots and security scanning

In B2B environments, corporate security tools — Mimecast, Barracuda, Proofpoint, Microsoft Defender — scan incoming emails by following every link and pre-loading content to check for threats. When they do this, they fire your tracking pixels.

This means opens and clicks recorded in B2B campaigns can include the security platform's scan, not a human being's interaction. In some cases this happens before the email has even been delivered to the inbox. You can also see this as the reason why switching ESPs often shows dramatically different click numbers — each platform tracks differently and captures bot activity differently.

Open-to-delete behaviour

Even setting aside all the technical factors, there is a fundamental human behaviour issue with using opens as a success metric.

A significant portion of your audience opens emails to delete them. That is their inbox habit. They scroll through, they open things to clear the unread indicator, they delete without reading a word. The pixel fired. The open was recorded. Your ESP thinks they engaged. They didn't.

This is particularly visible in B2C programmes where open rates can look healthy but click rates are extremely low — because nobody opened those emails to take action. They opened them because that is how they manage their inbox.

## There is no such thing as a good open rate

I get this question constantly: "What open rate should we be getting?"

My answer, which I know is unsatisfying: there isn't one.

With everything described above happening simultaneously — Apple inflating, Outlook suppressing, Gmail clipping, bots firing pixels, humans opening to delete — the number you are looking at is a product of your audience's device and app choices, your email's length, the corporate infrastructure your B2B contacts sit behind, and your ESP's specific tracking methodology. None of that is the same as another business. Which is why industry benchmarks for open rates are nearly meaningless as a comparison point. You are comparing incomparable numbers.

When I go into an email audit, I do not care about open rates as a performance indicator. What I will look at is whether the open rate is very significantly lower than I'd expect given the quality of the list.

If I'm looking at a programme with a healthy, intentionally-built list of people who signed up because they genuinely wanted what was on offer — and the open rate across all email types is sitting under 10-15% — that's a flag. Not because 10% is 'bad', but because something is likely wrong. Either a deliverability issue meaning the emails aren't reaching inboxes, a content issue meaning the value proposition broke down somewhere, or a list composition problem where too many consequential opt-ins have diluted the quality of the audience.

But that's an open rate being used as a diagnostic, not a success metric. There's a significant difference between the two.

## What opens are still useful for

I want to be clear here: I am not saying delete opens from your reporting entirely. I am saying stop treating them as a success metric and start treating them as what they actually are — an indicator that pairs with other signals to tell you whether something worth investigating has happened.

### Track by email type, not overall average

The single most common mistake I see in email reporting is people looking at an overall average open rate across their entire programme. If you are sending welcome emails, re-engagement flows, newsletters, promotional campaigns, post-purchase sequences, and service emails all from the same domain, and then averaging the opens across all of them — that number is meaningless.

A welcome flow email to someone who has just downloaded a lead magnet, who is going into their inbox specifically to retrieve it, will naturally have a high open rate. A newsletter send to a long-established list will have a different pattern entirely. A promotional email to a mixed segment will look different again.

What you want to do is establish a baseline by email type. Your newsletter sits in a range. Your transactional emails sit in a range. Your re-engagement emails sit in a range. Once you have those baselines, you can use significant movement away from them as an indicator.

### Spikes and drops are the signal — not the number itself

A significant drop in opens for a specific email type — 7%, 10%, 15% overnight — is worth investigating. Not because the open rate proves anything, but because a sudden pattern change suggests something else has changed. It could be a deliverability issue. It could be a content shift. It could be a technical problem with how the email was built.

Equally, a dramatic spike — your newsletter suddenly hitting twice its normal open rate — is also worth investigating. Not to celebrate, but to understand. Clickbait subject lines produce spike opens. So does sending to a segment that normally doesn't get your emails. The spike is a question, not an answer.

Use opens for pattern recognition. Stop using them to declare success.

## Are clicks better? Yes — but not by as much as you think

Clicks are a stronger signal than opens. When someone clicks a link in your email, they have taken a deliberate action. They made a choice. That is meaningfully different from an open, which could mean almost anything.

But clicks have their own limitations.

- Security software auto-clicks. The same corporate security tools that pre-load images also follow links to scan them. Those clicks appear in your ESP as human interactions.
- Cross-device tracking breaks attribution. Someone reads your email on their phone, then opens it later on their desktop and clicks. The device change creates gaps in how that journey is tracked.
- Different ESPs track clicks differently. I have seen programmes move from one platform to another and watch reported click rates shift dramatically — not because the programme changed, but because the two platforms handle bot filtering and tracking methodology differently.
- A click is not a conversion. Someone clicked. They went somewhere. What they did when they got there is a completely different question that click data alone cannot answer.

Clicks are worth tracking. Click-to-open rate is a useful ratio for understanding the quality of engagement among people who opened. But the same fundamental problem remains: a high click rate does not tell you that your email worked. It tells you that people clicked. What you actually need to know is what happened next — and that requires looking outside of the email platform entirely.

## Moving beyond the dashboard: meaningful actions

This is the section that changes how you think about email measurement.

Every business has actions that genuinely indicate engagement, intent, or progress toward a commercial outcome. These are what I call meaningful actions — and they are the thing you should be building your email reporting around.

A meaningful action is anything a subscriber does that signals real engagement with your brand or business. Not an open. Not even necessarily a click. Something that tells you: this person is actively involved with what we do.

### What a meaningful action looks like

The specific meaningful actions will vary by business type, but the principle is consistent. Here are examples:

- - Downloaded a resource or lead magnet
		- Signed up to an event, webinar, or masterclass
		- Visited a high-intent page (pricing, services, contact, product detail)
		- Submitted an enquiry form or booked a call
		- Made a purchase
		- Completed a quiz, assessment, or survey
		- Replied to an email directly
		- Signed up to a pop-up or secondary opt-in
		- Logged into a customer portal or product
		- Renewed a subscription or contract

Notice what is not on that list. Opening an email. Those are outputs of behaviour. Meaningful actions are the behaviour itself.

### The John example

Let me make this concrete.

Say John (I actually don't know any John's btw, but if you're called John - hey) signed up to your newsletter a year ago. John has not opened a single email in the last three months. By standard email reporting logic, John is disengaged. He should probably be on a re-engagement campaign, even maybe he should be suppressed.

But here's what John is actually doing: he visits your blog every week. He attended one of your webinars last month. He has visited your services page four times in the past fortnight.

John is not disengaged. John is in research mode. He is building familiarity with you, probably building a case internally, possibly getting close to a conversation. The email is reaching him — it is showing up in his inbox and contributing to his awareness of you. He is just not opening it in a way your tracking pixel can see.

If you had suppressed John based on email engagement alone, you would have removed a warm prospect from your programme at the moment he was getting closest to a decision.

This is the core argument for meaningful actions. You need to look at what people are doing, not just what they're doing in the email.

### The difference by business type

Meaningful actions look different depending on your context, and it's worth being specific:

B2B:

- Meaningful actions tend to be high-intent and lower frequency. Webinar registration, content downloads, pricing page visits, enquiry forms, sales conversations triggered. The buying cycle is longer, so you're looking at meaningful actions over a 30, 60, 90-day window.

B2C and D2C:

- Meaningful actions are typically transactional and more frequent. Purchases, product page visits, cart additions, wishlist additions, loyalty programme interactions, review submissions. The window might be tighter — 7 to 30 days — but the principle is the same.

Charities and non-profits:

- Meaningful actions often look like donations, volunteer sign-ups, event registrations, campaign shares, petition signatures. Email's role is mobilisation and stewardship, and your reporting should reflect that.

SaaS and subscription businesses:

- Meaningful actions are often in-product: feature adoption, session activity, upgrade behaviour, renewal engagement, support ticket patterns. Email in these contexts is often about retention and activation, and the signal of whether it's working is inside the product, not the inbox.

The question to ask for your business is: what would tell us that this person is genuinely engaged with us right now? Build your meaningful actions list from the answer to that question.

## How to report on email properly — the quarterly framework

Now the practical bit. Here is how I actually structure email reporting, both for my own programme and when I work with clients. It is deliberately designed to move the conversation away from opens and clicks and toward the signals that actually tell you something useful.

### What to track consistently

These are the things worth monitoring regularly, framed correctly:

### The quarterly reporting structure I use

Rather than reporting per campaign in isolation, I look at programme health over a rolling 90-day period. Here's the framework:

- - List health — how many active contacts, how many meaningful action takers, how does list composition look (intentional vs consequential opt-ins), what does new subscriber engagement look like in the first 30 days
		- Engagement quality — not volume of opens, but what percentage of the active list took at least one meaningful action in the period. This is your real engagement rate.
		- Programme influence — what commercial outcomes (leads, enquiries, sales, renewals, bookings) occurred during the period, and what portion of those contacts were active in the email programme
		- Deliverability health — any significant changes in bounce rates, complaint rates, or unusual open rate patterns that suggest placement issues
		- What changed and what we learned — what did we test, what did the data suggest, what are we doing differently next quarter

This framework is not easy to build if your CRM and email platform don't talk to each other. Which is one of the reasons I am a strong advocate for connected ecosystems — because you cannot report on meaningful actions if the only data you have is what your ESP dashboard shows you.

### The attribution question — being honest about it

Email attribution is genuinely hard, and I think it's important to be honest about that rather than pretend otherwise.

In Klaviyo, for example, the default attribution model credits email with a purchase if the contact received an email in the last 30 days and made a purchase. That is a very generous window. It means an email I sent three weeks ago that you never opened gets credited when you buy today because you saw an Instagram ad that converted you.

This is not a Klaviyo-specific problem. Attribution across any channel is messy because humans do not make decisions in single linear steps. They see something in their inbox, they search for it later, they see it on social, they visit the website, they Google the brand name, they buy. Email might have been the first touchpoint, the middle touchpoint, or completely irrelevant. You cannot always know.

What you can say honestly is: email was a touchpoint in this person's journey. Email contributed to their familiarity with us. Email is an assister in our revenue. That is a defensible, accurate position. Claiming email generated £X of revenue because the attribution model said so is not.

## The challenge of system limitations — and what to do about them

I want to address something real, because this is where a lot of email marketers get stuck.

Everything I have described above — meaningful actions, cross-channel influence, programme health over time — requires data from outside your email platform. You need CRM data, website behaviour data, conversion data, sales pipeline data. And for many teams, that data is either in different systems that don't connect, or it requires significant technical setup to make usable.

This is a genuine constraint and I don't want to be glib about it. If your email platform and your CRM are separate and not integrated, you are limited to what the email dashboard shows you. And in that situation, it's harder to move away from opens and clicks because they're the only numbers you have.

But here is what you can do, even with limited systems:

- - Start defining your meaningful actions list now, even if you can't fully track them yet. Knowing what you're looking for is the first step.
		- Push for the system connections that make better measurement possible. This is a commercial argument: "we can't prove the value of email without connecting it to what happens after someone clicks." That is a conversation worth having.
		- Use the data you do have more intelligently. Track open rate ranges by email type. Monitor complaint rates. Look at website traffic patterns in the days after major sends. Use what you have while building toward better.
		- Stop reporting averages. Even without better data, you can report more intelligently on what you have by being more specific about what each number means and doesn't mean.
		- Be honest with stakeholders about what opens mean. You do not have to have a perfect reporting framework in place to have a conversation about why a 40% open rate is not evidence that the email worked. You can start that conversation now.

Better measurement is a direction of travel, not a switch you flip overnight. Start moving in the right direction.

## What to do this week

This is where I want to leave you with something practical.

- Stop using opens for subject line testing. It's measuring the wrong thing in the wrong way. Use clicks, replies, and downstream actions instead.
- Map your email types and establish a baseline open rate for each. Not to celebrate or panic about the number — just to have a reference point for when something changes significantly.
- Define your meaningful actions. Write them down. What does genuine engagement with your brand or business look like? What would tell you a subscriber is alive and interested?
- Find one way to connect email activity to a meaningful action. Even if it's manual and imperfect — even if you are cross-referencing two spreadsheets — start building the habit of looking at what happens after the email.
- Change the conversation in your reporting. You do not have to overhaul everything at once. But you can start framing opens as indicators rather than success metrics the next time someone asks about them.

The goal is not to throw away the data you have. It is to understand what it is actually telling you — and to stop asking it questions it cannot answer.

### Further reading from The Vault:

Why Opens and Clicks Are Lying to You — weareastral.co.uk/thevault (existing blog)  
[Email Is an Impact Channel, Not a Conversion One](https://weareastral.co.uk/thevault/email-is-an-impact-channel-not-a-conversion-one-and-thats-a-good-thing)  
[SIO: Search Inbox Optimisation](https://weareastral.co.uk/thevault/sio-search-inbox-optimisation)  
[The Science of Inbox and Email Attention](https://weareastral.co.uk/thevault/the-science-of-attention-why-people-really-stop-reading-your-emails)  
[What Email Deliverability Actually Is](https://weareastral.co.uk/thevault/what-email-deliverability-actually-is-and-the-3-metrics-that-really-matter)  
[How to Email More People Without Ruining Your Deliverability](https://weareastral.co.uk/thevault/how-to-email-more-people-without-ruining-your-deliverability)  
  

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.
