---
categories:
  - Clippings
authors: ["[[antirez]]"]
url: "https://antirez.com/news/169"
source: "[[Archives/2026-07-13 Control the ideas, not the code|2026-07-13 Control the ideas, not the code]]"
published: 2026-07-13
created: 2026-07-15
relevance: średnia
tags:
  - "vibe-coding"
  - "LLM"
  - "trendy-AI"
---

# Control the ideas, not the code

Antirez (twórca Redis) twierdzi, że w erze generatywnego AI czytanie i recenzowanie kodu linia po linii jest coraz częściej bezcelowe — programiści powinni skupić się na kontrolowaniu idei i architektury, a nie na samym kodzie. Argumentuje, że LLM-y są bardzo dobre w pisaniu lokalnie optymalnego kodu, a coraz lepsze w dużych koncepcjach, więc czas lepiej spędzić na projektowaniu, QA i myśleniu o kierunku produktu niż na przeglądaniu tysięcy linii kodu dziennie. Jego rekomendacja dla doświadczonych programistów: zamiast recenzji kodu, pisać dokumentację projektową (np. DESIGN.md) opisującą idee i mechanizmy w języku naturalnym — to bardziej użyteczne niż sam kod. Zastrzega jednak, że młodzi, niedoświadczeni programiści wciąż powinni uczyć się pisać kod od podstaw, żeby zbudować model mentalny działania systemów.

## Wnioski

- Wartość pracy programisty przesuwa się z "pisania i czytania kodu" na "kontrolowanie idei i architektury" — kod staje się szczegółem implementacyjnym generowanym przez [[LLM]].
- Dokumentacja projektowa (design docs) opisująca idee i decyzje architektoniczne w języku naturalnym zyskuje na znaczeniu bardziej niż sam kod — to ona pozwala kolejnym osobom (lub agentom AI) zrozumieć system.
- Dla mniej doświadczonych osób budowanie fundamentalnego zrozumienia (pisanie prostych struktur danych, interpreterów) wciąż ma wartość — automatyczne akceptowanie output'u LLM bez zrozumienia nie buduje kompetencji.

## Zastosowanie
Przydatne w kontekście własnych projektów automatyzacji i pluginów Claude Code — sugeruje warto dokumentować idee i architekturę rozwiązań (np. w plikach DESIGN.md) zamiast polegać wyłącznie na przeglądzie wygenerowanego kodu, co przyspiesza iterację przy budowie narzędzi AI.
