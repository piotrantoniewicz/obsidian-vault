---
categories:
  - Project
status: Aktywny
created: 2026-07-08
due: 2026-08-15
area: "[[Marka osobista LinkedIn]]"
tags:
  - content-marketing
  - LLM
  - organizacje-społeczne
---

# Cykl artykułów ngo.pl — GEO i widoczność w sektorze

Uruchomić i utrwalić regularny cykl artykułów na publicystyka.ngo.pl (rytm: jeden artykuł co 2 tygodnie) jako górny lejek marki osobistej i fundament widoczności w LLM-ach (GEO). Cel potrójny: poruszać aktualne sprawy sektora, pozycjonować Piotra jako osobę rozwiązującą realne pain pointy organizacji społecznych, budować treść, którą modele językowe mogą cytować i przypisywać autorowi. Sukces = system działa niezawodnie (kolejne cykle bez zacinania się) i **retrospektywa po 2–3 cyklach** przeprowadzona (poprawki komendy/skilla na bazie tego, co redakcja przyjęła i jak reagowali czytelnicy).

**Stan wyjściowy (2026-07-08):** workflow zrealizowany jako plugin Cowork `artykuly-ngo` (5 komend: `/radar` → `/brief` → `/pisz` → `/redakcja` → `/dystrybucja`); artykuł nr 1 opublikowany 2026-06-23; trwa cykl nr 2 (radar gotowy, brief i szkic „luka governance AI" powstały, czeka wybór/domknięcie tematu przez Piotra).

## Architektura (skrót)
- **Oś = 5 skilli projektowych** wywoływanych ręcznie (bo między etapami są decyzje człowieka: wybór tematu, akceptacja briefu, redakcja finalna). Subagenci użyci *wewnątrz* skilli — do hałaśliwego researchu (`/radar`, `/brief`) i do świeżego oka w `/redakcja`.
- **Trzy filary każdego artykułu:** Wiedza (vault Obsidian, ~4200 notatek, `qmd`) × Aktualność (radar: wiadomosci/publicystyka.ngo.pl, raporty, zmiany prawne) × Głos (`glos.md` — cichy ekspert, persona „Marta", analiza struktury Kariny Janus). Temat wchodzi do briefu tylko, gdy łapie wszystkie trzy filary.
- **GEO wbudowane** w `/pisz` i `/redakcja`: stała formuła bio, nagłówki-pytania, zdania definicyjne, liczby ze źródłem i rokiem, nazwane frameworki, sekcja FAQ, linki do własnych wcześniejszych tekstów.

## Kolejne kroki
- [ ] Domknąć cykl nr 1: `/artykuly-ngo:dystrybucja <link>` — post LinkedIn + ingest artykułu do vaultu (`Resources/` + aktualizacja `Galaxy/`)
- [ ] Cykl nr 2: wybór/akceptacja tematu (brief „luka governance AI" gotowy) → `/pisz` → `/redakcja` → publikacja
- [ ] Utrzymywać rytm dwutygodniowy (data następnego cyklu pilnowana w `PUBLIKACJE.md`)
- [ ] Po 2–3 cyklach: **retrospektywa** — poprawić komendy i skill pluginu (edycja plików + ponowny zip + reinstalacja) na bazie reakcji redakcji i czytelników
- [ ] GEO — pierwszy pomiar ~2026-09: zapytać kilka modeli o tematy artykułów, notować w `PUBLIKACJE.md`, czy zaczynają wskazywać nazwisko/teksty

## Powiązane zasoby
- `~/Artykuly/` — folder roboczy: `WORKFLOW.md` (pełny opis systemu), `PUBLIKACJE.md` (log publikacji + data następnego cyklu), `glos.md`, analiza struktury Kariny Janus, `radar/`, `briefy/`, `artykuly/`
- `~/Documents/Plugins/artykuly-ngo/` — plugin Cowork (5 komend, wspólna wiedza: głos, struktura, GEO, reguły)
- Artykuł nr 1: [Połowa Twojego zespołu już używa AI. Czas to zauważyć](https://publicystyka.ngo.pl/polowa-twojego-zespolu-juz-uzywa-ai-czas-to-zauwazyc) (2026-06-23)
- [[Marka osobista LinkedIn]] — obszar nadrzędny (artykuły = górny lejek: CTA → LinkedIn i konsultacje)
- [[content-marketing]] · [[digital-campaigning]] — domeny tematyczne

## Log decyzji
- 2026-07-08 — utworzenie notatki-huba projektu w vaultcie (źródło prawdy treści i systemu pozostaje w `~/Artykuly`). Routing: praktyka powracająca, ale z metą projektową (uruchomienie systemu + retrospektywa po 2–3 cyklach), więc Project pod obszarem [[Marka osobista LinkedIn]], nie osobny Area — obszar już wskazuje artykuły jako swój górny lejek.
