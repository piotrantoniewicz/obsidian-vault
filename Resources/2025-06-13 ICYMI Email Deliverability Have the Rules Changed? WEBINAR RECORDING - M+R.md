---
categories: Clippings
authors:
  - '[[Anne Paschkopić]]'
  - '[[Josh VanDavier]]'
url: >-
  https://www.mrss.com/lab/icymi-email-deliverability-have-the-rules-changed-webinar-recording/
source: >-
  [[Archives/2025-06-13 ICYMI Email Deliverability Have the Rules Changed?
  WEBINAR RECORDING - M+R|2025-06-13 ICYMI Email Deliverability Have the Rules
  Changed? WEBINAR RECORDING - M+R]]
published: '2025-06-13'
created: '2026-04-05'
relevance: wysoka
tags:
  - fundraising
  - digital-campaigning
---
# ICYMI Email Deliverability Have the Rules Changed? WEBINAR RECORDING - M+R

Nagranie webinaru [[M+R]] prowadzonego przez [[Anne Paschkopić]] (M+R) i [[Josh VanDavier]] ([[Trust for Public Land]]) poświęconego zmianom w zasadach dostarczalności emaili przez Google, Microsoft i Yahoo. Kluczowy wniosek: dostarczalność stała się bardziej wymagająca — dostawcy skrzynek znacznie zaostrzyli kryteria dotyczące reputacji nadawcy, co wymaga aktywnego zarządzania listą i segmentacji odbiorców. Webinar koncentruje się na praktykach higieny list, obsłudze nieaktywnych subskrybentów oraz poprawnej konfiguracji technicznej (DMARC, SPF, DKIM). Zapis Q&A ujawnia konkretne problemy, z którymi mierzą się organizacje — w tym specyficzne trudności z domenami Microsoft.

## Frameworki i metody

- **Segmentacja według zaangażowania przed wysyłką** — wysyłanie najpierw do najbardziej aktywnych odbiorców, by budować pozytywne sygnały przed dotarciem do mniej zaangażowanych; rekomendowane przy problemach z dostarczalnością
- **Monitorowanie reputacji domeny według dostawcy** — śledzenie open rate i CTR osobno dla domen Gmail (Google Postmaster), Microsoft (SNDS) i innych; problemy ograniczone do jednej domeny wskazują na konieczność zaostrzenia kryteriów higieny dla tej domeny
- **Higiena listy według domeny** — dla niektórych domen akceptowalny próg nieaktywności to 3 miesiące, dla innych 9 i więcej; brak problemów = nie ma potrzeby radykalnej zmiany; problemy = zawężanie grupy do aktywnych odbiorców

## Kluczowe dane

- Google i Yahoo ogłosiły (i wdrożyły) nowe wymagania dla nadawców masowych — DMARC, SPF, DKIM stały się obowiązkowe
- Microsoft domeny wykazują znacząco niższe open rates w 2025 r. w porównaniu z poprzednimi latami — problem zgłaszany przez wielu klientów M+R

## Wnioski

- Ciągłe wysyłanie do nieangażujących się odbiorców trwale niszczy reputację nadawcy — [[ISP]] interpretuje to jako spam i filtruje wiadomości; konieczne aktywne zarządzanie suppression
- Folder Promotions w Gmail nie jest katastrofą — użytkownicy często oczekują tam emaili marketingowych i rzadziej oznaczają je jako spam, co może chronić reputację nadawcy
- Metryki dostarczalności należy analizować per domena i per typ emaila (fundraising vs newsletter) — globalne open rates maskują rzeczywiste problemy u konkretnych dostawców

## Zastosowanie

Dla organizacji NGO prowadzących email fundraising i email-to-target kampanie poprawna konfiguracja techniczna (DMARC, SPF, DKIM) i regularna higiena listy to warunek skuteczności — bez tego budżety na kampanie emailowe przepadają na spamie. W kursie Fundraising z AI warto uwzględnić moduł o dostarczalności jako element podstaw efektywnej komunikacji emailowej z bazą darczyńców.
