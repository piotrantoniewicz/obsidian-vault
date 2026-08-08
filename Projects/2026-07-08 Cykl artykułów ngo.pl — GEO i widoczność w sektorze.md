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

**Stan (2026-08-08):** workflow zrealizowany jako plugin Cowork `artykuly-ngo` (5 komend: `/radar` → `/brief` → `/pisz` → `/redakcja` → `/dystrybucja`). Trzy artykuły opublikowane i w pełni domknięte (ingest do `Resources/` + post LinkedIn): nr 1 „Połowa Twojego zespołu już używa AI" (23.06, LinkedIn 26.06), nr 2 „Luka governance w AI" (09.07, LinkedIn 13.07), nr 3 „AI Act przesunięty? Nie tam, gdzie myślisz" (23.07, LinkedIn 24.07). Brief artykułu nr 4 („kodeks etycznego używania AI") gotowy, czeka na sekcję „Doświadczenie Piotra" — termin cyklu (06.08) już minął, patrz `PUBLIKACJE.md`.

## Architektura (skrót)
- **Oś = 5 skilli projektowych** wywoływanych ręcznie (bo między etapami są decyzje człowieka: wybór tematu, akceptacja briefu, redakcja finalna). Subagenci użyci *wewnątrz* skilli — do hałaśliwego researchu (`/radar`, `/brief`) i do świeżego oka w `/redakcja`.
- **Trzy filary każdego artykułu:** Wiedza (vault Obsidian, ~4200 notatek, `qmd`) × Aktualność (radar: wiadomosci/publicystyka.ngo.pl, raporty, zmiany prawne) × Głos (`glos.md` — cichy ekspert, persona „Marta", analiza struktury Kariny Janus). Temat wchodzi do briefu tylko, gdy łapie wszystkie trzy filary.
- **GEO wbudowane** w `/pisz` i `/redakcja`: stała formuła bio, nagłówki-pytania, zdania definicyjne, liczby ze źródłem i rokiem, nazwane frameworki, sekcja FAQ, linki do własnych wcześniejszych tekstów.

## Kolejne kroki
- [x] Cykl nr 1 — artykuł 23.06, post LinkedIn 26.06 ([Notion](https://app.notion.com/p/347e4dd29ba88053a29bc6c8c0e11439?v=347e4dd29ba880e29c00000ce4c9f096)), ingest do vaultu domknięty
- [x] Cykl nr 2 — artykuł „Luka governance w AI" 09.07, post LinkedIn „Luka governance AI — 92% vs 7%" 13.07, ingest do vaultu domknięty
- [x] Cykl nr 3 — artykuł „AI Act przesunięty? Nie tam, gdzie myślisz" 23.07, post LinkedIn „AI Act oznaczanie treści 2 sierpnia" 24.07, ingest do vaultu domknięty
- [ ] Cykl nr 4 — termin 06.08 minął; brief gotowy (kodeks etycznego używania AI), czeka na sekcję „Doświadczenie Piotra" przed `/artykuly-ngo:pisz`
- [ ] Utrzymywać rytm dwutygodniowy (data następnego cyklu pilnowana w `PUBLIKACJE.md`)
- [ ] Po 2–3 cyklach: **retrospektywa** — poprawić komendy i skill pluginu (edycja plików + ponowny zip + reinstalacja) na bazie reakcji redakcji i czytelników
- [ ] GEO — pierwszy pomiar ~2026-09: zapytać kilka modeli o tematy artykułów, notować w `PUBLIKACJE.md`, czy zaczynają wskazywać nazwisko/teksty

## Powiązane zasoby
- `~/Projekty/Artykuly/` — folder roboczy: `WORKFLOW.md` (pełny opis systemu), `PUBLIKACJE.md` (log publikacji + data następnego cyklu), `glos.md`, analiza struktury Kariny Janus, `radar/`, `briefy/`, `artykuly/`
- `~/Documents/Plugins/artykuly-ngo/` — plugin Cowork (5 komend, wspólna wiedza: głos, struktura, GEO, reguły)
- Artykuł nr 1: [Połowa Twojego zespołu już używa AI. Czas to zauważyć](https://publicystyka.ngo.pl/polowa-twojego-zespolu-juz-uzywa-ai-czas-to-zauwazyc) (2026-06-23) · post LinkedIn (2026-06-26 13:20)
- Artykuł nr 2: [Luka governance w AI: dlaczego 92% organizacji korzysta z AI, a tylko 7% coś dzięki temu zyskuje](https://publicystyka.ngo.pl/luka-governance-w-ai-dlaczego-92-organizacji-korzysta-z-ai-a-tylko-7-cos-dzieki-temu-zyskuje) (2026-07-09) · post LinkedIn „Luka governance AI — 92% vs 7%" (2026-07-13)
- Artykuł nr 3: [AI Act przesunięty? Nie tam, gdzie myślisz](https://publicystyka.ngo.pl/ai-act-przesuniety-nie-tam-gdzie-myslisz-543722) (2026-07-23) · post LinkedIn „AI Act oznaczanie treści 2 sierpnia" (2026-07-24)
- Wszystkie posty LinkedIn: [baza Posty w Notion](https://app.notion.com/p/347e4dd29ba88053a29bc6c8c0e11439?v=347e4dd29ba880e29c00000ce4c9f096)
- [[Marka osobista LinkedIn]] — obszar nadrzędny (artykuły = górny lejek: CTA → LinkedIn i konsultacje)
- [[content-marketing]] · [[digital-campaigning]] — domeny tematyczne

## Log decyzji
- 2026-07-08 — utworzenie notatki-huba projektu w vaultcie (źródło prawdy treści i systemu pozostaje w `~/Projekty/Artykuly`). Routing: praktyka powracająca, ale z metą projektową (uruchomienie systemu + retrospektywa po 2–3 cyklach), więc Project pod obszarem [[Marka osobista LinkedIn]], nie osobny Area — obszar już wskazuje artykuły jako swój górny lejek.
- 2026-07-11 — Obsidian Web Clipper przestał działać na stronie ngo.pl; treść artykułów nr 1 i nr 2 wstawiona ręcznie do `Inbox/` (Tavily extract + format zgodny z konwencją Web Clippera), czeka na standardowe przetworzenie `/clippings-to-notes:clip`. Potwierdzone: post LinkedIn dla artykułu nr 1 już opublikowany 2026-06-26 13:20 (Notion), więc z checklisty domknięcia cyklu nr 1 zostaje tylko ingest do vaultu.
- 2026-07-12 — folder roboczy projektu przeniesiony do `~/Projekty/Artykuly` (reorganizacja: wszystkie projekty w `~/Projekty`); ścieżki w notatce zaktualizowane
- 2026-08-08 — odświeżenie stanu: notatka i `PUBLIKACJE.md` nie odzwierciedlały artykułu nr 3 (opublikowany 23.07, pominięty w logu) ani zrealizowanych dystrybucji LinkedIn dla cykli 2 i 3; poprawiono oba dokumenty. Cykl nr 4 (termin 06.08) jest przeterminowany — brief gotowy, czeka na uzupełnienie przed pisaniem.
