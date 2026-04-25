---
categories: Clippings
authors: ["[[Anthropic]]"]
url: https://claude.com/blog/introducing-routines-in-claude-code
published: 2000-04-14
created: 2026-04-24
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "produkty-cyfrowe"
source: "[[Archives/2000-04-14 Introducing routines in Claude Code|2000-04-14 Introducing routines in Claude Code]]"
---

# Introducing routines in Claude Code

[[Anthropic]] wprowadza *routines* w [[Claude Code]] — mechanizm automatyzacji, który pozwala skonfigurować zadanie (prompt + repozytorium + connectory) i uruchamiać je według harmonogramu, przez API lub w odpowiedzi na zdarzenia zewnętrzne, bez konieczności utrzymywania własnej infrastruktury. Routines działają na serwerowej infrastrukturze [[Claude Code]], co eliminuje zależność od uruchomionego laptopa. To istotny krok w kierunku w pełni zautomatyzowanego cyklu wytwarzania oprogramowania — od triażu błędów, przez weryfikację deploymentu, po automatyczne review PR-ów. Dla użytkowników budujących własne narzędzia na [[Claude Code]] otwiera to nowy poziom integracji z istniejącymi pipeline'ami CI/CD i systemami alertowymi.

## Frameworki i metody

- **Scheduled routines** — uruchamianie prompta według harmonogramu (co godzinę, nocnie, tygodniowo); np. nocny triage błędów z [[Linear]] i otwarcie draft PR
- **API routines** — każda rutyna dostaje własny endpoint i token; można ją wyzwolić HTTP requestem z dowolnego systemu (alerty, hooki deploymentu, wewnętrzne narzędzia)
- **Webhook routines (GitHub)** — subskrypcja na zdarzenia repozytorium (np. otwarcie PR); [[Claude Code]] tworzy nową sesję per zdarzenie i przetwarza follow-upy (komentarze, błędy CI)

## Kluczowe dane

- Pro: max 5 rutyn dziennie
- Max: max 15 rutyn dziennie
- Team/Enterprise: max 25 rutyn dziennie
- Dostępne dla planów Pro, Max, Team, Enterprise z włączonym [[Claude Code]] on the web

## Wnioski

- Routines eliminują potrzebę samodzielnego zarządzania cronami i infrastrukturą, co obniża próg wejścia w automatyzację powtarzalnych zadań developerskich opartych na [[Claude Code]]
- Integracja z [[GitHub]] przez webhooki umożliwia budowanie całkowicie zautomatyzowanych przepływów code review i portowania zmian między repozytoriami
- Dla osób budujących [[pluginy Claude Code]] i własne narzędzia AI, routines to naturalny kolejny krok — możliwość uruchamiania złożonych automatyzacji bez dodatkowego stacku infrastrukturalnego

## Zastosowanie

Routines mogą uprościć utrzymanie własnych pluginów Claude Code — np. automatyczne testowanie, triage issue'ów czy synchronizacja dokumentacji po merge'ach. Dla pracy konsultingowej z NGO warto mieć pod ręką znajomość tego mechanizmu jako wzorzec do rekomendowania klientom budującym powtarzalne procesy AI. Warto przetestować API routines jako backend dla automatyzacji opartych na [[Make.com]] lub bezpośrednich integracji z systemami klientów.
