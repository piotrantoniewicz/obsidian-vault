# Strategia rozbudowy Galaxy/ — 2026-06-15

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-06-15)

**Galaxy/ = 18 stron** w trzech domkniętych, gęsto połączonych działach indeksu:
- **Fundraising** — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców
- **AI w organizacjach** — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering
- **Komunikacja i digital campaigning** — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał

**Ostatnia operacja — Lint 2026-06-15:** graf zdrowy, zero zerwanych linków, brak sierot (min. 2 linki przychodzące na stronę). Naprawiona 1 luka: Major gifts dolinkowany wstecz ze Stewardship i Pledge (1 → 3 incoming).

**Następny krok (popyt):** Mobilizacja cyfrowa (gałąź digital campaigning, bez czerwonego linku), Owned vs rented audience lub Higiena listy (awansują przy 2. wystąpieniu), Transfer międzypokoleniowy majątku (czerwony link z Pokoleń).

**Czerwone linki — backlog** (wszystkie ×1, próg napisania = **≥2 incoming**): Higiena listy, Owned vs rented audience, Transfer międzypokoleniowy majątku, Public Narrative, Sprawczość organizacyjna, RODO i dane wrażliwe, LLM Wiki, Wizualizacja danych, Harness i scaffolding. Narzędzia/organizacje (CRM, Make.com, LLM, Blackbaud, Ollama) świadomie poza Galaxy — to nie pojęcia.

## Zasada nadrzędna

Galaxy/ rośnie **od popytu, nie od podaży**. Nie przerabiamy Resources/ hurtowo na pojęcia — tworzymy stronę wtedy, gdy: (a) istnieje czerwony link, (b) klaster ma masę krytyczną źródeł, (c) padło pytanie, na które odpowiedź była syntezą wielu notatek (operacja Query z CLAUDE.md).

### Kryteria przyjęcia pojęcia do Galaxy/

1. **Min. 4–5 źródeł** w Resources/ (weryfikacja: `qmd query`)
2. **Pojęcie, nie news** — musi być aktualne za rok (mechanizm, framework, zjawisko; nie "premiera GPT-X")
3. **Relevance dla profilu**: NGO / fundraising / AI dla organizacji / digital campaigning / ghostwriting
4. Format i sekcje wg `CLAUDE.md` (type: concept, sources, definicja → mechanizmy → powiązane pojęcia → zastosowanie NGO → otwarte pytania)

## Workflow tworzenia notatki konceptowej (przepis qmd)

```bash
# 1. Zbierz kandydatów na źródła (hybrydowo, z rerankingiem)
qmd query "<pojęcie + kontekst>" -n 15

# 2. Doprecyzuj lukę lub wątek (czysty BM25, szybko, bez LLM)
qmd search "<frazy kluczowe>" -c obsidian

# 3. Pobierz treść wybranych notatek
qmd get qmd://obsidian/resources/<plik>.md
```

Zasady:
- **Źródła cytuj z `Resources/`, nie z `Archives/`** — qmd zwraca oba (duplikaty treści); w frontmatter `sources` zawsze wersja z Resources/
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
