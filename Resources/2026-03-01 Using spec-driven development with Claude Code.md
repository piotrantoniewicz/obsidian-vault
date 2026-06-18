---
categories:
  - Clippings
authors: ["[[Heeki Park]]"]
url: "https://heeki.medium.com/using-spec-driven-development-with-claude-code-4a1ebe5d9f29"
source: "[[Archives/2026-03-01 Using spec-driven development with Claude Code|2026-03-01 Using spec-driven development with Claude Code]]"
published: 2026-03-01
created: 2026-06-17
relevance: wysoka
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "prompt-engineering"
---

# Using spec-driven development with Claude Code

Heeki Park, solutions architect, opisuje jak spec-driven development (SDD) pozwala okiełznać "vibe coding" i utrzymać jakość wytwarzanego kodu w Claude Code. SDD to podejście, w którym przed generowaniem kodu tworzy się i utrzymuje specyfikację — dokument wymagań, architektury i planu implementacji. Park wyróżnia trzy poziomy SDD: spec-first (spec jako punkt startowy), spec-anchored (spec utrzymywana po zakończeniu zadania) i spec-as-source (spec jako jedyne źródło prawdy, human nigdy nie dotyka kodu). Praktyczny wniosek: czas zainwestowany w upfront planning zwraca się wielokrotnie w jakości outputu i mniejszej liczbie przeróbek.

## Frameworki i metody

**Trzy poziomy spec-driven development (wg Birgitta Böckeler / Martin Fowler blog):**
1. **spec-first** — przemyślana spec jest pisana przed pracą z AI; używana jako kontekst w workflow
2. **spec-anchored** — spec jest utrzymywana nawet po ukończeniu zadania; ewoluuje razem z projektem; główny cel to ciągłe revisiting
3. **spec-as-source** — spec jest jedynym plikiem edytowanym przez człowieka; kod generowany jest wyłącznie przez AI na jej podstawie

**Antypattern: spec-once development** — spec powstaje na starcie projektu, ale zostaje zapomniana gdy projekt nabiera tempa. Autor przyznaje, że sam często w to wpada.

**Workflow Heeki Parka (3 fazy projektu):**
1. Due diligence — czytanie dokumentacji i źródeł; danie Claude Code tego samego kontekstu przez fetch/ingest
2. Planowanie zasobów — przemyślenie zależności, modularnego testowania, flow projektu; podział na sub-projekty i fazy
3. Iteracja na specyfikacji — wielokrotne przejrzenie przed implementacją; aktualizowanie spec przy każdej zmianie kursu

**Praktyczne tidbity Claude Code:**
- Okno kontekstu 200k tokenów (plan Pro) wystarczy dla większości prototypów; 1M dostępne tylko na Max 20x lub przez Bedrock z custom headerem
- Opus 4.6 szybko wyczerpuje limity planu (45-60 min intensywnej pracy); Sonnet 4.6 — brak limitów przy wielogodzinnym użyciu
- Warto instruować Claude Code, żeby zadawał pytania z zestawem opcji do wyboru (menu) — przyspiesza back-and-forth
- `tmux` + wiele równoległych sesji Claude Code przydatne przy agent teams

## Wnioski
- Inwestycja w spec upfront eliminuje większość "course-correcting" w trakcie projektu — follow-up interakcje stają się drobnymi poprawkami, nie przebudowami
- Spec-anchored > spec-first: ciągłe revisiting i aktualizowanie spec przy zmianach utrzymuje projekt w ryzach; autor aktywnie aktualizował `CLAUDE.md` i stworzył `SKILL.md` po projekcie
- Bezpieczeństwo (np. OAuth) warto budować od początku, nie dodawać na końcu — retrofit security w architekturach wielowarstwowych jest kosztowny

## Zastosowanie
Bezpośrednio użyteczne przy budowaniu pluginów Claude Code: spec-driven approach to dobra praktyka dla każdego projektu, gdzie Piotr generuje kod agentami. Stworzenie własnych `SKILL.md` po każdym projekcie (jak sugeruje autor) może istotnie przyspieszyć przyszłe projekty podobnego typu. Trójpoziomowy framework SDD warto przedstawić na szkoleniach dla NGO jako sposób na odpowiedzialne wdrażanie AI do pracy — antidotum na "vibe coding" w organizacjach.
