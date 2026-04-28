---
type: Web
authors: '[[Lauren Meyer]]'
url: 'https://send-it-right.com/blog/building-sender-reputation'
published: 2024-07-13T00:00:00.000Z
created: 2026-04-27T00:00:00.000Z
tags:
  - digital-campaigning
  - content-marketing
---


This week’s lesson is all about sender reputation and the very large part recipient engagement plays in building and maintaining yours.

But I don’t wanna make your eyeballs bleed, so let’s pretend we're in a totally rad band together…your choice on what style of music we’re into. And the way we collect and manage our email lists, how recipients react to our content, and whether we’re properly authenticated is gonna make or break our chances at hitting it big.

We’re gonna start at the tippity top. Or I guess, the bottom…where the only people coming to our shows are a few friends (and sometimes our moms).

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/UHVJadoTpn9fQhory6?wmode=opaque" width="480" height="320"></iframe>

[via GIPHY](https://giphy.com/gifs/UHVJadoTpn9fQhory6)

Our friends are having a blast though. So that's good.

## What’s Sender Reputation?

Well, friend, the answer’s about as squishy as [trying to accurately define “deliverability”](https://www.linkedin.com/posts/lauren-meyer-emailgeek_why-your-deliverability-rate-is-wrong-activity-7093244201617821696-e0fI). It’s essentially a multi-faceted score attempting to figure out if your mail deserves a ticket to the inbox, a general admission seat waaaay back in the Spam section, or if it should be bounced at the front door.

The fun part? **There are** **hundreds of factors** **affecting sender reputation**, including authentication, configuration, list quality, IP and domain reputation, sending volumes, recipient reactions, and well, you *know* I could go on. But I won’t. Not this time. (You’re welcome. 💌)

**The funner part?** Most of those hundreds of factors aren't even visible to us senders. They’re happening inside an anti-spam algorithm or a person’s mailbox, and their providers don’t share that feedback with us. It’s like trying to figure out why our band’s new song is a hit without being able to see who’s buying our albums or attending our shows…besides Mom. She’s very vocal with her support (and her opinions on Kyle’s new *experimental* songs).

**The** **even funnerer** **part?** (Yesss, it’s a word now…roll with it.) Sometimes the factors affecting our inbox placement are outside our control, such as when we’re sending from the shared IP of a less-than-savory ESP and other customers start dragging down your reputation. Or when Jenny in sales decides to start spraying (and not even praying!) cold email from the same domain your newsletters, purchase confirmations *and* password resets are sent from. We all know that’s not gonna end well. 😒

Oh, and **here’s a** [**monkey wrench**](https://www.youtube.com/watch?v=I7rCNiiNPxA), just for good measure: each mailbox provider you send to has their own set of rules about what makes it into their users’ inboxes. And you’ve gotta play by all of ‘em if you wanna land that next gig, even if you disagree with them. Their house, their rules.

So, I can hear you sighing all the way from here. Let’s move on, yeah?

#### Why are mailbox providers tracking reputation?

I mean, if you’re reading this, you likely already know the answer: because spammers gonna spam, phishing and other nefarious email attacks are continuously on the rise, and advancements in AI have made bad mail look more legit, so it’s harder for everyday users to stay safe within their inboxes.

Which is why **the primary goals of mailbox providers are** **protecting their users** **and ensuring they stay** **happy** **with their email experience.**

How do they ensure their users stay happy?

### How do mailbox providers measure recipient happiness, anyway?

Lots of ways. **Mailbox providers have access to** **a whooooole lot more data** **about their users’ activities than us senders can even wish for.** Some examples of recipient happiness (ahem: engagement) signals that factor into their anti-spam algorithms include…

**Positive Engagement Signals:**

- Opens and Clicks: These are like fans cheering and dancing.
- Replies: Fans hopping into your DMs to tell you how much they love our new song (and Dave…they always love Dave).
- Categorizing: Actions like moving an email from spam to the inbox are like fans launching a Kickstarter campaign to help us go on tour. They’re telling the mailbox providers our emails should go to the inbox. This is helpful to deliverability, particularly when a lot of recipients are doing it.
- Forwards: Beautiful, wonderful, supportive fans (and moms) sharing your songs with others.

**Negative Engagement Signals:**

- Marking as Spam: Those dreaded hecklers booing you from the audience.
- Deleting Without Opening: Like fans walking out without listening, or showing up after the opening bands have gotten out of the way. One day we’ll be the headliner, Kyle. One day.
- Unsubscribing: I’m listing this as a negative because people leaving in the middle of your first song is never a good sign. BUT, it’s important to note that while it hurts to have someone bail, **unsubscribes don’t impact your deliverability the way spam complaints do**. You can read more about why in this piece I did with a couple of email pals: [Autumn Tyr-Salvia](https://www.linkedin.com/in/autumn-tyr-salvia-3267815/), [Desislava Zhivkova,](https://www.linkedin.com/in/desislava-zhivkova/) and [Skyler Holobach.](https://www.linkedin.com/in/skyler-holobach/)

Now, I don’t think I need to tell you that senders don’t have access to data on all of these actions. Bummer, for sure. But it’s not [the end of the world as we know it (and I feel fine)](https://www.youtube.com/watch?v=-s97_bBGobQ).

### Senders have ways to measure recipient happiness, too.

No need to get antsy. **There are** **plenty of proxy metrics** **senders can use** to mimic the positive and negative sentiment mailbox providers are able to see, including [opens](https://www.socketlabs.com/blog/email-performance-red-flags-low-open-rates/), clicks, replies, [unsubscribes](https://www.socketlabs.com/blog/email-performance-red-flags-high-unsubscribe-rate/), and [spam complaints](https://www.socketlabs.com/blog/email-performance-red-flags-spam-complaints/) coming in via feedback loops. Email’s [cool like that](https://www.youtube.com/watch?v=cM4kqL13jGM).

There’s 3rd party data available directly from mailbox providers, including Google Postmaster Tools and Yahoo’s Sender Hub. And we can monitor [blocklistings](https://www.socketlabs.com/blog/how-to-avoid-email-blocklists/) which, in some cases, are driven by spam complaints.

Seed testing (or just signing up for your own list and checking where that mail lands) can also help uncover reputation issues because **when messages go to the spam folder with Google, they share a message indicating why.** For example…

![](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/ff8ca4b0-9f59-4ece-b086-21656d2cbc3f/Similar+messages+identified+as+spam.png?format=2500w)

Why’s this message in spam? Gmail says “It is similar to messages that were identified as spam in the past.”

Here’s one that's even more specific, calling out the actual sending domain that’s driving the issue.

Sooo, yeah. Not a great feeling when your mail is landing in the spam folder or worse — getting blocked. There are ways of avoiding that though…

![](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/e50eb674-9ca1-4022-addc-03418e2a3b2b/Similar+messages+identified+as+spam+%282%29.png?format=2500w)

Why’s this message in spam? Gmail gets more specific, saying “Lots of messages from \[domain\] were identified as spam in the past.” It doesn’t get much clearer than that, does it?

### So, how do we manage our sender reputation?

Well, it requires a multi-layered, sometimes delicate approach...just like telling Kyle we’re *not* playing his newest song at our next gig. 😒

And we’ve gotta build our band reputation, errr… brand reputation up over time with each email we send…starting with the gigs where only a couple of friends (and our moms) show up before working our way up to sold out shows at Madison Square Garden.

Thankfully, major mailbox providers like Google and Yahoo have very clearly written what they require from email senders right on the wall, making it easier to know exactly what to focus on. We’ve got to align our practices with *their* expectations because hiding behind legislation like CAN-SPAM in the U.S. is no longer gonna work (as if it ever really did). Say it with me now, **legality** **does not** **equal inbox placement.**

Here’s what mailbox providers expect in 2024:

- **Proper Authentication:** Use SPF, DKIM, and DMARC — it’s like ensuring our band has all the right permits and a solid manager. Not to mention, our fog machine. Gotta remember the fog machine next time (DAVE!! 🙄).
- **Positive user engagement:** You’ve gotta be sending relevant content to people who’ve opted in — it’s like playing the hits our fans actually want to hear instead of that experimental stuff Kyle’s always on about.
- **Evidence you’re monitoring and acting upon bounces:** There’s a lot of detail in the bounces mailbox providers send to us when they don’t accept an email into their system. Be sure to handle hard bounces (invalid addresses) and soft bounces (temporary issues, usually driven by a poor reputation) — much like how Kevin ensures our instruments stay tuned and the merch table’s all set up.
- **An easy unsubscribe process**: One making it simpler for people to opt-out than it was to opt-in — like a concert venue with a clear path to the exit so when Kyle gets his way, they can head to the bar next door. (Never again, Kyle. For real this time. *Never again.*)

Sounds reasonable enough, but it can be overwhelming when you actually get into the nitty gritty of things. Just remember, you’re not alone. Here’s a list with a bunch of [excellent email people who can help](https://send-it-right.com/experts-to-learn-from), and another list where you can [meet even more email people](https://send-it-right.com/connect-with-email-nerds) to commiserate (and troubleshoot) with.

A few suggestions for building a solid foundation for our sender reputation:

#### 1\. Stay Compliant

If you’re asking “with what?” please scroll up, like, 4 inches. My oh my. WAKE UP.

#### 2\. Focus on what you can control

Which is certainly not Kyle’s reaction (or that of your recipients)...people are unpredictable.

But there are many things you *can* control. Be sure you’ve got these loaded up in our van before it’s time to leave for the show:

- **Authentication.** We talked about this **👏 just 👏 last 👏 week!** If you missed it, go find that email in your inbox or [read the expanded version](https://send-it-right.com/blog/intro-to-email-authentication) on my email marketing bl(aahhhh!)g.
- **Whose garage we practice in.** Here, I’m referring to which ESP you’re sending email through. Some of them (like the one I work for) have strict policies and procedures in place to ensure bad senders aren’t able to send through us. Others do not. They let other bands sneak in the back door and even get up on stage with us sometimes. Not cool (except that time they interrupted Kyle’s new song…which was even less cool). Point is, we need to find a provider who’s gonna help us knock the audience’s socks off, not become an agent of chaos by putting deliverability problems on our plate. Sharing (ahem, sending) our hand-written love songs with the world is already stressful enough…we don’t need to add in a dance routine, too. (Seriously, Kyle. Enough already. 😒)
- **How we build up our fan base.** Did Ashley buy that list of people who went to the music festival but clearly didn’t come to see us (since we had 7 people in our audience, including dear old Dad)? Or did Kevin have a signup sheet (or QR code!) on our merch table so people who had a good time to see us live again? Depending on which path we choose, our email stats (and deliverability) will look wildly different: low vs high open and click rates…not to mention, spam complaint rates. (the [Chris Gaines](https://en.wikipedia.org/wiki/Chris_Gaines) equivalent to email). Build it right so you can send it right, mmkay?
- **Merch** - no explanation needed. You gotta have [great merch](https://www.emailloot.com/?ref=send-it-right.com) (ahem, content).
- **How we treat our fan base.** Ideally, you’re like Dave Grohl or Lady Gaga, who absolutely love their fans and go to great lengths to support them like a community. That bodes well for generating lots of positive reactions from your fans and very few negative interactions. Even still, fans can be fickle. Some loved one of our songs intensely but now they’re over it. Others loved the first album but aren’t into our current stuff. One person on our list only signed up because they had a crush on Dave last summer.

Do your best to suss out who’s a super fan, who’s gonna show up to our gigs once or twice a year, who *might* still be interested if we stop letting Kyle write songs (ahem, change up our email content to something they might resonate with more), and who’s probably a lost cause. Once you understand it, act on what you learned!

#### 3\. Consider how to influence what’s outside your control

Mailbox providers (MBPs) are like the fat cat record execs determining if we get to make another record or not. And they’re relying heavily on how our listeners interact with us to determine our fate.

For example, every positive interaction (like an open or a click) nudges our new single closer and closer to the Billboard Top 40. But negative actions (like being marked as spam) are like getting booed off the stage, which is really gonna hurt our chances of landing our next gig.

We very rarely get to know why someone does or doesn’t like our songs (...Kyle 👀), but we *can* try to create more songs like the ones that made them fall in love with us in the first place. Which reminds me…

#### 4\. Pay attention!

If you spend a little time reviewing your email performance, you’ll be able to see how recipients engage with your mail and what MBPs think of you. Alongside metrics like delivered rates and bounces, you get a better idea of how things are going holistically. Don’t just watch clicks or conversions—consider the whole picture.

Starting with your ESP metrics. Look for trends that might suggest recipients are engaging less-than-positively with your mail (i.e. marking it as spam or unsubscribing), or that mailbox providers are rejecting it due to an issue with sender reputation (i.e. soft bounces).

Google Postmaster Tools is great for Gmail insights into issues with spam complaints, domain and IP reputation, and checking compliance with [their new rules](https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/). Yahoo has a Sender Hub which can help you “identify opportunities for improving how well your emails are received” (their words) by monitoring your spam complaint rates. I dove deeper into performance monitoring [in this blog post](https://www.socketlabs.com/blog/monitoring-email-metrics-after-google-and-yahoo-enforcement/). Go read it if you’re ready to look alive.

Also be sure to keep an eye on blocklistings, as these can sometimes be driven by a high rate of spam complaints. By looking at all of these data points as a bigger picture, it becomes easier to see what’s not going well. Speaking of which…

#### 5\. Try new things!

Perhaps you’re thinking, “what we’re doing is working, why rock the boat?” But eventually, we’re gonna need to evolve to keep our fans interested. One can only listen to so many versions of “Spamming Me Softly” before they’re begging one of us to go solo.

And the only way to evolve your style along with your audience is to test new things. They won’t all be winners (e.g. Kyle’s *experimental phase*), but some of those tests could help you identify really unique and brilliant ways to improve performance.

Think of your tests like a focus group where we find out what our fans *really* love about us. Some options include:

- length and style of subject lines,
- using our drummer, Dave’s name as our Friendly From instead of our band name
- segmenting to only send tour announcements to fans in the city where we’re performing vs all over the world (because you *know* we’ve gone global)
- Short vs long-form content
- One CTA vs links for days

See what resonates, and then start makin’ moves.

#### 6\. If you see something, don’t just say something, DO SOMETHING.

The same way our rockin’ band is constantly tweaking our setlist based on fan feedback (and Kyle’s whims 🙄), you should adjust your email strategy to keep your positive engagement levels high and your spam complaints low.

If engagement is trending in the wrong direction, use your data to make decisions about what to do: stop sending to purchased lists and unresponsive recipients, respect unsubscribes, and analyze what content and frequency work best. Or, you know, just tell Kyle we’re *not* playing his newest song at our next gig. 🙄

#### 7\. Don’t go chasing waterfalls.

In that list above, you may have noticed how I sorta glossed over hard bounces (invalid addresses). That’s because mailbox providers have become very focused on recipient engagement to help them determine the future fate of emails from a sender.

*Quick tip though, while we’re on the subject: unless your bounce rate is really high, they aren’t as impactful on deliverability as they used to be. If you’re anywhere near or above 5%, dig into how you can improve your list collection practices and send to your recipients more consistently — both could be contributing to a high hard bounce rate.*

**Why Recipient Reactions Matter (A Lot)**

Recipient reactions are like fan feedback being piped straight into a record exec’s analytical hands. Positive signals, such as opening, clicking, and forwarding your emails onto their friends are like rave reviews and sold-out shows. They tell mailbox providers your mail deserves to be in the inbox. You might as well be Taylor Swift, you email genius, you.

One practice that’s often overlooked: using a real reply-to address instead of a no-reply. This can be tough to do at scale because it requires you to actually man that address, but opening up a line for communication where our band can engage with fans on their terms can help us build loyalty and trust over time — kinda like inviting fans backstage to chat with us after the show.

Negative signals, like deleting emails without opening them and marking them as spam are like bad press and controversies that could very easily tank our careers, [Milli Vanilli](https://en.wikipedia.org/wiki/Milli_Vanilli) -style. These negative reactions play a huge role in whether emails reach the inboxes (and hearts of your readers) or get pulled down into the spam folder abyss by those swamp monsters Linda’s so in love with.

**Tips for Building Trust**

Before sending large volumes, warm up to mailbox providers like we do when we're the opening act. High delivery rates, lots of opens and clicks, and low spam complaints are our goals. Follow guidance from mailbox providers like Yahoo and Google, as if we’re working with our record label to bring our next album to life.

---

### Before you go...

What part of sending it right brings out the most stage fright in you?

[Reach out and let me know](https://send-it-right.com/contact). Your answers *help me* tailor my future lessons to *help you*.

---

Alright, that’s enough for this week. If I’m tired, I’m sure you are, too.

Remember, engagement and reputation are like the greatest hits and performances of our band’s long and storied career as musical legends. But only if we put the recipient experience at the heart of everything we do. Every day, all of the time.

[There are no backstage passes to the inbox](https://www.linkedin.com/posts/lauren-meyer-emailgeek_get-your-backstage-pass-to-the-inbox-activity-7071840668460990464-6XjS), despite what some folks might try to tell you. (RUN AWAY from folks trying to sell you one…it’s a fake. Hands down.)

Ultimately, happy recipients lead to positive engagement, which leads to happy mailbox providers, which leads to a happier YOU, too. And then the cycle repeats. So, get that flywheel spinnin’, my friends. It’s time to send it right!

For real now. That’s it, folks. Lights are comin’ up, it’s time to go home. No more encores…Kyle’s being Kyle again. 🙄

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/26BRKmqUonCPPit1e?wmode=opaque" width="480" height="270"></iframe>

[via GIPHY](https://giphy.com/gifs/colbertlateshow-stephen-colbert-late-show-ziggy-marley-26BRKmqUonCPPit1e)

Seeeeeee ya.

### Grab some of this merch on your way out.

Kevin doesn’t want to carry it home. [He’s got bigger problems.](https://www.youtube.com/watch?v=pMHA8yd8Pf4)

- [Google Postmaster Tools](https://www.socketlabs.com/blog/google-postmaster-tools/) and the Yahoo Sender Hub are two examples of tools that can help you gauge sender reputation.
- I recently interviewed reps from the product teams of Google and Yahoo! about their [new requirements that went into effect in Feb 2024](https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/). Check out the [highlights from our interactive discussion](https://www.socketlabs.com/blog/webinar-highlights-google-yahoo-talk-email-marketing-in-2024/) to understand the perspective of email’s record execs.
- Sick of reading? My bad. Here are some short (4 min) videos I recorded on [what sender reputation is](https://www.socketlabs.com/blog/teach-me-email-what-is-sender-reputation/) and [how to manage it](https://www.socketlabs.com/blog/teach-me-email-how-to-manage-sender-reputation/).
- Check out my deliverability resources — including hours of [video content](https://send-it-right.com/videos), [tools to help you send it right](https://send-it-right.com/tools-for-sending-it-right), [email experts to learn from](https://send-it-right.com/experts-to-learn-from), and a list of places you can go to [connect with other email nerds](https://send-it-right.com/connect-with-email-nerds) online and in person. My personal favorite is [The Watercooler.](https://send-it-right.com/watercooler)
- If you found this blog post helpful but aren’t signed up for my [Send It Right newsletter](https://send-it-right.com/newsletter) on email deliverability, jump on in.
- [Connect with me on LinkedIn](https://www.linkedin.com/in/lauren-meyer-emailgeek/) to join in on email deliverability discussions. We like to have fun. You should be a part of it!

I appreciate you taking the time to read this. You friggin’ rock. You know that?

Until next time, happy sending! 💌
