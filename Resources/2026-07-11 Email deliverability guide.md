---
categories:
  - Clippings
authors: ["[[ECDA]]"]
url: "https://www.centerfordigitalaction.eu/resources/technology/email-deliverability-guide?source=newsletter&email_referrer=email_3305908&email_subject=hows-your-content-looking&can_id=32cae499f95a9349c734a72403321b9c&link_id=12"
source: "[[Archives/2026-07-11 Email deliverability guide|2026-07-11 Email deliverability guide]]"
created: 2026-07-11
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
---

# Email deliverability guide

Poradnik European Center for Digital Action wyjaśnia deliverability e-maili: zdolność dotarcia wiadomości do głównej skrzynki odbiorczej zamiast spamu czy zakładki promocje. Autorzy tłumaczą techniczne podstawy (SPF, DKIM, DMARC), proces migracji na nowe narzędzie mailingowe (rekomendują ActionNetwork) oraz sposób oceny zdrowia listy kontaktów. Całość zamyka zestaw dobrych praktyk: opt-in, sekwencja powitalna, usuwanie nieaktywnych, segmentacja i praca na danych. To praktyczny, techniczny przewodnik przydatny każdej organizacji prowadzącej kampanie mailowe do darczyńców i wspierających.

## Frameworki i metody

**Konfiguracja deliverability przy nowym/migrowanym mailerze — 3 kroki:**

1. **Kup domenę** — własna domena jest podstawą profesjonalnego wizerunku i pozwala ustawić parametry deliverability.
2. **Skonfiguruj SPF, DKIM i (przy liście 5000+) DMARC** — dedykowane wsparcie oferują helpdeski narzędzi mailingowych; poprawność można zweryfikować checkerem takim jak InboxAlly.
3. **Rozgrzej listę kontaktów** — podziel listę na małe losowe grupy, wysyłaj stopniowo (np. od 500 do całej bazy w ciągu kilku tygodni), monitoruj wyniki i usuwaj adresy z bounce. Efekt: podział na listę „ciepłą" (otwierającą) i „zimną" (niereagującą).

**6 dobrych praktyk utrzymania zdrowej listy:** dobra polityka opt-in (wymóg RODO), sekwencja powitalna dla nowych kontaktów, usuwanie lub reaktywacja nieaktywnych (6-12 miesięcy bez otwarcia), treści angażujące z jasnym CTA, precyzyjna segmentacja odbiorców, monitorowanie statystyk jako busoli do dalszych działań.

## Wnioski
- Deliverability to nie efekt wysyłki, tylko wynik technicznej konfiguracji (SPF/DKIM/DMARC) połączonej z higieną listy — jedno bez drugiego nie wystarczy.
- Rozgrzewanie listy przy migracji na nowe narzędzie (np. [[ActionNetwork]]) to proces rozłożony na tygodnie, nie jednorazowa wysyłka do całej bazy.
- DMARC jest wymagany dopiero od 5000 kontaktów — mniejsze organizacje mogą zacząć od samego SPF i DKIM.

## Zastosowanie
Bezpośrednio przydatne przy doradztwie organizacjom społecznym wdrażającym lub migrującym system mailingowy — checklistę SPF/DKIM/DMARC i proces rozgrzewania listy można wykorzystać jako gotowy protokół wdrożeniowy. Warto też jako materiał do kursu mailowego o fundraisingu.
