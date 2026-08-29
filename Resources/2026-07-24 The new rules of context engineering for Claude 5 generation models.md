---
categories:
  - Clippings
authors:
  - "[[Anthropic]]"
url: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
source: "[[Archives/2026-07-24 The new rules of context engineering for Claude 5 generation models|2026-07-24 The new rules of context engineering for Claude 5 generation models]]"
published: 2026-07-24
created: 2026-08-28
relevance: wysoka
tags:
  - context-engineering
  - prompt-engineering
  - narzędzia-AI
---

# The new rules of context engineering for Claude 5 generation models

Anthropic opisuje, jak zmienił się sposób prowadzenia [[Claude Code]] wraz z nową generacją modeli (Claude Opus 5, Claude Fable 5) — z systemowego promptu usunięto ponad 80% treści bez mierzalnej straty jakości w evalach kodowania. Główna teza: nowsze modele mają lepszy osąd i nie potrzebują sztywnych reguł, przykładów ani powtórzeń — zamiast tego liczy się dobry design narzędzi, progresywne ujawnianie kontekstu (skille, CLAUDE.md, memory) i bogate referencje (kod, testy, rubryki) zamiast prostych specyfikacji tekstowych. Tekst formułuje to jako listę sześciu przesunięć „wtedy → teraz" w budowaniu kontekstu dla Claude. To bezpośrednia wskazówka dla każdego, kto pisze własne CLAUDE.md, skille i pluginy Claude Code — nadmiar reguł i przykładów może dziś ograniczać model bardziej niż mu pomagać.

## Frameworki i metody

**Sześć przesunięć w context engineeringu (wtedy → teraz):**

1. **Dawaj Claude sztywne reguły → Pozwól Claude użyć osądu** — starsze modele wymagały twardych zasad (np. „nigdy nie pisz komentarzy"), bo bez nich popełniały błędy. Nowsze modele lepiej radzą sobie z niejednoznacznością i sprzecznymi instrukcjami z różnych źródeł (system prompt, skille, CLAUDE.md, prośba użytkownika).
2. **Dawaj przykłady użycia narzędzi → Projektuj dobre interfejsy narzędzi** — przykłady zawężają przestrzeń eksploracji modelu. Lepiej inwestować w ekspresyjne parametry narzędzi (np. enum statusów w [[Todo tool]]), które same podpowiadają sposób użycia.
3. **Wszystko na starcie → Progresywne ujawnianie** — zamiast jednego centralnego pliku ze wszystkimi praktykami, warto budować drzewo mniejszych plików (skille, [[CLAUDE.md]]) ładowanych dopiero wtedy, gdy są potrzebne. Dotyczy to też narzędzi — część z nich to „deferred loading" przez [[ToolSearch]], żeby nie zajmowały kontekstu, dopóki nie są używane.
4. **Powtarzaj instrukcje → Proste opisy narzędzi** — instrukcje obsługi narzędzia lepiej umieszczać raz, w opisie samego narzędzia, niż powtarzać je dodatkowo w systemowym promptcie.
5. **Pamięć w CLAUDE.md → Auto-memory** — zamiast ręcznego zapisywania faktów do CLAUDE.md, Claude automatycznie zapamiętuje informacje istotne dla pracy i użytkownika.
6. **Proste specyfikacje → Bogate referencje** — proste pliki markdown z planami ustępują miejsca bogatszym referencjom: artefaktom HTML, testom, kodowi z innego repo do przeniesienia, rubrykom oceniającym gust (np. co to znaczy „dobry design API"), weryfikowanym przez osobne agenty.

## Kluczowe dane
- Anthropic usunęło ponad 80% systemowego promptu Claude Code dla modeli klasy Claude Opus 5 / Claude Fable 5 bez mierzalnej straty w evalach kodowania.

## Wnioski
- Nadmiar sztywnych reguł w [[CLAUDE.md]] i skillach może dziś szkodzić bardziej niż pomagać — nowsze modele lepiej radzą sobie z niejednoznacznością i osądem sytuacyjnym niż ze sprzecznymi, nakładającymi się instrukcjami.
- Progresywne ujawnianie kontekstu — dzielenie dokumentacji i skilli na mniejsze pliki ładowane na żądanie — to lepsza strategia niż jeden centralny plik-repozytorium wszystkich praktyk.
- Bogate referencje (kod, testy, rubryki, artefakty) dają dziś wyższą wierność przekazu niż proste opisy tekstowe czy zrzuty ekranu — warto to uwzględniać przy projektowaniu własnych pluginów i skilli.

## Cytat
> Częstym mitem jest przekonanie, że CLAUDE.md czy pliki Skill.md powinny być centralnym repozytorium każdej znanej praktyki, na jaką można natrafić — zamiast tego warto mieć drzewo plików ładowanych we właściwym momencie.

## Zastosowanie
Bezpośrednia wskazówka do przeglądu własnych pluginów Claude Code (np. `artykuly-ngo`, `clippings-to-notes`) i plików CLAUDE.md w vaultcie — warto sprawdzić, czy nie są przeciążone sztywnymi regułami i przykładami, które można zastąpić lepszym designem narzędzi i progresywnym ujawnianiem. Przydatne też przy budowie Second Brain (EPARAX + Obsidian + Cowork) jako argument za strukturą wielu małych, ładowanych na żądanie plików zamiast jednego dużego dokumentu.
