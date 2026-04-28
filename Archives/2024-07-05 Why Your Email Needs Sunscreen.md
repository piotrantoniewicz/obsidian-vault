---
type: Web
authors: '[[Lauren Meyer]]'
url: 'https://send-it-right.com/blog/intro-to-email-authentication'
published: 2024-07-05T00:00:00.000Z
created: 2026-04-27T00:00:00.000Z
tags:
  - digital-campaigning
---


Summer's in full swing, and all I can think about is SPF...only not the kind we use at the beach. 😒☀️ I'm thinkin' about email authentication, baby. (And yes, I AM a hoot at parties. Thanks for asking.)

That's right: SPF, DKIM, and DMARC. The acronyms every sender needs to embrace if they want to reach the inbox in 2024.

### Why should you care about authentication?

💌 Much like SPF protects us from the sun, email authentication protects your brand and sender reputation from fraudsters looking to hijack it and ride the wave as long as your reputation stays afloat...which won't be long, honestly. This is helpful to your deliverability, and also to maintaining a high level of trust with your email recipients.

💌 It gives everyone involved in the sending and delivering of an email more confidence in the fact that the mail is being sent by the REAL you, not that doppelganger who loves pretending to be you. This is helpful to your deliverability.

💌It sets you apart from other senders on the internet. Clea Moore, principal product manager for [Yahoo told me](https://www.socketlabs.com/blog/webinar-highlights-google-yahoo-talk-email-marketing-in-2024/) ~95% of the mail they receive on any given day is really bad mail — phishing, malware, and other stuff they don’t accept into their servers. The remaining ~5% of it **(that’s you!)** is gray or white mail, and they need to sort out which of *that 5%* is trustworthy vs something potentially harmful. Authenticating your mail allows you to establish your own sender reputation that (hopefully) very clearly shows you deserve to reach the inbox.

💌 Oh yeah, it's also required by Mama and Papa Email (aka major mailbox providers like Google, Yahoo, and Microsoft, among others). That's right: no auth, no entry into the mailboxes of your subscribers. You like delivering mail to these destinations, right? I thought so. Here’s [an article I wrote that gives a breakdown](https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/) of what’s required by these providers.

## What each authentication protocol does:

We’ll only get into the high-level today because there’s…a lot…to authentication and nobody’s got time for that during the summer. True story: I’ve gotta implement *the other* kind of SPF on my children in a couple minutes. They’re gettin’ antsy. So, here we go!

#### SPF

Sun protection factor 😎 (oops!) — I mean Sender Policy Framework (SPF). This one helps prevent sender address forgery by allowing senders to publish a list of IP addresses or server names authorized to send on their behalf. Mail is coming from an IP that’s not on the list? SPF = fail.

Here’s what SPF records look like:

![](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/bb57d6a8-350b-435f-ace9-c3bf067c37aa/example+SPF.png?format=2500w)

An example SPF record.

SPF does have its limitations, though: it doesn’t protect against types of spam, spoofing, and phishing where a fraudster intercepts a message during transit and changes the content or replays that content forward with different URLs (maliciously), kinda like a gang of mobsters swapping out original works of art for counterfeits. Which is why DKIM was created…

#### DKIM

DomainKeys Identified Mail (DKIM) allows the recipient mail server (e.g. Yahoo) to know if a message has been altered during transit, helping combat malicious actors lookin' to do a little spamming, spoofing, or phishing. It’s kinda like your email’s armored car, getting it from the artist (that’s you!) to the gallery without any hijinx.

Here’s what a DKIM record looks like:

![](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/96971d23-f46c-4126-9b76-4080470c1664/example+dkim+record.png?format=2500w)

An example DKIM record. 😐

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/de4aRYwfD7T7q?wmode=opaque" width="480" height="265"></iframe>

[via GIPHY](https://giphy.com/gifs/de4aRYwfD7T7q)

I know. This stuff hurts my eyes, too. Hang in there, we're past the worst of it (I think). 💌

#### DMARC

This is the last one we’re gonna cover today. **Domain-based Message Authentication, Reporting, and Conformance** (DMARC). A mouthful, I know. But this one’s worth the twisted tongue because it alerts you when bad actors are attempting to hijack or spoof your brand. It also tells you when **you’re failing your own mail** because it’s not properly authenticated.

How it works: you publish a TXT record telling receiving servers (like Google) what you'd like them to do with mail sent using your domain that doesn't pass DMARC checks: deliver it as normal (p=none), accept the mail into their systems but quarantine it from the inbox (p=quarantine), or reject it completely (p=reject). This is called setting policy.

Here’s what a DMARC record looks like:

![](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/b51365d2-fcc4-48ce-b27f-012dd04a3a72/Example+DMARC.png?format=2500w)

Example DMARC record with a policy of p=none.

Mailbox providers don't *have* to listen to you—they deliver anything they believe their users want to receive, even if it goes against the DMARC policy that’s been published—but you can still tell ‘em your wishes through your DMARC record.

Publishing SPF and DKIM records is normally a one-and-done thing, but DMARC requires a bit more of a phased approach where you set a different policy.

**Phase 0:** Your SPF and DKIM must already be in place.

**Phase 1:** Publish a DMARC record with a policy of **p=none** (what I like to call “monitoring mode”) and provide an email address where authentication failure reports can be sent. Monitor for at least a few weeks (or months) to ensure all of your mail is lookin’ good. Do not pass “Go” until you’ve corrected any issues uncovered through your DMARC reports.

**Phase 2:** Change your DMARC policy to **p=quarantine**. This one still allows you to monitor, but also sends instructions along to mailbox providers, asking them to keep your mail away from the inbox if it’s not passing authentication checks. This means you can doom your own mail to the spam folder (or an adjacent ‘quarantine’ zone) if your authentication isn’t buttoned up. This is why you don’t skip Phase 1.

**Phase 3:** The holy grail. Here, you’re changing your DMARC policy to **p=reject** which is (you guessed it!) asking mailbox providers to bounce your mail back to sender at the front door. Obviously do not skip Phases 1 or 2 unless you like telling your boss that you didn’t make your plane to the conference because you forgot your ID badge, again. (ugh)

**Phase 4:** Keep monitoring your DMARC reports and act on any failures you discover…asap. If you’re at p=reject and you note a problem, consider pausing outgoing mail or dropping your policy to p=quarantine or none until you resolve it.

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/lmUCSWmFkThuCP3PTo?wmode=opaque" width="480" height="480"></iframe>

[via GIPHY](https://giphy.com/gifs/warnerbrosukandireland-catherine-tate-nan-the-movie-lmUCSWmFkThuCP3PTo)

I feel you. After that last section, you want out. Even after 18 years in email, I *still* don’t enjoy authentication.

## Do you really need authentication?

Unfortunately you do really need authentication if you want to reach the inbox. In case you missed it earlier, it’s now **required by major mailbox providers.**  
  
But if you do it right, you only have to think about it sporadically, like spring cleaning. And it’ll help you avoid getting rejected at the front door to major mailbox providers like Google, Yahoo, and Microsoft.

Here’s a graph my coworker [Brian Godiksen](https://www.linkedin.com/in/bgodiksen/) shared with me, *very* clearly highlighting the impact of not properly authenticating your mail. Three domains are sending the same type of mail. Two are properly authenticated but the third is not. Open rates for all three were truckin’ along for months, until Google started sending mail from the unauthenticated domain to the spam folder.

![](https://images.squarespace-cdn.com/content/v1/660772c2f422d154e08ae5a3/ce169840-356a-4790-a99c-454b7631912a/Gmail+Open+rate+by+domain+%281%29.png?format=2500w)

A graph showing unauthenticated email going to the spam folder with Gmail, as indicated by a drop in open rates from ~55% to 5%.

Thankfully, you can see that this sender’s performance bounced back quickly once they got themselves compliant with Google and Yahoo’s new rules, but wow, what a rough couple of weeks.

## A few authentication gotchas that (hopefully) won’t getcha

Email authentication is one of the more technical aspects of email, but there are two non-technical things to keep in mind…

### You get the deliverability you deserve

Authenticating your mail allows mailbox providers to more easily tell you apart from all the other senders out there, even if you’re sending from shared IPs. Which means if any of your email practices are less-than-best, you might have more trouble reaching the inbox than you used to. And switching IPs or ESPs won’t help either since a domain-based bad reputation can follow you around like a shadow.

### You can’t set and forget it completely

Authentication records don’t need to change often but they might need your attention from time to time. The good news? You’ll notice any issues quickly because your delivery and/or open rates will start dropping, Mailbox providers who care about authentication *really* care about it, so your delivery patterns will change. Be sure to monitor your metrics at the destination level (e.g. Gmail vs Hotmail vs Yahoo, etc)

A few example issues you might encounter:

- **Records Gone Missing:** Your IT team removed some records because they didn’t know you still needed ‘em.
- **Incorrect Records:** Your product or IT team did a database refresh or new product release that deleted your sending domain’s DNS records by mistake. When they add them back, they forget one of the characters at the end.
- **Bloated SPF Records** - If your SPF record on one domain gets too crowded with different suppliers (like your ESP, CRM platform, that *other* ESP, or support ticketing service), it can exceed the 10 DNS lookup limit, leading to delivery issues. If you’re sending multiple, unrelated types of mail, consider how you can use subdomains for each —welcome programs, marketing newsletters, transactional emails, sales emails, etc. This’ll help you keep everything neatly segmented and authenticated properly.

## We made it to the end!

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/1hI6RMzoejy0w4dt0j?wmode=opaque" width="480" height="480"></iframe>

[via GIPHY](https://giphy.com/gifs/1hI6RMzoejy0w4dt0j)

Let the celebration begin! This lesson is over, mostly...

Email authentication is an ice cream headache in the making. No two ways about it. And it needs your full attention when you’ve been tasked with setting it up or solving a problem. **Contact your ESP or IT team** if you need help, or ask me! I won’t help you myself because, well, I dislike authentication and you can’t make me. But I know a lot of folks who love it and are more than happy to help out. **Just reply to this email** and we’ll get your issue sorted out (quickly).

### Resources to help you learn more about authentication:

I’ve mentioned this is technical, yeah? Hopefully you’ve gotten enough to know what this stuff is, why it’s important, and when you need to think about it… ***and nothing more.*** It’s summer, and this newsletter is meant to be fun, not torture.

Here are a few resources if you ***do*** need to set up or troubleshoot authentication, starting with a few lols (authentication-related, of course…you’ve been forewarned).

- Here’s what email folks including Alison Gootee, Michael Hammer, Al Iverson, Travis Hazlewood, and more had to say when [we chatted about this on LinkedIn](https://www.linkedin.com/posts/lauren-meyer-emailgeek_email-emailmarketing-authentication-activity-7214355226596716544-6Wfg). Got something to add about email authentication? Jump in on the convo!
- Wanna go a level deeper than I did in today’s lesson, but not sooo deep that your brain freezes solid? I’ve worked with my team at SocketLabs to create full blogs on how [SPF](https://www.socketlabs.com/blog/spf-email-authentication/) and [DKIM](https://www.socketlabs.com/blog/what-is-dkim/) work, and a few on DMARC: an [intro to the basics](https://www.socketlabs.com/blog/dmarc-your-calendar-using-dmarc-ahead-of-google-and-yahoo-changes/) and [how to create and publish a DMARC record](https://www.socketlabs.com/blog/how-to-create-and-publish-a-dmarc-record/).
- Game for *a* *little* mental exercise? I did an even [deeper dive into authentication](https://blog.kickbox.com/all-about-email-authentication/?utm_source=senditright&utm_medium=blog&utm_campaign=authentication) with Matthew Vernhout (founder of emailKarma) that gets into some of the technicalities of how these authentication protocols work and how to set them up. It has a pretty robust set of FAQs as well, so check it out if you have a specific question I didn’t answer. Or, you know, just reply to this email and let me know!
- Google Postmaster tools (GPT) has a compliance dashboard to tell you how you’re faring, although buyer (well, free user) beware, it’s been a bit…buggy lately. Take your results with a grain of salt or two. My buddy Brian wrote a blog that I found super helpful in [making the most out of GPT](https://www.socketlabs.com/blog/google-postmaster-tools/).
- Steve Atkins from Word to the Wise (WttW) created a tool called [AboutMy.Email](https://aboutmy.email/). Send an email to it and get a full rundown of how your email is faring, authentication and configuration-wise. WttW’s created a whole set of wiseTools allowing you to check and minimize published SPF records, check DKIM keys and records, check your DMARC policy, and a whole lot more. It’s on my list of [tools for sending it right](https://send-it-right.com/tools-for-sending-it-right).
- My company's actually hosting a watch party on July 31st where my super smart email pals [Seth Blank](https://www.linkedin.com/in/sethblank/) and [Brian Godiksen](https://www.linkedin.com/in/bgodiksen/) will walk us through what DMARC is, why it matters, and how to do it (without breaking your brain, or your email deliverability).

Reach out with any questions so I can update this blog to be more clear…perhaps we’ll tackle ‘em in our DMARC watch party, too! You bring the popcorn though…it’s a virtual party. 🍿

Until next time, happy sending! 💌
