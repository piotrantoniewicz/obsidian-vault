---
categories: Clippings
authors: ["[[Rachel Wolan]]"]
url: https://www.youtube.com/watch?v=BTcG59ZR9sg
source: "[[Archives/2025-12-29 How Webflow s CPO built an AI chief of staff to manage her calendar and drive internal AI adoption|2025-12-29 How Webflow s CPO built an AI chief of staff to manage her calendar and drive internal AI adoption]]"
published: 2025-12-29
created: 2026-05-12
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "szkolenia-AI"
---

# How Webflow's CPO built an AI chief of staff to manage her calendar and drive internal AI adoption

[[Rachel Wolan]], CPO [[Webflow]], zbudowała od zera osobistą aplikację AI zarządzającą jej kalendarzem, emailem i przygotowaniem do spotkań — używając [[Claude Code]] i Google APIs. Aplikacja działa lokalnie, przechowuje dane jako pliki markdown i uczy się jej kontekstu osobistego. Równolegle wdrożyła serię „builder days" — całodniowych hackathonów dla wszystkich zespołów, które dramatycznie zwiększyły adopcję narzędzi AI. Przypadek pokazuje, że executives muszą sami używać AI na głębokim poziomie, żeby autentycznie prowadzić organizacyjną transformację.

## Frameworki i metody

**Architektura osobistego AI chief of staff:**
1. Lokalnie uruchamiana aplikacja webowa (vibe coding, [[Claude Code]])
2. Integracja przez API tokeny: Google Calendar (tylko odczyt), Gmail (tworzenie draftów, archiwizacja, labelowanie)
3. Dane osobiste jako pliki markdown w repozytorium (bio, styl komunikacji, informacje o produktach)
4. Oddzielne terminale [[Claude Code]] dla różnych typów zapytań (kontrola kontekstu)
5. Ephemeral widgets — małe aplikacje budowane na jedno użycie i odrzucane

**Przepływ dzienny (AI chief of staff):**
1. Analiza kalendarza: co delegować, co zrobić async, co odwołać
2. „Brutal truth" — brutalna ocena jak spędzany jest czas vs. priorytety CPO
3. Przygotowanie do spotkań: executive summary, 3 wersje autoprezentacji, tematy rozmów
4. Triage emailowy: archiwizacja niepotrzebnych, drafty odpowiedzi, flagowanie pilnych
5. Prep na networking dinners: web + LinkedIn research każdego uczestnika, tematy rozmów

**Model „Builder Days" — wdrożenie AI w organizacji:**
1. Cały zespół (product, design, data science, engineering, user research) zatrzymuje normalną pracę
2. Różne tracki i zadania dla różnych funkcji
3. Dostęp do narzędzi: [[Cursor]], Figma, [[Make.com]], Webflow
4. Wsparcie techniczne on-call od inżynierów
5. Panel jurorów (CEO, CPO, cross-functional leaders), nagrody, kategorie
6. Pomiar: sentiment surveys, śledzenie adopcji narzędzi po wydarzeniu (Hex dashboardy)
7. Wynik po builder day #2: 80+ prototypów, wzrost adopcji u wcześniejszych niechętnych

## Kluczowe dane

- 80+ prototypów zbudowanych w ciągu jednego dnia (builder day #2)
- Wskaźnik adopcji narzędzi AI: dramatyczny wzrost po każdym builder day
- Filozofia: executive musi sam używać AI, żeby mieć credibility przy wdrażaniu w organizacji

## Wnioski

- Markdown jako format przechowywania danych osobistych to game-changer: zarówno [[Claude Code]] jak i web UI mogą odczytać te same pliki, bez potrzeby bazy danych
- „Builder days" działają, bo łączą mandat top-down (musisz przyjść) z autonomią bottom-up (buduj cokolwiek chcesz) — i nagrody napędują zaangażowanie
- Najważniejsza bariera adopcji AI w organizacji to brak zaufania do możliwości narzędzi — jeden dzień prototypowania może go przełamać lepiej niż miesiąc szkoleń

## Cytat

> Lider bez wiarygodności nie może autentycznie przekonać zespołu do narzędzi, których sam nie używa — „builder days" były moim sposobem na pokazanie, że buduję razem z nimi.

## Zastosowanie

Dla Piotra prowadzącego szkolenia AI dla NGO, model „builder days" to gotowy framework do przetestowania z klientami organizacyjnymi. Szczególnie wartościowe są: struktura różnych tracków dla różnych ról, mechanizm nagród i jurorów, oraz mierzenie adopcji po wydarzeniu. Architektura AI chief of staff (markdown + [[Claude Code]] + lokalne API) może inspirować przy budowaniu podobnych narzędzi dla liderów NGO szukających narzędzi do zarządzania kalendarze i komunikacją.
