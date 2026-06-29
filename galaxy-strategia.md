# Strategia rozbudowy Galaxy/ — 2026-06-29

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-06-29)

**Galaxy/ = 21 stron** w trzech domkniętych, gęsto połączonych działach indeksu:
- **Fundraising** — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców
- **AI w organizacjach** — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering
- **Komunikacja i digital campaigning** — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, **Higiena listy** ← nowa

**Ostatnia operacja — przegląd re-source 2026-06-29 (w toku):** jednorazowy przegląd istniejących stron Galaxy/ nowym workflow zbierania źródeł (3 kanały recall). Dotąd wzbogacono **7 stron fundraisingowych**: Tożsamość darczyńcy, Pokolenia darczyńców, Stewardship, Recurring giving, Pledge program, Major gifts, Transparentność operacyjna (status per strona — patrz sekcja w `CLAUDE.md`). Bez nowych stron — Galaxy = 21. Najważniejsze efekty: atrybucja statystyk do *Giving Signals Report*, typologia trzech person (*Fundraising Fallacy*), case Chive 98% (Stewardship/Recurring), nowy mechanizm „kanał akwizycji przesądza o retencji", twarde dane Giving USA 2026 (megagifty 19,2 mld, zapisy +17%) w Major gifts/Pledge, naprawiony przeterminowany fakt w Major gifts (8,07 mld 2023 → 19,2 mld 2025). **Dwa czerwone linki przekroczyły próg ≥2** (RODO i dane wrażliwe; Transfer międzypokoleniowy majątku — drugi incoming z Pledge). `qmd update` + `embed` wykonywane po każdej turze; nowe wikilinki walidowane. Wcześniej tego samego dnia: domknięto stronę **Higiena listy**.

**Klastry-kandydaci na nowe strony (z przeglądu 2026-06-22, akt. 2026-06-26):** Ghostwriting / marka osobista; Suwerenność technologiczna / europejskie alternatywy (linkowana z Owned vs rented). **Nowe propozycje z transkryptu Jones-Rooy — punkt wyjścia: `Resources/2026-06-24 How a Former NYU Professor Uses Claude Code.md`:**
- **Evale / „skąd wiesz, że jest dobrze"** — definiowanie kryteriów jakości outputu AI (benchmark, kontekst, outcomes > outputs); najmocniejszy kandydat. Naturalne incoming: Wdrażanie AI (mech. 9), Agentic AI (nadzór above the loop / rubber-stamping), Context engineering (otwarte pytanie „jak zmierzyć jakość kontekstu"), AI governance. Domykać, gdy uzbiera się ≥4 źródła (eval/„co znaczy dobrze"/pomiar jakości) — transkrypt to źródło #1.
- **Context layer organizacji** — kandydat na *wydzielenie* z Context engineering, jeśli dorośnie: organizacyjna baza kontekstu (transkrypty, voice memo, archiwum) jako fosa i paliwo samouczącego się systemu. Na razie żyje jako mechanizm 8 Context engineering; wydzielić przy ≥2 incoming + osobnych źródłach.
- **AI jako współpracownik / digital workforce** — wielo­agentowa struktura org (chief of staff → dyrektorzy → specjaliści → watchdog), agent-jako-plik, meta-prompting. Na razie mechanizm 8 Agentic AI; osobna strona dopiero, gdy będzie ≥4 źródła o *organizacji* agentów (nie samej technologii).

**Następny krok (popyt):** **dwa** czerwone linki osiągnęły próg **≥2 incoming**: (1) **RODO i dane wrażliwe** (AI governance + Higiena listy — provenance/suppression/double opt-in jako praktyki zgodności); (2) **Transfer międzypokoleniowy majątku** (Pokolenia darczyńców + Pledge program — Wielki Transfer Bogactwa, zapisy testamentowe +17% r/r wg Giving USA 2026). Oba do napisania po zebraniu ≥4 źródeł — dla Transferu naturalna pula: Giving USA, Developing Major Donors and Planned Giving, Nonprofit of 2030, Major gifts/legacy. Pozostałe wiszą na 1: **Mobilizacja cyfrowa** (Owned vs rented — dorzucić drugi incoming, naturalnie z Higieny listy lub Newslettera). Z klastrów AI nadal najmocniejszy **Evale / „skąd wiesz, że jest dobrze"** (zbierać ≥4 źródła).

**Czerwone linki — backlog** (próg napisania = **≥2 incoming**, aktualne liczniki z 2026-06-29): **RODO i dane wrażliwe (2 ← próg osiągnięty, do napisania)**, **Transfer międzypokoleniowy majątku (2 ← próg osiągnięty, do napisania)**, Mobilizacja cyfrowa (1), Suwerenność technologiczna (1), Public Narrative (1), Sprawczość organizacyjna (1), Wizualizacja danych (1), LLM Wiki (1), Harness i scaffolding (1). ~~Higiena listy~~ — domknięta 2026-06-29. Narzędzia/organizacje (CRM, Make.com, LLM, Blackbaud, Ollama) świadomie poza Galaxy — to nie pojęcia.

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
