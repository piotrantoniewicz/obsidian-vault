---
type: Web
authors: '[[Lauren Meyer]]'
url: 'https://send-it-right.com/blog/what-to-do-with-deliverability-issues'
published: 2024-06-27T00:00:00.000Z
created: 2026-04-24T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
  - content-marketing
---


Ever wondered if your emails are making it to the inbox? You’re not alone. I’ve had countless conversations over the years with senders who thought they had a deliverability issue, only to discover it was actually something content-related. Imagine having high delivery and open rates but clicks and conversions are waning — frustrating, right?

On the flip side, I’ve also worked with senders who were blissfully unaware that their emails were landing in the spam folder or being delayed…that is, until a customer complained. And then a flood of customers complained. They didn’t notice it because their delivery rate (which they had confused with their deliverability rate) looked normal.

Today, let’s dig into what to do when you think you’ve got a problem reaching the inbox. How might you notice it, what’s likely causing it, and most importantly, how you can respond and bounce back gracefully.

So, first things first…

## How you’ll notice a deliverability issue

- **Reduction in performance:** Follow the trends, my friends! It’s ok to see a blip or two, but when something looks out of place, take a closer look. For example, you might notice lower engagement within your ESP metrics ([opens](https://www.socketlabs.com/blog/email-performance-red-flags-low-open-rates/?utm_source=senditright&utm_medium=blog&utm_campaign=spam_issues), clicks) or campaign performance (conversions, revenue). Figure, *most* people aren’t gonna open, click, *or* convert if your mail’s snoozin’ in their spam folder…they won’t even see it.
- **Reports from recipients:** Ok, fine, your marketing mail is *that* amazing and customers **do** complain when it goes missing. Or it was a transactional piece of mail they were expecting (and furiously refreshing their inboxes for) such as a password reset or movie tickets and they reached out to your support team asking “WTF?” before realizing it was chillin’ like an email villain in their spam folder.
- **Compliance investigation:** If you’re generating high bounces, [unsubscribes](https://www.socketlabs.com/blog/email-performance-red-flags-high-unsubscribe-rate/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues), or [spam complaint rates](https://www.socketlabs.com/blog/email-performance-red-flags-spam-complaints/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues), it could trigger your ESP's compliance team to be the ones asking “WTF?” as they’re restricting your sending to investigate. Before you reach this point though, you might notice your complaint rates are sometimes elevated above 0.03% or there are spikes from time to time.
- **Alerts from your ESP or a 3rd party monitoring tool:** Depending on the email platform you’re sending from, you might get alerts within your ESP's dashboard or a third-party tool about changes in your sender reputation, authentication failures, blocklists they’ve found you on, or bounces that mean something very specific (such as “messages from this domain have been flagged as spam"). Some of these alerts are automated, others might just be a friendly tap on the shoulder from your ESP’s support team who is *the next* one asking “WTF?” (politely, of course…support folks are some of the kindest, most patient people I know 💌).

Okaaaay, so you know you’ve got an issue. Great…but what ***(******TF!!!******)*** caused it?

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/wa9cjJWGekfEuNcEuL?wmode=opaque" width="480" height="320"></iframe>

[via GIPHY](https://giphy.com/gifs/wa9cjJWGekfEuNcEuL)

Linda's gettin' a little verklempt about her deliverability. Let's discuss.

## Common Reasons Senders Face Deliverability Issues

Enough with the heartburn! Let’s talk about why you might be having an issue. Here are the most common reasons:

1. **Data quality:** Sending to people who aren’t expecting to hear from you — either because they didn’t sign up or because it’s been so long, they forgot you exist — is gonna lead to issues…like, **people marking your emails as spam**, which can be murder for inbox placement. You want a list full of highly engaged recipients who are receptive to communications with your brand… maybe even jazzed about ‘em! Collect it right so you can start sending it right.
2. **Subscriber management:** Even if someone has signed up for your emails, they can still mark ‘em as spam faster than you can say “green eggs and ham”. Be consistent with how you manage your list between the point of signup and when someone’s removed.
3. **Tunnel vision:** If you’re only focused on optimizing your content for opens and clicks, you might not realize those engagements never lead to conversions (however you’re defining conversion). Or you might notice that people open, but then quickly unsubscribe or mark your email as spam once they’ve gotten their one-time use coupon code. **Consider the bigger picture** (data collection, content strategy, targeting) to ensure you’re using the right lead magnets to bring the right people to your signup form. Properly set expectations about what they’ll get from you and how often. And look at your performance metrics over time so you can send content that the data supports they engage with and seem to find value in. **Make it easy for them to get off the ride if they wish**, too. If not, they *will* mark your emails as spam.
4. **Business as usual:** Outdated practices like weak signup forms that aren’t protected against bot signups, or neglecting to collect a signup at all, simply because it’s the way it’s always been done is…silly. And dangerous to deliverability. Email is a data-rich channel, so put that data to use, my friend! Figure out what’s putting your email performance at risk and take baby steps towards fixing it. Like, today! One small step at a time.
5. **Skipping fundamental steps:** Some things that were considered a nice-to-have in the past are now required by major mailbox providers like Google and Yahoo. Not properly authenticating your sending domain (with [SPF](https://www.socketlabs.com/blog/spf-email-authentication/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues), [DKIM](https://www.socketlabs.com/blog/what-is-dkim/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues), [DMARC](https://www.socketlabs.com/blog/dmarc-your-calendar-using-dmarc-ahead-of-google-and-yahoo-changes/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues)) or skipping warmup on your domains or IPs is like showing up late to class without even having an excuse like “my dog ate my homework”. Not the ideal way to start the semester, and definitely not the way to reach the inbox with consistency.

## Reacting to Deliverability Issues

When something comes up, take a goooood look around…including in the mirror, friend. The problem is oftentimes something within your control. Whether that thing is easy to fix or not is an entirely different story. But we’ll get into that another day.

For now, let’s discuss the order of operations when you find a problem.

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/b0ELsIT6zlraBhvcEe?wmode=opaque" width="480" height="348"></iframe>

[via GIPHY](https://giphy.com/gifs/b0ELsIT6zlraBhvcEe)

Linda's not intimidated by deliverability issues; you shouldn't be either!

**Understand the impact**

- **How did you discover the issue?** We *just* talked about this! Look alive, people. Did you find it through a reduction in performance (high bounces or spam complaints, low opens or conversions), a report from a single recipient, a flood of support tickets from *many* affected recipients, or a heads up from your ESP or deliverability monitoring tool?
- **How widespread is it?** For example, is it happening only at Hotmail, or *everywhere*? If you found the issue through a reduction in performance (high bounces or spam complaints, low opens or conversions), it’s likely affecting many recipients. If the report came from a single recipient (or your CEO!) but there’s not a flood of support tickets coming from *many* affected recipients, it’s likely pretty isolated…for now. If you got a heads up (or a raised eyebrow) from either your ESP or deliverability monitoring tool, lean into the details they provide so you can nip it in the bud.
- **Is the problem still happening?** If so, don’t panic. Just get moving on answering the rest of these questions so you can solve this thing! The longer you wait to fix what’s broken, the more it will impact your [sender reputation](https://www.socketlabs.com/blog/teach-me-email-what-is-sender-reputation/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues).

**Identify the cause of your deliverability issue**

- **Where is it happening?** Every mailbox provider has their own set of rules and algorithms and spam filters to determine how each piece of mail is treated. Knowing which destinations you’re struggling with can put a spotlight on where the problem lies. For example, Google and Yahoo are incredibly domain-focused, whereas other providers are still putting more emphasis on IP reputation. Some care a lot about user complaints and hard bounces while others will give you a hard time over hitting spam traps or landing on a particular blocklist. Knowing where you’re affected can help you get closer to whyyyyy as well. It can also help you figure out if any VIP customers are affected. You’ll want to take extra special care of them.
- **When did it start?** Note, this is different than when did you notice it. Trace that lil’ dogie back to the beginning of its downward spiral by looking at your email performance data over time…go back at least a couple of days before you noticed the problem to see if anything else sticks out as odd. Keep tracking backwards until you uncover an inflection point.
- **Can you replicate it?** If not, it’s possible the issue was isolated or has already resolved, yay! If you can replicate it, the information available within the email headers or bounces might be helpful in determining the root cause of your issue. Just…ask a deliverability person or your ESP for help deciphering this stuff unless ice cream headaches are your thing.
- **Did you change anything around that time…like,** **anything**: big or tiny? New campaign or type of content, sending from a different ESP or domain, changes to your authentication (potentially caused by a new product release or an IT person who thought those DNS records were no longer needed), sending to inactive subscribers to inform them of a change to your terms of service, a new salesperson who’s trying realllly hard to close their first deal (via cold email 😢), sending to a list you found on your grandma’s hard drive from 2004… ***Anything***? Consider it all.

Once you’ve found your smoking gun(s), it’s time to…

**Take action!**

If you’ve been following along, you should have a good list of **questions** ***and answers*** **to help you figure out what to do next:**

- Confirm it was a false positive or an issue on the mailbox provider side, thank your lucky stars, and move on…but keep a close eye on it for a while, just to be sure, ok?
- Reach out to your ESP or a deliverability-minded friend (ahem, **ME**!) for help understanding what you’re seeing. Or join one of the [monthly email marketing roundtable events](https://www.socketlabs.com/roundtable/?utm_source=senditright&utm_medium=blog&utm_campaign=deliv_issues) I host for SocketLabs and get answers directly from experts in deliverability, strategy, and more. They’re a blast, and I usually walk away with at least 3 pages of notes.
- **Fix what’s wrong** once you’ve found it. Don’t back away slowly; don’t pretend you didn’t see it. Face the facts of what needs to be done next and make it happen. If you need to get buy-in or approval, check out the section in my last blog on [why businesses don’t properly invest in email](https://send-it-right.com/blog/why-email-deliverability-matters) for ideas on how to make your case quickly and effectively. (spoiler: speak in business impact and $$$!)

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/l3vRhBz4wCpJ9aEuY?wmode=opaque" width="480" height="321"></iframe>

[via GIPHY](https://giphy.com/gifs/mike-myers-coffee-talk-verklempt-l3vRhBz4wCpJ9aEuY)

Linda’s tired. You’re tired. I’m tired.

Hang in there, Linda…we’re almost there. A couple of other questions I get often…

## FAQs about Deliverability Issue Resolution

#### How long does it take to resolve a deliverability issue?

That depends on a lot of factors. Typically if you’ve been sending it right most of the time and you make a little MOPs oops, the mailbox providers and blocklist providers are forgiving. Worst case, you need to file a ticket with your ESP or the provider directly to let them know you made a mistake and have fixed it.

If you haven’t been sending it right, then it depends on how deep of a hole you’ve dug yourself into. In those cases, it can take a while…like, weeks or months in very severe cases, and you shouldn’t expect improvement until you’ve fixed what caused the issue in the first place.

Patience and persistence are your best friends here. So is following the data to understand what’s most likely driving your issue and then fixing what’s within your control: authentication, list collection, segmentation, content, you name it. Do something. Anything. Baby steps are perfectly acceptable as long as you’re moving in the right direction.

#### When should I reach out for help with an email performance issue?

If you’re sending through an ESP, your first outreach should be to their support team. They’ve handled 1000’s of tickets and have likely seen an issue similar to yours before.

But only reach out after you’ve taken that hard look in the mirror and resolved any underlying issues on your side.

When you do reach out, be clear and concise about who you are as a sender, what kind of mail you’re sending, what’s happened, and **what you want their help with.** Are you looking for more information on what’s going on, asking them to remove restrictions on your account after you generated some bad statistics, or do you need help to request mitigation from a blocklist operator or mailbox provider? The clearer (and kinder) you can be, the better.

#### Can’t I just solve my issue by sending from a different IP or ESP?

No. Ok, well maybe. For a little while. Email’s weird and sometimes you get to cruise down the freeway for a bit before you get a speeding ticket. But I wouldn’t roll those dice if I were you. Switching ESPs is a nightmare when it’s done in a rush, and trying to warmup your reputation on a new one isn’t very likely to solve your deliverability issue any faster than staying put and solving it the right way. 💌

Not to mention, mailbox providers are continually becoming more and more focused on domain reputation. In fact, the biggest ones like Google and Yahoo are now requiring you to authenticate your sending domain if you want to reach the inboxes of their users — you may have heard the term “no auth, no entry”…or anyway, now you’ll know what it means when you see it. 🙃

What this means for senders is that it’s a lot harder to hide your bad behavior than it used to be. You can’t just skip town and expect your new classmates to not find out you were called “Farty Artie” in your last school. We’re living in a digital age, folks. Word spreads, fast.

Since sender reputation is now so closely tied to your sending domain (which just so happens to be associated with your company’s website domain), and since your company’s name is gonna be all over that email, your bad (or good!) reputation follows you. There really is no escape when you have so many breadcrumbs leading directly back to your company.

TL;DR — don’t waste your time jumping from one place to another. **Just send it right!** Follow the practices you know you’re supposed to be following and when there’s a problem, (kindly) ask your ESP for help instead of jumping ship.

## Wrapping it up

Alright, folks, I’ve tried my best to explain the most common signs and causes of deliverability issues, and hopefully gave you some helpful guidance on initial steps you can take to investigate and solve ‘em. There’s a LOT more to it than I’ve described here, but in the words of my email pal [Alison Gootee](https://www.linkedin.com/in/alisongootee/), **“that’s deliverability, baby!”**

<iframe frameborder="0" allowfullscreen="" src="https://giphy.com/embed/phK5FH5IiNL4PfcWjB?wmode=opaque" width="480" height="348"></iframe>

[via GIPHY](https://giphy.com/gifs/phK5FH5IiNL4PfcWjB)

Linda's feelin' good, how 'bout you?

Until next time, happy sending! 💌

PS - Got a topic you’d like me to jump to the front of the list? [**Let me know**](https://send-it-right.com/contact) **…please! 💌**
