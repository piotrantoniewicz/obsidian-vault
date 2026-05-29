---
categories: Clippings
authors: ["[[Zevi Arnovitz]]"]
url: "https://www.youtube.com/watch?v=1em64iUFt3U"
source: "[[Archives/2026-01-18 How a Meta PM ships products without ever writing code  Zevi Arnovitz|2026-01-18 How a Meta PM ships products without ever writing code  Zevi Arnovitz]]"
published: 2026-01-18
created: 2026-05-12
relevance: średnia
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "produkty-cyfrowe"
---

# How a Meta PM ships products without ever writing code — Zevi Arnovitz

[[Zevi Arnovitz]], PM w [[Meta]] bez żadnego tła technicznego, pokazuje jak w ciągu roku nauczył się samodzielnie budować produkty cyfrowe używając [[Cursor]], [[Claude Code]] i systemu własnych /komend. Centralny argument: kod to tylko słowa — każda inteligentna osoba może nauczyć się budować produkty cyfrowe z pomocą AI, jeśli stopniowo oswaja narzędzia i buduje własny workflow. Odcinek jest pokazem konkretnego systemu pracy, który można skopiować.

## Frameworki i metody

- **Workflow 6-fazowy** — Arnovitz stworzył sekwencję /komend w [[Claude Code]] uruchamianych kolejno: (1) `/create-issue` — szybkie przechwycenie pomysłu/buga do [[Linear]] mid-development, (2) `/explore` — eksploracja problemu z pytaniami doprecyzowującymi, bez pisania kodu, (3) `/create-plan` — generowanie pliku markdown z planem implementacji, (4) `/execute-plan` — wykonanie planu, (5) `/review` — Claude Code recenzuje własny kod, (6) `/peer-review` — różne modele wzajemnie recenzują kod (np. [[Codex]] + [[Cursor]]), (7) `/update-docs` — aktualizacja dokumentacji po zmianach.

- **"CTO jako projekt AI"** — tworzenie dedykowanego projektu w [[ChatGPT]]/[[Claude]] z promptem systemowym definiującym rolę technicznego współzałożyciela. Projekt utrzymuje kontekst przez wiele sesji i wymusza niebycie "people pleaserem" — AI ma kwestionować decyzje, nie potakiwać.

- **Ścieżka graduacji narzędzi** — rekomendowana kolejność nauki: projekt ChatGPT → Bolt/Lovable → [[Cursor]] w light mode → [[Claude Code]] w terminalu. Każde narzędzie oswaja z kodem przed przejściem do bardziej zaawansowanego.

## Wnioski

- Osoby nietech. mogą budować realne produkty z AI, ale wymagają własnego systemu /komend i planowania — spontaniczne "wibowanie" działa tylko na prototypach.
- Kod review przez wiele modeli równocześnie (np. [[Claude Code]] + [[Codex]]) zmniejsza ryzyko niewychwycenia błędów przez jednego asystenta.
- Planowanie przed kodowaniem jest kluczowe — agenci chętnie skaczą do pisania kodu bez planowania, co przy złożonych projektach generuje trudne do debugowania błędy.

## Cytat

> Jeśli ludzie wyjdą z tego odcinka myśląc "ale z ciebie gość", poniosłem porażkę. Jeśli otworzą komputer i zaczną budować — udało mi się.

## Zastosowanie

Workflow /komend w [[Claude Code]] jest bezpośrednio użyteczny dla Piotra — szczególnie faza eksploracji przed implementacją i peer review przez dwa modele. Podejście do AI jako "CTO projektu" z anty-sycofantycznym promptem można zaadaptować przy budowaniu pluginów i narzędzi automatyzacyjnych. Ścieżka graduacji narzędzi to dobra analogia dla szkoleń AI dla NGO — od prostych chatbotów do zaawansowanej automatyzacji.
