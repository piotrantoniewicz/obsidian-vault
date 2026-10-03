---
categories:
  - Clippings
url: "https://aininjas.pl/priv/d599ecfd-f26a-47fa-992c-2195f921cc7b/"
source: "[[Archives/2026-10-02 Jak pisać dobre prompty (Framework R-F-K-A)|2026-10-02 Jak pisać dobre prompty (Framework R-F-K-A)]]"
created: 2026-10-02
relevance: wysoka
tags:
  - "prompt-engineering"
  - "szkolenia-AI"
---

# Jak pisać dobre prompty (Framework R-F-K-A)

Materiał szkoleniowy z aininjas.pl opiera się na zasadzie „garbage in, garbage out": jakość odpowiedzi AI zależy od struktury polecenia, więc zamiast „rozmawiać" z modelem, trzeba go „programować" językiem naturalnym. Autorzy proponują czteroelementowy framework R-F-K-A (Rola, Format, Kontekst, Akcja) i pokazują, jak przejść od słabego do profesjonalnego prompta. Największy nacisk kładą na kontekst, bo właśnie tam większość osób daje za mało informacji. To prosty, dobrze rozpisany szkielet, który da się od razu wykorzystać w szkoleniach z AI.

## Frameworki i metody

**Framework R-F-K-A:**

1. **R — Rola (Role):** kim ma być model. Deklaracja roli aktywuje wzorce z danych treningowych i narzuca styl komunikacji. Trzy poziomy: podstawowy (sam zawód), szczegółowy (zawód + specjalizacja + doświadczenie), kontekstowy (+ perspektywa i ograniczenia). Anti-pattern: rola „supermana" z mnóstwem superlatyw rozmywa fokus; lepiej wskazać jedną specjalizację i jeden akcent.

2. **F — Format (Format):** jak ma wyglądać wynik. Oszczędza czas, wymusza strukturę myślenia i ułatwia automatyzację. Opcje: tekstowe (akapit, lista, tabela, FAQ, dialog), strukturalne (JSON, XML, Markdown, YAML, CSV) oraz długość (liczba słów, punktów, zdań). Im precyzyjniej (np. kolumny tabeli, sortowanie, wiersz podsumowania), tym lepiej.

3. **K — Kontekst (Context):** co model musi wiedzieć. Złota zasada: podaj wszystko, co powiedziałbyś nowemu pracownikowi w pierwszy dzień pracy. Cztery elementy: odbiorca, cel, ograniczenia (czego unikać), tło (co już wiem lub mam). Szablon: Odbiorca / Cel / Tło / Ograniczenia / Ton. Heurystyka: powyżej ok. 500 słów kontekstu rozważ podział zadania lub streszczenie.

4. **A — Akcja (Action):** co dokładnie ma się wydarzyć. Używaj czasowników operacyjnych (Przeanalizuj, Porównaj, Napisz, Wygeneruj zamiast „zrób coś z tym"), przy złożonych zadaniach rozpisz kroki w sekwencji, a oczekiwany wynik opisz konkretnie (np. 10 pomysłów, każdy z hookiem, wartością i call-to-action).

**Ćwiczenie „napraw prompt":** przepisanie słabego polecenia („Wymyśl nazwę dla mojej firmy") według R-F-K-A i porównanie jakości odpowiedzi.

## Wnioski
- Struktura polecenia (rola, format, kontekst, akcja) daje większy skok jakości niż samo „lepsze" sformułowanie pytania, a kontekst jest elementem, na którym użytkownicy najczęściej oszczędzają.
- Test „co powiedziałbym nowemu pracownikowi pierwszego dnia" to praktyczna reguła dla zespołów organizacji społecznych, które dopiero uczą się pracy z [[Claude]] czy [[ChatGPT]].
- Framework da się zamienić w szablon wielokrotnego użytku, co łączy się z promptami w automatyzacjach i własnych narzędziach.

## Zastosowanie
Gotowy do użycia w szkoleniach z AI dla organizacji społecznych: ćwiczenie „napraw prompt" można osadzić na przykładach z fundraisingu (np. mail do darczyńców). Szablon kontekstu (odbiorca, cel, tło, ograniczenia, ton) nadaje się do porównania z innymi frameworkami promptowania w materiałach szkoleniowych.
