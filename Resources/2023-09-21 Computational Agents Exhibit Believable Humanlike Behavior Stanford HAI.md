---
categories: Clippings
url: https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior
source: "[[Archives/2023-09-21 Computational Agents Exhibit Believable Humanlike Behavior Stanford HAI|2023-09-21 Computational Agents Exhibit Believable Humanlike Behavior Stanford HAI]]"
published: 2023-09-21
created: 2026-03-24
relevance: średnia
tags:
  - "LLM"
  - "narzędzia-AI"
  - "trendy-AI"
---

# Computational Agents Exhibit Believable Humanlike Behavior — Stanford HAI

Badacze z [[Stanford University]] — [[Joon Sung Park]], [[Michael Bernstein]] i [[Percy Liang]] — stworzyli architekturę „generative agents": agentów opartych na [[LLM]], którzy w symulowanym środowisku (miasteczku Smallville) zachowują się w wiarygodny, ludzki sposób — planują dzień, nawiązują relacje, pamiętają zdarzenia i reagują na nie. Kluczowym osiągnięciem jest prosta, ale efektywna pętla: percepcja → strumień pamięci → refleksja → planowanie → działanie. Co istotne, agenci wykazali emergentne zachowania społeczne (przyjęcia, kampanie wyborcze), których nie zaprogramowano wprost. Artykuł pochodzi z 2023 r. i jest jednym z przełomowych papierów definiujących architekturę agentów AI.

## Frameworki i metody

- **Architektura generative agents**: percepcje agenta trafiają do strumienia pamięci (memory stream), który umożliwia retrieval (wyszukiwanie wspomnień) → refleksję (co z tego wynika) → planowanie (co zrobić) → działanie — pętla powtarza się ciągle
- **Social prototyping** — zastosowanie agentów do symulowania zachowań grup ludzi przed wdrożeniem interwencji społecznych (np. moderacja treści, kampanie informacyjne); pozwala testować scenariusze zanim dojdzie do realnych problemów

## Wnioski
- Architektura pamięć-refleksja-planowanie to fundament nowoczesnych systemów agentowych — warto znać ją przy budowaniu własnych narzędzi opartych na [[MCP]] i [[Langflow]]
- Social prototyping z agentami AI może być narzędziem dla organizacji prowadzących digital campaigning — symulacja reakcji odbiorców przed wdrożeniem kampanii
- Etyczne zagrożenia agentów (parasocjalne relacje, dezinformacja z wiarygodnego źródła) są szczególnie istotne w kontekście pracy z organizacjami społecznymi budującymi zaufanie publiczne

## Zastosowanie
Artykuł dostarcza solidnych podstaw koncepcyjnych do rozmów z klientami o tym, czym są agenty AI i jak działają — szczególnie pętla pamięci-refleksji może służyć jako intuicyjne wytłumaczenie działania narzędzi agentowych. Koncepcja social prototyping jest warta uwagi przy projektowaniu kampanii digital dla NGO — mogłaby trafić do kursu lub konsultacji jako perspektywa przyszłościowa. Kwestie etyczne (przezroczystość, logi, ryzyko zastąpienia człowieka) warto mieć pod ręką przy tworzeniu polityk AI dla organizacji.
