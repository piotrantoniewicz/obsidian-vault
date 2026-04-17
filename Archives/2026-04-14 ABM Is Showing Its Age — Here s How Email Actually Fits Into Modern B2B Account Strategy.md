---
type: Web
authors: '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/abm-is-showing-its-age-heres-how-email-actually-fits-into-modern-b2b-account-strategy?utm_medium=email&_hsenc=p2ANqtz-9Syd-2EkrLs2jgKcNfztukdMjf8v369IIUxrIi1EfNf0cXwFAU0XfAbl_yJR-LxaXXcpG6b2iQuR8C7fG0vKp4MIr1OB3BZdEUxxlYANKWFT0UUYQ&_hsmi=133521287&utm_content=133531118&utm_source=hs_email
published: 2026-04-14T00:00:00.000Z
created: 2026-04-17T00:00:00.000Z
tags:
  - digital-campaigning
  - content-marketing
---


Account-Based Marketing has had a very good decade.

It arrived as the sophisticated alternative to spray-and-pray demand generation, and in many ways it was. The core idea — identify the accounts that matter most, concentrate your resources on them, personalise your approach, and align marketing with sales — is genuinely sound. As a philosophy, ABM represented a real maturity step for B2B go-to-market thinking.

But somewhere between the philosophy and the execution, something went wrong. ABM became a product category. A software purchase. A process with tiers — ABM 1:1, ABM 1:few, ABM 1:many — that increasingly looked like just... segmented marketing with better branding. And the email component of most ABM programmes became one of the most mechanically over-engineered and strategically under-thought parts of the whole thing.

This blog is not a takedown of ABM. It is an honest look at where the concept is showing its age, why email specifically is harder and more complicated in an account-based context than most ABM frameworks acknowledge, and what the more useful frame for B2B email in 2026 actually looks like.

Spoiler (of course): it's intent, not account lists.

## What ABM actually means for email — and what most programmes get wrong

In a traditional ABM programme, email plays a supporting role to a broader multi-channel approach: ads targeting specific accounts, personalised content, coordinated outreach from sales, and marketing campaigns designed to create awareness and momentum within defined target accounts.

In theory, email in this context is powerful. You can send highly relevant content to specific stakeholders at accounts you've identified as high-value. You can align messaging with what sales is saying. You can create a coherent narrative across multiple touchpoints within a single organisation.

In practice, most ABM email programmes look like this:

- A list of target accounts is assembled, usually based on firmographic data — industry, size, revenue, geography
- Contacts within those accounts are identified and added to a CRM
- A sequence of emails is built and sent to those contacts, usually manually or via a sales engagement tool
- The emails are personalised with company name, industry, and sometimes a reference to a specific pain point
- Results are measured in reply rates, meeting bookings, and pipeline attribution

And the problem — the one that the ABM industry rarely discusses honestly — is that this approach conflates two very different things: targeting an account and reaching the people within it.

An account is a company. A company does not read emails. People read emails. And those people have their own inboxes, their own priorities, their own relationship to email as a communication channel, and — critically — their own corporate infrastructure that may actively prevent your emails from reaching them at all.

## The corporate email infrastructure problem nobody in ABM talks about

This is the section that will be genuinely new information for many B2B marketers — and it is one of the most practically important things to understand about email in an account-based context.

When you email someone at a large or mid-sized organisation, your email does not simply travel from your sending server to their inbox. It passes through a series of corporate security and filtering layers that can intercept, quarantine, modify, or silently block your message — regardless of your sender reputation, your authentication setup, or the quality of your content.

### Corporate email security infrastructure: what's actually between you and the inbox

Most enterprises and mid-market organisations use dedicated email security platforms layered on top of their email client. The most common are Mimecast, Proofpoint, Barracuda, and Microsoft Defender for Office 365 — and they are specifically designed to filter out unwanted, suspicious, or potentially harmful external email.

These systems operate very differently from consumer spam filters like Gmail's algorithm. They are:

- - Configurable at organisation level — IT teams set policies that apply to the entire organisation, and individual preferences matter less
		- More aggressive by default — enterprise environments prioritise security over convenience; when in doubt, they block
		- Pattern-aware — they track sending behaviour across the organisation, not just to individual recipients
		- Link-rewriting and sandboxing — all links in your email may be rewritten and resolved through the security provider's infrastructure before the recipient sees them, which can inflate click data and slow delivery
		- Tenant-wide in their decisions — a single employee marking your email as junk can influence how your domain is treated for the entire organisation.

### The simultaneous send problem in ABM

This is one of the most significant and least discussed deliverability risks in B2B email, and it is particularly acute in ABM programmes.

When ABM identifies a high-priority account and marketing or sales sends coordinated outreach to the CEO, CFO, Head of IT, and VP of Operations at the same company in the same campaign window — which is exactly what many ABM programmes are designed to do — the following things can happen:

- Volume-based filtering triggers. The security platform sees multiple messages from the same sending domain to multiple internal recipients in a short period. This matches patterns associated with phishing campaigns and bulk outreach. Filtering kicks in.
- Cross-recipient learning. If one of the five recipients marks your email as junk, that signal propagates. Their security platform may apply that signal broadly — blocking your domain for other recipients at the same organisation, sometimes retroactively.
- Link analysis queues. Security platforms sandbox and analyse every link in your email before allowing it to resolve. If five people at the same organisation all receive an email with the same links at the same time, those links get queued for analysis simultaneously. This can introduce significant delays or cause the links to be blocked if the analysis produces a red flag.
- Reputational flagging at organisation level. Enterprise security providers share intelligence. A sender flagged as suspicious by Proofpoint at one organisation can affect how that sender is treated by Proofpoint at other organisations.

The cruel irony is that the more carefully targeted your ABM programme is — the more you concentrate your outreach on specific, high-value accounts — the more likely you are to trigger exactly these patterns. Because concentration is what the security infrastructure is designed to detect.  

### What to do about it

This is not an unsolvable problem, but it requires understanding the constraint before you can design around it.

- - Stagger multi-stakeholder sends within the same account. If you are emailing multiple people at the same organisation, do not send simultaneously. Space sends across days, not hours. The pattern of multiple simultaneous external emails is what triggers security flags — spreading them out significantly reduces the risk.
		- Monitor engagement signals at account level, not just individual level. If an entire account shows zero engagement across multiple contacts, that is more likely an infrastructure block than universal disinterest. Investigate before assuming.
		- Use your CRM data to identify which organisations use enterprise security platforms. Enterprise and mid-market accounts in regulated industries (finance, healthcare, legal, government) are almost universally running aggressive filtering. Calibrate your expectations and approach accordingly.
		- Consider alternative first touchpoints for high-priority accounts. If the goal is to establish a relationship with a specific account, email may not be the best opening move — particularly for cold or warm-but-not-opted-in contacts. LinkedIn, event meetings, or inbound content that pulls them to you will not trigger corporate security infrastructure in the same way.
		- Never mix cold outreach with your marketing email domain. This is worth repeating in an ABM context: cold or warm outreach to accounts that have not opted in should never come from the same domain as your marketing programme. The reputation damage from one flows to the other.

## The 95% problem: why ABM's fundamental premise is more complicated than it admits

ABM is built on a targeting assumption: identify the right accounts, concentrate your resources, and create the conditions for a sale.

What this assumption struggles with is the basic reality of B2B buying: at any given moment, roughly 95% of your total addressable market is not in an active buying cycle for what you offer. They are not evaluating vendors. They are not building business cases. They are not ready to take a sales meeting.

This is true whether or not they appear on your ABM target account list.

ABM frameworks typically respond to this by saying: focus your efforts on accounts that show buying signals, firmographic fit, or both. Which is sensible advice. But in practice, most ABM programmes are not actually doing sophisticated signal detection — they are working from a static list of companies someone decided were "ideal customers" based on criteria that were set months or years ago.

A company can be a perfect firmographic fit — right industry, right size, right tech stack — and still be completely out of market because:

- They just signed a three-year contract with a competitor
- Their budget is frozen for the rest of the financial year
- A key decision-maker just left and the role is vacant
- They are mid-way through an internal reorganisation that has paused all vendor decisions
- The problem you solve is not their priority right now

None of these things are visible from firmographic data. None of them are captured by an account list. And all of them make your carefully crafted ABM email sequence completely irrelevant to the recipient — regardless of how personalised it is.

This is the fundamental gap in traditional ABM: it tells you who to target but not when targeting them actually makes sense.  

## Intent-led account strategy: the evolution ABM needs

Here is my actual take, and I'll own it.

ABM as a category is not wrong, but it has become too static, too list-driven, and too focused on who rather than when. The evolution that makes it genuinely powerful in 2026 is layering real intent signals on top of account targeting — and letting those signals, not the account list, drive email timing and content.

Intent-led account strategy starts from the same place as ABM: identify the accounts that matter. But instead of then executing a pre-planned campaign sequence, it does something different. It watches those accounts for signals that indicate genuine readiness, interest, or need — and only triggers meaningful outreach when those signals appear.

The result is not fewer emails overall. It is emails that arrive at the right moment — when there is something real to respond to, rather than when the campaign calendar says it is time.

### What intent signals look like in a B2B account context

Intent signals in an account-based context can come from multiple sources, and the most sophisticated programmes combine several of them:

- First-party behavioural signals — contacts at the account visiting your website, reading specific content, viewing pricing pages, attending webinars, downloading resources. These are the strongest signals because they are self-generated and directly connected to your specific brand.
- Third-party intent data — platforms like Bombora, G2, TechTarget, and similar providers track content consumption across the web and can indicate when companies are actively researching topics relevant to your category. Someone at your target account reading multiple pieces of content about CRM implementation across different publications is a meaningful signal, even before they've visited your site.
- CRM and pipeline signals — movement within your own pipeline, reactivation of dormant contacts, changes in engagement patterns from previously quiet accounts.
- Organisational signals — new hires in relevant roles (a new VP of Marketing at a target account is a buying signal for marketing technology), funding rounds, acquisitions, new office openings. These indicate strategic change that often correlates with purchasing activity.
- Negative signals that tell you to wait — contract renewal dates, financial year timings, leadership changes that pause decisions, public announcements that indicate budget freezes or strategic pivots.

The critical difference between intent-led account strategy and traditional ABM is this: the signal triggers the outreach, not the calendar. You are not running a sequence because it is week three of the account's place in your programme. You are sending an email because something has happened that makes this the right moment to be in contact.

### How email fits into intent-led account strategy

Within an intent-led model, email plays specific, defined roles — and those roles are different from the campaign sequences that characterise traditional ABM email.

Role 1: Awareness and ambient presence.

Before a contact at a target account shows active intent, email's job is the same as it is in any relationship-building context: show up with consistent value, build familiarity, be the brand that is remembered when the need arrives. This is not a sales email. It is a thought leadership email, a useful resource, an insight they haven't seen elsewhere. It earns the relationship slowly, not aggressively.

Role 2: Signal-triggered follow-up.

When a contact at a target account visits a high-intent page — pricing, case studies, implementation guides — or downloads a specific resource, an intent-triggered email responds to that signal directly. Not a generic nurture. An email that acknowledges where they are and offers what they need next, whether that is more information, a comparison, or a gentle invitation to talk.

Role 3: Supporting the sales conversation.

When a target account is in active evaluation, email works in close coordination with the sales team. Marketing provides content that supports the specific conversation the sales rep is having — objection-handling material, relevant case studies, stakeholder-specific resources for different buying committee members. The email is not running independently of the sales motion; it is amplifying it.

Role 4: Post-meeting and post-conversation follow-up.

One of the highest-value uses of email in an account-based context is the structured follow-up after a meaningful conversation. A well-designed post-meeting email that reinforces key points, addresses questions raised, and provides supporting evidence is far more effective than any amount of pre-meeting cold outreach.

## The buying committee challenge: emailing multiple stakeholders without creating a deliverability disaster

B2B buying decisions are not made by individuals. They are made by committees — groups of people with different roles, different priorities, different levels of seniority, and different relationships to the purchase decision.

Research consistently suggests that the average B2B purchase involves anywhere from six to ten stakeholders, depending on deal size and organisational complexity. ABM is specifically designed to address this reality by engaging multiple stakeholders within a target account simultaneously.

But doing this via email carries the infrastructure risks described earlier — plus some additional strategic complications that are worth understanding separately.

### Different stakeholders need fundamentally different emails

A CFO evaluating a significant technology purchase and a Head of IT evaluating the same purchase are not the same audience. They have different priorities, different objections, different measures of success, and different emotional relationships to the decision.

- The CFO wants to understand total cost of ownership, ROI, risk, and strategic fit. They are not interested in technical implementation details. They want confidence that this is the right commercial decision.
- The Head of IT wants to understand integration requirements, security posture, implementation complexity, and ongoing support. They are not interested in ROI narratives. They want confidence that this will not create problems for them.
- The end user champion — the person whose daily work will change — wants to understand what it means for them specifically. Will this make their job easier or harder? What does the transition look like? What happens if it goes wrong?
- The CEO or sponsor wants strategic alignment. Does this fit with where the organisation is going? Is the vendor credible enough to trust with something important?

A single ABM email sequence that tries to speak to all of these people simultaneously will speak to none of them properly. The content that reassures the CFO is irrelevant to the IT lead. The technical detail that satisfies IT is impenetrable to the CEO.

This is where ABM email gets genuinely hard — and where most programmes take shortcuts that reduce effectiveness significantly.

### Practical approach: stakeholder-specific content, coordinated timing

The solution to the buying committee challenge is not sending the same email to everyone with a different first name token. It is building stakeholder-specific content that addresses each person's actual concerns, coordinated to arrive in a sequence that makes sense across the committee — not simultaneously, for the infrastructure reasons already covered.

- Map the buying committee before building content. For each target account, identify who the relevant stakeholders are and what their primary role in the purchase decision is. Sponsor, technical evaluator, end user, financial approver, procurement. Each of these needs different content.
- Build content that speaks to each role's specific concerns. Not a different version of the same email — genuinely different content that addresses what matters to that person. An ROI-focused piece for the commercial stakeholders. A security and implementation guide for IT. A change management and adoption piece for end users.
- Coordinate but stagger. Sales and marketing should coordinate on which stakeholders to engage and when — but the actual sends should be staggered to avoid triggering infrastructure flags. A two to three day gap between stakeholders within the same account is a reasonable minimum.
- Let the CRM be the single source of truth for account status. Everyone emailing into the same account needs to know what everyone else has said and when. Without this, you get the most damaging ABM failure mode: a prospect receiving contradictory or duplicative messages from multiple people at your organisation, in the same week, with no apparent awareness of each other.

## What actually works: a practical email framework for B2B account strategy

Having challenged the traditional ABM model and laid out the complications, here is what a practically effective approach to email within a B2B account strategy actually looks like.

Layer 1: The awareness foundation — before outreach begins

Before you send a single targeted email to anyone at a target account, you should have already built some degree of familiarity through non-intrusive channels. Content that surfaces in their research, LinkedIn presence, conference participation, referrals, and any other touchpoints that create recognition without requiring an email interaction.

Email outreach to someone who has never encountered your brand before is cold outreach, regardless of how carefully you've researched their company. The awareness foundation does not make the subsequent email warm by itself — but it increases the probability that when your email arrives, the sender name triggers a positive or neutral recognition rather than "who is this?"

Layer 2: First-party signal monitoring — wait for the right moment

For contacts at target accounts who are on your database — whether through a content download, event registration, or direct opt-in — monitor first-party signals before sending anything account-specific.

The signals that matter most:

· Multiple visits to high-intent pages (pricing, case studies, implementation, comparison guides)

· Downloads of mid-to-late funnel content

· Webinar attendance, particularly on commercially relevant topics

· Increased frequency of any engagement after a quiet period

· Direct enquiry or reply to any previous communication

These signals tell you something has changed for this contact. A purchase cycle may have opened. A budget conversation may have started. A problem may have become urgent. That is when email has the best chance of being genuinely relevant rather than interruptive.

Layer 3: Signal-triggered email — the right message for the right moment

When a first-party signal appears, the triggered email should respond directly to what the signal reveals. Not a generic nurture. A message that is specifically useful given what the behaviour implies.

A contact who has visited your pricing page three times in a week is likely in a commercial conversation internally. The email they need is not "did you know we offer X feature?" It is: a clear explanation of what the investment looks like and what it includes, a relevant case study showing ROI for a comparable company, a direct and low-friction invitation to talk if they have questions.

Use TFDS to map what this person is most likely thinking, feeling, doing, and saying at the moment the signal appeared. The answers tell you exactly what content the email should contain.

Layer 4: Sales alignment — email as support, not competition

In an account-based context, email and sales outreach must be coordinated, not independent. The moment a target account enters active evaluation, marketing email should shift from independent nurture to sales support — providing content that supports the specific conversation the sales team is having, not running a parallel track.

This requires:

· Sales reps flagging account status in the CRM in real time

· Marketing having a defined suppression rule: when an account is in active sales conversation, broad marketing sends stop

· A shared content library of sales enablement emails that sales reps can send or recommend for specific objections and questions

· A clear hierarchy: sales conversation takes priority over marketing cadence, always

Layer 5: Post-purchase and expansion — the most underused email in B2B

Most B2B ABM programmes focus almost entirely on new business acquisition. They invest heavily in the pre-purchase journey and then largely abandon the post-purchase relationship to customer success or account management.

This is a significant missed opportunity. Existing customers are the easiest accounts to expand, the most likely to refer new business, and the most credible advocates for your brand. And email is one of the most effective tools for maintaining and deepening those relationships — if it is designed for relationship maintenance rather than constant upselling.

Post-purchase account email should focus on:

· Ensuring successful adoption and realising value from the purchase already made

· Sharing relevant developments, insights, and thought leadership that is genuinely useful to their role

· Building the relationship with stakeholders beyond the primary contact

· Surfacing expansion opportunities when intent signals suggest readiness — not on a fixed cadence

## How to measure email performance in an account-based context

Standard email metrics — open rate, click rate, unsubscribe rate — are even less useful in an account-based context than they are in general email marketing. In B2B account strategy, you need metrics that reflect account-level progress, not individual email interactions.

The metrics that actually matter in an account-based email programme:

- - Account engagement score over time — not per email, but the aggregate engagement pattern from contacts at a target account across your programme. Is engagement increasing, stable, or declining? This tells you more about account health than any individual send.
		- Pipeline velocity for email-touched accounts — do accounts that are engaged with your email programme move through the sales pipeline faster than those that aren't? This is one of the most defensible measures of email's contribution to B2B revenue.
		- Stakeholder coverage — within your most important accounts, what percentage of the relevant buying committee has any form of engagement with your content or email programme? Low coverage means high risk: you're dependent on a single contact and have no relationship with the other decision-makers.
		- Intent signal response rate — when you trigger an email in response to a specific intent signal, what percentage result in a meaningful next action (reply, page visit, content download, meeting booking)? This tells you whether your signal-triggered emails are actually relevant to the moment.
		- Account re-engagement rate — for accounts that have gone cold, what percentage respond to re-engagement attempts? And more importantly, what does re-engagement look like — is it a click, or is it a meaningful action like a reply or a meeting?
		- Revenue influenced — not revenue attributed (which requires perfect attribution, which doesn't exist), but accounts where email was a consistent touchpoint in the journey to close. Track this as a trend over time, not a single number.

## The honest summary: email works in B2B — but not the way ABM assumes

Email is genuinely powerful in a B2B account-based context. It is persistent, personal, documentable, and capable of delivering exactly the right content to exactly the right person at exactly the right moment — when it is done properly.

But "done properly" in 2026 looks very different from the account list plus email sequence model that most ABM programmes run. It requires:

- - Understanding that corporate email infrastructure can silently block your most carefully targeted outreach — and designing around that reality
		- Accepting that firmographic targeting tells you who to watch, not when to act — and building intent signal monitoring into the approach
		- Treating different stakeholders within the same account as genuinely different audiences — not the same email with a different name
		- Coordinating email with sales in real time — not running parallel, unconnected tracks to the same people
		- Measuring at account level, over time — not at campaign level, per send

The fundamental shift is from account lists and campaign calendars to account signals and triggered relevance. That shift is what makes email genuinely powerful in a B2B context — rather than a well-intentioned source of corporate spam filter material.

ABM pointed us in the right direction. Intent got us the rest of the way.

### Further reading from The Vault:

- [Intent Over Personalisation](https://weareastral.co.uk/thevault/intent-over-personalisation-what-personal-actually-means-in-email-and-how-to-build-it)
- [Your B2B Email Marketing Strategy Needs More Reassurance, Not Offers](https://weareastral.co.uk/thevault/your-b2b-email-marketing-strategy-needs-more-reassurance-not-offers-heres-why)
- [Why Cold Email Is Dying](https://weareastral.co.uk/thevault/why-cold-email-is-dying)
- [What Email Deliverability Actually Is](https://weareastral.co.uk/thevault/what-email-deliverability-actually-is-and-the-3-metrics-that-really-matter)
- [The Missing Layer in Your Email Strategy](https://weareastral.co.uk/thevault/how-to-audit-your-external-comms-for-timing-problems)
- [Designing Email Journeys Using TFDS](https://weareastral.co.uk/thevault/designing-email-journeys-using-tfds)
- [What an Email Marketing Strategy Actually Needs to Look Like in 2026](https://weareastral.co.uk/thevault/what-an-email-marketing-strategy-actually-needs-to-look-like-in-2026)

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.
