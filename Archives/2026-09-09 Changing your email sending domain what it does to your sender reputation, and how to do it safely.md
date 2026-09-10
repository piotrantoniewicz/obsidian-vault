---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/changing-your-email-sending-domain-what-it-does-to-your-sender-reputation-and-how-to-do-it-safely?utm_medium=email&_hsenc=p2ANqtz-9KIFr353MSvtW-CRWZsrI0gyif2gfnVm_5v7eK-t4cXyBQTUJgJ_LId0lrTQTBkWXAPfpSIXAxIemEdltI2MI6DT1NfqpFGAJ-RHeeCI9jJauyvNI&_hsmi=145370304&utm_content=145358476&utm_source=hs_email"
published: 2026-09-09
created: 2026-09-10
tags:
  - "digital-campaigning"
  - "narzędzia-AI"
---


Changing your sending domain is the most dangerous single thing you can do to an email programme, and most businesses do it because somebody changed the logo.

The reason it is dangerous is straightforward once you see it. Sender reputation attaches to your domain, so your domain is the thing that carries fifteen years of good behaviour, or two years of bad. Move to a new one and none of that comes with you. You are not starting from a clean slate, you are starting from nothing, and nothing is not neutral. To a mailbox provider, a domain with no history that suddenly starts sending at volume looks exactly like the behaviour they built their filters to catch.

So this blog is in two halves. The first half is about whether you should change it at all, because most of the time the answer is no and the project quietly gets cancelled somewhere around the third paragraph. The second half is how to do it without destroying your programme, for the people who really do have to.

## The first question:

## Is changing your domain necessary? Probably not

Changing your sending domain does not fix a sending problem, it relocates one. Whatever behaviour damaged the old domain will damage the new one, and it will do it faster, because a new domain has no accumulated goodwill to absorb the hits.

### Reasons for:

- A rebrand where the old domain is being retired. The company name has changed, the old domain is going away, and continuing to send from it stops making sense to the recipient. A real reason, and it comes with a real timeline attached.
- An acquisition or a merger. Two organisations becoming one, or a brand being absorbed. Usually forced on you rather than chosen, which is why it goes badly so often.
- Separating streams that should never have shared reputation. Promotional mail sitting on the same domain as your order confirmations, or outbound prospecting running from your corporate domain. Worth fixing, and it is almost always a subdomain job rather than a domain change.
- A domain so badly burned that recovery costs more than rebuilding. Rare, and it is a decision that needs evidence behind it rather than a feeling. Recovery is slow but it is usually possible, and abandoning a domain should be a last resort.

### Reasons against:

- Escaping a reputation problem you have not fixed. The most common reason people move and the worst one. You will burn the new domain within a quarter using the same list and the same sending habits, and you will have lost the old one as a fallback.
- A marketing team wanting a shorter or punchier name. Understandable, and not worth several months of degraded placement and the risk of not recovering.
- Somebody read that subdomains are best practice. Subdomains often are the right structure. Reading that and immediately migrating your entire programme onto one without warming it is how a sensible principle becomes an outage.
- You are switching ESP. Your domain does not have to move because your platform did. Domain reputation is yours and it travels with you, which is also why switching platform never launders a bad history.

## The structure

## Subdomain or main domain, and what the difference buys you

Before the decision, some plumbing, because a surprising number of people running email programmes cannot say precisely what their sending domain is.

- Your root or organisational domain. The main one. astral-digital.co.uk. It carries your website, your corporate email, your invoices and everything else your business does online.
- A subdomain. Something in front of it. news.astral-digital.co.uk or mail.astral-digital.co.uk. It belongs to you, it inherits certain settings from the root, and it builds a reputation of its own.
- Your from address versus your return path. The from address is what the recipient sees. The return path, or envelope sender, is where bounces go and it is frequently a different domain belonging to your ESP. Reputation is being assessed on both, which is why alignment between them matters.

### Why you would use a subdomain

The purpose is isolation. Different types of mail have different risk profiles, and putting them on separate subdomains means a bad month in one place does not take down the others.

- Transactional mail on its own subdomain. Order confirmations, password resets, delivery updates. These must never share a reputation with your marketing, because if a hard week of campaigns takes down your order confirmations you have converted a deliverability problem into a customer service crisis.
- Marketing on its own. Campaigns and newsletters, where volume is high and complaint risk is highest.
- Outbound or prospecting somewhere else entirely. Ideally a separate domain rather than a subdomain, because cold outreach carries a risk profile nothing else in your programme comes close to.
- Your corporate mail left alone on the root. The one people forget. Your root domain is what your invoices, your contracts and your sales conversations travel on, and it should generally be protected rather than used for bulk marketing.

The discipline is to have as few subdomains as you can justify, each with a clear purpose that somebody can explain. Programmes that end up with eleven of them usually created them one at a time to solve a problem nobody documented, and none of them has enough volume to build a reputation worth having.

## The relationship

## Does a subdomain affect your main domain?

The question I get asked most on this subject, and the answer is partially, asymmetrically, and differently depending on the provider. Which is unsatisfying, so let me break it down properly, because people get it wrong in both directions.

### What is separate

- Each subdomain builds its own reputation. Engagement, complaints and bounces on news.yourdomain.com accumulate against that subdomain, which is the entire point of the separation and the reason it works.
- A bad month on one does not transfer wholesale to the others. A promotional subdomain having a difficult quarter should not stop your transactional mail arriving, and that protection is real.

### What is not separate

- The root influences how a new subdomain is treated at the start. A brand new subdomain has no history, so providers lean on what they know about the organisational domain while it establishes itself. A healthy root gives a new subdomain a gentler start. A damaged root does not give you a clean slate underneath it.
- DMARC is set at the organisational domain and inherits downward. Your policy applies to subdomains unless you explicitly override it with a subdomain policy, which is a detail people discover at the worst possible moment.
- Root-level problems affect everything beneath. A blocklisting on the organisational domain, a broken SPF record, or an authentication failure at root level takes the whole structure with it.
- Reputation systems vary in how they treat the relationship. Some weigh the organisational domain heavily, some are far more granular, and none of them publish exactly how. Assume more connection than you would like rather than less.

## The move

## How to change domain without destroying your programme

If you have a real reason and you have decided to go ahead, the sequence matters more than anything else. Almost every failed migration I have seen failed because somebody did the right things in the wrong order.

1. Set up authentication on the new domain first, and prove it works. SPF with a single record, DKIM signing correctly with the right selector, and DMARC in place. Verify with more than one tool and send test mail to accounts at each major provider before anything else happens.
2. Decide your structure before you send anything. Which streams live where, what the root is used for, and what each subdomain is called. Changing this later means warming twice.
3. Keep the old domain live and sending. Do not retire it on day one. It is your fallback, it carries your volume while the new domain has none, and you will need it for months.
4. Start with your most engaged people, in small volumes. The first mail from a new domain should go to the audience most likely to open, click and reply, because those positive signals are what establishes the domain as legitimate.
5. Ramp in steps across weeks, watching at every stage. Increase gradually, monitor complaints, bounces and placement daily, and hold at the current level rather than pushing on whenever anything moves in the wrong direction.
6. Split volume between old and new during the transition. The new domain takes an increasing share as it earns its history, and the old one covers everything it cannot yet carry.
7. Tell people the from address is changing. From the old domain, before it happens. Recognition is processed before content, so a new sender name arriving unannounced gets treated as an unknown sender by both the human and the filter.
8. Update everything that references the old address. Signup forms, preference centres, unsubscribe links, reply-to addresses, help documentation, and any automation that hard-codes a domain.
9. Only retire the old domain once the new one is fully established. And keep the DNS records live even after you stop sending, because removing authentication from a domain that people still have in their address books creates its own problems.

### Warming UP UP UP:

Warming is not a formality, and it is not something a tool does for you. You are teaching several different providers, independently, that mail from this domain is wanted, and teaching takes repetition over weeks.

- Think in weeks and months, not days. A meaningful warm-up runs across four to eight weeks minimum, and longer for large programmes. Anybody promising it in a fortnight is describing a volume schedule rather than a reputation.
- Start small and increase in steps. Modest daily volumes rising gradually. The exact numbers depend on your list size, and the shape matters more than the figures: steady, predictable, and never doubling overnight.
- Sequence your audience by engagement. Most engaged first, then the next tier, and so on. Never open with a broad send, and never include your dormant group at any point during warming.
- Watch complaints and bounces at every step. If either moves in the wrong direction, hold at that volume until it settles rather than pushing through and hoping.
- Keep the cadence consistent. Sending patterns matter as much as volume. A domain that sends every few days looks established. One that sends in bursts looks like software.
- Avoid automated warm-up tools for this specifically. The behaviour they simulate is precisely the pattern providers built detection for, the accounts get recycled across many customers, and using one on a brand new domain teaches providers the wrong thing about you from the very beginning.

## The cautionary bit

## What happens if you just switch

Worth walking through, because it is what most businesses do and the failure is predictable enough to describe in advance.

Monday morning. New domain configured, new from address, and the usual campaign goes out to the whole list, because the rebrand launches today and the deck said so.

From a provider's point of view, a domain with no sending history has just started sending at scale immediately. That specific pattern sits on every provider's list of negative signals, and it is there because it is what list buyers and spammers do. So the mail gets throttled, deferred, or delivered straight into spam, and a large share of your audience never sees the launch you spent three months planning.

What follows is worse than the bad send. Everybody who did not receive it generates no positive signals, the people who did receive it in spam generate complaints, and the new domain now has a history, which is a bad one. Meanwhile the old domain has been retired, so there is no fallback, no fully warmed alternative and nowhere to go while you fix it.

Recovery from that position takes months rather than weeks, and it is entirely avoidable by starting three months earlier.

## The timeline

## Working backwards from your cutover date

1. Three to six months out. Decide the structure, register and configure the new domain, get authentication in place and verified, and agree what each stream will send from.
2. Eight to twelve weeks out. Begin warming with your most engaged audience at low volume, increasing in steps, monitoring daily.
3. Four to eight weeks out. Run both domains in parallel, shifting an increasing share of volume onto the new one as it earns its reputation.
4. Two to four weeks out. Tell your audience the from address is changing, from the old domain. Update every form, link and automation that references the old one.
5. Cutover. The new domain carries the majority of volume, the old one stays live and available.
6. Three months after. Only now consider retiring the old domain, and keep its DNS records in place afterwards.

And never run a domain migration into peak trading. The busiest sending period of the year is the worst possible moment to be establishing a reputation from scratch, and the freeze on infrastructure changes in the run-up to peak exists precisely for this.  

## The conclusion

Your domain is the one asset in your email programme that truly belongs to you. Platforms change, IPs are usually somebody else's, templates get redesigned, and the domain quietly accumulates every good and bad decision you have ever made about sending.

Which makes changing it expensive in a way that does not show up on any project plan. So the order of questions matters: do we need to move at all, would a subdomain solve the actual problem, and only then how do we move without losing what we have built.

Most businesses that ask me the third question have not answered the first two, and about half of them do not need to move at all once they have.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.