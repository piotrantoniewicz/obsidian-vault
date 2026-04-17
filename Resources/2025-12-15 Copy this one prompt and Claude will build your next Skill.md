---
categories:
  - Emails
published: 2025-12-15
created: 2026-03-06
labels:
  - AI with ALLIE
relevance: niska
tags:
  - automatyzacja
  - narzędzia-AI
  - prompt-engineering
---
# Copy this one prompt and Claude will build your next Skill

[[Claude Skills]] to foldery z plikiem SKILL.md zawierającym instrukcje — raz stworzone, dostępne w każdej rozmowie bez konieczności pisania kodu. Autorka zbudowała skill "AI-First Index Assessment" (700+ linii), który skrócił jej tygodniową pracę do 3 godzin. Skill można wygenerować automatycznie z istniejącego wątku rozmowy jednym promptem, a następnie zainstalować przez Settings > Capabilities > Skills. W przyszłości skills będą się "stackować" — wiele skills wywoływanych sekwencyjnie w ramach jednej agentic workflow.

## Wnioski
- Skill budowany z istniejącego wątku to najszybsza droga do automatyzacji — wystarczy skopiować jeden prompt: *"Please use your skill that builds other skills and turn this entire chat thread into a Claude Skill"* — idealne dla konsultanta, który wielokrotnie wykonuje podobne analizy dla różnych NGO.
- Trójpodział instrukcji w SKILL.md (*always do / ask first / never do*) to wzorzec rodem z [[prompt-engineering]], który zwiększa niezawodność i kontrolę — warto stosować przy tworzeniu skillów do fundraisingu lub oceny strategii dla [[organizacje-społeczne]].
- "Multi-skill stacking" (brainstorm → produktyzacja → prototypowanie) to kierunek rozwoju agentów [[Claude]] — organizacje NGO mogą budować pipeline'y: zbieranie danych → analiza → raport, całkowicie bez kodu.

## Cytat
> "Instead of building 100 different agents, you leverage one agent with access to a set of skills and tools."

## Zastosowanie
Warto stworzyć własny skill do cyklicznych analiz (np. oceny gotowości NGO na AI lub audyt fundraisingowy) — raz zbudowany skill skróci każde kolejne zlecenie z tygodnia do kilku godzin.
