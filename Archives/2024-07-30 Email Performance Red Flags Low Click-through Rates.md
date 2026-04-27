---
type: Web
authors: '[[Lauren Meyer]]'
url: >-
  https://www.socketlabs.com/blog/email-performance-red-flags-low-click-through-rates/?utm_campaign=deliverability_rate&utm_medium=blog&utm_source=senditright
published: 2024-07-30T00:00:00.000Z
created: 2026-04-27T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
---


![A cover image for a blog post on Email Performance red flags: Click through rates](https://www.socketlabs.com/wp-content/uploads/2024/07/Low-Clicks.jpg)

A cover image for a blog post on Email Performance red flags: Click through rates

Hi friends, welcome back to another edition of Email Performance Red Flags: this time, low click-through rates (CTRs)! I’m happy to see the series has picked up steam and is proving helpful guidance for our readers. If you’re interested in helping us with a future edition, just hit me up and we’ll find a place for you on a future topic’s expert panel.

But now, let’s get into our next red flag.

After covering [spam complaints](https://www.socketlabs.com/blog/email-performance-red-flags-spam-complaints/), [unsubscribes](https://www.socketlabs.com/blog/email-performance-red-flags-high-unsubscribe-rate/), and [low opens](https://www.socketlabs.com/blog/email-performance-red-flags-low-open-rates/) as email red flags, you might be assuming this is an email deliverability-focused series. It’s not. It’s an **email performance** series.

And today, we’re going to explore a topic a bit farther removed from actual delivery and more aligned with a major factor impacting your ability to reach your goals with email.

So, your emails are getting delivered and you’re getting a lot of opens, but…

## Today’s Red Flag: LOW CLICK-THROUGH RATES

You’re seeing a major email performance red flag waving in the wind: low clicks!

For some, low click-through rates are par for the course and that’s ok. There’s no reason to panic if your aim is to deliver high value *in the newsletter itself* (like we do with [ours](https://www.socketlabs.com/socketlabs-monthly-newsletter/)).

For others, low click-through rates are a sign of a problem. One that’ll to make it hard for you to reach your goals with email.

As with our past editions, we decided to ask a few experts to help us unpack this issue and share their best advice to help you turn things around. Let’s meet them before we dive in.

## Today’s Expert Panelists

[**Alyssa Dulin**](https://www.linkedin.com/in/alyssadulin/) started her professional career as a teacher before deciding to help us educate email marketers on how to send better email nearly eight years ago. After a few deliverability-focused roles with Campaign Monitor, she now shares her email marketing experience in her role as Manager of Creator Growth at [Kit](https://convertkit.com/) (formerly ConvertKit), where she also worked in email deliv & compliance! I highly recommend checking out her podcast, [Deliverability Defined](https://convertkit.com/deliverability), with co-host [Melissa Lambert](https://www.linkedin.com/in/melissa-lambert-906330113).

[**Jeanne Jennings**](https://www.linkedin.com/in/jeannejennings/) is the founder and CEO at [Email Optimization Shop](https://emailopshop.com/) and general manager of Only Influencers, the original community of email industry professionals. She is Chair of the annual Email Innovations World, and brings more than two decades of digital marketing experience to students in graduate school at Georgetown University as an adjunct professor. Jeanne and I worked closely together on the [OI Metrics Project](https://oimetrics.com/) a few years ago — her approach is incredibly data-driven. Get ready to take notes (like I do).

[**Aubrey Miller-Schmidt**](https://www.linkedin.com/in/aubreymiller/) has more than 13 years of experience in marketing and a passion for email. In her current role as Senior Marketing Manager at [Main Street America Insurance](https://msainsurance.com/), she manages email marketing and communications campaigns, wrangles code for Outlook, and plans engaging customer lifecycle experiences — among other things. She also does improv! …and much like Alyssa, spent some time teaching the youth of our nation prior to becoming an email marketer.

With our email smarties introduced, it’s time to get down to business.

## How are click rates measured?

Let’s start at the very beginning. What kind of click rate are we even talking about? There are a few types to be aware of which you can use for diagnostic email performance monitoring:

### Click rate (CR)

The total number of links clicked on emails that have been delivered.

*Click rate (CR) = # of clicks divided by # of emails delivered, then multiplied by 100*

So, if you deliver 100 emails and have a total of 10 clicks, then…

*CR = (10 clicks / 100 emails delivered*) \* 100

*CTR = 10%*

One important note: if subscribers click on links multiple times, these will be recorded separately. So, if one recipient clicks the same link five times, it will be counted as five clicks. This can inflate your click rate, making it seem higher than the actual number of unique recipients who clicked. Great for leadership updates, not so great for your actual email performance.

For this reason, it’s ideal to look at your **unique click rate**, which counts only the first time a recipient clicks on any link within an email. This gives you a more accurate view of *how many* people clicked. Once you have this, you can calculate your unique click-through rate.

### Click-through rate (CTR)

The amount of people (well, unique email addresses) who receive your mail and click on a link within it. If your mail includes multiple links and a subscriber clicks on more than one of them, they’ll only be counted once since the CTR is measuring the number of unique email addresses who’ve clicked.

*Click-through rate (CTR) = # of unique clicks divided by # of emails delivered, then multiplied by 100*

If you deliver 100 emails and have 10 clicks, but 3 of those clicks are from the same person, then your unique click count is 7. So…

*CTR = (7 unique clicks / 100 emails delivered*) \* 100

*CTR = 7%*

The CTR allows you to understand how engaging and relevant your email content is…including your subject line, friendly From, preheader text, and the messaging and call-to-action (CTA) within the body of your email. Did that combination of email magic inspire them to take the next step (ahem, click)?

### Click-to-open rate (CTOR)

The amount of people who first open your mail, then click a link to be taken to wherever it is you’re asking them to go. Note that this one is calculated based on the number of unique opens, unlike the CTR which focuses on messages delivered. Similar to the CTR though, if people click on more than one link, the CTOR will only count them once.

*Click-to-open rate (CTOR) = # of unique clicks divided by # of unique opens, then multiplied by 100*

If you have 20 opens and 10 clicks, but again, 3 of those clicks are from the same person, then your unique click count is still 7. So…

*CTOR = (7 unique clicks / 20 unique opens) \* 100*

*CTOR = 35%*

As Jeanne wrote [for the OI Metrics Project](https://oimetrics.com/diagnostic/click-through-rate-ctr), *“CTOR gives you a good, clean read on how effective the body of your email is at driving clicks. It adjusts for any variance in open rate between email messages when you are comparing one to another (or one to many). This can be very useful when you’re doing A/B split testing to boost performance.*“

One major caveat with the CTOR is that both opens and clicks are susceptible to bot activity, often called non-human interaction (NHI). This can come from pre-fetched image loading like with [Apple MPP](https://www.socketlabs.com/blog/apple-mail-privacy-protection-for-email-senders/) as well as anti-spam filters following links to make sure they’re safe for recipients to engage with. I would contend though, that if a mailbox provider decided to pre-fetch the content for a recipient yesterday and the day before, they’re likely to do it again on future sends, so the trends in CTOR are still helpful for diagnostic purposes.

Got all that? I know, it’s a lot.

Before we move on, here’s a quick view of these 3 metrics so you can see the difference.

![The calculations for the click rate (# of clicks divided by delivered), click-to-open rate (# of unique clicks divided by # of unique opens) and click-through rate (# of unique clicks divided by # sent - # of bounces.)](https://www.socketlabs.com/wp-content/uploads/2024/07/Click-rates.png)

The calculations for the click rate (# of clicks divided by delivered), click-to-open rate (# of unique clicks divided by # of unique opens) and click-through rate (# of unique clicks divided by # sent - # of bounces.)

## Why we prefer CTR over the other types of click rates

When it comes to catching and dealing with email performance red flags, we suggest you focus on your unique click-through rate (CTR) more than your click rate (CR) or click-to-open rate (CTOR) because it gives you a more accurate look at how recipients engage with what you send as a whole.

Don’t get us wrong, all of them have value.

It’s just that the CTR allows you to look at the engagement of a wider array of things including your subject line, preheader text, friendly From, and so on…which more closely aligns with the way mailbox providers track [recipient engagement](https://www.socketlabs.com/blog/engagement-and-reputation-are-two-sides-of-the-same-coin/). The CTOR, on the other hand, is a better indicator of your call-to-action (CTA) or messaging success within the body of your emails.

With that established, let’s focus in on click-through rates, or CTRs, for the rest of today’s discussion.

## What’s Considered a Low Click-through Rate?

Alert, alert: Unsatisfying answer incoming.

There’s not a great benchmark for a CTR because it’s entirely dependent on your personal record of CTRs. It also depends on what your goals are with email: are you an eCommerce brand looking to capture an immediate sale, an Enterprise SaaS vendor running a sales nurture campaign, or sending a newsletter attempting to provide high value without people having to link out? Your ideal CTR is gonna be wildly different, depending on your answer.

So, you’ll need to calculate your average CTR to create your own benchmark and goals.

Jeanne works with a variety of clients, and she says, *“A low click-through rate is one that’s below your internal benchmark for that kind of campaign, that audience segment, and/or that type of content. It’s not difficult to calculate your own internal benchmarks, and internal benchmarks are more relevant and more useful than industry benchmarks.”*

She continued by pointing out that*, “Using an internal benchmark drives you to always look for ways to improve your CTRs – it doesn’t allow you to rest on your laurels if your CTRs are consistently above the industry benchmark. And it keeps you from getting discouraged and giving up if your CTRs are never anywhere near the industry benchmark. Your email marketing program is unique – your performance is as well!”*

Love that. Fully agree. Do better today than you did yesterday, and learn from what went well (and not so well) along the way.

Aubrey had some great suggestions on what to look at during your calculations…

![Aubrey Miller-Schmidt from Main Street America Insurance says "One method is to take 12-18 months of performance metrics and calculate a mean CTR. Ideally, each campaign should have at least 1,000 recipients. Next, calculate the standard deviation to measure the variability of your CTRs. If your CTR is more than one standard deviation away from the mean, it can be considered low.](https://www.socketlabs.com/wp-content/uploads/2024/07/In-blog-Graphic-Aubrey.jpg)

Aubrey Miller-Schmidt from Main Street America Insurance says "One method is to take 12-18 months of performance metrics and calculate a mean CTR. Ideally, each campaign should have at least 1,000 recipients. Next, calculate the standard deviation to measure the variability of your CTRs. If your CTR is more than one standard deviation away from the mean, it can be considered low.

After a while — and especially if you work with multiple senders over time (or at once!) — you might find some anecdotal evidence about when a CTR becomes worrisome in general.

We pressured our experts to give us an answer on when to worry, but don’t forget to apply a healthy shake of salt grains when Alyssa says, *“In general, I’d say a click rate below 2% is low, but again, there’s a lot of ‘it depends’ at play here. Each sender should use their own average click rate as a baseline to determine what ‘low’ looks like to them.”*

Oh, and add a few more pinches of salt for this part: a lot of folks throughout the industry are reporting elevated click activity recently due to non-human interaction (NHI) associated with anti-spam filtering. The amount of bot activity should be pretty consistent send over send, but it doesn’t help when you’re trying to assess how humans engage with your mail.

If you’re in the Email Geeks Slack group, you can find a few threads where people are discussing it. If you’re *not* in this group, go [apply here](https://email.geeks.chat/)! It’s an incredibly helpful industry resource for connecting with other email practitioners and having your questions answered by experts. *Note: we’re not affiliated, just find it share-worthy.*

## What is the Impact of Low Click-through Rates?

This is a great spot to reiterate the difference between CTRs and click rates (CRs). Remember, we’re talking about **how many people receive your mail and then take the next step to click** on your CTA, not the total number of clicks (which might include a few hyper-clickers misleadingly inflating your CR).

### Lower Return on Investment

A low CTR can have a hugely negative impact on the return on investment (ROI) of your entire email program. Fewer clicks on your mail means fewer email conversions. If you’re spending time and money collecting email addresses, managing lists, and creating emails with the intent to get people to purchase a product after receiving the email, and they’re not making purchases, your ROI will be in the dumps. Huge amount of effort with very little to show for it.

### Less Brand Loyalty from Email Subscribers

A low CTR is a major indicator that your combination of sender, subject line, preheader text, offer, and messaging isn’t ideal. Remember, these people received your mail, but they didn’t feel compelled to open and click on through to your website.

Subpar messaging — particularly within the first few emails you send — could be damaging your brand value and your likelihood of building a strong email relationship with subscribers.

They signed up for your mail with curiosity but somewhere along the way, you lost their interest. Could they now expect another uninteresting email from your brand? Perhaps. You don’t want them to think you’re The Boring Brand <sup>TM</sup>.

### Impacts on Deliverability

Clicks are positive engagement. Less clicks mean less positive engagements, which means less opportunities to prove to mailbox providers that your mail deserves to stay in the inbox.

Delivered emails without clicks could also lead to list churn. For example:

- People receiving your mail, opening it, and then marking it as spam, which would hurt deliverability on future sends.
- Recipients opening your mail, not liking what they see, and promptly [unsubscribing](https://www.socketlabs.com/blog/email-performance-red-flags-high-unsubscribe-rate/). This one doesn’t hurt your deliverability, but it does prevent you from building a relationship with people via email.
- Subscribers deciding they’ve received enough snoozey subject lines from you that they make use of the [one-click list-unsubscribe](https://www.socketlabs.com/blog/2024-is-the-year-of-the-one-click-list-unsubscribe/) mechanism that’s now [required by Google and Yahoo](https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/), allowing them to unsubscribe without opening an email. Again, not a problem for your deliverability, but still not ideal.

## How to Spot a Low Click-through Rate

If you’ve been reading along with this series, you know what we’re gonna suggest…

Always be monitoring your email performance metrics! Without monitoring them regularly, and over time, you won’t be able to see how things are progressing, whether positively or negatively. Which makes it hard to identify problems and opportunities to improve your email performance, and even harder to tell a compelling story about how well your email marketing is going to your customers and/or leadership team.

The data you need to keep track of your click-through rate should be available at any email service provider (ESP). This is a core metric most people track.

If your ESP doesn’t give you a CTR right off the bat, it’s easy to calculate it yourself. We mentioned it up top, but quickly: divide the amount of clicks your emails get by the amount of non-bounced emails (aka the # of emails delivered).

![The calculation for the click-through rate is # of unique clicks divided by # sent - # of bounces.](https://www.socketlabs.com/wp-content/uploads/2024/07/CTR.jpg)

The calculation for the click-through rate is # of unique clicks divided by # sent - # of bounces.

Also review metrics downstream of click activity: are you seeing a decline in website traffic, conversions, and/or revenue-per-email as well?

## When to Worry About a Low CTR

So…let’s say you notice a sudden drop in your click-through rate. Despite what you may be feeling inside, it’s not time to start hyperventilating.

*“If your CTR drops but every other metric stays in normal range, I wouldn’t be concerned just yet, but I would be curious,”* reported Alyssa. *“Is there anything about the content or layout that changed? Were the CTAs clear? Is the topic relevant to your subscribers? There might be some great learnings here!”*

Aubrey echoed Alyssa’s sentiments, so you know it’s good advice.

*“Ask yourself: Is there something broken in my message? Is there an event or something in the news that impacted my campaign? Why do I think this happened? Create a hypothesis,”* Aubrey suggested.

*“What can I test to find out more? These kinds of questions can lead to actionable insights. While a single low CTR isn’t typically a cause for concern, it’s essential to monitor trends. If you notice a consistent decline or multiple instances of low CTRs over a few campaigns, it’s time to investigate further. Identifying patterns and testing hypotheses can help* *pinpoint the underlying issues and guide you towards effective solutions.”*

Now we know how to spot a low CTR and we know to take a nice, deep breath when we see something amiss. What next?

It’s time to figure out what’s causing your low CTR so you can start working on fixing the problem(s). So, let’s examine how you might find yourself in this scenario.

## What Causes a Low CTR

Jeanne said, *“There are a lot of things that can cause a CTR to drop. You need to investigate and see what, if any, other symptoms are present. Are other metrics also low or trending downward? Did anything change around the time the CTR fell, or began to fall?”*

She also provided this handy list of some common causes of low CTRs:

![](https://www.socketlabs.com/wp-content/uploads/2024/07/In-blog-Graphic-Jeanne-1-1.jpg)

Click rate (CR) = # of clicks divided by # of emails delivered, then multiplied by 100

### Factors Within Your Control

The great news about a low CTR is there are so many ways to improve it! First, let’s look deeper at the most likely reasons that are within your control, followed by the ones you can’t.

**Deliverability**

While some of you reading along might contend that deliverability is not within your control, we respectfully disagree.

The new rules put in place by Google and Yahoo require bulk senders (defined as those sending more than ~5k messages per day) to authenticate with SPF, DKIM, and DMARC. This requirement means mailbox providers can much more easily tell one sender apart from all others (even when they’re sending from the same IP). Which means senders are now getting the deliverability deserve.

So, if you’re not following foundational best practices such as getting permission before emailing, authenticating your sending domain, and making it easy to unsubscribe, your mail is at risk of being delivered to the spam folder. It’s gonna be hard to maintain a healthy click-through (or open!) rate if recipients aren’t seeing your mail in their inbox.

#### Subject Line and Preview Text

These are our first impression in the inbox. While we know our CTR is more concerned with clicks after someone receives the message, you’ll (hopefully) see a lift in your CTR by enticing more people to open with a great subject line and preview text. More people opening your mail provides an opportunity for more clicks through to your landing page.

If you’re concerned your subject line or preheader are negatively impacting your CTR, evaluate whether these email elements are aligned with your recipients’ interests or expectations of you as a sender.

#### Messaging

Let’s get back into the challenge of moving from delivered to opened to clicked. If you’re not making your way to the end of that email rainbow, it’s possible your messaging isn’t hitting them right. Is there a poor fit between recipient and content? Consider whether you’ve used personalization, segmentation, or other ways of making sure the content is tailored to the recipients’ interests.

More broadly, if you’re noticing your business-driven messages, like the kinds of sales or offers you’re bringing, aren’t enticing a click, perhaps you need to reconsider more than your email strategy. It’s possible the business needs to introduce different incentives and lead magnets to see if certain types of offers are more intriguing than what’s been used historically.

Alyssa had a great example of expectation not meeting reality when helping a customer troubleshoot a low CTR on confirmed opt-in mail.

*“In these instances, the issue is usually that the sender tried to disguise the opt-in confirmation as something else. For example, the subject line is often something like ‘Here’s your freebie!’ and the button to confirm your opt-in is disguised as ‘Click here to access your freebie,’” explained Alyssa.*

*“We find opt-in confirmation emails are much more successful and gain more clicks when senders are very transparent about what the message is for, and that a click is required to stay on the list.”*

#### Call-to-action (CTA)

Looking even more closely at your messaging is imperative: Is your call-to-action clear, apparent, and appealing?

People won’t click on something if you don’t make it clear they’re supposed to click. It’s possible you’ve been too vague in describing their next step as a customer. Maybe the button isn’t prominent enough, or the text isn’t very clear, or maybe you didn’t use a button and they aren’t aware there’s something to click on. Maybe you didn’t use a CTA at all!

Take this experience Jeanne had with a sender trying to increase paid subscriptions to heart:

*“When I looked at the wireframe template, I had an idea why; there was one CTA button and it appeared at the bottom of the email,”* recalled Jeanne. *“People would have to read it all (it wasn’t short) and/or scroll down to see it. The CTA was not visible in the first screen view of the message.”*

Jeanne’s solution provided a two-fold benefit: *“We added a CTA at the top. The image was full-width, so we put the CTA just below the image and just above the copy. So simple it seems silly, right? But we got a significant boost in* [*revenue-generated-per-email-sent (RPE)*](https://oimetrics.com/business/revenue-per-email-sent-rpe) *– and in CTR.”*

Also be sure your CTA button has a working link! Nothing worse than finding our your CTR issue is because your button wasn’t linking out.

#### Frequency

…This is a tough question to ask, and it’s even tougher to answer, but we’ve gotta go there.

Are people sick of your email?

Maybe they’re still receiving your email, but are you giving them stale offers or the same things repeatedly? Are they not opening (or clicking) your mail at all because you’re simply sending too much?

Evaluate the frequency of your email and the variety you’re sending, because it’s not unusual for a person to open five emails from the same brand in a week, but if all five have the same offer…do you expect them to click every time?

I wouldn’t be so sure they will, pal…

### Factors Beyond Your Control

While we said we were looking at things you can influence, we’d be remiss if we didn’t mention factors you need to be aware of, even though you don’t have control over them directly.

#### Seasonality & Current Events

The biggest one is seasonality. It might not affect your inbox placement, but the volume and frequency of seasonal emails can certainly impact your customers’ behavior.

Aubrey encouraged marketers to, *“Take a step back and check the news, holidays, typical vacation patterns, and your competitors. Sometimes people are just not in the mood to hear from you due to these external influences.”*

*“For instance, during major holidays or significant global events, engagement may drop as people are preoccupied with other activities or concerns. In such cases, it’s beneficial to align your email campaigns with the seasonal mood or simply pause during major disasters.”*

Maybe you aren’t stressed by holiday shopping because you aren’t selling a product, but your recipients surely have an inbox full of other folks selling to them super hard. This year, attention-spans for those of us in the U.S. are also divided because of the massive number of emails being sent about the upcoming presidential election.

Consider your industry, your audience, and what’s going on in your recipients’ lives and make decisions accordingly.

Though you can’t control things like an election year (gulp) or sudden natural disasters, don’t forget these things impact the people you’re trying to influence.

#### Technical Reasons

Alyssa told us, *“I often see CTRs fluctuate from bot clicks. It’s common for the links in our emails to get automatically “clicked” by spam filters to check for safety, and spam filters have their own logic to determine when links should be auto-clicked. Sometimes I’ll see a sender’s click rate drop and it’s clear there was a huge decrease in bot clicks for the email compared to past emails they’ve sent.”*

So, before going down a never-ending rabbit hole, make sure you’re considering whether less *humans* are clicking on your email, or if less bot clicks are the reason your CTR is lower. This may actually be a *good* sign, suggesting your sender reputation has improved to the point that spam filters feel less need to click into your links to make sure they’re safe for their users.

## Improving Your CTR

We’ve walked through some reasons you might be seeing a low CTR, but you might still be wondering what you should do once you determine the cause, especially if the cause is a mix of things.

Should you immediately launch into [re-engagement](https://www.socketlabs.com/blog/re-engage-before-you-disengage/)? Should you just change your subject line or CTA and see what happens next? Your options are kind of endless, which is both a great and anxiety-inducing place to be.

*“The short answer is performance testing. Even if your CTR isn’t low, you should be testing to boost your bottom-line metrics on an ongoing basis,”* reminded Jeanne.

Let’s break down some good solutions to try.

### Troubleshoot Deliverability Issues

When you’re seeing high delivery rates but everything downstream is low (i.e. your opens, clicks, web traffic, and/or conversions), it’s possible that mail is being accepted by mailbox providers’ servers, but it’s not landing in the inbox. In this scenario, your low CTR is driven by the fact that recipients aren’t seeing your mail in a place they can readily engage with it.

If you suspect this is your reason for a low CTR, check out this blog we wrote on the [top reasons your email lands in spam](https://www.socketlabs.com/blog/5-reasons-why-your-email-goes-to-spam-instead-of-the-inbox/), and this one all about [how to deal with low open rates](https://www.socketlabs.com/blog/email-performance-red-flags-low-open-rates/) (which are oftentimes a symptom of a deliverability issue).

### Reconfigure (or Start Using) Segmentation

Are you segmenting your lists? This can be as simple as splitting a list in half to try sending one version in the morning and one version in the afternoon. It can be as complex as building a profile based on location, past purchases, click history, and more. The opportunities are endless, but the intent is clear:

[Segment your lists](https://www.socketlabs.com/blog/5-ways-to-segment-email-for-better-performance/) into sections so you can better tailor the message to the people you’re sending to and encourage more engagement.

### Use Personalization

Personalization goes hand-in-hand with segmentation. Your segments should reflect opportunities to deeply personalize your email messaging.

We’re not just talking about throwing a first name into the subject line, either. Build your emails to speak to the recipients’ needs or interests. And build those emails around the reasons people signed up to hear from you in the first place.

If you send someone an email about a seasonal sale, and they open it to see what you’ve got…if they’re in a warm climate and all you have on sale is winter jackets, it’s doubtful you’ll earn their click. Aligning recipient interests with your approach is a fundamental method of personalization.

Maybe 80% of the people on your list don’t click on email when you send it to them in the morning, but they engage regularly when you contact them at night. That’s personalization, too.

### Test Messaging: What’s Resonating (or Not)?

While the overarching advice is “test everything,” we want to be super-specific about testing messaging because as we determined earlier, your CTR is a direct correlation between people receiving your mail, opening and reading it, then choosing whether to click.

Messaging and a compelling CTA are key, and Alyssa has you covered with one way to test…

![Alyssa Dulin from Kit says, "Give your subscribers a good reason to click! Avoid using 'click here' or similar vague terms on your CTAs. Instead, use something descriptive that highlights the value of clicking like 'Alyssa's secret to improving the CTR".](https://www.socketlabs.com/wp-content/uploads/2024/07/In-blog-Graphic-Alyssa-2.jpg)

Alyssa Dulin from Kit says, "Give your subscribers a good reason to click! Avoid using 'click here' or similar vague terms on your CTAs. Instead, use something descriptive that highlights the value of clicking like 'Alyssa's secret to improving the CTR".

### Test Formatting: What Makes it Easy to Engage?

Not only should you test the actual copy you’re using, but also play around with how you’re formatting the message.

*“I’ve found success boosting click rates by better formatting the email’s content,”* shared Alyssa. *“If your email isn’t easily skimmable with really clear CTAs (and very few of them), it’s less likely subscribers will click on the links. Utilize headers, images, small groups of text, and buttons to make your email easy to skim through and quickly find the CTAs.”*

### Incorporate Customer Feedback

Because great minds think alike, Aubrey suggested a similar tactic with a little extra on top: *“Assess if you have any product or brand reputation Issues. Is your product or offer in your email appealing to your audience? Gather voice of the customer feedback to understand if there are product or service concerns impacting interest. By investigating these areas, you can usually identify the root causes of low CTRs and implement targeted strategies to improve engagement.*

### Analyze. Test. Optimize. Repeat.

Jeanne gave us some food for thought as well. Instead of only focusing on what works…don’t forget to spend time analyzing what doesn’t.

*“Sometimes you can get learnings even if a test fails. For instance, you might have a test which delivers a conversion rate that’s lower than the control, but a CTR that’s higher,”* said Jeanne.

*“That’s a prime opportunity to think about why it drove more clicks and see if you can implement that in your next test to drive an increase in your key performance indicator (KPI).”*

TL;DR is the amount of knobs and levers you have at your disposal to tweak and toggle is vast. Think big. Think outside the box. Try everything.

## That’s All, Folks!

Just kidding, email never sleeps and we’ll never run out of things to talk about! But we *will* wrap up this blog here.

We hope you now have a good sense of how to monitor your CTR for worrisome trends, how to investigate causes, and what you can do to get your email back on track. We’d like to thank Alyssa, Jeanne, and Aubrey for sharing their expertise and anecdotes to help put these abstract concepts into real-world context.

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

<iframe src="https://app.hubspot.com/conversations-visitor/5046138/threads/utk/10ed2794ed0749e8846a598582c47282?uuid=053c265452924f079a33da5adebe485c&amp;mobile=false&amp;mobileSafari=false&amp;hideWelcomeMessage=false&amp;hstc=257878996.5f7a8dac7988abbddb7c85a8820f7202.1777314367729.1777314367729.1777314367729.1&amp;domain=socketlabs.com&amp;inApp53=false&amp;messagesUtk=10ed2794ed0749e8846a598582c47282&amp;url=https%3A%2F%2Fwww.socketlabs.com%2Fblog%2Femail-performance-red-flags-low-click-through-rates%2F%3Futm_campaign%3Ddeliverability_rate%26utm_medium%3Dblog%26utm_source%3Dsenditright&amp;inline=false&amp;isFullscreen=false&amp;globalCookieOptOut=&amp;isFirstVisitorSession=true&amp;isAttachmentDisabled=false&amp;isInitialInputFocusDisabled=false&amp;enableWidgetCookieBanner=false&amp;isInCMS=false&amp;hideScrollToButton=true&amp;isIOSMobile=false&amp;hubspotUtk=5f7a8dac7988abbddb7c85a8820f7202" title="Widżet czatu" allowfullscreen=""></iframe>
