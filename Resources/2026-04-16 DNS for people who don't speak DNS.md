---
categories: Clippings
authors: ["[[Sara Cederberg]]"]
url: "https://www.civicshoutnewsletter.com/p/dns-for-people-who-don-t-speak-dns?utm_source=www.civicshoutnewsletter.com&utm_medium=newsletter&utm_campaign=why-your-fundraising-emails-need-their-own-subdomain&_bhlid=008d17bdd515e7d2b244814cda02291022bbaae8"
source: "[[Archives/2026-04-16 DNS for people who don't speak DNS|2026-04-16 DNS for people who don't speak DNS]]"
published: 2026-04-16
created: 2026-05-29
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
---

# DNS for people who don't speak DNS

Artykuł wyjaśnia w przystępny sposób trzy kluczowe rekordy DNS odpowiadające za dostarczalność emaili: SPF, DKIM i DMARC. Autorka tłumaczy, że bez tych rekordów emaile organizacji mogą lądować w spamie lub być blokowane, szczególnie od 2024 roku, gdy Google i Yahoo zaostrzyły wymagania dla masowych nadawców. Artykuł jest praktyczny: podaje narzędzie diagnostyczne ([[MXToolbox]]) i pokazuje ścieżkę dojścia do pełnej ochrony domeny.

## Frameworki i metody

- **SPF (Sender Policy Framework)** — lista serwerów uprawnionych do wysyłania emaili w imieniu domeny; jeśli platformy emailowej nie ma na liście, jej wiadomości mogą być uznane za podejrzane
- **DKIM (DomainKeys Identified Mail)** — cyfrowa pieczęć woskowa na każdym emailu; pozwala serwerowi odbiorczemu sprawdzić, że wiadomość nie była modyfikowana w drodze
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** — łączy SPF i DKIM; mówi providerom co robić z emailami, które nie przechodzą uwierzytelnienia: przepuścić (`none`), skierować do spamu (`quarantine`), odrzucić (`reject`)
- **Ścieżka dojrzewania DMARC**: `none` → `quarantine` → `reject`; wymagana do aktywacji [[BIMI]] (wyświetlanie logo w skrzynce)

## Wnioski

- Od 2024 r. SPF, DKIM i DMARC są obowiązkowe dla nadawców powyżej 5 000 emaili dziennie do Gmaila i Yahoo; [[Microsoft]] dołączył z podobnymi zasadami dla Outlooka w maju 2025 — organizacje, które tego nie wdrożyły, ryzykują blokadą
- Polityka DMARC `none` to jedynie monitoring — nie chroni domeny przed phishingiem ani nie poprawia dostarczalności; trzeba przejść do `quarantine` i docelowo `reject`
- Diagnostykę można zacząć od [[MXToolbox]] — darmowe narzędzie, które sprawdza konfigurację SPF, DKIM i DMARC dla dowolnej domeny

## Zastosowanie

W pracy z NGO prowadzącymi email fundraising ten artykuł można wykorzystać jako punkt wejścia do rozmowy o infrastrukturze emailowej — szczególnie z organizacjami, które nigdy nie robiły przeglądu higieny technicznej. Warto polecić [[MXToolbox]] jako pierwszy krok samodzielnej diagnozy przed większą zmianą platformy.
