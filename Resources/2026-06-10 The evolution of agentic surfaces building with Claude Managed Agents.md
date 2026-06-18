---
categories:
  - Clippings
authors: ["[[Anthropic]]"]
url: "https://claude.com/blog/building-with-claude-managed-agents"
source: "[[Archives/2026-06-10 The evolution of agentic surfaces building with Claude Managed Agents|2026-06-10 The evolution of agentic surfaces building with Claude Managed Agents]]"
published: 2026-06-10
created: 2026-06-17
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "strategia-AI"
---

# The evolution of agentic surfaces building with Claude Managed Agents

[[Anthropic]] opisuje ewolucję infrastruktury do budowania agentów AI — od prostego API (tokeny in/out) przez [[Claude Agent SDK]] do Claude Managed Agents: zarządzanej platformy produkcyjnej. Kluczowy problem, który rozwiązuje: większość zespołów spala czas na infrastrukturę (hosting, sesje, bezpieczeństwo, skalowalność), zamiast na to, co wyróżnia ich agenta — zarządzanie kontekstem i domenową wiedzę. Managed Agents rozdziela "mózg" (harness wywołujący model) od "rąk" (sandbox do wykonywania kodu), co eliminuje największe wąskie gardła produkcyjne. Artykuł zawiera konkretne dane o wydajności i przykłady wdrożeń u klientów (Notion, Rakuten, Sentry, Asana, Atlassian).

## Frameworki i metody

**Ewolucja architektury Anthropic (3 poziomy):**
1. **Messages API** — jedno żądanie, jedna odpowiedź modelu; deweloper buduje własną pętlę i infrastrukturę
2. **Claude Agent SDK** — harness z [[Claude Code]] udostępniony deweloperom; pętla, narzędzia, subagenci, zarządzanie kontekstem już wbudowane
3. **Claude Managed Agents** — pełna infrastruktura produkcyjna zarządzana przez Anthropic: hosting, skalowanie, sesje, sandbox, bezpieczeństwo credentials, obserwowalność

**Trzy główne zasoby w Managed Agents:**
- *Agent* — konfiguracja: model, prompt, narzędzia, guardrails
- *Environment* — kontekst wykonawczy: sandbox, reguły sieci, preinstalowane pakiety
- *Session* — para agent+environment z izolowanym sandboxem; persystuje pełną historię eventów

## Kluczowe dane
- Czas do pierwszego tokenu: skrócony o ~60% (mediana) i >90% (p95) vs architektura bez Managed Agents
- Rakuten: wdrożył agentów specjalistycznych w każdym dziale w ~tydzień na dział
- Notion: prototyp skrócił 12h pracy do 20 minut
- Sentry: agent debugujący napisany przez jednego inżyniera w tygodniach (nie miesiącach)

## Wnioski
- Kluczową barierą produkcyjną dla agentów nie są możliwości modelu, ale infrastruktura: hosting, credentials, sesje, observability — Managed Agents eliminuje te problemy "out of the box"
- Rozdzielenie harnessu od sandboxu (brain vs. hands) rozwiązuje jednocześnie problemy bezpieczeństwa (credentials poza sandbox) i latencji (model zaczyna myśleć przed startem kontenera)
- Harness musi ewoluować razem z modelem — "context anxiety" w [[Claude Sonnet 4.5]] wymagała innych poprawek niż Claude Opus 4.5; Managed Agents zdejmuje ten ciężar z deweloperów

## Zastosowanie
Bezpośrednio użyteczne przy rozbudowie własnych pluginów Claude Code — Managed Agents to kolejny krok po Agent SDK dla agentów wymagających produkcyjnej infrastruktury. Przy projektach dla klientów NGO: jeśli Piotr będzie budował bardziej złożone automatyzacje (wieloagentowe, długotrwałe), Managed Agents eliminuje konieczność samodzielnego budowania hostingu i zarządzania sesjami. Warto śledzić jako kierunek, w którym zmierza platforma [[Anthropic]].
