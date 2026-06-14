---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2025/12/jak-rozpoznawac-slopy-ai-w-tekstach-na-pewno-nie-maszynowo"
published: 2025-12-08
created: 2026-06-14
tags:
---


Slop to niskiej jakości, masowe i monotonne wytwory AI. Kojarzymy je głównie z męczącymi grafikami, zalewającymi media społecznościowe i portale. Jednak slop może mieć też postać tekstową i wyrażać się w całych tekstach lub infekować ich fragmenty. Jak w takim przypadku go rozpoznawać?

Dwa artykuły opublikowane jesienią dają nam wgląd w cechy slopu i inspirują do wypracowania metod jego rozpoznawania w badanych przez nas tekstach (np. przygotowanych przez studentów na zaliczenie albo tworzonych w redakcjach, które chcą oszczędzić na ludzkiej pracy). Pierwszy artykuł proponuje podstawową typologię slopu, drugi jest już badaniem slopów tekstowych z wykorzystaniem zestawu cech.

Artykuł *The 7Vs of AI Slop: A Typology of Generative Waste* (DOI: [10.2139/ssrn.5558018](https://dx.doi.org/10.2139/ssrn.5558018), 2025) stara się odpowiedzieć na problem definicji slopu. Wydaje się, że - tak jak jest to ze *spamem* czy nawet *pornografią*, trudno tu podać jednoznaczną definicję, która nie wyraziłaby jakichś wartości estetycznych czy etycznych. W komunikacji naukowej warto jednak dbać o pewien standard rozumienia obiektów, które się bada - stąd propozycja autorów tekstu. Opiera się ona na siedmiu cechach, mających wykazać, że

> \[...\] slop nie jest przypadkowym efektem ubocznym generatywnej AI, lecz systemową cechą kapitalizmu platformowego. Nasza propozycja ma podwójny charakter. Po pierwsze, typologia dostarcza pojęciowego słownika do identyfikowania powtarzających się logik slopu oraz wyjaśniania, w jaki sposób ze sobą współdziałają. Po drugie, zestaw propozycji przekłada te wymiary na tezy badawcze, które można rozwijać w badaniach empirycznych. \[Nasze\] propozycje mają budować język, ale i wskazywać mapę drogową niezbędną do zrozumienia, w jaki sposób slop kształtuje kulturę, wiedzę, politykę, życie gospodarcze i aktywność instytucji.

**Podstawowe cechy slopu**

Badacze zdecydowali się opisać podstawowe cechy slopu, odwołując się do siedmiu wartości:

- skala / objętość (volume) - narzędzia AI pozwalają masowo generować treści, przez co mogą one wypierać ludzką twórczość, np. z wyników wyszukiwania. Każda nisza może być zalana generatywnymi wytworami. Dobrym przykładem takiego zjawiska jest masowe publikowanie generatywnych ocen w sklepach internetowych, blogi generowane pod SEO a nawet [publikowanie naukowe](https://en.wikipedia.org/wiki/Essay_mill). Ostatnio także na Spotify wygenerowane maszynowo piosenki [zabierają miejsce na playlistach](https://www.theguardian.com/technology/2025/nov/13/ai-music-spotify-billboard-charts) - a więc uwagę odbiorców - ludzkim autorom i autorkom,
- szybkość / prędkość (velocity) - slop może być generowany błyskawicznie na wielką skalę. Przez to trudno objąć go jakąkolwiek kontrolą - np. moderacją lub weryfikacją. Przykładem, ilustrującym wagę tej cechy, jest według autorów obieg fake newsów albo nieustanna rotacja na platformach społecznościowych generowanych maszynowo memów (meme churn),
- zróżnicowanie (variety) - slop przyjmować może wiele form (tekst, grafika, audio, nawet kod źródłowy), korzystać z wielu gatunków i stylów. Mimo tego, jak czytamy w opracowaniu, slop jest homogeniczny - chociaż technicznie czy formalnie kompletny, to stylistycznie płaski. Dobrym przykładem są tu generowane maszynowo artykuły / eseje, czy nawet recenzje prac naukowych albo dokumenty wytwarzane przez działy HR w firmach,
- niska wartość lub brak wartości (value) - rozpowszechnianie się slopu prowadzić ma do dewaluacji oryginalności i znaczenia (meaning). Slop nie niesie za sobą żadnych wartości, w opracowaniu podkreśla się to stwierdzeniem o tym, że jest *nutritionally empty* (dosłownie *pozbawiony wartości odżywczych*). Przykłady, w których ujawnia się ta cecha, to np. nie niosące ze sobą żadnej wartości opracowania (hollow essays), [workslop](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity) - treści i produkty symulujące aktywność pracowników czy generyczny branding firm,
- brak wiarygodności / weryfikowalności (veryfication) - systemy AI produkują nieistniejące odnośniki i cytaty, mogą tworzyć obrazy (wizerunki), które nie mają nic wspólnego z rzeczywistością, chociaż mogą być przedstawiane jako autentyczne,
- widoczność (visibility) - rozpowszechnianie się slopu wzmacniane jest algorytmicznie na platformach społecznościowych, platformy priorytetyzują często publikowane, nowe i angażujące treści, a te warunki slop spełnia bardzo dobrze. Dzieje się to oczywiście kosztem widoczności jakościowych treści tworzonych przez ludzi,
- wirusowość (virality) - wytwory slopowe zdobywają popularność dzięki własnej dziwaczności, niesamowitości lub specyficznemu humorowi. Są przez to szybko przyswajane i normalizowane. Kogo dziś dziwi [krewetkowy Jezus](https://www.niemanlab.org/2024/04/from-shrimp-jesus-to-fake-self-portraits-ai-generated-images-have-become-the-latest-form-of-social-media-spam/)?

Zaproponowana lista cech slopu AI pozwala zrozumieć, że w żadnym wypadku nie jest to nowa, bardziej agresywna wersja spamu, a więc, że nie można z nim walczyć tak, jak walczy się z niechcianymi mailami czy wiadomościami w mediach społecznościowych. Spam nie jest tak zróżnicowany jak slop, w żaden sposób nie jest angażujący, nie staje się też wirusową treścią, która nagle i niespodziewanie zdobywa wielką popularność. Nikt też spamu nie traktuje jako coś, co powinno podlegać weryfikacji. Spam się blokuje, slopy bardzo trudno zablokować. Twórcy projektu [Slop Evader](https://tegabrain.com/Slop-Evader) zdecydowali na przykład, że prawdziwie wolne od slopu będą treści opublikowane przed publiczną premierą Chat GPT (a więc przed 22 listopada 2022 roku).

**Jak rozpoznać slop w tekście?**

Wspomniane wyżej opracowanie *The 7Vs of AI Slop: A Typology of Generative Waste* daje nam podstawowe rozeznanie w cechach slopu, możemy nawet próbować na jego podstawie zaproponować jakąś definicję, jednak trudno je bezpośrednio wykorzystać w analizie generatywnych tekstów. Dlatego warto sięgnąć po preprint *Measuring AI "Slop" in Text* (DOI: [10.48550/arXiv.2509.19163](https://doi.org/10.48550/arXiv.2509.19163), 2025), którego autorzy proponują sprofilowaną taksonomię slopu.

Podstawą omawianej pracy były wywiady z dziewiętnastoma ekspertami, reprezentującymi takie domeny jak przetwarzanie języka naturalnego (NLP), literatura, dziennikarstwo, lingwistyka i filozofia. Rozmówcy zostali poproszeni o podanie definicji slopu w kontekście tekstów generowanych maszynowo oraz o określenie, jakie cechy tekstu mogą wskazywać, że mamy z nim do czynienia. Na podstawie wywiadów opracowano taksonomię (zestaw i hierarchię cech), którą następnie przetestowano za pomocą analizy zakodowanych nią tekstów maszynowych - zbadano, jak bardzo zgodne są oceny zaproponowanych tekstów testowych w poszczególnych kategoriach tej taksonomii.

Interesować nas będzie tutaj sama taksonomia, pamiętajmy jednak, że podczas jej testowania oceny tekstów dla wybranych kategorii okazały się mocno subiektywne, a zgodność ocen binarnych była na bardzo niskim poziomie. Mówiąc inaczej, osoby podejmujące na podstawie taksonomii decyzje, czy badany tekst jest slopem, czy nie jest, raczej nie byli ze sobą zgodni (wskaźnik kappa Cohena wskazywał na słabą do miernej zgodność), chociaż grupa testująca raczej zgodnie identyfikowała niewielkie fragmenty, które na ten slop miały wskazywać.

Taksonomia zaprezentowana przez autorów badania składa się z kategorii (motywów) oraz przynależnych do nich cech. Oto tabelka przedstawiająca tę taksonomię:

| Cecha | Opis | Przykład |
| --- | --- | --- |
| 1\. Jakość informacji |  |  |
| 1.1 Faktualność (Factuality) | Nieprawidłowe lub zmyślone informacje. Wprowadzające w błąd lub fałszywe twierdzenia. | *Dr Sarah Johnson z Uniwersytetu Harvarda opublikowała w 2022 r. przełomowe badania na ten temat*. (Slop, jeśli dr Johnson nie istnieje, nie pracuje na Harvardzie lub nie opublikowała takich badań). |
| 1.2 Stronniczość (Bias) | Tekst wydaje się zbyt "obiektywny", chociaż właściwe byłoby podkreślenie subiektywności. Brak niezbędnego retorycznego podkreślenia, że stwierdzenie jest wyrazem określonego punktu widzenia lub szczególnej perspektywy. Treść wydaje się obiektywna, chociaż wyraża pewne zaangażowanie. | *Zmiany w polityce gospodarczej w 2023 r. były powszechnie korzystne*. (Slop, ponieważ przedstawia jednostronny widok złożonych skutków polityki). |
| 2\. Użyteczność informacyjna |  |  |
| 2.1 Gęstość informacyjna (Information Density) | Tekst jest rozwlekły, ale przekazuje niewiele informacji. Ogólne stwierdzenia lub nadmierne użycie słów-wypełniaczy, które nie wnoszą żadnej wartości. | *W dzisiejszym, szybkim, nowoczesnym świecie najnowocześniejszych technologii i innowacji, stało się niezwykle ważne, aby rozważyć różne czynniki i elementy, które przyczyniają się do naszego zrozumienia tej złożonej i wieloaspektowej kwestii...* |
| 2.2 Znaczenie / Adekwatność (Information Relevance) | Treść, która nie uwzględnia niuansów zapytania lub zadania, nie wnosi nic istotnego do kontekstu/zapytania/zadania. Tekst wydaje się nie spełniać zamierzonego celu. Jeśli tekst ma dodatkowe informacje w innym miejscu, uwzględnij je w analizie. Dla tekstu bez dodatkowego kontekstu, weź pod uwagę jego wewnętrzną adekwatność. | Odpowiedź na pytanie *Jak mogę poprawić swój rekord w maratonie?*: *Bieganie jest doskonałą formą ćwiczeń, przynoszącą wiele korzyści zdrowotnych, w tym poprawę funkcjonowania układu sercowo-naczyniowego, lepszy nastrój oraz kontrolę wagi*. (Slop, ponieważ zdanie nie odpowiada na konkretne pytanie dotyczące poprawy wyników w bieganiu) |
| 3\. Precyzja i przejrzystość |  |  |
| 3.1 Precyzja (Precision) | Niejasne lub niejednoznaczne informacje, które pozostawiają zbyt wiele miejsca na interpretację. Ogólnikowe stwierdzenia, które zaciemniają znaczenie. | *Poprawa była znacząca*. (Slop, ponieważ brakuje precyzyjnych danych lub punktu odniesienia do oceny poprawy). |
| 3.2 Powtarzanie (Repetitiveness) | Niepotrzebne powtórzenia tego samego pomysłu lub informacji w tekście. Parafrazowanie bez dodawania nowej wartości. | *Nowe badanie ujawniło, że kawa jest zdrowa. Badania pokazują również, że napój kawowy ma właściwości zdrowotne dla organizmu.* (Slop, ponieważ jest to powtórzenie tego samego pomysłu). |
| 3.3 Nieużyteczne formatowanie/struktura | Zbyt skomplikowana lub chaotyczna struktura, która utrudnia czytelność. Niepotrzebne nagłówki, akapity lub wyróżnienia. | Tekst z nadmierną liczbą podpunktów, pogrubień i nagłówków do prostego tematu. |
| 3.4 Spójność (Coherence) | Fragmenty tekstu, które nie pasują do siebie. Wprowadzenie dygresji lub nagła zmiana tematu. | *Kawa mi smakowała. Następnie poszedłem do parku. To, co było kałużą, było teraz suche*. (Slop, ponieważ przejście między kawą a suchą kałużą w parku jest niespójne). |
| 3.5 Obszerność (Verbosity) | Nadmierna rozwlekłość w stosunku do przekazywanych informacji. Niepotrzebnie "kwiecisty" język lub priorytet liczby słów nad wartością informacyjną. | *Spożycie wyżej wymienionego napoju, który został przygotowany z najwyższą starannością i dbałością o szczegóły przez wykwalifikowanego baristę, dostarczyło mi poczucia satysfakcji i zadowolenia, które ogarnęło całą moją istotę* (Slop, ponieważ można by po prostu powiedzieć *Kawa mi smakowała*). |
| 3.6 Złożoność Słownictwa (Word Complexity) | Nieodpowiednie użycie słownictwa w stosunku do kontekstu. Niepotrzebny żargon, skomplikowana terminologia lub modne słowa, które zaciemniają znaczenie. | W ogólnym artykule o ogrodnictwie: *Związki fenolowe w niektórych odmianach wykazują właściwości przeciwbakteryjne, które ograniczają kolonizację przez drobnoustroje patogeniczne* (Slop, ponieważ używa niepotrzebnie złożonej terminologii, niezgodnej z oczekiwaniami odbiorców). |
| 3.7 Ton (Tone) | Ogólny (generyczny) głos pozbawiony charakteru lub celu. Brak perspektywy/punktu widzenia lub język zbyt formalny/nieformalny w danym kontekście. | We wpisie na blogu o osobistych doświadczeniach z podróży: *Wyżej wymieniony cel podróży oferuje liczne atrak...* |

Takie zestawienie wydaje się idealne do wykorzystania w prompcie, który zmusi dowolny duży model językowy do wygenerowania oceny tekstu. Maszynowe ocenianie slopów tekstowych na pewno znalazłoby zastosowanie w systemie edukacji albo nawet algorytmach rekomendacyjnych w wyszukiwarkach.

Autorzy opracowania przetestowali wykrywanie slopu w tekstach z wykorzystaniem opracowanej przez siebie taksonomii i modeli `GPT-5`, `Deepseek-V3` i Open AI `o3-mini`. Zadaniem dla modeli było sprawdzenie, czy tekst jest slopem (predykcja binarna) i ekstrakcja fragmentów slopu. Modelom dostarczono niezbędny kontekst - taksonomię oraz szczegółowy opis zadania. Niestety - jak czytamy - zgodność maszynowego oznaczania tekstów slopowych oraz bezpośrednich fragmentów charakterystycznych dla slopu z ocenami ludzkimi była bardzo niska.

![enter image description here](https://blog.humanistyka.dev/content/images/20251208234522-66941c7926097813f381d9a485315eb011dcc35cbdd0aa40a7f49f8a9c1a33e9.png)

Parametr `κ` w nazwie kolumny pierwszej tabeli oznacza poziom zgodności interpretacji maszynowych z interpretacjami ludzkimi ([współczynnika kappa Cohena](https://pl.wikipedia.org/wiki/Kappa_Cohena)) w binarnej predykcji slopu. Automatyczne metody wykrywania slopu nie są jeszcze dostępne do wdrożenia 😞.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).