---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/email-qa-how-to-proof-and-test-your-emails-before-sending?utm_medium=email&_hsenc=p2ANqtz-_h-LLyai00b6U3gehhVzG_KKvFG6YbQGCE5ttK5sZjmBTKbzYzULvt3kJRkQMQI_EaDZCBVYxmQJPUV2JqI_nC8ZgxTgnRJQpsTaXsBlPsj7Zo2A8&_hsmi=135269154&utm_content=135270488&utm_source=hs_email"
published: 2026-05-07
created: 2026-05-07
tags:
---


I am going to be completely honest with you upfront: I am VERY bad at this when it comes to my own emails.

I am impulsive. I get the email written, I check the important stuff, and I want it out. I have sent emails with small design quirks, the odd formatting issue, the occasional line that sits slightly wrong on a specific device. And you know what? Someone once emailed me because my email was completely invisible on their version of Outlook. They could not see anything. They bought two masterclass tickets anyway.

So when I talk about email QA, I am talking about it as someone who genuinely believes that getting something slightly imperfect out the door — with the messaging right, the exclusions right, the strategy right — is almost always better than spending three weeks making the footer pixel-perfect while the moment passes.

That said, there is a framework. And it matters. Not because every email needs to be flawless before it goes out, but because the things that genuinely damage your programme — the wrong message to the wrong audience, the deliverability risk from a poorly segmented send, the negative association from an email that should never have been sent at all — are entirely avoidable with a structured approach.

This blog gives you that framework. Three layers, in the right order, with a practical checklist for each.

## The order matters

Most email QA processes work from the outside in. You check how the email looks, you test the links, you make sure the images load, and then — if you have time — you might think about whether this email should actually be going to this list.

That is backwards.

The things that matter most happen long before you open Litmus. The strategic questions — who is receiving this, what are they thinking right now, is this going to help or harm the relationship, is this going to hurt deliverability — are the ones that should be answered first. Because if the answers to those questions are wrong, no amount of device testing is going to save you.

A perfectly rendered email going to the wrong people at the wrong time is a much bigger problem than a slightly imperfect email going to exactly the right people with exactly the right message.

Here is the order. Three layers. Start at Layer 1 and work your way down.

## LAYER 1 - Help or Harm?

#### Deliverability and risk, before anything else.

Before you think about who receives this email or what it says, ask the deliverability question: is sending this email going to help your sender reputation, harm it, or make no difference?

This is not a question most teams ask. It should be the first one.

### Volume risk

One of the most reliably dangerous things an email programme can do is dramatically increase send volume in one go. Inbox providers watch sending behaviour patterns. A sudden spike — from 20,000 contacts to 300,000 contacts in a single send — is a recognised red flag. It is the kind of pattern associated with acquired lists, compromised accounts, and spam operations. Even if every contact is legitimate, the pattern itself triggers scrutiny.

I have seen this happen. A brand did a rebrand and decided to tell their entire database. They usually sent to around 20,000 people. They wanted to send to 300,000. Nobody on the team raised a hand to ask whether this was safe. The deliverability impact was significant and took months to recover from.

If you are planning a send significantly larger than your usual volume, that needs a warm-up plan. Not a three-day plan. A proper, gradual ramp that gives providers time to trust the pattern.

### List quality risk

How old is this list segment? When were these contacts last emailed? Have you validated the addresses recently? Old lists carry bounce risk, and a bounce spike is a negative event that damages sender reputation immediately and sometimes severely.

If you are emailing a segment that has been sitting uncontacted for six months or more, run it through a validation tool before you send. Remove hard bounces. Check for spam trap risk. The five minutes this takes is worth considerably more than the reputation damage from getting it wrong.

## LAYER 2 - In or out?

#### Segmentation, exclusions, and messaging alignment.

This is the layer I wish every marketing team spent more time on. Not because it is complicated — it is not. But because it requires a mindset shift that most teams have not made yet.

The shift is this: getting the list smaller is the goal, not the compromise.

We have been conditioned to believe that larger lists equal better results. More people receiving the email means more opens, more clicks, more conversions. So we include as many people as possible, we set exclusions as a reluctant afterthought, and we send to anyone who technically qualifies.

This is exactly wrong. The most powerful thing you can do for your email performance — and for your deliverability — is be ruthlessly precise about who should and should not receive this specific email. Not who could receive it. Who should.

### Exclusions first — always

Before you think about who is in, get everyone who should definitely be out out first.

The people who should almost always be excluded from any campaign send:

- Anyone with an active open complaint or unresolved customer service issue
- Anyone who has unsubscribed or been suppressed — this should be automatic, but check it
- Anyone who has already received this message through another route
- Anyone whose lifecycle stage makes this message irrelevant — a customer receiving a new customer welcome, a prospect receiving a loyalty communication
- Anyone who is mid-way through a sales conversation that this automated send might disrupt or confuse
- Anyone in a segment that would logically be affected by this message in a negative way

The last one is the one most teams miss. Think about what else is happening. Who has just purchased something and should be in a post-purchase flow, not a promotional campaign? Who has just submitted a complaint that makes receiving a celebratory email actively damaging to the relationship?

### Who is actually in — and should they all be?

Once you have excluded everyone who should be out, look at what remains. Is this genuinely a coherent audience? Do the people in this segment share enough context that the same message makes sense for all of them?

If the answer is no — if you have a mix of people at very different stages of the journey, with very different relationships to your brand, with very different levels of intent — the email needs to be either more specific in its targeting or more flexible in its messaging. Or both.

The question to ask for every segment: if this email landed in their inbox right now, given everything you know about where they are and what they are dealing with, would it feel relevant? Would it feel like you understand them? Or would it feel like noise?

### Messaging alignment — the most important pre-send question

Once you have the right audience, read the email again. Not from your perspective — from theirs.

Think about what they are thinking and doing when this email arrives. Use TFDS: Think, Feel, Do, Say. What is this person's mental context when they open their inbox? What problem are they sitting with? What does their relationship with your brand look like from their side?

Then ask: does this email speak to that?

If the email is about something completely disconnected from where the subscriber is right now — if it is pushing a product at someone who just complained, if it is selling to someone who is deep in a learning phase, if it is being promotional at someone who signed up for thought leadership — the messaging is misaligned. No amount of perfect design will fix that. The email will feel irrelevant. And irrelevance builds negative associations.

## LAYER 3 - Does it work?

#### Technical testing, rendering, and the final deployment check.

This is the layer most teams spend the most time on. It should be the last layer, not the first. But it still matters — and there are things worth checking properly before anything goes out.

The realistic framing here: you cannot guarantee a perfect experience across every email client, every device, every version of every app, for every person on your list. You cannot. There will always be someone on an outdated version of Outlook on a PC from 2014 who sees something unexpected. Your job is to get it right for the majority, to catch the things that would genuinely break the email for significant portions of your audience, and to make peace with the reality that perfect is not possible.

### Build and test a template — not individual emails

If you are sending regularly, the most efficient approach is to develop and thoroughly test a template that you know works across the main environments, and then work within that template. Testing every email from scratch every time is not realistic — and if you are trying to do that, you will either spend too long on it or cut corners on the things that matter more.

Test the template exhaustively once. Know where it is strong and where it has limitations. Then for individual sends, focus your testing on the elements that have changed — new image blocks, unusual formatting, significantly different layouts from the template standard.

### The environments that matter most

Priority testing environments in order of audience impact:

- Mobile — specifically iOS Mail and Gmail on Android. The majority of consumer email is opened on mobile. If it does not work on a phone, it does not work.
- Gmail web — the largest single email client globally.
- Outlook desktop (Windows) — the most common B2B environment and the one most likely to cause rendering issues. Test on current versions.
- Dark mode — across all of the above. Dark mode is default for a significant proportion of users. If your design relies on a white background for text contrast, it may become unreadable in dark mode.
- Images-off rendering — especially important for B2B where Outlook defaults to images off. What does your email look like with no images? Can someone still understand the message and find the call to action?

### Tools for rendering tests

You do not need to manually test across every environment. Rendering test tools do this for you:

- Litmus — renders your email across a wide range of clients and devices simultaneously. Includes accessibility checks and dark mode previews.
- Email on Acid — similar functionality to Litmus, different pricing structure. Worth evaluating both.
- Your ESP's built-in preview — useful for a quick sanity check but not a substitute for a proper rendering test tool. Most ESPs only show a handful of environments.

### The things most commonly missed

Based on what I see go wrong most often:

- Links not working or pointing to the wrong destination — check every link, every time. Especially dynamic links, UTM parameters, and any links that were pasted from a previous version of the email.
- Preheader text not set — or set to something that makes no sense, or the email client is pulling in the first line of body text instead. Check what actually appears in the inbox preview.
- Mobile text sizing — a three-line paragraph on desktop can become six lines on mobile, pushing the call to action far below the fold. Check your mobile rendering carefully.
- Alt text missing on images — for accessibility, and for the images-off experience. Every image should have meaningful alt text.
- Unsubscribe link not working — test it. Every time. A broken unsubscribe link is both a legal risk and a deliverability risk.
- From name and reply-to address correct — especially if you are sending from a template that was originally configured for a different sender or campaign.
- Subject line and preheader cut-off on mobile — test what actually appears in an inbox preview on a phone. On most devices you have around 30-40 characters before the subject line is truncated.

## The framework at a glance

Layer 1 — Help or Harm? (Do this first)

**Deliverability and risk.**

Is this going to protect or damage our sender reputation? Volume check, list quality check, domain safety check. If anything here is a red flag, resolve it before going anywhere near the content.

Layer 2 — In or Out? (Do this second)

**Segmentation, exclusions, and messaging alignment.**

Who should definitely not receive this? Get them out first. Then look at who remains and ask honestly: does this message make sense for all of them right now? Use TFDS. Be strict.

Layer 3 — Does It Work? (Do this last)

**Technical rendering and deployment checks.**

Test the template, not every individual email from scratch. Focus on mobile, dark mode, images-off, links, and the preheader. Use a rendering tool. Check your actual inbox.

## The truth about email quality assurance

Perfectionism kills email marketing. I have seen marketing teams spend three weeks perfecting a template while a genuinely useful email sat unsent, the moment passed, and the audience moved on. That is not quality assurance. That is fear dressed up as rigour.

Real quality assurance is about asking the right questions in the right order. And the right order puts strategy and risk before aesthetics. Always.

The email that goes out with a slightly imperfect logo but lands with the right message, to exactly the right people, at exactly the right moment — that email does its job. The perfect email that goes to the wrong people, or creates a deliverability problem, or builds the wrong association, or disrupts a sales conversation — that email fails regardless of how good it looks.

Layer 1, then Layer 2, then Layer 3. In that order, every time.

Get the important stuff right first, then the rest is detail.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.