---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/who-owns-email-deliverability-not-it?utm_medium=email&_hsenc=p2ANqtz-82BUhpAr8HryV5NLaN4YlhuiDYtdDON6Y_edGlga3XdCA6jjWUzKmV2xUc9ka8TBrPRycWUQW6OLgmZwlkJvXWKqWivnwVsSFBn8kgc1_ipihTOtg&_hsmi=146462425&utm_content=146421244&utm_source=hs_email"
published: 2026-09-23
created: 2026-09-24
tags:
---


Ask a business who owns deliverability and most of them say IT, or our IT sort it or set it up (deliverability can't be set up).

Wrong answer if you said that, and it is one of the main structural reasons email programmes end up in trouble.

IT should not own your DNS and authentication as a decision. Marketing should own it, with IT supporting the function and executing the changes.

Whoever controls, leads or manages the email marketing function owns deliverability. Aswell as all the people executing it - it's ALL your responsibility.

The head of CRM, the email manager, the marketing director, the founder doing it themselves, the email marketing exec, the marketing manager. The leader of the function is the owner, and it is not delegable.

If you look after an email function and you are not sure of your deliverability, you are failing at part of your role (in the nicest way possible!!). Not being harsh I swear, I just don't want you to end up where I've seen many teams and people this year because they had no idea what their email deliverability is!

## The default answer is always IT

Nothing against IT (or maybe a little). The problem is that the ownership sits in a place with no visibility of the thing that causes deliverability problems.

- IT cannot see your sending behaviour. They do not see your list quality, your frequency, your complaint rate, your segmentation, your acquisition sources or what you promised people at signup. All of which are the actual causes. And it's not their job to understand this either.
- They implement records, they do not set strategy. A DNS change is a ticket. Whether you should be moving DMARC to enforcement this month, given what marketing is about to send, is a judgement that requires knowing what marketing is about to send.
- The timescales do not match. Deliverability degrades over months (sometimes years). IT works in tickets, sprints and incidents. Slow erosion never generates a ticket, so it never gets noticed until it is an emergency.
- Nobody checks the outcome. Marketing asks for a change, IT makes it, the ticket closes. Whether the change improved placement is not on anybody's list.
- And there is no accountability for the result. When placement collapses, IT has no incentive to notice, no data to notice with, and no reason to believe it was theirs to watch.

So you end up with a shared arrangement where marketing cannot change anything and IT cannot see anything, and the thing itself belongs to nobody.

## Deliverability is behaviour, not configuration

The real definition of deliverability is... Email Deliverability is the ongoing health of your sending reputation, a condition shaped by your behaviour over time, which determines whether you reach the inbox rather than spam.

Behaviour, not configuration. Configuration is the small part you set up once and maintain. Behaviour is everything you do every week, and behaviour is owned by whoever decides what gets sent.

### This is what builds (positive) or destroys (negative) deliverability

- Who you send to, and who you leave out ([exclusions](https://weareastral.co.uk/thevault/stop-sending-the-wrong-emails-step-by-step-exclusion-strategies) are your best friend!!)
- How often you send, and to which segments
- What you send, and whether it is worth receiving
- How you acquire people, and what you promised them (and the type of acquiring - [see this blog here](https://weareastral.co.uk/thevault/intentional-vs-consequential-opt-ins))
- Whether you suppress, and how quickly
- Whether you separate your streams
- How easy you make leaving (unsubscribing)

Every single one of those is a marketing decision (duh!).

### The things IT should be doing

- Publishing and maintaining DNS records to the specification marketing asks for.
- Domain and subdomain setup, once the structure has been decided.
- Access, security and infrastructure.
- Flagging anything that would break what marketing is trying to do.

IT is the executor and the enabler. Marketing decides, IT implements, and getting that relationship the wrong way round is the single most common structural error I find on audits.

## The owner

## The leader of the function owns it (and ulitmately responsible for it)

Not a specialist somewhere in the team, not an agency (for the love of biscuits do not let anyone outside your business be responsible for it; I am a specialist, but I NEVER own my client's deliverability), not a tool. The person who leads the email function, whatever their title happens to be.

Which is uncomfortable if you lead an email function and have never looked at your placement, and it is meant to be. Deliverability is not a specialism sitting alongside your job; it is the condition that determines whether your job produces anything at all.

### What that means in practice

- You know your numbers. Placement by provider, complaint rate, bounce rate, and the trend on each. Not perfectly, and not daily, but you know roughly where you stand, and you would notice a change.
- You can explain them in really simple commercial terms. To a board, to a finance director, to a sceptical CEO, without needing somebody from IT in the room.
- You can say no to a send. And you are prepared to, when the request would damage the programme. Ownership without a veto is just blame in advance.
- You are in the room for decisions that affect it. Acquisition changes, a new signup flow, a rebrand, an ESP migration, a sales team deciding to do outbound from the main domain.
- You escalate before it is an emergency. Because recovery takes months now and the cheap window is early.

## Everybody else

## Who affects deliverability without owning it

Plenty of people can damage your deliverability. None of them own it, and the distinction matters because an input is not an owner.

- IT. DNS, records, infrastructure and access. Executes what marketing specifies and flags what will break.
- Data and operations. List hygiene, deduplication, acquisition source tagging, the joins between systems. Quietly one of the biggest influences on your complaint and bounce rates.
- Legal and compliance. Lawful basis, consent language, retention. Advises on what is permissible, does not decide what is sensible.
- Product. The one that surprises people. Signup flows, the unsubscribe experience, transactional email and in-app notifications. A product team can create a forced opt-in problem without ever speaking to marketing.
- Sales. Outbound, and specifically whether it is running from your main domain. A single enthusiastic prospecting campaign can undo a year of careful sending.
- Customer service. How complaints get handled, and whether unhappy customers stay on marketing lists while their issue is open.
- Finance. Holds the budget for fixing it, and will not release it until somebody explains the revenue consequence in their language.

### The failure mode, written out

IT controls DMARC policy and has no idea what moving to enforcement does to a marketing send. Marketing controls what gets sent and cannot edit a DNS record. Product ships a new signup flow that bundles marketing consent and never mentions it. Sales starts prospecting from the company domain because that is what they had access to. Service leaves complainants on the list because removing them is somebody else's system.

Every one of those people did their job correctly. Placement falls twenty points over eighteen months, and there is no meeting where anybody would have noticed, because the outcome belongs to nobody!!

## Making it real

## What the owner needs in order to function

1\. Visibility

Google Postmaster Tools access, Microsoft SNDS, placement testing, and complaint and bounce data broken down by source and segment. You cannot own a number you cannot see. And of course being able to run a FULL Email Deliverability Audit - y **[ou can learn how to do one here](https://weareastral.co.uk/emaildeliverability/training)**.

2\. Authority to say no

A documented right to stop or reduce a send that would damage the programme, agreed before the argument rather than during it.

3\. A seat at the decisions that affect it.

Acquisition, product, sales enablement, rebrands, migrations. If email finds out after the fact, email owns a problem it had no chance to prevent.

4\. An agreed way into IT

A named contact, a rough turnaround expectation, and a shared understanding of which changes are routine and which are risky.

5\. A monitoring cadence somebody keeps

Weekly glance, monthly review, quarterly deeper look, and a baseline written down while nothing is wrong.

6\. A line in the reporting

Placement and complaint rate reported upward regularly, so that when it moves, the business has already been told it matters.

### If you have been handed it with none of that

Common, and worth handling deliberately rather than resenting.

- Get the visibility first. Postmaster access and your own complaint data cost nothing and change the conversation immediately, because you arrive with numbers rather than concerns.
- Write down what you do not control. A short list of the decisions affecting deliverability that sit elsewhere. Not to blame anybody, to make the gap visible.
- Ask for one thing. The veto, or a seat in one meeting, or Postmaster access. Asking for a whole governance model gets nothing. Asking for one thing usually gets it.
- Put the revenue number on it. Roughly fifteen per cent of a typical send does not reach the inbox (you need to run your own audit to understand your spam placement rate btw, don't just rely on this). Work out what that is worth in your business and say it out loud. Finance directors move faster than anybody else on this once they understand it.

## The conclusion

Deliverability is not a technical discipline that marketing has to tolerate. It is the condition of the channel marketing runs, shaped almost entirely by decisions marketing makes, and it belongs to the person who makes them.

IT supports it. Data supports it. Legal advises on it. Product, sales and service can all damage it. None of them own it, and handing it to any of them is how a programme ends up with nobody watching the one number that determines whether any of the work reaches a human being.

If you run email, you own this. Learn it, watch it, and be able to explain it. It is the most valuable thing you can know in this job and the thing fewest people in it can do.