# Audyt Resources/index.md — 2026-06-09

## 1. Duplikaty wpisów w indeksie

Cztery wpisy pojawiają się w `index.md` dwukrotnie (identyczny link `[[...]]`):

- `2025-05-20 We did the math on AI s energy footprint. Here s the story you haven t heard.`
- `2025-05-22 77 million miles of waterways were missing from maps. AI found them in record time`
- `2026-02-03 Analiza głosu odbiorców w NGO. Jak wspierać ją narzędziami AI`
- `2026-02-11 Wellbeing w erze AI w NGO. Dlaczego szybsza praca nie oznacza zdrowszej pracy`

---

## 2. Pliki bez wpisu w indeksie

~~**Zweryfikowano 2026-06-10** — wszystkie poniższe pozycje to fałszywe alarmy. Stary regex `[^\]|]+` zatrzymywał się na pierwszym `]` wewnątrz tytułu (np. `[OLB]`, `[30 Day Growth Challenge]`), przez co nie wyciągał pełnego tytułu i `comm` zgłaszał pliki jako brakujące. Wszystkie serie i pojedyncze pliki są w indeksie. Regex w CLAUDE.md poprawiony 2026-06-10.~~

### ~~Seria [OLB] — 5 plików (2024-08-15–19)~~ ✓ wszystkie w indeksie

- ~~`2024-08-15 [OLB] Day 1 - Understanding the OODA Loop Framework`~~
- ~~`2024-08-16 [OLB] Day 2 - Observation & gathering data`~~
- ~~`2024-08-17 [OLB] Day 3 - Orientation - synthesising and analysing data`~~
- ~~`2024-08-18 [OLB] Day 4 - Decision & why you're not ready`~~
- ~~`2024-08-19 [OLB] Day 5 - Action & staying agile`~~

### ~~Pojedyncze~~ ✓ wszystkie w indeksie

- ~~`2025-09-18 United we [digitally] organize`~~
- ~~`2026-04-20 Is Reddit REALLY THE KEY to AI Search? Let's Find Out…`~~
- ~~`2026-04-21 Is a shared IP secretly harming your deliverability?`~~
- ~~`2026-06-02 Why Missing the Inbox Costs More Than You Realize`~~ *(to `Send It Right - Why Missing...` — ten sam plik, inny tytuł w indeksie)*

### ~~Seria [30 Day Growth Challenge] — 13 plików (2026-03-16 – 2026-04-14)~~ ✓ wszystkie w indeksie

### ~~Seria [Day X] Substack — 4 pliki (2026-04-23–25)~~ ✓ wszystkie w indeksie

---

## 3. Zduplikowane pliki (dwa pliki, jeden artykuł)

Różnica wyłącznie w interpunkcji nazwy — jeden z plików jest zbędny:

| Para plików | Różnica |
|---|---|
| `2025-05-22 77 million miles of waterways were missing from maps AI found them in record time.md` vs `...maps. AI found them...` | brak/obecność kropki |
| `2026-02-03 Analiza głosu odbiorców w NGO Jak wspierać ją narzędziami AI.md` vs `.... Jak wspierać...` | brak/obecność kropki |
| `2026-02-11 Wellbeing w erze AI w NGO Dlaczego szybsza praca nie oznacza zdrowszej pracy.md` vs `.... Dlaczego...` | brak/obecność kropki |
| `2026-02-03 What you need to know about Google s AI inbox.md` vs `...Google's AI inbox.md` | prosta vs. kędzierzawa apostrof |

---

## Podsumowanie

| Problem | Liczba |
|---|---|
| Duplikaty wpisów w indeksie | 4 |
| Pliki bez wpisu w indeksie | ~37 → **0** (fałszywe alarmy, zob. sekcja 2) |
| Zduplikowane pliki (do usunięcia jednego) | 4 pary |
