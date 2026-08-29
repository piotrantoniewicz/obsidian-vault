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

Sekcje treści: definicja (2–4 zdania własnymi słowami) → kluczowe mechanizmy / zasady → **sprzeczności** (sekcja warunkowa) → powiązane pojęcia (wikilinki) → zastosowanie w kontekście organizacji społecznych → otwarte pytania.

## Sekcja „Sprzeczności" (warunkowa, obowiązkowa gdy źródła się kłócą)

Gdy nowe źródło kłóci się z tym, co strona już twierdzi — inna liczba, przeciwny wniosek, nowsze badanie obalające starsze — konflikt **zostaje zapisany na stronie**, nie tylko w raporcie sesji. Sekcja `## Sprzeczności` stoi między „Kluczowe mechanizmy" a „Powiązane pojęcia". Zakładasz ją przy pierwszym konflikcie; strony bez konfliktów jej nie mają (pusty nagłówek = usterka do usunięcia).

Format pozycji:

```
- **<nazwa sporu w 3–6 słowach>** [mech. N] — A: <teza z liczbą> ([[YYYY-MM-DD Źródło A|Źródło A]], rok, n=…, kontekst). B: <teza z liczbą> ([[YYYY-MM-DD Źródło B|Źródło B]], rok, n=…, kontekst). *Status: otwarte.*
```

- **Nie rozstrzygaj i nie uśredniaj** — ani „prawda leży pośrodku", ani ciche przyjęcie nowszej liczby. Zapisujesz obie wersje z metryczkami i zostawiasz decyzję człowiekowi.
- **Nie nadpisuj mechanizmu**, z którym nowe źródło się kłóci (append, never overwrite) — sprzeczność jest komentarzem do mechanizmu, nie jego zamiennikiem.
- **Metryczka po obu stronach:** źródło (wersja z `Resources/`), rok, n, kraj/rynek; brak którejś → napisz to wprost.
- **Pozorny konflikt** (inna populacja, inna definicja metryki, inny rynek) to doprecyzowanie zakresu w mechanizmie, nie sprzeczność.
- **Status zmienia wyłącznie człowiek:** `*Status: rozstrzygnięte RRRR-MM-DD — <co przyjęto i dlaczego>.*` Pozycji nie usuwaj — to ślad proweniencji.
- Spór dotykający kilku stron zapisz na każdej z nich.

## Test skali w dół (warunek wejścia do „Zastosowania")

Jednostka odniesienia: organizacja **2–5 osób, bez działu IT, bez etatu prawnika, z bazą kilkuset kontaktów**. Każda rekomendacja w sekcji zastosowania niesie jedną z trzech odpowiedzi, wprost w tekście punktu:

1. **działa w tej skali** — z nakładem lub narzędziem („arkusz i godzina miesięcznie");
2. **działa od progu** — z nazwanym progiem lub warunkiem („od ~2000 adresów", „gdy ktoś odpowiada za CRM");
3. **nie działa w tej skali** — z tańszym substytutem albo wskazaniem, z czego zrezygnować.

Rekomendacja bez jednej z tych odpowiedzi nie wchodzi na stronę. Gdy źródła nie dają podstaw — napisz to w punkcie wprost, a pytanie o próg przenieś do „Otwartych pytań". Progu nigdy nie zmyślaj.

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
