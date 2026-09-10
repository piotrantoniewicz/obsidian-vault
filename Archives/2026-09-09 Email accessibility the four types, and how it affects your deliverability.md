---
type: Web
authors: '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/email-accessibility-the-four-types-and-why-it-affects-your-deliverability?utm_medium=email&_hsenc=p2ANqtz--1yElViC-0KmngY1GJZIXvbc4vBU8269zgfarEC05tKINXa9XTyAAosW2VWRbInExMFHFzKUCk9jCN3I2puM03nfgXytVbHtd7Tzjb_msftBLPH8E&_hsmi=145370304&utm_content=145358476&utm_source=hs_email
published: 2026-09-09T00:00:00.000Z
created: 2026-09-10T00:00:00.000Z
tags:
  - fundraising
  - digital-campaigning
  - content-marketing
---


The accessibility conversation in email is stuck in two places. Somebody raises the legal position, everybody nods, a task goes into a backlog. Or somebody makes the moral case, everybody agrees because, obviously, and then the next campaign goes out with white text on a pale background and eight images and no alt text.

Both arguments are correct and neither one changes behaviour, which is why I want to make a third one.

An email somebody cannot read is an email that does not get opened, does not get clicked and does not get replied to. It gets deleted without being read, or abandoned halfway through. Those are the precise signals mailbox providers use to decide whether you belong in the inbox, so an inaccessible email does not only fail the person who could not read it. It generates negative signals that degrade your sender reputation, which costs you placement with everybody else on your list, including the people who could read you perfectly well.

Accessibility, in other words, is a deliverability subject. Almost nobody frames it that way, and the framing changes what you do about it.

## The basics

## What email accessibility means

Accessibility is not one thing, and it is not a checklist item that gets ticked, which is part of why it stalls. A more useful definition is a question: can a person receive, perceive, understand and act on your email, regardless of how they are reading it, what they are reading it on, and what they are working with at the time?

Four words doing four different jobs there, and each maps onto a different type of accessibility. Perceive is a sensory question. Understand is a cognitive one. Act is partly technical and partly design. And receive, which sits underneath all of them, is deliverability, which I will come back to at the end because it is the part everybody forgets.

So rather than one accessibility, there are four types, and most businesses are only ever thinking about the first one.

## Three answers

## Is it really that important? Three answers, in ascending order of usefulness

The legal answer

In some places, and increasingly. The European Accessibility Act brought obligations into force for a range of consumer-facing digital services, and in the UK the Equality Act creates a duty to make reasonable adjustments that plenty of organisations have never thought to apply to their marketing email. I have written about the European Accessibility Act separately and would rather point you there than repeat it.

The trouble with the legal argument on its own is that it produces minimum compliance, done reluctantly, by somebody who resents it. Which never produces good email.

### The moral answer

The scale is larger than most people assume. An estimated 16.8 million people in the UK had a disability in 2023/24, around a quarter of the population, and roughly one in four adults across the UK, EU and US live with a disability. The World Health Organization puts the number of people worldwide with a vision impairment of some kind at over 2.2 billion.

Worth noticing too that in the UK data, mobility, stamina and mental health conditions are more prevalent than vision or hearing, which quietly undermines the assumption that accessibility means screen readers and nothing else.

Everybody agrees with the moral argument and very little changes, because agreeing costs nothing and rebuilding a template costs a fortnight.

### The commercial and deliverability answer:

Think about what happens mechanically when somebody cannot read your email.

- They delete it without opening, or open and abandon it immediately. Both register as negative engagement signals, and deletion without opening is on every provider's list of things that count against you.
- They do not click, because they could not find or use the link. So you lose the strongest positive signal available to you.
- They stop opening over time. Somebody who has struggled with three of your emails learns to skip the fourth, and that learning happens below the level of any conscious decision about your brand.
- Some of them report you. An email that cannot be read but keeps arriving looks like something unwanted, and the spam button is the fastest way to make it stop.

Individually, those are negative signals and fairly harmless. Clustered across a segment of your list, campaign after campaign, they become negative events, and negative events are what erode a sending reputation. Providers do not assess you one recipient at a time, they form a view from the aggregate, so a group of people who consistently cannot engage with your email drags down placement for everybody you send to.

## The four types

## One: technical accessibility

The code layer, and the only one of the four that is close to binary. Can assistive technology parse this email at all, and does it come out in a sensible order when it does?

### Semantic structure and real headings

Screen reader users navigate by structure rather than reading top to bottom, in the same way a sighted person scans. A properly marked-up heading lets somebody jump between sections. A paragraph that has been made big and bold to look like a heading gives them nothing to navigate by, so they have to sit through the whole email in sequence to find out whether any of it is relevant.

Which means using real heading elements rather than styled text, in the correct order, without skipping levels. Most email templates have no headings at all, which is the equivalent of handing somebody a document with the table of contents removed.

### Layout tables and the presentation role

Email is still built with tables, and a screen reader encountering a table assumes it contains data, so it announces the dimensions and then reads it cell by cell with positional information. On a typical marketing email that produces a stream of announcements about rows and columns before the reader gets to a single word of your copy.

Marking layout tables with role=“presentation” tells assistive technology to ignore the structure and read the content. It costs one attribute per table and it is the single highest-impact technical fix in most templates.

### Alt text that does a job

Alt text is not a description of the image, it is a replacement for the function of the image. The question to ask is what this image is doing, and then write that.

- A product shot. Name the product as somebody would search for it, rather than describing the styling of the photograph.
- An image with text baked into it. The alt text has to carry that text, because otherwise the message simply does not exist for a portion of your audience.
- A button built as an image. Alt text is the button label. Not “button”, but what happens when it is pressed.
- A purely decorative divider or flourish. Empty alt attribute, so it gets skipped silently rather than announced as “image”.
- A logo. The company name, once. Not on every instance in the same email.

Worth knowing that missing alt text is the most widespread failure on the open web too, with WebAIM's 2025 analysis finding more than half of homepages missing alternative text for images. Email is almost certainly worse, because nobody audits email.

### Live text rather than images of text

The habit that causes more accessibility damage than any other, and it is usually a design decision made for brand reasons. Text baked into an image cannot be read by a screen reader, cannot be resized, cannot be selected or translated, does not reflow on a narrow screen, and disappears entirely when images are blocked.

Which is why it is also a deliverability problem, since an image-heavy, text-light email is one of the patterns filters weigh against you, and an email that renders as an empty box with images off produces exactly the non-engagement that damages your reputation.

### Language attributes

A lang attribute on the email tells the screen reader which language to pronounce the content in. Without it, English read by a screen reader set to another language becomes close to unintelligible, and for multilingual programmes this is not a small detail.

### Link text that means something

Screen reader users can pull up a list of every link in a message. If yours all say click here, read more or shop now, that list is useless and they have to go back and read around each one for context.

Which happens to be good copywriting advice regardless, because a link that describes its destination outperforms one that does not for everybody.

### The emoji problem

Screen readers read out the name of every emoji. Three in a subject line becomes a recital before the recipient reaches your actual words, and a decorative emoji used as a bullet point becomes a repeated announcement down the length of the email.

Not a reason never to use one. A reason to use one deliberately, at the end rather than the start where possible, and never as a substitute for a word that carries meaning.

## Two: sensory accessibility

The eye layer. The email is technically parseable, and can a human eye comfortably process it?

### Contrast, and the numbers that matter

The Web Content Accessibility Guidelines set a minimum contrast ratio at level AA of 4.5 to 1 for normal text, and 3 to 1 for large text, where large means at least 18 point, or 14 point if it is bold. Contrast is the most commonly failed criterion on the web by a distance, present on the large majority of top sites.

It is also the easiest thing to test, because contrast is mathematically calculable rather than a matter of opinion. Which brings me to an uncomfortable example.

### My own brand fails this, and yours might too

My coral is #FF4E5F. Against white, it produces a contrast ratio of 3.23 to 1, which passes AA for large text and fails it for normal text. So coral headings are fine, and coral body copy or small links are not, and white text on a coral button is the same 3.23 to 1, which means my call-to-action buttons fail at standard text sizes.

The fix in my case is simple once you know: put my ink colour on the coral button rather than white, because #242223 on #FF4E5F comes out at 4.90 to 1 and passes. My blush pink at #FFBAC0 on white manages 1.61 to 1, which fails everything, so it is a decorative colour and can never carry text.

I mention it because almost every brand palette has this problem somewhere, it is usually in the button or the link colour, and nobody finds out because nobody checks. Ten minutes with a contrast checker and your hex codes will tell you more than any accessibility article will.

### Size, spacing and tap targets

- Body text at 16 pixels minimum. Fourteen is an absolute floor and it is uncomfortable on a phone in any light that is not perfect.
- Generous line height. Around 1.5 for body copy. Tight leading is the single most common reason a well-written email is hard to read.
- Line length kept sensible. Very wide columns of text are difficult for everybody and particularly for people with dyslexia or tracking difficulties.
- Tap targets of at least 44 by 44 pixels. A text link in a paragraph is a difficult target for anybody with a tremor, and an impossible one on a moving train.
- Avoid pure black on pure white for long passages. Maximum contrast is not always maximum comfort, and a very slightly softened dark on off-white reads more easily over several paragraphs.

### Colour must never be the only signal

Around one in twelve men has some form of colour vision deficiency, so a red warning box that is only identifiable as a warning because it is red carries no information for a meaningful slice of your audience. Anything colour is telling somebody needs to be repeated in words, an icon or a shape.

### Motion and animation

Animated GIFs that loop indefinitely, flashing content and fast transitions cause difficulty for people with vestibular disorders and, in extreme cases, present a seizure risk. Keep animation short, avoid anything that flashes more than three times a second, and make sure the first frame carries the message so nothing is lost when animation is blocked.

### Dark mode

Dark mode is a sensory accessibility feature that a large share of people now use by default, and email clients handle it in three incompatible ways: leaving your email alone, inverting some colours, or forcibly inverting everything.

The common failures are a black logo disappearing into a dark background, a coloured button whose text inverts to become unreadable, and a carefully chosen brand colour becoming something else entirely. Transparent PNGs with a light outline, avoiding pure white and pure black in favour of near-neutrals, and testing in a client that force-inverts will catch most of it.

## Three: cognitive accessibility

The brain layer, and the one almost nobody in email thinks about at all. The email is readable and can it be understood without effort?

It affects people with dyslexia, ADHD, autism, anxiety, brain fog, long covid, the effects of medication and simple exhaustion. It also affects every single person reading you while doing two other things, which is most of your list most of the time.

- Plain language. Short sentences where short works, familiar words over impressive ones, and no idioms or metaphors carrying essential meaning.
- One clear action. An email with six competing calls to action creates a decision, and a decision creates cognitive load. Most people resolve it by leaving.
- Predictable structure. Emails that arrive in a recognisable shape are easier to process every time, which is one of the quiet arguments for consistency over novelty.
- Front-load the point. What this is and what you want, in the first two lines, before any context. Somebody who runs out of attention halfway should still have got the message.
- Chunk it. Short paragraphs, clear headings and white space, so the email can be scanned rather than only read.
- No manufactured time pressure. Countdown timers and artificial urgency are a genuine accessibility problem for anybody with an anxiety condition or who needs longer to process a decision, on top of being a trust problem.
- Tell people what happens next. Uncertainty is cognitive load. Saying what the button does before somebody presses it removes it.

## Four: situational accessibility

The type that reframes the whole subject, and the reason the minority objection does not hold.

Access needs are not only permanent. Microsoft's design work popularised a useful way of thinking about this: a permanent condition, a temporary condition and a situational constraint often produce the identical barrier. Somebody with one arm, somebody with a broken wrist, and somebody holding a baby all have one hand available, and your email is equally difficult for all three.

Which means the situational version of every category above:

- Bright sunlight. Turns a low-contrast email into a blank screen for somebody with perfect vision.
- A cracked or scratched screen. Small text and tight tap targets become unusable.
- One hand. Holding a coffee, a child, a handrail. Small links become unhittable.
- Bad signal or a data cap. Images do not load, so an image-based email is a blank rectangle.
- Images blocked by default. Still the default behaviour in several corporate environments, which means your carefully designed email arrives as alt text and nothing else.
- An old or cheap device. Slower rendering, smaller screen, older client, less support for anything clever.
- Exhaustion, distraction, and eleven at night. Cognitive capacity is not fixed. It varies by hour, and your email does not get to choose when it is opened.
- A noisy train, an open-plan office, a meeting. Content that relies on sound, or that requires sustained attention, loses.
- Temporary conditions. A migraine, an eye infection, dilated pupils after an optician appointment, concussion, the first three months of a new baby. Everybody passes through these.

## The fixes

## What to do, in order of impact

1. Put real text back in. Live text rather than text baked into images, everywhere it is possible. One change fixes screen reader access, resizing, translation, images-off rendering and your image-to-text ratio at the same time.
2. Add role="presentation" to your layout tables. One attribute per table, and it stops assistive technology reading your template structure aloud before it reaches your copy.
3. Write proper alt text on every meaningful image, and empty alt on decorative ones. Replacement for function rather than description of appearance.
4. Run your palette through a contrast checker. Ten minutes, your hex codes, and the numbers are objective. Fix the button and link colours first, because those are where the failures usually are.
5. Set body text to 16 pixels with line height around 1.5. Costs nothing, helps everybody, and is the change people notice most.
6. Add semantic headings in a sensible order. So somebody navigating by structure can find what matters instead of listening to all of it.
7. Reduce to one clear action. Which improves conversion as well as accessibility, and is a good example of the two pulling in the same direction more often than people assume.
8. Rewrite your link text. Descriptive rather than generic, which helps screen reader users and improves clicks for everybody.
9. Add a lang attribute and check your unsubscribe. Small, fast, and the unsubscribe one protects your complaint rate.
10. Test in dark mode and with images off. The two conditions most likely to break a template that looks perfect in preview.

### How to test it without buying anything

- Turn images off and read it. The fastest and most brutal test available. If the email makes no sense, a real portion of your audience is receiving that version.
- Use a screen reader for five minutes. VoiceOver is built into every Mac and iPhone, and NVDA is free on Windows. Listening to your own email once will change how you build them permanently.
- Zoom to 200 percent. Does anything break, overlap or get cut off?
- Read it outside in bright light. Your contrast problems will announce themselves immediately.
- Open it on the oldest phone in the office. Not the newest one on the design team's desk.
- Read it aloud. Anything you stumble over is cognitive load, and your reader will stumble too.

## The one that beats all of them

## The most inaccessible email is the one that never arrived

Everything above assumes the email reached somebody. Alt text, contrast, semantic structure and plain language are all improvements to a message that made it to an inbox.

An email sitting in a spam folder is inaccessible to one hundred percent of its audience, regardless of how beautifully it was built. Around fifteen percent of a typical send does not reach the inbox at all, which makes deliverability the largest single accessibility failure in most email programmes and nobody counts it as one.

So the hierarchy runs the other way round from how people usually approach it. Deliverability sits at the top, because it determines whether anybody can access the email at all. Technical accessibility comes next, because it determines whether the message can be parsed. Then sensory and cognitive, which determine whether it can be processed. And situational sits across all of them, because it multiplies the number of people affected by every failure above it.

The two disciplines also feed each other, which is the part I find most useful. Live text improves your image-to-text ratio. A findable unsubscribe reduces complaints. Plain language and one clear action increase clicks. Every one of those is an accessibility fix that produces a positive engagement signal, and positive signals are what keep you landing in the inbox for everybody.

## The conclusion

Accessible email is not a separate project, a compliance exercise or a favour you are doing for a small group of people. It is the difference between an email built for perfect conditions and an email built for the conditions people are in.

Somebody on your list is reading you on a cracked phone, in the sun, with one hand, with images off, at the end of a long day. Most of your list is in some version of that state most of the time, and the email that works for them is the same email that works for a screen reader user.

Do it because it is right, do it because in some markets you are required to, and do it because the engagement signals it produces are the ones your sender reputation is built from. Three arguments, all true, and you only need to act on one of them.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.
