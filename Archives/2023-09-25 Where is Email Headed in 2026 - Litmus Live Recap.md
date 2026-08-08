---
type: "Web"
authors: "[[Kimberly Huang]]"
url: "https://www.litmus.com/blog/where-is-email-marketing-headed-in-2026-takeaways-from-litmus-live?ck_subscriber_id=3412528627&utm_source=convertkit&utm_medium=email&utm_campaign=%F0%9F%92%BB%20open%20tabs%20%7C%20the%20ROI%20number%20to%20bring%20to%20your%20board%20-%2022752420&sh_kit=ebb8f2fb51f8b6f5b192f8b07d9aae25086a45840059610b97f734dbb8655eb6"
published: 2023-09-25
created: 2026-08-03
tags:
  - "digital-campaigning"
  - "trendy-AI"
  - "content-marketing"
---


### Key takeaways ✨

- **Deliverability isn’t getting easier** —but good senders who follow best practices have a clear path forward.
- **AI is reshaping the inbox experience**, from relevancy sorting to AI-generated summaries, and marketers need to adapt their content strategies accordingly.
- **Email metrics are getting fuzzier** as opens become less reliable, making it more important than ever to look beyond surface-level engagement signals.
- **AI-generated email code looks polished at first glance** but can break across real inboxes, underscoring the need for rigorous testing.
- **Implementing DMARC is one of the most important things** senders can do to stay identifiable as a good, legitimate sender.

Litmus Live 2026 was packed with expert insights across two action-filled days. One of the most popular sessions titled “Where Is Email Marketing Headed in 2026?” was a 30-minute deep dive hosted by Validity’s own Guy Hanson and Danielle Gallant. Valimail’s Al Iverson also joined the fun!

If you didn’t catch it live, here’s a quick recap—plus answers to the questions from the live chat that the trio didn’t have time for during the session. You can also watch the session recording on [Litmus’ website](https://www.litmus.com/conference#agenda) and [YouTube](https://youtu.be/mugf2HHGotM?si=yHiVG9mtswJJHTai).

## Deliverability is not getting easier

The panel wasted no time getting into the hard truths. [Email deliverability](https://www.litmus.com/blog/why-email-deliverability-matters) is getting more complex. Mailbox providers keep refining their filters—and legitimate senders are feeling the impact.

The good news? Following responsible sending practices are still the most reliable path to inbox placement. As Al Iverson put it: “Good marketers are never the target of mailbox provider spam filters. Good marketers get caught up in a mailbox provider’s best efforts to stop the really malicious stuff. Implementing [DMARC](https://www.litmus.com/blog/reading-first-dmarc-reports) with an actual level of protection is what keeps you identifiable as a good sender.”

The practical takeaway: don’t just set and forget DMARC. Moving to a p=quarantine or p=reject policy isn’t just a compliance checkbox—it’s what signals to mailbox providers that you’re a trustworthy sender.

## Relevancy sorting is changing inbox behavior

One of the most significant trends the panel explored is how mailbox providers use AI to sort and prioritize messages by [relevance](https://www.validity.com/blog/gmail-updates-marketers-need-to-know-purchase-tracking-and-most-relevant-promotions/). It’s no longer enough to land in the inbox—your email needs to earn visibility at the top of the inbox.

This means engagement signals matter more than ever. Senders who consistently deliver value to their subscribers are rewarded; those who send to unengaged or poorly segmented lists will see their visibility erode over time. This means that regular [list hygiene](https://www.validity.com/blog/why-you-should-not-buy-email-lists/), strategic [segmentation](https://www.litmus.com/blog/combining-segmentation-and-personalization), and [permission-based sending](https://www.validity.com/resource-center/easy-steps-to-power-up-your-email-preference-center/) aren’t just best practices—they’re marketing survival strategies.

## AI summaries are forcing a content shift

[AI-generated summaries](https://www.validity.com/blog/gmail-annotations-in-2025-what-they-are-how-they-work-and-what-comes-next/) are already changing how subscribers interact with email. Instead of reading your full message, many recipients may only ever see a machine-generated synopsis. This has significant implications for how marketers write their emails. their emails.

The panel highlighted the need for senders to think about the “summary layer” of their content: What does your email look like when distilled into two or three sentences by AI? If your value proposition, offer, or call to action isn’t immediately clear, you risk being skipped entirely.

This is a strong argument for leading with clarity in your emails. Front-load your subject lines and preview text and include the most important information first. Write for humans but structure for algorithms.

## Metrics are getting fuzzier

Opens have been unreliable ever since [Apple’s Mail Privacy Protection](https://www.validity.com/blog/how-to-grapple-with-apple/) (MPP) arrived in 2021, and the problem has only compounded since. Clicks are more and more affected by bot activity and security scanners. The panel underscored the need for marketers to look beyond these top-level metrics and build a richer picture of engagement.

More [meaningful signals](https://www.litmus.com/blog/email-metrics-that-matter-what-to-measure) include downstream conversions, site visits originating from email, time spent on site, and behavioral actions like replies, adding items to a cart, or completing a form. You can also look at your offline performance like foot traffic in your physical location that can be attributed to your email program. These metrics can be trickier to collect, but they tell a far more accurate story about whether your email program is actually driving results.

## AI-generated code looks good…until it doesn’t

The session touched on a cautionary note for marketers and developers: AI tools make it easier than ever to generate email code, but that code doesn’t always hold up across real inboxes. A template that looks flawless in a preview can fall apart in Outlook, Gmail app, or dark mode environments.

The message was clear: AI is a useful starting point, not a finish line. [Email testing](https://www.litmus.com/blog/smarter-email-client-testing) across mailbox providers and environments remains non-negotiable.

## Questions from the live chat—answered

The session generated a lot of great questions in the Litmus Live chat that the panelists unfortunately didn’t have time for. Lucky for us, they met up offline to tackle a few of the leftovers.

### 1\. For your prediction that DMARC requirements will be further tightened, do you think p=quarantine will be enough for compliance or will you need a p=reject record?

**Guy Hanson**: Mailbox providers want to tighten up on all the senders who still rely on p=none because this policy implies the sender isn’t taking any action based on their DMARC reporting data. In the context of our prediction, p=quarantine will be fine, although we recommend moving to p=reject when you’re confident all your legitimate email traffic is accounted for.

**Al Iverson**: I personally think “reject” is better than “quarantine” when it comes to DMARC protection—block that bad stuff at the edge! Check out [Valimail’s new DMARC report](https://www.valimail.com/dmarc-report-2026\)) for more!

**Danielle Gallant**: In addition to a p=reject requirement for DMARC, I expect there will soon be requirements for strict DKIM and SPF alignment too. Make sure everything is aligned to save yourself future frustration.

### 2\. Are text-heavy emails now better than image-heavy for AI inboxes? Does that conflict with keeping CTAs above the fold?

**Guy Hanson**: Balanced is best. Make sure the text you want AI summaries to surface is accessible—use headings, alt text, meaningful CTAs, and semantic HTML. These are all accessibility best practices anyway, so the benefits extend well beyond AI.

**Al Iverson**: Just be careful not to blow up your email code for AI summaries. Balanced text and imagery were already best practice before AI inboxes arrived—this just reinforces the need for them.

### 3\. When AI email summaries are generated, does this involve a bot open?

**Guy Hanson**: Yes, we’ve seen [research](https://folderly.com/blog/gmail-gemini-ai-email-deliverability-2026) that backs this up.

**Danielle Gallant**: Thankfully, there are ways to identify bot clicks through time-to-click analysis, honeypot links, and ESP support. Our fantastic colleague Megan Farquharson [recently wrote about this](https://www.validity.com/blog/are-these-clicks-for-real-the-rise-of-bot-clicks-and-what-marketers-can-do-about-it/)!

### 4\. Would clicking a “mailto” link serve the same purpose as clicking reply in terms of metrics? Or would mailbox providers place more value in an actual reply click?

**Guy Hanson**: A mailto link is a great way to encourage two-way dialogue, but it won’t send the same strong intent signal to mailbox providers that an organic reply does. Be intentional about designing emails that invite real replies—encourage subscribers to respond and make it easy for them to do so.

**Al Iverson**: Just to second what Guy is saying, mailbox providers are firm in their guidance that replies help, so I would definitely encourage them.

### 5\. Regarding the metric of engagement offline or outside of the email ecosystem, how does this affect the MBP engagement metrics that will determine reputation?

**Guy Hanson**: Mailbox providers, especially Google, already have cross-channel visibility. A subscriber who receives your email in Gmail, searches your brand on Google, browses your site in Chrome, and watches a product review on YouTube before buying? Google can connect all of those dots.

### 6\. How could some of your points apply to B2B email marketing?

**Danielle Gallant**: Guy and I recently recorded a [live episode of our podcast](https://senderscore.org/podcasts/email-after-hours/the-abcs-of-b2b-email-marketing-live-at-marketingprofs-b2b-forum/) at the MarketingProfs B2B Forum diving deeper into this topic. We cover how B2B email success hinges on strong consent practices, ongoing list maintenance, reputation management, and realistic performance measurement—all through the lens of the unique challenges B2B senders face, from higher churn and stricter filtering to longer buying cycles. You’ll see a few similarities with what we discussed in the Litmus Live session and the specific B2B nuances. Definitely check it out!

## Sending with confidence in 2026

While the challenges persist, so does our community of email marketing experts. You can watch the full “Where Is Email Marketing Headed in 2026?” session on [Litmus’ website](https://www.litmus.com/conference#agenda) and [YouTube](https://youtu.be/mugf2HHGotM?si=yHiVG9mtswJJHTai).

Want to stay ahead of email deliverability and engagement trends? Check out Validity’s [2026 Email Deliverability Benchmark report](https://www.validity.com/resource-center/2026-email-deliverability-benchmark-report/) to see how your performance stacks up.

Matt is a Content Marketer at Validity