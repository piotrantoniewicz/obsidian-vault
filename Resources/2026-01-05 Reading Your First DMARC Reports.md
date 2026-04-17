---
categories: Clippings
authors:
  - '[[Kimberly Huang]]'
url: 'https://www.litmus.com/blog/reading-first-dmarc-reports'
source: >-
  [[Archives/2026-01-05 Reading Your First DMARC Reports|2026-01-05 Reading Your
  First DMARC Reports]]
published: '2026-01-05'
created: '2026-03-22'
relevance: średnia
tags:
  - digital-campaigning
  - fundraising
  - automatyzacja
---
# Reading Your First DMARC Reports

Artykuł [[Kimberly Huang]] z bloga [[Litmus]] wyjaśnia, jak interpretować raporty agregujące DMARC i co z nimi robić w praktyce. DMARC (Domain-based Message Authentication, Reporting, and Conformance) chroni domenę przed phishingiem i spoofingiem, a jego raporty ujawniają, które emaile przechodzą autoryzację, z jakich serwerów są wysyłane i jakie działania podejmują serwery odbierające. Artykuł skupia się na trzech priorytetowych elementach analizy: legalnych emailach failujących autoryzację, nieznanych adresach IP próbujących wysyłać w imieniu domeny oraz skuteczności egzekwowania polityki DMARC. Praktyczna wartość: właściwa konfiguracja DMARC bezpośrednio przekłada się na dostarczalność emaili — co jest fundamentem skutecznych kampanii fundraisingowych i cyfrowych.

## Frameworki i metody

- **Analiza raportów DMARC** — trzyetapowy proces interpretacji danych:
  1. Zidentyfikuj legalne emaile failujące autoryzację (błędna konfiguracja [[SPF]] lub [[DKIM]]) → zaktualizuj rekordy DNS
  2. Sprawdź nieznane adresy IP wysyłające w imieniu domeny → zaostrzenie polityki z `p=none` na `quarantine` lub `reject`
  3. Zweryfikuj, czy polityka DMARC jest faktycznie egzekwowana przez serwery odbierające

## Wnioski

- Polityka DMARC ustawiona na `p=none` jest aktywnie wykorzystywana przez phisherów — przejście na `quarantine` lub `reject` jest niezbędne dla ochrony reputacji domeny wysyłającej kampanie [[digital-campaigning]].
- Błędna konfiguracja SPF lub DKIM może powodować, że legalne emaile organizacji trafiają do spamu — to bezpośrednie zagrożenie dla skuteczności kampanii [[fundraising]]owych.
- Regularne czytanie raportów DMARC to element [[automatyzacja|higieny technicznej]] każdej organizacji prowadzącej komunikację emailową — warto wdrożyć jako rutynowy proces, nie akcję jednorazową.

## Zastosowanie

Przy wdrożeniach email marketingu dla NGO warto sprawdzić konfigurację DMARC jako jeden z pierwszych kroków technicznych — błędy tu mogą niwelować efekty nawet najlepiej napisanych apeli fundraisingowych. Temat można włączyć do kursu "Fundraising z AI" jako element modułu o technicznej infrastrukturze emaila. Przydatne też przy audytach email deliverability u klientów.
