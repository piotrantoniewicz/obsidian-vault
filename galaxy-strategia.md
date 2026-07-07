# Strategia rozbudowy Galaxy/ — 2026-07-06 (sześć nowych stron: Transfer międzypokoleniowy majątku, RODO i dane wrażliwe, DAF, Evale, Context layer organizacji, LLM Wiki)

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-07-06)

**Galaxy/ = 27 stron** w trzech gęsto połączonych działach indeksu:
- **Fundraising** — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców, **Transfer międzypokoleniowy majątku** ← nowa, **DAF** ← nowa
- **AI w organizacjach** — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering, **RODO i dane wrażliwe** ← nowa, **Evale** ← nowa, **Context layer organizacji** ← nowa, **LLM Wiki** ← nowa
- **Komunikacja i digital campaigning** — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, Higiena listy

**Ostatnia operacja — trzy nowe strony (2026-07-06), wszystkie czerwone linki ≥2 z backlogu domknięte:**
(1) **Transfer międzypokoleniowy majątku** — 5 źródeł (Giving USA 2026 — zapisy +17% r/r; Nonprofit of 2030 — 124 bln USD do 2045; CauseVox Planned Giving — 4 formy + Legacy Society; Beyond the Ask/FreeWill — luka stewardshipu 53%, zapisy 23,7% datków osobistych; Generational Remix — dziedzice/DAF 42% milenialsów). Czerwone linki w Pledge program (2×) i Pokolenia darczyńców zrealizowane; nowy świadomy czerwony link **[[DAF]]** → próg 2 incoming (Major gifts + Transfer).
(2) **RODO i dane wrażliwe** — 7 źródeł (AI Act & RODO przewodnik Krzywickiej — 8 kroków compliance, kary 4%+7%; 6 pytań Maciejewicz/Sektor 3.0 — DPIA, human-in-the-loop, ToS jako umowa; poradnik prywatności Śliwowskiego — anonimizacja, modele lokalne; webinar Chrobok/Porembiński — Shadow AI 60%, 4 poziomy narzędzi, 5 pytań do dostawcy/DPA; Hidden Privacy Trap Voty — transkrypcje, strefy bez AI; Stanford/King — 6/6 firm domyślnie trenuje na rozmowach; wPraktyce.AI — „model vs wiedza", paradoks bezpieczeństwa). Czerwone linki w AI governance i Higienie listy zrealizowane; nowy świadomy czerwony link **[[AI Act]]** (1 incoming).
(3) **DAF** — 5 źródeł (Civic Shout/IRC — 6× wzrost do 54 mld USD, Daffy/mid-level, DAF Day, DAFpay; Veritus — 23% darowizn indywidualnych USA, soft credit, audyt kwartalny, KPI gift processors; CauseVox — definicja, 4 kroki, niuanse pledges/gale; RKD — „chronicznie niewykorzystany kanał", edukacja całoroczna; Generational Remix — 42% milenialsów). Czerwone linki w Major gifts i Transferze zrealizowane; strona bez nowych czerwonych linków; relevance średnia (mechanizm USA — dla Polski radar, nie wdrożenie).
(4) **Evale** — pierwszy klaster-kandydat domknięty (operacja Query, nie czerwony link); masa krytyczna potwierdzona recallem: 6 źródeł (transkrypt Jones-Rooy — „czy liczba jest dobra", human as a judge, token maxing; Husain ×2 — error analysis ~100 śladów, open/axial coding, LLM-as-judge binarny/kalibrowany, TPR/TNR, traces; Anthropic skill-creator — capability uplift vs encoded preference, benchmark mode, comparator agents; Sullivan — 4 tryby błędów analizy, VERIFIED/PARAPHRASE/NOT FOUND, few-shot calibration; 9X — evale jako warunek POC→produkcja). Dodano 4 linki przychodzące zgodnie z planem: Wdrażanie AI, Agentic AI, Context engineering (częściowa odpowiedź na tamtejsze otwarte pytanie), AI governance. Bez nowych czerwonych linków.
(5) **Context layer organizacji** — drugi klaster-kandydat domknięty, wydzielenie z mechanizmu 8 Context engineering (warunek ≥2 incoming spełniony: Context engineering + Evale). 7 źródeł (Jones-Rooy — boil the ocean, odpytywanie archiwum, voice memo; Nadella — human+token capital, learning loop, suwerenność modelu, „nie zlecisz uczenia się"; Roberts — SCOPE, 20h→20min, analogia pracownika; Tectonica — struktura bije wolumen, 3 filary jakości danych; Neider — data strategy = mission strategy, 5 filarów suwerenności, no-access mindset; Bush — master context folder 8 dokumentów, „What Good Looks Like" vault; Acker/Wilkowski — suwerenność funkcjonalna platform jako kontrapunkt). Strona rozstrzyga napięcie „zalej ocean" vs „struktura bije wolumen" (różne piętra: archiwum jakościowe surowe + dane operacyjne czyste). Mechanizm 8 w Context engineering odsyła teraz do wydzielonej strony.
(6) **LLM Wiki** — czerwony link ≥2 (RAG + Context layer, próg osiągnięty tego samego dnia) domknięty. 4 źródła (Gökçe — L1/L2, schema jako kontrakt, ingest 5 faz, lint z auto-fix; Lipowczan — 3 warstwy Karpathy'ego, progressive disclosure 3 indeksów i 30× mniej kontekstu, 4 workflow, CLAUDE.md ręcznie wg ETH Zurich, git jako siatka; Yu — RAG vs wiki bezstanowe/kumulatywne, agregacja vs atomizacja, Model Collapse; Partisan — governance Wikipedii: proweniencja, logi, człowiek decyduje, slow capture). Czerwone linki w RAG i Context layer zrealizowane; bez nowych czerwonych linków. Strona autoreferencyjna: Galaxy/ = implementacja wzorca; z niej wynika brakujący mechanizm vaultu — **contradiction detection przy ingest** (zanotowany w Zastosowaniu i Otwartych pytaniach).
**Cleanup 2026-07-06:** usunięto duplikat „The Nonprofit of 2030" — wersja 2026-06-14 (bez `published`) skasowana z Resources + Archives + index; kanoniczna została 2026-06-08 (cytowana przez Wdrażanie AI). Przy okazji naprawiono wpis indeksu „2026-06-03 ANALYSIS Creators…" — jego opis (M+R, creator playbook) był doklejony do wpisu duplikatu; przywrócony na miejsce.

**Następny krok:** backlog ≥2 znów pusty. Kandydaci: (a) klastry — **Ghostwriting/marka osobista**, **AI jako współpracownik/digital workforce** (≥4 źródła o *organizacji* agentów), **Suwerenność technologiczna/europejskie alternatywy**; (b) przy najbliższej edycji stron dorzucić drugi incoming **Mobilizacji cyfrowej** (z Higieny listy lub Newslettera) albo **AI Act** (z Wdrażania AI lub Agentic AI); (c) operacyjnie: rozważyć wdrożenie **contradiction detection przy ingest** (wniosek ze strony LLM Wiki) do pluginów `*-to-notes`.

**Klastry-kandydaci na nowe strony (z przeglądu 2026-06-22, akt. 2026-07-06):** Ghostwriting / marka osobista; Suwerenność technologiczna / europejskie alternatywy (linkowana z Owned vs rented). **Propozycje z transkryptu Jones-Rooy — punkt wyjścia: `Resources/2026-06-24 How a Former NYU Professor Uses Claude Code.md`:**
- ~~**Evale / „skąd wiesz, że jest dobrze"**~~ — **domknięty 2026-07-06** jako strona `2026-07-06 Evale` (6 źródeł, 4 planowane incoming zrealizowane).
- ~~**Context layer organizacji**~~ — **domknięty 2026-07-06** jako strona `2026-07-06 Context layer organizacji` (7 źródeł; wydzielenie z mechanizmu 8 Context engineering, 2 incoming: Context engineering + Evale).
- **AI jako współpracownik / digital workforce** — wielo­agentowa struktura org (chief of staff → dyrektorzy → specjaliści → watchdog), agent-jako-plik, meta-prompting. Na razie mechanizm 8 Agentic AI; osobna strona dopiero, gdy będzie ≥4 źródła o *organizacji* agentów (nie samej technologii).

**Czerwone linki — backlog** (próg napisania = **≥2 incoming**, liczniki przeliczone `grep`-em 2026-07-06): Mobilizacja cyfrowa (1 — drugi incoming naturalnie z Higieny listy lub Newslettera), AI Act (1 — z RODO i dane wrażliwe; regulacja-pojęcie, nie news), Suwerenność technologiczna (1), Public Narrative (1), Sprawczość organizacyjna (1), Wizualizacja danych (1), Harness i scaffolding (1). ~~Higiena listy~~ — domknięta 2026-06-29. ~~Transfer międzypokoleniowy majątku~~, ~~RODO i dane wrażliwe~~, ~~DAF~~, ~~LLM Wiki~~ — domknięte 2026-07-06. Narzędzia/organizacje (CRM, Make.com, LLM, Blackbaud, Ollama) świadomie poza Galaxy — to nie pojęcia.

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
