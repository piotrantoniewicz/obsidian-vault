---
type: Web
authors: '[[Marcin Wilkowski]]'
url: >-
  https://blog.humanistyka.dev/2026/03/stylometryczne-cechy-tekstow-generowanych-maszynowo?utm_source=newsletter&utm_medium=email&utm_term=2026-06-14&utm_campaign=+Wyborcza+zupe%C5%82nie+na+serio+opublikowa%C5%82a+rozmow%C4%99+z+ChatGPT+Stylometryczne+cechy+tekst%C3%B3w+generowanych+maszynowo+Humanistyczne+prowokacje+wobec+AI+Vintage+Large+Language+Models+Zaproszenie+na+webinar
published: 2026-03-21T00:00:00.000Z
created: 2026-06-14T00:00:00.000Z
tags:
  - LLM
  - trendy-AI
---


Rozpoznawanie tekstów generowanych maszynowo to niełatwa sprawa, szczególnie w przypadku automatycznego parafrazowania ludzkich tekstów. Badacze i badaczki z Uniwersytetu Jagiellońskiego w swoim eksperymencie sprawdzili efektywność stylometrii w tym zadaniu. Ich metoda wydaje się bardzo obiecująca.

Stylometria, jako zbiór metod pozwalających na pozyskanie *lingwistycznego odcisku palca* z tekstu, nie jest nową propozycją. Jej początki sięgają już XV wieku, a dokładnie dzieła *De falso credita et ementita Constantini Donatione declamatio* Wawrzyńca Valli, które pozwoliło na wykazanie fałszerstwa tzw. [Donacji Konstantyna](https://pl.wikipedia.org/wiki/Donacja_Konstantyna). Takie spojrzenie na tekst, w którym szuka się jego nieoczywistych, językowych cech, w celu wykazania autorstwa albo podobieństwa do innych tekstów, jest szeroko praktykowane w cyfrowej humanistyce. W artykule *Stylometry recognizes human and LLM-generated texts in short samples* (DOI: [10.1016/j.eswa.2025.129001](https://doi.org/10.1016/j.eswa.2025.129001), 2026) przekonuje się nas, że można je z powodzeniem użyć także do rozpoznawania tekstów generowanych maszynowo.

**Stylometryczne miary warte zastosowania**

Nie jest to łatwe zadanie, ponieważ duże modele językowe proponują coraz lepszą jakość tekstów - do tego wygenerowane już treści można dodatkowo parafrazować (także automatycznie), utrudniając identyfikację z wykorzystaniem automatycznych systemów detekcji albo w trakcie uważnego czytania. Opisywany przeze mnie wcześniej artykuł na ten temat podkreśla znaczenie [budowania osobnych heurystyk dla każdego zadania tego typu](https://blog.humanistyka.dev/2026/02/rozpoznawanie-tekstow-ai-piec-grup-cech-zamiast-jednego-wskaznika) i brania pod uwagę aż pięciu warst (czy też grup cech) analizowanego tekstu.

Jedną z takich grup jest właśnie analizowanie *zaburzeń we wzorcu występowania kolejnych słów w tekście*, które dają się wykryć metodami stylometrycznymi. W jaki sposób chcieliby to zrobić autorzy i autorki z UJ?

Najpierw musieli przygotować treści do testów. Skorzystali z podsumowań haseł Wikipedii w języku angielskim (napisane przez ludzi przed marcem 2022 r., aby uniknąć tekstów maszynowych - dostępność ChatGPT), ich streszczeń generowanych automatycznie (T5, BART, Gensim i Sumy), automatycznych parafraz wygenerowanych z użyciem modeli DIPPER i Parrot oraz fragmentów wygenerowanych od postaw (purely generated) przez modele językowe (GPT-3.5, GPT-4, LLaMa 2/3, Orca i Falcon), którym jako prompt podano jedynie dane hasło Wikipedii. Z tego zbioru do analiz wyodrębniono fragmenty składające się z 10 zdań.

Do wyodrębnienia cech tekstów użyto narzędzie [StyloMetrix](https://github.com/ZILiAT-NASK/StyloMetrix), opracowane w NASK, oraz dodatkowo samodzielnie zaprojektowany schemat analizy n-gramów. Stylometryczne charakterystyki tekstów, wyliczane w ramach analizy, obejmować mogły nawet 195 cech, w tym:

- szczegółowe formy gramatyczne: czasy, czasowniki modalne itp.
- główne reguły gramatyczne,
- specyficzne formy leksykalne: typy zaimków, słowa obraźliwe, interpunkcja,
- częstości występowania części mowy,
- sentyment, wzmacniacze leksykalne, maskowane słowa,
- formy składniowe: pytania, zdania, środki stylistyczne,
- ogólne statystyki tekstu takie jak współczynnik Type-Token Ratio (TTR), spójność tekstu itp.

**Główne cechy tekstów generowanych maszynowo**

Type-Token Ratio (TTR) to bardzo ciekawa miara jakości tekstu, opisująca bogactwo leksykalne i zróżnicowanie słownictwa - wylicza się ją na podstawie stosunku liczby unikalnych słów do całkowitej liczby słów w tekście. To właśnie wskaźnik TTR dla lematów (czyli podstawowych form wyrazów) ma być - jak przekonują autorzy i autorki badania - jedną z czterech najważniejszych cech stylometrycznych, na podstawie których identyfikować można teksty wygenerowane maszynowo za pomocą tzw. drzew decyzyjnych.

Obok TTR, wartościowymi miarami były

- częstotliwość występowania przymiotników w stopniu wyższym (szybki -> szybszy),
- zróżnicowanie słów pełniących funkcje gramatyczne (takich jak przyimki czy spójniki). Wytwory maszynowe były pod tym względem słabo zróżnicowane (np. *Mikołaj Kopernik studiował w Krakowie, wyjechał do Włoch i tam uczył się prawa i zajmował się astronomią* zamiast *Mikołaj Kopernik studiował w Krakowie, następnie wyjechał do Włoch, gdzie uczył się prawa, a jednocześnie zajmował się astronomią* - tego przykładu nie ma w artykule),
- obecność inwersji - przesuwanie określonych elementów zdania na jego początek w celu podkreślenia ich znaczenia (np. *W Toruniu w 1473 roku urodził się Mikołaj Kopernik* zamiast *Mikołaj Kopernik urodził się w Toruniu w 1473 roku* - tego przykładu nie ma w artykule).

**Inne cechy tekstów generowanych maszynowo**

![Przykład tekstu wygenerowanego przez GPT‑4 z zaznaczonymi istotnymi cechami stylometrycznymi](https://blog.humanistyka.dev/content/images/20260321205920-ed5219c1159ff8ebac5ee5d16948ac566e6c687ecc25269d920f9d7573d52010.jpg) Przykład tekstu wygenerowanego przez GPT‑4 z zaznaczonymi istotnymi cechami stylometrycznymi. Źródło: [10.1016/j.eswa.2025.129001](https://doi.org/10.1016/j.eswa.2025.129001), 2026.

Omawiane badanie nie analizowało jedynie tekstów generowanych przez LLMy, ale też teksty streszczone automatycznie przez narzędzia takie jak T5, BART, Gensim oraz Sumy, a także teksty sparafrazowane. Okazało się, że metody stylometryczne także dobrze radzą sobie z wykrywaniem takich streszczeń i parafraz. Niektóre z metod generowania streszczeń miały też bardzo specyficzne i łatwe do rozpoznania cechy: przykładowo, model BART generował zazwyczaj małą liczbę krótkich zdań a T5 niepotrzebnie powtarzał w tekście te same litery lub słowa, dodawał też nadmierną liczbę kropek.

Jednak *state of the art* są dziś duże modele językowe i to za ich pomocą generuje się teksty, przedstawiane następnie jako własne. Jakie inne cechy takich tekstów udało się ustalić?

- teksty Wikipedystyczne pisane przez ludzi były bardziej "nasycone faktami", zawierały znacznie więcej dat, liczebników oraz nazw własnych niż wytwory maszynowe (w gatunku hasła encyklopedycznego),
- niektóre modele (np. GPT-4) wykazywały tendencję do nadużywania określonych wyrazów - "significant" (znaczący), "notable" (godny uwagi) czy "despite" (pomimo),
- modele AI mogą mieć specyficzne wzorce interpunkcyjne (np. liczba kropek czy przecinków)
- w tekstach AI (np. wygenerowanych przez model LLaMa 2) często pojawiały się artefakty techniczne, takie jak nadmiarowe spacje (tokeny SPACE) na początku akapitów lub między wyrazami, które rzadko występują w starannie redagowanych tekstach tworzonych przez ludzi,
- wytwory modeli językowych charakteryzują się większą standaryzację gramatyczną i językową niż teksty pisane przez człowieka.

**Ograniczenia stylometrii**

Autorzy badania podkreślają, że metody stylometryczne pozwalają niemal doskonale rozpoznać teksty generowane maszynowo, jednak

> dobrze działające (well-performing) modele nie mają pojedynczych, łatwo rozpoznawalnych cech, lecz ich styl jest bardziej rozproszony wśród wielu zmierzonych cech. Co więcej, wyjaśnienia \[tzn. wartości cech, charakteryzujące maszynowe generowanie\] nie są ogólne, lecz mogą się różnić w zależności od modelu

Warto zwrócić też uwagę, że badanie opierało się na *well-defined text generation task* - teksty wytworzone były wokół treści haseł Wikipedii, stąd miały specyficzne cechy, po których można było je analizować (np. nasycenie faktami):

> Ograniczenia niniejszego artykułu dotyczą głównie materiału poddanego analizie. Po pierwsze, wyniki i konkretne wnioski odnoszą się wyłącznie do wybranego typu tekstu, tj. wstępów (introductions) do artykułów Wikipedii, które mają odpowiadać stylowi encyklopedycznemu: prostemu, rzeczowemu i częściowo sformalizowanemu. Niektóre z najbardziej charakterystycznych cech odzwierciedlają tę specyfikę i nie można ich uogólniać na klasyfikację innych typów tekstów. Jednakże sam proces analityczny można wykorzystać do innych celów po włączeniu w niego specjalnie wyodrębnionych cech, zaprojektowanych i używanych w kontekście tekstów literackich.

Co więcej

> język próbek tekstu ogranicza się wyłącznie do języka angielskiego. Dokładne cechy leksykalne, gramatyczne i inne bardziej złożone właściowści będą inne w przypadku innych języków. Wiadomo, że skuteczność narzędzi stylometrycznych w dużym stopniu zależy od języka, a w szczególności od jego rodzaju

Warto zwrócić uwagę także na to, że teksty źródłowe z Wikipedii, które stały się podstawą całego badania, były pisane przez wielu autorów. W przypadku badań nieuczciwości naukowej czy maszynowych plagiatów w wydawnictwach mamy do czynienia zazwyczaj z jednym autorem/autorką.

Moim zdaniem badanie z UJ to kolejny argument przeciwko skuteczności generycznych detektorów tekstów maszynowych: parametry takiego badania zawsze muszą uwzględniać specyfikę badanych tekstów, kontekst gatunkowy, tematykę oraz możliwość wykorzystania parafraz przez nieuczciwego autora. Dostosowany do specyfiki tekstów proces detekcji może być jednak niezwykle skuteczny, jeśli użyje się w nim miar stylometrycznych.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).
