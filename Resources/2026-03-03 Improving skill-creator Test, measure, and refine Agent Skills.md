---
categories: Clippings
authors: ["[[Anthropic]]"]
url: https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
source: "[[Archives/2026-03-03 Improving skill-creator Test, measure, and refine Agent Skills|2026-03-03 Improving skill-creator Test, measure, and refine Agent Skills]]"
published: 2026-03-03
created: 2026-05-01
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "prompt-engineering"
---

# Improving skill-creator: Test, measure, and refine Agent Skills

[[Anthropic]] rozszerza skill-creator o możliwość pisania evals, uruchamiania benchmarków i porównywania wersji skilli — bez potrzeby pisania kodu. Aktualizacja wypełnia lukę między tworzeniem skilla a pewną wiedzą, że skill działa tak jak powinien. Kluczowe rozróżnienie: skille "capability uplift" (model nie umie czegoś bez skilla) kontra "encoded preference" (sekwencja kroków specyficzna dla workflow danego zespołu) — oba wymagają testowania, ale z różnych powodów.

## Frameworki i metody

- **Dwa typy skilli w praktyce:**
  - *Capability uplift* — skill uczy modelu czegoś, czego nie umie domyślnie (np. precyzyjne tworzenie DOCX/PDF); może stać się zbędny gdy model się poprawi — evals to potwierdzą
  - *Encoded preference* — skill sekwencjonuje kroki według procesu zespołu; trwalszy, ale wymaga weryfikacji czy faktycznie odwzorowuje prawdziwy workflow

- **Evals (testy skilli):**
  - Definiujesz prompty testowe (+ pliki jeśli potrzeba) i opisujesz co jest "dobrym" wynikiem
  - Skill-creator sprawdza czy skill spełnia oczekiwania
  - Dwa główne zastosowania: wykrywanie regresji po aktualizacji modelu + sprawdzenie czy skill jest jeszcze potrzebny

- **Benchmark mode:**
  - Standaryzowane uruchomienie evals po aktualizacjach modelu lub po edycji skilla
  - Śledzi: pass rate evals, czas wykonania, zużycie tokenów

- **Multi-agent evals:**
  - Evals uruchamiane równolegle przez niezależne agenty (czysty kontekst, brak cross-contamination między testami)
  - Comparator agents do A/B: dwie wersje skilla oceniane ślepo (bez wiedzy który jest który)

- **Optymalizacja opisu skilla:**
  - Skill-creator analizuje opis skilla względem przykładowych promptów
  - Sugeruje edycje redukujące fałszywe wyzwalania i pominięcia
  - Test na 6 publicznych skillach: 5 z 6 poprawiło triggerowanie

## Wnioski
- Distinction między "capability uplift" a "encoded preference" jest kluczowa przy decyzji o budowie skilla — dla NGO większość skilli to encoded preferences (sekwencje procesów organizacji), które są trwalsze i nie przestarzeją się z rozwojem modeli.
- Evals to most między budowaniem a wdrażaniem skilli — bez nich skill "działa" tylko w sensie subiektywnym; to ważna luka w obecnym workflow tworzenia pluginów.
- Kierunek rozwoju: SKILL.md jako specyfikacja "co" zamiast instrukcja "jak" — model sam wywnioskuje implementację; warto pisać skille pod ten paradigmat już teraz.

## Cytat
> Evals już opisują "co". Z czasem ten opis może stać się samym skillem.

## Zastosowanie
Bezpośrednio użyteczne przy budowie własnych pluginów Claude Code — warto wdrożyć evals dla istniejących skilli (clippings-to-notes, emails-to-notes, outreach) żeby sprawdzić jakość i stabilność po aktualizacjach modeli. Distinkcja capability uplift vs encoded preference pomaga decydować kiedy warto inwestować w skill a kiedy wystarczy dobry prompt. Benchmark mode szczególnie przydatny przed wdrożeniem nowej wersji skilla klientom NGO.
