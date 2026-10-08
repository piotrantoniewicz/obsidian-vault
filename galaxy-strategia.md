# Strategia rozbudowy Galaxy/ — 2026-10-08 (`/galaxy:lint` — 7 kontroli, 0 sierot, 0 zepsutych wikilinków, 5 poprawek terminologii, liczniki backlogu bez zmian)

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-10-08, ostatnia operacja: **`/galaxy:lint`**)

**Galaxy/ = 36 stron** (w tym 3 wydzielone z *Wdrażania AI*) w trzech działach indeksu:
- **Fundraising** (11) — Tożsamość darczyńcy, Recurring giving, Stewardship, Kampania końcoworoczna, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców, Transfer międzypokoleniowy majątku, DAF
- **AI w organizacjach** (15) — Wdrażanie AI w organizacji społecznej, Wdrożenie i własność stosu technologicznego, Ludzie, role i zmiana w organizacji, Luka adopcyjna, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering, RODO i dane wrażliwe, Evale, Context layer organizacji, LLM Wiki, Suwerenność technologiczna, AI Act
- **Komunikacja i digital campaigning** (10) — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, Higiena listy, Ghostwriting, Marka osobista, Rapid response

**Ostatnia operacja — `/galaxy:lint` (2026-10-08).** Siedem kontroli na 36 stronach. Sieroty: 0 (każda strona ma linki przychodzące z innych stron Galaxy). Zepsute wikilinki: 0; brak aliasu w „Powiązane pojęcia”: 0. Indeks `Galaxy/index.md`: 36 wpisów = 36 stron, bez widm i duplikatów. Format: frontmatter kompletny, tagi z zamkniętej listy (max 3), ≥4 źródła, ≥3 linki do stron Galaxy i sekcja zastosowania na każdej stronie. Naprawiono 5 wystąpień „NGO” / „organizacji pozarządowych” w treści (*Wdrażanie AI*, *Luka adopcyjna*, *Framing*, *Marka osobista*). Liczniki backlogu czerwonych linków przeliczone grep-em po całym `Galaxy/` — bez zmian. Ustalenia wymagające decyzji (dane starsze niż rok, niepełne metryczki w sekcjach `## Sprzeczności`, test skali w dół w starszych stronach) poszły do raportu lintu.

**Następny krok.** Kandydaci do napisania (≥2 incoming z różnych stron): *Sprawczość organizacyjna* (3), *Relational organising* (2), *Thought leadership* (2), *Automatyzacja* (2). Kolejna partia ingestu, gdy w `Resources/` pojawią się nowe notatki (kolejka pusta). Progi rekompilacji (skrypt, 2026-10-08): przekraczają *Email deliverability* (11 631 słów, 41 mech.), *Newsletter jako kanał* (13 922 słów, 43 mech.), *Widoczność w AI search* (34 mech.), *Owned vs rented audience* (10 580 słów, 38 mech.), *Higiena listy* (34 mech.), *Ghostwriting* (13 126 słów, 53 mech.) i *Suwerenność technologiczna* (27 mech.); z poprzedniej partii wciąż: *Stewardship*, *Transparentność operacyjna*, *Wdrażanie AI*, *AI governance*, *Agentic AI*; wg stanu sprzed tych dwóch partii (nie mierzone ponownie) także *Framing*, *Recurring giving* i *Prompt engineering*. Backlog czerwonych linków: liczniki bez zmian.

**Pozostało w kolejce: 0** (policzone metodą kursora po jego przesunięciu).

<!-- ingest-cursor: 2026-10-08 | 2026-10-08 how to land your first writing client this week.md -->


**Sprzeczności między źródłami** zapisuje się wyłącznie w sekcjach `## Sprzeczności` na stronach Galaxy — ten plik ich nie zbiera i nie prowadzi ich listy.


**Klastry-kandydaci na nowe strony** prowadzi osobny plik `galaxy-kandydaci.md` (jedna linia na klaster) — tego pliku ich nie zbiera.

**Czerwone linki — backlog** (próg napisania = **≥2 incoming z różnych stron**; liczniki **przeliczone grep-em po całym `Galaxy/` 2026-10-08** (`/galaxy:lint`; poprzednio 2026-10-06, po dopisaniu sekcji „Powiązane pojęcia" nowej strony *Rapid response*); osobno odnotowane: `[[CRM]]` ma 8 incoming, ale jako encja narzędziowa pozostaje poza Galaxy — kandydatem jest proces wdrożenia i własności stosu, nie narzędzie): **Sprawczość organizacyjna (3 — Agentic AI + Suwerenność technologiczna + Rapid response; NAJSILNIEJSZY KANDYDAT w backlogu linków, licznik podbity 2026-09-07)**, **Relational organising (2 — Peer-to-peer fundraising + Framing; próg osiągnięty 2026-09-06)**, **Thought leadership (2 — Ghostwriting + Marka osobista → KANDYDAT)**, **Automatyzacja (2 — Wdrażanie AI + Agentic AI; przyjęta jako pojęcie decyzją Piotra 2026-08-17, licznik zweryfikowany 2026-09-07)**, **Komunikacja kryzysowa (1 — z Rapid response; NOWA pozycja 2026-09-07, jednocześnie klaster z trzema źródłami — patrz kandydaci wyżej)**, Employee advocacy (1 — z Marki osobistej), AI Office (1 — z AI Act), Digital Omnibus (1 — z AI Act), Mobilizacja cyfrowa (1 — z Owned vs rented), Multi-touch attribution (1 — z Widoczności w AI search), Public Narrative (1 — z Framingu), Wizualizacja danych (1 — ze Storytellingu), Harness i scaffolding (1 — z Context engineeringu), **Storytelling w jednym zdaniu i technika mostu (1 — ze Storytellingu)**. ~~**Kampania końcoworoczna**~~ — domknięta 2026-09-30 (wydzielona ze Stewardship). ~~**Marka osobista**~~ — domknięta 2026-08-17. ~~AI Act~~ — 2026-07-20. ~~Suwerenność technologiczna~~ — 2026-07-07. ~~Higiena listy~~ — 2026-06-29. ~~Transfer międzypokoleniowy majątku~~, ~~RODO i dane wrażliwe~~, ~~DAF~~, ~~LLM Wiki~~ — 2026-07-06. Narzędzia, osoby i organizacje (Capgemini, McKinsey, Social Change Lab, Sheila McKechnie Foundation, Better Fundraising, Google for Nonprofits, Olmo 3, Wispr Flow, Claude Code, Make.com, NextAfter, CRM i in.) świadomie poza Galaxy — to nie pojęcia. **Pozycje encyjne (2026-08-17):** `[[Claude AI]]`, `[[Claude Code]]`, `[[Claude Cowork]]` — narzędzia, świadomie poza Galaxy.

## Zasada nadrzędna

Galaxy/ rośnie **od popytu, nie od podaży**. Nie przerabiamy Resources/ hurtowo na pojęcia — tworzymy stronę wtedy, gdy: (a) istnieje czerwony link, (b) klaster ma masę krytyczną źródeł, (c) padło pytanie, na które odpowiedź była syntezą wielu notatek (operacja Query z CLAUDE.md).

### Kryteria przyjęcia pojęcia do Galaxy/

1. **Min. 4–5 źródeł** w Resources/ (weryfikacja: `qmd query`)
2. **Pojęcie, nie news** — musi być aktualne za rok (mechanizm, framework, zjawisko; nie "premiera GPT-X")
3. **Relevance dla profilu**: NGO / fundraising / AI dla organizacji / digital campaigning / ghostwriting
4. Format i sekcje wg `CLAUDE.md` (type: concept, sources, definicja → mechanizmy → powiązane pojęcia → zastosowanie NGO → otwarte pytania)

## Workflow tworzenia notatki konceptowej (przepis qmd)

Cel zbierania: **jak najszersza pula kandydatów**, potem ręczna kuracja do ≥4–5 źródeł. Jedno zapytanie ciąży ku dominującej frazeologii klastra i gubi tematyczne outliery — dlatego trzy niezależne kanały recall + kilka sformułowań pojęcia.

```bash
# 1. Hybryda, szeroka pula (expansion + BM25 + wektory + reranking)
qmd query "<pojęcie + kontekst>" -c obsidian -n 25 -C 120

# 2. Czysto semantyczny — łapie inne notatki niż hybryda (to samo znaczenie, inne słowa)
qmd vsearch "<pojęcie>" -c obsidian -n 30

# 3. Recall niezależny od embeddingów — Twoje własne opisy 2600+ notatek
grep -iE "<słowa kluczowe|synonimy>" Resources/index.md

# 4. Powtórz 1–2 dla 2–3 różnych sformułowań pojęcia (synonimy, węższe/szersze ujęcia)
#    np. "tożsamość darczyńcy" / "przynależność wspólnota" / "lojalność darczyńcy"

# 5. Pobierz treść wybranych notatek
qmd get qmd://obsidian/resources/<plik>.md
```

Zasady:
- **Dedup po tytule:** Archives/ i Resources/ to ten sam temat (oryginał vs synteza), nie dwa źródła. W `sources` wpisuj **wersję z Resources/**; oryginał z Archives/ otwieraj po pełne dane, kontekst i dosłowne cytaty (Archives = głębia, Resources = cytowanie). **Nie wykluczaj Archives z wyszukiwania** — pełny tekst i język oryginału zwiększają recall.
- Resources są po polsku — zapytania formułuj po polsku (oryginał angielski siedzi w Archives i tak wpada przez pełnotekstowe dopasowanie).
- Po napisaniu notatki: dopisz wpis do `Galaxy/index.md` + sprawdź, czy inne strony Galaxy/ powinny dostać wikilink do nowego pojęcia
- Czerwone linki w sekcji "Powiązane pojęcia" zostawiaj świadomie — to backlog następnych stron
- Po sesji pisania: `qmd update` + `qmd embed`, żeby nowe strony były wyszukiwalne następnym razem

## Operacje stałe (metoda Karpathy'ego)

- **Ingest** (przy każdym przetwarzaniu Inbox/maili/PDF): po dodaniu notatki do Resources/ sprawdź `qmd vsearch "<temat notatki>"` ograniczone do Galaxy/ — zaktualizuj istniejące strony (`updated` + nowe źródło w `sources`), zamiast tworzyć nowe
- **Query** (ad hoc): wartościowa odpowiedź na pytanie → nowa strona lub rozszerzenie istniejącej
- **Lint** (co miesiąc):
  - sieroty: strony Galaxy/ bez linków przychodzących (`grep -rl "[[<nazwa>" --include="*.md"` po vaulcie)
  - czerwone linki: pojęcia linkowane ≥2 razy z różnych stron → priorytet do napisania
  - przeterminowane twierdzenia (statystyki starsze niż rok)

## Tempo i miara sukcesu

- **Tempo**: 2–3 pojęcia tygodniowo (jedna sesja z Claude = 1 fala mini: query → źródła → notatka → index)
- **Kwartał**: ~25–30 stron pokrywających klastry fundraising + AI w organizacjach
- **Miara jakości, nie ilości**: każda strona ma ≥4 źródła, ≥3 wikilinki do innych stron Galaxy/, sekcję zastosowania NGO. Strona, której nie da się zastosować w pracy konsultanta — nie powstaje.
