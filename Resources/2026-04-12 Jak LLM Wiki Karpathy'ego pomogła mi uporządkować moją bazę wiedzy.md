---
categories:
  - Clippings
authors: ["[[Pawel Lipowczan]]"]
url: "https://pawel.lipowczan.pl/blog/llm-knowledge-base-brain-karpathy"
source: "[[Archives/2026-04-12 Jak LLM Wiki Karpathy'ego pomogła mi uporządkować moją bazę wiedzy|2026-04-12 Jak LLM Wiki Karpathy'ego pomogła mi uporządkować moją bazę wiedzy]]"
published: 2026-04-12
created: 2026-06-17
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "context-engineering"
---

# Jak LLM Wiki Karpathy'ego pomogła mi uporządkować moją bazę wiedzy

[[Pawel Lipowczan]] opisuje ewolucję od ręcznych notatek w [[Obsidian]] do systemu zarządzania wiedzą pilnowanego przez agenta AI ([[Claude Code]]), którą skrystalizował framework „LLM Wiki" [[Andrej Karpathy|Karpathy'ego]] z kwietnia 2026. Karpathy nie był dla autora odkryciem nowego świata, lecz katalizatorem: dał nazwy warstwom (raw sources, wiki, schema), których Lipowczan używał organicznie od 2022 roku. Centralnym konceptem jest **progressive disclosure** — organizacja notatek tak, żeby agent AI mógł je znaleźć bez zaśmiecania okna kontekstowego: trzy poziomy indeksów (vault-map → catalog → graph) zastępują grep-owanie 185 plików. Artykuł to konkretna architektura z liczbami i workflow, nie teoria: 185 notatek, CLAUDE.md z 300+ liniami, 4 zdefiniowane przepływy pracy.

## Frameworki i metody

**Trzy warstwy systemu (wg Karpathy'ego, zaimplementowane przez autora):**

| Warstwa | Karpathy | Implementacja autora |
|---|---|---|
| Raw sources | Immutable drop zone | `_raw/inbox/` — poza buildem |
| Wiki | LLM-generated .md files | `/content/<TOPIC>/` — budowane i publikowane |
| Schema | Config document | `CLAUDE.md` — 300+ linii konfiguracji agenta |

**Progressive disclosure — trzy indeksy nawigacyjne:**
- **vault-map.md** (~80 linii) — bird's-eye view całego vault; agent czyta zawsze jako pierwszy
- **catalog.md** (~650 linii) — jedna linia per notatka z tytułem, kategorią i opisem; agent sięga po konkretną notatkę
- **graph.md** — wikilink graph (outgoing + incoming edges); agent czyta gdy potrzebuje kontekstu powiązań

Dzięki temu agent czyta ~3000 słów zamiast ~92 500 słów (185 plików × ~500 słów) — **30× mniej kontekstu przy trafniejszych odpowiedziach**.

**Cztery workflow:**
1. **INGEST** — drop pliku do inbox/ → `ingest` w [[Claude Code]] → agent nawiguje, tworzy notatkę, dodaje wikilinki bidirectionally, archiwizuje źródło, aktualizuje 3 indeksy. Dotyka 10–15 plików w jednym passie. 5 min vs. 20–30 min ręcznie.
2. **COMPILE** — synteza wielu notatek w jeden skompilowany artykuł z cytowaniami i attribution do źródeł
3. **Q&A** — pytanie → agent czyta indeksy, identyfikuje kandydatów, syntetyzuje odpowiedź z cytowaniami z własnych notatek
4. **LINT** — health-check vault: broken wikilinks, orphan notes, brakujące summaries, TODO markery, niekompletny frontmatter

**CLAUDE.md — zasady pisania:**
- Pisać ręcznie, nie generować przez LLM (badanie ETH Zurich 2026: LLM-generated agentfiles pogarszały performance przy 20%+ wyższym koszcie)
- Zaczynać od ~50–80 linii, rozbudowywać na podstawie konkretnych failures
- Każda reguła musi mieć uzasadnienie

## Kluczowe dane

- 185 notatek w 13 kategoriach tematycznych (stan po 3 latach iteracji)
- CLAUDE.md: 300+ linii (vs. ~80 na początku Fazy 3)
- Progressive disclosure: 3000 słów kontekstu na zapytanie vs. 92 500 słów bez indeksów
- INGEST: 5 min z agentem vs. 20–30 min ręcznie; jeden pass dotyka 10–15 plików

## Wnioski

- Kluczowy podział ról: agent odpowiada za bookkeeping (tworzenie, linkowanie, indeksowanie, LINT), człowiek za kuratorstwo (co ingestować, jakie pytania zadawać, co kompilować) — to odwrócenie problemu tradycyjnego PKM, gdzie utrzymanie rośnie wykładniczo.
- [[progressive disclosure]] działa jako fundament, nie optymalizacja: bez nawigacyjnych indeksów agent albo dostaje za dużo kontekstu (cały vault), albo wymaga ręcznego wskazywania plików — indeksy eliminują oba problemy jednocześnie.
- System git-based (każda zmiana tracked, każdy ingest to commit) to safety net bez którego nie warto oddawać agentowi kontroli nad setkami plików — błąd agenta da się cofnąć przez `git revert`.

## Cytat

> Nudna część utrzymania knowledge base to nie czytanie ani myślenie. To bookkeeping. LLM-y się nie nudzą.

## Zastosowanie

Dla własnego projektu „Second Brain w strukturze EPARAX" — artykuł to gotowy blueprint z konkretnymi decyzjami architektonicznymi i uzasadnieniami. Szczególnie użyteczne: progressive disclosure (trzy indeksy), zasady pisania CLAUDE.md (ręcznie, nie LLM-generated) i workflow INGEST jako wzorzec dla procesowania clippingów. Można zaadaptować framework bezpośrednio do aktualnej struktury vault i [[Claude Code]] skills do zarządzania wiedzą.
