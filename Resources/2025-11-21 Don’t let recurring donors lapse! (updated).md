---
categories:
  - Clippings
authors:
  - '[[Mark Ristaino]]'
url: >-
  https://blog.actionkit.com/dont-let-recurring-donors-lapse-updated/?utm_source=www.civicshoutnewsletter.com&utm_medium=newsletter&utm_campaign=what-happens-when-a-recurring-charge-fails&_bhlid=f7fdb2e7d6a6b921c214d184574cb76b04f71e78
source: >-
  [[Archives/2025-11-21 Don’t let recurring donors lapse! (updated)|2025-11-21
  Don’t let recurring donors lapse! (updated)]]
published: '2025-11-21'
created: '2026-06-30'
relevance: średnia
tags:
  - fundraising
  - narzędzia-AI
---
# Don't let recurring donors lapse! (updated)

Artykuł [[Mark Ristaino|Marka Ristaino]] (ActionKit) to techniczny poradnik, jak odzyskiwać darczyńców rekurencyjnych, których karty płatnicze wygasają lub nie przechodzą. Autor pokazuje ośmiokrokowy workflow w [[ActionKit]]: od stworzenia stron "Update"/"Cancel" dla darowizn cyklicznych, przez login string ułatwiający donorowi dostęp do profilu bez logowania, aż po skonfigurowanie cyklicznego mailingu targetowanego na "kartach wygasających w przyszłym miesiącu". Tekst jest praktyczny i produktowy — skierowany do organizacji korzystających konkretnie z ActionKit, ale logika procesu (proaktywne wykrywanie wygasających kart, uproszczony login, automatyzacja mailingu) jest uniwersalna dla każdego CRM fundraisingowego.

## Frameworki i metody

**8-krokowy workflow odzyskiwania recurring donorów:**
1. Stwórz stronę ActionKit typu "Update Recurring Donation" lub "Cancel Recurring Donation".
2. Wygeneruj login string donora — pozwala ominąć ekran logowania i przenieść darczyńcę bezpośrednio do jego profilu z poziomu maila.
3. Stwórz mailing informujący o wygasającej karcie i możliwości jej aktualizacji.
4. Podlinkuj mailing do strony update przez login string.
5. Przetestuj cały proces na własnym koncie z aktywną darowizną cykliczną.
6. Targetuj mailing wbudowanym raportem "Donors Whose Cards Expire Next Month".
7. Ustaw mailing jako cykliczny (set it and forget it).
8. Skonfiguruj serię mailingu cyklicznego z wykluczeniami, by nie wysyłać powtórnie do osób, które niedawno dostały tę wiadomość.

## Wnioski

- Recurring donorzy to często najbardziej zaangażowani wspierający — proaktywne wykrywanie wygasających kart zapobiega niepotrzebnej utracie ich wsparcia.
- Automatyzacja (login string + cykliczny mailing) pozwala prowadzić ten proces bez ręcznej pracy zespołu — "ustaw i zapomnij".
- Warto ostrzegać darczyńców, by nie przekazywali dalej maila z login stringiem, bo link loguje odbiorcę jako darczyńcę bez hasła.

## Zastosowanie

Przydatne jako wzorzec procesu przy doradztwie dla organizacji korzystających z innego CRM/ESP niż ActionKit — logikę (raport wygasających kart, uproszczony login, cykliczny mailing z wykluczeniami) można przenieść np. do rekomendacji dla klientów pytających o retencję recurring donorów.
