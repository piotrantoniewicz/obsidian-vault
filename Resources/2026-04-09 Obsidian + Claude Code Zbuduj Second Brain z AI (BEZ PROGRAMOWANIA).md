---
categories: Clippings
authors: ["[[Robert Szewczyk]]"]
url: https://www.youtube.com/watch?v=7i85dqtkptU
source: "[[Archives/2026-04-09 Obsidian + Claude Code Zbuduj Second Brain z AI (BEZ PROGRAMOWANIA)|2026-04-09 Obsidian + Claude Code Zbuduj Second Brain z AI (BEZ PROGRAMOWANIA)]]"
published: 2026-04-09
created: 2026-04-24
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "strategia-AI"
---

# Obsidian + Claude Code: Zbuduj Second Brain z AI (BEZ PROGRAMOWANIA)

Materiał pokazuje konkretny system zarządzania wiedzą oparty na [[Obsidian]] i [[Claude Code]], zainspirowany podejściem [[Andrej Karpathy|Andreja Karpathy'ego]] — lokalna baza wiedzy w Markdown, zero chmury, LLM jako backend do przetwarzania. Autor zbudował system nie tylko odpowiadający na pytania, ale aktywnie krystalizujący wiedzę: klasyfikuje notatki z inbox, wykrywa niewidoczne połączenia między notatkami i generuje raporty topologiczne grafu. Kluczowe rozróżnienie względem innych podobnych setupów: to nie "Obsidian jako chatbot", lecz Obsidian jako baza wiedzy z agentowymi komendami, które robią robotę automatycznie. Materiał jest szczególnie wartościowy, bo całość jest osiągalna bez umiejętności programowania — Claude Code generuje potrzebne skrypty na podstawie opisu.

## Frameworki i metody

- **Setup minimalny** — dwa pluginy do zainstalowania w Obsidian:
  1. *Terminal* (autor: polyipseiti) — umożliwia uruchomienie Claude Code bezpośrednio w Obsidian
  2. *Show Hidden Files* (ten sam autor, instalacja przez GitHub) — pokazuje ukryte foldery (.obsidian, .claude) w panelu plików
  - Następnie: stworzenie `CLAUDE.md` z instrukcją systemową (persona, język, struktura Volta, reguły formatowania, wikilinkowania, tagowania)
  - Opcjonalnie: instalacja Obsidian Skills dla Claude Code (repozytorium z 21 000 gwiazdkami)

- **Komenda `/brain-sweep`** — cotygodniowy rytuał krystalizacji wiedzy:
  1. Skanuje folder inbox (autor: IdeaVerse), klasyfikuje każdą notatkę jako: `watch` (film), `read` (artykuł), `check` (sprawdzić), `idea-content` (pomysł na treść), `idea-project` (projekt), `insight` (refleksja), `note` (dłuższy tekst), `task` (konkretna akcja)
  2. Interaktywnie pyta o decyzję dla każdej notatki: przetworzyć / zachować / pominąć
  3. Po potwierdzeniu: przenosi notatki z inbox do archiwum, aktualizuje `home.md` (dashboard) i state file
  4. Nic nie ginie — wszystko trafia do archiwum z pełną historią

- **Pipeline głosowy** — automatyczne zapisywanie notatek głosowych do Obsidian:
  - [[WhisperFlow]] (Mac + iPhone) transkrybuje mowę na tekst i zapisuje do wyznaczonego folderu
  - Skrypt Python (wygenerowany przez Claude Code) monitoruje bazę WhisperFlow (SQLite), co 15 minut lub przy zmianie pliku eksportuje nowe notatki do inbox Volta
  - Efekt: mówisz do telefonu → tekst automatycznie pojawia się w Obsidian inbox

- **Komenda `/emerge`** — odkrywanie ukrytych połączeń:
  - Skanuje cały Volt, analizuje gęstość linków, liczy backlinki
  - Wykrywa klastry tematyczne i sugeruje połączenia między notatkami, które nie są jeszcze zlinkowane
  - Generuje raport topologiczny: wzorce, napięcia, rekomendacje

- **Komenda `/ask`** — zapytanie do całego Volta:
  - Odpowiada na pytanie z cytatami ze źródeł
  - Pokazuje w ilu plikach pojawia się dany temat i jak ewoluował w czasie

## Kluczowe dane

- System działa na Claude Opus 4.6 z milionowym kontekstem (autor korzysta z tej wersji)
- Andrej Karpathy: ~400 000 słów Markdown jako lokalna baza wiedzy — bez RAG, bez chmury
- Repozytorium Obsidian Skills dla Claude Code: ponad 21 000 gwiazdek na GitHubie

## Wnioski

- `CLAUDE.md` w Obsidian to odpowiednik system prompt dla całej bazy wiedzy — to tam definiujesz jak Claude ma rozumieć strukturę Volta, wikilinki, tagi i twój profil; bez tego Claude Code "widzi" pliki, ale nie "rozumie" systemu
- Komenda `/brain-sweep` rozwiązuje dokładnie ten sam problem, który Piotr rozwiązuje swoim pluginem `clippings-to-notes` — warto porównać oba podejścia i zobaczyć, co można zaczerpnąć
- Wartość systemu nie tkwi w pojedynczych komendach, ale w tym, że Claude ma dostęp do całego grafu wiedzy naraz — może widzieć połączenia, których właściciel Volta sam by nie zauważył

## Zastosowanie

Materiał jest bezpośrednim odniesieniem dla projektu Second Brain w strukturze EPARAX — komendy `/emerge` i `/ask` są gotowymi kandydatami do implementacji jako własne komendy lub skille. Pipeline głosowy z [[WhisperFlow]] może zastąpić lub uzupełnić ręczne clipowanie artykułów: nagrywasz refleksję po przeczytaniu, skrypt wrzuca ją do inbox, skill przetwarza. Warto sprawdzić repozytorium Obsidian Skills dla Claude Code — może zawierać gotowe skille kompatybilne z obecnym setupem.
