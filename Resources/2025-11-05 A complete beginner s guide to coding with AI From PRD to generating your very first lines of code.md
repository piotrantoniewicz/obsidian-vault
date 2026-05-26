---
categories: Clippings
authors: ["[[Claire Vo]]"]
url: https://www.youtube.com/watch?v=k0gmTOm1eus
source: "[[Archives/2025-11-05 A complete beginner s guide to coding with AI From PRD to generating your very first lines of code|2025-11-05 A complete beginner s guide to coding with AI From PRD to generating your very first lines of code]]"
published: 2025-11-05
created: 2026-05-11
relevance: niska
tags:
  - "narzędzia-AI"
  - "vibe-coding"
  - "automatyzacja"
---

# A complete beginner s guide to coding with AI From PRD to generating your very first lines of code

[[Claire Vo]] prowadzi krok po kroku przez budowanie pierwszego projektu kodowego od zera przy użyciu AI — bez żadnej wcześniejszej wiedzy o programowaniu. Kluczowy insight: platformy vibe-coding (v0, Lovable, Bolt) mają tendencję do "scope creep" — budują zbyt wiele funkcji, których nie prosisz; lepiej iść od razu do [[Cursor]] z konkretnym, uproszczonym promptem. Folder `agents/` z plikami Markdown jako instrukcje dla agentów to przenośne rozwiązanie analogiczne do skills/commands w [[Claude Code]]. Artykuł jest skierowany do osób, które nigdy nie napisały linii kodu — product managerów, designerów, pracowników NGO.

## Frameworki i metody

- **Workflow "0 do 1" z Cursor** — dziesięcioetapowy proces dla niekoderów:
  1. Napisz PRD w ChatPRD lub innym narzędziu (lepsze wyniki na dalszych etapach)
  2. Opcjonalnie: wypróbuj v0/Lovable/Bolt — ale bądź gotowy wycofać się jeśli scope jest za duży
  3. Stwórz pusty folder na komputerze, otwórz w [[Cursor]]
  4. Wyślij do agenta Cursor: "I want a very simple Next.js app, super basic, give me all steps to set up and run"
  5. `npm run dev` → podgląd lokalny na localhost
  6. [[GitHub Desktop]] do wizualnego śledzenia zmian (zielone = dodane, czerwone = usunięte)
  7. Folder `agents/` z plikami `.md` = instrukcje dla agentów tworzących dokumenty
  8. Użyj agent-file (np. `prd.md`) do konsekwentnego generowania PRD-ów przez `@mention`
  9. Folder `prototypes/` z subdirectories = widoczne w aplikacji prototypy
  10. README update + Git commit po każdej sesji

- **Zasada prostego promptu** — "very simple, super basic, starting from scratch, give me all steps" daje lepsze wyniki niż szczegółowy spec, gdy zależy na minimalnej złożoności

## Wnioski

- Vibe-coding platformy (v0, Lovable, Bolt) są bardziej skłonne do scope creep niż Cursor z bezpośrednim prostym promptem — dla zupełnych początkujących Cursor z Composer One jest szybszy i bardziej kontrolowany
- Folder `agents/` z plikami Markdown to przenośny model definiowania workflow podobny do `skills/` i `commands/` w [[Claude Code]] — warto stosować analogiczne podejście w różnych narzędziach
- GitHub Desktop (nie CLI) to właściwa ścieżka dla niekoderów — wizualne diff, historia commitów i możliwość undone bez stresowania się terminalem

## Zastosowanie

Piotr mógłby wykorzystać ten workflow jako materiał do kursu "Fundraising z AI" lub szkoleń dla NGO — "personal project hub" w Cursor jest dobrym ćwiczeniem praktycznym pokazującym, że AI-assisted coding jest dostępny dla każdego. Model `agents/` folder = plik `.md` z instrukcjami jest bezpośrednim odpowiednikiem pluginów/skills w Claude Code i warto go pokazać uczestnikom jako "niezależne od platformy" myślenie o agentach. Sam artykuł ma niską relevancję dla zaawansowanego użytkownika, ale jako materiał referencyjny dla szkoleń może być użyteczny.
