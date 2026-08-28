---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/how-to-run-cold-email-without-destroying-your-domain.-and-what-to-build-before-the-window-closes?utm_medium=email&_hsenc=p2ANqtz-8tEQHjH0O0u-Q8RLH0-1bF6RqyphmGOlcghqGZgC8t4Nj0N80uhoPz7dvXfkCN0ZsUl2oYPRc8ggGbfxUPJscXE1d-OVtlTroYciAb9TgC538k_7w&_hsmi=144226179&utm_content=144165921&utm_source=hs_email"
published: 2026-08-25
created: 2026-08-28
tags:
  - "digital-campaigning"
  - "fundraising"
---


I have written before that [cold email will be finished by 2030](https://weareastral.co.uk/thevault/why-cold-email-is-dying), and nothing since has changed my mind. It is dying; the decline is mechanical rather than moral (although people are completely filtered out now), and I would not build a business on it today.

Which is easy for me to say. If your entire pipeline currently runs on outbound, telling you to stop is not advice; it is a lecture, and you would be right to ignore it. Somebody has to hit a number this quarter.

So this blog does two things at once. It shows you how to run cold email in a way that does not destroy your sending reputation, your domain or your marketing programme, because most businesses doing outbound are carrying risks they have never been told about. And it shows you what to build alongside it, because every improvement below buys you time rather than a future.

## The decline

## Why cold email is dying, and why it has nothing to do with ethics

People assume I object to cold email on principle. I do have views about interrupting strangers, and they are not the argument. The argument is that the infrastructure stopped tolerating it, and infrastructure does not care what you think.

- Microsoft hosts most corporate mail and is now the hardest inbox to reach. Which is precisely where B2B outbound is aimed. Microsoft brought in its own sender requirements and will not accept a monitoring-only DMARC policy, so the provider that matters most for outbound is the one enforcing hardest.
- Gmail moved from soft deferrals to hard rejections. Non-compliant bulk mail is now refused outright rather than dropped somewhere you might eventually notice.
- Filtering is engagement-led, and cold email produces the wrong signals by definition. No prior relationship, low reply rates, high complaint risk, no history of anybody wanting your mail. Every signal the providers weigh most heavily is a signal cold outreach cannot generate.
- AI made the volume unbearable and burned the commons. Anybody can now generate ten thousand personalised-looking emails before lunch, recipients have learned the patterns, and the response rates that made outbound viable have collapsed for everybody, including the people doing it carefully.
- **Cold email filters.** Tools [like this one](https://www.getinboxzero.com/block-cold-emails) are becoming popular! Meaning your emails get filtered out and not seen again.

The window is closing rather than closed. There is still a version of this that works, for a while, if you do it properly. Doing it properly is considerably more work than the tooling suggests.

## The risks

## What you are gambling, usually without knowing it

The thing that alarms me most about the businesses I get called into is not that their outbound has stopped working. It is what they were staking on it.

Your domain reputation is the whole estate

Domain reputation has overtaken IP as the primary trust signal, which has a consequence people miss. Reputation attaches to your domain and follows it everywhere, so switching ESP does not launder a bad history, and running cold outreach from your primary domain puts your marketing email, your order confirmations, your password resets and your invoices behind the same reputation as your outbound.

A bad quarter of cold email does not cost you a campaign. It costs you the ability to email your existing customers, and it does so at whatever moment the damage tips over rather than at a convenient one.

### Blocklists and spam traps

Scraped and purchased data contains spam traps as a matter of design. Pristine traps are addresses that were never real and were seeded to catch people harvesting, so hitting one is proof you did not collect the address, not evidence that you made a mistake. Recycled traps are old abandoned mailboxes brought back into service, which is why an ageing list is dangerous as well as ineffective.

Landing on a major blocklist is recoverable, and the recovery takes weeks you will not have planned for, during which everything else you send suffers.

### The legal position, which is narrower than people are told

In the UK and EU, business-to-business marketing to corporate subscribers sits in a more permissive space than consumer marketing, and that latitude gets stretched well past where it belongs. Sole traders and most partnerships are treated as individual subscribers rather than corporate ones. Data protection obligations apply regardless of the marketing rules, so you still need a lawful basis, you still owe people transparency about where you got their details, and you still have to honour objections.

Worth taking proper advice on your own situation rather than the summary above, and worth noticing that most outbound tooling is built for a jurisdiction with different rules from yours.

## The setup

## What a defensible cold email setup looks like

If you are going to do this, do it in a way that quarantines the risk. Everything below is about containment first and performance second, which is the correct order and the opposite of how most setups get built.

1. Never send cold from your primary domain. Use a separate domain that carries its own reputation, so a bad outcome stays inside the outbound programme instead of taking down your marketing and transactional mail with it.
2. Keep it separate from everything else, permanently. Different domain, different platform, different mailboxes. No sharing with campaigns, no sharing with transactional, no exceptions when somebody is in a hurry.
3. Authenticate the sending domain properly. SPF, DKIM and DMARC, aligned, with DMARC at enforcement rather than sitting at p=none. Microsoft in particular will find you out.
4. Warm slowly, through real sending. Small volumes rising in steps over weeks, watching complaints and bounces at every stage, and holding when either moves the wrong way.
5. Avoid automated warm-up tools. Filters have got good at spotting the patterns they create, the same accounts get recycled across many customers, and the behaviour they simulate looks less like engagement every year. They are becoming a liability rather than a shortcut. I do like warm up tools but for brand new domains it's a red flag - it needs to be treated like a REAL inbox.
6. Keep volume per mailbox low and steady. Consistency is the signal. A mailbox sending a modest, stable volume looks like a person. A mailbox sending in bursts looks like software.
7. Do not build a rotation to evade limits. Dozens of lookalike domains cycling through mailboxes is exactly the pattern the providers built detection for, and it converts a deliverability problem into an enforcement one.
8. Include a working opt-out. People will tell you cold email does not need one. Somebody who cannot find a way out uses the spam button instead, and a complaint costs you far more than an opt-out does.
9. Monitor daily, not monthly. Postmaster Tools, complaint rate, bounce rate and reply rate, checked every day. Outbound goes wrong quickly and the early signals are the only cheap

## The data

## Where cold email really dies

Almost every outbound failure I have investigated was a data failure wearing a copywriting costume. The team assumed the messaging was wrong, rewrote everything, and the numbers stayed flat, because the problem was never the words.

### Bounces are the first thing that kills you

A high bounce rate on a new list tells the providers you did not collect this data, and it tells them immediately, before anybody has had a chance to reply to anything. Bounce rate is the fastest way to establish yourself as a sender who does not know their audience, and once established that impression is expensive to shift.

So verification is not a nice-to-have and it is not optional. If the bounce rate on a fresh list is anything more than very low, the list is bad, and no amount of clever sequencing will rescue it.

### Verification, and then verification again

- Verify immediately before sending, not when you bought the data. B2B data decays fast because people change jobs, and a file that was accurate three months ago is not accurate now.
- Re-verify anything older than a few weeks. Particularly if it has been sitting in a tool between campaigns.
- Strip role addresses. Anything beginning info, sales, admin, hello, contact or support. They belong to nobody, they get shared, and they attract complaints at a much higher rate than a named mailbox.
- Treat catch-all domains as a risk rather than a pass. A catch-all accepts everything, which means verification tells you nothing about whether the mailbox exists. Sending into them at volume is guessing.
- Suppress hard bounces permanently, the first time. Not for this campaign. Forever, across every system you own.

### Where the data came from matters more than how clean it is

A perfectly verified list of people who never heard of you is still a list of people who never heard of you, and verification only removes the technical problem. Scraped data carries traps, purchased data carries traps and resentment, and both carry the same fundamental issue, which is that nobody in the file has any reason to want your email.

The version of outbound with any future is the one where the data was built rather than bought. People who visited, downloaded, attended, replied, or work somewhere that just did something you have a specific reason to contact them about.

## Operating rules

## If you are going to run it, run it like this

- Small volumes, high relevance. Fifty properly researched emails will outperform five thousand generated ones, and they will not cost you your domain.
- Research, rather than merge fields. A first name and a company name is not personalisation, it is evidence of automation, and recipients now read it as exactly that.
- Reply rate is your only real metric. Opens are unreliable, and clicks are thin on cold. Replies are what you want commercially, and replies are also the strongest positive signal you can send a mailbox provider. Plus search increase - especially if you have your brand name in there
- Stop chasing non-responders. An eight-step sequence to somebody who has ignored you seven times is a complaint generator. Two touches, three at most, then leave them alone.
- One offer and one ask per email. Multiple asks read as a template, and templates get pattern-matched and deleted before they are read.
- Suppress aggressively and permanently. Anybody who asked you to stop, anybody who bounced, anybody who complained, anybody who ignored a full sequence, and every address at a domain that told you to go away.
- **Outbound to inbound.** My personal FAVE, this means we aren't going to sell, we provide value and something that if it's hyper relevant means this person is more likely to reply and say yes they want the lead magnet or a place at the event - and therefore they come to you and become inbound

## The shift

## What to build while outbound still works

Everything above buys you time. None of it changes the direction of travel, and the businesses that come through this are the ones that used the remaining window to build the thing that replaces outbound rather than to squeeze another quarter out of it.

The shift is uncomfortable to hear and completely doable, which is that you need a much smaller audience of far higher quality, coming to you rather than being pushed at.

### What that looks like in practice

- Publish the answers your buyers are already searching for. Every question your sales team gets asked in the first ten minutes of a call is a piece of content, and content is how a stranger becomes somebody who arrived on purpose.
- Make the opt-in intentional rather than consequential. Somebody who downloaded a guide to get past a form is not the same person as somebody who subscribed because they want to hear from you, and treating them identically is how good lists go bad.
- Build for the buyers who are not in market. Most of your audience will not buy for months or years, so the job of the programme is to be useful and present until the moment arrives, rather than to convert everybody this quarter.
- Let sales assist rather than lead. Outreach to somebody who has already engaged with you is a different activity from cold, carries almost none of the reputational risk, and converts at rates cold never approached.
- Report on pipeline influenced, not emails sent. Volume metrics are what keep outbound alive past its usefulness, because they always go up when you try harder.

## The conclusion

Cold email is not dying because somebody decided it was rude. It is dying because the mailbox providers built systems that reward wanted mail and punish unwanted mail, and cold outreach is the purest form of the second thing.

If you have to run it, quarantine it. Separate domain, verified data, low volume, real research, short sequences, daily monitoring, and a permanent suppression habit. That will keep you alive and it will keep the rest of your email programme out of the blast radius.

And use the time it buys you. The businesses that will be fine in 2030 are the ones building an audience now, while outbound still works well enough to pay for it.