---
paths:
  - "Resources/**"
---

# Resources/ — format notatki i praca z index.md

## Format notatki

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

## Praca z index.md

Weryfikację kompletności indeksu (brakujące wpisy, duplikaty) wykonuje plugin: **`/index:update vault`**.

Uwagi techniczne przy każdej operacji na `Resources/index.md`:
- Plik ma ~670 KB i 3150+ linii — **nigdy nie czytaj go w całości**, używaj `grep -n` i Edit.
- Wpisy wstawiaj **chronologicznie**: znajdź przez `grep -n "YYYY-MM-DD"` ostatni wpis z tej samej lub najbliższej wcześniejszej daty i użyj Edit z sąsiednim wierszem jako kontekstem.
- Nazwy plików mogą zawierać curly apostrofy (') — `head` z dosłowną nazwą zawiedzie, używaj `find ... -name "YYYY-MM-DD*"`.
