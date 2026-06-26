# Vault Piotr — instrukcje dla Claude

## Struktura

```
Piotr/
├── Inbox/        surowe webclipy z Web Clipper — czekają na przetworzenie
├── Archives/     oryginały po przetworzeniu — tylko do odczytu, nigdy nie modyfikuj
├── Resources/    przetworzone notatki (artykuły, newslettery, raporty)
│   └── index.md  katalog wszystkich notatek — czytaj jako pierwsze przy wyszukiwaniu
├── Attachments/  pliki binarne (PDF, obrazy)
├── Galaxy/       encyklopedia pojęć — syntezy łączące wiele notatek z Resources/
├── Projects/     przedsięwzięcia z celem i terminem — notatki-huby (MOC)
├── Areas/        stałe odpowiedzialności i role — notatki-huby (MOC)
├── Templates/    szablony notatek
└── References/   — w budowie
```

## Zasady

- `Archives/` i `Attachments/` są tylko do odczytu — nigdy tam nie pisz ani nie edytuj
- Przy każdym pytaniu o vault zacznij od `Resources/index.md` — to mapa 2000+ notatek
- Nowe notatki trafiają do `Resources/`, nazwa: `YYYY-MM-DD Tytuł artykułu.md`
- **Znak `#` jest zakazany w nazwach plików** — Obsidian traktuje `#` w wikilinku jako separator nagłówka, co łamie nawigację. Zamiast `#41` używaj `nr41`.
- Po dodaniu notatki do `Resources/` dopisz wpis do `Resources/index.md` w formacie:
  `- [[YYYY-MM-DD Tytuł]] — jednozdaniowy opis co zawiera`
- **Terminologia: zawsze pisz „organizacje społeczne" zamiast „NGO" / „organizacje pozarządowe"** — we wszystkich notatkach, syntezach, hubach i przy każdym zapisywaniu treści. **Wyjątki (oryginalne brzmienie zostaje):** (1) surowe pliki trafiające do `Inbox/` (webclipy, oryginały) — podmieniaj dopiero przy przetwarzaniu do `Resources/`, `Galaxy/`, `Projects/`, `Areas/`; (2) oryginalne tytuły maili, clipów, artykułów itp. — jeśli zawierają „NGO" / „organizacje pozarządowe", zostawiaj je bez zmian (nie przepisujemy cudzych tytułów).

## Praca z index.md

Weryfikację kompletności indeksu (brakujące wpisy, duplikaty) wykonuje plugin: **`/index:update vault`**.

Uwagi techniczne przy każdej operacji na index.md:
- Plik ma ~450 KB i 2300+ linii — **nigdy nie czytaj go w całości**, używaj `grep -n` i Edit.
- Wpisy wstawiaj **chronologicznie**: znajdź przez `grep -n "YYYY-MM-DD"` ostatni wpis z tej samej lub najbliższej wcześniejszej daty i użyj Edit z sąsiednim wierszem jako kontekstem.
- Nazwy plików mogą zawierać curly apostrofy (') — `head` z dosłowną nazwą zawiedzie, używaj `find ... -name "YYYY-MM-DD*"`.

## Wyszukiwanie w vaultcie (qmd)

Vault jest zaindeksowany w qmd (kolekcja `obsidian`, `**/*.md`). Zasady:

- **Domyślnie `qmd query "<fraza>" -n 15`** — 15 wyników daje szeroki kontekst do syntezy.
- Wyszukiwania zawężaj do vaultu: `-c obsidian` (druga kolekcja `Ghostwriting` jest osobna).
- `qmd query` = hybryda (expansion + BM25 + wektory + reranking); `qmd search` = szybki BM25 bez LLM.
- Źródła cytuj z `Resources/`, nie z `Archives/` (qmd zwraca oba — duplikaty treści).
- Po sesji pisania w `Galaxy/`: `qmd update` + `qmd embed`, żeby nowe strony były wyszukiwalne następnym razem.

## Format notatki (Resources/)

```yaml
---
categories: Clippings
authors: ["[[Imię Nazwisko]]"]
url: https://...
published: YYYY-MM-DD
created: YYYY-MM-DD
relevance: wysoka | średnia | niska
tags:
  - tag1
  - tag2
source: "[[Archives/YYYY-MM-DD Tytuł|YYYY-MM-DD Tytuł]]"
---
```

Sekcje treści po polsku: synteza (3–5 zdań) → frameworki i metody → kluczowe dane → wnioski → cytat → zastosowanie. Sekcje opcjonalne (dane, cytat) tylko gdy jest konkretna treść.

Wikilinki tylko dla: narzędzi (`[[Obsidian]]`), pojęć technicznych (`[[RAG]]`), osób (`[[Sam Altman]]`), organizacji (`[[OpenAI]]`).

## Relevance — zasady oceny

Relevance oceniaj na podstawie profilu właściciela vaultu: freelance konsultant i trener organizacji społecznych, specjalizacja w AI, automatyzacji, fundraisingu, digital campaigningu i ghostwritingu.

- `wysoka` — bezpośrednio przydatne w aktywnych projektach: organizacje społeczne, fundraising, digital campaigning, AI dla organizacji, automatyzacja
- `średnia` — ogólnie użyteczne, może się przydać: marketing, strategia, komunikacja, narzędzia
- `niska` — marginalne znaczenie dla profilu właściciela

## Tagi — zamknięta lista

Tagi obowiązują we wszystkich notatkach (Resources/ i Galaxy/). Zasady:

- Max 3 tagi na notatkę
- Wyłącznie z tej listy — nie twórz nowych tagów

```
automatyzacja        szkolenia-AI         strategia-AI
ghostwriting         fundraising          framing
organizacje-społeczne  narzędzia-AI       LLM
prompt-engineering   vibe-coding          produkty-cyfrowe
content-marketing    trendy-AI            digital-campaigning
context-engineering  strategia-organizacji
```

## Format notatki (Galaxy/)

> **Plik podstawowy agenta piszącego noty Galaxy/: [`galaxy-strategia.md`](galaxy-strategia.md)** (w katalogu głównym vaultu). Przeczytaj go przed każdą sesją pisania w Galaxy/ — zawiera bieżący stan rozbudowy (fale, „Gdzie jesteśmy"), kryteria przyjęcia pojęcia, workflow `qmd` i kolejny krok. Po każdej istotnej zmianie w Galaxy/ aktualizuj ten plik (data w tytule H1 + sekcja „Gdzie jesteśmy"). Sekcja poniżej opisuje sam format notatki; strategia *co* i *kiedy* pisać jest w `galaxy-strategia.md`.

Galaxy/ to wiki pojęć — kompilacja wiedzy z wielu notatek Resources/. Działa jak u Karpathy'ego: LLM jest bibliotekarzem, który buduje i aktualizuje encyklopedię. Notatka konceptowa nie jest jednorazowym zapisem — rośnie przy każdym nowym źródle.

```yaml
---
categories: Concept
tags:
  - tag1
created: YYYY-MM-DD
updated: YYYY-MM-DD
relevance: wysoka | średnia | niska
sources:
  - "[[YYYY-MM-DD Tytuł notatki]]"
---
```

Nazwa pliku: `YYYY-MM-DD Tytuł pojęcia.md` (np. `2026-06-03 Uczenie transferowe.md`).

Sekcje treści: definicja (2–4 zdania własnymi słowami) → kluczowe mechanizmy / zasady → powiązane pojęcia (wikilinki) → zastosowanie w kontekście organizacji społecznych/AI/fundraising → otwarte pytania.

### Trzy operacje (metoda Karpathy'ego)

**Ingest** — po dodaniu notatki do Resources/ sprawdź, które strony Galaxy/ dotyczą tego tematu i zaktualizuj je o nowe wnioski. Jedno źródło może zaktualizować kilka stron Galaxy/. Jeśli pojęcie nie istnieje w Galaxy/ a zasługuje na własną stronę — utwórz ją.

**Query** — gdy odpowiedź na pytanie jest wartościowa i nowa (nie wynika wprost z jednej notatki), zapisz ją jako nową stronę Galaxy/ lub rozszerz istniejącą.

**Lint** — okresowo: szukaj stron Galaxy/ bez linków przychodzących (sieroty), nieaktualnych twierdzeń, luk tematycznych. Zaproponuj uzupełnienia.

## Areas i Projects — warstwa działań (PARA nad wiki)

Vault łączy dwie logiki: **wiki** (wiedza — `Resources/` + `Galaxy/`) i **PARA** (działania — `Projects/` + `Areas/`). Resources i Galaxy są jedynym źródłem prawdy dla treści; Projects i Areas są **soczewką działania** — trzymają wyłącznie notatki-huby (MOC) linkujące do wiedzy, **nigdy nie duplikują treści**.

### Reguła routingu — gdzie trafia notatka

1. Czy to **treść/wiedza** (artykuł, raport, newsletter, pojęcie)? → `Resources/` (źródło) lub `Galaxy/` (synteza). Bez zmian.
2. Czy to **przedsięwzięcie z konkretnym celem i momentem zakończenia** (data albo jasne „gotowe")? → `Projects/`.
3. Czy to **trwała odpowiedzialność lub rola bez końca**, którą utrzymujesz na pewnym standardzie? → `Areas/`.

Pytanie rozstrzygające Projects vs Areas: **„Czy to się kiedyś skończy?"** Tak, z metą → Project. Nie, trwa i wymaga utrzymania → Area.

Przykłady (profil: konsultant/trener organizacji społecznych — AI, fundraising, digital campaigning, ghostwriting):
- „Szkolenie AI dla Fundacji X — 12 maja" → **Project** (ma datę i metę)
- „Kampania fundraisingowa 2026 — domknięcie do końca Q1" → **Project**
- „Ghostwriting — klient Y" jako stała współpraca → **Area**
- „Digital campaigning / własna marka" jako ciągła praktyka → **Area**
- „Fundraising" jako stała dziedzina kompetencji → **Area**

### Relacje między folderami

- Każdy **Project** wskazuje nadrzędny **Area** (pole `area:`) i linkuje do potrzebnych `Resources/` i `Galaxy/`.
- Każdy **Area** agreguje swoje aktywne **Projects** oraz kluczowe pojęcia z `Galaxy/` i źródła z `Resources/` (wikilinki).
- Po zakończeniu projektu: ustaw `status: zakończony` i zostaw w `Projects/` (lub `Projects/Zakończone/`). **Nie** przenoś do `Archives/` — ten folder jest zarezerwowany na oryginały clipów (tylko-odczyt).
- Tagi w Projects/ i Areas/ — z tej samej zamkniętej listy co Resources/ i Galaxy/, max 3.

### Format notatki (Projects/)

```yaml
---
type: project
status: aktywny | wstrzymany | zakończony
created: YYYY-MM-DD
due: YYYY-MM-DD
area: "[[Areas/Nazwa obszaru]]"
tags:
  - tag1
---
```

Nazwa pliku: `YYYY-MM-DD Tytuł projektu.md`.
Sekcje: cel i definicja sukcesu (1–2 zdania) → kolejne kroki / zadania → powiązane zasoby (wikilinki do `Resources/` i `Galaxy/`) → log decyzji.

### Format notatki (Areas/)

```yaml
---
type: area
status: aktywny
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - tag1
---
```

Nazwa pliku: `Nazwa obszaru.md` (bez daty — obszar jest trwały).
Sekcje: standard do utrzymania (co znaczy „w porządku") → aktywne projekty (wikilinki do `Projects/`) → kluczowe pojęcia i źródła (wikilinki do `Galaxy/`/`Resources/`) → kadencja przeglądu.

## Szablony (`Templates/`)

Frontmatter każdego szablonu ma puste pola dat — wypełnia je plugin przy tworzeniu notatki albo użytkownik ręcznie. Tokeny `{{title}}`/`{{date:YYYY-MM-DD}}` występują tylko w treści (nie w properties).

| Szablon | `categories` | Folder docelowy | Do czego |
|---|---|---|---|
| `Clippings.md` | Clippings | `Resources/` | webclip z artykułu (plugin `/clippings-to-notes:clip`) |
| `Emails.md` | Emails | `Resources/` | newsletter / mail (plugin `/emails-to-notes:process`) |
| `Reports.md` | Reports | `Resources/` | raport PDF (plugin `/pdfs-to-notes:extract`) |
| `LinkedIn.md` | LinkedIn | `Resources/` | post LinkedIn (plugin `/linkedin-to-notes:save`) |
| `Concepts.md` | Concept | `Galaxy/` | nota pojęciowa (synteza z wielu źródeł) |
| `Projects.md` | Project | `Projects/` | przedsięwzięcie z celem i terminem (hub/MOC) |
| `Areas.md` | Area | `Areas/` | stała odpowiedzialność / rola (hub/MOC) |

Cztery pierwsze (Clippings/Emails/Reports/LinkedIn) to wzory referencyjne — pluginy `*-to-notes` generują treść własnym promptem i wpisują realne wartości frontmatteru. Trzy pozostałe (Concepts/Projects/Areas) są do ręcznego wstawiania.

## Pluginy

| Komenda | Źródło | Cel |
|---|---|---|
| `/clippings-to-notes:clip` | `Inbox/` | przetwarza clipy → `Resources/` + `Archives/` |
| `/emails-to-notes:process <etykieta>` | Gmail | newslettery → `Resources/` |
| `/pdfs-to-notes:extract [podfolder]` | `~/Documents/Email/` | raporty PDF → `Resources/` |
| `/linkedin-to-notes:save` | wklejony post LinkedIn | post → `Resources/` |
| `/index:update vault` | `Resources/` | weryfikacja i naprawa `Resources/index.md` |
