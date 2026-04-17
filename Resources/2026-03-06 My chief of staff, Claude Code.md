---
categories: Clippings
authors: "[[Jim Prosser]]"
url: https://x.com/jimprosser/status/2029699731539255640
source: "[[Archives/2026-03-06 My chief of staff, Claude Code|2026-03-06 My chief of staff, Claude Code]]"
published: 2026-03-06
created: 2026-03-07
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
---

# My chief of staff, Claude Code

Jim Prosser — solo konsultant PR bez doświadczenia programistycznego — opisuje jak w 36 godzin zbudował z pomocą [[Claude Code]] w pełni funkcjonalny system automatyzacji operacji swojej firmy. System składa się z nocnego skanera maili (tworzy zadania z atrybutami do porannego przeglądu), porannego triaż (klasyfikacja zadań na 4 kategorie: wykonaj/przygotuj/moje/odłóż), 6 równoległych subagentów (szkice maili, notatki klientów, planowanie spotkań, research) oraz time-blockera kalendarza z rzeczywistymi czasami dojazdu z Google Maps API. System oszczędza 30–45 minut każdego ranka i eliminuje stały "cognitive load" związany z zarządzaniem operacjami.

## Frameworki i metody

**Architektura systemu AI (Chief of Staff)**
- **Nocne automatyzacje** (model Sonnet): skanowanie maili + tworzenie zadań z metadanymi; aktualizacja kalendarza o czasy dojazdu
- **AM Sweep** (przycisk na Stream Deck): pobranie zadań + kontekstu → klasyfikacja: Zielony (Claude wykonuje), Żółty (Claude 80%, ja kończę), Czerwony (moje), Szary (odłóż)
- **6 subagentów równolegle** (model Opus): szkice maili, notatki klientów w [[Obsidian]], planowanie spotkań, research; każdy z własnym oknem kontekstu i dostępem do narzędzi
- **Time Blocker**: zamiana zadań na zdarzenia kalendarza z uwzględnieniem lokalizacji, batching zadań offline, priorytetyzacja

**Zasada dispatch/prep/yours/skip (kluczowy framework)**
- System nigdy nie wysyła maili — tylko szkicuje do review
- Zasada: im bardziej ambigualne zadanie, tym więcej "prep" (80% gotowości) zamiast "dispatch" (pełna egzekucja)
- Dokumenty strategiczne i komunikacja relacyjna — zawsze 100% ludzkie

## Kluczowe dane
- 36 godzin od pomysłu do działającego systemu (bez znajomości programowania)
- Oszczędność 130–195 godzin rocznie (30–45 min/dziennie × 5 dni × 52 tygodnie)
- Koszt: ~$100/miesiąc (plan Claude Max) + ~$5-10 za API overrun; ekwiwalent asystenta wirtualnego: $400–$1000/miesiąc

## Wnioski
- [[Claude Code]] pozwala myśleć w kategoriach architektury systemu (co z czym się komunikuje, jakie są granice ludzkie/AI) bez znajomości składni kodu — kluczowy insight dla non-programistów
- Subagenty działające równolegle są przełomem: nie jeden chatbot sekwencyjny, lecz kilku wyspecjalizowanych agentów z oddzielnymi kontekstami
- Najważniejsza decyzja w projektowaniu automatyzacji: co zostaje ludzkie; błąd w obu kierunkach (za mało vs za dużo automatyzacji) jest kosztowny

## Cytat
> "Krok wstecz od automatyzacji to nie tchórzostwo, to projekt."

## Zastosowanie
Architektura dispatch/prep/yours/skip może być bezpośrednio zastosowana przy projektowaniu własnych automatyzacji lub przy doradztwie NGO w zakresie wdrażania AI do procesów operacyjnych.
