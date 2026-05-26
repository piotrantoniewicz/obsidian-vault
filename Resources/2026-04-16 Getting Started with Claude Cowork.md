---
categories: Clippings
authors: ["[[Ryan Carr]]"]
url: https://www.youtube.com/watch?v=tNir8inDLpA
source: "[[Archives/2026-04-16 Getting Started with Claude Cowork|2026-04-16 Getting Started with Claude Cowork]]"
published: 2026-04-16
created: 2026-05-08
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
---

# Getting Started with Claude Cowork

[[Ryan Carr]] z agencji Moodboard prezentuje Claude Cowork jako "Claude Code dla pracy nietech" — narzędzie do agenturowej automatyzacji wiedzy bezpośrednio na komputerze użytkownika. Kluczowym wyróżnikiem jest system skilli (pliki Skill.md), które Claude może sam aktualizować na podstawie feedbacku, tworząc pętlę samodoskonalenia. Scheduled tasks pozwalają automatyzować cykliczne zadania bez nadzoru, a integracje z [[Notion]], Google Drive i [[Slack]] umożliwiają przepływ danych między narzędziami. Carr podkreśla, że wartość cowork rośnie z organizacją folderów — im lepiej zorganizowana baza wiedzy, tym skuteczniejsze działanie agenta.

## Frameworki i metody

- **Struktura projektu Cowork** — trzy foldery: `resources/` (kontekst i materiały referencyjne), `outputs/` (artefakty tworzone przez Claude), `skills/` (pliki Skill.md z instrukcjami zadań)
- **Cykl skilla** — tworzysz Skill.md → Claude wykonuje zadanie → dajesz feedback → Claude aktualizuje skill → kolejna iteracja jest lepsza; po 3–4 iteracjach skill działa niemal bez korekty
- **Project instructions jako indeks** — zamiast szczegółowych instrukcji w projekcie, wystarczy opisać strukturę folderów; szczegóły zadań trafiają do Skill.md
- **Scheduled tasks** — uruchamiane komendą `/schedule`; można połączyć z integracjami (np. pobieranie danych z Notion → tworzenie draftu → zapis pliku)

## Wnioski

- Organizacja folderów na komputerze to inwestycja, która procentuje w Claude Cowork — nieuporządkowane foldery spowalniają agenta i zwiększają ryzyko błędów
- Skille to prawdziwe centrum wartości Cowork: jeden dobry skill powtarzalnego zadania eliminuje potrzebę wielokrotnego opisywania tego samego procesu
- Dispatch (dostęp z telefonu) i computer use (przejęcie sterowania komputerem) to rosnące funkcje agenturowe, które zbliżają Cowork do pełnej automatyzacji

## Zastosowanie

Materiał przydatny jako punkt wyjścia do tworzenia własnych skilli dla powtarzalnych zadań w pracy z NGO — warto wzorować się na strukturze folderów resources/outputs/skills. Scheduled tasks mogą automatyzować cotygodniowe raporty, drafty postów czy przeglądy Notion. Film jest też przydatnym zasobem referencyjnym przy wdrażaniu Cowork u klientów z sektora NGO zainteresowanych [[automatyzacja|automatyzacją procesów]].
