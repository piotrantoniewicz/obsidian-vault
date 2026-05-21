---
categories:
  - "Emails"
published: 2026-05-14
created: 2026-05-21
labels:
  - "Ryan Carr"
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "context-engineering"
---

# Build a home for your AI projects 🗂️

Ryan Carr (Moodboard) proponuje podejście do pracy z AI, które uniezależnia workflow od konkretnego modelu: zamiast optymalizować pod narzędzie, należy zbudować dobrze zorganizowany folder projektu z plikiem indeksu jako "mapą" dla każdego agenta. Centralnym elementem jest plik `CLAUDE.md`, `AGENTS.md` lub `PROJECT_INDEX.md` umieszczony w głównym katalogu, który tłumaczy każdemu modelowi czym jest projekt, gdzie leżą zasoby, jakie skille istnieją i gdzie zapisywać wyniki. Dzięki temu zmiana modelu (która następuje co kilka tygodni) nie wymaga migracji — wystarczy wskazać nowy agent na ten sam folder. To podejście sprawia, że kontekst i dokumentacja projektu stają się trwałym aktywem, niezależnym od aktualnie używanego narzędzia AI.

## Frameworki i metody

- **Project Index Wizard** — trzyetapowy prompt do tworzenia pliku indeksu projektu:
  1. **Inspekcja** — agent analizuje, co już znajduje się w folderze
  2. **Wywiad** — 5–6 dynamicznych pytań o sposób użycia projektu i cele
  3. **Zapis indeksu** — tworzy lub aktualizuje `AGENTS.md` (dla Codex), `CLAUDE.md` (dla [[Claude Code]]) lub `PROJECT_INDEX.md` (format neutralny)

- **Plik indeksu projektu** — dokument MD w głównym katalogu folderu, który przekazuje agentowi:
  - co projekt produkuje i czym jest
  - gdzie leżą ważne zasoby i referencje
  - które pliki są zaufanymi wzorcami
  - gdzie zapisywać nowe wyniki (np. `Outputs/Drafts/`)
  - jakie skille istnieją i kiedy ich używać
  - czego nie ruszać (np. robocze szkice nie powinny służyć jako wzorce głosu)

- **Project Setup Wizard** — poprzedni krok: przeprowadza wywiad, tworzy strukturę folderów i pisze instrukcje projektu; Index Wizard przejmuje tam, gdzie Setup Wizard kończy

## Wnioski

- Budowanie dobrze udokumentowanego folderu projektu z plikiem indeksu to inwestycja, która mnoży wartość każdej kolejnej sesji AI — niezależnie od tego, który model jest aktualnie najlepszy.
- Plik `CLAUDE.md` lub jego odpowiednik działa jak "mapa przy wejściu": nowy agent dostaje kontekst natychmiast bez konieczności tłumaczenia mu projektu od zera; to szczególnie ważne przy budowie [[Second Brain]] w [[Obsidian]] połączonego z [[Claude Code]].
- Indeks spełnia też funkcję diagnostyczną — jeśli model po przeczytaniu pliku nie wie, co robić, to sygnał, że projekt nie jest wystarczająco czytelny i wymaga porządku.

## Cytat

> Zbuduj bazę danych swojej pracy i mapę do niej, a każdy nowy agent stanie się mądrzejszy w momencie, gdy do niej wejdzie.

## Zastosowanie

Piotr buduje Second Brain w Obsidian i własne pluginy do [[Claude Code]] — struktura folderów opisana w newsletterze bezpośrednio przekłada się na jego sposób pracy. Warto zastosować Project Index Wizard do każdego aktywnego projektu (dobryai.pl, plugin outreach, workflow NGO), tworząc `CLAUDE.md` w każdym folderze projektowym. Dzięki temu kolejne modele i narzędzia będą mogły od razu pracować z pełnym kontekstem bez dodatkowego onboardingu.
