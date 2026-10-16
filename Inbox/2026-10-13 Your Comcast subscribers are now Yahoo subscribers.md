---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/your-comcast-subscribers-are-now-yahoo-subscribers-and-nobody-told-you?utm_medium=email&_hsenc=p2ANqtz-8tUWC88ROB0wZsDk2U2-ePPQIs0aWkK6tgSOVd4w0A20ci78uPv1zbIZlUUjof6SHDpbweupASK9YI5SS6Db9QE3L9akS0TSTisxhZuA9BnCIMOA4&_hsmi=100685374690&utm_content=148103566&utm_source=hs_email"
published: 2026-10-13
created: 2026-10-16
tags:
---


If you send to US consumers, a chunk of your list has moved from one filtering regime to another and you will not have seen it happen.

Comcast started migrating comcast.net mailboxes to Yahoo Mail in June 2025, in phases, running through 2026. Users keep their @comcast.net addresses, their mail and their contacts. What changes is the infrastructure behind the address, and with it, whose filters decide whether you reach the inbox.

So the address on your list says Comcast. The thing deciding your fate is Yahoo.

## What happened

## The migration, and why it is invisible to senders

- It started in June 2025 and rolls through 2026. User by user, in waves, with each customer invited to upgrade and given notice. A gradual migration rather than a cutover.
- Addresses do not change. Somebody on your list at an @comcast.net address stays at that address. Nothing in your database updates, because nothing about the contact has changed.
- Access and filtering move to Yahoo. Mail is accessed through Yahoo Mail, and Yahoo's filtering, thresholds and engagement weighting apply.
- And the MX records have not caught up. The comcast.net MX records still point at Comcast-operated hosts, which means the migration is reaching users before senders can see it in DNS.

That last point is the reason nobody noticed. The usual way to detect this sort of change is to look at where the domain's mail is being routed, and the routing still looks like Comcast. The users are already somewhere else.

## What changes

## Yahoo filters differently, and your old benchmarks do not transfer

- Engagement weighting gets harsher. Yahoo's inboxing is heavily engagement-led, so dormant comcast.net addresses that were quietly tolerated before now count against you properly.
- Domain reputation leads. Yahoo made a significant change in April 2025 toward assessing the reputation of the From domain rather than relying primarily on IP, which is the regime your Comcast contacts have just joined.
- The complaint ceiling is Yahoo's. Bulk senders are expected to stay under 0.3%, and the error codes you see when you breach it will be Yahoo's rather than Comcast's. Expect TS03 and TS04 responses if your complaint rate is high.
- Promotional and affiliate-heavy sending is treated more strictly. Yahoo has been noticeably tougher on senders leaning hard on promotions or mailing unengaged audiences.
- Forwarding stops. Anybody who was forwarding their Comcast mail elsewhere loses that arrangement after migration, which produces behaviour changes you will see in your data without an obvious cause.

### What you will see in your reporting

- Bounce spikes on comcast.net during switchover windows. Particularly where somebody has not completed the transition or has not updated settings in a third-party client.
- Open rates shifting without a campaign change. Different filtering, different placement, different numbers. Not necessarily a problem with your email.
- Comcast and Yahoo performance converging over time. Which is the clearest sign the migration has reached your audience.
- And a comcast.net column in your provider report that has stopped meaning what it meant. Because it is now a mix of migrated and unmigrated users behaving in two different ways.

## What to do

## Four things, none of them difficult

1. Re-map your provider reporting by infrastructure, not by domain. Count comcast.net alongside Yahoo, aol.com and the rest of the Yahoo estate, because that is whose filters they sit behind. The same applies to att.net and sbcglobal.net, which have been routing through Yahoo infrastructure for some time.
2. Stop benchmarking comcast.net against its own history. Your pre-2025 Comcast numbers were produced under different filtering. Comparing this quarter against two years ago is comparing two different systems.
3. Clean the dormant comcast.net addresses. Yahoo punishes dormant recipients harder than Comcast did, so inactive contacts that were sitting there harmlessly are now a liability. The single highest-value action on this list.
4. Watch bounces on that domain more closely than usual. Through the remainder of the migration, because the switchover windows produce temporary failures that look like data quality problems and are not.

## The conclusion

Nothing in this post requires a project. It requires knowing that a chunk of your list changed filtering regime without changing address, and adjusting your reporting and your list hygiene to match.

What it illustrates is the more useful lesson. Your provider breakdown is a reflection of what the address says, and the address is not always a reliable guide to whose rules apply. Infrastructure moves underneath senders regularly, quietly, and without anybody sending you a note about it.

Which is why watching your numbers by provider, as a trend, is worth the fifteen minutes a week it takes. You would have spotted this in your own data long before anybody wrote an article about it.

### Further reading from The Vault:

- [How to Know Your Sender Reputation](https://weareastral.co.uk/thevault/how-to-know-your-sender-reputation.-why-you-cannot-look-it-up-any-more-and-how-to-work-it-out-instead)
- [How to Build an Email Early Warning System](https://weareastral.co.uk/thevault/how-to-build-an-email-early-warning-system-so-you-find-out-before-it-costs-you)
- [Email List Churn: What's Normal, and What Isn't](https://weareastral.co.uk/thevault/email-list-churn-whats-normal-and-what-isnt-and-when-should-you-stop-emailing-someone)
- [The State of Email Deliverability in 2026](https://weareastral.co.uk/thevault/the-state-of-email-deliverability-in-2026.-and-what-i-think-happens-in-2027)
- [Email Behaving Badly: Why Compliance Will Not Save Your Deliverability](https://weareastral.co.uk/thevault/email-behaving-badly-why-compliance-will-not-save-your-deliverability)
- [Black Friday 2026: What Not to Do](https://weareastral.co.uk/thevault/black-friday-2026-what-not-to-do-how-to-prep-your-deliverability-and-what-to-send)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.