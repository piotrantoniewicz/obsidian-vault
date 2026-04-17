---
categories: Clippings
authors: ["[[Anthropic]]"]
url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
source: "[[Archives/2025-09-29 Effective context engineering for AI agents|2025-09-29 Effective context engineering for AI agents]]"
published: 2025-09-29
created: 2026-04-17
relevance: wysoka
tags:
  - "context-engineering"
  - "prompt-engineering"
  - "LLM"
---

# Effective Context Engineering for AI Agents

[[Anthropic]] definiuje context engineering jako naturalną ewolucję prompt engineeringu — zamiast koncentrować się wyłącznie na treści promptów, skupia się na optymalnym doborze wszystkich tokenów trafiających do modelu w danym momencie. Kluczowy insight: [[LLM|modele językowe]] mają ograniczony "budżet uwagi" i wraz ze wzrostem długości kontekstu ich zdolność do precyzyjnego wyszukiwania informacji maleje — zjawisko zwane context rot. Artykuł, napisany przez praktyków budujących [[Claude Code]], opisuje konkretne techniki zarządzania kontekstem w agentach długoterminowych: kompakcję, strukturalne notatki i architektury wieloagentowe. Przewodnia zasada: znajdź najmniejszy możliwy zestaw tokenów o wysokim sygnale, który maksymalizuje prawdopodobieństwo pożądanego zachowania.

## Frameworki i metody

**Context engineering vs. prompt engineering**
- Prompt engineering skupia się na pisaniu instrukcji; context engineering zarządza całym stanem tokenów (system prompts, tools, [[MCP]], message history, dane zewnętrzne)
- Context engineering jest iteracyjny — faza kuracji następuje przy każdym wywołaniu modelu, nie tylko raz

**Anatomia efektywnego kontekstu**
- System prompts w "goldilocks zone" — nie za szczegółowe (fragile, brittle), nie za ogólne (brak konkretnych sygnałów); optymalne: wystarczająco konkretne, by kierować zachowaniem, wystarczająco elastyczne, by model mógł działać samodzielnie
- Tools: minimal viable set, brak nakładania się funkcjonalności, opisy jednoznaczne i token-efficient
- Przykłady kanoniczne zamiast listy edge case'ów — "pictures worth a thousand words"

**Techniki dla long-horizon tasks**
1. **Compaction** — podsumowanie kontekstu bliskiego granicy okna do nowego okna; zachowanie decyzji architektonicznych, niezrealizowanych zadań, szczegółów implementacji; usunięcie zbędnych tool outputs i redundantnych wiadomości. Bezpieczna forma: tool result clearing.
2. **Structured note-taking** — agent regularnie zapisuje notatki poza kontekstem (plik NOTES.md, to-do list), które są wczytywane na żądanie; [[Claude Code]] stosuje ten wzorzec natywnie
3. **Sub-agent architectures** — wyspecjalizowane subagenty wykonują zadania z czystym kontekstem i zwracają skondensowane podsumowania (1000–2000 tokenów) do agenta głównego

**Just-in-time context retrieval**
- Agent przechowuje lekkie identyfikatory (ścieżki plików, zapytania, linki) zamiast ładować pełne dane z góry
- Dynamiczne ładowanie danych w runtime narzędziami (glob, grep, zapytania do bazy)
- Progressive disclosure: agent odkrywa kontekst stopniowo, utrzymując w pamięci tylko to, co potrzebne

## Kluczowe dane

- Context rot: zdolność precyzyjnego wyszukiwania informacji maleje przy każdym dodanym tokenie — efekt dotyczy wszystkich modeli, choć z różną intensywnością
- Subagenty mogą eksplorować dziesiątki tysięcy tokenów i zwracają tylko 1000–2000 tokenów podsumowania do agenta głównego
- [[Claude Code]] stosuje model hybrydowy: CLAUDE.md ładowany z góry + glob/grep dla just-in-time exploration

## Wnioski

- Kontekst to skończony zasób z malejącymi przychodami krańcowymi — każdy nowy token uszczupla budżet uwagi modelu; celem jest minimalizacja szumu, nie maksymalizacja ilości informacji
- [[Claude Code]] jest wzorcową implementacją context engineering: CLAUDE.md jako stały kontekst + narzędzia eksploracji just-in-time to konkretny pattern możliwy do zastosowania przy budowie własnych agentów i pluginów
- Architektura wieloagentowa to nie tylko obejście limitu kontekstu, ale też lepszy separation of concerns — subagenty eksplorują bez zaśmiecania kontekstu agenta koordynującego

## Cytat

> Kontekst należy traktować jak skończony zasób z malejącymi przychodami krańcowymi. Każdy nowy token wprowadzony do kontekstu uszczupla budżet uwagi modelu — dlatego dobry context engineering to znalezienie najmniejszego możliwego zestawu tokenów o wysokim sygnale, który maksymalizuje prawdopodobieństwo pożądanego zachowania.

## Zastosowanie

Przy budowie własnych pluginów [[Claude Code]] i narzędzi AI techniki z artykułu (compaction, just-in-time retrieval, sub-agent architectures) można zastosować bezpośrednio do optymalizacji agentów automatyzujących pracę NGO. Framework "goldilocks zone" dla system promptów jest bezpośrednio użyteczny przy tworzeniu skillów i komend w Cowork — pozwala unikać zarówno nadmiernej szczegółowości jak i zbyt ogólnych instrukcji. W szkoleniach z AI dla organizacji artykuł dostarcza solidnej podbudowy pojęciowej do wyjaśniania, dlaczego projektowanie kontekstu jest ważniejsze niż sam prompt.
