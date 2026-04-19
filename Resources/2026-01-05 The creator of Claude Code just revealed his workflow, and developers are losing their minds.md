---
categories: Clippings
authors: ["[[Michael Nuñez]]"]
url: https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are
source: "[[Archives/2026-01-05 The creator of Claude Code just revealed his workflow, and developers are losing their minds|2026-01-05 The creator of Claude Code just revealed his workflow, and developers are losing their minds]]"
published: 2026-01-05
created: 2026-04-19
relevance: średnia
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "strategia-AI"
---

# The creator of Claude Code just revealed his workflow, and developers are losing their minds

[[Boris Cherny]], twórca [[Claude Code]] w [[Anthropic]], ujawnił swój osobisty workflow, który wywołał dyskusję w środowisku programistycznym. Jego podejście to równoległe uruchamianie 5 instancji [[Claude Code]] jednocześnie — zamiast pisania kodu linijka po linijce, działa jak dowódca floty agentów AI. Kluczowa teza: bottleneck w pracy z AI to nie szybkość generowania tokenów, lecz czas człowieka na korektę błędów — dlatego warto płacić „compute tax" za mądrzejszy model i oszczędzać „correction tax" później.

## Frameworki i metody

- **Równoległa praca wielu agentów** — 5 instancji [[Claude Code]] w zakładkach terminala (numerowanych 1–5) z powiadomieniami systemowymi; każda obsługuje inne zadanie jednocześnie (testy, refaktoryzacja, dokumentacja)
- **CLAUDE.md jako żywa baza wiedzy** — jeden plik w repozytorium git; gdy AI popełni błąd, trafia do CLAUDE.md jako reguła; codebase staje się samokorygującym organizmem — im dłużej pracujesz, tym lepszy agent
- **Slash commands do automatyzacji** — np. `/commit-push-pr` obsługuje cały cykl git (commit, push, PR) jednym poleceniem; komendy są wersjonowane w repozytorium
- **Weryfikacja pętlowa** — agent automatycznie testuje każdą zmianę przez przeglądarkę (rozszerzenie Chrome), iteruje dopóki UI działa i UX jest poprawny; weryfikacja własna AI poprawia jakość wyniku 2–3×
- **Specjalizowane sub-agenty** — `code-simplifier` do czyszczenia architektury po głównej pracy, `verify-app` do end-to-end testów przed wdrożeniem

## Kluczowe dane

- 5 równoległych instancji [[Claude Code]] w terminalu + 5–10 sesji na claude.ai jednocześnie
- Weryfikacja własna AI poprawia jakość kodu o 2–3×
- [[Claude Code]] osiągnął $1 mld ARR

## Wnioski

- Model CLAUDE.md to wzorzec transferowalny poza kod: każdy „błąd" AI staje się regułą, która stale doskonali agenta — warto stosować analogiczne pliki kontekstowe w dowolnym projekcie AI
- Wybór wolniejszego, mądrzejszego modelu ([[Claude Opus]]) jest często szybszy w praktyce niż użycie szybkiego modelu z wieloma korektami — quality over speed
- Przejście mentalne od „AI jako asystent" do „AI jako workforce" to klucz do 5-krotnego wzrostu produktywności

## Cytat

> Narzędzia do pięciokrotnego zwiększenia ludzkiego output już istnieją. Wymagają tylko gotowości do przestania traktowania AI jako asystenta i zaczęcia traktowania go jak siłę roboczą.

## Zastosowanie

Wzorzec CLAUDE.md — dokumentowanie błędów i reguł AI w jednym pliku — można wdrożyć natychmiast w pracy z własnymi narzędziami AI i pluginami [[Claude Code]]. Równoległa praca wielu agentów jest przydatna przy większych projektach automatyzacji dla klientów NGO. Filozofia „mądrzejszy model = mniej korekt" warta uwzględnienia przy doborze modeli do własnych workflow.
