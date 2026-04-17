---
type: Web
authors: '[[Jeff Robertson]]'
url: >-
  https://www.truesense.com/blog/boost-your-nonprofits-email-reach-a-beginners-guide-to-spf-dkim-dmarc-and-bimi?utm_source=www.civicshoutnewsletter.com&utm_medium=newsletter&utm_campaign=bimi-why-your-logo-belongs-in-the-inbox&_bhlid=cd89f5acb53271b457c2a83d563a63af173b3c82
published: 2025-04-09T00:00:00.000Z
created: 2026-03-23T00:00:00.000Z
tags:
  - digital-campaigning
  - organizacje-społeczne
  - fundraising
---


By:

As part of a nonprofit, you rely on email to engage donors, inform supporters, and share important information. If your messages are being marked as spam, however, you lose this crucial opportunity to build and maintain those relationships. That’s where email authentication protocols such as SPF, DKIM, DMARC, and BIMI come in.

## What Is SPF?

SPF (Sender Policy Framework) is a system that helps email providers verify that the server sending your email is authorized to do so on behalf of your domain. It works by comparing the “From” domain in your email with a list of authorized IP addresses or servers that are allowed to send email from that domain.

Without SPF, malicious actors can send fake emails that appear to come from your nonprofit: a practice called email spoofing that can damage your organization’s reputation. By setting up SPF, you help email providers recognize your legitimate emails and block fake ones.

To set up SPF, you’ll need to create a DNS (Domain Name System) record for your domain that includes a list of authorized servers. Your email service provider or IT team can help you create and add this record.

## What Is DKIM?

DKIM (DomainKeys Identified Mail) adds a layer of security by digitally signing your emails with a cryptographic signature that is unique to each email. This signature proves that the email has not been altered after being sent and that it truly came from your nonprofit.

If someone intercepts or modifies your email as it travels through the internet, DKIM ensures that the recipient can tell that the message was tampered with. Additionally, DKIM helps to establish trust with email providers, ensuring that they treat your emails as legitimate.

Setting up DKIM typically involves generating a public/private key pair. The public key is added as a DNS record, and the private key is used by your email system to sign the emails you send. Your email service provider or IT team can help you generate and add the DKIM keys — and regularly rotate them for additional security.

## What Is DMARC?

DMARC (Domain-based Message Authentication, Reporting, and Conformance) is an email-authentication protocol that builds on both SPF and DKIM. It helps you control what happens to emails that fail the SPF or DKIM checks and provides reports about how recipients’ email servers are treating your emails.

DMARC allows you to set a policy for how you want email servers to handle emails that fail the SPF or DKIM checks. For instance, you can choose to have such emails quarantined (sent to the spam folder) or rejected outright. Through its reporting, you can track who is sending emails on behalf of your domain and identify any potential misuse.

To set up DMARC, you’ll need to add a DMARC record to your domain’s DNS settings. This record specifies your policy for handling authentication failures and provides a way to receive reports. Start with a quarantine policy to monitor how your emails are being treated before enforcing stricter rules.

## What Is BIMI?

BIMI (Brand Indicators for Message Identification) allows your nonprofit’s logo to appear next to your email in recipients’ inboxes, providing instant visual recognition and increasing trust. To use BIMI, you need to have a properly implemented DMARC policy in place.

BIMI helps recipients recognize your legitimate emails more easily, which is especially important for nonprofits trying to build strong relationships with supporters. Having your logo displayed next to your email not only boosts your brand’s visibility, but it also reassures recipients that the email is from a trusted source.

Before using BIMI, however, it’s essential to ensure that the logo you plan to display is legally protected. Trademarking your logo is a critical step to safeguarding your nonprofit’s brand identity because it grants you exclusive rights to use your logo and prevents others from using it in ways that could confuse your supporters or dilute your brand’s trustworthiness.

When you set up BIMI, email providers will display your trademarked logo next to your emails in the inbox. If your logo is not trademarked, others could potentially use it or a similar version in their emails, creating confusion for your supporters. Trademarking your logo ensures that your visual identity is legally protected and distinct, and it helps maintain the integrity of your communications.

To implement BIMI, you’ll need to have a valid DMARC policy (usually set to reject), create a high-quality SVG (scalable vector graphic) version of your logo, and upload it to a publicly accessible location. Then, you add a BIMI record to your DNS that points to the location of your logo.

## Why Email Deliverability Matters for Nonprofits

Email deliverability is essentially the success rate of your emails in reaching the intended recipients’ inboxes. A variety of factors influence deliverability, including:

- The reputation of the sending server
- Whether the content of your email is considered spammy
- How recipients interact with your messages in terms of open rates and clicks
- The authentication measures you have in place to prove that your emails are legitimate.

By implementing SPF, DKIM, DMARC, and BIMI, you’re not only improving your email deliverability but also protecting your organization’s brand, reputation, and security. These protocols help email providers identify and trust your messages, reducing the chances that they will end up in the spam folder or be rejected entirely.

Although setting up these protocols may seem technical, they’re well worth the effort. Work with your email provider or IT team to get these records set up correctly, and monitor them regularly to ensure that your emails continue to reach your supporters’ inboxes.

With a bit of effort, you’ll build a stronger, more trusted relationship with your audience — and that means better outcomes for your nonprofit’s mission.

Tag(s):## Growing a Quality Email List for Your Nonprofit

Learn More

[View original](https://www.truesense.com/blog/growing-a-quality-email-list-for-your-nonprofit)[

## Email Marketing for Nonprofits: The Science of Subject Lines

Learn More

](https://www.truesense.com/blog/email-marketing-for-nonprofits-subject-lines)[

## What Nonprofits Need to Know About GoFundMe’s Unauthorized Nonprofit Pages

Learn More

](https://www.truesense.com/blog/what-nonprofits-need-to-know-about-gofundmes-unauthorized-nonprofit-pages)
