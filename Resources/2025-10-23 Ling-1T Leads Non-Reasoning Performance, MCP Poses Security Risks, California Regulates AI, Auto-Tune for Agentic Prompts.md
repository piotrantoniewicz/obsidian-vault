---
categories:
  - "Emails"
published: 2025-10-23
created: 2026-04-24
labels:
  - "The Batch"
relevance: wysoka
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "narzędzia-AI"
---

# Ling-1T Leads Non-Reasoning Performance, MCP Poses Security Risks, California Regulates AI, Auto-Tune for Agentic Prompts

Andrew Ng opisuje praktyczne podejście do analizy błędów (error analysis) w systemach agentycznych — kluczowego narzędzia diagnostycznego dla budowniczych pipeline'ów AI. Główna idea: zamiast oceniać wyłącznie wyniki końcowe, należy systematycznie przeglądać ślady (traces) poszczególnych kroków workflow i porównywać je z jakością wykonania przez człowieka (Human Level Performance). Autor zachęca do zaczynania od prostych, nieformalnych analiz — już kilka przejrzanych traces może wskazać, gdzie agent zawodzi. Szybki rozwój [[LLM]]-ów sprawia, że warto regularnie przebudowywać pipeline'y: usuwać sztywne reguły i delegować więcej decyzji modelowi. To praktyczna wskazówka dla każdego, kto buduje systemy agentyczne — wymagają one ciągłej inżynierii, nie jednorazowej konfiguracji.

## Frameworki i metody

- **Error analysis procedure** — systematyczne przeglądanie traces kroków workflow i porównywanie ich jakości do Human Level Performance (HLP); zaczyna się od kilku przykładów, a z dojrzewaniem systemu ewoluuje ku rygorystycznej analizie statystycznej
- **Trace-based debugging** — dla każdego wejścia, gdzie wynik końcowy jest słaby, przegląda się wyniki każdego kroku pośredniego, by zidentyfikować, który krok najczęściej odpowiada za problem
- **Ripping out scaffolding** — pattern refaktoryzacji agentic workflow: gdy dostępny jest mocniejszy [[LLM]], usuwa się dodatkowe kroki "porządkujące" i deleguje więcej bezpośrednio do głównego modelu
- **Zastępowanie twardych reguł decyzjami LLM** — kolejny pattern ewolucji: krok wcześniej oparty na hard-coded logic (np. decyzja, które strony pobrać) zastępowany jest autonomiczną decyzją agenta; sygnałem do zmiany jest error analysis pokazująca, że sekwencja kroków łącznie wypada poniżej HLP, choć każdy krok z osobna wygląda dobrze

## Kluczowe dane

- Przykładowy workflow Deep Research agenta: (i) generowanie zapytań wyszukiwania, (ii) wywołanie API wyszukiwarki, (iii) selekcja najcenniejszych źródeł, (iv) napisanie raportu
- Rarchitekturę workflow uzasadnia error analysis pokazująca, że jednotkowe kroki są dobre, ale razem — zbyt sztywne

## Wnioski

- Analiza błędów w [[automatyzacja|systemach agentycznych]] powinna być prowadzona na poziomie poszczególnych kroków workflow, nie tylko wyniku końcowego — traces to podstawowe narzędzie diagnostyczne, dostępne nawet przy małej liczbie przykładów
- Szybki rozwój [[LLM]]-ów umożliwia regularne upraszczanie pipeline'ów poprzez zastępowanie twardych reguł decyzjami modelu — co prowadzi do bardziej elastycznych i wydajnych systemów [[automatyzacja|automatyzacji]]
- Jeśli error analysis pokazuje, że poszczególne kroki działają dobrze, ale razem generują słaby wynik — to sygnał, że struktura workflow jest zbyt sztywna i wymaga przebudowy architektury, nie tuningu

## Cytat

> Zacznij od przejrzenia kilku traces, żeby poczuć, gdzie agent zawodzi — rygorystyczna analiza przyjdzie z dojrzewaniem systemu.

## Zastosowanie

Przy budowaniu automatyzacji w [[Make.com]] lub [[Langflow]] dla NGO, error analysis traces pomoże zidentyfikować, który krok pipeline'u zawodzi — np. przy przetwarzaniu zapytań od darczyńców czy generowaniu raportów. Podejście "zacznij od kilku przykładów" jest idealne dla projektów bez dużych zbiorów danych testowych — wysoka wartość przy niskim koszcie wejścia. Regularne przeglądanie wyników kroków pośrednich zwiększy niezawodność automatyzacji wspierających fundraising bez potrzeby fine-tuningu modeli.
