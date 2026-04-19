---
categories: Clippings
authors: ["[[Addy Osmani]]"]
url: https://addyosmani.com/blog/claude-code-agent-teams/
source: "[[Archives/2026-02-05 Claude Code Swarms|2026-02-05 Claude Code Swarms]]"
published: 2026-02-05
created: 2026-04-19
relevance: średnia
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "strategia-AI"
---

# Claude Code Swarms

[[Claude Code]] wprowadził „agent teams" (swarms) — architekturę, w której jeden agent-lider deleguje zadania do wielu równoległych agentów-współpracowników, każdy z własnym kontekstem i specjalizacją. [[Addy Osmani]] wyjaśnia, dlaczego to fundamentalna zmiana: pojedynczy agent degraduje przy rozbudowanym kontekście, natomiast wąsko sprofilowane agenty działają lepiej, bo mają czysty kontekst i nie „rozpraszają się". Kluczowa zasada: im precyzyjniejsza specyfikacja zadania, tym lepszy wynik — swarms zamieniają inżynierię w sztukę dekomponowania problemów.

## Frameworki i metody

- **Architektura agent teams** — team lead spawns niezależnych agentów-teammates, każdy z własnym oknem kontekstu; współdzielona lista zadań z dependency tracking; skrzynka odbiorcza do komunikacji między agentami (nie tylko do lidera)
- **Kiedy używać swarms vs subagents** — subagenty: szybkie, skoncentrowane zadania gdzie liczy się tylko wynik; agent teams: złożona praca wymagająca dyskusji, wzajemnej weryfikacji, koordynacji; swarms kosztują więcej tokenów
- **Plan approval** — ryzykowne zadania wymagają zatwierdzenia planu przez lidera przed implementacją; teammate działa w trybie read-only do momentu zatwierdzenia
- **Delegate mode** — lider ograniczony wyłącznie do koordynacji (Shift+Tab), nie dotyka kodu; zapobiega rozpraszaniu lidera na implementację zamiast delegowania
- **File ownership** — każdy teammate odpowiada za różne pliki; zapobiega konfliktom przy jednoczesnej edycji
- **Compound Engineering Plugin** — workflow: 80% planowania i review, 20% wykonania; specjalizowane agenty do code review (security, performance, architecture), dokumentowanie learnings dla przyszłych agentów

## Kluczowe dane

- LLM działa gorzej w miarę rozrastania się kontekstu — to podstawowe uzasadnienie dla multi-agent architecture
- 5–6 zadań na agenta to optymalny zakres — wystarczające dla produktywności, możliwe do reassignment

## Wnioski

- Zasada czystego kontekstu jest transferowalna: każde zadanie AI działa lepiej, gdy ma wąski, precyzyjny zakres — dotyczy to promptów, slash commands i wszystkich prac agentowych
- Umiejętności dobrego managera (task sizing, clear ownership, precise briefs) to jednocześnie umiejętności efektywnego orkiestrowania agentów AI
- Swarms są potężne, ale aktywność agentów nie jest równoznaczna z wartością — należy pozwolić problemowi wybrać narzędzie, nie odwrotnie

## Zastosowanie

Architektura agent teams jest przydatna przy budowaniu bardziej złożonych narzędzi automatyzacji — np. system, w którym jeden agent researchuje, drugi pisze, trzeci weryfikuje. Zasada 80/20 (planowanie/wykonanie) z Compound Engineering Plugin warta wdrożenia przy tworzeniu własnych pluginów. Dla szkoleń z AI dla NGO: swarms to dobry przykład ilustrujący, jak myśleć o delegowaniu zadań do AI systemów.
