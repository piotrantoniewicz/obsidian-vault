---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/email-tracking-pixels-now-require-consent-in-france-and-italy?utm_medium=email&_hsenc=p2ANqtz-9is2VQ_aY7XZM5xV5ArRlQWC6EDtEKdkGE8tPcFPUewoqBksyJkw-8rw0fgCoqZvhJik45WRVvMPhWrjkmTD3t-BwEmjk9LWAQ9F94nuNzVJ3jiCo&_hsmi=140873362&utm_content=140822143&utm_source=hs_email"
published: 2026-07-15
created: 2026-07-16
tags:
---


Open rates have been unreliable for years. Apple Mail Privacy Protection inflated them from 2021. Gmail’s Gemini integration has been auto-opening emails to generate AI summaries since January 2026, inflating them further. Most experienced email marketers already treat the open rate as a directional signal at best and a vanity metric at worst.

Now two European regulators have weighed in with something that goes further than just questioning the metric. France’s CNIL and Italy’s Garante have both ruled that the tracking pixel producing that open rate is, legally speaking, the same category of technology as a cookie — and requires the same kind of consent before it can be used.

The French deadline was 14 July 2026. Italy’s is 28 October 2026.

If you send to anyone in France or Italy, this affects you!! It does not matter where your business is based. It does not matter which platform you use. It does not matter whether you are B2B or B2C, a charity or a commercial operation. If a tracking pixel fires in an email landing in a French or Italian inbox, the rules apply to you.

This blog explains exactly what has changed, whether it affects your programme, what you are allowed and not allowed to do, and, most importantly, the specific steps to take in the platforms most of you are using.

## What a tracking pixel actually is and why this is happening now

A tracking pixel is a 1x1 transparent image embedded invisibly in the HTML of your email. The moment a recipient’s email client loads the image — which happens when the email is opened — a request fires back to your ESP’s server. That request carries information: who opened it, when, from which device, in which location. Your ESP logs it. Your open rate goes up.

This technology is not new. It has been in email marketing since the early 2000s. What is new is that regulators have finally caught up to it.

The legal logic is this: the EDPB (European Data Protection Board) confirmed in its Guidelines 2/2023, finalised in October 2024, that loading a pixel counts as “gaining access to information on the user’s terminal equipment” under Article 5(3) of the ePrivacy Directive. That is the same legal basis that governs cookies. Cookies require consent. Therefore, by extension, tracking pixels require consent.

France and Italy have not invented new law. They have applied existing law — the ePrivacy Directive and GDPR — to a practice that has been operating without proper legal basis for years. The CNIL put it plainly: the obligation to obtain consent before deploying tracking pixels has existed since GDPR took effect in 2018. What changed in April 2026 is that both regulators published formal guidance and attached deadlines to their expectations, which removes the “we didn’t know” defence that organisations have relied on.

Roughly 68% of all email sent today contains at least one tracking pixel, according to industry estimates. The vast majority were never gated behind explicit consent. They were enabled by default in Mailchimp, HubSpot, Klaviyo, and every other major platform — and most senders have never changed the default setting.

## France and Italy: what each country requires and where they differ

The two frameworks share the same legal foundation but differ in their legal weight, timing, and some specifics. If you send to both countries, you need to plan for both.

### France — CNIL Recommendation (Deliberation 2026-042)

*Deadline: 14 July 2026 for existing contacts. Immediate for new contacts from 14 April 2026.*

The CNIL’s guidance is a recommendation rather than a binding regulation, but the CNIL has explicitly stated it will enforce from 14 July 2026 — and its track record supports taking this seriously. Google paid €325 million in September 2025 for advertising practices the CNIL had warned about for two years.

The key requirements:

- Consent to receive emails and consent to be tracked inside them are not the same permission. They must be collected separately. A newsletter sign-up that bundles email and pixel consent into one tick box is not sufficient under France’s framework.
- For contacts collected before 14 April 2026: you had until 14 July 2026 to inform them about pixel tracking and give them a meaningful way to object. If you have not done this, you should stop tracking these contacts until you have.
- For contacts collected on or after 14 April 2026: explicit, separate tracking consent is required from the point of sign-up. No transitional grace period applies.
- Recipients must be able to withdraw tracking consent independently — they must be able to opt out of the pixel without unsubscribing from the list entirely.
- There is a narrow deliverability exemption: open tracking used purely to manage list hygiene (suppressing inactive contacts, adjusting sending frequency) may not require consent, provided the data stored is limited to the date of last open only, and is used for no other purpose.
- Aggregated, anonymised open counts (where no individual is identifiable) are also permitted without consent.

### Italy — Garante Provision No. 284

*Deadline: 28 October 2026 for existing contacts. Immediate for new contacts from 29 April 2026.*

The Garante’s provision is binding law, not a recommendation. Italy gives more time — the six-month transitional window runs until 28 October 2026 — and is slightly more flexible on consent bundling, but less flexible on the exemptions.

The key requirements:

- Unlike France, Italy permits consent for tracking to be bundled with general marketing email consent, provided the request is neutral and non-coercive and the recipient is clearly informed about both purposes.
- For contacts collected before 29 April 2026: tracking can continue during the six-month window, provided you inform each contact about pixel use in the next email you send to them and give them a way to opt out.
- For contacts collected on or after 29 April 2026: compliant consent must be in place before any tracked email is sent.
- The withdrawal right is non-negotiable: recipients must be able to opt out of tracking without unsubscribing from emails. A single “unsubscribe from everything” button does not satisfy this requirement. There must be a separate, clearly visible mechanism — the Garante’s preferred implementation is a standardised icon or link in the email footer.
- Italy’s exemption for anonymised tracking is narrower than France’s: it requires one shared pixel per campaign (not per-recipient tracking), with IP addresses and technical identifiers fully anonymised. Standard per-recipient ESP tracking does not meet this exemption under the Garante’s interpretation.

## Does this affect you? How to find out quickly

If you have any contacts in France or Italy on your list, yes. The rules apply to any sender emailing recipients located in those countries, regardless of where the sender is based. A UK business, a US company, a Singapore agency — if the email lands in a French or Italian inbox with a tracking pixel in it, the obligation applies.

The first step is to understand your exposure. Here is how to do a quick audit.

Step 1: Check your list for French and Italian contacts

Search your contact database for email domains associated with French and Italian providers. This will not catch everyone (many people use Gmail or Outlook), but it gives you an indication of your exposure. Also us IP country if you have it!!

French provider domains to look for:

- @orange.fr, @wanadoo.fr — Orange France
- @laposte.net — La Poste
- @sfr.fr, @neuf.fr, @cegetel.net, @club-internet.fr, @numericable.fr — SFR and legacy brands
- @free.fr — Free

Italian provider domains to look for:

- @libero.it, @virgilio.it, @iol.it, @inwind.it, @blu.it — ItaliaOnline
- @alice.it, @tim.it, @tin.it — TIM
- @tiscali.it — Tiscali
- @email.it — Email.it

If your CRM stores country data on contacts, run a filter there too. Domain matching only finds a subset — a French person with a Gmail address is equally covered by the CNIL guidance.

Step 2: Understand how you are using tracking data

The consent obligation applies to open tracking used for campaign measurement, behavioural profiling, lead scoring, segmentation, sales alerts, or any commercial purpose.

Ask yourself:

- Do open rates feed into your reporting dashboards?
- Do opens trigger any automations or flows?
- Do opens feed into lead scoring in your CRM?
- Does your sales team receive notifications when a contact opens an email?
- Are opens used to segment your list, define engagement tiers, or inform suppression decisions?

If the answer to any of these is yes — and for most programmes it will be — those uses require consent for French and Italian contacts. The deliverability exemption is narrow and does not cover campaign measurement or any commercial use of open data.

Step 3: Check whether your ESP can handle per-contact tracking suppression

This is the critical operational question, and as of mid-July 2026 the platform responses are still catching up. The ideal solution is per-contact enforcement: a consent field on the contact record that tells the platform whether to insert the tracking pixel in emails sent to that person. Not a campaign-level toggle. Not an account-level switch. Per-contact, per-send.

We will cover the current state of each major platform below.

## What the exemptions cover and what they do not

Both regulators acknowledge that some uses of open tracking fall within existing ePrivacy exemptions and do not require consent. It is worth being precise about what these cover, because they are narrower than many senders hope.

### What IS permitted without consent (under both frameworks, with conditions)

- Deliverability management: suppressing inactive contacts, adjusting sending frequency based on engagement. France permits per-recipient tracking for this purpose, but only if the data stored is limited to the date of last open and used for no other purpose. Italy requires aggregate-only data for this exemption.
- Fully anonymised aggregate open counts: where no individual recipient is identifiable, aggregate statistics do not require consent. The anonymisation must be real — not pseudonymised data that could be re-linked.
- Security and authentication: open tracking used to confirm that an email containing an authentication code was opened on the intended device falls outside the consent requirement.
- Legally mandated communications: certain mandatory institutional notices.

### What is NOT permitted without consent

- Campaign performance measurement: reporting on open rates per campaign, per audience, per send type
- Lead scoring: using open behaviour to score or qualify leads
- Behavioural segmentation: creating segments based on who opened what and when
- Sales alerts and notifications: alerting a sales rep when a prospect opens an email
- Send-time optimisation fed by individual open history: ML-based timing that relies on individual-level open data
- Re-engagement flows triggered by non-opens: any automation that fires because a contact has not opened in X days  
	Personalisation driven by open behaviour: content or frequency adjustments based on individual open patterns

In short: the vast majority of what email marketers actually use open data for requires consent in France and Italy. The exemption covers the narrow operational case. It does not cover the commercial analytics layer.

## What to do

There are two realistic paths here: turn off tracking for French and Italian contacts until you have collected proper consent, or pursue a consent collection process that allows you to continue tracking those who agree. For most senders, turning off tracking for the relevant segment is the faster, lower-risk starting point.

### Step 1: Segment your French and Italian contacts

Build a segment or list in your ESP of contacts you have identified as likely to be in France or Italy. Use country fields in your CRM where available. Supplement with domain matching. Accept that this will not be perfect — someone with a Gmail address and no country field recorded may be French and you will not know. For the contacts you can identify, act on them. For the unknown, your DPO should advise.

### Step 2: Disable open tracking for this segment

This is where the platforms diverge significantly in what they currently support. The gold standard is per-contact enforcement, where a consent field on the contact record tells the platform whether to include the tracking pixel in each email sent to that person. As of July 2026, most mainstream platforms are not fully there yet, but they are moving.

The current practical approach for most senders is to create no-pixel versions of your emails for the French/Italian segment and send those separately, with tracking disabled at the campaign level. Not elegant, but functional.

### Step 3: Audit your automations and flows

Every automation that is triggered by, or that segments on, open behaviour needs to be reviewed. Common automations to check:

- Re-engagement flows triggered by non-opens — these will not work reliably without open data
- Sales notifications triggered by email opens
- Lead scoring rules that weight opens
- Segmentation that creates “engaged” or “lapsed” tiers based on open history
- Send-time optimisation if it draws on individual open history

For French and Italian contacts without tracking consent, these flows need fallback logic based on clicks, website visits, purchases, or other meaningful actions rather than opens. If your flows have no click-based fallback, this is the moment to build one — which is genuinely the right thing to do anyway, given how unreliable open data has become across all geographies.

### Step 4: Update your consent capture for new sign-ups

For France: new contacts collected on or after 14 April 2026 require explicit, separately collected tracking consent at the point of sign-up. Your sign-up form needs a distinct, unchecked checkbox or toggle for tracking consent, separate from the marketing email consent box, with a plain-language explanation of what the tracking pixel does and why.

For Italy: new contacts collected on or after 29 April 2026 require consent before any tracked email is sent. Italy permits this to be bundled with marketing consent, provided the request is non-coercive and the recipient is clearly informed. But recipients must be able to withdraw tracking consent independently at any time.

### Step 5: Add a tracking opt-out mechanism to your emails

Both regulators require that recipients can withdraw tracking consent at any time, without unsubscribing from the list entirely. This means your email footer needs more than an unsubscribe link. It needs a separate “manage tracking preferences” link or a standardised icon (as the Garante suggests) that allows the recipient to switch off the pixel independently.

How you implement this depends on your platform. Most will require a preference centre update. The key requirement is that opting out of tracking and opting out of emails are two distinct choices presented with equal prominence.

### Step 6: Do not use opens in your re-permission email

If you are sending a communication to your French and Italian contacts to inform them about tracking and collect consent, that email must itself be sent without open tracking. Turn off the pixel for this specific send before it goes. Using an open from that email as a proxy for consent is explicitly invalid under the CNIL framework.

## What your platform currently supports and what it does not

This is the area moving fastest. Platform responses were arriving throughout early July 2026, and what was accurate at time of writing may have been updated by your platform since. Check the documentation links below and your platform’s own communications for the most current state.

### HubSpot

*Per-email tracking toggle now in beta. Per-contact enforcement not yet available.*  
  
HubSpot wrote to account admins on 2 July 2026 about the CNIL and Garante guidance. As of 8 July 2026, HubSpot documented a per-email tracking toggle in beta: Super Admins can enable the portal for this feature, then switch tracking off per individual marketing email in the editor, which removes the pixel from that email entirely.

What is not yet available: per-contact enforcement. There is no native way in HubSpot to have a consent field on the contact record that automatically suppresses the pixel for that person across all sends. The HubSpot Community has active feature requests for this — linked below — but it is not in the product as of mid-July 2026.

The current working pattern for HubSpot users is: build a segment of French/Italian contacts, create a version of each email send with tracking disabled using the beta per-email toggle, and send that version to the French/Italian segment. Duplicate effort, but functional.

Where to find the settings: Settings → Tools → Marketing → Email → Tracking (account level). Per-email toggle: in the email editor, under Tracking — requires Super Admin permission override to be enabled first.

### Klaviyo

*Per-contact opt-out now live. Sign-up form consent collection in development.*

Klaviyo has moved the furthest of the major platforms as of mid-July 2026. They have published dedicated guidance on the CNIL and Garante requirements and launched two controls:

- Account-wide tracking off: Settings → Email → Tracking — disables open tracking for every email your account sends
- Per-recipient opt-out: every recipient now carries an open tracking consent status, separate from their marketing consent. Opt a recipient out and Klaviyo stops recording their opens immediately, including going forward. You can set statuses in bulk via CSV import, SFTP/data warehouse sync, or the API.

What is still in development: native consent collection on sign-up forms. Klaviyo has flagged this as their next phase of work but it is not yet live.

Practically, Klaviyo users can import a list of French/Italian contacts and set their open tracking consent status to opted-out via bulk import. Per-campaign tracking can also be disabled individually.

### Mailchimp

*Per-campaign toggle available. No per-contact enforcement yet.*

Mailchimp’s open tracking is on by default for every campaign except plain-text sends. You can disable it per campaign in the email builder under Settings & Tracking → Edit → uncheck Track opens. This is a manual per-campaign step with no global kill switch for specific segments, so unless you template this in, it needs to be done on every send.

There is no per-contact tracking enforcement in Mailchimp as of July 2026. The practical approach is the same as HubSpot: segment your French/Italian contacts and send them a version of each campaign with tracking disabled.

### Braze

*Per-profile fields available for open and click tracking suppression.*  
  
Braze documents per-profile fields (email\_open\_tracking\_disabled and its click equivalent) that remove the pixel per recipient. Genuine consent-level enforcement is available currently for SparkPost and SendGrid sending infrastructure. This is the architecture the other platforms are working towards.

### Adobe Journey Optimizer

*Per-message toggles and consent schema available.*  
  
Adobe published a dedicated CNIL guidance page for Journey Optimizer on 7 July 2026, mapping its per-message open and click toggles, link-level "never track" mode, AEP consent schema and preference-centre pattern to the recommendation.

### ActiveCampaign, Brevo, and others

Most major platforms offer list-segment-level tracking toggles or per-contact tracking flags. Check your platform’s own documentation for CNIL/Garante compliance guidance — most published something in June or July 2026. The pattern to look for is the same everywhere: can a consent field on the contact record, not a campaign-level setting, decide whether the pixel fires?

## What this means for your metrics and reporting

For French and Italian contacts without tracking consent, you will not have open data. That is the point. The question is what you measure instead.

This is actually a conversation that should have happened years ago — Apple MPP started inflating open rates in 2021, Gmail Gemini auto-opens have been inflating them further in 2026, and opens have been unreliable as a meaningful engagement signal for some time. France and Italy just made the transition obligatory for part of your list.

The metrics that work without open data:

- Click rate — a real human action, not a machine-generated event. This is the primary engagement metric for your French and Italian contacts going forward.
- Website activity — if your ESP or CRM integrates with your web analytics, contacts visiting your site after an email send is a meaningful signal independent of open tracking
- Purchases and conversions — the commercial outcome that matters more than any intermediate metric
- Email replies — the clearest engagement signal there is
- Unsubscribe and complaint rate — negative signals that remain measurable regardless of tracking consent

Your re-engagement flows and lead scoring models will need to be rebuilt around these signals for your French and Italian segments. Flows triggered by non-opens need click-based or website-visit-based alternatives. Lead scoring that weights opens needs to shift weight towards clicks and page visits.

This is the same transition I have been advocating for across all geographies regardless of regulation. Opens are not a meaningful action. Clicks, replies, purchases, and website visits are. The regulation has just made it compulsory for part of your list to start measuring what actually matters.

## The bigger picture — this is not just a France and Italy problem

France and Italy moved first. But the ePrivacy Directive sits in the same statute books in every EU member state. The legal logic the CNIL and Garante applied — confirmed by the EDPB’s own guidelines from October 2024 — is available to every other data protection authority in Europe. Other regulators have the same text in front of them.

Beyond the EU, the same logic is filtering through other privacy frameworks. The UK’s PECR and ICO guidance impose comparable requirements for cookie-like technologies. Canada’s CASL, Brazil’s LGPD, and emerging US state-level privacy laws are all moving in the same direction.

Treating this as a France-and-Italy problem is the comfortable reading. The more accurate reading is that France and Italy moved first, and the programmes that build compliant consent infrastructure now will not be scrambling when the third and fourth rulings arrive.

If you are building a consent and tracking preference centre for France and Italy, build it to work globally. The extra effort to make it applicable to your whole list is minimal compared to rebuilding it jurisdiction by jurisdiction as new requirements emerge.

## What to do right now

If you have French or Italian contacts on your list, here is the immediate priority list:

- Identify your French and Italian contacts using country fields in your CRM and domain matching against the provider lists above
- Disable open tracking for these contacts using whatever mechanism your platform currently supports — per-campaign toggle is the minimum viable approach while per-contact enforcement is being rolled out
- Audit every automation that relies on opens and build click-based or activity-based fallbacks
- Update your sign-up process to collect tracking consent separately from email consent for France (immediately) and Italy (by 28 October 2026)
- Add a standalone tracking opt-out to your email footer — separate from the unsubscribe link, with equal prominence
- Send your re-permission or notification email without open tracking enabled — the pixel cannot be used to gather the consent it needs
- Involve your DPO or legal counsel before finalising your consent model — this blog is marketing operations guidance, not legal advice

Open rates have been declining in reliability for years. Apple MPP, Gmail Gemini auto-opens, and now regulatory intervention have collectively made the case that clicks, replies, website visits, and conversions are the signals worth building your programme around. France and Italy just made that case compulsory for part of your list.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.