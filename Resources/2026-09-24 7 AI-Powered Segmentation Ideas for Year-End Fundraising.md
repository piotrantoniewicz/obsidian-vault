---
categories:
  - Clippings
authors: ["[[Nathan Hill]]"]
url: "https://fast.wistia.com/embed/transcripts/ivlirgjghp.html"
source: "[[Archives/2026-09-24 7 AI-Powered Segmentation Ideas for Year-End Fundraising|2026-09-24 7 AI-Powered Segmentation Ideas for Year-End Fundraising]]"
created: 2026-09-24
relevance: wysoka
tags:
  - "fundraising"
  - "narzędzia-AI"
  - "automatyzacja"
---

# 7 AI-Powered Segmentation Ideas for Year-End Fundraising

Zapis webinaru firmy Avid (dostawca „AI fundraising operating system") o wykorzystaniu AI do segmentacji darczyńców przed sezonem end-of-year. Główne ostrzeżenie: sama liczba segmentów nie poprawia wyników — nadmierna segmentacja bez pokrycia w danych to praca bez efektu, warto segmentować tam, gdzie dane wskazują konkretny problem lub okazję (np. słaba retencja recurring donors). Prowadzący opisują bezpieczny proces użycia AI do segmentacji (surowe dane → anonimizacja/tokenizacja → wytrenowanie AI na słowniku organizacji → budowanie segmentów w rozmowie) oraz siedem konkretnych pomysłów na segmenty pod kampanię końcoworoczną. Materiał częściowo promocyjny (produkt Avid), ale warstwa metodologiczna i lista segmentów są przenaszalne na inne narzędzia (Claude, ChatGPT) i inne CRM.

## Frameworki i metody

**Bezpieczny proces użycia AI do segmentacji (4 kroki):**
1. Zbierz dane na poziomie pojedynczego darczyńcy — dane zagregowane nie wystarczą; potrzeba danych surowych łączących historię darowizn z danymi zaangażowania (maile, wydarzenia, wolontariat).
2. Zanonimizuj dane przed przekazaniem AI — nigdy nie przekazuj [[LLM]] danych identyfikujących (e-mail, adres, ID darczyńcy); zastąp je losowym tokenem, który można później dopasować z powrotem do rekordu w bezpiecznym systemie.
3. Wytrenuj AI na słowniku organizacji — zdefiniuj kanały (mail, direct mail, face-to-face), poziomy dawania (broad/mid/major/mega) i cykl życia darczyńcy, zanim AI zacznie budować segmenty.
4. Buduj segmenty w rozmowie z AI i iteruj — np. „stwórz listę uśpionych darczyńców zaangażowanych mailowo", łącząc kilka warstw danych naraz.

**Siedem pomysłów na segmentację pod kampanię końcoworoczną (plus jeden bonusowy):**
1. Darczyńcy średniego poziomu (mid-level) — budowanie „matchu" na mniejszą skalę, analogicznego do dopasowań dla dużych darczyńców.
2. Model skłonności do awansu na mid-level wśród darczyńców podstawowych (broad-based).
3. Reaktywacja uśpionych darczyńców — z podaniem kwoty i daty ostatniej darowizny w treści maila.
4. Darczyńcy cykliczni (recurring) — nie wykluczać ich z kampanii końcoworocznej, tylko wersjonować komunikację.
5. Aktywacja nowych darczyńców cyklicznych — model skłonności do konwersji na recurring wśród niedarczyńców i darczyńców jednorazowych.
6. Darczyńcy niezaangażowani mailowo — retargeting wielokanałowy (Meta, Google Ads) zamiast polegania wyłącznie na mailu.
7. Najbardziej prawdopodobni dawcy dużych darowizn (major gift) — przekazanie listy do gift officerów zamiast masowej wysyłki.
8. Bonus — lista wykluczeń: darczyńcy, którzy dali w ciągu ostatnich 30 dni, żeby nie zasypywać ich prośbami zaraz po darowiźnie.

## Kluczowe dane
- Test maila reaktywacyjnego z podaniem kwoty i daty ostatniej darowizny: +247% konwersji.
- Ok. 30% darczyńców cyklicznych robi dodatkowy jednorazowy dar rocznie; mediana dodatkowej kwoty to 77 USD (2–3x wysokość ich daru cyklicznego).
- Tylko 7% organizacji odnotowuje istotny strategiczny wpływ inwestycji w AI (dane Fundraising AI).

## Wnioski
- Sama liczba segmentów nie poprawia wyników — segmentować warto tam, gdzie dane wskazują konkretną okazję lub problem, inaczej to praca bez efektu.
- Darczyńcy cykliczni to niewykorzystany potencjał dodatkowego przychodu — traktowanie ich jako „już zdobytych" i pomijanie w kampaniach końcoworocznych jest błędem.
- Bezpieczne użycie AI w fundraisingu wymaga świadomej anonimizacji danych — surowe dane darczyńców (PII) nie powinny trafiać do ogólnodostępnych modeli [[LLM]].

## Zastosowanie
Gotowy materiał do warsztatu lub checklisty dla klientów NGO planujących kampanię end-of-year — zwłaszcza proces anonimizacji danych przed użyciem AI oraz lista segmentów jako punkt wyjścia do audytu bazy darczyńców. Przydatne też jako punkt odniesienia dla dobryai.pl: pokazuje, że firmy trzeciej strony już budują produkty wokół tego samego problemu, który można rozwiązywać indywidualnie dla mniejszych organizacji.
