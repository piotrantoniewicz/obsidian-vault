# Vault Piotr — instrukcje dla Claude

## Struktura

```
Piotr/
├── Inbox/        surowe webclipy z Web Clipper — czekają na przetworzenie
├── Archives/     oryginały po przetworzeniu — tylko do odczytu, nigdy nie modyfikuj
├── Resources/    przetworzone notatki (artykuły, newslettery, raporty)
│   └── index.md  katalog wszystkich notatek — czytaj jako pierwsze przy wyszukiwaniu
├── Attachments/  pliki binarne (PDF, obrazy)
├── Galaxy/       encyklopedia pojęć — syntezy łączące wiele notatek z Resources/
├── Projects/     przedsięwzięcia z celem i terminem — notatki-huby (MOC)
├── Areas/        stałe odpowiedzialności i role — notatki-huby (MOC)
├── Templates/    szablony notatek
└── References/   — w budowie
```

Szczegółowe formaty notatek i procedury poszczególnych folderów ładują się automatycznie z `.claude/rules/` przy pracy z plikami danego folderu: `resources.md` (format Resources/ + praca z index.md), `galaxy.md` (format Galaxy/, walidacja wikilinków, liczniki czerwonych linków, operacje Karpathy'ego), `projects-areas.md` (PARA: routing, relacje, formaty).

## Zasady

- `Archives/` i `Attachments/` są tylko do odczytu — nigdy tam nie pisz ani nie edytuj
- Przy każdym pytaniu o vault zacznij od `Resources/index.md` — to mapa 2000+ notatek
- Nowe notatki trafiają do `Resources/`, nazwa: `YYYY-MM-DD Tytuł artykułu.md`
- **Znak `#` jest zakazany w nazwach plików** — Obsidian traktuje `#` w wikilinku jako separator nagłówka, co łamie nawigację. Zamiast `#41` używaj `nr41`.
- Po dodaniu notatki do `Resources/` dopisz wpis do `Resources/index.md` w formacie:
  `- [[YYYY-MM-DD Tytuł]] — jednozdaniowy opis co zawiera`
- **Terminologia: zawsze pisz „organizacje społeczne" zamiast „NGO" / „organizacje pozarządowe"** — we wszystkich notatkach, syntezach, hubach i przy każdym zapisywaniu treści. **Wyjątki (oryginalne brzmienie zostaje):** (1) surowe pliki trafiające do `Inbox/` (webclipy, oryginały) — podmieniaj dopiero przy przetwarzaniu do `Resources/`, `Galaxy/`, `Projects/`, `Areas/`; (2) oryginalne tytuły maili, clipów, artykułów itp. — jeśli zawierają „NGO" / „organizacje pozarządowe", zostawiaj je bez zmian (nie przepisujemy cudzych tytułów).

## Reguła routingu — gdzie trafia notatka

1. Czy to **treść/wiedza** (artykuł, raport, newsletter, pojęcie)? → `Resources/` (źródło) lub `Galaxy/` (synteza).
2. Czy to **przedsięwzięcie z konkretnym celem i momentem zakończenia** (data albo jasne „gotowe")? → `Projects/`.
3. Czy to **trwała odpowiedzialność lub rola bez końca**, którą utrzymujesz na pewnym standardzie? → `Areas/`.

Rozstrzygnięcie Projects vs Areas i formaty hubów: `.claude/rules/projects-areas.md`.

## Wyszukiwanie w vaultcie (qmd)

Vault jest zaindeksowany w qmd (kolekcja `obsidian`, `**/*.md`, obejmuje całość). Zasady:

- **Domyślnie `qmd query "<fraza>" -n 15`** — 15 wyników daje szeroki kontekst do syntezy. Do szerokiego zbierania źródeł podnoś: `-n 25 -C 120` (większa pula kandydatów do rerankingu).
- Wyszukiwania zawężaj do vaultu: `-c obsidian` (druga kolekcja `Ghostwriting` jest osobna).
- `qmd query` = hybryda (expansion + BM25 + wektory + reranking); `qmd search` = szybki BM25 bez LLM; `qmd vsearch` = czysto semantyczny (łapie notatki o tym samym znaczeniu, innym słownictwie).
- Po sesji pisania w vaultcie: `qmd update` + `qmd embed`, żeby nowe strony były wyszukiwalne następnym razem.

### Archives vs Resources — oryginał (głębia) vs synteza (cytowanie)

`Archives/` i `Resources/` **nie są duplikatami**: Archives to pełny oryginał artykułu (dłuższy, w języku oryginału — często angielskim, surowe dane i cytaty), Resources to skondensowana polska synteza. Dzielą tytuł/nazwę pliku, ale różnią się treścią. Dlatego:

- **Nie wykluczaj Archives z wyszukiwania** — pełny tekst i język oryginału zwiększają recall (łapią to, co synteza wycięła; jedyna warstwa anglojęzycznego dopasowania).
- **Reguła dedupu po tytule:** gdy qmd zwróci tę samą nazwę z `Archives/` i `Resources/`, traktuj je jako **jeden temat**. Do `sources`/cytowania bierz **wersję z Resources/**; oryginał z Archives/ otwieraj po detale, dane i dosłowne cytaty przy pisaniu.
- Dwuwarstwowo: **Resources = szerokość + cytowanie, Archives = głębia.**

## Relevance — zasady oceny

Relevance oceniaj na podstawie profilu właściciela vaultu: freelance konsultant i trener organizacji społecznych, specjalizacja w AI, automatyzacji, fundraisingu, digital campaigningu i ghostwritingu.

- `wysoka` — bezpośrednio przydatne w aktywnych projektach: organizacje społeczne, fundraising, digital campaigning, AI dla organizacji, automatyzacja
- `średnia` — ogólnie użyteczne, może się przydać: marketing, strategia, komunikacja, narzędzia
- `niska` — marginalne znaczenie dla profilu właściciela

## Tagi — zamknięta lista

Tagi obowiązują we wszystkich notatkach (Resources/, Galaxy/, Projects/, Areas/). Zasady:

- Max 3 tagi na notatkę
- Wyłącznie z tej listy — nie twórz nowych tagów

```
automatyzacja        szkolenia-AI         strategia-AI
ghostwriting         fundraising          framing
organizacje-społeczne  narzędzia-AI       LLM
prompt-engineering   vibe-coding          produkty-cyfrowe
content-marketing    trendy-AI            digital-campaigning
context-engineering  strategia-organizacji
```

## Szablony (`Templates/`)

Frontmatter każdego szablonu ma puste pola dat — wypełnia je plugin przy tworzeniu notatki albo użytkownik ręcznie. Tokeny `{{title}}`/`{{date:YYYY-MM-DD}}` występują tylko w treści (nie w properties).

| Szablon | `categories` | Folder docelowy | Do czego |
|---|---|---|---|
| `Clippings.md` | Clippings | `Resources/` | webclip z artykułu (plugin `/clippings-to-notes:clip`) |
| `Emails.md` | Emails | `Resources/` | newsletter / mail (plugin `/emails-to-notes:process`) |
| `Reports.md` | Reports | `Resources/` | raport PDF (plugin `/pdfs-to-notes:extract`) |
| `LinkedIn.md` | LinkedIn | `Resources/` | post LinkedIn (plugin `/linkedin-to-notes:save`) |
| `Concepts.md` | Concept | `Galaxy/` | nota pojęciowa (synteza z wielu źródeł) |
| `Projects.md` | Project | `Projects/` | przedsięwzięcie z celem i terminem (hub/MOC) |
| `Areas.md` | Area | `Areas/` | stała odpowiedzialność / rola (hub/MOC) |

Cztery pierwsze (Clippings/Emails/Reports/LinkedIn) to wzory referencyjne — pluginy `*-to-notes` generują treść własnym promptem i wpisują realne wartości frontmatteru. Trzy pozostałe (Concepts/Projects/Areas) są do ręcznego wstawiania.

## Pluginy

| Komenda | Źródło | Cel |
|---|---|---|
| `/clippings-to-notes:clip` | `Inbox/` | przetwarza clipy → `Resources/` + `Archives/` |
| `/emails-to-notes:process <etykieta>` | Gmail | newslettery → `Resources/` |
| `/pdfs-to-notes:extract [podfolder]` | `~/Documents/Email/` | raporty PDF → `Resources/` |
| `/linkedin-to-notes:save` | wklejony post LinkedIn | post → `Resources/` |
| `/index:update vault` | `Resources/` | weryfikacja i naprawa `Resources/index.md` |
| `/galaxy:ingest [notatka\|dni]` | nowe notatki w `Resources/` | aktualizacja istniejących stron `Galaxy/` + flagowanie sprzeczności |
| `/galaxy:query <pytanie>` | `Galaxy/` + `Resources/` | odpowiedź z cytowaniami; wartościowa synteza → propozycja utrwalenia |
| `/galaxy:pisz <pojęcie>` | `Resources/` (3 kanały recall) | nowa strona pojęciowa `Galaxy/` + indeks + liczniki |
| `/galaxy:lint` | `Galaxy/` | miesięczny health-check: sieroty, czerwone linki, zepsute wikilinki, format |
