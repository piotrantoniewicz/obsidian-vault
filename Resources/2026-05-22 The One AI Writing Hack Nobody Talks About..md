---
categories:
  - Clippings
authors: ["[[Nate B Jones]]"]
url: "https://www.youtube.com/watch?v=ltbzgzZZmgI"
source: "[[Archives/2026-05-22 The One AI Writing Hack Nobody Talks About.|2026-05-22 The One AI Writing Hack Nobody Talks About.]]"
published: 2026-05-22
created: 2026-06-17
relevance: wysoka
tags:
  - "context-engineering"
  - "narzędzia-AI"
  - "strategia-AI"
---

# The One AI Writing Hack Nobody Talks About.

[[Nate B Jones]] analizuje sprawę kancelarii Sullivan & Cromwell, która złożyła do sądu wniosek z dziesiątkami sfabrykowanych lub błędnych cytatów — wygenerowanych przez AI. Kluczowy argument: przyczyną nie był zły model ani złe prompty, lecz chaotyczne środowisko pracy wokół modelu. Rozwiązaniem jest metodologia „project room" (data room) — przygotowanie ustrukturyzowanego obszaru roboczego z inwentarzem źródeł, dziennikiem konfliktów i listą brakujących danych PRZED zleceniem agentowi napisania finalnego dokumentu. Materiał jest transkryptem z YouTube i odnosi się do możliwości modeli [[Claude AI|Claude]] Opus 4.7 i [[ChatGPT]] 5.5 w zakresie długotrwałych zadań agentic na systemach plików.

## Frameworki i metody

**Metodologia Project Room (Data Room) — 4 etapy przed napisaniem dokumentu:**

1. **Inwentarz źródeł (Source Inventory)** — tabela, w której agent rejestruje ścieżkę każdego pliku, typ, datę, autorytatywność, czy plik jest aktualny czy zdezaktualizowany, jakie twierdzenia wspiera i jakie ma ograniczenia. To pierwsza rzecz, o którą prosimy agenta po zorganizowaniu folderu.

2. **Dziennik konfliktów (Conflict Log)** — agent identyfikuje sprzeczności między źródłami (stary PDF vs. aktualny plan, dwa dokumenty z różnymi datami). Pozwala użytkownikowi podjąć decyzje PRZED napisaniem finału, zamiast zostawić je modelowi do „wygładzenia".

3. **Lista brakujących kontekstów (Missing Context List)** — agent raportuje, czego mu brakuje do dobrego wykonania zadania. Brakujące dane są często ważniejsze niż dostępne — jeśli model nie wie, że czegoś brakuje, wynajduje odpowiedź.

4. **Raport duplikatów (Duplicates Report)** — w AI duplikaty to problem z rozumowaniem, nie tylko porządkiem. Trzy wersje planu bez oznaczenia aktualności mogą być mieszane przez model. Agent identyfikuje rodziny wersji i prawdopodobne duplikaty — decyzja należy do człowieka.

**Prompt po przygotowaniu pokoju projektowego** jest bardzo krótki: wskaż które źródło jest autorytatywne dla liczb, które dla kontekstu decyzji, które to tylko tło — i dopiero wtedy napisz.

## Wnioski

- Halucynacje AI w poważnej pracy wiedzy to efekt strukturalny — chaotyczne środowisko plików, a nie zły model; nie da się tego naprawić lepszym promptem.
- Nowe modele agentic (Opus 4.7, GPT 5.5) potrafią chodzić po drzewach folderów, porównywać daty, sprawdzać metadane — co zmienia pierwszą instrukcję w projekcie z „napisz dokument" na „zbuduj mi pokój roboczy".
- Podział ról: agent przygotowuje canvas (inwentarz, konflikty, braki, duplikaty), człowiek weryfikuje i podejmuje decyzje, agent pisze finalny dokument — to różnica między AI jako narzędziem a AI jako kolegą.

## Cytat

> Stare pytanie AI brzmiało: czy model może zrobić tę rzecz? Nowe pytanie brzmi: czy agent może pomóc przygotować warunki, w których dobra praca jest możliwa?

## Zastosowanie

W pracy z NGO przy tworzeniu strategii, raportów czy wniosków grantowych metodologia data room pozwala uniknąć błędów przy syntezie wielu źródeł (dokumenty projektowe, raporty, transkrypty rozmów). Dla szkoleń z AI: to gotowy framework do modułu o agentic workflows — konkretny, z realnym przykładem porażki prawniczej i trzema artefaktami do wdrożenia. Warto przetestować z [[Claude Code]] na własnych projektach klienckich.
