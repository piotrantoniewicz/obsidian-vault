---
paths:
  - "Galaxy/**"
  - "galaxy-strategia.md"
---

# Galaxy/ — format notatki i procedury obowiązkowe

> **Plik podstawowy agenta piszącego noty Galaxy/: [`galaxy-strategia.md`](../../galaxy-strategia.md)** (w katalogu głównym vaultu). Przeczytaj go przed każdą sesją pisania w Galaxy/ — zawiera bieżący stan rozbudowy (fale, „Gdzie jesteśmy"), kryteria przyjęcia pojęcia, workflow `qmd` i kolejny krok. Po każdej istotnej zmianie w Galaxy/ aktualizuj ten plik (data w tytule H1 + sekcja „Gdzie jesteśmy").

Galaxy/ to wiki pojęć — kompilacja wiedzy z wielu notatek Resources/. Działa jak u Karpathy'ego: LLM jest bibliotekarzem, który buduje i aktualizuje encyklopedię. Notatka konceptowa nie jest jednorazowym zapisem — rośnie przy każdym nowym źródle.

## Format notatki

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

## Uzgadnianie liczników czerwonych linków (obowiązkowe po każdej zmianie w Galaxy/)

Backlog czerwonych linków w `galaxy-strategia.md` (próg napisania = **≥2 incoming z różnych stron Galaxy/**) musi być **przeliczany, nie dopisywany**. Za każdym razem, gdy tworzysz lub edytujesz stronę Galaxy/ i zmieniasz sekcję „Powiązane pojęcia" (dodajesz/usuwasz czerwony link), **w tej samej sesji** uzgodnij liczniki:

1. Przelicz incoming dla każdego dotkniętego pojęcia (faktyczny stan, nie pamięć):
   `grep -rl "\[\[<pojęcie>" Galaxy/ --include="*.md" | grep -v index.md`
2. Zaktualizuj liczniki w backlogu **oraz** zdanie zbiorcze w „Następny krok" (np. „żaden link nie ma ≥2" jest prawdziwe tylko do pierwszego przekroczenia progu).
3. Jeśli pojęcie osiągnęło **≥2** — oznacz je jako kandydata do napisania (nie zostawiaj jako „(1)").

Typowa pułapka: napisanie nowej strony dorzuca drugi incoming istniejącemu czerwonemu linkowi (przez własną sekcję „Powiązane pojęcia"), ale licznik tamtego pojęcia nie zostaje podbity → backlog kłamie. Po sesji liczniki w `galaxy-strategia.md` muszą zgadzać się z `grep`.

## Walidacja wikilinków (obowiązkowa po każdej edycji Galaxy/)

Każdy nowy wikilink (w `sources`, „Powiązane pojęcia" i w treści) musi celować w **dosłowny basename pliku**, nie w tytuł H1 ani z pamięci. Po sesji pisania zweryfikuj, że nowe linki do Resources/ trafiają w realne pliki:

```bash
find . -name "<dokładny tytuł>.md" -not -path '*/.claude/*'
```

Dwie powtarzalne pułapki:
- **Sanityzacja znaków w nazwie pliku** — cudzysłowy, `?`, `:` itp. z oryginalnego tytułu bywają w nazwie pliku zamienione na myślniki (`"thank you"` → `-thank you-`). Nie odtwarzaj nazwy z H1 — sprawdź realny plik (`find`/`qmd get` zwraca ścieżkę). To samo dotyczy znaków `&`, `$`, curly apostrofów (').
- **Konwencja aliasu w „Powiązane pojęcia"** — linki do innych stron Galaxy/ pisz zawsze jako `[[YYYY-MM-DD Tytuł|Tytuł]]` (alias ukrywa datę). Pojedynczy link bez `|` wyświetli się z datą i złamie spójność sekcji.

## Trzy operacje (metoda Karpathy'ego)

**Ingest** — po dodaniu notatki do Resources/ sprawdź, które strony Galaxy/ dotyczą tego tematu i zaktualizuj je o nowe wnioski. Jedno źródło może zaktualizować kilka stron Galaxy/. Jeśli pojęcie nie istnieje w Galaxy/ a zasługuje na własną stronę — utwórz ją.

**Query** — gdy odpowiedź na pytanie jest wartościowa i nowa (nie wynika wprost z jednej notatki), zapisz ją jako nową stronę Galaxy/ lub rozszerz istniejącą.

**Lint** — okresowo: szukaj stron Galaxy/ bez linków przychodzących (sieroty), nieaktualnych twierdzeń, luk tematycznych. Zaproponuj uzupełnienia.

Po sesji pisania w Galaxy/: `qmd update` + `qmd embed`, żeby nowe strony były wyszukiwalne następnym razem.
