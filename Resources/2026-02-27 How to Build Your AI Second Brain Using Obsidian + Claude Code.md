---
categories: Clippings
authors: "[[Noah Vincent]]"
url: https://x.com/noahvnct/status/2027435582461259997
source: "[[Archives/2026-02-27 How to Build Your AI Second Brain Using Obsidian + Claude Code|2026-02-27 How to Build Your AI Second Brain Using Obsidian + Claude Code]]"
published: 2026-02-27
created: 2026-03-07
relevance: wysoka
tags:
  - narzędzia-AI
  - automatyzacja
  - prompt-engineering
---

# How to Build Your AI Second Brain Using Obsidian + Claude Code

Noah Vincent opisuje swój setup łączący [[Obsidian]] z [[Claude Code]] w celu stworzenia "AI second brain" — systemu, w którym AI działa wewnątrz bazy wiedzy użytkownika, a nie na zewnątrz niej. Kluczowa idea: zamiast za każdym razem podawać AI kontekst od zera, instalujesz go w folderze Obsidiana i działa z pełną wiedzą o twoich projektach, stylu i historii pracy od pierwszego promptu w każdej sesji. System narasta — im więcej go używasz, tym lepiej dostosowany jest do twojego sposobu pracy.

## Frameworki i metody

**Architektura AI Second Brain (Obsidian + Claude Code)**
- **CLAUDE.md** — plik czytany automatycznie przy każdym starcie sesji; zawiera profil użytkownika, projekty, reguły pisania, preferencje; aktualizowany przez Claude'a w trakcie pracy
- **memory.md** — log sesji; Claude zapisuje tu kluczowe decyzje i postępy po każdej sesji, by zachować ciągłość między rozmowami
- **Skills (komendy /skill)** — przepływy pracy utrwalone jako pliki SOP; każdy workflow budowany z Claude'em można przekształcić w powtarzalną komendę /nazwa-skilla
- **MCP (Model Context Protocol)** — rozszerzenie Claude Code o zewnętrzne narzędzia (np. [[Things3]], Tana, API); Claude czyta dane z zewnętrznych systemów w czasie rzeczywistym

**Workflow tworzenia skilla**
1. Przejdź przez workflow z Claude'em do uzyskania satysfakcjonującego wyniku
2. Poproś Claude'a o napisanie SOP (Standard Operating Procedure) dla procesu
3. Zapisz SOP jako plik skilla
4. Od tej pory wpisujesz /nazwa-skilla → cały przepływ uruchamia się automatycznie

## Wnioski
- Kontekst bije prompt — AI z pełnym dostępem do bazy wiedzy użytkownika produkuje wielokrotnie lepsze wyniki niż AI odpowiadające na jednokrotny, nawet świetnie napisany prompt
- [[Claude Code]] + [[Obsidian]] to najtańszy i najbardziej kontrolowany setup AI dla knowledge workerów — ~20 EUR/miesiąc, lokalne pliki Markdown, pełna własność danych
- System narasta: każda sesja wzmacnia dopasowanie AI do użytkownika — to fundamentalna różnica względem chatbotów resetujących kontekst

## Zastosowanie
Setup można bezpośrednio zastosować do własnej pracy w [[Obsidian]] — zarówno dla osobistego zarządzania wiedzą, jak i przy budowaniu zautomatyzowanych przepływów dla klientów NGO (np. automatyczne opracowywanie materiałów, przygotowanie treści kampanijnych).
