---
categories:
  - "Emails"
published: 2026-05-26
created: 2026-05-27
labels:
  - "Civic Shout"
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
  - "organizacje-społeczne"
---

# Why your fundraising emails need their own subdomain

Newsletter Civic Shout autorstwa Sary Cederberg wyjaśnia, dlaczego organizacje non-profit powinny oddzielić swoje subdomeny mailowe dla kampanii fundraisingowych i wiadomości transakcyjnych. Gmail i Yahoo coraz silniej opierają decyzje o dostarczaniu na reputacji domeny — nie IP — co sprawia, że jedna nieudana wysyłka może zablokować potwierdzenia darowizn. Subdomena tworzy warstwę ochrony: problemy z kampanią marketingową nie uderzają bezpośrednio w reputację transakcyjną. To konkretna rekomendacja infrastrukturalna dla organizacji prowadzących regularny email marketing.

## Frameworki i metody

- **Dwie subdomeny jako minimum** — jedna dla kampanii fundraisingowych i marketingowych (np. `email.example.org`), druga dla wiadomości transakcyjnych (np. `notify.example.org`); mailbox providers traktują je oddzielnie
- **Autentykacja per subdomena** — każda subdomena wymaga własnych rekordów SPF, DKIM i DMARC; bez tego reputacja jest niezdefiniowana
- **Warmup subdomeny** — na shared IP: 1–2 tygodnie, zaczynając od najbardziej zaangażowanych subskrybentów; na dedicated IP: 4–8 tygodni
- **Monitoring w [[Google Postmaster Tools]]** — bezpłatne śledzenie reputacji osobno dla każdej subdomeny; szczególnie ważne w sezonie wysokich wolumenów

## Kluczowe dane

- Reputacja domeny jest przez Gmail traktowana co najmniej tak samo ważnie jak reputacja IP — i staje się głównym czynnikiem decydującym o dostarczalności
- Ponad 1 000 organizacji korzysta z Civic Shout do pozyskiwania darczyńców i aktywistów

## Wnioski

- Separacja subdomeny kampanijnej od transakcyjnej to prosta zmiana infrastrukturalna, która chroni potwierdzenia darowizn przed wylądowaniem w spamie — kluczowe przy prowadzeniu [[fundraising|digital fundraising]] dla NGO
- Mailbox providers (zwłaszcza Gmail) zbliżają się do modelu, w którym reputacja domeny determinuje inbox — organizacje bez subdomeny narażają się na efekt domino po każdej słabej wysyłce kampanijnej
- Wdrożenie [[Google Postmaster Tools]] jako standardowego elementu monitoringu deliverability jest szczególnie ważne dla organizacji używających [[Impact Stack]] lub podobnych platform

## Cytat

> „Reputacja przypisana do Twojej domeny to nie jeden z czynników — to coraz bardziej THE faktor."

## Zastosowanie

Wdrażając kampanie email dla klientów NGO, warto jako standard rekomendować konfigurację subdomeny kampanijnej i transakcyjnej — szczególnie gdy organizacja prowadzi regularne wysyłki fundraisingowe w [[Impact Stack]] czy MailChimp. To niska złożoność techniczna, ale wysoka wartość ochronna. Temat można włączyć do modułu o deliverability w kursie „Fundraising z AI".
