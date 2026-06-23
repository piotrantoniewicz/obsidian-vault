---
categories:
  - Clippings
authors: ["[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/how-i-ai-how-to-write-ai-agent-loops?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
source: "[[Archives/2026-06-22 🎙️ How I AI How to write AI agent loops in Claude Code and Codex + How Claude Mythos found a 15-year-old bug in Mozilla Firefox|2026-06-22 🎙️ How I AI How to write AI agent loops in Claude Code and Codex + How Claude Mythos found a 15-year-old bug in Mozilla Firefox]]"
published: 2026-06-22
created: 2026-06-23
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "LLM"
---

# 🎙️ How I AI: How to write AI agent loops in Claude Code and Codex + How Claude Mythos found a 15-year-old bug in Mozilla Firefox

Odcinek "How I AI" z Lenny'ego Rachitsky'ego wyjaśnia mechanikę pętli agentów AI w [[Claude Code]] i [[Codex]] (OpenAI), przekształcając je z abstrakcyjnego pojęcia w konkretne narzędzie automatyzacji. Claire pokazuje cztery typy pętli (heartbeat, cron, webhook, goal-based) i buduje realne automaty: dzienny przegląd PR i tygodniową pętlę umiejętności z subagentami. Kluczowy typ to pętla goal-based — agent działa do momentu walidacji wyniku, a nie przez określony czas, i wymaga precyzyjnych kryteriów sukcesu. Najważniejszy insight: pętla to nic innego jak prompt, który odpalany jest samoczynnie — heartbeaty, crony i webhooki istniały od dekad, nowe jest skierowanie ich na agenta AI.

## Frameworki i metody

- **Cztery typy pętli agentów AI**:
  - Heartbeat — pętla odpalana w regularnych, krótkich odstępach czasu
  - Cron — pętla według harmonogramu (np. co piątek o 10:00)
  - Webhook — pętla wyzwalana przez zdarzenie zewnętrzne
  - Goal-based — agent działa do momentu walidacji zdefiniowanego celu (najsilniejszy typ; wymaga precyzyjnych kryteriów sukcesu)
- **Model onboardingowy** — myśl o pętli jak o nowym pracowniku: zdefiniuj co sprawdza, jak często, jaki output produkuje, do kogo się zgłasza gdy coś nie gra
- **Subagent loops** — pętla może spawnować własne subpętle jako dedykowane agenty (np. tygodniowa pętla umiejętności spawns subagenty do walidacji każdej umiejętności goal-based)

## Wnioski

- Pętle goal-based są najsilniejszym typem automatyzacji, ale rozmyte kryteria sukcesu prowadzą do nieskończonej pętli palącej tokeny — precyzja opisu celu jest krytyczna
- Morning briefing w [[Claude Code]] (Cowork) to naturalny punkt startowy do budowania pętli — bez kodu, gotowy do skalowania
- Sufit automatyzacji opartej na pętlach to jakość opisu zadania, nie złożoność techniczna — "jak dobrze definiujesz pracę?"

## Zastosowanie

Piotr buduje własne narzędzia AI i pluginy [[Claude Code]] — pętle agentów mogą automatyzować przegląd emaili, aktualizacje Obsidian czy monitoring projektów NGO bez ciągłej interwencji. Goal-based loops z walidacją to architektura do rozważenia przy budowie zaawansowanych automatyzacji w [[Make.com]] lub bezpośrednio w Claude Code. Koncepcja subagent loops jest bezpośrednio zastosowalna przy projektowaniu pluginów z wieloetapowymi procesami.
