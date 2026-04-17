---
categories:
  - Emails
published: '2026-04-07'
created: '2026-04-11'
labels:
  - Marek Staniszewski
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - strategia-AI
---
# Heuristica Newsletter | Budowanie własnego agenta czy gotowy workflow?

Newsletter Marka Staniszewskiego z Heuristica przedstawia framework decyzyjny pomagający wybrać między budowaniem własnego agenta AI a zastosowaniem gotowego workflow do automatyzacji. Kluczowe zmienne to przewidywalność ścieżki zadania oraz tolerancja wariancji na błędy. Autor proponuje macierz 2×2 z czterema archetypami systemów: pełny agent, workflow z LLM, hybryda i klasyczny workflow. W praktyce wiele projektów AI „wykłada się" nie przez zły model, lecz przez błędne zdefiniowanie typu zadania. Przewagę buduje architektura wokół modelu, nie sam model.

## Frameworki i metody

- **Macierz decyzyjna agent vs. workflow** — dwie osie: przewidywalność ścieżki (niska/wysoka) i tolerancja wariancji błędów (wysoka/niska), tworząca 4 archetypy:
  - Niska przewidywalność + wysoka tolerancja → **Pełny agent** — research, otwarte zadania, eksploracja, web search, synteza (np. analiza komunikacji 5 konkurentów)
  - Wysoka przewidywalność + wysoka tolerancja → **Workflow + LLM** — klasyfikacja, generacja treści, transformacja (np. opisy 500 produktów e-commerce)
  - Niska przewidywalność + niska tolerancja → **Hybryda** — agent-router + dedykowane workflow; compliance, finanse, moderacja komentarzy w social mediach
  - Wysoka przewidywalność + niska tolerancja → **Klasyczny workflow** — raportowanie KPI, znane źródła, znany format (np. cotygodniowy raport [[Meta Ads]] i [[LinkedIn]])
- **6 pytań diagnostycznych przed wyborem architektury** — lista pytań do zadania przed podjęciem decyzji:
  1. Czy z góry wiemy, jakie kroki trzeba wykonać — czy zawsze są to te same kroki?
  2. Ile jest realnych wariantów ścieżki? (2–5 → może wystarczy workflow; 6+ → agent w grze)
  3. Jaki jest koszt błędu pojedynczego uruchomienia?
  4. Jak często zmieniają się reguły biznesowe?
  5. Kto to rozwiązanie będzie utrzymywał i uaktualniał za pół roku?
  6. Czy zadanie wymaga „rozumowania", czy transformacji danych?

## Wnioski

- Wybór między agentem a workflow to nie wybór technologii, lecz profilu ryzyka i skalowalności — zanim zbudujesz agenta w [[n8n]], zdiagnozuj, czy zadanie to eksploracja (agent) czy transformacja (workflow).
- Gotowe workflow w [[Make.com]] lub [[n8n]] wygrywają przy zadaniach z wysoką przewidywalnością i niską tolerancją błędów (np. raporty KPI) — tu kreatywność modelu jest zagrożeniem, nie zaletą.
- Hybrydowa architektura (agent-router + dedykowane workflow) sprawdza się wszędzie tam, gdzie ścieżka jest nieprzewidywalna, ale koszt złej reakcji jest wysoki — np. moderacja komentarzy, obsługa skarg, reagowanie kryzysowe.

## Cytat

> W systemach AI przewagę buduje nie to, jak zaawansowany jest model, ale to, na ile dobrze zaprojektowana jest wokół niego architektura.

## Zastosowanie

Framework bezpośrednio wspiera Piotra przy konsultacjach wdrożeń AI w NGO — macierz decyzyjna pomaga klientom zrozumieć, kiedy nie warto budować agenta i wystarczy prosty workflow w [[Make.com]]. Sześć pytań diagnostycznych to gotowe narzędzie do audytu projektów automatyzacji u klientów i może stać się ćwiczeniem na warsztatach „Fundraising z AI". Rozróżnienie eksploracja/transformacja upraszcza rozmowy strategiczne z organizacjami, które często błędnie zakładają, że każde zadanie wymaga agenta.
