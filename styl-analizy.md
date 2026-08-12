# Styl analizy — jak Piotr myśli o materiale (DRAFT do korekty, 2026-08-12)

> **Rola pliku:** reguły relevance (CLAUDE.md) mówią, CO brać. Ten plik mówi, JAK to przetwarzać — przy każdej syntezie: Inbox → Resources, Resources → Galaxy, hubach, briefach, talk pointach. Docelowe miejsce: `.claude/rules/styl-analizy.md` + podpięcie w skillach `*-to-notes` i `galaxy`.
>
> **Skąd wyprowadzony:** wyłącznie z materiału pisanego lub rozstrzyganego ręcznie przez Piotra (Talk pointy v2, notatki podcastowe, fundraising-2026-liczby, galaxy-strategia, huby Projects/Areas, reguły vaultu) oraz z sekcji Otwarte pytania w Galaxy. Nie z outputów pipeline'u.

## Ruchy analityczne

**1. Reframe na wejściu — teza, nie streszczenie.**
Synteza zaczyna się od zdania, które odwraca potoczne ujęcie tematu, a dopiero potem idą dowody.
Wzorzec: „Fundraising nie tworzy zaufania — on je odzwierciedla" · „prośba ujawnia, nie tworzy" (Talk pointy v2) · „AI unieważniło tekst jako dowód, że komuś zależy" (Dowód troski).
Tak nie: „Artykuł omawia znaczenie zaufania w fundraisingu".

**2. Mechanizm przyczynowy, nie relacja z treści.**
Każdy punkt odpowiada na „co powoduje co i dlaczego działa", z przypisaniem do źródła. Jeśli z akapitu nie da się wyciągnąć mechanizmu — akapit nie wchodzi do syntezy.
Wzorzec: „Powtarzanie szkodliwej narracji w celu jej obalenia ją wzmacnia — odbiorca zapamiętuje tezę, nie zaprzeczenie" (backfire).
Tak nie: „Autor podkreśla wagę dobrej komunikacji".

**3. Kontrast jako jednostka dowodu.**
Najmocniejsza forma argumentu to para: dwie liczby albo dwa pojęcia postawione naprzeciw siebie.
Wzorzec: 79% vs 32% (retencja stały vs jednorazowy) · 94% vs 6% (apel konkretny vs abstrakcyjny) · $161 vs $115 · sympatia vs salience · owned vs rented · „RATOWAĆ niż BUDOWAĆ" · „transparentność jest warunkiem koniecznym, responsywność akceleratorem".
Przy pytaniu „co ważniejsze: X czy Y" nie wybieraj — rozdziel funkcje i czas działania obu, potem podaj praktyczną kolejność przy ograniczonych zasobach (Talk pointy v2, sekcja 4).

**4. Liczba tylko z metryczką.**
Każda liczba niesie: źródło + rok + n (jeśli jest) + kraj/kontekst — i jest podpięta pod argument, któremu służy.
Wzorzec: „Neon One 2026 (4107 organizacji, 718 darczyńców)" · „RCT Social Change Lab, n=3467" · „79% vs 32% → argument za recurring giving" (fundraising-2026-liczby, sekcja „Top 3 liczby").
Tak nie: „badania pokazują, że retencja jest wyższa".

**5. Filtr polskiego kontekstu.**
Benchmark lub model z rynku zachodniego nigdy nie wchodzi jako uniwersalny — dostaje jawne pytanie o przenośność albo polski odpowiednik/kontrprzykład (1,5% podatku, BLIK, Pomagam.pl, zbiórki jednostkowe, słabsza kultura recurring, CSR zamiast majątków prywatnych).
Wzorzec: „Na ile benchmarki amerykańskie przekładają się na polski kontekst, gdzie duże zbiórki płyną przez portale typu Pomagam.pl?" (Recurring giving) · „Polska specyfika: darczyńca skrajnie ufny wobec jednostek, nieufny wobec biurokracji" (Talk pointy v2).

**6. Test małej organizacji.**
Jednostką odniesienia jest organizacja 2–5 osób, bez działu IT, bez etatu prawnika, z bazą kilkuset kontaktów. Każda rekomendacja przechodzi pytanie: czy to się skaluje W DÓŁ — a jeśli nie, gdzie leży próg opłacalności.
Wzorzec: „czy framework czterech filarów skaluje się w dół, czy potrzebuje uproszczonej wersji?" (Wdrażanie AI) · „jak zmierzyć billboard effect dla listy kilkuset osób, gdzie test A/B jest statystycznie bezsensowny?" (Newsletter jako kanał).

**7. Domknięcie operacyjne — forma użytkowa albo próg.**
Mechanizm domyka się czymś, co da się jutro zastosować w pracy konsultanta: test jednozdaniowy, audyt, checklist, praktyczna kolejność 1–4 — albo jawnie nazwanym progiem/granicą, jeśli formy jeszcze nie ma.
Wzorzec: test „my robimy → ty możesz sprawić" · audyt żargonu · „praktyczna kolejność dla NGO z ograniczonymi zasobami: 1. responsywność ≤48h…" (Talk pointy v2) · pytania „gdzie przebiega próg/granica" w każdej stronie Galaxy.
Zasada nadrzędna: „strona, której nie da się zastosować w pracy konsultanta — nie powstaje" (galaxy-strategia).

**8. Sprzeczność = flaga, nie rozstrzygnięcie.**
Gdy nowe źródło kłóci się z dotychczasową linią, obie tezy zostają zapisane obok siebie z rekomendacją „do decyzji Piotra" — nigdy nie uśredniaj i nie wybieraj po cichu.
Wzorzec: „higiena listy vs częstotliwość wysyłki — obie tezy zapisane jako mechanizm 8 na obu stronach, bez nadpisywania starych; decyzja należy do Piotra" (galaxy-strategia 2026-07-24).

**9. Metryka rozjeżdża się z oczekiwaniem → diagnoza per składnik.**
„Nie wyszło" nie jest wnioskiem. Rozbij wynik na składowe, znajdź mechanizm rozjazdu, przestaw priorytet.
Wzorzec: pomiar SSI 39/100 zamiast 50 → tabela per filar → „mianownik rośnie szybciej niż licznik" → priorytet na dwa filary poniżej baseline (Sprint SSI 35 na 50).

## Kanon pytań

Pytania, które Piotr zadaje każdemu materiałowi — używaj ich do sekcji „Otwarte pytania" i do oceny źródeł (frazowanie z istniejących stron Galaxy):

- **Przenośność:** na ile to przekłada się na polski kontekst — które elementy przenoszą się, a które wymagają lokalnej walidacji?
- **Próg/granica:** gdzie przebiega granica między X a Y (użyciem a nadużyciem, higieną a stratą, minimum realnym a fasadą)?
- **Skala w dół:** czy działa przy 2–5 osobach bez zaplecza — od jakiej skali ma sens, kiedy jest przedwczesną komplikacją?
- **Pomiar/proxy:** jak to zmierzyć, gdy standardowa metryka się rozsypuje (open rate po MPP, mały ruch, mała lista) — jaki sygnał zastępczy?
- **Drugi rząd AI:** czy AI nie podkopie fundamentu, na którym stoi ten mechanizm (autentyczność, otwarcia jako sygnał, dryf ku middlingowi)?
- **Realność:** czy to osiągalne, czy życzeniowe — jaki jest najtańszy poziom, który da się utrzymać?
- **Właściciel:** kto to utrzymuje i kto odpowiada, gdy autor odejdzie / rotują wolontariusze / błąd trafi do beneficjenta?
- **Etyka:** gdzie wzmacnianie przechodzi w manipulację — zwłaszcza wobec darczyńców, beneficjentów i osób w słabszej pozycji?

## Formy, w których zapisuję myślenie

Teza (1 zdanie) → punkty z mechanizmami i źródłami → domknięcie operacyjne. Tabela liczba–kontekst–źródło z flagą kraju. „Sukces = …" zdefiniowany na starcie każdego przedsięwzięcia; log decyzji z uzasadnieniem routingu; retrospektywa po 2–3 cyklach. Cytaty odkładane jawnie „do użycia", z nazwiskiem.

## Anty-wzorce (tak nie)

Streszczenie bez mechanizmu. Liczba bez źródła/roku/n/kraju. Benchmark USA podany jako uniwersalny. Rada dla „organizacji" niesprawdzona na skali 2–5 osób. Rozstrzyganie sprzeczności za Piotra albo uśrednianie stanowisk („z jednej strony, z drugiej strony"). News zamiast pojęcia. Hype bez pytania o realność. Wniosek „nie działa" bez diagnozy per składnik.

## Utrzymanie profilu

Plik jest żywy. Po każdej sesji, w której Piotr poprawił output (Resources, Galaxy, brief, artykuł), dopisz różnicę jako jedną linię do Logu korekt — to najcenniejszy sygnał stylu. Gdy w logu uzbiera się wzorzec (≥2 podobne korekty), awansuj go do ruchu lub anty-wzorca powyżej i wyczyść wpisy.

## Log korekt

- (puste — start 2026-08-12)
