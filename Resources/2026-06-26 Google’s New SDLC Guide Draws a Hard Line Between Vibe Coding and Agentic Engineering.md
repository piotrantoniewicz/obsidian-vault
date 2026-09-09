---
categories:
  - Clippings
authors: ["[[Mehmet Özel]]"]
url: "https://medium.com/data-science-collective/googles-new-sdlc-guide-draws-a-hard-line-between-vibe-coding-and-agentic-engineering-29ee5514c48c"
source: "[[Archives/2026-06-26 Google’s New SDLC Guide Draws a Hard Line Between Vibe Coding and Agentic Engineering|2026-06-26 Google’s New SDLC Guide Draws a Hard Line Between Vibe Coding and Agentic Engineering]]"
published: 2026-06-26
created: 2026-09-09
relevance: wysoka
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "strategia-AI"
---

# Google’s New SDLC Guide Draws a Hard Line Between Vibe Coding and Agentic Engineering

Punktem wyjścia jest termin „vibe coding" ukuty przez Andreja Karpathy'ego w lutym 2025 roku — programowanie polegające na promptowaniu, akceptowaniu wyniku i uruchamianiu kodu bez weryfikacji. Szesnaście miesięcy później Google opublikował 50-stronicowy whitepaper „The New SDLC With Vibe Coding" (współautorzy: Addy Osmani, Shubham Saboo, Sokratis Kartakis), który stawia twardą tezę: vibe coding sprawdza się w prototypach, ale w systemach produkcyjnych po cichu generuje dług, którego zespoły nie dostrzegają, bo szkody kumulują się powoli. Artykuł zapowiada rozbicie argumentacji whitepaperu i wytyczenie granicy między chaotycznym vibe codingiem a ustrukturyzowanym, weryfikowalnym „agentic engineering" — granicą tą jest weryfikacja.

## Wnioski
- Vibe coding i agentic engineering to dwa różne tryby pracy z AI w programowaniu — różnicę wyznacza obecność (lub brak) systematycznej weryfikacji wyniku, nie samo użycie AI.
- Google formalnie uznaje problem: dotychczasowy cykl życia oprogramowania (SDLC) wymaga przedefiniowania w erze narzędzi typu [[Claude Code]] i podobnych asystentów agentowych.
- Ryzyko vibe codingu w produkcji jest odroczone w czasie — brak natychmiastowej awarii usypia czujność zespołów, co czyni je bardziej niebezpiecznym niż widoczne od razu błędy.

## Cytat
> W pełni poddaj się flow, obejmij eksponenty i zapomnij, że kod w ogóle istnieje.

## Zastosowanie
Przydatne jako punkt odniesienia przy rozwijaniu własnych pluginów Claude Code — pomaga świadomie oddzielić szybkie prototypowanie „na flow" od fragmentów wymagających strukturalnej weryfikacji przed wdrożeniem. Może też posłużyć jako argument w rozmowach z klientami organizacji społecznych o tym, dlaczego wdrożenia AI wymagają procesu, a nie tylko promptowania.
