---
categories:
  - Emails
created: '2026-09-22'
labels:
  - Send It Right
published: '2026-09-22'
relevance: wysoka
tags:
  - digital-campaigning
  - fundraising
---
# Send It Right: How to Diagnose and Fix Deliverability Disasters

Autorka newslettera Send It Right przedstawia systematyczny proces diagnozowania i naprawy kryzysów deliverability e-mail — od rozpoznania sygnałów ostrzegawczych, przez ustalenie przyczyny problemu, po wdrożenie poprawek i budowę odporności programu na przyszłość. Główna teza: najczęstszym błędem nadawców jest naprawianie objawów bez zdiagnozowania przyczyny, co tylko wydłuża czas powrotu do skrzynek odbiorczych. Tekst kładzie nacisk na dyscyplinę działania — zmieniać jedną rzecz naraz, monitorować metryki osobno dla każdego dostawcy poczty i dokumentować wnioski jako część post-mortem.

## Frameworki i metody
- **Krok 1: Jak rozpoznać kryzys** — nagłe spadki wyników (opens, kliknięcia, konwersje), skargi odbiorców, flagi compliance od ESP, alerty z narzędzi deliverability, np. [[Google Postmaster Tools]]
- **Krok 2: Diagnoza, nie łatanie** — ustal, kiedy zaczął się spadek, gdzie występuje (który dostawca poczty jest dotknięty) i co zmieniło się po stronie nadawcy (nowa kampania, nowy segment, zmiana częstotliwości, zmiana platformy lub DNS)
- **Krok 3: Działaj strategicznie, nie desperacko** — wygaś nieaktywnych odbiorców, spowolnij tempo wysyłki, sprawdź uwierzytelnianie (SPF, DKIM, DMARC), zmieniaj jedną rzecz naraz, monitoruj metryki codziennie per dostawca poczty, eskaluj do ESP z konkretami (daty, objawy, kontekst, wprowadzone zmiany)
- **Krok 4: Debriefing i post-mortem** — udokumentuj oś czasu zdarzenia, zbuduj lub zaktualizuj plan awaryjny, przejrzyj strategię wysyłkową, przeszkol zespół w zakresie tego, co szkodzi deliverability
- **Krok 5: Napraw przyczyny strukturalne** — zdefiniuj politykę re-engagementu i sunsetu, segmentuj wg realnego zaangażowania (kliknięcia, konwersje, nie tylko otwarcia), dopasuj treść i częstotliwość do oczekiwań z momentu zapisu, zadbaj o podstawy (tekst w mailu, wersja mobilna, działający link wypisu)
- **Krok 6: Buduj odporność, nie żal** — utrzymuj czyste, oparte na zgodzie listy, ustalaj i wzmacniaj oczekiwania odbiorców, monitoruj trendy deliverability regularnie (co najmniej raz w miesiącu)

## Kluczowe dane
- Wskaźnik skarg spamowych powinien pozostać poniżej 0,1%; wzrost powyżej 0,03% — nawet jednorazowy — wymaga sprawdzenia treści, segmentacji i źródeł listy
- Poprawa deliverability po wdrożeniu zmian następuje zwykle w ciągu kilku dni do kilku tygodni, w zależności od skali problemu

## Wnioski
- Niski open rate przy jednocześnie zerowym wskaźniku skarg to sygnał, że mail ląduje w spamie, a nie w skrzynce głównej — [[Google Postmaster Tools]] pozwala to zweryfikować osobno dla każdego dostawcy poczty
- Narzędzia typu GlockApps czy Validity opierają się głównie na testach seedowych i dają tylko orientacyjny obraz miejsca doręczenia — nie warto traktować ich jako ostatecznego wyroczni
- Eskalacja do postmastera ma sens dopiero po usunięciu przyczyny problemu, a wcześniejsza, uczciwa komunikacja z ESP (konkretne daty, kontekst, opisane zmiany) skraca czas rozwiązania sprawy

## Cytat
> Nie da się naprawić czegoś, czego się nie rozumie — nawet drobna zmiana może wywołać efekt domina w dole lejka.

## Zastosowanie
Sześciostopniowy framework można wykorzystać jako checklistę przy monitorowaniu kampanii mailowych klientów NGO (np. w ramach dobryai.pl) oraz jako materiał referencyjny w kursie mailowym o fundraisingu z AI, przy budowaniu procedur reagowania na kryzysy deliverability.
