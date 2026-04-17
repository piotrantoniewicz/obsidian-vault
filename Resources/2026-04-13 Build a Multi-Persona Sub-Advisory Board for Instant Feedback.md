---
categories: Clippings
authors:
  - '[[ChatPRD]]'
url: >-
  https://www.chatprd.ai/how-i-ai/workflows/build-a-multi-persona-sub-advisory-board-for-instant-feedback
source: >-
  [[Archives/2026-04-13 Build a Multi-Persona Sub-Advisory Board for Instant
  Feedback|2026-04-13 Build a Multi-Persona Sub-Advisory Board for Instant
  Feedback]]
published: '2026-04-13'
created: '2026-04-13'
relevance: wysoka
tags:
  - narzędzia-AI
  - prompt-engineering
  - strategia-AI
---
# Build a Multi-Persona Sub-Advisory Board for Instant Feedback

Krótki opis workflow z [[ChatPRD]]: zamiast pytać jednego agenta AI o feedback, uruchamia się serię subagentów, z których każdy ma odrębną personę reprezentującą konkretny segment odbiorców (np. AI builders, AI executives, osoby zainteresowane AI). Każdy subagent ocenia materiał ze swojej perspektywy, dając wielowymiarową informację zwrotną w jednym kroku. To zastosowanie architektury multi-agent do symulowania rady doradczej.

## Frameworki i metody

- **Multi-persona review agent** — skill oparty na równoległych subagentach z różnymi personami; każdy subagent reprezentuje jeden segment ICP (Ideal Customer Profile) i ocenia materiał niezależnie, co eliminuje efekt jednej perspektywy
- **ICP segmentation w AI feedback loop** — dopasowanie person subagentów do profilu docelowych odbiorców treści lub produktu, np. dla newslettera: AI builders, AI executives, laicy zainteresowani AI

## Wnioski

- Architektura multi-persona to praktyczna alternatywa dla testów użytkownika — pozwala szybko zebrać feedback z różnych perspektyw bez angażowania zewnętrznych osób
- Podejście można bezpośrednio zastosować do recenzowania treści przed publikacją (posty, newslettery, oferty szkoleń), uruchamiając subagentów jako „radę" złożoną z typowych czytelników lub klientów
- Wpisuje się w szerszy trend context engineering — zamiast jednego promptu z wieloma rolami, osobne agenty z pełnym kontekstem każdej persony dają trafniejsze i mniej rozmyte odpowiedzi

## Zastosowanie

Workflow bezpośrednio przydatny do testowania materiałów szkoleniowych i ofert dobryai.pl — można skonfigurować subagentów jako: koordynator NGO bez wiedzy technicznej, fundraiser szukający narzędzi, dyrektor organizacji oceniający ROI. Dla Piotra to też inspiracja do budowania własnych skillów w Claude Cowork opartych na multi-agent feedback.
