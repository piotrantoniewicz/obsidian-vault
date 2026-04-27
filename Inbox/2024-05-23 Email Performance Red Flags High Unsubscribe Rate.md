---
type: "Web"
authors: "[[Lauren Meyer]]"
url: "https://www.socketlabs.com/blog/email-performance-red-flags-high-unsubscribe-rate/?utm_campaign=deliverability_rate&utm_medium=blog&utm_source=senditright"
published: 2024-05-23
created: 2026-04-27
tags:
---


<iframe frameborder="0" title="Submit HubSpot product feedback" src="https://app.hubspot.com/feedback-web-fetcher"></iframe>

[![SocketLabs Logo](https://www.socketlabs.com/wp-content/uploads/2024/04/logo-dark.svg)](https://www.socketlabs.com/)

![](https://www.socketlabs.com/wp-content/uploads/2024/05/Unsubscribes.png)

Welcome back to our series, Email Performance Red Flags!

Last time, we asked Marcus Biel, Will Boyd, and Alison Gootee to share their perspectives on one of the most important email performance metrics to watch: [spam complaints](https://www.socketlabs.com/blog/email-performance-red-flags-spam-complaints/).

Now, we know spam complaints are a visceral reaction from people who don’t want to receive email from you. What’s a much less damaging but equally clear indicator your email isn’t impressing people? High unsubscribe rates.

## Red Flag: High Unsubscribe Rates

Ah, unsubscribes. A bittersweet phenomenon.

The upside? They aren’t going to tank your [sender reputation](https://www.socketlabs.com/blog/teach-me-email-what-is-sender-reputation/). In fact, Clea Moore, Principal Product Manager for [Yahoo recently told us](https://www.socketlabs.com/blog/webinar-highlights-google-yahoo-talk-email-marketing-in-2024/) senders are seeing approximately 30% reductions in spam complaint rates on average simply by making the unsubscribe process easier.

But seeing an elevated number of your email recipients opting out should still be viewed as a serious red flag waving in the wind because it’s a form of negative engagement with your email.

One person’s unsubscribe today could be another’s spam complaint tomorrow.

So, we’ve recruited a new set of email smarties to help us walk you through what could be causing a high unsubscribe rate, how you investigate it, and what to do with your findings to lower that pesky red flag back down to the ground where it belongs.

### Today’s Expert Panelists

First, let’s welcome our unsubscribe experts: [Autumn Tyr-Salvia](https://www.linkedin.com/in/autumn-tyr-salvia-3267815/), [Desislava Zhivkova,](https://www.linkedin.com/in/desislava-zhivkova/) and [Skyler Holobach.](https://www.linkedin.com/in/skyler-holobach/)

Autumn Tyr-Salvia’s been in email for almost 15 years, spanning roles in anti-abuse, compliance, and deliverability at places like Cloudmark, Marketo, Message Systems, and Agari. Today she’s a senior deliverability strategist at one of the largest and most respected email names in biz: [Klaviyo](https://www.klaviyo.com/).

Desislava Zhivkova got her start in email as a support agent for Mailjet before diving deeper into anti-abuse as a senior compliance and deliverability analyst. Desi is now the deliverability team lead for [Omnisend](https://www.omnisend.com/), helping their global customers maximize their email performance.

Skyler Holobach is SocketLabs’ vice president of product design and experience…and boy, is it [an experience](https://www.socketlabs.com/hub/spotlight-email-reporting/). Before embracing her current, product-focused role, she racked up more than 10 years of email experience, including pioneering an email reputation position at Pardot and spending several years in privacy and compliance at Salesforce.

Alright, enough with the introductions. Let’s get on with today’s red flag: unsubscribes!

### What is an Unsubscribe Rate?

Google would define the unsubscribe rate as the percentage of email subscribers who opt out of receiving emails from a sender. It’s calculated by dividing the number of unsubscribed users by the number of emails delivered. Then, multiplying that number by 100 to get a percentage.

We prefer Desi’s description, though:

*“I like to think of the unsubscribe rate as constructive feedback from a manager.* *Just as constructive feedback helps employees improve and stay motivated, analyzing unsubscribe rates can guide email senders to refine their email strategy. This ensures it meets the needs and interests of their audience, thus reducing churn and fostering subscriber loyalty.”*

Your unsubscribe rate is a good barometer for recipient sentiment and can help you get ahead of more damaging problems!

Because after all, it’s much better to have someone unsubscribe than flag your email as spam with their mailbox provider (MBP). One signal is disappointing; the other is incredibly damaging to your deliverability.

### What causes a high unsubscribe rate?

Lots of things! First and foremost, the cardinal sin of email:

***Sending to a purchased list***

*“When I worked in compliance, high unsub rates were one of my key indicators that a customer was doing something wrong. I had plenty of cases in which I’d be doing an investigation and I could pinpoint what day they started sending to a purchased list, because you’d suddenly see a MASSIVE uptick in unsubscribes,”* recalled Skyler.

In my head, it goes something like this…

![](https://www.socketlabs.com/wp-content/uploads/2024/05/Unsub-1-2048x1244.jpg)

However, sometimes what went “wrong” was really just an accident or mistake.

***Technical issues or mistakes***

*“The worst unsubscribe spikes I have seen have been due to technical errors, such as a misconfigured send that resulted in the same subscribers receiving dozens of copies of the same message,”* said Autumn. DOZENS?! Woof.

She went on to say, *“Occasional minor mistakes such as ‘Subject line (subject line) (proofread this!!)’ don’t cause this, but malfunctions resulting in a lot of mail do make subscribers think the only way to fix their flooded mailbox is to unsubscribe. That’s particularly upsetting for senders, because even though those people responded to an error, you can’t reach out to ask them to resubscribe because violating their unsubscribe status can have serious repercussions.”*

The experiences Autumn shared are a great reminder of why it’s important to be on the lookout for red flags like this. If a technical issue goes unchecked, the damage could be painful and long-lasting.

*“Another* *customer I worked with had a custom-built technical integration that was built incorrectly in such a way that it overwrote the unsubscribe status on a daily basis. People would unsubscribe on Monday, then their integration would update them that night back to subscribed and they’d get another email on Tuesday. A number of people tried to unsubscribe multiple times. Thankfully we identified it before this had gone on too long, and were able to correctly re-unsubscribe all the people who had been mistakenly resubscribed over and over, but the sender could have landed themselves in serious trouble if we hadn’t collectively been paying attention.”*

Crisis averted, mostly. Way to go, Autumn!

***Lack of permission and expectation-setting***

The way your list has been built plays a major role in how recipients will respond when your mail arrives. You should always be getting their consent and setting expectations about what they’ll receive from you before giving you their address.

*“There’s nothing I love like a shipping confirmation. There’s also nothing I dislike quite like getting bombarded with emails MULTIPLE. TIMES. A. DAY. There’s also nothing quite as awful as unchecking the box that says, ‘Yes I want to opt in to emails from <so and so>,’ but still getting emails,”* stressed Skyler.

So, be clear about how you’ll communicate with people right at the point of address collection. And stick to what you promised! If they think they’re signing up for a newsletter and you immediately start sending aggressive sales email, you might get a fast unsub…or worse!

Piggybacking on that concept, sending a confirmation email in which the recipient needs to further indicate they want your mail is another safe bet. If they’ve double opted-in (also known as confirmed opt-in), you know the address is valid and they truly want your messages. That’s a high-quality address for your list! Next, you can send them a welcome series to reinforce what they can expect and let the email fun begin.

***Email content***

I’m sure you’re not surprised to see content issues on the list. A few of the most common reasons include:

- a lack of personalization
- a misalignment of what you promised and what you actually provide
- using phrases or tactics people consider “spammy” like misleading subject lines

Also remember, email marketing does not happen within a vacuum. As often as you can, consider the other marketing channels your subscribers may be seeing and the activities they may be engaging in that affect the types of content you should send.

*“I remember one case I had with a client who is an online fashion retailer with pretty good overall statistics. I was surprised to see that one of their campaigns had a sudden spike in the unsubscribe rate. Upon diving deeper into the data, it became apparent that in their eagerness to promote their winter collection they’ve sent a campaign to their entire contact list including everyone who recently ordered winter items from their store,”* shared Desi.

*“Once they focused more on user engagement and started excluding segments with contacts who recently purchased items that are being promoted in the current campaign, they managed to decrease their unsub rates significantly.”*

With so many potential content pitfalls in your path, it’s important to get permission, set expectations, and do your best to understand the humans you’re engaging with via email. That way, you can cater to the type of content they’ve shown interest in.

*“If you get a lot of people signing up and then unsubscribing a week later, that’s a problem even if your overall rate is excellent,”* noted Autumn. *“Unsubscribes are a leading indicator of a failure to connect with recipients; breaking them out in creative ways can help drive strategy.”*

So, take the time to segment and understand your lists. Then you can then start testing different creatives…

- Maybe you want to use less words or more images, or vice versa
- Try new kinds of offers or discounts
- Freshen up your subject lines and preheader texts to entice the click – or at least be interesting enough to convince your recipient to keep receiving your mail.

*“There are many factors that can lead to a high unsubscribe rate but one of the main reasons I’ve seen is irrelevant content,”* confirmed Desi.

***List maintenance***

If you’re treating subscribers who consistently NEVER open your emails the same as the ones who engage regularly, at some point, they might unsubscribe (or complain, which is worse!)

You’ll have greater success in avoiding this fate by having a consistent list [hygiene regimen](https://www.socketlabs.com/blog/your-guide-to-spring-email-cleaning-2024/) to remove unengaged addresses, [segment](https://www.socketlabs.com/blog/5-ways-to-segment-email-for-better-performance/) low-engagement folks into re-engagement campaigns, and focus on ensuring you’re delivering the right mail to the people who actually want it.

***Frequency***

This is a BIG one! Are you sending too often? Dela Quist would contend [there is no such thing](https://www.onlyinfluencers.com/email-marketing-blog-posts/best-practice-email-strategy/entry/email-frequency-how-many-is-too-many): *“A good marketer with quality content, good design and well thought out offers, will likely be able to send more emails a week than a poor marketer and will generally do better for any given frequency be that 3,4,5 even 20 emails a week.”*

And hey, we all have targets to hit and money to make.

But ask yourself, “How much email is too much for the people on ***my list***?” The only way to truly know is to do a little testing and monitor your data closely to see how people react.

With that said, be intentional with any changes you make to your frequency — even if you’re only doing a test — and keep your subscribers in the loop!

*“One organization I worked with wound up with a high unsubscribe rate because they initially decided to dramatically increase sending and push more commercial content for a long-time list that had been low volume and relatively low on sales content,”* said Autumn. *“They didn’t announce this shift in their sending strategy, just started sending out sales-heavy emails multiple times a week when they had previously sent educational content once a month.*

*As you might imagine, that didn’t go well. I recommended they reduce the new strategy and send a re-introduction email to let subscribers know they would be reaching out more frequently with different types of content, and that they alternate sales and educational content. This would give subscribers a chance to feel in control and more connected to the brand, rather than ‘acted upon.’”*

Autumn’s advice worked exactly as planned: *“They did lose some subscribers with their re-introduction email, but fewer than they had been losing with the unannounced shift in strategy, and the unsubscribe rate stabilized not too long after their new strategy stabilized.”*

If you’re not heeding the signs when people aren’t interested in what you’re sending, you run the risk of over-saturating your recipients’ inboxes and inflating your unsubscribe rate. So, monitor all your email engagement metrics, including [opens](https://www.socketlabs.com/blog/email-performance-red-flags-low-open-rates/), clicks, unsubscribes, and [complaints](https://www.socketlabs.com/blog/email-performance-red-flags-spam-complaints/) for signs of a problem.

If you’re sending through SocketLabs, our [StreamScore](https://www.socketlabs.com/hub/streamscore/) helps you monitor performance by analyzing all of your metrics (plus a whole lot more) to let you know when engagement is becoming a problem.

![](https://www.socketlabs.com/wp-content/uploads/2024/05/Homepage-HERO.png)

***Disconnected email streams, teams, and strategies***

As organizations grow, it’s common for various mail streams to be managed by separate teams, which can lead to recipients receiving multiple emails in a short period of time.

Imagine: Marketing is sending newsletters and promotions, automations are in place and firing according to their pre-determined triggers, other automations are in place reminding recipients to pay their bill or try out that new feature, sales is doing their thing — you get the picture.

If you have multiple teams sending email, get on the same page to ensure recipients aren’t facing an email blizzard from your brand. If possible, consider adding rules within your sending platform to limit the number of emails someone can get within the same hour/day/week, prioritizing your [transactional](https://www.socketlabs.com/blog/what-is-transactional-email/) mail streams.

***Business stakeholders’ lack of understanding about email***

*“Some of the senders I work with who have high unsubscribe rates due to over-mailing are in that situation due to pressure from their leadership. When a CEO thinks sending more email equates to making more money, it’s very challenging for anyone else to say no. One technique that can help build a business case for backing off is measuring average subscriber tenure against lifetime customer value. This turns the conversation from ‘send more = make more money’ to ‘long term subscribers = make more money,’”* shared Autumn.

I love this approach! Many practitioners fall into the trap of trying to get their bosses to understand how email works. Hate to break it to you, friends, but that’s almost never going to happen (unless [Tim Moore](https://www.linkedin.com/in/tim-moore-38186b1/) is your CEO… #emailnerd4liiiiiife! )

Speaking in revenue and business impact is always the way to go when you’re speaking to the folks who are charged with ensuring your company meets their goals.

And finally, we have one that’s very much outside of your control…

***Changes in recipients’ interests and preferences***

You read that right! Sometimes the reason for an unsubscribe has very little to do with you.

![](https://www.socketlabs.com/wp-content/uploads/2024/05/Screenshot-2024-05-20-at-10.23.21%E2%80%AFAM.png)

As Desi explained, *“I have a friend who changes hobbies every other month. At one point she is interested in painting, then she decides to run a marathon or to brew her own beer at home. I can only imagine how her inbox would look if the unsubscribe option did not exist.*

*What senders can take out of this is that it’s normal for subscribers to change interests. What you can do about it is try to get to know your audience better, monitor their behavior, implement a preference center and ask them why they are leaving. This information can tell you a lot and help you build an even stronger email program.”*

### How Does a High Unsubscribe Rate Affect Performance?

***Deliverability***

The good news? Unsubscribes don’t impact your inbox placement the way spam complaints do. They’re more of a warning than a punishment — a canary in the coal mine, if you will.

Skyler told us, *“High unsub rates aren’t usually the reason there’s reputation damage, they’re just indicators that you’re doing something that needs to be investigated further.”*

Autumn added, *“I haven’t seen a scenario where a high unsub rate alone was the only factor causing damage. Usually by the point things get into damaging territory, there’s low engagement, high unsubscribes, spam complaints, abuse reports, bounces, blocks, etc.”*

That doesn’t mean you should sit back and kick your feet up, though!

*“In the absence of some sort of technical problem, high unsubscribe rates usually happen before anything more serious; ignoring a high unsub rate is when you begin to see worse issues that cause damage.”*

That means you need to keep a close eye on your unsubscribes, along with other performance metrics like delivery rates, opens, etc. Even actions like deleting emails without opening is considered “negative,” so if they’re seeing very little positive engagement and frequent unsubscribe requests, you could land on their radar as a potentially problematic sender.

***Return on investment***

Your unsubscribe rate is also meaningful when discussing the email channel’s return on investment (ROI) for your brand.

As Autumn pointed out, *“High unsubscribe rates alone – in the absence of other performance issues – are primarily damaging to long term revenue goals. When a subscriber stays on your mailing list, there’s a much greater chance that they will buy from you (or donate to your cause for nonprofit senders) in the future.*

*When someone unsubscribes, especially in the case where something about your mailing left a bad taste in their mouth that prompted the unsubscribe, you are much less likely to win their dollars down the line. Maintaining an active connection with subscribers gives you the opportunity to win repeat business and create relationships with enthusiastic supporters that can sustain your organization in the long term.”*

If you’re losing subscribers faster than you’re adding them, you have less opportunities to meet your goals, which can be just as worrisome as having trouble delivering mail…particularly for senders in publishing or other industries where list size is a primary KPI.

At the end of the day, the emails you send are an extension of your brand. They’re a chance to build trust and loyalty with a group of people who have shown interest in your brand. So, don’t blow it!

If you’re sending so much mail (or irrelevant mail, or annoying mail; fill in your own blank) your recipients are asking you to leave them alone, you’re damaging your brand.

Autumn knows the pain of this first-hand: *“There is a particular clothing retailer whose products I like but whose emails I really do not like. They send me WAY too much email, and it makes me buy less from them than I would otherwise. I finally unsubscribed when they sent me five emails about the same weekend sale.”*

Been there, Autumn. Been there.

### What’s Considered a “High” Unsubscribe Rate, Anyway?

This can vary based on the type of mail you’re sending, the industry you’re in, the products or services your company offers, the way you’ve collected your list, etc.

What you consider high might be someone’s lowest unsubscribe rate ever and they’re over the moon about it. *“Compare yourself to yourself,”* is how Autumn puts it.

Case in point: When I’m pinned down for an answer without knowing more, my recommendation has typically been to keep your unsubscribe rates consistently below 1% and *always* below 1.4%. But this is based on the senders I’ve worked with.

Then we’ve got Autumn, who is currently supporting Klaviyo customers. She says, “ *A great unsubscribe rate is under.2%, but if you’re normally at.02% and suddenly you’re at.15%, that might be worth looking into.”*

*“I personally pay attention to major spikes,”* said Skyler. *“If you have five people unsubscribing from your sends and suddenly 55 people are unsubscribing from a single send, that’s a problem (and there’s usually other alarm bells going off, like your spam complaint rate).”*

None of these answers are wrong…but you need to review your own baselines to know what should be considered “high” within your organization. By viewing your unsubs rates over time, it will be easy to spot changes in the level of negative sentiment with your emails.

Also consider the context of your sending program when you spot an elevated unsubscribe rate to determine if this is really something to be concerned about.

For example, having two or three unsubscribes when you send to 100 people may *seem* like a lot because the unsub rate is much higher than your normal sending volume of 100,000 (i.e. 3% vs 0.003%)…

- If that happens occasionally, nothing much to see here — back to your regularly scheduled programming.
- If it becomes a trend, it’s time for a closer look at that small-volume program. We’ll get into how to do that in a bit.
- If you suddenly have a huge uptick in unsubscribes, something likely went wrong and should be avoided in the future. Go figure it out.

Autumn shared a recent example that perfectly highlights the need to base your analysis in reality: *“I just saw a customer campaign with a 2.5% unsubscribe rate, which raised both my eyebrows, so I went to take a look. Turns out, the sender is shuttering their business in a particular country, and this was their final announcement to subscribers in that location. Understandably, many locals who will no longer be customers chose to unsubscribe.”*

### What Should You Do When You Have a High Unsubscribe Rate?

First, scroll back up to our section on what causes spikes or elevations in your unsubscribe rate.

Did you try something risky? Send a few extra emails this week? Is your subject line stale? Have you not cleaned your lists in a while? Is something broken? All within the realm of possibility.

If nothing seems out of the ordinary, here are a few recommendations to try to reduce the amount of unsubscribes on your next sends:

- **Audit your list collection and hygiene practices.** Ensure your lead magnets are aligned with the content you plan to send, getting permission and setting expectations at the point of signup, and removing unsubscribes and complainers so you don’t send to them again.
- **Test your signup forms and automations** to ensure everything’s working as expected.
- **Evaluate your messaging** to ensure you’re fulfilling the promises you’ve made about your content, frequency, offer selection, etc.
- **Go back to the drawing board!** Testing should be your new best friend, because it’ll help you understand what’s working: segment lists, try new content, personalize your offers, etc.
- **[Segment your recipients](https://www.socketlabs.com/blog/5-ways-to-segment-email-for-better-performance/)** into logical groupings like new subscribers, legacy subscribers, demographics, etc., so you can start analyzing any patterns you may find.

Autumn shared a multi-pronged approach she uses when counseling senders looking to decrease their unsubscribe rates. It’s something you can try once you tackle that last bullet point above.

*“Depending on what data you have available, it can be really interesting to track unsubscribe rates by cohorts such as purchasers vs. non-purchasers, recent subscribers vs. older subscribers, etc. (Depending on the specifics of your business, you might try other cohorts such as different product interests, demographics, or geographic region.)*

*Look to your cohort analysis to try to get a feel for whether the unsubscribe rate seems to be pretty even across your whole subscriber base, or whether certain groups of subscribers are more likely to unsubscribe. Here’s a few common issues and ways to counter them:*

- ***Losing new subscribers****: Check your subscription forms and pages. Are you accurately setting expectations? Is it possible people are signing up only for a coupon or a “chance to win” and then unsubscribing immediately afterwards? Try to pitch long term subscriber value on your sign-up pages and with a nurturing welcome series.*
- ***Losing old subscribers:*** *Look for buying patterns. Is your brand changing and losing older fans? Could someone have bought everything they want from you? Look for fresh tie-ins and value adds.*
- ***Losing subscribers based on product or region:*** *Send specialized promotions that speak to these subscribers.*
- ***Losing subscribers of similar demographics:*** *Consider design language and brand voice. Are you speaking their language? Do your emails look too old or too young? Consider paid user studies to understand your audience.”*

One other bit of advice: Don’t make it hard for people to unsubscribe!

*“I’ve seen brands putting extra effort in hiding the unsubscribe link in their campaigns. This can not only be extremely damaging for your sender reputation, but it’s also borderline illegal,”* said Desi.

*“If a subscriber cannot find an easy way to unsubscribe, they will most probably mark your emails as spam or report you as an abusive sender. I’ve worked with clients who managed to decrease their spam complaint rates significantly just by moving their unsubscribe link to the top of the email body instead of hiding it in the footer.”*

Google and Yahoo agree on the need to make unsubscribing easy, which is why they’ll start enforcing a one-click unsubscribe (RFC 8058) within the headers of any bulk message you send in June 2024. This topic is entirely related to unsubscribes, but it’s a whole ‘nother ball of wax, so you can [read more about it here](https://www.socketlabs.com/blog/2024-is-the-year-of-the-one-click-list-unsubscribe/).

## Final Notes

It never feels good when people jump off your list, but unsubscribes are a healthy form of negative engagement allowing recipients to politely tell you, “No thanks” without smashing the complaint button and making their MBP look at you sideways like you are a spammer.

A high unsubscribe rate is, indeed, a red flag, but it’s best treated like a caution flag since it’s not an indicator of a major emergency.

As always, if there is a dramatic and sudden increase in your performance, you’ll need to launch into investigation-mode to make sure you can get back to normal before you really do run into reputation issues. We hope this blog gave you the right tools for that job.

And of course, if you’re having challenges with a high unsubscribe rate — or anything else about email performance — [reach out](https://www.socketlabs.com/contact/). We’d be happy to provide recommendations specific to your use case.

Happy sending!

1. [Email Performance Red Flags: High Unsubscribe Rate](#elementor-toc__heading-anchor-0)
2. [Red Flag: High Unsubscribe Rates](#elementor-toc__heading-anchor-1)
	1. [Today’s Expert Panelists](#elementor-toc__heading-anchor-2)
		2. [What is an Unsubscribe Rate?](#elementor-toc__heading-anchor-3)
		3. [What causes a high unsubscribe rate?](#elementor-toc__heading-anchor-4)
		4. [How Does a High Unsubscribe Rate Affect Performance?](#elementor-toc__heading-anchor-5)
		5. [What’s Considered a “High” Unsubscribe Rate, Anyway?](#elementor-toc__heading-anchor-6)
		6. [What Should You Do When You Have a High Unsubscribe Rate?](#elementor-toc__heading-anchor-7)
3. [Final Notes](#elementor-toc__heading-anchor-8)
4. [Related Posts](#elementor-toc__heading-anchor-9)

#### Categories

- [Transactional Email](https://www.socketlabs.com/blog/category/transactional-email/)
- [Tools](https://www.socketlabs.com/blog/category/tools/)
- [SMTP](https://www.socketlabs.com/blog/category/smtp/)
- [Service Provider](https://www.socketlabs.com/blog/category/service-provider/)
- [Product Updates](https://www.socketlabs.com/blog/category/product-updates/)
- [On-Demand](https://www.socketlabs.com/blog/category/on-demand/)
- [News](https://www.socketlabs.com/blog/category/news/)
- [Migrations](https://www.socketlabs.com/blog/category/migrations/)
- [Integrations](https://www.socketlabs.com/blog/category/integrations/)
- [Hurricane MTA Server](https://www.socketlabs.com/blog/category/hurricane-mta-server/)
- [Events](https://www.socketlabs.com/blog/category/events/)
- [Email Marketing](https://www.socketlabs.com/blog/category/email-marketing-2/)
- [Email Analytics](https://www.socketlabs.com/blog/category/email-analytics/)
- [Developers & APIs](https://www.socketlabs.com/blog/category/development/)
- [Deliverability](https://www.socketlabs.com/blog/category/deliverability/)
- [Customer Experience](https://www.socketlabs.com/blog/category/customer-experience/)
- [Community](https://www.socketlabs.com/blog/category/community/)
- [Best Practices](https://www.socketlabs.com/blog/category/best-practices/)
- [Authentication & Security](https://www.socketlabs.com/blog/category/authentication-security/)

<iframe src="https://app.hubspot.com/conversations-visitor/5046138/threads/utk/794b263584f846f8922f08479cfd8e9a?uuid=54b4d7b92ebd4f0d8f82b0c44bfc0d5a&amp;mobile=false&amp;mobileSafari=false&amp;hideWelcomeMessage=false&amp;hstc=257878996.5f7a8dac7988abbddb7c85a8820f7202.1777314367729.1777314367729.1777314367729.1&amp;domain=socketlabs.com&amp;inApp53=false&amp;messagesUtk=794b263584f846f8922f08479cfd8e9a&amp;url=https%3A%2F%2Fwww.socketlabs.com%2Fblog%2Femail-performance-red-flags-high-unsubscribe-rate%2F%3Futm_campaign%3Ddeliverability_rate%26utm_medium%3Dblog%26utm_source%3Dsenditright&amp;inline=false&amp;isFullscreen=false&amp;globalCookieOptOut=&amp;isFirstVisitorSession=true&amp;isAttachmentDisabled=false&amp;isInitialInputFocusDisabled=false&amp;enableWidgetCookieBanner=false&amp;isInCMS=false&amp;hideScrollToButton=true&amp;isIOSMobile=false&amp;hubspotUtk=5f7a8dac7988abbddb7c85a8820f7202" title="Widżet czatu" allowfullscreen=""></iframe>