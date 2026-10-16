---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/italys-email-tracking-pixel-deadline-is-28-october-2026.-what-happens-to-your-open-tracking-and-what-to-do-in-the-next-three-weeks?utm_medium=email&_hsenc=p2ANqtz-9GR8z2mI2J8eF4Pe_VEbQx7VjhqMEu8QE6TbKg2jnfDRXaFfuvl0cyMh-7OgpzUwvNneqXILW1Vq1Waiaz7aiE5W4BV4lR8kv5sYZX0jPXMW-hUYM&_hsmi=100685374690&utm_content=148103566&utm_source=hs_email"
published: 2026-10-13
created: 2026-10-16
tags:
---


14 days (from right now when I posted this). That is what is left before Italy's tracking pixel rules bite, and a surprising number of businesses sending into Italy have no idea the deadline exists.

France went first, on 14 July. Italy follows on 28 October, and Italy's version has a sting in it that France's does not, because the exemption everybody is relying on almost certainly does not cover the way your email platform works.

I wrote about both regimes when the guidance landed, so take this as the deadline post, with the detail, and with the part nobody is discussing: what happens to your engagement definitions, your automations and your suppression rules when open tracking stops being available for a chunk of your list.

Worth saying clearly before anything else. I am not a lawyer and none of this is legal advice. I am an email consultant explaining what the guidance says and what it means operationally. Take proper advice on your own position, and read the source guidance rather than my summary of it.

## The rule

## What the Garante decided, and when

- 17 April 2026. Italy's data protection authority, the Garante per la protezione dei dati personali, adopted Provvedimento n. 284, its first dedicated guidelines on tracking pixels in email.
- 29 April 2026. Published in the Gazzetta Ufficiale, which started a six-month compliance window.
- 28 October 2026. The window closes. A small number of commentators read the date as 29 October, so treat 28 October as your working deadline and do not cut it fine.

The legal mechanism is the part that surprises people. The Garante has classified the tracking pixel as access to information stored on the recipient's terminal equipment, which brings it under Article 122 of the Italian Privacy Code and Article 5(3) of the ePrivacy Directive. In other words, the same legal bucket as a cookie.

Which means the default position is prior consent, and tracking without it is only permitted where a specific exemption applies.

## The exemption

## And why your platform almost certainly does not qualify for it

Italy does offer a consent-free route that France does not, and it is the reason a lot of people have decided they are fine. Read it properly and most of them are not.

### What the aggregate exemption requires

- Anonymised, aggregated open-rate statistics only. Measurement at the level of the campaign, not the individual.
- One shared pixel per campaign. Identical for every recipient of that send. Not a unique pixel per person.
- IP addresses and technical identifiers anonymised. So nothing in the request can be traced back to a person.
- No route back to an individual, at all. The standard here follows the Article 29 Working Party's Opinion 05/2014 on anonymisation techniques, which is a high bar rather than a nod toward one.

### Now look at what your ESP really does

Standard email platforms generate a unique pixel per recipient. That is how the open gets attributed to a contact record, how your engagement segments populate, and how your open-triggered automations fire.

Per-recipient tracking is, by definition, not aggregate and not anonymised. So the exemption does not cover it, and most platforms do not offer a genuine aggregate-only mode as a setting you can switch on.

Which leaves most senders with two options for Italian contacts: get consent, or turn the pixel off.

### The other exemptions

- Security and authentication. One-time passcodes, fraud detection, and similar. Narrow, and useful where it applies.
- Legally mandated or institutional communications. Again narrow, and not a route for marketing.
Neither of those helps a marketing programme, which is the point.  

## Italy versus France

## The differences that change what you build

- Consent bundling. Italy permits pixel consent to be combined with general marketing consent, provided the wording is neutral and properly informs people about the tracking. France does not, and wants consent specific to the purpose.
- Aggregate statistics. Italy grants the anonymised aggregate exemption. France declines to recognise it at all.
- Withdrawal. Italy expects granular withdrawal, so somebody can withdraw tracking consent without unsubscribing from your email entirely.
- Deadlines. France was 14 July 2026 and has already passed. Italy is 28 October 2026.

So if you operate across both, you cannot build one mechanism and apply it everywhere. France needs separate consent, Italy allows combined consent with granular withdrawal, and the exemption you might lean on in Italy does not exist in France.

## The part nobody is discussing

## What breaks in your programme when opens disappear

Every article I have read about this treats it as a compliance task. Update the form, send a re-permission email, tick the box, done.

What none of them mention is that open tracking is load-bearing in most email programmes, and removing it for a segment breaks things that nobody has thought to check.

### Your engagement definition stops working for that group

If your definition of engaged includes opened in the last X days, then Italian contacts without tracking consent will look dormant from the moment you turn the pixel off. Not because they went quiet, because you stopped being able to see them.

Left alone, your own suppression rules will quietly sunset a group of perfectly engaged subscribers for the crime of being Italian.

### Open-triggered automations will not fire

- Did not open, so resend with a different subject line. Will now resend to everybody in that segment, forever.
- Opened but did not click, so follow up. Will never trigger.
- Re-engagement flows keyed to a period of no opens. Will pull in people who are reading every email you send.
- Lead scoring that awards points for opens. Will systematically under-score one country.

### Your reporting becomes incomparable

Blended open rates across a list containing both tracked and untracked contacts mean nothing. You will see a decline that is not a decline, and if you do not flag it, somebody in your business will react to it.

## What to do

## In the next 14 (ish) days

1. Find out how many Italian contacts you have. By country field if you hold one, and by looking at.it domains and known Italian consumer providers if you do not. Most businesses are surprised in one direction or the other.
2. Decide your position per country, not globally. Turning tracking off for everybody is simple and costs you data you did not need to lose. Country-level control is the right answer and it needs a reliable country field, which is its own project.
3. Check what your platform can do. Can you disable open tracking for a segment rather than for a whole send? A surprising number of platforms cannot, and the answer determines everything else.
4. If you are going for consent, send the re-permission email now. With open tracking switched off for that send. You cannot use the pixel to collect the consent that the pixel requires, which is a trap several people have already walked into.
5. Fix the signup flow for new contacts. Anyone collected on or after 29 April 2026 needs compliant consent in place before any tracked email goes to them. That is already live rather than pending.
6. Audit every automation that depends on an open. List them, and decide for each one whether it gets rebuilt on clicks, rebuilt on another signal, or excludes the untracked segment.
7. Rebuild your engagement definition on clicks and real actions. Replies, purchases, logins, downloads, event attendance. Better than opens for everybody, and now necessary for some.
8. Separate your reporting. Tracked and untracked segments reported apart, with a note explaining why, so nobody panics at a number that was always going to fall.
9. Write down what you decided and why. Accountability is part of the framework and a short internal note now is worth a great deal later.

## The sources

## Read the guidance rather than the commentary

Including mine. The write-ups circulating about this vary in accuracy and several of them are wrong about the aggregate exemption, so go to the source where you can.

- The Garante's guidelines. Provvedimento n. 284 of 17 April 2026, published in Gazzetta Ufficiale no. 98 on 29 April 2026. Available on the Garante's own site, in Italian.
- The CNIL's recommendation on email tracking pixels. For the French position, which differs in the ways set out above.
- Article 29 Working Party Opinion 05/2014 on anonymisation techniques. Worth reading if you are relying on the aggregate exemption, because it sets the standard the Garante points at.
- Your own legal advisers. Really. The operational decisions in this post are mine to comment on. Whether your specific consent wording and lawful basis hold up is not.

## The conclusion

Two things are happening here and only one of them is about Italy.

The narrow thing is a deadline on 28 October that applies to anybody with Italian recipients, where the available exemption is narrower than most people think and standard platform tracking does not qualify for it.

The broader thing is that the open rate has been dying for five years and regulators are now finishing the job. Apple broke it in 2021, AI inboxes are inflating it, France removed it as a default in July, Italy follows this month, and there is no reason to assume the list of countries stops there.

A programme that still defines engagement by opens is a programme with a structural dependency on a signal that is being dismantled in front of us. Fix that for everybody and the Italian deadline becomes an administrative task rather than a crisis.

### Further reading from The Vault:

- [Email Tracking Pixels Now Require Consent in France and Italy: Your Action Plan](https://weareastral.co.uk/thevault/email-tracking-pixels-now-require-consent-in-france-and-italy)
- [Email List Churn: What's Normal, and What Isn't](https://weareastral.co.uk/thevault/email-list-churn-whats-normal-and-what-isnt-and-when-should-you-stop-emailing-someone)
- [How to Know Your Sender Reputation](https://weareastral.co.uk/thevault/how-to-know-your-sender-reputation.-why-you-cannot-look-it-up-any-more-and-how-to-work-it-out-instead)
- [Using the Data You Already Have](https://weareastral.co.uk/thevault/using-the-data-you-already-have-derived-properties-predictive-insights-and-where-ai-really-helps)
- [Email Marketing Best Practice Is Mostly Wrong](https://weareastral.co.uk/thevault/email-marketing-best-practice-is-mostly-wrong.-what-the-internet-says-what-i-say-and-why-we-have-all-been-taught-email-backwards)
- [Email Operations: The Processes That Turn a Pile of Campaigns Into a Programme](https://weareastral.co.uk/thevault/email-operations-the-processes-that-turn-a-pile-of-campaigns-into-a-programme)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.