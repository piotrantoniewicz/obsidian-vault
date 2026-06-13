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
├── Templates/    szablony notatek
└── Areas/  Projects/  References/  — w budowie
```

## Zasady

- `Archives/` i `Attachments/` są tylko do odczytu — nigdy tam nie pisz ani nie edytuj
- Przy każdym pytaniu o vault zacznij od `Resources/index.md` — to mapa 2000+ notatek
- Nowe notatki trafiają do `Resources/`, nazwa: `YYYY-MM-DD Tytuł artykułu.md`
- **Znak `#` jest zakazany w nazwach plików** — Obsidian traktuje `#` w wikilinku jako separator nagłówka, co łamie nawigację. Zamiast `#41` używaj `nr41`.
- Po dodaniu notatki do `Resources/` dopisz wpis do `Resources/index.md` w formacie:
  `- [[YYYY-MM-DD Tytuł]] — jednozdaniowy opis co zawiera`

## Praca z index.md

Weryfikację kompletności indeksu (brakujące wpisy, duplikaty) wykonuje plugin: **`/index:update vault`**.

Uwagi techniczne przy każdej operacji na index.md:
- Plik ma ~450 KB i 2300+ linii — **nigdy nie czytaj go w całości**, używaj `grep -n` i Edit.
- Wpisy wstawiaj **chronologicznie**: znajdź przez `grep -n "YYYY-MM-DD"` ostatni wpis z tej samej lub najbliższej wcześniejszej daty i użyj Edit z sąsiednim wierszem jako kontekstem.
- Nazwy plików mogą zawierać curly apostrofy (') — `head` z dosłowną nazwą zawiedzie, używaj `find ... -name "YYYY-MM-DD*"`.

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

Relevance oceniaj na podstawie profilu właściciela vaultu: freelance konsultant i trener NGO, specjalizacja w AI, automatyzacji, fundraisingu, digital campaigningu i ghostwritingu.

- `wysoka` — bezpośrednio przydatne w aktywnych projektach: NGO, fundraising, digital campaigning, AI dla organizacji, automatyzacja
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
type: concept
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

Sekcje treści: definicja (2–4 zdania własnymi słowami) → kluczowe mechanizmy / zasady → powiązane pojęcia (wikilinki) → zastosowanie w kontekście NGO/AI/fundraising → otwarte pytania.

### Trzy operacje (metoda Karpathy'ego)

**Ingest** — po dodaniu notatki do Resources/ sprawdź, które strony Galaxy/ dotyczą tego tematu i zaktualizuj je o nowe wnioski. Jedno źródło może zaktualizować kilka stron Galaxy/. Jeśli pojęcie nie istnieje w Galaxy/ a zasługuje na własną stronę — utwórz ją.

**Query** — gdy odpowiedź na pytanie jest wartościowa i nowa (nie wynika wprost z jednej notatki), zapisz ją jako nową stronę Galaxy/ lub rozszerz istniejącą.

**Lint** — okresowo: szukaj stron Galaxy/ bez linków przychodzących (sieroty), nieaktualnych twierdzeń, luk tematycznych. Zaproponuj uzupełnienia.

## Pluginy

| Komenda | Źródło | Cel |
|---|---|---|
| `/clippings-to-notes:clip` | `Inbox/` | przetwarza clipy → `Resources/` + `Archives/` |
| `/emails-to-notes:process <etykieta>` | Gmail | newslettery → `Resources/` |
| `/pdfs-to-notes:extract [podfolder]` | `~/Documents/Email/` | raporty PDF → `Resources/` |
| `/index:update vault` | `Resources/` | weryfikacja i naprawa `Resources/index.md` |
