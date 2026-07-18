---
categories:
  - "Emails"
published: 2026-07-09
created: 2026-07-18
labels:
  - "AI with ALLIE"
relevance: średnia
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "automatyzacja"
---

# My Exact AI Stack: Which Model I Use for What

Allie K. Miller publikuje swój aktualny stack narzędzi AI po premierze dwóch nowych modeli frontier — Fable 5 (Anthropic) i GPT-5.6 (OpenAI). Zamiast ogólników poleca konkretny model do konkretnego zadania: [[Claude Code]] jako główne środowisko pracy, Fable 5 jako doradcę dla tańszych agentów, Opus 4.8 jako AI Chief of Staff, Sonnet 5 do subagentów, a Codex + GPT-5.6 do computer use. Autorka podkreśla, że wybór modelu to dziś decyzja kosztowo-wydajnościowa, nie tylko jakościowa, i że w pracy zespołowej harnessy AI muszą przestać być „single player" — stąd jej dedykowany kanał Slack łączący zespół z flotą agentów.

## Frameworki i metody
- **Wzorzec doradca-wykonawca** — tańszy, szybszy model (np. Sonnet 5) prowadzi codzienną pracę i eskaluje do droższego, mocniejszego modelu (Fable 5) tylko gdy utknie na powtarzalnym błędzie lub przed uznaniem zadania za zakończone; komenda `/advisor` w [[Claude Code]]
- **Routing modeli wg zadania** — Chief of Staff / orkiestracja: Opus 4.8 (tryb „high"); subagenci: Sonnet 5 (liczy się szybkość i równoległość); coding złożonych systemów: Fable 5 i GPT-5.6 razem, jeden jako manager, drugi jako executor; brainstorming: modele mid-tier wystarczą
- **Dyktowanie zamiast pisania** — [[Wispr Flow]] do wprowadzania tekstu głosem bezpośrednio do Claude Code, Codex, iMessage i Slacka

## Kluczowe dane
- Sonnet 5 z Fable 5 jako doradcą osiąga ~92% wyniku Fable 5 solo na SWE-bench Pro przy ~63% ceny
- Fable 5: 80,3% na SWE-bench Pro; GPT-5.6 Sol: 88,8% na Terminal-Bench (91,9% w trybie „ultra" z podagentami)
- Koszty: Fable 5 — 10$/50$ za milion tokenów (input/output); GPT-5.6 Sol — 5$/30$

## Wnioski
- Wybór modelu do agentów to dziś kompromis koszt/jakość, nie tylko „najlepszy model" — warto stosować tańsze modele do wykonania i droższe tylko jako doradcę, co można przełożyć na własne wdrożenia [[automatyzacja|automatyzacji]] w pracy z organizacjami
- Praca zespołowa z AI wymaga wspólnej przestrzeni (np. dedykowany kanał [[Slack]]), bo domyślnie większość harnessów AI jest „single player" — istotne przy budowaniu procesów zespołowych, nie tylko indywidualnych
- Publikowane benchmarki są nieobiektywne, bo każde laboratorium publikuje wykres, na którym wygrywa — traktować je kierunkowo, testować na własnych przypadkach użycia zamiast ufać marketingowym porównaniom

## Zastosowanie
Wzorzec doradca-wykonawca i routing modeli wg zadania to gotowy szablon do zaprojektowania własnej floty agentów w automatyzacji procesów klientów. Przydatne też jako argument w szkoleniach: dobór modelu to decyzja biznesowa (koszt vs jakość), nie tylko techniczna.
