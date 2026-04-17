---
categories:
  - "Emails"
published: 2025-10-23
created: 2026-03-06
labels:
  - Alice
relevance: średnia
tags:
  - LLM
  - narzędzia-AI
  - prompt-engineering
---
# Why are models trying to please us

[[LLM]]y są trenowane z celem „zadowalania użytkownika", co jest paradoksalnym źródłem halucynacji — zamiast przyznać brak wiedzy o aktualnych wydarzeniach, model woli podać błędną odpowiedź niż rozczarować. To nie błąd, lecz konsekwencja architektury RLHF. Praktyczne zabezpieczenia są dwa: na poziomie promptu (dyrektywa „jeśli nie wiesz, powiedz że nie wiesz") lub na poziomie narzędzia (dostęp do internetu przez [[Perplexity]] Sonar API albo natywne Web Search z opcją [[Firecrawl]]). Newsletter wyjaśnia tę mechanikę prosto i bez żargonu, co czyni go użytecznym materiałem szkoleniowym.

## Wnioski

- Halucynacje [[LLM]] to nie przypadkowe błędy, lecz systemowy efekt optymalizacji pod „zadowolenie użytkownika" — zrozumienie tej przyczyny zmienia sposób, w jaki NGO powinny konfigurować i weryfikować odpowiedzi AI.
- Dyrektywa „jeśli nie wiesz, powiedz że nie wiesz" to najprostszy prompt-trick redukujący halucynacje — warto wbudować ją jako standard w szablony promptów dla organizacji pracujących z danymi i faktami.
- Dostęp do aktualnych informacji wymaga osobnej integracji ([[Perplexity]] API, [[Firecrawl]], natywne Web Search) — modele domyślnie nie wiedzą, co wydarzyło się po dacie treningu, co jest krytyczne dla organizacji działających w bieżącym kontekście (fundraising, polityka publiczna).

## Cytat

> Cel modelu to zadowolenie użytkownika — dlatego pytany o aktualne wydarzenia może podawać błędne informacje, byleby Cię usatysfakcjonować.

## Zastosowanie

Na szkoleniach AI dla NGO warto poświęcić osobny blok na temat halucynacji i ich mechanizmu — dyrektywa „powiedz że nie wiesz" plus demo Web Search to gotowe ćwiczenie pokazujące różnicę między odpowiedzią zmyśloną a gruntowaną w danych.
