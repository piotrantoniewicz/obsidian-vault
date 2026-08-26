---
categories:
  - Clippings
authors: ["[[Kasia Szczesna]]"]
url: "https://behavioralinsight.substack.com/p/a-process-doesnt-have-a-single-level"
source: "[[Archives/2026-08-24 A process doesn’t have a single level of automation|2026-08-24 A process doesn’t have a single level of automation]]"
published: 2026-08-24
created: 2026-08-25
relevance: wysoka
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "strategia-organizacji"
---

# A process doesn’t have a single level of automation

Kasia Szczęsna, opierając się na przeglądzie blisko dekady badań zespołu z [[Uniwersytet Zhejiang]] nad Human–AI Interaction, argumentuje, że pytanie „co zautomatyzować?" jest źle postawione. Zakłada bowiem, że proces to jeden blok z jednym poziomem automatyzacji, podczas gdy realny przepływ składa się z faz o zupełnie różnym profilu — zbieranie materiału może działać jako System 0, interpretacja jako System 2, a redakcja jako System 1. Kluczowe pojęcie to **dwukierunkowe wzmocnienie** ([[HCHAC]]): pytamy osobno dla każdej fazy, w którą stronę płynie wzmocnienie i kto trzyma kontrolę. Autorka mocno odróżnia to od zasady human-in-the-loop — obecność człowieka z przyciskiem „zatwierdź" i stuprocentowym wskaźnikiem akceptacji w logach to nie nadzór, tylko jego pozór. Dla mnie to najlepsze narzędzie porządkujące rozmowę o wdrożeniach AI, jakie widziałem ostatnio — bo przenosi punkt startu z listy zadań do automatyzacji na diagnozę tego, co dzieje się z człowiekiem.

## Frameworki i metody

**Trzy mechanizmy [[HCHAC]] — pytania zadawane osobno dla każdej fazy przepływu:**

1. **Przywództwo wertykalne (człowiek nad AI).** Gdzie w tym przepływie leży decyzja, której człowiek nie może oddać? Autorzy wskazują oceny etyczne i wybory strategiczne. Praktyczne przełożenie: który krok musi mieć twardy punkt zatrzymania, a nie tylko możliwość cofnięcia tego, co już się stało.

2. **Przywództwo transformacyjne (AI wzmacnia człowieka).** Czy ten krok podnosi zdolność użytkownika, czy ją zastępuje? Jeśli po trzech miesiącach korzystania użytkownik radzi sobie z zadaniem bez narzędzia gorzej niż przed wdrożeniem, deklarowane wzmocnienie było w rzeczywistości substytucją.

3. **Współdzielona odpowiedzialność.** Jak alokacja odpowiedzialności zmienia się między fazami? To rozbija milczące założenie, że zadanie ma jeden poziom automatyzacji — karta wzorca zaprojektowana pod „całe zadanie" zawsze będzie źle skalibrowana w co najmniej jednej fazie.

**[[BehaviorAI Design Framework]] — mapowanie przed kalibracją:**
- **Mapowanie:** rozłóż przepływ na fazy i sprawdź, co dzieje się z człowiekiem w każdej z nich — nie zgodnie z procedurą, tylko w rzeczywistości. Gdzie faktycznie podejmuje decyzję, gdzie tylko zatwierdza cudzą, gdzie przestał już patrzeć mimo formalnej odpowiedzialności, gdzie obchodzi system, bo bez niego jest szybciej.
- **Kalibracja:** dopiero teraz ustal, ile współpracy z AI ma sens w każdej fazie osobno i w którym punkcie decyzja musi wrócić do człowieka.
- Odwrócenie kolejności daje jeden suwak dla całego procesu — czyli powrót do punktu wyjścia.

**Test wzmocnienia (po kwartale, nie na etapie planowania):** sprawdź, czy zespół radzi sobie z zadaniem bez narzędzia lepiej czy gorzej niż przed wdrożeniem. Jeśli gorzej — to nie było wzmocnienie.

## Wnioski
- Poziom automatyzacji trzeba ustawiać fazami, nie dla całego procesu — i wracać do tej alokacji po kwartale, bo dojrzałość zespołu w pracy z modelami sama się zmienia w czasie.
- Human-in-the-loop bez realnego wpływu jest fikcją nadzoru; sto procent zatwierdzeń w logach to sygnał ostrzegawczy, nie dowód kontroli.
- Ludzie w jednym zespole są na skrajnie różnych etapach zaufania do modeli — jeden poziom automatyzacji będzie dla jednej osoby zbyt luźny, dla drugiej zbyt ciasny; diagnoza mikrozachowań musi poprzedzić projekt procesu.
- Badacze przyznają, że brakuje strategii dynamicznego przekazywania kontroli i danych długookresowych o degradacji kompetencji — to argument za świadomym rozpisywaniem alokacji, nie za wstrzymywaniem wdrożeń.

## Cytat
> Lepsze pytanie na start to nie „co zautomatyzować?", tylko „co dzieje się tutaj z człowiekiem, zanim cokolwiek zmienimy?".

## Zastosowanie
To gotowy szkielet pierwszego bloku warsztatu wdrożeniowego dla organizacji — zamiast otwierać listą procesów do automatyzacji, zacząć od mapowania mikrozachowań w wybranym przepływie (np. obsługa darczyńcy albo przygotowanie wniosku grantowego). Trzy pytania [[HCHAC]] można przerobić na prostą tabelę fazową do wypełnienia przez zespół klienta. Test „po kwartale" warto wpisać do umów konsultacyjnych jako mierzalne kryterium sukcesu wdrożenia — odróżnia realne wzmocnienie kompetencji od uzależnienia od narzędzia.
