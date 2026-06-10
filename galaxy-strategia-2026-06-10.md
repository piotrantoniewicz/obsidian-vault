# Strategia rozbudowy Galaxy/ — 2026-06-10

## Stan wyjściowy

- **Resources/**: 2421 notatek, skatalogowanych w `Resources/index.md` (po audycie 2026-06-09 — kompletny, 4 duplikaty wpisów do wyczyszczenia)
- **Galaxy/**: 1 notatka — `[[2026-06-03 Tożsamość darczyńcy]]` — która już linkuje do 5 nieistniejących pojęć (czerwone linki = gotowy backlog)
- **qmd**: kolekcja `obsidian` (3765 plików, indeks świeży), wyszukiwanie hybrydowe BM25 + wektory + reranking — sprawdzone, zwraca trafne źródła z procentowym score

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

## Fala 1 — czerwone linki (5 pojęć, natychmiast)

Z `[[2026-06-03 Tożsamość darczyńcy]]`:

- [ ] **Recurring giving** (dawanie cykliczne) — qmd potwierdza bogaty materiał: Neon One 2026, GivingPulse, retention benchmarks
- [ ] **Stewardship** (opieka nad darczyńcą) — retencja 31.9%, konwersja 1→2 wpłata 25.84%, frameworki relacyjne
- [ ] **Peer-to-peer fundraising** — proxy trust, Pomagam.pl, model społecznościowy
- [ ] **Pledge program** (program zobowiązań)
- [ ] **Transparentność operacyjna**

Efekt: spójny klaster fundraisingowy — 6 stron gęsto połączonych wikilinkami, od razu widoczny w graph view.

## Fala 2 — klastry z rozkładu tagów (kolejne ~10 pojęć)

Rozkład tagów w Resources/ wskazuje masę krytyczną (liczba notatek z tagiem):

| Klaster | Notatek | Kandydaci na pojęcia |
|---|---|---|
| digital-campaigning | ~1070 | Email deliverability, Mobilizacja cyfrowa, Framing w kampaniach |
| organizacje-społeczne | ~910 | Wdrażanie AI w organizacji, Wellbeing w erze AI |
| fundraising | ~770 | Donor retention (jeśli nie wejdzie w Stewardship), Pokolenia darczyńców |
| strategia-AI | ~670 | Agency vs agents (sprawczość w org.), AI governance w NGO |
| narzędzia-AI / LLM | ~680 | RAG, Context engineering, Prompt engineering |
| content-marketing | ~690 | Newsletter jako kanał, Storytelling oparty na danych |

Przed każdą notatką: `qmd query` weryfikuje, czy klaster faktycznie ma ≥4–5 konkretnych źródeł, czy to tylko szum tagów.

## Fala 3 — rytm stały (operacje Karpathy'ego)

- **Ingest** (przy każdym przetwarzaniu Inbox/maili/PDF): po dodaniu notatki do Resources/ sprawdź `qmd vsearch "<temat notatki>"` ograniczone do Galaxy/ — zaktualizuj istniejące strony (`updated` + nowe źródło w `sources`), zamiast tworzyć nowe
- **Query** (ad hoc): wartościowa odpowiedź na pytanie → nowa strona lub rozszerzenie istniejącej
- **Lint** (co miesiąc):
  - sieroty: strony Galaxy/ bez linków przychodzących (`grep -rl "[[<nazwa>" --include="*.md"` po vaulcie)
  - czerwone linki: pojęcia linkowane ≥2 razy z różnych stron → priorytet do napisania
  - przeterminowane twierdzenia (statystyki starsze niż rok)

## Infrastruktura — do zrobienia raz

- [ ] **`Galaxy/index.md`** — analogicznie do Resources/index.md: sekcje tematyczne (Fundraising / AI w organizacjach / Komunikacja / Narzędzia i metody), wpis = `- [[pojęcie]] — definicja jednym zdaniem`. Przy 1 notatce to 2 minuty, przy 50 — niemożliwe do odtworzenia
- [ ] **Higiena Resources/index.md** — usunąć 4 duplikaty wpisów i 4 pary zduplikowanych plików (audyt 2026-06-09), żeby `sources` w Galaxy/ nie wskazywały na niejednoznaczne tytuły
- [ ] Po każdej sesji pisania Galaxy/: `qmd update`, żeby nowe strony były wyszukiwalne w następnej sesji

## Tempo i miara sukcesu

- **Tempo**: 2–3 pojęcia tygodniowo (jedna sesja z Claude = 1 fala mini: query → źródła → notatka → index)
- **Kwartał**: ~25–30 stron pokrywających klastry fundraising + AI w organizacjach
- **Miara jakości, nie ilości**: każda strona ma ≥4 źródła, ≥3 wikilinki do innych stron Galaxy/, sekcję zastosowania NGO. Strona, której nie da się zastosować w pracy konsultanta — nie powstaje.
