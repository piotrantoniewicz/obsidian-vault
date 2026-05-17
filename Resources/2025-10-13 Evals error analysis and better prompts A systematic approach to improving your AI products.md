---
categories: Clippings
authors: ["[[Hamel Husain]]"]
url: https://www.youtube.com/watch?v=PgzOBNse2EA
source: "[[Archives/2025-10-13 Evals error analysis and better prompts A systematic approach to improving your AI products|2025-10-13 Evals error analysis and better prompts A systematic approach to improving your AI products]]"
published: 2025-10-13
created: 2026-05-11
relevance: średnia
tags:
  - "prompt-engineering"
  - "LLM"
  - "strategia-AI"
---

# Evals, error analysis, and better prompts. A systematic approach to improving your AI products.

[[Hamel Husain]] prezentuje systemowe podejście do poprawy jakości produktów AI, oparte na analizie danych — nie intuicji. Centralną tezą jest to, że „vibe checking" (sprawdzanie przez wrażenie) jest niewystarczający do skalowania produktu AI: zamiast tego potrzebna jest analiza prawdziwych konwersacji użytkowników, kategoryzacja błędów i iteracyjne poprawianie promptów oraz ewaluatorów. Framework jest prosty, dostępny dla PM-ów bez zaplecza technicznego i przynosi mierzalne rezultaty w ciągu kilku godzin pracy.

## Frameworki i metody

- **Error analysis** — analiza ~100 losowych śladów (traces) z systemu produkcyjnego: pisanie krótkich notatek o tym, co poszło nie tak (open coding), a następnie kategoryzowanie błędów i zliczanie ich częstości; punkt wyjścia do priorytetyzacji napraw
- **Traces i obserwowalność** — logowanie pełnych sekwencji interakcji AI (wejście → wywołania narzędzi → odpowiedź) w narzędziach jak [[Braintrust]] lub Phoenix; kluczowe do zrozumienia, co naprawdę dzieje się w systemie
- **LLM-as-a-Judge** — automatyczny ewaluator oparty na modelu językowym; skuteczny tylko gdy: (1) daje binarne wyniki (dobry/zły), nie skalę; (2) jest skalibrowany ręcznie przed wdrożeniem; (3) jest napisany pod konkretny problem, nie ogólny
- **Custom annotation tool** — prosta aplikacja do szybkiego przeglądania i etykietowania śladów, dostosowana do specyfiki produktu; minimalizuje tarcie i przyspiesza analizę

## Wnioski

- Najcenniejszą czynnością przed pisaniem ewaluatorów jest ręczne przejrzenie ~100 konwersacji — daje grounding w rzeczywistości użytkownika, niemożliwy do zastąpienia syntetycznymi danymi
- Binarne oceny (pass/fail) są wielokrotnie bardziej użyteczne niż arbitralne skale (np. „helpfulness: 4.2/10") — dają jasne kryteria i można je walidować z ręcznym etykietowaniem
- Analiza błędów to fundament, od którego należy zacząć — dopiero po niej wiadomo, jakie ewaluatory warto pisać i dlaczego

## Cytat

> Najważniejszą rzeczą jest patrzenie na dane. To był najważniejszy element jeszcze przed erą AI — i teraz jest tak samo. Potrzebujesz tylko nieco innego podejścia.

## Zastosowanie

Przy budowaniu narzędzi AI dla NGO (chatboty, automatyzacja odpowiedzi, klasyfikatory treści) podejście error analysis pozwoli szybko zidentyfikować najczęstsze awarie bez kosztownej infrastruktury ewaluacyjnej. Framework jest na tyle prosty, że można go wdrożyć samodzielnie, bez data scientista — wystarczy kilka godzin pracy i spreadsheet.
