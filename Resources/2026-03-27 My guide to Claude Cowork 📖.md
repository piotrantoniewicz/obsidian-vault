---
categories: Clippings
authors: ["[[Ryan Carr]]"]
url: https://moodboard.beehiiv.com/p/my-guide-to-claude-cowork
source: "[[Archives/2026-03-27 My guide to Claude Cowork 📖|2026-03-27 My guide to Claude Cowork 📖]]"
published: 2026-03-27
created: 2026-05-18
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "strategia-AI"
---

# My guide to Claude Cowork 📖

[[Ryan Carr]] z newslettera Moodboard opisuje swój system pracy z [[Claude Cowork]] po tygodniu intensywnych eksperymentów — od struktury folderów projektów, przez skill files, po scheduled tasks zintegrowane z [[Notion]] i Slack. Artykuł jest praktycznym przewodnikiem "jak zacząć", nie teorią: autor dzieli się konkretną architekturą folderów i przykładami automatyzacji, które sam wdrożył. Kluczowa teza: Cowork zaczyna przypominać "second brain" — ale tylko jeśli zainwestuje się w organizację plików na starcie.

## Frameworki i metody

- **Trzy sposoby tworzenia projektu w Cowork**: od zera (nowy folder + instrukcje), z istniejącego folderu na komputerze, import z Claude Chat jednym kliknięciem (przenosi instrukcje, pliki wiedzy i skompresowany kontekst).
- **Struktura projektu — trzy kluczowe foldery**:
  - `Skills/` — pliki Markdown z instrukcjami dla każdego powtarzalnego zadania; [[Claude Cowork]] może je sam aktualizować na podstawie feedbacku użytkownika
  - `Outputs/` — finalne outputy Claude, zorganizowane według typu
  - `Reference/` — wiedza o projekcie: brand voice, dane kampanii, analizy, materiały tła
- **Skompresowany feedback loop przez skill files** — po każdej iteracji użytkownik daje feedback, Claude aktualizuje plik skill. Następne uruchomienie zadania ma feedback "wbudowany". Z każdą rundą output jest lepszy bez wzrostu nakładu pracy od użytkownika.
- **Scheduled tasks z integracjami** — przykłady autora: auto-draft postu LinkedIn z każdego wydania newslettera (Notion → [[Claude Cowork]] → draft), codzienna kuracja branżowych newsów → Slack dla zespołu. Cowork łączy się z [[Notion]], [[Google Drive]], Slack przez MCPs lub oficjalne konektory.

## Wnioski

- Organizacja plików na komputerze to nie estetyka — Claude czyta co ma w folderze projektu, więc chaos w plikach bezpośrednio przekłada się na jakość outputów.
- Skill files to mechanizm ciągłego doskonalenia: [[Claude Cowork]] może je sam edytować na podstawie feedbacku, co tworzy pętlę uczenia się bez dodatkowego nakładu pracy od użytkownika.
- [[Claude Cowork]] staje się "second brain" dopiero gdy project instructions + skill files + reference folder działają razem — samo otwarcie aplikacji nie wystarczy.

## Zastosowanie

Bezpośrednio przydatne dla Piotra budującego własny second brain w Obsidian + [[Claude Cowork]]. Architektura Skills/Outputs/Reference może być szablonem dla projektów klientów NGO — osobny projekt Cowork per klient, skill files dla raportów, kampanii i outreach. Scheduled tasks z [[Notion]] mogą zautomatyzować content pipeline dla dobryai.pl lub kampanii email.
