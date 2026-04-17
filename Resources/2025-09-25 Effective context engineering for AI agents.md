---
categories: Clippings
authors:
  - "[[Prithvi Rajasekaran]]"
  - "[[Ethan Dixon]]"
  - "[[Carly Ryan]]"
  - "[[Jeremy Hadfield]]"
url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
source: "[[2025-09-25 Effective context engineering for AI agents]]"
published: 2025-09-25
created: 2026-03-13
relevance: wysoka
tags:
  - strategia-AI
  - automatyzacja
  - context-engineering
---

# Effective context engineering for AI agents

Context engineering to naturalny następca prompt engineering — zamiast skupiać się wyłącznie na pisaniu instrukcji, projektujemy optymalny zestaw tokenów trafiający do okna kontekstowego modelu na każdym etapie jego działania. Artykuł [[Anthropic]] argumentuje, że LLM-y mają skończony „budżet uwagi" i cierpią na zjawisko „context rot" — im więcej tokenów w oknie, tym słabsza precyzja i zdolność do odtwarzania informacji. Kluczowa zasada: najlepszy kontekst to jak najmniejszy zestaw tokenów o wysokim sygnale, który maksymalizuje szansę na pożądany wynik. Dla zadań długohoryzontalnych autorzy opisują trzy techniki radzenia sobie z ograniczeniami okna: compaction, structured note-taking oraz sub-agent architectures — każda z innym profilem zastosowania.

## Frameworki i metody

**Anatomia dobrego kontekstu:**
- **System prompty** — działają na właściwym „altitude": nie za szczegółowe (kruche, jeśli-to-inaczej), nie za ogólne (fałszywie zakładają wspólny kontekst); optymalne to Goldilocks zone między tymi biegunami
- **Narzędzia (tools)** — powinny być minimalne, samodzielne, bezbłędne i jednoznaczne; bloated tool sets z nakładającymi się funkcjami to jeden z najczęstszych błędów; narzędzie powinno być token-efektywne i promować efektywne zachowania agenta
- **Few-shot examples** — zamiast listy edge cases: zestaw różnorodnych, kanonicznych przykładów; przykłady to „obrazki warte tysiąc słów"
- **Historia wiadomości** — traktować jako zasób wymagający aktywnej kuracji, nie pasywny log

**Trzy techniki dla zadań długohoryzontalnych:**

1. **Compaction** — gdy historia zbliża się do limitu okna, model ją podsumowuje i reinicjalizuje nowe okno ze skrótem; zachowuje decyzje architektoniczne, nierozwiązane błędy, kluczowe detale implementacji; odrzuca nadmiarowe wywołania narzędzi; rekomendacja: zacznij od maksymalizowania recall, potem iteruj w kierunku precyzji

2. **Structured note-taking (agentic memory)** — agent regularnie zapisuje notatki do pamięci zewnętrznej poza oknem kontekstowym, które są później wczytywane z powrotem; przykład: [[Claude Code]] tworzy listy zadań, niestandardowy agent utrzymuje plik NOTES.md; umożliwia śledzenie postępu przez dziesiątki wywołań narzędzi

3. **Sub-agent architectures** — zamiast jednego agenta z rosnącym kontekstem: wyspecjalizowane podagenty wykonują skupione zadania z czystymi oknami, zwracają skondensowane podsumowania (1000–2000 tokenów) do agenta koordynującego; separacja concerns — szczegółowy kontekst eksploatacji pozostaje izolowany w podagentach

**Just-in-time context:**
- Agenci utrzymują lekkie identyfikatory (ścieżki plików, zapytania, linki) i dynamicznie ładują dane w runtime za pomocą narzędzi
- Zamiast wstępnie przetwarzać wszystkie dane, agent odkrywa kontekst progresywnie — rozmiar pliku sugeruje złożoność, nazwy plików sugerują cel, timestamps to proxy dla aktualności
- [[Claude Code]] implementuje podejście hybrydowe: pliki CLAUDE.md wczytywane z góry, glob/grep do nawigacji just-in-time

## Wnioski
- Im mniejszy i bardziej sygnałowy kontekst, tym lepsze wyniki agenta — kuracja kontekstu to ważniejsza umiejętność niż pisanie długich system promptów, a traktowanie kontekstu jako zasobu skończonego powinno być wyjściowym założeniem każdego projektu automatyzacji.
- Narzędzia agentów (np. w [[Make.com]] lub [[n8n]]) wymagają tego samego rygoru co dobry kod: minimalne nakładanie się funkcji, jasna specjalizacja, efektywność tokenowa — jeśli człowiek nie potrafi jednoznacznie wskazać, które narzędzie użyć w danej sytuacji, agent też nie potrafi.
- Dla złożonych, wieloetapowych zadań compaction + structured note-taking + sub-agenci to trzy uzupełniające się mechanizmy — wybór zależy od charakteru zadania: compaction dla konwersacyjnych, note-taking dla iteracyjnych, sub-agenci dla zadań wymagających równoległej eksploracji.

## Cytat
> „Znajdź jak najmniejszy zestaw tokenów o wysokim sygnale, który maksymalizuje szansę na pożądany wynik."

## Zastosowanie
Wiedza o context engineering — szczególnie zasada Goldilocks altitude w system promptach i techniki compaction/sub-agentów — bezpośrednio przełoży się na jakość agentów budowanych w projektach automatyzacji dla NGO oraz szkoleń AIDEAS.
