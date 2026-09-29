---
type: "Web"
authors: "[[Mateusz Wojdalski]]"
url: "https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/jak-pisac-prompty-przyklady/?utm_source=newsletter&utm_medium=email&utm_term=2026-09-29&utm_campaign=KSeF+od+stycznia+dla+ka%C5%BCdej+JDG+Kary+dopiero+w+2028"
published: 2026-09-28
created: 2026-09-29
tags:
  - "prompt-engineering"
  - "szkolenia-AI"
  - "narzędzia-AI"
---


Jak pisać prompty, żeby czat AI odpowiadał konkretnie i bez ogólników? Anthropic, Google i OpenAI mają na to oficjalne przewodniki i w najważniejszych punktach mówią to samo. Model potrzebuje kontekstu, którego sam nie ma. Potrzebuje przykładu tego, co chcesz dostać, i jasno opisanego formatu odpowiedzi. Poniżej zebraliśmy siedem zasad z tych przewodników, a każdą pokazujemy na polskich przykładach z codziennej pracy: mailu do klienta, streszczeniu umowy i planie tygodnia. Na końcu opisujemy, jak prosić model o źródła i jak sprawdzać, czy czegoś nie zmyślił. Te same zasady pomagają w pracy z ChatGPT, Claude’em i Gemini.

## Czym jest prompt i dlaczego zwykłe pytanie nie wystarcza

Prompt to polecenie, które wpisujesz do czatu AI. Może to być jedno pytanie albo kilka akapitów z instrukcją, materiałem do pracy i przykładem.

Kłopot z krótkim pytaniem polega na tym, że model zna świat, ale nie zna ciebie. Nie wie, kim jest twój klient, jak piszesz maile ani do czego posłuży odpowiedź. Każdą lukę wypełnia więc czymś przeciętnym. Stąd biorą się odpowiedzi poprawne, ale nijakie.

Anthropic ujmuje to w swojej dokumentacji obrazowo. Radzi traktować model jak bardzo zdolnego, ale nowego pracownika, który nie zna zwyczajów firmy. Im dokładniej wytłumaczysz, czego chcesz, tym lepszy wynik. Z tego samego przewodnika pochodzi prosty test: pokaż prompt koledze, który nie zna zadania. Jeśli on nie wiedziałby, co zrobić, model też nie będzie wiedział.

## Jak pisać prompty: siedem zasad z oficjalnych przewodników

Zasady poniżej pochodzą z przewodników [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices), [Google](https://ai.google.dev/gemini-api/docs/prompting-strategies) i [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), czytanych 28 września 2026 roku. Przy każdej podajemy, kto ją zaleca.

1. **Pisz konkretnie.** Określ, co ma powstać, dla kogo, jak długie i w jakim tonie. Zaleca to cała trójka.
2. **Dodaj kontekst i powód.** Anthropic podaje przykład: zakaz wielokropków działa lepiej z wyjaśnieniem, że tekst przeczyta syntezator mowy.
3. **Pokaż przykład.** Google zaleca dołączać przykłady zawsze, Anthropic radzi od trzech do pięciu.
4. **Opisz format odpowiedzi.** Tabela, lista punktów, trzy zdania, mail z tematem.
5. **Zamieniaj ogólniki na liczby.** OpenAI radzi pisać “akapit z trzech do pięciu zdań” zamiast “dość krótko”.
6. **Mów, co zrobić, zamiast czego unikać.** Tak radzą OpenAI i Anthropic. Zamiast “nie pisz sztywno” napisz “pisz tak, jak mówisz do znajomego z pracy”.
7. **Dziel duże zadania na kroki.** Najpierw fakty z dokumentu, potem wnioski. Google i Anthropic radzą numerować kroki, gdy liczy się kolejność.

Najwięcej daje zwykle trzecia zasada. Jeden wklejony przykład twojego maila powie modelowi o stylu więcej niż akapit opisu.

Dwie rzeczy warto dodać przy długich materiałach. Anthropic zaleca wklejać dokument na początku, a pytanie zadawać na końcu. W testach producenta poprawiało to jakość odpowiedzi nawet o 30%. Drugi zabieg to oddzielenie instrukcji od materiału, na przykład nagłówkiem “Tekst:” albo cudzysłowem.

Pierwsza Misja AI · Kodożercy

### Używasz AI codziennie, ale czy robisz to dobrze?

Kurs Pierwsza Misja AI pokaże Ci techniki promptowania, które naprawdę działają. Praktyczne ćwiczenia na żywym modelu, gamifikacja i certyfikat.

[Sprawdź program kursu →](https://kursy.kodozercy.pl/pierwsza-misja-ai/?utm_source=devstockacademy-blog&utm_medium=article-banner&utm_campaign=pierwsza-misja-ai&utm_content=jak-pisac-prompty-przyklady)

![Pierwsza Misja AI - Kodożercy](https://devstockacademy.pl/wp-content/uploads/2026/04/pierwsza-misja-ai-pudelko-1.png.webp)

## Przykładowe prompty przed i po

Trzy sytuacje z codziennej pracy. W każdej najpierw prompt, jaki większość z nas wpisuje odruchowo, potem wersja poprawiona i krótko, co się zmieniło.

### Mail do klienta o opóźnieniu

Przed:

> Napisz maila do klienta, że projekt się opóźni.

Po:

> Prowadzę małe biuro projektowe. Piszę do pani Anny, właścicielki kawiarni, której robimy nową stronę internetową. Umówiliśmy się na oddanie strony 10 października, ale oddamy ją 17 października, bo fotograf przesunął sesję zdjęciową. Klientka jest miła, ale bardzo pilnuje terminów, bo planuje otwarcie drugiego lokalu.
> 
> Napisz maila, który: przeprasza jednym zdaniem, podaje nowy termin i powód, proponuje, że wcześniej wyślemy wersję bez zdjęć do sprawdzenia. Ton uprzejmy i rzeczowy, zwracamy się per pani. Najwyżej 120 słów, z tematem wiadomości.

Druga wersja podaje, kim jest odbiorca, co się stało i co może go zdenerwować. Nazywa też długość, ton i elementy, które mail ma zawierać. Model nie musi już zgadywać.

### Streszczenie umowy najmu

Przed:

> Streść tę umowę. \[wklejona umowa\]

Po:

> Tekst umowy: \[wklejona umowa\]
> 
> Za tydzień podpisuję tę umowę najmu mieszkania jako najemca. Nie jestem prawnikiem. Wypisz w tabeli: kwotę czynszu i opłat, kaucję i warunki jej zwrotu, okres wypowiedzenia dla każdej strony, kary umowne. Przy każdej pozycji podaj numer paragrafu. Jeśli czegoś w umowie nie ma, napisz “brak w umowie”. Na końcu wymień trzy zapisy, o które warto dopytać właściciela, i wyjaśnij dlaczego.

Umowa stoi na początku, a pytanie na końcu, zgodnie z zaleceniem Anthropic dla długich dokumentów. Numery paragrafów pozwalają sprawdzić każdą odpowiedź w oryginale. Polecenie “napisz brak w umowie” daje modelowi wyjście, zamiast zachęcać go do zgadywania. Samo streszczenie nie zastąpi porady prawnika, ale podpowie, o co go zapytać.

### Plan tygodnia

Przed:

> Zrób mi plan tygodnia.

Po:

> Pracuję zdalnie od 9 do 17, w środy mam dzień spotkań. W tym tygodniu muszę: przygotować prezentację na piątek (około 6 godzin pracy), rozliczyć fakturę z księgową, zrobić zakupy na urodziny córki w sobotę. Dwa razy chcę pójść na basen, najlepiej rano. Rozpisz plan od poniedziałku do piątku w tabeli: dzień, godzina, zadanie. Prezentację podziel na kilka krótszych bloków i skończ ją najpóźniej w czwartek. Zostaw codziennie godzinę bez zadań na rzeczy, które wypadną.

Tu działa zasada liczb. Zamiast “mam dużo pracy” jest sześć godzin i konkretne terminy, a zamiast “ułóż sensownie” reguły, według których model ma ułożyć tabelę.

## Prompt przed i po: ściągawka w tabeli

| Co poprawiasz | Przed | Po |
| --- | --- | --- |
| Kontekst | “Napisz maila do klienta” | kim jest klient, co się stało, czego się obawia |
| Cel i powód | “Streść umowę” | “podpisuję umowę jako najemca, nie jestem prawnikiem” |
| Format | brak | tabela, lista, mail z tematem, liczba słów |
| Ogólniki | “krótko”, “sensownie” | “najwyżej 120 słów”, “skończ w czwartek” |
| Przykład | brak | wklejony twój wcześniejszy mail albo wzór tabeli |
| Wyjście awaryjne | brak | “jeśli czegoś nie ma, napisz brak w umowie” |
| Kolejność przy długim tekście | pytanie, potem dokument | dokument, potem pytanie |

## Jak prosić AI o źródła i sprawdzać halucynacje

Halucynacja to odpowiedź, która brzmi pewnie, a jest nieprawdziwa. Model może wymyślić paragraf, którego w umowie nie ma, albo źródło, które nie istnieje. Anthropic w osobnym przewodniku o [ograniczaniu halucynacji](https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) podaje kilka technik, które przydadzą się każdemu:

- **Pozwól powiedzieć “nie wiem”.** Dopisz: “Jeśli nie masz pewności albo w tekście brakuje informacji, napisz to wprost”.
- **Każ najpierw cytować.** Przy długim dokumencie poproś o dosłowne cytaty z tekstu, a dopiero potem o analizę opartą na tych cytatach.
- **Każ sprawdzić każde twierdzenie.** Po odpowiedzi poproś: “Do każdego twierdzenia znajdź cytat, który je potwierdza. Twierdzenia bez cytatu usuń”.
- **Ogranicz model do materiału.** Napisz: “Korzystaj wyłącznie z wklejonego tekstu, nie z ogólnej wiedzy”.
- **Zadaj to samo pytanie kilka razy.** Jeśli odpowiedzi różnią się w faktach, potraktuj to jako sygnał do dodatkowego sprawdzenia.

Anthropic zastrzega, że te techniki ograniczają halucynacje, ale ich nie eliminują. Przy ważnych decyzjach i tak sprawdzasz informację u źródła. Jeśli model podaje link, otwórz go i poszukaj tam cytowanego zdania. Sama prośba o podanie pewności procentowej nie wystarczy, co opisaliśmy w tekście o [promptach z pewnością 95%](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/95-procent-confidence-prompt-meta-prompting-chatgpt-claude-2026/).

## Czego w promptach nie trzeba już robić

W sieci krąży sporo gotowych formułek: obietnica napiwku, groźba, zdanie “jesteś najlepszym ekspertem na świecie”, prośby pisane wielkimi literami. Żaden z trzech przewodników, które przeczytaliśmy, takich zabiegów nie zaleca. OpenAI radzi natomiast korzystać z najnowszych modeli, bo łatwiej je prowadzić.

Rola ma sens, jeśli jest konkretna. Anthropic potwierdza, że nawet jedno zdanie o roli zmienia ton i skupienie odpowiedzi. Zdanie “jesteś doradcą najemcy, który wyłapuje niekorzystne zapisy” pracuje jednak dlatego, że zawiera zadanie. Sam tytuł eksperta niewiele wnosi.

Nie trzeba też pisać długo za wszelką cenę. Kontekst ma znaczenie, ale zbędne słowa kosztują w limitach i rozpraszają model. Skrajną wersję tej oszczędności opisaliśmy przy [promptach w stylu jaskiniowca](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/caveman-prompting-claude-tokeny-oszczednosc-2026/).

## Szablon promptu do skopiowania

Jeśli nie wiesz, od czego zacząć, wypełnij sześć pól. Nie każde zadanie potrzebuje wszystkich.

> Kontekst: \[kim jesteś, dla kogo to jest, co się wydarzyło\] Zadanie: \[co ma powstać\] Materiał: \[wklejony tekst, dane, notatki\] Format: \[tabela, lista, mail, liczba słów, ton\] Zasady: \[czego się trzymać, co zrobić, gdy brakuje informacji\] Przykład: \[wzór tego, co chcesz dostać\]

Po pierwszej odpowiedzi nie zaczynaj od nowa. Napisz, co poprawić: “krócej”, “bardziej po ludzku”, “dodaj kolumnę z terminem”. Dopracowanie wyniku w dwóch albo trzech krokach to normalny sposób pracy z czatem. Jeśli piszesz po polsku do ChatGPT, przydadzą się też wskazówki z tekstu o [ChatGPT po polsku](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/chatgpt-po-polsku/).

## Najczęstsze pytania

### Czy prompty trzeba pisać po angielsku?

Nie. Obecne modele dobrze rozumieją polskie polecenia i odpowiadają po polsku. Jeśli chcesz odpowiedzi w konkretnym języku, napisz to wprost, zwłaszcza gdy wklejasz materiał po angielsku.

### Czy te same prompty działają w ChatGPT, Claudzie i Gemini?

Zasady są te same, bo przewodniki Anthropic, Google i OpenAI zalecają w najważniejszych punktach to samo: kontekst, przykłady i jasno opisany format. Odpowiedzi różnych modeli na ten sam prompt mogą się różnić stylem i długością.

### Jak długi powinien być dobry prompt?

Tak długi, jak wymaga zadanie. Krótkie pytanie o fakt nie potrzebuje kontekstu. Mail do klienta, analiza dokumentu albo plan pracy potrzebują kilku zdań o sytuacji, celu i formacie.

### Jak sprawdzić, czy AI nie zmyśla?

Poproś o dosłowne cytaty z materiału i o źródło przy każdym twierdzeniu. Potem otwórz źródło i znajdź tam to zdanie. Pozwól też modelowi przyznać, że czegoś nie wie.

## Podsumowanie

Dobre prompty nie wymagają tajnych formułek. Przewodniki Anthropic, Google i OpenAI, choć pisane dla różnych modeli, zgadzają się w najważniejszym: model trzeba potraktować jak zdolnego nowego współpracownika, który nie zna sytuacji. Dostaje więc kontekst i powód zadania, przykład oczekiwanego wyniku, jasno opisany format i liczby zamiast ogólników. Przy długich dokumentach pomaga kolejność “materiał, potem pytanie” oraz prośba o cytaty. Przy faktach trzeba zostawić modelowi możliwość przyznania się do niewiedzy i sprawdzać odpowiedzi u źródła, bo żadna technika nie usuwa halucynacji całkowicie. Najprostszy praktyczny test przed wysłaniem promptu pochodzi z dokumentacji Anthropic: czy osoba, która nie zna zadania, wiedziałaby, co zrobić.

Newsletter · DevstockAcademy & Kodożercy

### Bądź na bieżąco ze światem IT, AI i automatyzacji

Co wtorek: newsy z branży, praktyczne tipy i narzędzia które warto znać. Zero spamu.