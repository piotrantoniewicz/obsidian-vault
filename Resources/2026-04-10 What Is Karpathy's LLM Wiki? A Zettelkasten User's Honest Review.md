---
categories: Clippings
authors: ["[[WenHao Yu]]"]
url: https://yu-wenhao.com/en/blog/karpathy-zettelkasten-comparison/
source: "[[Archives/2026-04-10 What Is Karpathy's LLM Wiki? A Zettelkasten User's Honest Review|2026-04-10 What Is Karpathy's LLM Wiki? A Zettelkasten User's Honest Review]]"
published: 2026-04-10
created: 2026-04-19
relevance: wysoka
tags:
  - "strategia-AI"
  - "LLM"
  - "context-engineering"
---

# What Is Karpathy's LLM Wiki? A Zettelkasten User's Honest Review

[[WenHao Yu]] przeprowadza uczciwe porównanie wzorca LLM Wiki [[Andrej Karpathy|Karpathy'ego]] z własnym systemem opartym na [[LYT]] i [[Zettelkasten]]ie. Główna teza Karpathy'ego: zamiast RAG (odtwarzania wiedzy przy każdym zapytaniu) warto zbudować persistentną wikię w Markdown, którą LLM kompiluje i utrzymuje — dzięki czemu koszt bookkeepingu spada do zera, a baza wiedzy ma efekt kumulacji. Yu potwierdza, że szkielety obu systemów są zbieżne, lecz wskazuje fundamentalną różnicę filozoficzną: LLM Wiki opiera się na agregacjach tematycznych (jedna strona = jeden temat), LYT/Zettelkasten na atomizacji (jedna karta = jedno pojęcie) — i tylko to drugie podejście eliminuje odwieczny problem klasyfikacji "do którego kontenera należy ten materiał?".

## Frameworki i metody

- **LLM Wiki Pattern (Karpathy)** — wzorzec budowy bazy wiedzy:
  - `raw/` — surowe źródła (artykuły, notatki, dokumenty)
  - `wiki/` — strony tematyczne utrzymywane przez LLM; wiele źródeł scala się w 1–2 strony
  - plik schematu (`CLAUDE.md`) — reguły i konfiguracja dla LLM
  - `index.md` — katalog stron (odpowiednik MOC)
  - LLM przy każdym ingeście: aktualizuje powiązane strony, flaguje sprzeczności, sugeruje nowe pojęcia wymagające własnej strony (lint)

- **Kluczowe różnice RAG vs LLM Wiki**:
  - RAG — każde zapytanie = ponowne wyprowadzenie odpowiedzi ze źródeł (bezstanowe, jednorazowe)
  - LLM Wiki — kompilacja raz, ciągłe utrzymanie (stanowe, kumulatywne); cross-referencje już istnieją, sprzeczności już oflagowane

- **Mapowanie LLM Wiki ↔ LYT**:
  - `raw/` ↔ `Atlas/Sources/`
  - `wiki/` ↔ `Atlas/Dots/` + `Maps/`
  - plik schematu ↔ `CLAUDE.md` + `SKILL.md`
  - `index.md` ↔ `Maps/` MOC

- **Mechanizmy z LLM Wiki warte integracji do LYT**:
  - Wykrywanie sprzeczności przy ingeście — LLM porównuje nowe źródło z istniejącymi kartami i flaguje konflikty
  - Chain updates — jedno nowe źródło może zaktualizować 10–15 stron jednocześnie
  - Lint — cykliczne przeglądy całej bazy: wykrywanie osieroconych kart, przestarzałych treści, brakujących pojęć

## Wnioski

- Wzorzec Karpathy'ego i LYT mają zbieżne szkielety, ale fundamentalną różnicę w granularności: agregacja tematyczna vs atomizacja — to drugie podejście eliminuje wieczny problem "do którego kontenera?", który nie znika wraz z LLM
- Ryzyko Model Collapse (Nature 2024) — LLM wielokrotnie przepisujący własne outputy może stopniowo tracić szczegóły; atomizacja z ludzką weryfikacją przed archiwizacją jest naturalną ochroną przed tym zjawiskiem
- Mechanizmy contradiction detection, lint i cross-card updates są wartościowe niezależnie od wyboru filozofii PKM i warto je zintegrować z istniejącym systemem [[LYT]]

## Cytat

> Nudna część utrzymywania bazy wiedzy to nie czytanie ani myślenie — to bookkeeping. Ludzie porzucają wiki, bo koszty utrzymania rosną szybciej niż wartość. LLM-y się nie nudzą.

## Zastosowanie

Dla Piotra budującego Second Brain w [[EPARAX]] artykuł dostarcza praktycznej mapy decyzji: czy warto adoptować wzorzec Karpathy'ego, czy pozostać przy atomizacji. Mechanizmy lint i contradiction detection to konkretne narzędzia do dodania do obecnego workflow z [[Claude Code|Claude Cowork]] bez zmiany filozofii. Jeśli Piotr planuje utrzymywać długoterminowe wiki tematyczne (np. fundraising NGO, AI dla organizacji), wzorzec LLM Wiki może mieć sens w tych obszarach jako warstwa obok atomicznych kart.
