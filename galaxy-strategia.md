# Strategia rozbudowy Galaxy/ — 2026-09-30 (`/galaxy:ingest 10 notatek`, dziewiętnasta partia kolejkowa — 11 stron zaktualizowanych, 14 nowych mechanizmów, 2 nowe spory w sekcjach Sprzeczności)

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-09-30, ostatnia operacja: **`/galaxy:ingest 10 notatek`**, dziewiętnasta partia kolejkowa)

**Galaxy/ = 32 strony** (bez zmian liczby stron — sesja dopisywała do istniejących) w trzech działach indeksu:
- **Fundraising** (10) — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców, Transfer międzypokoleniowy majątku, DAF
- **AI w organizacjach** (12) — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering, RODO i dane wrażliwe, Evale, Context layer organizacji, LLM Wiki, Suwerenność technologiczna, AI Act
- **Komunikacja i digital campaigning** (10) — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, Higiena listy, Ghostwriting, Marka osobista, Rapid response

**Ostatnia operacja — `/galaxy:ingest 10 notatek` (2026-09-30, dziewiętnasta partia kolejkowa).** Argument `10` bez jednostki — Piotr wybrał **10 notatek z kolejki**. Kontrola kompletności indeksu: **3483 wiersze = 3483 notatki**. Partia: 2 notatki z `created: 2026-09-28` i 8 z `created: 2026-09-29`. Wynik: **wszystkie 10 notatek wniosło coś do Galaxy** — **14 nowych mechanizmów na 11 stronach**, **13 nowych punktów w „Zastosowaniach"** (każdy z testem skali w dół), **2 nowe spory w `## Sprzeczności`** (jeden zapisany na dwóch stronach), **4 dopiski do istniejących sporów**.
- **Stewardship** (+ mech. 52, 53): polska sekwencja „48 h / 30 dni" wpisana w segmentację (Armiger / Impact Creator) i sezon końcoworoczny rozłożony na pięć okien i segmenty (Fundraise Up, *Pulse Check*). **Nowy spór**: tempo sekwencji po pierwszej wpłacie — miesiąc (Armiger) czy kwartał (CauseVox, mech. 33). Dopisek do sporu o retencję nowych darczyńców (polski odczyt: ok. 70% daje tylko raz).
- **Recurring giving** (+ mech. 32, 33): polskie formy wpłat regularnych (polecenie zapłaty, zlecenie stałe, karta, BLIK) i pierwszorazowi jako najbardziej skłonni do daru cyklicznego w sezonie. Dopisek po stronie B w sporze „drugi rok czy pierwsze trzy miesiące".
- **Higiena listy** (+ mech. 34): deduplikacja z raportem możliwych duplikatów i profil darczyńcy w CRM.
- **Newsletter jako kanał** (+ mech. 42): +81% przy niemal codziennej wysyłce i test częstotliwości (Civic Shout / LSSN). **Nowy spór**, zapisany też na *Higienie listy*: częstsze wysyłki — szybsza habituacja (O'Malley, mech. 11) czy wyższy przychód przy wypisach <1%?
- **Transparentność operacyjna** (+ mech. 38, 39): grant jako mnożnik, spis wsparcia rzeczowego i 90-dniowa kampania „proof" (DonorDock: Lebby, Burke); cash flow zamiast budżetu i rozmowa z zarządem (Kim Nagle). Dopisek do sporu o próg koncentracji: drugi głos za 40%.
- **Prompt engineering** (+ mech. 26): siedem zasad wspólnych dla Anthropic, Google i OpenAI oraz halucynacje ograniczane procesem (Wojdalski).
- **Wdrażanie AI** (+ mech. 73): adopcja płytka vs głęboka i siedem problemów behawioralnych (Szczesna). Dopisek do sporu o lukę wdrożeniową (MIT NANDA 40% vs 5%).
- **AI governance** (+ mech. 47): człowiek w pętli bez wpływu, czasu i wiedzy — test przeciw „moralnej strefie zgniotu" (Szczesna).
- **Context layer organizacji** (+ mech. 24): „konwersja dokumentów na markdown" jako produkt, test sześciu miesięcy (agencja Boom).
- **Framing** (+ mech. 56) i **Owned vs rented audience** (+ mech. 37): czytelnik jako bohater i wskazany złoczyńca; CTA do newslettera w każdym poście vs lead magnety (Tribe Digital / Rohan Sheth).

**Klastry-kandydaci** (`galaxy-kandydaci.md`): **Dywersyfikacja przychodów / odporność finansowa** podniesiona do „kandydat realny" (trzy nowe źródła, temat rozlany po ośmiu mechanizmach Transparentności). Podbite wiersze: **Kampania końcoworoczna** (Stewardship mech. 53, Recurring giving mech. 33), **Segmentacja bazy darczyńców** i **Marketing automation i sekwencje mailowe** (Stewardship mech. 52).

**Następny krok.** **Kolejka jest pusta** — kolejny ingest ma sens po dopływie nowych notatek do `Resources/`. **Priorytet strukturalny: rozbić stronę *Wdrażanie AI w organizacji społecznej*** (ok. 182 KB po tej partii) — najtańszą drogą jest `/galaxy:pisz` dla kandydata „Wdrożenie i własność stosu technologicznego w organizacji społecznej". Drugi kandydat do rozbicia to *Stewardship* (ok. 129 KB). Wśród klastrów najmocniej dojrzała **Dywersyfikacja przychodów / odporność finansowa** — strona odciążyłaby *Transparentność operacyjną*. Backlog czerwonych linków **bez zmian**: żadna sekcja „Powiązane pojęcia" nie była ruszana; nowe wikilinki to wyłącznie encje w treści mechanizmów (`[[Armiger]]`, `[[Impact Creator]]`, `[[Fundraise Up]]`, `[[Kim Nagle]]`, `[[Audubon]]`, `[[Lichen Sclerosus Support Network]]`, `[[Tribe Digital]]`, `[[Rohan Sheth]]`, `[[Mateusz Wojdalski]]`, `[[MIT NANDA]]`, `[[Gallup]]`, `[[Microsoft]]`, `[[Cory Doctorow]]`, `[[ChatGPT]]`).

**Pozostało w kolejce: 0** (policzone metodą kursora po jego przesunięciu).

<!-- ingest-cursor: 2026-09-29 | 2026-09-29 The grant that would have sunk them.md -->


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
