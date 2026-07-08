---
paths:
  - "Projects/**"
  - "Areas/**"
---

# Projects/ i Areas/ — warstwa działań (PARA nad wiki)

Vault łączy dwie logiki: **wiki** (wiedza — `Resources/` + `Galaxy/`) i **PARA** (działania — `Projects/` + `Areas/`). Resources i Galaxy są jedynym źródłem prawdy dla treści; Projects i Areas są **soczewką działania** — trzymają wyłącznie notatki-huby (MOC) linkujące do wiedzy, **nigdy nie duplikują treści**.

Pytanie rozstrzygające Projects vs Areas: **„Czy to się kiedyś skończy?"** Tak, z metą → Project. Nie, trwa i wymaga utrzymania → Area.

Przykłady (profil: konsultant/trener organizacji społecznych — AI, fundraising, digital campaigning, ghostwriting):
- „Szkolenie AI dla Fundacji X — 12 maja" → **Project** (ma datę i metę)
- „Kampania fundraisingowa 2026 — domknięcie do końca Q1" → **Project**
- „Ghostwriting — klient Y" jako stała współpraca → **Area**
- „Digital campaigning / własna marka" jako ciągła praktyka → **Area**
- „Fundraising" jako stała dziedzina kompetencji → **Area**

## Relacje między folderami

- Każdy **Project** wskazuje nadrzędny **Area** (pole `area:`) i linkuje do potrzebnych `Resources/` i `Galaxy/`.
- Każdy **Area** agreguje swoje aktywne **Projects** oraz kluczowe pojęcia z `Galaxy/` i źródła z `Resources/` (wikilinki).
- Po zakończeniu projektu: ustaw `status: zakończony` i zostaw w `Projects/` (lub `Projects/Zakończone/`). **Nie** przenoś do `Archives/` — ten folder jest zarezerwowany na oryginały clipów (tylko-odczyt).
- Tagi w Projects/ i Areas/ — z tej samej zamkniętej listy co Resources/ i Galaxy/, max 3.

## Format notatki (Projects/)

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

## Format notatki (Areas/)

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
