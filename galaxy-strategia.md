# Strategia rozbudowy Galaxy/ — 2026-07-24 (ingest: 30 notatek → 13 stron)

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-07-24)

**Galaxy/ = 30 stron** w trzech gęsto połączonych działach indeksu:
- **Fundraising** — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców, Transfer międzypokoleniowy majątku, DAF
- **AI w organizacjach** — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering, RODO i dane wrażliwe, Evale, Context layer organizacji, LLM Wiki, Suwerenność technologiczna, **AI Act** ← nowa
- **Komunikacja i digital campaigning** — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, Higiena listy, Ghostwriting

**Ostatnia operacja — ingest (2026-07-24):** 30 notatek z `Resources/` (2026-07-21 → 2026-07-24) → **13 stron zaktualizowanych**, 0 nowych stron. Największe przyrosty: **Framing** (+3 mechanizmy: sympatia vs salience/Stahl, gniew nie strach z RCT Social Change Lab n=3467, test „my robimy → ty możesz sprawić"), **AI governance** (+2: „pas startowy" wobec shadow AI i 3 pytania do dostawcy, Tri-Pillar + HITL jako praktyka stała — oba Neider), **Email deliverability** (+2: za rzadka wysyłka jako problem deliverability, BIMI jako efekt uboczny porządku), **Owned vs rented audience** (+3: odwrócenie rynku uwagi Quinn/Catalist, twórca jako partner Salander, erozja zaufania — 41% postów LinkedIn ze śladami AI). Dalej po jednym–dwóch mechanizmach: Suwerenność technologiczna (Ng o otwartych modelach, centra danych, rynek pracy), Widoczność w AI search (Q&A jako dźwignia GEO, TAYA), Storytelling oparty na danych (Aaker 5% vs 63%, decentralizacja narracji, dzień testowy), Higiena listy (kontrapunkt: wygaszaj po działaniu, nie po otwarciu), Newsletter jako kanał (funnel, EAA/WCAG), AI Act (art. 50 — 2 sierpnia 2026 bez zmian), Transparentność operacyjna (TAYA, jawność użycia AI), Wdrażanie AI (segmentacja apelu jako wzorcowy „Tuesday problem"), Transfer międzypokoleniowy (Giving USA 2026: zapisy +16,6%), Agentic AI (brak „przerwy sprawdzającej"), RODO (granica danych jako pierwszy artefakt). **Bez zmian w sekcjach „Powiązane pojęcia" — backlog czerwonych linków nietknięty** (liczniki przeliczone `grep`-em 2026-07-24, patrz niżej).

**Do decyzji Piotra (sprzeczność z ingestu):** **higiena listy vs częstotliwość wysyłki**. Dotychczasowa linia (Higiena listy mech. 1–4, Email deliverability mech. 5): nieaktywni szkodzą reputacji, sunset jest koniecznością. Nowe źródło (O'Malley, „Not Sending Enough Email"): (a) wygaszanie oparte na **otwarciach** jest zawodne po Apple MPP i integracji Gemini w Gmailu — potrafi odciąć realnie zaangażowanych; (b) **zbyt rzadka wysyłka też psuje deliverability** (Gmail sam proponuje wypisanie po ~30 dniach bez otwarć; cisza przerwana dużym wolumenem = wzorzec spamerski). Obie tezy zapisane jako mechanizm 8 na obu stronach, **bez nadpisywania starych** — decyzja, czy przyjąć „meaningful actions zamiast open rate" jako regułę nadrzędną, należy do Piotra.

**Następny krok:** bez zmian po ingest — backlog ≥2 ma nadal jednego kandydata: **Sprawczość organizacyjna** (2 incoming — Agentic AI + Suwerenność technologiczna; Ganz/agency, „AI odbiera sprawczość?", agency > agents) do napisania w pierwszej kolejności. Dalej: (a) klaster **AI jako współpracownik/digital workforce** (≥4 źródła o *organizacji* agentów); (b) **Marka osobista** (1 incoming, drugi naturalnie z Widoczności w AI search — E-E-A-T); (c) nowe czerwone linki AI Office / Digital Omnibus — obserwować, czy zbiorą drugi incoming; (d) operacyjnie: **contradiction detection przy ingest** (wniosek z LLM Wiki) do pluginów `*-to-notes`. Nowość z tej fali: klaster **Kampania końcoworoczna (year-end appeal)** ma najwyraźniej największą masę w całym vaultcie i jest kandydatem numer jeden po Sprawczości organizacyjnej.

**Klastry-kandydaci na nowe strony (z przeglądu 2026-06-22, akt. 2026-07-24):**
- **Kampania końcoworoczna / year-end appeal** — **NOWY, wysoka masa** (~34 trafienia w `Resources/index.md`: kalendarze, benchmarki NextAfter, strony donacji, testy, podsumowania 2025/2026). Mechanizmy już rozproszone po innych stronach (segmentacja AI z Wdrażania AI, dzień testowy ze Storytellingu, abandoned cart, Giving USA). Do napisania jako strona spinająca sezon Q4.
- **Twórcy, influencerzy i „amplifierzy" w kampaniach** — **NOWY, masa rośnie** (~36 trafień; z tej fali: Quinn/Catalist o rynku mediów obywatelskich, Salander o przewadze prawicy, Zaufanie w erze AI). Na razie mechanizmy 6–8 w Owned vs rented audience; osobna strona, gdy zbierze się warstwa *praktyki współpracy* z twórcami, nie samej diagnozy rynku.
- **Centra danych AI i opór lokalny** — **NOWY, ~11 trafień** (Waging Nonviolence 2026-07, referendum w Wisconsin, Missouri, Meksyk). Silny materiał kampanijny, ale bliżej newsa niż pojęcia — obserwować, czy wykrystalizuje się mechanizm (framing środowiskowy + koalicja ponad podziałami), czy zostanie case'em w Suwerenności technologicznej i Framingu.
- **Dostępność cyfrowa (EAA / WCAG)** — ~9 trafień, na razie za mało; wymogi zapisane jako mechanizm 8 w Newsletterze jako kanale. Obserwować.
- ~~**Ghostwriting / marka osobista**~~ — **domknięty 2026-07-07** jako strona `2026-07-07 Ghostwriting` (8 źródeł); wątek „marka osobista" świadomie wydzielony jako czerwony link.
- ~~**Suwerenność technologiczna / europejskie alternatywy**~~ — **domknięty 2026-07-07** jako strona `2026-07-07 Suwerenność technologiczna` (10 źródeł; czerwony link z Owned vs rented zrealizowany).
- ~~**AI Act**~~ — **domknięty 2026-07-20** jako strona `2026-07-20 AI Act` (8 źródeł; czerwone linki z RODO i dane wrażliwe + Suwerenność technologiczna zrealizowane).
- ~~**Evale**~~ i ~~**Context layer organizacji**~~ — domknięte 2026-07-06.
- **AI jako współpracownik / digital workforce** — wielo­agentowa struktura org (chief of staff → dyrektorzy → specjaliści → watchdog), agent-jako-plik, meta-prompting. Na razie mechanizm 8 Agentic AI; osobna strona dopiero, gdy będzie ≥4 źródła o *organizacji* agentów (nie samej technologii).

**Czerwone linki — backlog** (próg napisania = **≥2 incoming**, liczniki przeliczone `grep`-em 2026-07-24 — ingest 2026-07-24 nie zmienił żadnego licznika): **Sprawczość organizacyjna (2 — Agentic AI + Suwerenność technologiczna → KANDYDAT)**, Marka osobista (1 — z Ghostwritingu), Thought leadership (1 — z Ghostwritingu), AI Office (1 — z AI Act), Digital Omnibus (1 — z AI Act), Mobilizacja cyfrowa (1 — drugi incoming naturalnie z Higieny listy lub Newslettera), Public Narrative (1), Wizualizacja danych (1), Harness i scaffolding (1). ~~AI Act~~ — domknięty 2026-07-20. ~~Suwerenność technologiczna~~ — domknięta 2026-07-07. ~~Higiena listy~~ — domknięta 2026-06-29. ~~Transfer międzypokoleniowy majątku~~, ~~RODO i dane wrażliwe~~, ~~DAF~~, ~~LLM Wiki~~ — domknięte 2026-07-06. Narzędzia/organizacje (CRM, Make.com, LLM, Blackbaud, Ollama) świadomie poza Galaxy — to nie pojęcia.

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
