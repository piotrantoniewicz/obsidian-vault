---
type: Web
authors: '[[Kimberly Huang]]'
url: >-
  https://www.litmus.com/blog/what-is-microsoft-snds-why-your-deliverability-strategy-depends-on-it?ck_subscriber_id=3412528627&utm_source=convertkit&utm_medium=email&utm_campaign=%F0%9F%92%BB%20open%20tabs%20%7C%208%20questions%20to%20ask%20before%20investing%20in%20another%20tool%20-%2022847181&sh_kit=ebb8f2fb51f8b6f5b192f8b07d9aae25086a45840059610b97f734dbb8655eb6
published: 2023-09-25T00:00:00.000Z
created: 2026-08-10T00:00:00.000Z
tags:
  - digital-campaigning
---


### Key takeaways ✨

- Microsoft SNDS is a free, IP-based postmaster tool that reveals how Outlook, Hotmail, and Live see your sending reputation across 350+ million mailboxes.
- In 2026, SNDS moved to a new URL, shifted reporting to a REST API with OAuth 2.0, and standardized JMRP complaint feeds to headers-only data—breaking automated workflows built on the old system.
- Senders need to audit SNDS ownership, IP address coverage, and automated data pulls now, since 30-day link expirations and stripped-down complaint reports can silently create monitoring blind spots.

Microsoft’s [Smart Network Data Services](https://substrate.office.com/ip-domain-management-snds/SNDS) (SNDS) is a free postmaster tool that shows how your sending IPs are performing across Outlook, Hotmail, and Live—more than 350 million accounts. Unlike [Google Postmaster Tools](https://www.gmail.com/postmaster/) (domain-based), SNDS is IP-based: you need ownership of the IPs you send from to register.

SNDS surfaces sending volume, spam trap hits, filter status, and complaint rates. Think of it as a report card from Microsoft. It doesn’t fix anything; it tells you where to look.

It might sound complex, but it doesn’t have to be. Here’s a quick breakdown of how to use it and what’s changing in 2026.

## How to use SNDS data

Most senders only check SNDS after something breaks. Use it proactively instead.

**Watch filter status daily**. Green is healthy. Yellow is a warning. Red means mail is likely junked or blocked. Don’t wait for red!

**Treat spam trap hits as urgent**. Even a few signal list hygiene problems. Audit acquisition and suppression practices immediately.

**Track spam complaint rates over time**. A spike often appears in SNDS days before it shows up in your ESP. Compare trends against recent campaigns.

**Pair it with your ESP’s reporting**. SNDS shows what Microsoft sees; your ESP shows what you sent. If your ESP reports strong delivery but SNDS shows yellow, mail may be landing in junk.

## What changed in 2026

The underlying data SNDS surfaces is the same, but the delivery mechanisms changed enough to break workflows that teams had been running on autopilot. Four things shifted in 2026:

1. **Authentication is now required for network access management**. Since late 2025, approving or denying IP ranges requires authentication.
2. **SNDS moved to a new URL on June 8, 2026**.The old portal may redirect temporarily, but treat any hardcoded URL as expired. IP Status and IP Data reports moved to a REST API; automated CSV links now expire after 30 days.
3. **There is now a REST API with OAuth 2.0**. It supports optional date and IPv4 filtering, and is the better long-term path for pulling SNDS data programmatically.
4. **JMRP is now ARF-standardized and privacy-trimmed**. Complaint reports no longer include the full message body—only selected headers. Complaint sample downloads are discontinued. Any JMRP feed not linked to an SNDS account has been removed.

## Why the new SNDS changes break monitoring

Sender reputation problems surface slowly—often days after the damage is already accumulating. SNDS helps you catch issues earlier, but only when data is actually reaching you. For example, a 30-day automated link that expires mid-quarter and starts returning errors is easy to miss: your reporting just stops refreshing while everything looks normal. The same goes for scripts still pointed at the old portal, or JMRP parsers expecting a message body that no longer arrives.

Build in detection—flag zero-row downloads, approaching link expiry, and unexpected parse results—so gaps in coverage don’t go unnoticed.

## What to audit now

Here are a few things you should start auditing today to make sure SNDS is working and the data is actionable.

- Confirm the Microsoft account behind SNDS is active and owned by a current team member.
- Review IP coverage—add active sending IPs, remove ranges you no longer control.
- Inventory every script, cron job, and dashboard pulling SNDS CSV data and flag anything on an automated access link.
- Document link expiry: who owns it, where it’s used, how a failure gets detected.
- Update JMRP processing to map complaints from headers, not message bodies.
- Migrate to the OAuth 2.0 REST API as your long-term pull mechanism.

## Updating your complaint mapping

Without message bodies, complaint traceability now depends entirely on headers and stable metadata. Make sure your system can connect a complaint to its source using:

- Message-ID, campaign ID / customer ID
- Sending IP and mail stream
- DKIM selector / Return-Path domain
- Authentication-Results / Received-SPF

If you can’t trace a complaint to a campaign or sending stream, your abuse response slows down—and that matters most for ESPs and anyone sending across multiple brands.

## SNDS is one signal, not the whole picture

SNDS shows how Microsoft sees your IPs—not why they’re seeing it that way. For root cause, you need more: DMARC monitoring to catch authentication and alignment failures, SPF/DKIM health checks for configuration gaps, and blocklist monitoring to spot reputation flags on other networks. SNDS is your early warning from Microsoft’s side of the fence; the rest of your stack tells you where to dig.

## The bottom line

The 2026 changes are a good prompt to make sure someone on your team actually owns SNDS—and that ownership means more than logging in when something goes wrong. Review your access, update the workflows that pull data from it, get your JMRP mapping into shape, and confirm there’s a clear path from signal to action. Outlook is too large an audience to leave unmonitored.

Looking for more deliverability tips for Microsoft? Check out Validity’s [2026 Email Deliverability Benchmark Report](https://www.validity.com/resource-center/2026-email-deliverability-benchmark-report/).

Julie Stuck is a Sr. Email Strategist at Validity.
