---
categories: Clippings
authors: ["[[WenHao Yu]]"]
url: https://yu-wenhao.com/en/blog/ai-second-brain/
source: "[[Archives/2026-01-14 How I Built an AI Second Brain with Claude Code + Obsidian|2026-01-14 How I Built an AI Second Brain with Claude Code + Obsidian]]"
published: 2026-01-14
created: 2026-04-19
relevance: wysoka
tags:
  - "automatyzacja"
  - "strategia-AI"
  - "narzędzia-AI"
---

# How I Built an AI Second Brain with Claude Code + Obsidian

[[WenHao Yu]] opisuje kompletny system produktywności zbudowany na [[Claude Code]] i [[Obsidian]], w którym AI przejmuje rutynowe wykonanie, a człowiek skupia się wyłącznie na decyzjach. System opiera się na trzech zasadach: programowalnej infrastrukturze (wszystko w Markdown, lokalnie), decyzjach opartych na danych (AI centralizuje i analizuje, człowiek decyduje) oraz automatyzacji egzekucji (jeśli coś powtarzasz trzy razy — zautomatyzuj). Efekt praktyczny: poranny rytuał zredukowany z godziny "przygotowania do pracy" do pięciu minut decyzji, email z 40 do 10 minut, notatki przestają ginąć w archiwum. Autor trafnie diagnozuje: problemem nie jest siła woli — problemem jest niemożność zobaczenia siebie.

## Frameworki i metody

- **Trzy zasady projektowania systemu PKM z AI**:
  1. Programowalna infrastruktura — wszystkie pliki w Markdown, lokalnie, dostępne bezpośrednio przez API; [[Claude Code]] czyta i pisze pliki natywnie
  2. Decyzje oparte na danych — AI centralizuje dane ze wszystkich źródeł i analizuje; człowiek decyduje, nie szuka
  3. Automatyzacja egzekucji — coś powtarzane trzy razy lub więcej trafia do automatyzacji; czas przeznaczony na decyzje, nie na wykonanie

- **System codziennego Briefu (poranny rytuał "Let's go")**:
  - AI automatycznie przegląda poprzedni dzień, postęp celów tygodniowych, stan projektów, kalendarz, maile i trendy
  - Zadania kodowane kolorami: 🟢 AI sugeruje akcję do zatwierdzenia, 🟡 AI przygotowało opcje do wyboru, 🔴 człowiek musi zająć się sam, ⚪ bez akcji dziś
  - Cały proces: 5 minut zamiast godziny

- **Workflow spotkań (przed / w trakcie / po)**:
  - Przed: `/meeting prep` — AI generuje Playbook z kontekstem z kalendarza, maili i historii projektu
  - W trakcie: live transkrypcja + AI tactical advisor sugeruje pytania i kroki w czasie rzeczywistym
  - Po: AI generuje notatki ze spotkania (podsumowanie, decyzje, action items), zapisuje do systemu automatycznie

- **12 Week Year jako szkielet zarządzania celami** — rok traktowany jako 4 cykle 12-tygodniowe; śledzenie Leadów (działania) zamiast Lagów (wyniki); cotygodniowe WAM (Weekly Accountability Meeting) z AI analizującym przyczyny odchyleń

- **Struktura vaultu FLUX**:
  - `daily/` — planowanie i przeglądy dnia
  - `goals/` — śledzenie celów (12 Week Year)
  - `efforts/` — projekty i obszary
  - `Atlas/` — baza wiedzy (notatki + second brain)
  - `inbox/` — szybkie przechwytywanie pomysłów
  - `content/` — tworzenie treści
  - `Calendar/` — dziennik i refleksja

## Wnioski

- Kluczem nie jest struktura narzędzi, lecz automatyczny przepływ danych między nimi — [[Claude Code]] jako warstwa integrująca eliminuje ręczne kopiowanie między aplikacjami
- Śledzenie Leadów (działań) zamiast Lagów (wyników) zmienia reakcję z lęku na korektę strategiczną — to samo dotyczy prowadzenia organizacji NGO
- System buduje się iteracyjnie od jednego bólu — nie próbując od razu zautomatyzować wszystkiego; po 3 miesiącach iteracji autor ma system, który "działa, a on decyduje"

## Zastosowanie

Artykuł jest bezpośrednim punktem odniesienia dla projektu Piotra — budowania Second Brain w strukturze [[EPARAX]] z połączeniem [[Obsidian]] i [[Claude Code|Claude Cowork]]. Struktura vaultu FLUX i mechanizm codziennego Briefu to gotowe wzorce do adaptacji lub świadomego odrzucenia przy projektowaniu własnego systemu. Zasada "AI czyta i pisze pliki natywnie" jako warunek programowalnej infrastruktury potwierdza wybór Obsidian + lokalny vault jako właściwą bazę dla całego systemu.
