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
- Po dodaniu notatki do `Resources/` dopisz wpis do `Resources/index.md` w formacie:
  `- [[YYYY-MM-DD Tytuł]] — jednozdaniowy opis co zawiera`

## Uzupełnianie index.md — procedura

`Resources/index.md` ma ~451 KB i 2370+ linii — nie można go czytać w całości. Używaj wyłącznie narzędzi bash.

### Krok 1 — znajdź brakujące wpisy

```bash
# Wylistuj pliki i wyciągnij zaindeksowane tytuły
ls /Users/piotr_air/Obsidian/Piotr/Resources/*.md | grep -v '/index' | sed 's|.*/||; s|\.md$||' | sort > /tmp/all_files.txt

# Wyciągnij alias (po |) jeśli istnieje, inaczej tytuł — obsługuje oba formaty linków
grep -oP '(?<=\|)[^\]]+(?=\]\])|(?<=\[\[)[^\]|]+(?=\]\])' \
  /Users/piotr_air/Obsidian/Piotr/Resources/index.md \
  | sed 's|^[^/]*/||' | sort > /tmp/indexed.txt

comm -23 /tmp/all_files.txt /tmp/indexed.txt
```

**Uwaga na fałszywe alarmy** — `comm` może nadal zgłosić plik jako brakujący jeśli:
- tytuł w indeksie ma inną interpunkcję niż nazwa pliku (np. `Don't` vs `Don't` — curly vs straight apostrof)
- tytuł ma inną wielkość liter (np. `extreme heat` vs `Extreme Heat`)
- nazwa pliku zaczyna się od `[nawiasy kwadratowe]` — regex `[^\]|]+` zatrzymuje się na `[`

Przed uznaniem pliku za brakujący **zawsze zweryfikuj** samą datą:
```bash
grep -c "YYYY-MM-DD" /Users/piotr_air/Obsidian/Piotr/Resources/index.md
```
Jeśli wynik > 0 — plik jest w indeksie (może mieć inny tytuł). Jeśli wynik = 0 — plik naprawdę nie istnieje w indeksie i należy go dodać.

### Krok 2 — znajdź duplikaty

```bash
grep -oP '(?<=\[\[)[^\]]+(?=\]\])' /Users/piotr_air/Obsidian/Piotr/Resources/index.md | sort | uniq -d
```

### Krok 3 — odczytaj treść notatki

Pliki mogą mieć w nazwie curly apostrofy (') — `head` z dosłowną nazwą zawiedzie. Użyj `find`:
```bash
find /Users/piotr_air/Obsidian/Piotr/Resources/ -name "YYYY-MM-DD*" -exec head -30 {} \;
```

### Krok 4 — dopisz wpis do index.md

Wpis wstawiaj **chronologicznie** — znajdź ostatni wpis z tego samego dnia lub poprzedniego:
```bash
grep -n "YYYY-MM-DD\|YYYY-MM-DD-1" /Users/piotr_air/Obsidian/Piotr/Resources/index.md | tail -5
```
Następnie użyj Edit z dokładnym kontekstem sąsiedniego wiersza jako `old_string`.

Format wpisu:
```
- [[YYYY-MM-DD Tytuł]] — jednozdaniowy opis co zawiera
```

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

## Pluginy (INGEST)

| Komenda | Źródło | Cel |
|---|---|---|
| `/clippings-to-notes:clip` | `Inbox/` | przetwarza clipy → `Resources/` + `Archives/` |
| `/emails-to-notes:process <etykieta>` | Gmail | newslettery → `Resources/` |
| `/pdfs-to-notes:extract [podfolder]` | `~/Documents/Email/` | raporty PDF → `Resources/` |
