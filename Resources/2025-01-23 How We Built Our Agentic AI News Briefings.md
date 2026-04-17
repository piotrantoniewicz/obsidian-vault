---
categories: Clippings
authors:
  - '[[Allie K Miller]]'
url: 'https://www.youtube.com/watch?v=QS6mrTHgEuU'
source: >-
  [[Archives/2025-01-23 How We Built Our Agentic AI News Briefings|2025-01-23
  How We Built Our Agentic AI News Briefings]]
published: '2025-01-23'
created: '2026-03-25'
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - prompt-engineering
---
# How We Built Our Agentic AI News Briefings

[[Allie K Miller]] prezentuje szczegółową architekturę zautomatyzowanego systemu codziennych briefingów z AI, zbudowanego w [[GumLoop]] przy użyciu [[Claude]] 3.5 Sonnet i [[Gemini]] 1.5 Pro. System pobiera artykuły przez RSS, filtruje je słowami kluczowymi, skrobie i czyści HTML, podsumowuje i ocenia każdy artykuł, deduplikuje i rankinuje, a następnie generuje gotowy post z komentarzem w stylu autorki — cały workflow kosztuje poniżej 1 dolara dziennie i zajmuje 10 minut. Kluczowa lekcja: budowanie systemów agentowych wymaga myślenia o mikroserwisach, ludzkim przeglądzie i testowaniu wielu modeli — start simple, iterate fast.

## Frameworki i metody

- **Architektura agentic news briefing**: RSS feeds → filtr słów kluczowych → scraper → HTML cleaner → summarizer (Claude) → evaluator (Claude) → deduplication → ranking → storage ([[Supabase]]) → post formatter → human review → publish.
- **Battle Royale prompting**: przy każdym kroku model generuje 3 wersje (tytuły, podsumowania, oceny) i uzasadnia każdą — zamiast dawać jedną odpowiedź, model „pokazuje pracę". Technika zwiększa jakość outputu bez dodatkowych narzędzi.
- **Weighted evaluation scoring**: artykuły oceniane wg kryteriów z wagami (np. industry significance 40%, business impact 45%, technical innovation 15%) — wagi dobierane iteracyjnie przez testy.
- **Microservice workflow architecture**: każdy etap pipeline'u to oddzielna, wielokrotnego użytku jednostka (np. „summarize and evaluate group") — możliwość kompozycji i deployowania w innych automatyzacjach.
- **Human-in-the-loop review**: recenzja ludzka nie dotyczy gramatyki, lecz błędów strukturalnych: duplikaty, wcześniej opublikowane story, dezinformacja.
- **Prostszy wariant — [[ChatGPT]] Tasks**: dla osób bez zasobów technicznych — jednozdaniowy prompt + harmonogram + powiadomienia mobilne. Brak bazy danych i extensibility, ale szybkie wdrożenie.

## Kluczowe dane

- Koszt całego workflow: poniżej 1 dolara dziennie (przykład: 89 centów).
- Czas działania: ~10 minut od uruchomienia do gotowego draftu.
- Pipeline ocenia i przechowuje wszystkie artykuły, ale do posta trafia top 5.

## Wnioski

- Architektura mikroserwisów w automatyzacjach (modułowe bloki zamiast monolitu) znacznie ułatwia iterację i wielokrotne użycie komponentów — to bezpośrednio przenoszalne do budowania własnych pipeline'ów w [[Make.com]] czy [[Langflow]].
- Technika Battle Royale (generuj 3 wersje, uzasadnij każdą) to praktyczna technika [[prompt-engineering]], którą można stosować w dowolnym workflow wymagającym jakościowego outputu tekstowego.
- Budowanie bazy danych z ocenianymi artykułami (nawet tymi nieużytymi) otwiera nowe use cases: raporty tematyczne, porównania, wyszukiwanie semantyczne — warto projektować systemy z myślą o przyszłych zastosowaniach.

## Zastosowanie

Architektura opisana w filmie jest bezpośrednio adaptowalna do budowania systemu monitorowania mediów dla NGO lub klientów dobryai.pl — codzienne briefingi o fundraisingu, digital campaigningu lub AI w sektorze pozarządowym. Technika weighted evaluation scoring może być użyta do oceny jakości treści w automatyzacjach tworzonych dla organizacji (np. filtrowanie ważnych wiadomości od sponsorów lub darczyńców). Prostszy wariant z [[ChatGPT]] Tasks to gotowe demo do pokazania podczas szkoleń z AI dla organizacji, które chcą zacząć od małych kroków.
