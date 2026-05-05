---
type: Web
authors: '[[Lauren Meyer]]'
url: >-
  https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/?utm_campaign=sender_reputation&utm_medium=blog&utm_source=senditright
published: 2023-12-15T00:00:00.000Z
created: 2026-05-04T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
---


<iframe frameborder="0" title="Submit HubSpot product feedback" src="https://app.hubspot.com/feedback-web-fetcher"></iframe>

[![SocketLabs Logo](https://www.socketlabs.com/wp-content/uploads/2024/04/logo-dark.svg)](https://www.socketlabs.com/)

## First 2024 Priority: Meeting Google and Yahoo Email Standards

When do mailbox providers’ preferences become less of a best practice and more of a better-do-this-or-else practice? We found out recently Google and Yahoo email standards are changing when they announced they’ll require senders to follow a set of security protocols to even be admitted entrance to their users’ inboxes.

Since this is a broad topic and one with many different applications and things to know, we’re starting a quick series to get everyone involved up-to-date, ready, and compliant when the time comes in February 2024…and the clock is running out.

First up is everything you need to know. From what’s happening to why and when, we’ll walk you through the basics of their requirements and what this means for email at large.

## What Do the Announcements Say?

Let’s jump right into the 411. Here is [what Google had to say](https://support.google.com/mail/answer/81126) and here is [Yahoo’s](https://blog.postmaster.yahooinc.com/post/730172167494483968/more-secure-less-spam) spin. These lockstep announcements raise the bar for email authentication and general message security requirements for mail. You’ll notice the similarities and what looks like an overall, more official shift in our community to stricter standards for email.

But we should also read between the lines. Here’s what they’re really saying to senders: Cut down on the amount of spam reaching our users’ inboxes.

And they’re putting the onus on senders to send less spam, period.

## Why Now and What Next?

One of these questions is perhaps a little easier to answer than the other. Let’s start with the easier one.

Looking at the requirements, it’s pretty safe to say this is going to be the new standard for email across the board. After all, when two of the largest mailbox providers (MBPs) are raising the bar on bulk sender practices, you should assume other MBPs will follow suit. Our recommendation is to be proactive with any changes you make to your email program, applying those changes to all MBPs, not just Gmail and Yahoo.

But why now? Our guess is because now, after years of having what felt like unlimited data space for users, that space is getting crowded…and pricey for MBPs to maintain. Where is lots of that data? Sitting in spam. If they can reduce the amount of spam they need to process and store, they reduce data costs. Hey, who can blame them?

Another interesting consideration could be the fact we’re walking into another election year in the United States. Political mail’s placement in Gmail inboxes [became a hot topic](https://www.politico.com/news/2022/08/11/google-program-spam-filters-00051096), so could it be Gmail is looking to get ahead of the nonsense and make their delivery standards very clear? It seems possible.

## What is Required to Meet Google and Yahoo Email Standards?

Like we mentioned earlier, this blog is more about broad strokes than it is about fine-tuning. In our next blog, we’ll walk through the actual technical requirements, including how to implement everything, so you can make sure you’re ready to roll.

For now, here’s the general rundown of what these mandated Google and Yahoo email standards require you to do for your email to be delivered to their mailboxes.

### SPF and DKIM records

Your mail needs to have some kind of security confirmation before Google and Yahoo will deliver it. So, obviously, you need to have the basics in place. This means [SPF](https://www.socketlabs.com/blog/spf-email-authentication/) and [DKIM](https://www.socketlabs.com/blog/what-is-dkim/) authentication is not a nice-to-have and the more security to bake into your records, the better.

### All sending domains must have a DMARC record present

If you want to reach the inbox at Gmail and Yahoo, DMARC needs to be in your authentication mix. The good news is you don’t have to set your DMARC policy to a level of enforcement (p=quarantine or p=reject), which takes more time and expertise to execute without hiccups in delivery. Instead, you just need to have a DMARC record present on either your organizational domain (your company’s website) or directly on your sending domain, and it can be set to p=none. You don’t even need to specify an email address for where you want to receive reports during the setup process—although we highly recommend you do.

### The domain in the sender’s From: header must be aligned with either the SPF domain or the DKIM domain

Essentially, recipient systems are looking for alignment of the from address and the sending domain. This is required to pass DMARC alignment. So, while all messages to Google require some form of passing authentication starting in February, for bulk senders (defined as those more than 5,000 messages per day), some form of authentication must both pass and be aligned with the From: domain.

### Don’t impersonate Gmail by sending from @gmail.com

Come February when these requirements go into effect, Gmail will begin using a DMARC quarantine enforcement policy, where they are telling all mailbox providers who receive mail from @gmail.com addresses to send unaligned messages to…well, quarantine (aka the spam folder).

This means that any sender who is **not** Gmail and currently using an @gmail.com address will have to use a different sending domain if they want their mail delivered to the inbox instead of the spam folder. Note this doesn’t affect Google corporate domains; just @gmail.com.

While this move by Google may come as a shock to small and medium businesses who’ve been sending from Gmail addresses for years, Yahoo has actually been using a p=quarantine DMARC policy for years. So, Gmail is really just playing catching up here.

We’ve heard a wide variety of ways ESPs who support sending from Gmail addresses plan to tackle this. The primary focus for most is making it as easy as possible for their customers to continue with email business as usual, but choosing the path of least resistance might not be the ideal solution in this case.

Ultimately, senders using an @gmail.com address will have a few choices:

**1\. Keep sending from an @gmail.com address.** Some will undoubtedly do nothing until they see performance issues arise, but we never suggest waiting until you’ve spotted an issue to take action. Not only will mail go to spam, but it will also impact the reputation of the IP you’re sending from, which may mean their ESP starts snooping around (asking questions, applying rate limits, etc). While we expect Google to roll out the negative effects of this policy using a phased approach, proactivity is the name of the game here.

**2\. Register a new domain** and start building domain reputation from scratch. This is a logical and necessary step for businesses to take, and these new Google and Yahoo email standards are a great excuse to make the move, but it requires senders to go through a warmup process, even if you’re not switching IPs. Our advice is to take this fork in the road now because your email list is only going to keep growing right along with your business, however we understand it’s not for everyone.

**3\. Send from a subdomain associated with their company’s website.** This is our recommended setup even though it will require assistance from your IT team to create the subdomain and set up authentication accordingly, and you’ll also need to go through a [domain warmup process](https://www.socketlabs.com/hub/managing-warm-up/). The great thing about this approach is since the mail is coming from a domain that is already clearly associated with your brand, mailbox providers and recipients alike can have higher confidence that the mail is actually coming from you, not someone pretending to be you with a lookalike domain (e.g. socklabs.com vs socketlabs.com)… [we send email](https://www.socketlabs.com/blog/we-send-email/), not socks.

**4\. Send from their ESP’s shared domain.** In this scenario, the ESP would rewrite the from address for their senders, for example: changing a sender address such as coffeejoescafe@gmail.com to something like coffeejoescafe@UID.espdomain.com. This is a solid option, and one we think most ESPs (and their senders) will adopt due to it being a fairly reliable way to provide email delivery while limiting the involvement required by customers to make changes to their configuration. But be forewarned here, senders using an ESP’s shared domain are also sharing sender reputation, which can lead to deliverability problems “in the neighborhood” if the ESP’s [new customer vetting process](https://www.socketlabs.com/blog/how-to-conduct-an-email-customer-vetting-with-example-questions/?utm_source=blog&utm_medium=MBP_reqs&utm_campaign=customer_vetting) and compliance policies allow for spammy activity.

### Spam rates reported in Postmaster Tools must remain below 0.3%

It’s a widely accepted fact that spam complaints have a large impact on deliverability, but Gmail has made their expectations much clearer, requiring senders who send more than 5,000 messages per day to Gmail accounts to, “Keep spam rates reported in Postmaster Tools below 0.10% and avoid ever reaching a spam rate of 0.30% or higher.”

Let’s be safe in saying, though, volume will be determined by an algorithm so if you’re [anywhere near that 5,000 mark](https://support.google.com/a/answer/14229414?hl=en#zippy=%2Cwhat-is-a-bulk-sender), resist the urge to start bean counting your sending volumes and spam complaints, and just follow go their guidance. Your time and energy will be better-spent finding ways to maintain low complaint rates through delivering a positive email experience for your recipients.

This shouldn’t be a surprise to any ESP or really, to any sender, but it bears mentioning. You absolutely need to keep spam under control. That 0.3% figure should be viewed as your absolute ceiling on complaints, not a limbo bar you barely slide right under. As a sender, this should be something you’re always looking at because it has a direct impact on performance, and as an ESP you need to be diligent in monitoring and responding to spam-monsters.

### Sending domains and/or IPs must have valid forward and reverse DNS records (PTR records)

What is a PTR record? It stands for DNS pointer record (PTR for short), and it verifies the host or domain name associated with an IP. It’s the exact opposite of an A record, which tells you the IP address associated with a host or domain name. By pointing these two records at each other, mailbox providers can better identify you as a sender and have higher confidence your mail is legitimate.

While SocketLabs has always carried proper PTR records, not every mail server does, so you will want to check with your ESP or IT team to ensure you’re now adhering to this necessity.

Are you reading this from your chair in the IT department and you aren’t sure what we mean? Don’t worry, our next blog is specifically for you, so stay tuned.

### Messages must be formatted according to the Internet Message Format standard (RFC 5322)

RFC 5322 sounds pretty techy but it really only dictates proper email formatting. Since we’re talking about Google specifically, [here’s some info straight from them](https://support.google.com/a/answer/13567860?hl=en#:~:text=RFC%205322%20is%20an%20Internet,that%20send%20automated%20email%20messages.).

Most modern development libraries for email are pretty good about building complaint messages these days, so issues with this requirement should be rare. Though it should be said: Never consider anything a no-brainer. Ask for verification or check yourself because it’s better to be safe than sorry.

### Marketing messages and subscribed messages must support one-click unsubscribe

Before you raise your eyebrows or start worrying about major list churn, keep in mind that the primary goals of every mailbox provider are to protect their users from harm and to deliver a fantastic email experience. With this in mind, new Gmail and Yahoo email standards will require senders to make it easier for their recipients to unsubscribe by offering two ways to get off the ride:

**1\. Including a clearly visible unsubscribe link in the body of the email.** This has been required under CAN-SPAM legislation in the US for 20 years, so should not be new to literally anyone sending email, but it’s always good to be reminded. The good news is this unsubscribe link can still point to a preference center, allowing subscribers to *reduce* the amount or types of email they receive instead of churning from your list(s) completely.

**2\. Ensuring every marketing message offers the ability to unsubscribe with just one click.**  
In this case, the mechanism to unsubscribe lives within the headers of the email, allowing for an unsubscribe option to appear right next to the sender address within the recipient’s mailbox client when they open a message. In just one click, a person can be done. No preference centers, no need to type or confirm your email address. Just one click and voila! You’re off the list. Senders must honor these requests within two days, which is quite a step up from the 10-day window for processing unsub requests granted by loosey-goosey CAN-SPAM. The good news here is most reputable ESPs (like SocketLabs) will handle this requirement for you. Note, though, you need to have a decent sender reputation for Gmail to populate this option for you.

While neither of these providers has outright said this requirement will change the way spam complaints affect inbox placement, making it easier for recipients to unsubscribe from brands they trust will make it even clearer that there’s a problem when a sender’s spam complaints remain elevated. As a result, it’s possible we’ll see spam complaints have an even heavier influence on sender reputation and inbox placement than it has today.

## You’re Primed for New Google and Yahoo Email Standards

With that, you have the lay of the land. Really though, the new requirements boil down to a very simple takeaway.

Today’s bare minimum will not be the bare minimum of tomorrow and you need to ensure you’re prioritizing mailbox provider needs above your own, because even if you’re meeting the legal requirements (sigh, [CAN-SPAM](https://www.socketlabs.com/blog/transactional-email-can-spam/)), it doesn’t mean you’ll be placed in the inbox.

Does making changes to your email configuration take some care? Of course. But if you want to deliver mail to Gmail and Yahoo, you better do it. The same thought process should apply to anything contributing to the evolution of email.

If you need some more help decoding what these new requirements mean to you, let us know and we’ll set up a [free consultation](https://www.socketlabs.com/contact/). We can help you make sense of your next steps, both technical and strategic, so you can meet Google and Yahoo email standards without the anxiety of going it alone.

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

<iframe src="https://app.hubspot.com/conversations-visitor/5046138/threads/utk/5b87021ced534e6daddcd4ece4a79338?uuid=2e788427538b4a2a81f3913ba201ce9b&amp;mobile=false&amp;mobileSafari=false&amp;hideWelcomeMessage=false&amp;hstc=257878996.4da0b1781cb81675ca8efdc70ed69fd3.1777900698379.1777900698379.1777900698379.1&amp;domain=socketlabs.com&amp;inApp53=false&amp;messagesUtk=5b87021ced534e6daddcd4ece4a79338&amp;url=https%3A%2F%2Fwww.socketlabs.com%2Fblog%2Ffirst-2024-priority-meeting-google-and-yahoo-email-standards%2F%3Futm_campaign%3Dsender_reputation%26utm_medium%3Dblog%26utm_source%3Dsenditright&amp;inline=false&amp;isFullscreen=false&amp;globalCookieOptOut=&amp;isFirstVisitorSession=true&amp;isAttachmentDisabled=false&amp;isInitialInputFocusDisabled=false&amp;enableWidgetCookieBanner=false&amp;isInCMS=false&amp;hideScrollToButton=true&amp;isIOSMobile=false&amp;hubspotUtk=4da0b1781cb81675ca8efdc70ed69fd3" title="Widżet czatu" allowfullscreen=""></iframe>
