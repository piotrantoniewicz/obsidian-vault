---
type: Web
authors: '[[Lauren Meyer]]'
url: >-
  https://www.socketlabs.com/blog/webinar-recap-everything-you-really-need-to-know-about-dmarc-ft-valimail/?utm_campaign=deliverability_rate&utm_medium=blog&utm_source=senditright
published: 2024-08-07T00:00:00.000Z
created: 2026-04-27T00:00:00.000Z
tags:
  - digital-campaigning
  - automatyzacja
---


<iframe frameborder="0" title="Submit HubSpot product feedback" src="https://app.hubspot.com/feedback-web-fetcher"></iframe>

[![SocketLabs Logo](https://www.socketlabs.com/wp-content/uploads/2024/04/logo-dark.svg)](https://www.socketlabs.com/)

![](https://www.socketlabs.com/wp-content/uploads/2024/08/DMARC-Webinar-Blog.png)

All eyes have been on DMARC since [Google](https://support.google.com/mail/answer/81126) and [Yahoo](https://blog.postmaster.yahooinc.com/post/730172167494483968/more-secure-less-spam) [announced](https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/) their intention to require DMARC on all mail in late 2023. Six months past when those rules went into effect (in February 2024), we’re now noticing higher levels of enforcement within our data, suggesting the grace period for senders late to the game is approaching a close.

It’s time for bulk senders to truly get serious about implementing DMARC if they haven’t yet, and making sure the DMARC record applied on the mail is working appropriately.

The biggest problem is: DMARC is hard! Like, really hard! Not only is it a complex thing to understand, it’s an even more confusing thing to monitor. That’s why we linked up with our friend Seth Blank, Chief Technology Officer at Valimail to explain what you need to know.

Below you’ll find a full webinar recording of Brian Godiksen, SocketLabs’ Director of Customer Solutions, and Seth discussing the current state of DMARC: what it is, how to use it, why you *need* to use it, and what tools are available to help you succeed. The session was moderated by Lauren Meyer, chief marketing officer at SocketLabs.

We’ll also give you a breakdown of the conversation in a “greatest hits” blog under the list of video highlights, complete with clips and takeaways you can refer back to.

Let’s jump in!

<iframe title="Valimail DMARC webinar (final)" src="https://player.vimeo.com/video/980879637?h=25f8824986&amp;dnt=1&amp;app_id=122963" width="800" height="450" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write"></iframe>

## Overview & Fast Takeaways

### What is DMARC?

DMARC stands for “Domain-based message authentication, reporting, and conformance.”

It’s designed to look for aligned email authentication standards and then tells the mailbox provider receiving the mail what to do with it.

So, if the mail passes authentication checks (like SPF and DKIM), the DMARC record will instruct the receiver to deliver the mail. If the mail does not pass authentication, the DMARC policy will then indicate what should happen next.

### What DMARC Policies are Available?

There are three policies.

1. **P=none** tells the MBP to do whatever they choose to do with the mail if it fails, because the policy is just meant to observe what is and is not passing authentication. If your DMARC policy includes an email address where you can receive reports, you’ll be alerted when authenticate checks fail.
2. **P=quarantine** instructs the provider to accept the mail into their servers, but keep it away from the inbox. So, potentially a spam folder or other quarantined area of recipients’ mailboxes.
3. **P=reject** is the strictest policy, where the sender is instructing the MBP outright reject any email failing authentication.

While the domain owner is the one who sets the DMARC policy, it’s important to note that MBPs are the ones who ultimately decide what gets delivered to recipient inboxes. If they feel the mail is wanted by the recipient (based on past behavior), they have been known to override the DMARC policy in an effort to do what they think is best for their users.

So, think of your DMARC policy as more of a suggestion from senders to MBPs than a mandate that will be carried out each and every time.

### What are the Benefits of DMARC?

We’ll let the experts take this one on! The TL;DR is, “Once you have DMARC in place, you have greater control over your sender reputation.”

<iframe title="Valimail webinar: Benefits of DMARC" src="https://player.vimeo.com/video/995577864?h=d7d52bb056&amp;dnt=1&amp;app_id=122963" width="800" height="450" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write"></iframe>

Don’t forget, though: The security benefit of DMARC really only begins when you’re at a level of enforcement.

If you’re only using p=none, you are simply monitoring and not taking any action when authentication fails. Giving yourself a better opportunity to catch an issue via a report, is great, but your goal should be actively instructing MBPs to quarantine or bounce unauthorized mail.

### Why is DMARC Required Now?

The overall goal is to increase the security of the entire email ecosystem, especially after email became such a huge tool for businesses during the 2020 pandemic – that boom also came with a boom of malicious email attackers. So, Google and Yahoo’s DMARC requirement is a great step toward better protecting both senders and users.

We should note, while this is only firmly required by major mailbox for bulk senders distributing at least 5,000 emails per day we recommend DMARC for everyone because of the benefits mentioned earlier.

**DMARC Adoption Rates**

Seth pulled some cool facts to illustrate the impact of the DMARC requirement on the email ecosystem:

- DMARC adoption grew 55% between January 1 and March 31, 2024.
- 75% of domains using DMARC are at p=none without any reporting.
- This is a bad idea! You always want to know if you have gaps in security so you can close them ASAP.
- Only 3% of domains with a DMARC policy are at enforcement.
![](https://www.socketlabs.com/wp-content/uploads/2024/08/Copy-of-Valimail-DMARC-webinar-wide.png)

### What Happens Without DMARC Now?

Before, the risk of not using DMARC or having improperly (or missing) authentication was more about protecting reputation and reducing risk. Senders without a DMARC policy at a level of enforcement are at greater risk of being compromised, and as such, at a greater risk for reputation damage and deliverability issues.

At Google and Yahoo, they’ll simply stop delivering mail without DMARC. Period.

Seth and Brian shared a graph looking at a dedicated IP’s reputation at Google Postmaster Tools (GPT) from January to nearly May 2024. When DMARC wasn’t required and they did not have it in place, they had a good reputation until the requirement was enforced. The IP’s reputation quickly dropped from good to poor upon Google’s enforcement of DMARC, meaning they likely also saw some serious delivery issues during that period. When they realized what was happening, they implemented DMARC on April 3. Within 30 days, the reputation improved from poor to good.

![](https://www.socketlabs.com/wp-content/uploads/2024/08/Copy-of-Valimail-DMARC-webinar-wide-1.png)

The damage is real, but quick recovery is possible. The key is to make sure you’re paying attention to your reputation to detect problems quickly so you can solve immediately.

### How Do You Read DMARC Reports?

As they mentioned, DMARC reports are XML and that’s meant for computers, not humans. You’ll also get them from up to hundreds of places, so they can become overwhelming pretty quickly.

However, it’s extremely important for you to look at and understand your reports to know whether messages from your domain pass DMARC.

In general, though, these are the three most important things you can get from your reports:

1. The number of messages sent from a single IP address for the report time period
2. The SPF, DKIM, and DMARC authentication results for the messages
3. Any actions taken by the receiving server (aka the MBP), for example accepting unauthenticated messages because they passed ARC authentication

We highly recommend using a third-party service like Valimail to help you manage your XML reports so what you’re analyzing looks more like that pretty little summary on the left, instead of trying to interpret a message like the one on the left for each and every failure (yuck!).

![](https://www.socketlabs.com/wp-content/uploads/2024/08/Sending-Overview-3.png)

### How Do You Monitor DMARC Compliance?

You have a few options to help you understand how your DMARC is working. Google developed a [compliance page in GPT](https://www.socketlabs.com/blog/google-postmaster-tools/) to make this super easy.

![](https://www.socketlabs.com/wp-content/uploads/2024/08/7.png)

And generally, you can monitor your reputation at Google and Yahoo using something like SocketLabs Spotlight or simply by using GPT.

If you notice you have issues and you know you don’t use DMARC, surprise! You’re suffering the consequences. If you have issues but you thought your DMARC was solid, and you can’t identify other things that may be causing a slip in your reputation, you might want to consider a service like Valimail to help you sort everything out.

SocketLabs customers have a quick way to monitor your authentication status and your reputation (via StreamScore) all in the same place.

![](https://www.socketlabs.com/wp-content/uploads/2024/08/Webinar-Presentation-Slides-1.png)

### I Need DMARC Help.

You are far from alone! DMARC is difficult and there are a bunch of resources out there to help you.

We highly recommend starting your journey at Valimail, where they have a ton of free resources to guide you as far as you feel comfortable going on your own.

When you’re ready to monitor your overall authentication and its impact on your performance, or if you need a quick and simple solution to set up your DKIM and SPF because that’s where your DMARC problems really live, SocketLabs makes authenticating a step-by-step guided process to take all the guesswork out.

Whatever your needs may be, [reach out to us](https://www.socketlabs.com/contact/) and we can help you find the solution you need.

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

<iframe src="https://app.hubspot.com/conversations-visitor/5046138/threads/utk/388a311f2200472baee7f2199bb28317?uuid=dade93f5baaa4ad4a47751b8e85037b4&amp;mobile=false&amp;mobileSafari=false&amp;hideWelcomeMessage=false&amp;hstc=257878996.5f7a8dac7988abbddb7c85a8820f7202.1777314367729.1777314367729.1777314367729.1&amp;domain=socketlabs.com&amp;inApp53=false&amp;messagesUtk=388a311f2200472baee7f2199bb28317&amp;url=https%3A%2F%2Fwww.socketlabs.com%2Fblog%2Fwebinar-recap-everything-you-really-need-to-know-about-dmarc-ft-valimail%2F%3Futm_campaign%3Ddeliverability_rate%26utm_medium%3Dblog%26utm_source%3Dsenditright&amp;inline=false&amp;isFullscreen=false&amp;globalCookieOptOut=&amp;isFirstVisitorSession=true&amp;isAttachmentDisabled=false&amp;isInitialInputFocusDisabled=false&amp;enableWidgetCookieBanner=false&amp;isInCMS=false&amp;hideScrollToButton=true&amp;isIOSMobile=false&amp;hubspotUtk=5f7a8dac7988abbddb7c85a8820f7202" title="Widżet czatu" allowfullscreen=""></iframe>
