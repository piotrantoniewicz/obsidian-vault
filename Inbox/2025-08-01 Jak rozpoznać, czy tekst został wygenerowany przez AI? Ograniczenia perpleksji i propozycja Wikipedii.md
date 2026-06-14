---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2025/08/jak-rozpoznac-czy-tekst-zostal-wygenerowany-przez-ai-ograniczenia-perpleksji-i-propozycja-wikipedii"
published: 2025-08-01
created: 2026-06-14
tags:
---


Duża część detektorów, mających sprawdzać, czy dany tekst został wygenerowany przez LLM, bazuje na perpleksji. W konsekwencji, jeśli nie mamy naturalnie bogatego słownictwa, albo materia pracy pisemnej wymaga prostego języka, przygotowany przez nas tekst może zostać fałszywie oznaczony. Z tego powodu lepiej ręcznie starać się rozpoznawać generowane teksty. Metody takiego sprawdzania, użyteczne na przykład podczas oceny studenckich prac pisemnych, sugeruje społeczność Wikipedii.

Wyobraźmy sobie, że jesteśmy dużym modelem językowym 🥲. Dostajemy polecenie dokończenia zdania "Ala ma...". Bez problemu generujemy dopowiedzenie ze szkolnej czytanki, np. "kota", "rower", "zielony sweter", takie frazy pojawiają się bardzo często w danych treningowych i są przewidywalne. Kiedy jednak w prompcie dostajemy zadanie dokończenia frazy "Kot rozważał...", nie jest już tak łatwo. To statystycznie (w kontekście danych treningowych) nietypowy początek zdania, które może mieć przecież wiele bardzo różnych zakończeń: "kot rozważał, czy wskoczyć na stół", albo "kot rozważał wyjście do kina", albo zupełnie coś innego. W literaturze pięknej, szczególnie w poezji, na pewno znajdziemy pełno takich nieprzewidywalności, [na które zresztą nie stać dużych modeli](https://blog.humanistyka.dev/2025/07/poezja-bez-ryzyka-to-tylko-skladnia-dlaczego-chatgpt-nie-sprawdzi-sie-w-tworzeniu-poezji). W pierwszym naszym przypadku zakończenie zdania będzie łatwe do przewidzenia, drugim niepewność będzie większa. Poziom tej niepewności to [perpleksja](https://pl.wikipedia.org/wiki/Perpleksja), którą bada się zewnętrznie dla modelu językowego.

Kiedy staramy się maszynowo rozpoznać, czy nasi studenci generują eseje zaliczeniowe, zamiast pisać je po nocach, proponuje się nam oprogramowanie bazujące właśnie na analizie perpleksji. Tymczasem jak czytamy w DOI: [10.48550/arXiv.2304.02819](https://doi.org/10.48550/arXiv.2304.02819) (2023), taka analiza nie bierze pod uwagę zdolności językowej autorów badanych tekstów i może dyskryminować tych użytkowników języka, dla których jest on językiem wyuczonym. Osoby takie mają zazwyczaj ograniczony zasób słów czy pamięć fraz i idiomów, więc tworzony przez nich tekst może być statystycznie bardziej przewidywalny niż tekst kogoś, kto od dziecka posługuje się danym językiem i to w jego rejestrze literackim.

Czy można ufać detektorom AI w tekstach?

> W skrócie - nie, przynajmniej według naszego doświadczenia. Nasze badania nad detektorami nie wykazały, żeby były one wystarczająco wiarygodne, zwłaszcza że edukatorzy mogą podejmować na ich podstawie decyzje mające potencjalnie trwałe konsekwencje dla uczniów.

czytamy na stronach [dokumentacji OpenAI](https://help.openai.com/en/articles/8313351-how-can-educators-respond-to-students-presenting-ai-generated-content-as-their-own). OpenAI zresztą miało swój własny detektor, ale [zrezygnowało z niego po kilku miesiącach roku](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/) z uwagi na niską skuteczność.

Wydaje się, że pozostaje nam wyłącznie ręczna analiza. Społeczność Wikipedii, która [sama mierzy się z problemem edycji generowanych maszynowo](https://www.pcmag.com/news/wikipedia-tried-to-add-ai-summaries-to-articles-but-editors-revolted), [sugeruje nam kilka metod](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), jakie pozwolić nam mają na rozpoznanie nieuczciwych studentów. To opracowanie zasługuje na szersze omówienie, ale na razie spróbujmy zapoznać się z jego streszczeniem, dostosowanym odrobinę przeze mnie do kontekstu akademickiego:

| Kategoria błędu | Cechy |
| --- | --- |
| Język i ton | - nadmierne podkreślanie wagi / znaczenia opisywanych zjawisk i obiektów, - promocyjny styl, - niepotrzebne wyrażanie opinii (np. *Polska od lat zmaga się z problemem nadmiernej biurokracji, co w oczywisty sposób spowalnia rozwój gospodarczy*), - nadużywanie spójników, - powtarzanie już raz podanych informacji i ocen, - powierzchowne analizy, - nieprecyzyjne przypisywanie opinii i ich generalizacja (np. *większość badaczy uważa, że…*). |
| Styl i formatowanie | - niepotrzebne pogrubienia, - listy (zob. ["reguła trzech" w pisaniu](https://en.wikipedia.org/wiki/Rule_of_three_\(writing\))), - emoji, - nadużywanie półpauz, - niespójne cudzysłowy. |
| Zwroty i ujawnienia | - frazy wynikające z interakcji między użytkownikiem a modelem (np. *Zgodnie z poleceniem…*), - wzmianki o ograniczeniach wiedzy, - odmowy wykonania poleceń, - wzorce z pustymi miejscami (np. *jak pisze w swoim artykule \[Imię i nazwisko autora\]*). |
| Formatowanie i cytowania | - niepoprawne formatowanie odnośników, - halucynowana bibliografia (błędy w tytułach, datach wydania, miejscach wydania). |
| Treść mertoryczna | - ogólniki, - brak pogłębionej analizy, - powtarzanie pomysłów, - brak krytycznego podejścia, - niespójność stylu. |

Być może jednak te metody i tak przestają być skuteczne, kiedy nieuczciwy student odpowiednio wysteruje styl i jakość generowanego tekstu, prosząc w prompcie o zastosowanie języka akademickiego czy profesjonalnego, unikanie kolokwializmów czy podając modelowi kilka przykładów dobrze napisanych esejów.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).