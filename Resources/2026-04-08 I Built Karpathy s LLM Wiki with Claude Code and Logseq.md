---
categories: Clippings
authors: ["[[Mehmet Gökçe]]"]
url: https://mehmetgoekce.substack.com/p/i-built-karpathys-llm-wiki-with-claude
source: "[[Archives/2026-04-08 I Built Karpathy s LLM Wiki with Claude Code and Logseq|2026-04-08 I Built Karpathy s LLM Wiki with Claude Code and Logseq]]"
published: 2026-04-08
created: 2026-04-19
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "context-engineering"
  - "automatyzacja"
---

# I Built Karpathy's LLM Wiki with Claude Code and Logseq

[[Mehmet Gökçe]] zaimplementował pattern „LLM Wiki" opisany przez [[Andrej Karpathy]] — system, w którym [[Claude Code]] utrzymuje strukturyzowaną bazę wiedzy, automatycznie aktualizuje cross-references i sprawdza spójność danych, zamiast od nowa przeszukiwać źródła przy każdym zapytaniu. Kluczowa innowacja względem gista Karpathy'ego to dwuwarstwowa architektura L1/L2: stałe zasady ładowane do każdej sesji (L1) kontra głęboka wiedza projektowa dostępna na żądanie (L2). Wiki to nie notatnik — to skumulowany, rozrastający się artefakt wiedzy zasilany przez operacje ingest.

## Frameworki i metody

- **3-warstwowy model LLM Wiki (Karpathy)**: Raw Sources (URL, pliki, rozmowy) → The Wiki (strukturyzowane, cross-referenced strony) → The Schema (reguły rządzące strukturą, lint checks); 3 operacje: Ingest, Query, Lint
- **Architektura L1/L2**: L1 = pamięć [[Claude Code]] (~14 plików, auto-ładowane każdą sesję) — reguły, gotchas, credentials, preferencje; L2 = wiki w Logseq (~46 stron, na żądanie) — projekty, workflow, głęboka wiedza; reguła routingu: czy błąd bez tej wiedzy byłby krępujący/niebezpieczny? → L1; jedynie niewygodny? → L2
- **Schema jako kontrakt z LLM**: plik `Wiki___Schema.md` definiuje namespace'y, typy stron z wymaganymi polami, reguły lintowania (orphan pages, stale content, credential leak, minimum cross-references); bez schematu LLM tworzy niespójne strony — ze schematem możliwe są automatyczne kontrole jakości
- **Operacja Ingest (5 faz)**: Analyze & Extract → Scan Wiki (które strony dotknąć) → Update Pages (append, never overwrite) → Quality Gate (sprawdzenie schematu, cross-references, credentials) → Report; jedno zdanie wejściowe może zaktualizować 5 stron naraz
- **Lint z auto-naprawą**: skanuje orphan pages, stale content, brakujące właściwości, broken references, credential patterns; `--fix` auto-naprawia co można
- **Cechy dobrej strony wiki**: syntetyzowana wiedza (nie skopiowane notatki), datowane metryki, decyzje z uzasadnieniem, warstwowy detail, cross-references, sekcja otwartych pytań

## Kluczowe dane

- Wiki po tygodniu: 46 stron, 8 namespace'ów, 2-warstwowy cache
- Setup zajmuje 5 minut; projekt open source: github.com/MehmetGoekce/llm-wiki
- Reguła L1/L2: credentials MUSZĄ być w L1 (nie w git-tracked wiki)

## Wnioski

- Różnica między RAG a LLM Wiki: [[RAG]] zaczyna od nowa przy każdym zapytaniu; wiki akumuluje syntetyzowaną wiedzę — każdy ingest czyni ją gęstszą i bardziej wartościową (efekt złożony)
- Architektura L1/L2 rozwiązuje konkretny problem [[Claude Code]]: nie wszystko powinno być ładowane za każdym razem, ale część wiedzy musi być dostępna przed pierwszym pytaniem — analogia do hierarchii pamięci podręcznej CPU
- Schema warto zdefiniować od początku nawet dla małej bazy — jest znacznie trudniejsza do dodania później, gdy strony mają już niespójną strukturę

## Cytat

> Nudna część utrzymania bazy wiedzy to nie czytanie ani myślenie — to bookkeeping. LLM-y są do tego idealne. Nie nudzą się, nie pomijają aktualizacji cross-references w piątkowe popołudnie.

## Zastosowanie

Wzorzec LLM Wiki z architekturą L1/L2 jest bezpośrednio stosowalny do rozwijania własnego Second Brain w [[Obsidian]] + [[Claude]] Cowork — szczególnie podział na stałą pamięć sesji (reguły pracy, preferencje, kontekst projektów) i głębszą bazę wiedzy dostępną na żądanie. Schema z namespace'ami i typami stron można zaadaptować do struktury EPARAX. Warto rozważyć implementację komendy `/wiki ingest` jako pluginu do przetwarzania nowych materiałów bezpośrednio do vaultu.
