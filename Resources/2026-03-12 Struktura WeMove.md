---
categories: Emails
published: 2026-03-12
created: 2026-03-12
labels: WeMove
relevance: wysoka
tags:
  - fundraising
  - digital-campaigning
  - organizacje-społeczne
---
# 2026-03-12 Struktura WeMove

## Synteza

WeMove Europe prowadzi wielowątkową komunikację mailową łączącą trzy odrębne typy wiadomości: kampanie petycyjne, zbiórki funduszy i raporty z wygranych kampanii — każdy z własną strukturą i logiką CTA. W analizowanym okresie (czerwiec 2025 – marzec 2026) wysłano 82 maile z częstotliwością ~2,1/tydzień, bez dziennych mailingów, ale z regularną obecnością przez cały tydzień (piątek dominuje z 26%). Charakterystyczna jest technika kampanijnych nazw nadawców: zamiast imienia osoby, sender przyjmuje rolę kampanii ("Stop monopolowi Google'a", "Elon musi zapłacić", "Niech Elon zapłaci") — co jest unikalną mechaniką budowania kontekstu jeszcze przed otwarciem wiadomości. Wysyłka koncentruje się w dwóch oknach: porannym (09:00–11:00) i popołudniowym (14:00–16:00), co sugeruje świadome targetowanie obu rytmów dnia. Każdy mail zawsze zamyka stopkę z przyciskiem "DORZUĆ SIĘ" — donacja jest domyślna, niezależnie od typu wiadomości.

## Wnioski

1. **Trzy typy maili z własną logiką CTA**: [[WeMove]] nie stosuje jednego szablonu — petycja ma inną strukturę niż fundraising, a raport z wygranej to osobny format. Warto wzorować się na tym przy projektowaniu sekwencji dla [[Otwarte Klatki]]: mail-wygrana jako osobny typ, nie tylko mail-apel.
2. **Kampanijna nazwa nadawcy jako preheader**: "Elon musi zapłacić", "Powstrzymajmy Trumpa", "Na straży praw kobiet" — to nie jest imię, to CTA w polu From. Innowacyjna technika [[digital-campaigning]] budująca kontekst kampanii przed otwarciem maila.
3. **Stopka z donacją jako stały element infrastruktury**: każdy mail — petycyjny, zwycięski, fundraisingowy — kończy się przyciskiem "DORZUĆ SIĘ". [[Fundraising]] jest wbudowany w interfejs, nie tylko w dedykowane maile zbiórkowe.

> "Taïme (Barcelona), Till (Brussels), Jessie (London) oraz cały zespół WeMove Europe"

## Zastosowanie

Technika kampanijnej nazwy nadawcy jest gotowa do natychmiastowego testowania w kampaniach [[Otwarte Klatki]] — zamiast "Patrycja - OK" można użyć "Koniec klatek - Otwarte Klatki" jako pole nadawcy dla konkretnych kampanii. Warto też przetestować stałą stopkę donacyjną niezależnie od typu wiadomości.

---

## Analiza szczegółowa

### Dane podstawowe

- **Próba**: 82 maile, czerwiec 2025 – marzec 2026
- **Częstotliwość**: ~2,1 maila/tydzień, brak dziennych mailingów
- **Nadawca techniczny**: zawsze `info@e.wemove.eu`
- **Nadawcy personalni**: 15+ osób — Lesly Lila (12), Taïme Smit (9), Till Ehrmann (8), Aleksandra Zielińska (6), Virginia (6), Giulio (6), Olga Vukovic (5), Kelsey DePorte (5), Hajar Drissi (4), Olga Iskra (4) i inni — z podanymi miastami (Marsylia, Barcelona, Bruksela, Madryt, Helsinki)
- **Kampanijne nazwy nadawców** (~15% maili): "Stop monopolowi Google'a", "Niech Elon zapłaci", "Elon musi zapłacić", "Powstrzymajmy Trumpa", "Na straży praw kobiet", "Zatrzymać umowę UE-Izrael", "Zespół ds. 'eko' kłamstw"

### Trzy typy strukturalne maili

**Typ 1 — Petycja (kampanijny, ~50% maili)**

| # | Warstwa | Opis |
|---|---------|------|
| 1 | **Hook kryzysowy** | 2–4 zdania bez powitania, od razu problem i pilność |
| 2 | **Pierwsze CTA** | Przycisk "PODPISZ TERAZ!" / "Wspieram [kampanię]!" |
| 3 | **Personalizacja** | "Piotr, [kampania] prosi Cię o pomoc" |
| 4 | **Narracja** | Kontekst: dlaczego ta decyzja, kto jest zagrożony |
| 5 | **Drugie CTA** | Przycisk petycji lub wsparcia |
| 6 | **Sign-off** | Imiona + miasta: "Taïme (Barcelona), Till (Bruksela)..." |
| 7 | **Footnotes** | Linki do źródeł (inline lub numerowane) |
| 8 | **Stopka** | Boilerplate WeMove + social media + "DORZUĆ SIĘ" |

**Typ 2 — Fundraising (~20% maili)**

| # | Warstwa | Opis |
|---|---------|------|
| 1 | **Problem finansowy** | Bezpośrednie postawienie problemu (ludzie rezygnują z subskrypcji) |
| 2 | **Opcje donacji** | Przyciski 5 / 7 / 10 PLN tygodniowo + inna kwota + jednorazowo |
| 3 | **Narracja** | Dlaczego donacja jest ważna, co daje |
| 4 | **Success stories** | 3–4 przykłady wygranych kampanii z przypisami |
| 5 | **Ponowne opcje donacji** | Powtórzenie przycisków |
| 6 | **Sign-off + P.S.** | Imię + miasto + P.S. z ostatnią prośbą |
| 7 | **Stopka** | Boilerplate + "DORZUĆ SIĘ" |

**Typ 3 — Raport z wygranej (~10% maili)**

| # | Warstwa | Opis |
|---|---------|------|
| 1 | **Powitanie** | "Cześć, Piotr!" |
| 2 | **Podsumowanie wygranej** | 2–3 zdania celebrujące sukces |
| 3 | **3 stories** | Każde zwycięstwo: kontekst → akcja → rezultat + foto |
| 4 | **Soft donation ask** | Miękkie CTA donacyjne bez presji |
| 5 | **Sign-off** | Wielu autorów z miastami |
| 6 | **Stopka** | Boilerplate + "DORZUĆ SIĘ" |

**Typ 4 — Narracyjny/alertowy (~20% maili)** — mail o problemie bez bezpośredniego CTA petycyjnego; buduje świadomość, kończy się ogólnym CTA do działania.

### Typy i ilość CTA

- **Petycja** ("Podpisz", "PODPISZ TERAZ!", "Wspieram [kampanię]!"): ~50% maili, 1–2 CTA
- **Donacja regularna** (5/7/10 PLN tygodniowo): ~20% maili, 3–5 wariantów przycisków
- **Donacja jednorazowa**: opcja uzupełniająca w mailach fundraisingowych
- **Stopka "DORZUĆ SIĘ"**: 100% maili — donacja jest zawsze obecna
- **Średnia liczba CTA**: 2–3 (petycja: 2; fundraising: 5–8 wariantów donacyjnych; wygrana: 1)

### Godziny wysyłki (czas polski CET/CEST)

WeMove wysyła z serwerów w UTC+0; po przeliczeniu:

| Okno polskie | Udział | Charakterystyka |
|---|---|---|
| 06:00–08:00 | ~12% | Wczesny poranek |
| 09:00–11:00 | ~33% | **Szczyt poranny** |
| 12:00–13:00 | ~12% | Przerwa obiadowa |
| 14:00–16:00 | ~32% | **Szczyt popołudniowy** |
| 17:00–19:00 | ~7% | Wieczór |
| 21:xx | ~2% | Nocne (wyjątki) |

**Kluczowy insight**: bimodalna dystrybucja — dwa szczyty aktywności (9–11 i 14–16) vs. Avaaz (jeden szczyt 06–08) i OK (jeden szczyt 18–21).

### Dni tygodnia

| Dzień | Udział | Uwagi |
|---|---|---|
| Piątek | ~26% | **Dominujący** (podobnie jak OK) |
| Środa | ~17% | Drugi najczęstszy |
| Poniedziałek | ~17% | Trzeci |
| Czwartek | ~16% | Czwarty |
| Wtorek | ~12% | Piąty |
| Sobota | ~10% | Rzadki weekend |
| Niedziela | ~2% | Praktycznie brak |

**Kluczowy insight**: WeMove jest organizacją tygodniową — 88% w dni robocze, piątek dominuje, niedziela praktycznie nieobecna.

### Analiza tematów (subject lines)

- **Długość**: 5–12 słów (dłuższe od Avaaz, podobne do OK)
- **Personalizacja** ("Piotr" w temacie): ~7% maili (rzadkie)
- **Emoji w temacie**: ~17% (umiarkowane)
- **Technika "Re:/RE:"**: ~17% maili — follow-up na poprzednią wiadomość
- **Kampanijna nazwa nadawcy** zamiast imienia: ~15% maili (unikalna technika)
- **Styl**: dramatyczny ale kontekstowy — "Zatruli wodę, żywność… nawet naszą krew", "Ten dom się pali🔥", "Musk na liście rozrabiaków"
- **Pytania**: ~5% tematów ("Dla kogo naprawdę pracują politycy?", "Czy Musk odpowie za to?")

### Główne kampanie (przykłady)

| Temat kampanii | Obszar | Typ maila |
|---|---|---|
| Google / monopol Big Tech | Regulacje UE | Petycja + fundraising |
| Musk / X / Tesla | Technologia | Petycja |
| Traktat UE-Izrael / Gaza | Geopolityka | Petycja |
| Amazonia / odwierty | Środowisko | Petycja |
| Bałtyk / rurociąg | Środowisko | Petycja |
| Aborcja / My Voice My Choice | Prawa kobiet | Petycja |
| Trump / Europa | Geopolityka | Petycja + narracja |
| Grenlandia | Geopolityka | Petycja |
| Glifosat / Bayer-Monsanto | Żywność/środowisko | Petycja |
| Plastik | Środowisko | Petycja |
| Kryzys mieszkaniowy | Społeczne | Narracja |
| Rekiny / bioróżnorodność | Środowisko | Petycja |
| Wygrane kampanie | Retencja | Raport + soft donation |
| Zbiórkowe ("Termin: północ") | Fundraising | Wielokrotna donacja |

### Porównanie z Avaaz, Greenpeace i Otwarte Klatki

| Wymiar | WeMove | Avaaz | Greenpeace | Otwarte Klatki |
|---|---|---|---|---|
| Maile/tydzień | ~2,1 | ~1,1 | ~1,5 | ~2,5 |
| Dzienny mailing | nie | nie | nie | tak (Nov–Dec) |
| Dominant dzień | piątek | sobota | czwartek | piątek |
| Weekend | ~12% | 48% | 0% | <10% |
| Godzina (PL) | 09–11 i 14–16 | 06–08 | 08–10 | 18–21 |
| Typy maili | 4 (petycja/fundraising/wygrana/narracja) | 2 (petycja/donacja) | 3 | 3 |
| Personalizacja tematu | ~7% | 0% | 0% | ~60% |
| Emoji w temacie | ~17% | ~5% | ~10% | ~80% |
| Technika "Re:" | ~17% | ~20% | rzadko | rzadko |
| Kampanijna nazwa snd. | tak (unikalne) | nie | nie | nie |
| Stała stopka donacyjna | zawsze | nie | nie | nie |
| Sender cities | tak (Barcelona, Madryt…) | nie | nie | nie |
