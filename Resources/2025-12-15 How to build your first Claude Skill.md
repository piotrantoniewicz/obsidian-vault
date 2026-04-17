---
categories: Clippings
authors:
  - '[[Allie K Miller]]'
url: 'https://aiwithallie.beehiiv.com/p/how-to-build-your-first-claude-skill'
source: >-
  "[[Archives/2025-12-15 How to build your first Claude Skill|2025-12-15 How to
  build your first Claude Skill]]"
published: '2025-12-15'
created: '2026-04-06'
relevance: wysoka
tags:
  - narzędzia-AI
  - automatyzacja
  - prompt-engineering
---
# How to build your first Claude Skill

[[Allie K Miller]] wyjaśnia czym są Claude Skills — zipa z instrukcjami w pliku SKILL.md, które mówią [[Claude]] jak wykonywać powtarzalne zadania zgodnie z własnym procesem, stylem i preferencjami. Artykuł obala mit, że Skills są tylko dla programistów: plik SKILL.md to zwykły dokument w plain text, a Claude może zbudować Skill za użytkownika na podstawie istniejącego wątku rozmowy. Autorka pokazuje własny przypadek użycia — Skill "AI-First Index Assessment" (700+ linii), który skrócił jej tygodniową pracę do 3 godzin.

## Frameworki i metody

**Struktura Claude Skill:**
```
mój-skill/
├── SKILL.md          ← wymagany — instrukcje triggery i proces
├── references/       ← opcjonalne — dokumenty referencyjne
├── scripts/          ← opcjonalne — skrypty kodu
└── assets/           ← opcjonalne — szablony, obrazy
```

**SKILL.md — format:**
- Nagłówek YAML: `name` (max 64 znaki, tylko małe litery, cyfry, myślniki) + `description` (max 1024 znaki — kiedy Claude ma uruchomić Skill)
- Treść: instrukcje w markdown — co robić, jak krok po kroku, przykłady, reguły

**Najszybszy sposób tworzenia Skill:**
Wejdź w ulubiony wątek rozmowy z Claude i wklej prompt: *"Please use your skill that builds other skills and turn this entire chat thread and the main task into a Claude Skill."* → Claude buduje Skill, pakuje folder → zip → upload do Settings > Capabilities > Skills.

**Trzy kategorie instrukcji (best practice):**
- **Always do** — bez pytania
- **Ask first** — zapytaj mnie przed wykonaniem
- **Never do** — nigdy nie rób tego

**Judgment checkpoint** — po każdej kluczowej decyzji Claude raportuje: jaką decyzję podjął, dlaczego, jakie założenia przyjął, jakie alternatywy rozważał, trade-offy, otwarte pytania, poziom pewności, następne kroki dla użytkownika.

**Multi-skill stacking** — kilka Skillów w jednej rozmowie, przekazujących sobie pracę sekwencyjnie (np. brainstorm → produktyzacja → prototypowanie).

## Wnioski

- Claude Skills to najefektywniejszy sposób "enkapsulacji" własnego procesu pracy i przeniesienia go do każdej rozmowy — zamiast tłumaczyć kontekst od nowa, Skill niesie go automatycznie
- Model "jeden agent + zestaw Skillów" jest praktyczniejszy niż budowanie wielu oddzielnych agentów — Skills można stackować i wymieniać jak narzędzia w skrzynce
- Skill może zawierać własne pętle feedbacku (self-review checklist), co pozwala utrzymać jakość bez ręcznego nadzoru nad każdym krokiem

## Cytat

> Zamiast jednego "złotego wątku", każdy wątek może stać się złotym wątkiem.

## Zastosowanie

Piotr buduje własne pluginy dla Cowork — ten artykuł to bezpośrednie wsparcie techniczne i koncepcyjne: SKILL.md jest rdzeniem każdego pluginu, a wzorzec "judgment checkpoint" warto wbudować w skille wymagające oceny (np. ocena relevance notatek, analiza propozycji grantowych). Pomysł Skill "jak pisać jak ja" (z sekcjami dla różnych grup odbiorców: NGO, fundatorzy, urzędnicy) może być gotowym narzędziem ghostwritingowym dla klientów Piotra. Opis budowania Skillów bez kodowania to dobry materiał do szkoleń dla organizacji — obala mit, że automatyzacja wymaga programowania.
