---
categories: Clippings
authors: ["[[Wojtek Woźniak]]"]
url: https://www.youtube.com/watch?v=EzYcoPPlLxE
source: "[[Archives/2026-04-01 Obsidian + Claude Code - podstawy|2026-04-01 Obsidian + Claude Code - podstawy]]"
published: 2026-04-01
created: 2026-04-15
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "context-engineering"
  - "automatyzacja"
---

# Obsidian + Claude Code - podstawy

Wojtek Woźniak prezentuje warsztat budowania systemu Second Brain opartego na [[Obsidian]] i [[Claude Code]], gdzie notatki są plikami Markdown na dysku lokalnym, dostępnymi dla AI poprzez terminal. Kluczowa idea to utrzymywanie „żywego kontekstu" — zestawu plików opisujących projekty, zasady pracy i aktywne zadania — który AI ([[Claude Code]], [[Gemini CLI]]) odczytuje przy każdej sesji, eliminując problem „zaczynania od zera" w nowym czacie. System umożliwia delegowanie rutynowych czynności (porządkowanie inboxu, pisanie postów LinkedIn, journaling) bezpośrednio z terminala wbudowanego w [[Obsidian]], a całość działa niezależnie od konkretnego dostawcy AI. Wideo obejmuje instalację wtyczek (Terminal, Calendar), konfigurację claude.md, budowanie struktury folderów oraz praktyczne przykłady użycia skillów do journalingu i tworzenia treści.

## Frameworki i metody

- **Struktura vaultu z prefiksami numerycznymi** — foldery `00 Inbox`, `1.0 Journal`, `2.0 Projects`, `99 Systems` z cyframi na początku wymuszają pożądaną kolejność sortowania w [[Obsidian]]
- **Cowork Log** — plik systemowy aktualizowany po każdej sesji z AI; raz w tygodniu służy do analizy, co zautomatyzować lub ulepszyć w systemie pracy
- **Cykl pracy ze skillami** — [[Claude Code]] uruchamia predefiniowane skille (journal session, LinkedIn post, poranny przegląd) z ukośnika w terminalu; skill prowadzi przez kolejne etapy procesu krok po kroku
- **Czyszczenie kontekstu (`clear`)** — po zakończeniu zadania komenda resetuje sesję AI, dzięki czemu nowe zadania nie są obciążone historią poprzednich rozmów

## Wnioski

- [[Claude Code]] z dostępem do lokalnego vaultu [[Obsidian]] rozwiązuje problem utraty kontekstu między sesjami — AI zawsze „wie", nad czym pracujesz, bo czyta pliki, a nie pamięć czatu
- Prompty nie są skuteczne same w sobie — to właściwy, aktualny kontekst (pliki z projektami, zasadami, zadaniami) decyduje o jakości odpowiedzi AI; ta zasada bezpośrednio wspiera podejście [[context-engineering]]
- System jest niezależny od dostawcy AI — działa z [[Claude Code]], [[Gemini CLI]] czy [[Cursor]], bo dostęp do plików jest przez terminal, a nie przez API konkretnej platformy

## Cytat

> Kontekst jest dobry, gdy jest właściwy — jak mamy właściwy kontekst, to często nie muszę pisać co tam się ma wydarzyć, tylko daję pełną specyfikację i po prostu mówię: zbuduj to.

## Zastosowanie

Piotr aktywnie buduje Second Brain w strukturze EPARAX połączonej z [[Claude Code]] — ten warsztat pokazuje konkretne wzorce (struktura folderów, cowork log, skille, cykl clear → nowa sesja), które można bezpośrednio zaadaptować. Praktyka tworzenia skillów dla powtarzalnych zadań (fundraisingowych briefów, newsletterów, raportów dla NGO) to kolejny naturalny krok. Wideo jest też wartościowym materiałem referencyjnym przy projektowaniu szkoleń z AI dla organizacji, jako przykład realnego, codziennego wdrożenia Second Brain.
