---
type: Web
authors: '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/what-is-bimi-how-to-get-it-what-it-costs-and-does-it-help-email-deliverability?utm_medium=email&_hsenc=p2ANqtz-_Ep7CmOpP2CovoYTRtr1KIITgqU25EIOsujHfq4-KlyQviJtSMY0O-Sk_TXmYmtRqVKgcvvb4prEDEjAwW4D9PHZupQQr-KqMjB_RCroyV659Rwio&_hsmi=141442980&utm_content=141381565&utm_source=hs_email
published: 2026-07-22
created: 2026-07-24
tags:
  - digital-campaigning
  - fundraising
---


If you have been paying attention to email marketing news in the last few years, you have probably seen BIMI mentioned. It keeps appearing in trend roundups, vendor announcements, and conference keynotes alongside authentication, AI, and accessibility as one of the things serious email programmes are doing.

Some of what you have read about BIMI is accurate. Some of it is inflated. And a fair amount of it is written by companies that sell BIMI certificates, which shapes all of this info considerably.

This blog is the version I would want to read: what BIMI is, what it looks like in the inbox, exactly what you need to do to get it, what it costs, whether you can do it yourself, and the honest answer to the question I get asked most often about it — does it actually improve deliverability and engagement?

## What BIMI is

BIMI stands for Brand Indicators for Message Identification. In plain English: it is a standard that lets your verified brand logo appear next to your sender name in the inbox, before the email is opened.

Without BIMI, the circle or square next to your sender name in Gmail, Apple Mail, or Yahoo shows either a generic initial, a contact photo if the recipient has saved you, or nothing. With BIMI implemented correctly, it shows your actual brand logo — consistently, across every email you send to every inbox that supports it.

![BIMI](https://weareastral.co.uk/hs-fs/hubfs/BIMI.png?width=8439&height=6750&name=BIMI.png)

BIMI sits on top of email authentication. It does not replace SPF, DKIM, or DMARC — it requires them. Think of it as the visible reward for having your authentication in order: your logo only shows up once you have proven, at a technical level, that you are who you say you are!

The standard is supported by Gmail, Yahoo Mail, Apple Mail, Fastmail, and La Poste. As of mid-2026, Outlook and Microsoft 365 are in a limited preview and cannot be relied on as a live deployment target. If a significant portion of your audience is B2B and lives in Outlook, this matters and I wouldn't bother with it.

## What it looks like and the difference between VMC and CMC

Two certificate types enable BIMI logo display, and they produce slightly different results in the inbox. Understanding the difference is important before you decide which route to take.

### VMC — Verified Mark Certificate

*Requires a registered trademark. Displays your logo with a blue verified checkmark in Gmail.*  
  
A VMC is the full-fat version of BIMI. Your logo is cryptographically tied to your domain and your registered trademark, verified by an authorised Certificate Authority. In Gmail, VMC-authenticated senders display their logo with a blue verified checkmark — the email equivalent of the blue tick on social media, except backed by a legally registered trademark rather than platform whim.

This is the option that produces the most visible trust signal in the inbox. It is also the more expensive and complex route.

### CMC — Common Mark Certificate

*No trademark required. Logo displays without the blue checkmark. Apple Mail does not yet support it.*  
  
The CMC was introduced in 2024–25 specifically to widen BIMI access beyond organisations with registered trademarks. Instead of trademark registration, you need to demonstrate 12 months of consistent commercial logo use. The logo displays in Gmail and Yahoo Mail, but without the blue verified checkmark. Apple Mail and iCloud Mail do not support CMC as of mid-2026 — they require a VMC.

If your audience is heavy on Apple Mail users (common in consumer and mobile-first audiences), CMC has a coverage gap worth knowing about.

![](https://weareastral.co.uk/hs-fs/hubfs/image-png-Jul-22-2026-06-37-31-5078-AM.png?width=4626&height=2244&name=image-png-Jul-22-2026-06-37-31-5078-AM.png)

Above is an example showing you the blue tick!

## How to get BIMI

BIMI implementation is not complicated in concept, but it involves several steps that have to be done in the right order, and each one is a potential sticking point if your existing setup is not clean. Here is the full process.

Step 1: Get your authentication properly in place

*This is the prerequisite everything else depends on.*

BIMI requires DMARC at an enforcement policy — either p=quarantine or p=reject. p=none does not qualify. If you are not at the enforcement level, you cannot proceed with BIMI. You also need working SPF and DKIM across all your sending domains and third-party sending platforms (your ESP, your CRM, your sales email tool, any other service that sends email on your behalf).

This authentication step is where most organisations get stuck, not because it is technically difficult, but because it requires mapping every service that sends email from your domain and ensuring each one is properly authenticated. For complex organisations with multiple platforms, this can take weeks. For simpler setups, it can be done in a few days.

If you are not sure where your authentication stands, start there before thinking about BIMI at all.

Step 2: Decide whether you need a VMC or a CMC

*This determines your route and your costs.*

If you have a registered trademark for your logo with a recognised IP office (UK IPO, EUIPO, USPTO, IP Australia, and others), you can pursue a VMC. If you do not have a registered trademark but have been using your logo commercially for at least 12 months, CMC is your route.

If you want a VMC and do not have a registered trademark, you need to get one first. Trademark registration typically takes 6–12 months and costs upwards of a few hundred pounds depending on the jurisdiction and whether you use a trademark attorney. This is a separate cost and timeline to BIMI itself.

Step 3: Prepare your logo file in the correct format

*SVG Tiny PS only. PNG does not work.*  
  
Your logo must be in SVG Tiny 1.2 Portable/Secure format — a specific subset of SVG with strict security requirements. Most design files are not in this format. You cannot simply export an SVG from Illustrator and expect it to work. The file needs to pass a specific validation before a Certificate Authority will accept it.

Some certificate providers include logo conversion and validation in their service. Others do not. If yours does not, you will need a designer or developer to handle the conversion, or you can use one of the free SVG Tiny PS converters available online — Red Sift and DMARC Trust both offer them.

Step 4: Purchase a certificate from an authorised Certificate Authority

*This is where the annual cost sits.*  
  
Authorised VMC issuers as of mid-2026 include DigiCert and GlobalSign (Sectigo is in this market but confirm they appear on your target mailbox providers’ approved issuer lists before purchasing). The validation process for a VMC involves identity verification — including a video call with the CA — and confirmation that your logo is the registered trademark you claim.

Certificate costs in direct pricing: **VMC approximately £1,100–£1,400 per year** (DigiCert lists at around $1,416/year, Sectigo from $1,350/year). **CMC approximately £770–£990 per year** (Sectigo from $990/year). Reseller pricing can be lower — some resellers list VMCs from around $649 — but check what is included and whether the issuer is on your mailbox providers’ approved lists.

Certificates expire annually and require renewal. Build this into your calendar!

Step 5: Publish your BIMI DNS record

*A TXT record pointing to your logo and certificate.*  
  
Once you have your certificate, you host both your SVG logo file and the certificate.pem file at stable, non-redirecting HTTPS URLs. Then you publish a BIMI TXT record on your sending domain: default.\_bimi.yourdomain.com, pointing to the logo URL and the certificate URL.

This is a DNS change — whoever manages your domain DNS needs to do this. It typically propagates within a few hours but allow 24–48 hours for full propagation.

Step 6: Test and monitor

*Check it displays correctly across supported clients.*  
  
Once the DNS record is live, test across Gmail, Yahoo, and Apple Mail (for VMC). There are BIMI record checkers available, BIMI Group, MXToolbox, and others, that validate your record before it goes live. Check that your logo displays correctly, that the certificate is valid, and that the checkmark (VMC only) appears in Gmail.

## Can you do it yourself, or do you need an expert?

It depends entirely on your starting point.

If your authentication is already fully in order, DMARC at enforcement across all your sending domains, SPF and DKIM clean, and you have a registered trademark and a simple sending setup, a reasonably technical in-house team can implement BIMI without external help. The steps are well documented, the tools are available, and the DNS change itself is straightforward.

If your authentication is not fully in order, if you have multiple sending platforms that need auditing, if you are not sure whether all your third-party senders are properly authenticated, or if your DNS is managed by someone else in the business and requires a separate conversation — getting to the starting line for BIMI will require either significant internal coordination or external help.

Some managed DMARC and BIMI services, Red Sift OnDMARC being one, offer end-to-end BIMI implementation including certificate procurement, SVG conversion, DNS setup, and ongoing monitoring, starting from around £200 per month for combined DMARC + BIMI packages. If you do not have in-house expertise and want someone else to handle it, this is the route.

Timeline to expect: if authentication is already at enforcement, allow 2–4 weeks for certificate validation and DNS setup. If authentication needs work first, allow 6–8 weeks minimum. If you need trademark registration too, add 6–12 months.

## Does BIMI improve deliverability?

This is the question I get asked most about BIMI, and well the answer is: not directly.

BIMI does not tell inbox providers to deliver your email to the inbox. There is no signal being sent to Gmail that says “this sender has BIMI, therefore they should be in the Primary tab.” Inbox placement is determined by engagement signals, sending reputation, list hygiene, authentication, and content relevance — none of which BIMI changes.

What BIMI does do is display your verified logo before the email is opened. The argument is that a recognisable logo in the inbox increases the likelihood of an open, and higher open rates improve your engagement signals, which over time improves deliverability. That mechanism is real but it is long, indirect, and dependent on many other variables.

The engagement claims you will see cited for BIMI need treating with some scepticism. The figures most commonly quoted- 38% lift in open rates, 4–6% better engagement for TalkTalk, 21% lift in purchase intent, come from specific implementations at specific brands, measured at specific points in time. They are not independent studies with controlled variables.

The problem with those numbers is that when you implement BIMI, you are almost certainly also doing other things at the same time. Your authentication has been cleaned up. Your domain reputation may have improved as a side effect of getting DMARC to enforcement. Your sending practices may have been reviewed as part of the process. Any of those factors could explain improved engagement, independently of the logo display.

More importantly, inbox behaviour is not a controlled environment. The subscribers opening your emails this month are on different days than the subscribers opening your emails last month. Some of them came back from holiday. Some of them changed jobs. Some of them started using a new device. You cannot attribute a change in open rate to BIMI unless you have a proper testing framework with controlled audiences, sufficient sample sizes, and long enough measurement windows to eliminate seasonal and behavioural variation. Most of the BIMI engagement data being cited does not come from testing frameworks that meet that bar.

## Who should really get BIMI and who should wait

Think of it this way. Email programme success is built in layers. Before you can worry about the logo next to your sender name, you need the foundations: clean authentication, good list hygiene, intent-based sending, relevant content, honest measurement. I cover this in the [PPPP™ Framework,](https://weareastral.co.uk/pppp-email-framework) which maps out the full picture of what a healthy email programme looks like.

BIMI is near the end of that stack. It is something you do once everything below it is solid. Trying to implement BIMI while your deliverability is struggling, your list is disengaged, or your authentication is incomplete is like painting the outside of a house that has structural problems. The paint does not fix the structure!

### BIMI makes sense for you if:

- Your DMARC is already at p=quarantine or p=reject across all your sending domains
- You have a registered trademark for your logo
- Your brand is recognisable enough that logo display in the inbox would meaningfully help subscribers identify you
- You have the budget for annual certificate renewal (£800–£1,400+ per year) and the technical resource to implement and maintain it
- You send significant volume to Gmail, Yahoo, and Apple Mail (VMC) or Gmail and Yahoo (CMC) audiences
- Your programme fundamentals are solid and you are looking for additional marginal gains

### BIMI can wait for you if:

- Your authentication is not yet at enforcement level — getting there first is far more valuable
- You do not have a registered trademark and do not want to pursue one
- Your list health, deliverability, or engagement has room to improve through other means
- The majority of your audience is B2B in Outlook — where support is still limited
- You do not have the budget or technical resource to implement and maintain it properly
- Your brand is not yet at a scale where inbox logo recognition would meaningfully differentiate you

The strongest case for BIMI is at established consumer brands with high send volumes, strong brand recognition, and audiences concentrated in Gmail and Apple Mail. Think retail, financial services, media, subscription businesses. For smaller businesses, agencies, or B2B programmes, especially those still working on their deliverability fundamentals — BIMI is not the right priority.

## The case that i strongest for BIMI: anti-phishing

The engagement argument for BIMI is complicated. The anti-phishing argument is simpler and clearer-cut.

Email phishing attacks almost always involve impersonating a trusted brand. An attacker sends an email that looks like it is from your bank, your delivery company, your email provider. The email looks legitimate in the preview because the attacker has spoofed your sender name. The recipient opens it and hands over credentials or clicks a malicious link.

BIMI, combined with properly enforced DMARC, makes brand impersonation significantly harder. If your domain is at DMARC p=reject, emails that fail authentication are rejected before they reach the inbox. If your brand is BIMI-enrolled, your subscribers develop an association between your sender name and a verified logo — an email claiming to be from you without that logo is immediately suspicious to a trained eye.

For large consumer brands with high-value customer relationships like financial services, retail, healthcare, this is the strongest commercial case for BIMI. It is not primarily a marketing tool; it is a brand security measure that has marketing benefits as a secondary effect.

For smaller businesses where brand impersonation is a lower risk, the anti-phishing argument carries less weight. Your customers are less likely to receive phishing emails impersonating you because you are not a high-value enough target for sophisticated phishing operations.

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.
