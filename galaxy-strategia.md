# Strategia rozbudowy Galaxy/ — 2026-08-17 (ingest: 10 notatek 31.07→02.08 → 12 stron)

*Konwencja: data w tytule H1 = data ostatniej istotnej aktualizacji tego pliku. Przy każdej zmianie (nowe pojęcia, zamknięta fala, korekta planu) zaktualizuj datę w tytule.*

> **Reguła dziennika:** sekcja „Gdzie jesteśmy" to **jeden, nadpisywany** snapshot bieżącego stanu — **nie** rosnący log dopisków. Przy każdej sesji **nadpisz jej treść** (liczba stron, ostatnia operacja, następny krok, backlog), zamiast dopisywać kolejny akapit „Dopisek RRRR-MM-DD". Historię trzymają same notatki, `git` i `Galaxy/index.md`.

## Gdzie jesteśmy (akt. 2026-08-17)

**Galaxy/ = 30 stron** w trzech gęsto połączonych działach indeksu:
- **Fundraising** — Tożsamość darczyńcy, Recurring giving, Stewardship, Peer-to-peer fundraising, Pledge program, Transparentność operacyjna, Major gifts, Pokolenia darczyńców, Transfer międzypokoleniowy majątku, DAF
- **AI w organizacjach** — Wdrażanie AI w organizacji społecznej, AI governance, Agentic AI, RAG, Context engineering, Prompt engineering, RODO i dane wrażliwe, Evale, Context layer organizacji, LLM Wiki, Suwerenność technologiczna, AI Act
- **Komunikacja i digital campaigning** — Email deliverability, Framing, Storytelling oparty na danych, Newsletter jako kanał, Widoczność w AI search (GEO/AEO), Owned vs rented audience, Higiena listy, Ghostwriting

**Ostatnia operacja — ingest 31.07→02.08 (2026-08-17):** domyślne okno komendy (notatki nowsze niż data z H1) było **puste**; zakres wybrał Piotr — **10 notatek z okna mtime 2026-07-31 → 2026-08-02**, druga z trzech fal domykających zaległość lipcową. Wynik: **12 stron zaktualizowanych, 0 nowych stron, 15 nowych mechanizmów, 0 notatek bez trafienia** (każda z 10 notatek trafiła w co najmniej jedną stronę, sześć w dwie lub trzy — chain updates). Największe przyrosty: **Recurring giving** (+1 duży: branding programu cyklicznego — nazwa, poziomy i osobna tożsamość e-mailowa jako dźwignia retencji; case IRC „Rescue Collective” 45→51% / 70→72% / 66→70% / 50→54% oraz WCK „Kitchen Core” z czterema filarami i pięciokrokowym *Monthly Giving Builder*; plus blok benchmarków FEP 2021–2025 z dwiema sprzecznościami). **Ghostwriting** (+2: audyt konta wzorcowego i *credibility statement* jako hook — case Chris Donnelly, 1,25 mln followersów, 34 posty w 30 dni, 31 z 34 z CTA, marka przeżywa pivot oferty; „origin story” jako filtr redakcyjny — anegdota jest postem, nie tłem). **AI governance** (+2: „najpierw daj zaufanie” jako governance wyprzedzające regulację; „czy musimy to zbierać” zamiast „czy damy radę to przeanalizować” — minimalizacja danych jako decyzja zarządcza). **Newsletter jako kanał** (+2: newsletter a SEO — brak wpływu bezpośredniego, łańcuch pośredni i pięć błędów; kontrapunkt „newsletter nie jest warunkiem koniecznym sprzedaży”). Po +1: **Stewardship** (uznanie to treść, nie gadżety — ~40% newslettery w ankiecie IRC; onboarding po launchu i segmentacja na 8 grup u WCK), **Tożsamość darczyńcy** (od „wybawcy” do partnera — nazwa i poziom programu jako nośnik tożsamości), **Email deliverability** (*context box* — pięć warunków i reguła „jeśli nie precyzyjnie, to wcale”), **Widoczność w AI search** (kilkaset wzmianek zakorzenia markę w danych treningowych; 25,6% pokrycia cytowań między trybami ChatGPT; kara Google za AI-content), **Owned vs rented audience** (lejek bez własnego kanału — LinkedIn/X → Calendly, YouTube → Skool), **Suwerenność technologiczna** (*Kami* — mały, lokalny, odwoływalny agent; *write-back*, *talk-page protocol*, open-weight ~3% od frontier, *forking the government*), **Framing** („misja, nie wyścig” jako kadr budujący sojusze), **Wdrażanie AI w organizacji społecznej** (transformacji nie da się kupić — cztery nawyki do złamania, cztery zagrożenia dla zdolności mówienia „nie”, zbiorowe przyzwolenie).

**Sekcji „Powiązane pojęcia” nie zmieniano na żadnej stronie** — wszystkie nowe wikilinki w treści to albo istniejące strony Galaxy, albo notatki Resources, albo osoby i narzędzia świadomie poza Galaxy (Audrey Tang, Meenakshi Das, Al Iverson, Dana Snyder, Josh Spector, LinkedIn, Calendly, Skool, ChatGPT). Backlog czerwonych linków **bez zmian**, przeliczony `grep`-em 2026-08-17 (Sprawczość organizacyjna 2, Marka osobista 2, pozostałe po 1). Walidacja wikilinków przeszła na **całym** katalogu Galaxy/: **0 zepsutych linków datowanych**.

**Uwaga techniczna:** `qmd update && qmd embed` **nie zostało uruchomione** — CLI `qmd` nie jest dostępne w środowisku, z którego prowadzono tę sesję (most do maszyny udostępnia tylko `qmd query/get/status`). Do uruchomienia ręcznie w vaultcie przed następnym wyszukiwaniem.

*Wcześniej (skrót):* ingest 33 notatek z okna 02–03.08 → 21 stron, 43 mechanizmy; ingest 03–04.08 → 9 stron, 9 mechanizmów; ingest 41 notatek z okna 05–09.08 → 18 stron, 36 mechanizmów; ingest ECF ×5 → 4 strony. Szczegóły w historii `git` i w samych stronach.

**Do decyzji Piotra — otwarte sprzeczności i napięcia (1–5 z fali 05–09.08, 6–7 z fali 03–04.08, 8–10 z fali 02–03.08, 11–13 z tej fali):**
1. **Retencja nowych darczyńców: trzy różne liczby na to samo zjawisko.** Stewardship mech. 1 podaje **14–19%**, DonorDock (2026-07-30) — „tylko ok. **19%** nowych darczyńców daje drugi raz”, a Stewardship mech. 9 za FEP Q1 2026 — konwersja nowych na powtarzających **7,1%**. Możliwe, że mierzą różne rzeczy (retencja pierwszoroczna vs konwersja w kwartale), ale żadne źródło tego nie różnicuje.
2. **Eskalacja sprzeczności „42,9% vs 25,8%”.** Materiał DonorDock z 30 lipca 2026 nadal operuje **42,9%** jako aktualną średnią FEP — stara kotwica żyje w obiegu równolegle z nową. Hipoteza o zmianie metodologii FEP wzmocniona, ale niepotwierdzona.
3. **Cztery konkurencyjne frameworki gotowości do AI** — cztery filary Gatmaitana (z *cultural alignment*), pięć filarów Neidera (bez tej warstwy), pięć priorytetów Harfoush (warstwa kulturowa w centrum) i polski, operacyjny zestaw AI Leaders (pięć pytań + trzy warunki skalowania). Cztery ramy na jedną rozmowę doradczą to o trzy za dużo. Decyzja: który zestaw jest kanoniczny w ofercie, czy scalać w jeden autorski.
4. **Dezaktualizacja listy: 22–30% (B2B) vs 12–16% (organizacje społeczne)** — dwie kotwice obok siebie na jednej stronie. Decyzja: która jest domyślna.
5. **Napięcie „analog vs data readiness”** — papierowy planer i Google Alerts (Stewardship mech. 11) vs uporządkowany CRM jako warunek dźwigni AI (Agentic AI mech. 12, Recurring giving mech. 8); *lapse risk score* (Stewardship mech. 14) stoi po obu stronach naraz i jest najbliższą dostępną podpowiedzią, gdzie przebiega granica.
6. **Kolejność wysyłki w warmupie: od najbardziej zaangażowanych czy losowo?** Email deliverability mech. 8(c) i 10 vs mech. 16 za *Send It Right*. Żadne źródło ich nie godzi.
7. **„Człowiek ponad pętlą” vs *System 2*: kiedy wolniej jest lepiej.** Agentic AI mech. 3 vs Wdrażanie AI mech. 18 i 19 — trzy odpowiedzi, wciąż brak progu przełączającego tryb.
8. **Gniew czy nadzieja: która emocja mobilizuje?** Framing mech. 8 (RCT Social Change Lab — gniew) vs mech. 17 (ECDA — nadzieja i sprawczość). *Akt. 2026-08-17:* nowy mech. 20 („misja, nie wyścig”, Audrey Tang) dokłada **trzeci rejestr** — sprawczość **bez adresata-przeciwnika**, kadr, który ma rekrutować, a nie mobilizować przeciw. Trzy rejestry, nadal brak reguły przełączania.
9. **Jakość vs wolumen na kanale wynajętym.** Ghostwriting mech. 12–13 (pogłębianie jednego kanału) vs mech. 20 (Alvin Foo, 16 postów dziennie). *Akt. 2026-08-17:* nowy mech. 22 (Donnelly — **34 posty w 30 dni**, 31 z 34 z CTA, konto 1,25 mln) to **drugi niezależny case po stronie wolumenu**, i tym razem w niszy biznesowo-eksperckiej, nie newsowej — co osłabia dotychczasowe wyjaśnienie „to działa tylko przy wysokim tempie odświeżania tematu”. Napięcie zaostrzone, decyzja pilniejsza.
10. **Czy „bariera psychologiczna” wytrzymuje dane sektorowe?** Wdrażanie AI mech. 9 (Jones-Rooy — bariera psychologiczna) vs mech. 23 (Google for Nonprofits: 86% widzi potencjał, 49% korzysta; bariery finansowe i szkoleniowe). *Akt. 2026-08-17:* nowy mech. 25 (Das) dokłada **trzecią diagnozę — barierę systemową i kulturową** (norma zespołu, brak zbiorowego przyzwolenia na odmowę). Trzy diagnozy wymagają trzech różnych interwencji; decyzja: którą stawiać pierwszą w rozmowie z organizacją.
11. **NOWE — 7,9% czy 30%: ilu darczyńców naprawdę daje cyklicznie?** Recurring giving: dane FEP 2021–2025 (za *State of Recurring Giving*) podają **udział darczyńców cyklicznych w sektorze 6,6% → 7,9%** i **medianę 4% na organizację**, podczas gdy profil GivingPulse na tej samej stronie mówi, że **30% darczyńców pieniężnych w USA daje miesięcznie i automatycznie**. To pomiar po stronie **organizacji** (rekordy CRM) vs **deklaracja darczyńcy** w ankiecie — prawdopodobnie różne denominatory, ale żadne źródło tego nie różnicuje, a rozbieżność jest czterokrotna. Decyzja: którą liczbę cytować w rozmowie z zarządem i jak ją zastrzegać.
12. **NOWE — wartość roczna darczyńcy cyklicznego: 3×, +42% czy 938 USD?** Na jednej stronie żyją teraz trzy niesprowadzalne do siebie kotwice: **mediana 275 USD vs 100 USD rocznie (prawie 3×)** za *State of Recurring Giving*, **+42% rocznie** (CauseVox, mech. 7) oraz **938 USD rocznie / LTV 7 288 vs 3 607 USD** (Neon One, mech. 1). Każda brzmi przekonująco osobno, ale razem podważają się przy pierwszym pytaniu „skąd ta liczba”. Decyzja: jedna para liczb kanoniczna w materiałach, reszta jako przypis.
13. **NOWE — czy własna lista jest warunkiem, czy wzmacniaczem?** Newsletter jako kanał mech. 1 i Owned vs rented mech. 1–4 stoją na tym, że kanał własny jest **warunkiem odporności**; nowe mechanizmy (Newsletter mech. 16, Owned vs rented mech. 15, za Tribe Digital) pokazują **działający pełny lejek bez maila** (LinkedIn/X → Calendly, YouTube → Skool), w którym mail jest remarketingiem i osobnym produktem zaufania. Żadne źródło nie podaje **progu** — skali, cyklu sprzedaży, typu oferty — przy którym odpowiedź się zmienia. Dla organizacji społecznej ryzyko jest przy tym asymetryczne wobec biznesu jednoosobowego (utrata konta = utrata bazy darczyńców, nie tylko lejka sprzedażowego), co jest najmocniejszym argumentem, żeby **nie** przenosić tej rekomendacji wprost na klientów.

**Następny krok:** (a) **dokończyć zaległość** — po tej fali pozostaje **36 notatek z okna 2026-07-29 → 2026-07-31**, ostatnia fala domykająca lipiec; (b) uruchomić ręcznie **`qmd update && qmd embed`** (patrz uwaga techniczna wyżej) — bez tego zmiany z tej fali nie będą wyszukiwalne; (c) **backlog ≥2 bez zmian**: **Sprawczość organizacyjna** (2) i **Marka osobista** (2) nadal jedynymi kandydatami progowymi, przy czym **Marka osobista** dostała w tej fali kolejne dwa udokumentowania źródłowe (case Donnelly — marka przeżywa pivot oferty; „celem jest być znanym z rozwiązywania konkretnego problemu”) i pozostaje najlepiej uzasadnionym czerwonym linkiem w backlogu; (d) **Kampania końcoworoczna** nadal kandydatem numer jeden do `/galaxy:pisz` (masa ~55) — ta fala jej nie zmieniła; (e) do rozstrzygnięcia trzy nowe napięcia (7,9% vs 30%, trzy kotwice wartości rocznej, lista jako warunek vs wzmacniacz) — patrz wyżej.

**Klastry-kandydaci na nowe strony (z przeglądu 2026-06-22, akt. 2026-08-17):**
- **Kampania końcoworoczna / year-end appeal** — **masa potwierdzona: ~55 trafień**, cztery źródła bez pełnego miejsca na istniejących stronach; kalendarz i rozkład wysyłek nadal bez własnej strony. **Kandydat numer jeden do `/galaxy:pisz`.** Bez zmian w tej fali.
- **Przywództwo i zarząd w organizacji społecznej** — **masa ~32 („przywództwo/lider/leadership") + ~60 („zarząd/rada/board")** w `Resources/index.md`. *Akt. 2026-08-17:* trzy kolejne źródła, wszystkie wchłonięte — *Is Your Nonprofit Stuck on Financial Autopilot?* (DILLY, gatekeeper liczb → Transparentność mech. 12), *Why Employees Resist AI* (pięć taktów zaufania, opór jako brak bezpieczeństwa decyzyjnego → Wdrażanie AI mech. 19), *AI in HR / Harfoush* (agenda human-centered, burnout jako problem przywódczy → Wdrażanie AI mech. 22). Klaster rośnie, ale materiał przestał być bezdomny — decyzja: pisać teraz z masy, czy czekać na źródło, które nigdzie nie wsiąknie.
- **Wydarzenia fundraisingowe (eventy) — NOWY, słaba masa (~6 wąsko, ~35 szeroko).** Z tej fali dwa źródła: *The First Fundraiser is the Doorway to a Future Community* (cztery filary, jedna historia, segment to convert) i *What Years in Fundraising Events Taught Me About Community* (okno post-eventowe, sześć pytań relacyjnych, „nie każdy sponsor chce rozgłosu") — oba wchłonięte jako P2P mech. 8–9 i Stewardship mech. 15. Za mało na osobną stronę; obserwować, czy nie przerośnie P2P.
- **Optymalizacja strony i formularza darowizn — NOWY, słaba masa (~11 trafień).** Z tej fali jedno źródło **bez trafienia w Galaxy**: *NextAfter Minute 16 — Make Giving Easier: A Sticky Nav That Drives Donations* (sticky nav na mobile → **+72,4% kliknięć w Donate przy 99% poziomie ufności**, test A/B CaringBridge). Materiał sąsiaduje z Transparentnością mech. 10 („strona donacyjna jako egzamin z zaufania"), ale to inna warstwa — konwersja i UX, nie zaufanie. Obserwować; przy 3–4 kolejnych źródłach kandydat realny.
- **SMS / texting jako kanał** — ~23 trafienia; bez zmian.
- **Branding programu dawania cyklicznego (nazwa, poziomy, tożsamość per tier) — NOWY, obserwować.** Fala 31.07→02.08 dołożyła dwa mocne case'y (IRC „Rescue Collective”, WCK „Kitchen Core”) — oba wsiąkły w Recurring giving mech. 9 i Tożsamość darczyńcy mech. 9, więc materiał **nie jest bezdomny**; osobna strona miałaby sens dopiero, gdyby Recurring giving zaczęło pękać w szwach.
- **Dywersyfikacja przychodów / odporność finansowa** — ≥6 źródeł; ta fala dołożyła wątek **kultury finansowej i governance liczb** (DILLY → Transparentność mech. 12), ale sam temat przychodu i płynności nadal bez strony.
- **Ludzie w organizacji: wypalenie, rotacja, sukcesja** — **~22 trafienia**. Ta fala dołożyła burnout jako problem przywódczy (Wdrażanie AI mech. 22) i dane o upskillingu (<4% przekwalifikowanych, 24% pewności kompetencji). Sąsiaduje z klastrem przywództwa — do rozstrzygnięcia, czy to jedna strona, czy dwie.
- **Vibe-coding** — ~3 trafienia wąsko, ~92 szeroko. Ta fala dołożyła *landing page z ofertą w Claude Code* — wchłonięte jako Context engineering mech. 9. Nadal za wąsko na stronę.
- **Monetyzacja wiedzy / produkty cyfrowe** — słaba masa (~6). Bez zmian.
- **Prawa autorskie, dane treningowe i ekstrakcja stylu** — słaba masa (~3), materiał gęsty. Ta fala dołożyła **destylację głosu** (Ghostwriting mech. 19) — nadal wzmianka, nie klaster.
- **Twórcy, influencerzy i „amplifierzy" w kampaniach** — ~36 trafień; nadal jako mechanizmy 6–8 w Owned vs rented. Ta fala dołożyła **trendjacking i wolumen** (Ghostwriting mech. 20, Owned vs rented mech. 14).
- **Centra danych AI, woda i energia** — **~22 trafienia**. Ta fala dołożyła **trzy** źródła naraz (koalicja ponad podziałami Social Change Lab, hałas w Michigan, aresztowanie w Kansas) plus dwa środowiskowe (pełny rachunek Olmo 3, apel ONZ) — wszystkie wchłonięte jako Suwerenność technologiczna mech. 15–16. Strona macierzysta ma teraz **cztery** mechanizmy o warstwie fizycznej (9, 13, 15, 16), co jest granicą jej pojemności. **Decyzja dojrzała do podjęcia: wydzielić osobną stronę o warstwie fizycznej AI czy dalej rozbudowywać Suwerenność.** **Dostępność cyfrowa (EAA / WCAG)** — ~9 trafień; jako mechanizm 8 w Newsletterze. **AI jako współpracownik / digital workforce** — ta fala dołożyła always-on orchestration i pięć ról McKinseya (Agentic AI mech. 15); obserwować. **Testowanie kampanii / holdout testing** — ~2 trafienia, bez zmian.
- ~~**Ghostwriting / marka osobista**~~ — Ghostwriting domknięty 2026-07-07; wątek **marka osobista** jako czerwony link o 2 incoming. ~~**Suwerenność technologiczna**~~ — 2026-07-07. ~~**AI Act**~~ — 2026-07-20. ~~**Evale**~~, ~~**Context layer organizacji**~~ — 2026-07-06.

**Czerwone linki — backlog** (próg napisania = **≥2 incoming**, liczniki przeliczone `grep`-em 2026-08-17, **bez zmian wobec 2026-08-16** — w tej fali nie modyfikowano żadnej sekcji „Powiązane pojęcia"): **Sprawczość organizacyjna (2 — Agentic AI + Suwerenność technologiczna → KANDYDAT)**, **Marka osobista (2 — Ghostwriting + Owned vs rented audience → KANDYDAT, najmocniej udokumentowany)**, Thought leadership (1 — z Ghostwritingu), AI Office (1 — z AI Act), Digital Omnibus (1 — z AI Act), Mobilizacja cyfrowa (1 — z Owned vs rented), Public Narrative (1 — z Framingu), Wizualizacja danych (1 — ze Storytellingu), Harness i scaffolding (1 — z Context engineeringu). ~~AI Act~~ — domknięty 2026-07-20. ~~Suwerenność technologiczna~~ — 2026-07-07. ~~Higiena listy~~ — 2026-06-29. ~~Transfer międzypokoleniowy majątku~~, ~~RODO i dane wrażliwe~~, ~~DAF~~, ~~LLM Wiki~~ — 2026-07-06. Narzędzia, osoby i organizacje (Capgemini, McKinsey, Social Change Lab, Sheila McKechnie Foundation, Better Fundraising, Google for Nonprofits, Olmo 3, Wispr Flow, Claude Code, Make.com, CRM i in.) świadomie poza Galaxy — to nie pojęcia.

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
