---
categories:
  - "Emails"
published: 2026-09-26
created: 2026-10-03
labels:
  - "Tomasz Woliński"
relevance: wysoka
tags:
  - "automatyzacja"
  - "strategia-AI"
  - "narzędzia-AI"
---

# Postawiłem agenta na serwerze. To była łatwa część

Tomasz Woliński (stormit.pl) przekonuje, że uruchomienie agenta AI na serwerze to dziś kwestia jednego wieczoru, a prawdziwym wyzwaniem jest zaufanie do jego pracy bez nadzoru. Autonomia nie jest więc problemem technicznym ani przełącznikiem „ręcznie / samo", tylko drabiną pięciu szczebli. Na każdy szczebel wyżej wpuszcza „bilet", czyli dowód, że agent robi swoje na niższym poziomie. U autora biletem są liczby z pętli własnych poprawek, a nie sam serwer.

## Frameworki i metody
- **Drabina autonomii: 5 szczebli i bilet na każdy**
  1. **Obok** — agent pracuje w tle, Ty na tym samym komputerze (w [[Claude Code]] to jeden przełącznik przy uruchomieniu). Bilet: zadanie, które nie wymaga pytań (np. przygotowanie informacji o kliencie przed spotkaniem).
  2. **W zasięgu** — sesja prowadzona z telefonu, który jest tylko pilotem; praca dzieje się na komputerze, więc komputer musi działać. Bilet: wiesz z góry, o co agent zapyta.
  3. **W granicach** — agent działa bez pytania o zgodę, ale w wyznaczonych granicach; to, co poza nimi, oznacza jako „decyzja właściciela" i odkłada. Bilet: spisane 3 rzeczy, których agent NIE robi, oraz próg pewności, poniżej którego sprawa wraca do człowieka (przykład z agenta od leadów: pewność poniżej 0,7 albo kwota powyżej 10 tys. → akceptacja właściciela).
  4. **Bez Ciebie** — agent pracuje bez Twojego komputera (rutyna w chmurze lub własny serwer), a wynik dostajesz jako raport albo propozycję zmian do akceptacji. Bilet: sprawdzasz skutek, a nie status — nie ufasz słowu „gotowe", tylko weryfikujesz, czy pliki z odpowiedziami faktycznie powstały. Twarda zasada: osobny użytkownik, osobny serwer, nigdy produkcja.
  5. **Uczy się** — agent dopasowuje się do Twoich poprawek jak nowy pracownik po kilku tygodniach. Bilet: liczba — odsetek poprawek spada i nie wraca.

  Przez całą drabinę biegnie jedna szyna: pętla Twoich poprawek. Każdy szczebel zbiera Twoje decyzje; bez nich nie ma czym udowodnić, że można wejść wyżej. Nie każdy musi się wspinać — autonomia ma sens przy powtarzalnej robocie z wolumenem, a przy zadaniach raz w miesiącu wystarcza szczebel 1.

## Kluczowe dane
- Agent selekcji newsów: ok. 120 newsów tygodniowo, z których autor wybiera ok. 30; po 3 tygodniach testów trafia w ok. 95% jego wyborów (21 propozycji do prasówki, żadnej zmiany)
- Poprawki w tekście newslettera: z 20–30% na początku do ok. 5% dziś

## Wnioski
- Autonomia to nie kwestia narzędzia ani serwera: technicznie to „wieczór roboty", a błędy autonomicznego agenta zauważa się dopiero, gdy zobaczy je klient — dlatego liczy się dowód na niższym szczeblu ([[Claude Code]]).
- „Zielony status" uruchomienia niczego nie gwarantuje — na szczeblu 4 sprawdza się skutek (czy pliki powstały, czy maile zostały przetworzone), a nie komunikat „gotowe".
- Zaufanie można mierzyć: odsetek poprawek człowieka spadający w czasie to konkretny bilet na wyższy szczebel, a granice agenta (3 rzeczy, których nie robi, plus próg pewności) trzeba spisać, zanim zacznie pracować bez nadzoru.

## Cytat
> Serwer stawia się w jeden wieczór. Zaufanie buduje się poprawkami, tydzień po tygodniu.

## Zastosowanie
Drabina autonomii i „bilety" dają gotowy szkielet do szkoleń z AI dla NGO oraz do rozmów o wdrażaniu agentów z klientami (np. w dobryai.pl). Reguła „pewność poniżej progu → decyzja właściciela" nadaje się do wprowadzenia we własnych automatyzacjach, a pętla poprawek może służyć jako miara dojrzałości wdrożenia.
