---
categories: Clippings
authors: ["[[Jesse Sumrak]]"]
url: "https://www.twilio.com/en-us/blog/insights/email-reputation-101-ip-reputation-vs-domain-reputation"
source: "[[Archives/2025-07-23 IP Reputation vs. Domain Reputation Guide for Email Senders|2025-07-23 IP Reputation vs. Domain Reputation Guide for Email Senders]]"
published: 2025-07-23
created: 2026-05-29
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
---

# IP Reputation vs. Domain Reputation Guide for Email Senders

Artykuł [[Twilio]] wyjaśnia różnicę między reputacją IP a reputacją domeny i dlaczego obie mają znaczenie dla dostarczalności emaili. Reputacja IP jest powiązana z konkretnym adresem IP — stosunkowo łatwa do odbudowania (2–4 tygodnie), ale wspólna w przypadku shared IP. Reputacja domeny jest przenośna — podąża za nadawcą niezależnie od zmiany providera czy IP, a jej odbudowa trwa 6–12 tygodni. Współczesne providery, w tym Gmail, coraz bardziej priorytetyzują reputację domeny nad IP.

## Frameworki i metody

- **Kluczowe czynniki reputacji IP**: spójność wolumenu wysyłek, wskaźnik odrzuceń (bounce rate), skargi spamowe, wyniki uwierzytelniania, zaangażowanie (otwarcia, kliknięcia), obecność na blacklistach; skala 0–100, powyżej 80 = dobra, poniżej 70 = problemy
- **Kluczowe czynniki reputacji domeny**: wiek i historia domeny, autorytet strony, zgodność z DMARC, spójność podpisów DKIM, użycie subdomeny vs domeny głównej
- **Narzędzia do monitorowania**: Sender Score, Microsoft SNDS, Google Postmaster Tools — warto korzystać z kilku jednocześnie

## Wnioski

- Zmiana platformy emailowej lub IP nie resetuje reputacji domeny — jeśli domena ma złą historię, problem przenosi się razem z nią, dlatego reputacja domeny powinna być priorytetem strategicznym
- Emaile transakcyjne i marketingowe powinny być wysyłane z osobnych adresów IP — mieszanie ich obniża dostarczalność wiadomości transakcyjnych
- Warmup nowego IP jest konieczny przed wysyłką do całej listy — wysyłanie od najbardziej zaangażowanych segmentów buduje pozytywny sygnał dla providerów

## Cytat

> Reputacja IP to wynajem krótkoterminowy — można się przeprowadzić i zacząć od nowa. Reputacja domeny to stały adres — podąża za tobą wszędzie.

## Zastosowanie

Ten artykuł uzupełnia case study HSU o fundament techniczny: organizacje NGO, które planują migrację platformy emailowej lub mają problemy z dostarczalnością, powinny zrozumieć, że zmiana narzędzia nie wystarczy — reputacja domeny pozostaje. Warto włączyć to rozróżnienie do kursów szkoleniowych z fundraisingu emailowego.
