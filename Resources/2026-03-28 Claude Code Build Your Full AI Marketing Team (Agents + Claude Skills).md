---
categories: Clippings
authors: ["[[Grace Leung]]"]
url: https://www.youtube.com/watch?v=yLXLHnD4fco
source: "[[Archives/2026-03-28 Claude Code Build Your Full AI Marketing Team (Agents + Claude Skills)|2026-03-28 Claude Code Build Your Full AI Marketing Team (Agents + Claude Skills)]]"
published: 2026-03-28
created: 2026-05-08
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "content-marketing"
---

# Claude Code Build Your Full AI Marketing Team (Agents + Claude Skills)

[[Grace Leung]] pokazuje krok po kroku, jak zbudować pełny AI marketing team w [[Claude Code]]: 5 agentów (data analyst, content creator, market researcher, creative designer, campaign strategist) i 12 skills, wszystko zarządzane przez plik CLAUDE.md i zintegrowane z [[Notion]] jako tablicą zadań. Kluczowy wniosek: skills to "podręcznik" współdzielony przez agentów — gdy zadanie jest proste i wykonawcze, wystarczy skill; gdy wymaga syntezy i złożonego myślenia, potrzebny jest dedykowany agent. System można obsługiwać z telefonu przez remote control.

## Frameworki i metody

**4 kroki budowania AI marketing team w Claude Code:**
1. Zmapuj funkcje marketingowe — jakie zadania faktycznie wykonujesz co tydzień
2. Zamień każde powtarzalne zadanie w skill (jeden workflow = jeden skill)
3. Zgrupuj podobne skills w nienachodząco się agenty z dedykowaną rolą
4. Połącz agenty i skills w zespół przez CLAUDE.md — dodaj reguły routingu (kiedy agent, kiedy sam skill)

**Metody budowania skills:**
- *Reference-based method*: dajesz Claude przykłady/szablony "jak wygląda dobre" → Claude uczy się wzorców (np. branded deck skill)
- *MCP integration*: skill łączy się z zewnętrznym narzędziem przez `.mcp.json` (np. Nano Banana dla generowania obrazów)

**Integracja z [[Notion]]:**
- Kanban board jako kolejka zadań dla AI agentów
- Claude skanuje pending tasks i przypisuje agenty według priorytetu
- Po wykonaniu aktualizuje status na "Complete" i zapisuje ścieżki outputów

## Wnioski
- [[Claude Code]] agents + skills to praktyczna architektura do budowania własnych narzędzi AI bez głębokiej wiedzy programistycznej
- CLAUDE.md to centralny punkt konfiguracji całego projektu — routing agentów musi być tam explicite opisany, żeby system był przewidywalny
- Remote control przez telefon = Claude Code jako "24/7 teammate" — agenci wykonują zadania asynchronicznie podczas twojej nieobecności przy biurku

## Zastosowanie
Architektura 5 agentów + 12 skills z tego wideo jest bezpośrednim wzorcem do budowania własnego AI marketing team dla dobryai.pl. Workflow [[Notion]] → [[Claude Code]] → outputs można zaadaptować do obsługi zleceń klientów NGO — tablica zadań w Notion jako interfejs dla organizacji, agenci jako egzekutorzy. Framework 4 kroków (map → skills → agents → CLAUDE.md) to gotowy warsztat do pokazania na szkoleniach.
