---
categories: Clippings
authors: ["[[How I AI]]"]
url: https://www.youtube.com/watch?v=jwGQ9CrqVdA
source: "[[Archives/2026-04-13 Claude Cowork tutorial for non-engineers JJ Englert (Tenex)|2026-04-13 Claude Cowork tutorial for non-engineers JJ Englert (Tenex)]]"
published: 2026-04-13
created: 2026-04-13
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "context-engineering"
---

# Claude Cowork tutorial for non-engineers — JJ Englert (Tenex)

Transkrypt wywiadu z JJ Englertem, zaawansowanym użytkownikiem [[Claude Cowork]], na kanale [[How I AI]] prowadzonym przez [[Claire Vo]]. Englert pokazuje krok po kroku, jak niedewelopery mogą zacząć używać Cowork do codziennej pracy — od połączenia narzędzi biznesowych ([[Slack]], [[Gmail]], [[Notion]]) jednym kliknięciem, przez budowanie struktury projektów, po tworzenie wieloagentowych systemów recenzji. Centralna teza: kluczem do efektywności Cowork jest zbudowanie "brain file" — pliku Markdown z kontekstem o użytkowniku, preferencjach i projektach — dzięki któremu Claude nigdy nie zaczyna od zera. Cowork jest opisany jako pomost między zwykłym czatem AI a [[Claude Code]]: przeznaczony dla knowledge workers, którzy chcą, żeby AI faktycznie robiło rzeczy za nich.

## Frameworki i metody

**Struktura projektu w Claude Cowork:**
- **Projekt = folder na komputerze** — analogia do organizacji Google Drive lub Notion; Claude ma dostęp do plików w folderze i może w nim pracować
- **Brain file** — plik Markdown z preferencjami roboczymi użytkownika, listą członków zespołu, kontekstem projektów i sposobem pracy; ładowany automatycznie z każdym zadaniem
- **Daily Operating System** — projekt-szablon do zarządzania codzienną pracą w Cowork; opisany jako starter-kit do pobrania

**Multi-agent sub-advisory skill:**
- Uruchomienie 3 sub-agentów z osobnymi oknami kontekstu i różnymi personami (np. szef, partner inżynierski, klient)
- Każdy agent ocenia pracę z innej perspektywy i daje niezależny feedback
- Zastosowanie: recenzja PRD dla product managerów, analiza z perspektywy ICP w marketingu, walidacja pomysłów dla solo founderów

## Wnioski

- "Brain file" z kontekstem użytkownika to kluczowy unlock Cowork — przenosi kontekst między sesjami i eliminuje problem "zaczynania od nowa" znany z wątków chatowych
- Cowork i [[Claude Code]] to komplementarne narzędzia: Cowork dla trybu biznesowo-produktywnościowego (klikanie, łączenie narzędzi, dokumenty), Claude Code dla trybu budowania i programowania
- Sub-agenci z różnymi personami (szef, klient, partner) to praktyczna metoda wieloperspektywicznej walidacji pracy bez angażowania realnych ludzi

## Zastosowanie

Piotr buduje Second Brain w Obsidian połączony z Claude Cowork — ten tutorial pokazuje, jak zaawansowani użytkownicy strukturyzują projekty, co może zainspirować udoskonalenie własnego workspacu i architektury plików kontekstowych. Koncept "brain file" z preferencjami roboczymi to wzorzec bezpośrednio do zaadaptowania w pluginach i skillach Claude Code — Piotr już to robi w pliku `omnie.md`. Multi-agent sub-advisory (perspektywy szefa, klienta, partnera) warto włączyć jako case study do szkoleń dla NGO — jako tania metoda krytycznej walidacji strategii i dokumentów bez budżetu na zewnętrznych konsultantów.
