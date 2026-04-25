---
type: Web
authors: '[[Lauren Meyer]]'
url: 'https://send-it-right.com/blog/email-deliverability-red-flags'
published: 2024-11-13T00:00:00.000Z
created: 2026-04-24T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
  - content-marketing
---


We've all been there: you send out your latest campaign. You’re feelin’ confident. Excited. But then, you see a red flag start poppin’ up. Low open rates, high bounce rates or spam complaints – it's enough to make you wanna go back to bed…if only you could sleep after seeing what you just saw. Ugh.

Ok, but wait…don’t actually go back to bed.

We need to talk about how to identify these common deliverability issues (among others) before they escalate, and how to bring those red flags back down to the ground with a quickness.

## Understanding Email Performance Red Flags

Deliverability issues often start as subtle whispers in your performance metrics before escalating into full-blown tantrums. By tuning into these early warning signs (ahem, ***red flags***), it’ll give you time to troubleshoot and mitigate the issue before any lasting damage is done.

Here are the most common email performance red flags and how to tackle ‘em.

### 🚩 Low Delivery & High Bounce Rates

These are two halves of the same coin. If delivery rates are low, bounces are high. And if your emails aren’t getting delivered, it impacts every other metric we’re gonna talk about today.

Bounces come in two flavors: hard bounces (permanent failures like non-existent email addresses) and soft bounces (reputation-based blocks or temporary glitches such as a full inbox). The type of bounce you’re seeing can provide insight into your list quality and reputation.

If you notice a sudden rise in bounce rates — or a drop in delivery rates — it's essential to investigate and take action right away.

#### Common causes of low delivery / high bounce rates:

1. **Poor List Hygiene**: Bounces often come from sending to outdated or invalid email addresses, or failing to suppress spam complainers and unsubscribes. The more of these you send, the more harmful it becomes to sender reputation over time.
2. **Lack of Email Authentication**: This is like showing up to a club without your ID, particularly in 2024, when it’s required by major providers like Google and Yahoo—it’s very unlikely they’ll take you for a legitimate sender. If you’re not familiar with SPF, DKIM, and DMARC, take a quick look back at our past lesson on email authentication.
3. **Poor Sender Reputation**: Lots of spam complaints, particularly when paired with hard bounces, can collectively damage how mailbox providers view you. Take pause to consider what you’re doing wrong if bounces mention high spam complaints or being blocklisted by providers such as Proofpoint or Spamhaus. And if you're adding new subscribers, especially in high volumes, consider a warm-up period to avoid overwhelming mailbox providers with unexpected traffic.

While hard bounces are certainly not a good thing, it’s not the end of the world if they’re high from time to time…particularly if you’re a generally good sender. Any change in your typical patterns should be investigated, but generally speaking, aim to keep hard bounce rates below 2-3% on a regular basis, with minimal peaks above 5%. If soft bounces are exceeding 1%, contact your email service provider (ESP) to rule out more serious reputation issues.

### 🚩 Declining Open Rates

Tracking is harder and less accurate than ever, thanks to initiatives like [Apple’s Mail Privacy Protection](https://www.socketlabs.com/blog/email-open-rates-are-mostly-dead/?utm_source=senditright&utm_medium=blog&utm_campaign=red_flags) (MPP), but opens continue to be a useful way to gauge inbox placement since automated / proxy opens don’t happen when mail is delivered to the spam folder.

If you see open rates trending downwards—or if they fall off a cliff—you’ll have to figure out if this is a deliverability issue, or simply a problem with segmentation and content.

A great way to figure this out is by comparing your open rates across mailbox providers instead of just at the aggregate level. For example, if you notice your open rates are significantly lower at one destination (such as Microsoft) while they’re chugging right along with Gmail, Yahoo, and every other destination you send to, you likely have a spam folder issue with Microsoft, not a problem with snoozy subject lines.

Here’s an example of what that might look like…

![An example of aggregate open rates trending downward, but open rates at the destination reveal a very clear issue with inbox placement at Microsoft.](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/d9f2a660-ad1d-4de1-9dd6-29c3bd782f5a/Low+opens+at+MSFT+%283%29.png?format=2500w)

An example of aggregate open rates trending downward, but open rates at the destination reveal a very clear issue with inbox placement at Microsoft.

Ultimately, open rates are never gonna be accurate enough to truly know if a human opened your email or a bot. But if you track your open rates directionally over time, identifying slides in inbox placement becomes much easier.

### 🚩 Rising Spam Complaint Rates

Spam complaints are like kryptonite to email deliverability because they’re a signal—directly from recipients—telling mailbox providers that they don’t want to receive mail from you anymore.

If enough recipients mark your email as spam, it tells mailbox providers you’re sending unwanted content, have an unclear (or missing) opt-in process, or a poor user experience, all of which can rapidly impact your deliverability.

![An example of a fluctuation in spam complaints turning into an increasingly problematic trend.](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/798aff1a-194e-4d69-868a-c417d5b93c54/Spam+complaints%21.jpg?format=2500w)

An example of a fluctuation in spam complaints turning into an increasingly problematic trend.

Aim to keep spam complaint rates below 0.03% at all times. I know that sounds tiny, but it’s what works if you wanna maintain *consistent* inbox placement.

#### Ways to Reduce Spam Complaints:

- **Get Permission!** I cannot stress how important this is. Sending to people who aren’t expecting to hear from you is the most common cause for spam complaints, and it can also damage your brand’s image on the very first introduction. So, find any way (literally any one!) to get them hooked before you start showing up in their inbox.
- **Set Clear Expectations:** From the opt-in stage, clearly communicate what subscribers can expect from you in terms of frequency and content type, and stick to what you promised! If you plan to change frequency or the type(s) of content you send, consider giving them a heads up first.
- **Provide Easy Unsubscribe Options:** I know it sounds counter-intuitive…we’re trying to grow our lists, right? Well, making it easy to unsubscribe can reduce spam complaints by giving dissatisfied recipients a straightforward way to opt out. In fact, Clea Moore, Principal Product Manager for [Yahoo told me](https://www.socketlabs.com/blog/webinar-highlights-google-yahoo-talk-email-marketing-in-2024/?utm_source=senditright&utm_medium=blog&utm_campaign=red_flags) senders are seeing approximately 30% reductions in spam complaint rates on average, simply by making the unsubscribe process easier.

**Keep in mind: people cannot mark emails as spam if they’re already sitting in their spam folders.**

So, if you’re consistently sitting at a 0.00% spam complaint rate, it’s likely more of a bad sign than a good one. Scroll back up and try out my recommendation for reviewing open rates by mailbox provider for clues into whether it’s time to celebrate or investigate.

### 🚩 Elevated Unsubscribe Rates

An uptick in unsubscribes is your audience's way of saying, "This isn't working for me." It could be due to irrelevant content, overly ambitious (ahem, annoying) sending frequencies, or unmet expectations.

In a previous lesson, we talked about [why unsubscribes ***aren’t*** bad for deliverability](https://send-it-right.com/blog/why-unsubscribes-arent-bad-for-deliverability). I’ll take a thousand unsubscribes over a handful of spam complaints any day. That said, it’s important to keep them as low as possible (ideally below 1%) because if an increased number of recipients are asking to get off the ride by unsubbing, others may be *shouting* to get off by marking your emails as spam.

#### Strategies for Curbing Your Enthusiasm…errr, Unsubscribes:

- **Keep Their Enthusiasm!** The entire goal of sending email is to connect with our email audience in a way that is unique and genuinely helpful to them in some way. So pay them back for letting you into their digital homes (...storage units??) by regularly evaluating how (and why) they joined your list in the first place and whether your emails are delivering the information, promotions, or resources that are tailored to their needs.
- **Give Them Other Options:** A preference center can help reduce unsubscribes by letting users customize how often and what type of content they receive. You can also offer recipients options to reduce frequency or “snooze” emails from your brand for a set time period (e.g. 2 months) within the body of your email.
- **Monitor and Adjust Frequency:** Particularly during high-volume periods when everybody’s vying for recipient attention, scaling back email frequency can prevent subscriber fatigue, especially among less active segments. Don’t get me wrong — keep on sending to your active subscribers….in fact, consider testing if they want to hear from you *more!* But don’t treat active and inactive segments the same. Dig into your engagement data to suss out who should receive what, and how often.

### 🚩 Lowered Click-Through Rates

When it comes to catching and dealing with email performance red flags, the click-through rate (CTR) allows you to look at the engagement of a wider array of relevant factors including your subject line, pre-header (aka preview) text, friendly From, and so on…which aligns more closely with the way mailbox providers track recipient engagement than, say, just monitoring click rates alone.

While open rates indicate initial interest, CTRs reflect engagement quality. A low CTR suggests that recipients are not finding your content compelling or that your call-to-action (CTA) is not resonating.

#### Ways to Raise CTRs:

- **Troubleshoot Deliverability Issues:** When delivery rates are high but everything downstream is low (i.e. your opens, clicks, web traffic, and/or conversions), it’s likely mail’s being accepted by mailbox providers’ servers, but it’s not landing in the inbox. In this scenario, your low CTR is driven by the fact that recipients aren’t seeing your mail in a place they can readily engage with it.
- **Adjust Your CTA:** Make your call-to-actions (CTAs) clear, compelling, and aligned with the goal of your email. I loooove packing my emails as full of “value” as possible, but it can be overwhelming to recipients when you recommend multiple, competing actions. Consider what you *really* want them to do with that email and if it means you should stick to one primary CTA.
- **Test, Test, and Test Some More:** Effective messaging *and* design are both pivotal in making content scannable and CTAs stand out. Test different friendly From addresses, subject line styles, copy length and offer types, layouts, colors, and button placements.

## 🚩 What To Do When a Red Flag is Raised

There are 100’s of factors affecting what happens between when you push ‘send’ and when an email is ultimately delivered (or rejected) a few milliseconds later, so deliverability red flags can pop up, even when you’re doing your best to send it right.

Swift action can make all the difference between a minor blip and a major issue, so here are a few steps I recommend for when a flag starts wavin’ in your general direction:

**1\. Pinpoint the Problem**.

Start by reviewing your recent campaigns and identifying any patterns in the performance metrics. Be sure to look back at least a few days or weeks prior to when you noticed the issue to see if you can identify when it truly started. Review your metrics at the mailbox provider level (e.g. Gmail vs Microsoft vs exampledomain.com) if possible.

Are certain segments driving the spike in complaints or unsubscribes? Is a recent subject line or campaign underperforming, or do you potentially have an inbox placement issue at play? Spotting these trends can help you isolate the root cause.

**2\. Pause and Evaluate (If Necessary).**

If the issue seems widespread, consider pausing sends while you investigate to avoid worsening the problem. This gives you breathing room to troubleshoot and take the necessary steps on your side without risking more potential damage to your sender reputation.

You can start sending again as soon as you’ve identified and dealt with the problem.

**3\. Audit and Re-engage Segments.**

Use this opportunity to review your list collection sources, particularly those that are causing spam complaints, to help reduce the likelihood of more new signups marking your emails as spam.

Also review your audience segments to identify issues with list hygiene or low engagement, which might be contributing factors. Consider pulling back on frequency of sends to less engaged audiences while you iron out your issue. You can always run a re-engagement campaign once performance has returned to normal.

**4\. Revise Your Content Strategy.**

If you're experiencing more unsubscribes, complaints, or disengagement than usual, reassess your content and messaging strategy.

- Are your lead magnets bringing in the right kinds of signups…folks who are interested in engaging with your brand via email?
- Are you effectively setting expectations at the point of signup so people know what to expect?
- Are you delivering on the promises you made when subscribers opted in?
- Are you following your engagement data to ensure your content is still aligned with their interests and expectations?

Make a data-based hypothesis about what you *think* is contributing to your change in performance and take steps towards improving in that area…even if it’s just the teeeeeniest, tiniest baby step. Progress is progress.

**5\. Reach Out for Help.**

If your email red flags persist or you’re unsure of the best next steps, connect with your ESP or a deliverability nerd ([like me!](https://send-it-right.com/lets-talk-email)) who enjoys noodlin’ through email data. We can offer insights, help you run diagnostics, or suggest tailored solutions to get your program back on track.

Also consider dropping a question into #emailgeeks Slack, where you’re likely to have it answered by experts — and sometimes, mailbox provider themselves! Here’s a list of places you can go to [connect with other email folks](https://send-it-right.com/connect-with-email-nerds) who might be able to help.

## Wrapping it up.

If we want recipients to keep engaging with the emails we send, they need to be able to trust us to send relevant and genuinely helpful content, and to be respectful of their inbox.

By taking a proactive approach to monitoring, we can not only enhance our email performance, but also create a stronger relationship with our email subscribers. After all, they’re the whole reason we’re doin’ this, right?

Until next time, happy sending! 💌

## Want more content like this?

*Join 860+ other email nerds in subscribing to Send It Right, my weekly-ish newsletter for marketers and email practitioners* who wanna reach the inboxes (and hearts) of email recipients. [Hubspot included it in their 23 Favorite Free Marketing Newsletters](https://blog.hubspot.com/marketing/best-marketing-newsletters) article published in October 2024, so you know it’s got somethin’ goin’ for it.

[Get me on the list](https://send-it-right.com/newsletter)
