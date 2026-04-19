---
categories: Clippings
authors: ["[[Alex Finn]]", "[[Peter Yang]]"]
url: https://www.youtube.com/watch?v=D0nDWQdN3F4
source: "[[Archives/2025-09-07 Full Tutorial Build an AI Life Co-Pilot with Claude Code in 25 Minutes Alex Finn|2025-09-07 Full Tutorial Build an AI Life Co-Pilot with Claude Code in 25 Minutes Alex Finn]]"
published: 2025-09-07
created: 2026-04-19
relevance: średnia
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "strategia-AI"
---

# Full Tutorial: Build an AI Life Co-Pilot with Claude Code in 25 Minutes — Alex Finn

[[Alex Finn]] zbudował „Claude Life" — osobisty system operacyjny oparty na [[Claude Code]], który automatyzuje research do newslettera, analizuje notatki i agreguje codzienne wiadomości przez custom slash commands i sub-agenty. Kluczowa teza: [[Claude Code]] to nie narzędzie do kodowania — to agent AI, który wykonuje dowolne zadania, jeśli właściwie się go skonfiguruje. Najważniejsza umiejętność w erze AI to nawyk zadawania sobie pytania „jak mogę wdrożyć AI w to zadanie?" przy każdej czynności dnia.

## Frameworki i metody

- **Claude Life OS** — folder na komputerze z podkatalogami: brain dumps, newsletter, daily briefs; każda funkcja to osobny slash command + sub-agent
- **Newsletter Researcher** — slash command uruchamia sub-agenta, który czyta newslettery konkurencji (lista linków w markdown), identyfikuje trendy, a następnie pisze szkic w głosie autora; oszczędza 2–3 godz. tygodniowo
- **Brain Dump Analysis** — codzienne notatki z ostatnich 30 dni analizowane pod kątem powtarzających się tematów, wzorców i potencjalnych nowych filarów treści
- **Daily Brief Agent** — slash command przeszukuje internet w poszukiwaniu najnowszych wiadomości z wybranych obszarów (AI, tech, entrepreneurship), zwraca priorytety, trendy i proponowane kąty treści
- **Budowanie systemu przez prompt** — zamiast pisać prompty ręcznie, Alex prosi [[Claude Code]] o zbudowanie prompta do slash commanda; AI sama tworzy instrukcje dla sub-agentów na podstawie dostarczonych linków i kontekstu

## Wnioski

- Wzorzec „agentycznego życia" polega na delegowaniu powtarzalnych zadań intelektualnych do [[Claude Code]] przez slash commands — nie tylko kodowanie, lecz research, analiza, raportowanie
- Sub-agenty działają na lokalnych plikach markdown, co daje pełną kontrolę nad danymi i umożliwia integrację z narzędziami jak [[Obsidian]]
- Kluczowy reflex: przy każdym zadaniu pytaj „jak Claude może to zautomatyzować?" — system rośnie organicznie w miarę pracy

## Zastosowanie

Wzorzec „Claude Life OS" jest bezpośrednio przydatny przy rozwijaniu własnego Second Brain w [[Obsidian]] — slash commands do analizy notatek, research do newslettera czy codziennych briefów można zaadaptować do własnego workflow. Warto zbudować analogiczny system dla pracy z NGO: agent do monitorowania trendów w fundraisingu, analiza brain dumpów z klientami, automatyczne szkice komunikatów.
