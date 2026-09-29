# Strategia rozbudowy Galaxy/ — 2026-09-29 (`/galaxy:ingest 10 notatek`, siedemnasta partia kolejkowa — 9 stron zaktualizowanych, 11 nowych mechanizmów, 1 nowa pozycja w sekcjach Sprzeczności)

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-09-29, ostatnia operacja: **`/galaxy:ingest 10 notatek`**, siedemnasta partia kolejkowa)

**Galaxy/ = 32 strony** (bez zmian liczby stron — sesja dopisywała do istniejących) w trzech działach indeksu:
- **Fundraising** (10) — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców, Transfer międzypokoleniowy majątku, DAF
- **AI w organizacjach** (12) — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering, RODO i dane wrażliwe, Evale, Context layer organizacji, LLM Wiki, Suwerenność technologiczna, AI Act
- **Komunikacja i digital campaigning** (10) — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, Higiena listy, Ghostwriting, Marka osobista, Rapid response

**Ostatnia operacja — `/galaxy:ingest 10 notatek` (2026-09-29, siedemnasta partia kolejkowa).** Argument `10` bez jednostki — Piotr wybrał **10 notatek z kolejki**. Tym razem pełny indeks zbudowany awk-iem na komputerze Piotra; kontrola kompletności: **3483 wiersze = 3483 notatki**, brak plików poza indeksem. Partia: 7 notatek z `created: 2026-09-24`, 1 z 09-25, 2 pierwsze z 09-28. Wynik: **11 nowych mechanizmów na 8 stronach** (+ dopisek do istniejącego sporu na 9. stronie), **9 nowych punktów w „Zastosowaniach"** (każdy z testem skali w dół), **1 nowa pozycja w `## Sprzeczności`**, **1 notatka bez wkładu** (redesign strony WWW — brak strony i klastra).
- **Email deliverability** (+ mech. 41): właściciel deliverability to nie IT — sześć warunków zarządzania (O'Malley; luka kompetencyjna na 5000+ specjalistach).
- **Newsletter jako kanał** (+ mech. 41): *measurement mismatch*, „przychód jako opóźniony wskaźnik zaufania", osiem kroków „fundamenty przed wyrafinowaniem".
- **Higiena listy** (+ mech. 33): konwersja do zaufania — siedem poziomów siły zapisu, portfolio listy, *trust decay*; nowe otwarte pytanie o próg kohort.
- **Recurring giving** (+ mech. 30, 31): sustainerzy w apelu końcoworocznym (Avid: ok. 30% daje dodatkowo, mediana 77 USD); case Wheeler Mission (retencja sustainerów 87%, seria powitalna między 1. a 2. wpłatą). **Nowa pozycja w `## Sprzeczności`**: skala dodatkowego daru (+25% vs 30% × 77 USD).
- **Stewardship** (+ mech. 49, 50): 3 „P" Burk i rytm 12 miesięcy z podwyżką w rocznicę (Axelrad); reaktywacja z kwotą i datą ostatniej wpłaty (+247%, jeden test). Dopisek po stronie A w sporze „Podziękowanie po darowiźnie".
- **Framing** (+ mech. 55): własność problemu bije dystrybucję, architektura marki jako taktyka (Partisan, wybory w Niemczech).
- **Widoczność w AI search** (+ mech. 34): LinkedIn jako kanał AEO — indeksacja 1–2 dni, pierwsza linia jako odpowiedź (Zutrau).
- **Wdrażanie AI w organizacji społecznej** (+ mech. 72): „playground" i „priorytety, nie czas" (Behrend) — doprecyzowanie mech. 44, nie sprzeczność.

**Klastry-kandydaci** (`galaxy-kandydaci.md`): podbite wiersze **Segmentacja bazy darczyńców i odbiorców** (masa ~80, osiadł też na Recurring giving mech. 30 i Framing mech. 55) oraz **Kampania końcoworoczna** (~65, Recurring giving mech. 30). Redesign strony WWW — pojedyncze źródło, bez wiersza.

**Następny krok.** Kolejna partia startuje od pierwszej notatki po kursorze (2026-08-21 Social Media Video Statistics…, 2026-08-25 Power and Prosperity in Place…, 2026-08-28 A Virtual Auction Success Cheatsheet…). **Priorytet strukturalny bez zmian: rozbić stronę *Wdrażanie AI w organizacji społecznej*** (ok. 178 KB po tej partii) — najtańszą drogą jest `/galaxy:pisz` dla kandydata „Wdrożenie i własność stosu technologicznego w organizacji społecznej". Backlog czerwonych linków **bez zmian**: żadna sekcja „Powiązane pojęcia" nie była ruszana; nowe wikilinki to wyłącznie encje w treści mechanizmów (`[[Avid]]`, `[[Nathan Hill]]`, `[[Claire Axelrad]]`, `[[Bloomerang]]`, `[[Penelope Burk]]`, `[[Die Linke]]`, `[[Manuela Schwesig]]`, `[[Gabriella Zutrau]]`).

**Pozostało w kolejce: 20** (policzone metodą kursora po jego przesunięciu: 12 z `created: 2026-09-28`, 8 z 2026-09-29).

<!-- ingest-cursor: 2026-09-28 | 2026-08-18 How Long Should a Website Last Before a Redesign-.md -->


**Sprzeczności między źródłami** zapisuje się wyłącznie w sekcjach `## Sprzeczności` na stronach Galaxy — ten plik ich nie zbiera i nie prowadzi ich listy.


**Klastry-kandydaci na nowe strony** prowadzi osobny plik `galaxy-kandydaci.md` (jedna linia na klaster) — tego pliku ich nie zbiera.

**Czerwone linki — backlog** (próg napisania = **≥2 incoming z różnych stron**; liczniki **przeliczone grep-em po całym `Galaxy/` 2026-09-07**, po dopisaniu sekcji „Powiązane pojęcia" nowej strony *Rapid response*; osobno odnotowane: `[[CRM]]` ma 8 incoming, ale jako encja narzędziowa pozostaje poza Galaxy — kandydatem jest proces wdrożenia i własności stosu, nie narzędzie): **Sprawczość organizacyjna (3 — Agentic AI + Suwerenność technologiczna + Rapid response; NAJSILNIEJSZY KANDYDAT w backlogu linków, licznik podbity 2026-09-07)**, **Relational organising (2 — Peer-to-peer fundraising + Framing; próg osiągnięty 2026-09-06)**, **Thought leadership (2 — Ghostwriting + Marka osobista → KANDYDAT)**, **Automatyzacja (2 — Wdrażanie AI + druga strona; przyjęta jako pojęcie decyzją Piotra 2026-08-17, licznik zweryfikowany 2026-09-07)**, **Komunikacja kryzysowa (1 — z Rapid response; NOWA pozycja 2026-09-07, jednocześnie klaster z trzema źródłami — patrz kandydaci wyżej)**, **Kampania końcoworoczna (1 — z Rapid response; NOWA pozycja 2026-09-07, osobno ma masę ~55 trafień w Resources)**, Employee advocacy (1 — z Marki osobistej), AI Office (1 — z AI Act), Digital Omnibus (1 — z AI Act), Mobilizacja cyfrowa (1 — z Owned vs rented), Multi-touch attribution (1 — z Widoczności w AI search), Public Narrative (1 — z Framingu), Wizualizacja danych (1 — ze Storytellingu), Harness i scaffolding (1 — z Context engineeringu), **Storytelling w jednym zdaniu i technika mostu (1 — ze Storytellingu)**. ~~**Marka osobista**~~ — domknięta 2026-08-17. ~~AI Act~~ — 2026-07-20. ~~Suwerenność technologiczna~~ — 2026-07-07. ~~Higiena listy~~ — 2026-06-29. ~~Transfer międzypokoleniowy majątku~~, ~~RODO i dane wrażliwe~~, ~~DAF~~, ~~LLM Wiki~~ — 2026-07-06. Narzędzia, osoby i organizacje (Capgemini, McKinsey, Social Change Lab, Sheila McKechnie Foundation, Better Fundraising, Google for Nonprofits, Olmo 3, Wispr Flow, Claude Code, Make.com, NextAfter, CRM i in.) świadomie poza Galaxy — to nie pojęcia. **Pozycje encyjne (2026-08-17):** `[[Claude AI]]`, `[[Claude Code]]`, `[[Claude Cowork]]` — narzędzia, świadomie poza Galaxy.

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
