---
type: "Web"
authors: "[[Click & Pledge]]"
url: "https://clickandpledge.com/blog/pci-and-soc-2-the-gap-between-compliant-and-secure/"
published: 2026-05-07
created: 2026-07-09
tags:
  - "fundraising"
  - "strategia-organizacji"
---


Every nonprofit fundraising platform claims to be secure. The phrase “PCI compliant” appears on vendor websites the way “organic” appears on grocery packaging—frequently, confidently, and with wildly varying levels of substance behind it.

For nonprofit leaders evaluating technology, this creates a dangerous knowledge gap. Security vocabulary has been co-opted by marketing, and most organizations lack the technical literacy to tell the difference between a vendor that underwent months of independent security auditing and one that filled out a questionnaire about itself.

That difference matters. Nonprofits operate in a trust economy. Donors hand over not just money but personal data—names, addresses, emails, giving history, payment credentials. When that trust is violated through a data breach, the damage isn’t measured only in compliance fines. It’s measured in donors who never give again, board members asking questions nobody prepared to answer, and the slow erosion of an organization’s most irreplaceable asset: its reputation.

This article explains the two security frameworks most relevant to donor protection—PCI DSS and SOC 2—in plain language. Not to turn you into a security expert, but to give you enough understanding to ask the right questions and recognize when the answers are inadequate.

## What PCI DSS Actually Is

PCI DSS stands for Payment Card Industry Data Security Standard. It is a set of security requirements governing how any organization that accepts, processes, stores, or transmits credit card data must protect that data.

#### PCI DSS (Payment Card Industry Data Security Standard)

A set of security requirements created by the PCI Security Standards Council—founded by Visa, Mastercard, American Express, Discover, and JCB—governing how any organization that handles credit card data must protect it. PCI DSS is not a law; compliance is enforced through contractual relationships between merchants, payment processors, and acquiring banks.

The first thing to understand: PCI DSS is not a law. It was created by the credit card industry itself—specifically the PCI Security Standards Council, founded by Visa, Mastercard, American Express, Discover, and JCB. Compliance is enforced through the contractual relationship between a merchant, their payment processor, and the acquiring bank. This means enforcement is uneven, and the consequences of non-compliance often don’t surface until after something goes wrong.

The second critical concept: PCI DSS defines four merchant levels based on annual transaction volume, and the level determines how rigorously compliance is validated.

| Level | Annual Transactions | Validation Requirement |
| --- | --- | --- |
| **1** | Over 6 million | On-site audit by a Qualified Security Assessor (QSA), producing a Report on Compliance (ROC) |
| **2** | 1–6 million | Self-Assessment Questionnaire, may be validated by QSA or Internal Security Assessor |
| **3** | 20,000–1 million (e-commerce) | Self-Assessment Questionnaire |
| **4** | Fewer than 20,000 (e-commerce) | Self-Assessment Questionnaire |

Here is the problem: a platform that completes a Self-Assessment Questionnaire and a platform that undergoes a full Level 1 QSA audit both get to say **“PCI compliant.”** The phrase carries no indication of rigor. It is the difference between a building that passed a full structural engineering inspection and one where the owner filled out a form saying the foundation looks fine.

## The Merchant vs. Service Provider Chasm

The levels above apply to merchants. But a donation platform is not a merchant—it is a service provider, processing transactions on behalf of thousands of nonprofits. And the thresholds for service providers are dramatically different.

##### Merchant Level 1 Threshold

Six million transactions per year before a QSA on-site audit is required. Below that, self-assessment is permitted.

##### Service Provider Level 1 Threshold

300,000 transactions per year—a twenty-fold difference. Above that, a QSA on-site audit and Report on Compliance are mandatory.

A donation platform processing millions of transactions annually but classifying itself as a merchant—and self-assessing at the six-million threshold instead of meeting the service provider requirement at 300,000—is building its compliance on the wrong foundation.

When a vendor tells you they are PCI compliant, the first question should be: **compliant as what—merchant or service provider? At what level? And who validated it?**

## What Level 1 Actually Costs

Level 1 validation is not a checkbox exercise. It is an active, expensive operational discipline.

It requires hiring ethical hackers—authorized security professionals who launch simulated attacks against the network to find vulnerabilities before malicious actors do. Think of it as paying a friendly army to probe your defenses continuously, so that criminals cannot find an easy way in. Beyond penetration testing, Level 1 requires twenty-four-hour network monitoring, dedicated security operations staff, and annual on-site audits by an independent QSA.

#### Disclosure

At Click & Pledge, our annual Level 1 validation costs approximately $200,000—covering QSA audits, penetration testing, continuous monitoring, and dedicated security infrastructure. That figure scales with organizational complexity; larger operations pay more.

This is the economic reality behind the compliance gap: most fundraising technology vendors avoid Level 1 because the investment is substantial and ongoing. Self-assessment costs nearly nothing by comparison.

## The Shared Responsibility Problem

A common misconception in the nonprofit sector is that using a reputable payment gateway—like Stripe or PayPal—or hosting in a PCI Level 1 data center automatically makes an organization secure.

It does not. Think of the payment gateway or data center as a four-lane highway. The highway is modern, well-paved, and certified safe. But the nonprofit’s website, server configuration, and form-building software represent the car driving on that road. The road being Level 1 certified does not protect you if your car has bald tires and no brakes.

If a nonprofit builds its own donation forms and posts data to a gateway API, the nonprofit is responsible for the security of its own server environment—the patches, the configurations, the access controls, the scripts running on the page. The gateway secures the highway. Nobody is securing the car unless the nonprofit demands it from whoever built it.

Intrusion has almost nothing to do with the form fields themselves. **Attackers do not break the form. They attack the unpatched server or the insecure code surrounding it.**

## Digital Parking Lot Thieves

To understand the modern threat, consider the TJ Maxx breach—one of the largest payment data thefts in history. In that attack, criminals intercepted data from physical card readers and collected it wirelessly from the parking lot. They never entered the store. They never touched the register. They sat outside and harvested data in transit.

#### E-Skimming

The digital evolution of physical card skimming. A malicious actor injects a script—a digital stowaway—into a payment page. That script intercepts card data in the donor’s web browser before it ever reaches the payment processor. PCI DSS 4.0 now mandates script-level protections as a baseline requirement to prevent this attack.

E-skimming is the digital evolution of that same attack. The card reader is now the donor’s own web browser. The malicious actor injects a script—a digital stowaway—into the donation page. That script skims the card data in the browser before it ever reaches the safe road of the payment processor.

PCI DSS version 4.0, which took full effect in March 2025, directly addresses this with requirements 6.4.3 and 11.6.1. Organizations must now maintain an inventory of all scripts executing on payment pages, implement authorization mechanisms, verify script integrity, and detect unauthorized changes. These are not optional enhancements. They are baseline requirements.

Your donation page is a payment page. The question to ask your vendor is not just “do you process cards securely?” but **“how do you protect the donation page itself from being tampered with?”**

## What SOC 2 Type II Actually Is

SOC 2 stands for System and Organization Controls 2. It is an auditing framework developed by the American Institute of Certified Public Accountants—the AICPA. It is completely separate from PCI DSS, created by a different body, for a different purpose.

#### SOC 2 Type II

An auditing framework developed by the AICPA that evaluates an organization’s controls across up to five Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, and Privacy. A Type II report covers a sustained period of six to twelve months, proving that controls are not just designed but actually operating effectively over time.

Where PCI DSS focuses on payment card data, SOC 2 evaluates an organization’s controls across up to five Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, and Privacy. A SOC 2 audit is conducted by an independent CPA firm and produces a detailed report on control design and operating effectiveness.

For nonprofits, this framework matters because PCI DSS has a blind spot. Even when credit card data is fully outsourced to a payment processor, fundraising platforms still store vast amounts of donor personally identifiable information: names, email addresses, physical addresses, phone numbers, giving history, donation amounts, campaign participation, volunteer records, notes, and internal communications. None of that is covered by PCI DSS. All of it is exactly the kind of data that, when stolen, turns a technical incident into a relationship crisis.

## Type I vs. Type II—This Distinction Matters

##### SOC 2 Type I

A snapshot. On this date, these controls existed and were suitably designed. Proves intent. Like showing someone your gym membership card.

##### SOC 2 Type II

A sustained evaluation over 6–12 months. These controls existed, were suitably designed, and actually worked as intended. Proves practice. Like showing twelve months of workout logs.

For donor platforms, Type II is the meaningful standard. Security is not a configuration you set once. It is an ongoing operation. A Type II report is the clearest available evidence that controls are actually functioning—not just promised in a policy document that sits in a drawer.

When evaluating a SOC 2 report, ask which Trust Services Criteria are included. A report covering only Security provides narrower assurance than one also including Confidentiality and Privacy—both directly relevant to donor data. Also look for exceptions: findings where the auditor determined a control was not operating as designed. Exceptions are not automatically disqualifying, but they should be read and understood.

## Why Both Frameworks Matter—The Two Risks

PCI DSS and SOC 2 address two fundamentally different risks, and nonprofits are exposed to both.

**Risk 1: Payment page compromise.** An attacker injects a script that skims card data from your donation page—the digital parking lot thief. This is a financial event. Cards get reissued, fraud monitoring activates, and the payment industry’s insurance infrastructure engages. The response is mechanical and familiar.

**Risk 2: Donor PII breach.** An attacker gains access to your fundraising platform’s database—through a compromised admin account, an unpatched vulnerability, or a third-party integration. Names, emails, addresses, giving history, and communications are exfiltrated. This is a relationship event. There is no “reissue” for a donor’s personal information.

A vendor can hold PCI compliance and still have no meaningful controls on who can access, export, or mishandle your entire donor file. A nonprofit that only asks “are you PCI compliant?” is asking about half the risk—and arguably the less damaging half.

## The Proof Tiers: Evaluating Vendor Claims

Not all security claims carry equal weight. Nonprofit boards have a fiduciary obligation to look past marketing claims. This tiered model provides a framework for evaluating where a vendor’s evidence actually falls.

| Tier | Description |
| --- | --- |
| **Tier 0** | Marketing claims. “PCI compliant” or “bank-level security” on the website. No documentation available. Functionally meaningless. |
| **Tier 1** | Attestation without scope clarity. Documents exist (perhaps an SAQ or SOC 2 Type I) but the scope is unclear. Paperwork without context. |
| **Tier 2** | Evidence matched to architecture. Clear payment flow description, appropriate PCI validation, current SOC 2 Type II with identified scope, and incident response commitments. |
| **Tier 3** | Evidence plus operational maturity. Everything in Tier 2, plus: continuous monitoring, tested incident response, payment page anti-tampering, pen testing, and MFA-enforced admin controls. |

The question that separates these tiers is not “are you compliant?” The question is: **“Show me the evidence that matches your architecture, and show me that your controls operate continuously.”**

## What Every Board Should Be Asking

Board members do not need to understand cryptographic protocols. But they have a fiduciary obligation to govern risk, and donor data security is squarely within that obligation.

**Where does donor PII live?** In how many systems, with how many vendors, and who can export it in bulk? If no one can answer this clearly, the board has found its first priority.

**What independent evidence do our vendors provide?** “They told us they’re compliant” is Tier 0. Requesting actual SOC 2 Type II reports and understanding the PCI validation level is the minimum threshold for governance.

**How are our donation pages protected?** PCI DSS 4.0 made payment page security a requirement. If the vendor cannot describe their controls for script inventory, authorization, and tamper detection, the board should understand what that absence signals.

**Are our vendors validating as service providers or merchants?** A donation platform processing hundreds of thousands of transactions should be meeting the service provider threshold of 300,000—not hiding behind the merchant threshold of six million.

**Has our incident response plan been tested?** Not written—tested. A plan that has never been practiced is not a plan. It is a document.

**What changed this quarter?** This question forces ongoing attention rather than annual box-checking. Security is not a state. It is a direction.

## Conclusion

PCI DSS and SOC 2 are not interchangeable terms and they are not trophies. They are distinct evidence frameworks that address different dimensions of the same underlying obligation: protecting the people who trust your organization with their data.

PCI DSS governs the payment transaction—the moment a donor enters their card number. Its rigor depends entirely on the level of validation, and a Level 1 QSA audit and a self-assessed questionnaire are not equivalent, no matter what a vendor’s marketing page suggests. SOC 2 Type II governs operational controls—the sustained, ongoing protection of donor data across every system that stores it. Together, they form the minimum evidence standard that any nonprofit should expect from its technology partners.

#### Key Insight

The donors who fund your mission are trusting you with something they cannot reissue: their personal information and their confidence that you will steward it responsibly. That trust is not a compliance checkbox. It is infrastructure—and it deserves to be treated as such.

### References

1. PCI Security Standards Council. (2025). Payment Page Security and Preventing E-Skimming—Guidance for PCI DSS Requirements 6.4.3 and 11.6.1. PCI SSC Information Supplement. [PCI SSC →](https://blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming?ref=blog.clickandpledge.com)
2. PCI Security Standards Council. (2022). PCI DSS v4.0. Payment Card Industry Data Security Standard. [PCI SSC →](https://www.pcisecuritystandards.org/document_library/?ref=blog.clickandpledge.com)
3. American Institute of Certified Public Accountants. (2017). SOC 2—SOC for Service Organizations: Trust Services Criteria. AICPA Trust Services Framework. [AICPA →](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2?ref=blog.clickandpledge.com)
4. National Institute of Standards and Technology. (2024). Cybersecurity Framework (CSF) 2.0. NIST. [NIST →](https://www.nist.gov/cyberframework?ref=blog.clickandpledge.com)
5. Federal Trade Commission. (2024). Data Breach Response: A Guide for Business. FTC Business Guidance. [FTC →](https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business?ref=blog.clickandpledge.com)
6. Visa. (2026). Global Registry of Service Providers: Level 1 Service Provider Requirements. Visa Inc. [Visa →](https://www.visa.com/splisting/?ref=blog.clickandpledge.com)

#### PCI & SOC 2: The Gap Between “Compliant” and Secure

Hear this research discussed in depth on the Fundraising Command Center Podcast.

[Listen to Episode →](https://podcast.clickandpledge.com/episodes/pci-soc-2-the-gap-between-compliant-and-secure?ref=blog.clickandpledge.com)

#researchTechnology#S2E67#has-podcast