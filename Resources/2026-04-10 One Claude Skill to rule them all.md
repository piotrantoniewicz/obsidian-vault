---
categories:
  - Emails
published: '2026-04-10'
created: '2026-04-11'
labels:
  - Ryan Carr
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - strategia-AI
---
# One Claude Skill to rule them all 👑

Ryan Carr opisuje architekturę „zagnieżdżonych umiejętności" (nested skills) w [[Claude Code|Claude Cowork]]: jeden skill-orchestrator koordynuje pracę zestawu wyspecjalizowanych sub-skills, z których każdy odpowiada za jeden etap procesu. Podejście to rozwiązuje problem monolitycznych, trudnych w utrzymaniu skryptów — każdy sub-skill jest samowystarczalny, wie co pobiera i co produkuje, dzięki czemu można go aktualizować lub pomijać bez wpływu na pozostałe. Orchestrator nie wykonuje zadań bezpośrednio, lecz śledzi postęp, zarządza zależnościami i deleguje do właściwego specjalisty. Carr podkreśla, że architektura sprawdza się wszędzie tam, gdzie proces jest wieloetapowy, a niektóre kroki mogą przebiegać równolegle lub być pomijane zależnie od kontekstu. Autor rekomenduje iteracyjne budowanie systemu — zaczynając od 3 skillów, nie od 12 — z kluczowym wymogiem jawnego definiowania ścieżek plików między komponentami.

## Frameworki i metody

- **Architektura orchestrator + sub-skills** — jeden skill-koordynator zarządza zbiorem wyspecjalizowanych sub-skills; każdy sub-skill deklaruje swoje wejście, wyjście i zależności
- **Mapa zależności (dependency map)** — orchestrator wie, które kroki wymagają wcześniejszego wykonania innych; blokuje przejście do następnego etapu, jeśli poprzedni nie jest gotowy
- **Checklist, nie sekwencja** — operator decyduje o kolejności, orchestrator pilnuje kompletności; pozwala na równoległe ścieżki i pomijanie nieistotnych kroków
- **Explicit file paths** — każdy sub-skill musi znać dokładną ścieżkę do pliku wejściowego (np. `/Resources/Brand & Voice/`), nie ogólne odwołania
- **Build 3 before 12** — buduj minimalny działający system (orchestrator + 2–3 sub-skills), skaluj iteracyjnie dodając kolejne moduły

## Wnioski

- Architektura orchestrator + sub-skills w [[Claude Code|Claude Cowork]] pozwala skalować automatyzację złożonych procesów bez utraty przejrzystości — każdy moduł jest edytowalny niezależnie, co eliminuje ryzyko psucia całego systemu przy drobnych zmianach
- Wzorzec jeden-koordynator / wielu-specjalistów jest bezpośrednio stosowalny w projektach Piotra — np. wieloetapowy onboarding klientów szkoleń AI, prowadzenie kampanii fundraisingowej lub cykl produkcji treści
- Jawne definiowanie ścieżek plików między skillami jest zasadą równie ważną w ekosystemach [[Make.com]] i [[Langflow]], gdzie niejasne odwołania do zasobów to częste źródło błędów integracyjnych

## Cytat

> Orchestrator nie pisze newslettera ani nie projektuje logo — ale zna pełen zakres pracy, śledzi postęp i deleguje każdy element do właściwego specjalisty.

## Zastosowanie

Ta architektura jest bezpośrednio przydatna przy rozwijaniu własnych pluginów dla [[Claude Code|Claude Cowork]] — Piotr może zaprojektować orchestrator skill dla procesów takich jak onboarding klienta szkoleń AI lub wieloetapowa kampania fundraisingowa, delegując każdy etap do dedykowanego sub-skilla. Podejście pozwala też na modułowe rozbudowywanie systemu Second Brain w Obsidianie: każdy typ przetwarzania (clippings, emaile, PDF-y) może być osobnym sub-skillem pod wspólnym koordynatorem. Zasada „zacznij od 3 skillów" daje konkretny, niski próg wejścia bez potrzeby projektowania całego systemu z góry.
