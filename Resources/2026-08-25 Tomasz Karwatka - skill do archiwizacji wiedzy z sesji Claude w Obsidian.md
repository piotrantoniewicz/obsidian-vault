---
categories:
  - LinkedIn
authors: ["[[Tomasz Karwatka]]"]
published: 2026-08-25
created: 2026-08-29
relevance: wysoka
tags:
  - "context-engineering"
  - "narzędzia-AI"
  - "vibe-coding"
---

Autor opisuje, jak w jednej rozmowie z Claude zaprojektował własny skill archiwizujący wiedzę z sesji do jego vaulta Obsidian — bez napisania linijki kodu. Problem, który rozwiązuje: rozmowy z LLM generują decyzje, odrzucone alternatywy i wnioski, które giną w historii czatów zamiast się kumulować. Rozwiązanie to skill uruchamiany komendą (lub proponowany samodzielnie przez Claude po merytorycznej sesji), który zapisuje esencję sesji na jedną stronę w vaultcie. Kluczowa teza: to zmienia AI z narzędzia do rozmów w system budujący ślad procesu decyzyjnego w czasie, co po roku pozwala zestawić decyzje z osiągniętymi efektami.

## Frameworki i metody
- **Proces projektowania skilla przez rozmowę z Claude:**
  1. Użytkownik formułuje ogólną intencję ("zaprojektuj skill, który zarchiwizuje wiedzę z sesji do mojego [[Obsidian]] vault")
  2. Claude zadaje doprecyzowujące pytania: gdzie zapisywać, co zapisywać, kiedy się uruchamiać
  3. Claude pisze skill, pakuje go i testuje na samym sobie
- **Zawartość archiwizowanej notatki z sesji:**
  1. Decyzje + uzasadnienie (dlaczego akurat tak)
  2. Odrzucone alternatywy (żeby nie wracać do tego samego tematu drugi raz)
  3. Wnioski i twarde dane, które padły w rozmowie
- **Dwa tryby uruchomienia:** ręczna komenda ("/archiwizuj sesję") oraz proaktywna propozycja ze strony Claude, gdy sesja była na tyle konkretna, że warto ją zapisać

## Wnioski
- Model "agent buduje własne narzędzia dla siebie" — [[skill]] powstał w całości z rozmowy, bez ręcznego kodowania, co obniża barierę wejścia do budowania własnych narzędzi AI
- Kumulowanie decyzji + uzasadnień + odrzuconych alternatyw w czasie tworzy materiał do retrospektywnej analizy skuteczności własnych wyborów, nie tylko archiwum wiedzy
- Proaktywne proponowanie archiwizacji przez Claude (a nie tylko reagowanie na komendę) obniża ryzyko, że wartościowa sesja przepadnie, bo użytkownik zapomni ją zapisać

## Zastosowanie
Bezpośrednio zbieżne z własnym kierunkiem budowania Second Brain w strukturze EPARAX i łączenia Obsidian z Claude Cowork — wzorzec "skill archiwizujący sesję" (decyzja + uzasadnienie + odrzucone opcje) można rozważyć jako uzupełnienie istniejących pluginów `*-to-notes` o osobny mechanizm zapisu wniosków z rozmów roboczych, nie tylko przetworzonych źródeł. Format "esencja na jedną stronę" pasuje też jako wzorzec dla notatek w `Areas/` przy dokumentowaniu decyzji projektowych.
