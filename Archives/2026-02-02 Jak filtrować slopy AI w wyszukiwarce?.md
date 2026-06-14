---
type: Web
authors: '[[Marcin Wilkowski]]'
url: >-
  https://blog.humanistyka.dev/2026/02/jak-filtrowac-slopy-ai-w-wyszukiwarce?utm_source=newsletter&utm_medium=email&utm_term=2026-06-14&utm_campaign=Jak+filtrowa%C4%87+slopy+AI+w+wyszukiwarce+Technologia+venture+capital+i+hype+wojenny+Rozpoznawanie+tekst%C3%B3w+AI+Cyfryzacja+domowego+archiwum+Teologiczny+benchmark+modeli+generatywnych+Nagrania+z+webinari%C3%B3w+o+danych+dziedzictwa
published: 2026-02-02T00:00:00.000Z
created: 2026-06-14T00:00:00.000Z
tags:
  - narzędzia-AI
  - trendy-AI
---


Gdyby istniało niezawodne narzędzie do rozpoznawania treści generowanych maszynowo, wyszukiwarki pozycjonujące się jako alternatywy wobec Google już dawno by z niego korzystały. Tymczasem nadal polegają na listach domen i zgłoszeniach użytkowników. Technicznie problem jest trudniejszy, niż sugerują marketingowe hasła firm AI publikujących komercyjne detektory. Blokowanie slopów AI jest już jednak wyraźną częścią oferty alternatywnych wyszukiwarek, które rozpoznały rosnące zapotrzebowanie użytkowników na internet bez maszynowych wytworów.

DuckDuckGo to rozwijana od 2008 roku wyszukiwarka, której główną zaletą ma być wysoki poziom ochrony prywatności. Po 17 latach budowania wizerunku alternatywy wobec “wszystkowiedzącego” Google, wydawcy DDG starają się skutecznie odpowiedzieć na nowy problem, z którym także Google sobie nie radzi, a być może nawet nie uznaje go za problem. Problemem tym są zalewające wyniki wyszukiwania slopy “AI” oraz maszynowe podsumowania wyników wyszukiwania.

W wakacje zeszłego roku DDG [udostępniło opcję filtrowania slopów z materiałów wizualnych](https://techcrunch.com/2025/07/18/duckduckgo-now-lets-you-hide-ai-generated-images-in-search-results/). Od niedawna pod adresem [noai.duckduckgo.com](https://noai.duckduckgo.com/) dostępna jest wyszukiwarka blokująca generowane maszynowo obrazki oraz ze [standardowo wyłączonym generowaniem streszczeń AI](https://duckduckgo.com/duckduckgo-help-pages/results/ai-assisted-answers). Jak [czytamy na stronach DDG](https://duckduckgo.com/duckduckgo-help-pages/duckai/approach-to-ai),

> \[W DuckDuckGo\] rozumiemy, że nie każdy chce korzystać z AI na co dzień, dlatego wszystkie nasze funkcje AI są opcjonalne i można je wyłączyć lub ograniczyć w ustawieniach wyszukiwarki i przeglądarki \[DDG udostępnia też [przeglądarkę](https://play.google.com/store/apps/details?id=com.duckduckgo.mobile.android&referrer=utm_campaign%3Dstatic-atb-static%26origin%3Dfunnel_home_searchresults)\]

Porównajmy to [z podejściem Google](https://support.google.com/websearch/answer/14901683?hl=en#zippy=%2Chow-to-control-your-data):

> Podsumowania AI są podstawową funkcją wyszukiwarki Google, podobnie jak panele wiedzy. Funkcji tych nie można wyłączyć.

Poza szanowaniem preferencji użytkowników co do stosowania lub unikania AI w procesie wyszukiwania, DuckDuckGo udostępnia też przyjazny interfejs do korzystania z czołowych modeli sztucznej inteligencji (bez logowania i udostępniania danych). Piszę o tym, bo korzystam z [duck.ai](https://duck.ai/) na zajęciach i chciałbym polecić to rozwiązanie jako świetną alternatywę dla ChatGPT czy Google Gemini w warunkach warsztatowych (choćby właśnie ze względu na brak logowania).

**Jak blokować slopy AI?**

Ponieważ na blogu kilka razy pisałem już [o próbach filtrowania slopów AI](https://blog.humanistyka.dev/2025/10/proponuje-sie-juz-certyfikaty-ludzkiego-autorstwa-dla-wydawnictw-i-tworcow) czy [metodach rozpoznawania maszynowo generowanych tekstów](https://blog.humanistyka.dev/2025/12/jak-rozpoznawac-slopy-ai-w-tekstach-na-pewno-nie-maszynowo), zainteresowało mnie to, jak mają działać filtry DuckDuckGo. Czy wyszukiwarka korzysta z jakiegoś komercyjnego narzędzia, mającego rozpoznawać maszynowe wytwory i [czy to rzeczywiście może działać](https://blog.humanistyka.dev/2025/10/wiecej-tresci-w-sieci-tworzy-ai-niz-ludzie-zanim-w-to-uwierzysz-sprawdz-jak-to-policzono)?

Wystarczyło odrobinę poszperać na stronach DDG i okazało się, że do filtrowania obrazków AI wykorzystywany jest indeks [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist). Listy tego typu [rozwijane są przez społeczność](https://majkiit.github.io/polish-ads-filter/) i używane głównie we wtyczkach do przeglądarek, które mają blokować reklamy. Ponieważ jednak slopy AI stały się tak samo wszechobecne i irytujące jak pojawiające się wszędzie reklamy, zaczęto rozwijać indeksy mające blokować także wytwory AI.

Okazuje się, że szybciej i skuteczniej jest ręcznie wskazywać źródła potencjalnych slopów niż korzystać z narzędzi, które będą na bieżąco sprawdzać indeks wyszukiwania i automatycznie wyłapywać te treści po określonych cechach. To oczywiście mrówcza robota, bo źródeł slopów nieustannie przybywa. W repozytorium filtrów [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) znajdziemy plik [`list_uBlacklist.txt`](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/blob/main/list_uBlacklist.txt) identyfikujący hosty upowszechniające tego typu wytwory (tutaj jego fragment):

> '#Sites that have.art domain extension *://*.imagine.art/\* *://*.jasper.art/\* *://*.artgeneratorai.art/\* *://*.nft-generator.art/\* *://*.dreamlike.art/\* *://*.foxify.art/\* *://*.lexica.art/\* *://*.generators.art/\* *://*.pixai.art/\* *://*.dreamerai.art/\* *://*.blueshadow.art/\* *://*.zetu.art/\* *://*.quickqr.art/\* *://*.tensor.art/\* *://*.pixagen.art/\*

Jednak wskazanie hostów nie wystarcza, bo masowym źródłem slopów może być wszystko, nawet wybrane konto na Twitterze czy wątek na Reddicie. Trudno blokować całą platformę, dlatego trzeba wskazywać poszczególne jej części:

> *://*.reddit.com/r/3amAI/\* *://*.reddit.com/r/AIArtCreator/\* *://*.reddit.com/r/AIEscher/\* *://*.reddit.com/r/AIGenArt/\* *://*.reddit.com/r/aisettings/\* *://*.reddit.com/r/AmazingAI/\* *://*.reddit.com/r/ArtIsForEveryone/\* *://*.reddit.com/r/craiyon/\* *://*.reddit.com/r/dallemini/\* *://*.reddit.com/r/dawnAi/\* *://*.reddit.com/r/DimensionTraveler/\* *://*.reddit.com/r/DiscoDiffusion/\*

Blokowanie reklam wydaje się łatwiejsze niż walka ze slopem. W indeksach filtrów takich jak [EasyList](https://easylist.to/easylist/easylist.txt) identyfikowane są serwery (hosty) reklamowe, które publikują reklamy na milionach stron. Rolą tych hostów jest zarządzanie publikowaniem i rozliczaniem reklam, cały system ma więc pewne centralne punkty. Zablokowanie już tylko jednego reklamowego źródła rozwiązuje problem w wielu miejscach. W przypadku slopów tak to nie zadziała, rozpowszechniane są przecież one zupełnie niezależnie - można zablokować wybrane strony czy fora, ale wciąż pojawiać się będą w nowych miejscach.

Rozwiązania informatyczne, [mające pozwolić na skuteczne automatyczne oznaczanie maszynowych wytworów](https://blog.humanistyka.dev/2025/09/synthid-daje-sie-skutecznie-oznaczac-i-wykrywac-teksty-generowane-maszynowo) nie są jeszcze na tyle powszechne, żeby można było je skutecznie użyć w wyszukiwarkach i przeglądarkach. Poza tym na ich zastosowanie zgodzić się muszą wydawcy narzędzi do produkcji tego typu treści oraz wdrożyć odpowiednie mechanizmy w swoim oprogramowaniu. Z pewnością nie wszyscy będą chcieli to zrobić.

**Skąd pochodzą slopy AI?**

Swobodny dostęp do [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) pozwolił mi na szybkie sprawdzenie, jakie są główne źródła slopów wizualnych w internecie (zdaniem edytorów tego indeksu oczywiście). Przetworzyłem sobie [źródłowy plik](https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list.txt) `list.txt` z repozytorium filtrów i zebrałem liczbę wystąpień poszczególnych hostów. Oto lista dwudziestu hostów, z których blokowanych jest najwięcej podstron / profili użytkowników:

| host | liczba\_filtrowanych\_adresow |
| --- | --- |
| reddit.com | 348 |
| pinterest.com | 140 |
| twitter.com | 106 |
| x.com | 104 |
| instagram.com | 88 |
| play.google.com | 44 |
| behance.net | 36 |
| amazon.com | 32 |
| deviantart.com | 30 |
| youtube.com | 22 |
| freepik.com | 16 |
| ko-fi.com | 12 |
| medium.com | 12 |
| adobe.com | 6 |
| apple.com | 6 |
| artstation.com | 6 |
| facebook.com | 6 |
| aigirlfriend.wtf | 4 |
| arthub.ai | 4 |
| astria.ai | 4 |
| blimeycreate.com | 4 |
| designbundles.net | 4 |
| etsy.com | 4 |
| phraser.tech | 4 |
| pixels.com | 4 |
| pokeit.ai | 4 |
| redbubble.com | 4 |
| sarahmeyohas.com | 4 |

Zidentyfikowane źródła slopów AI są bardzo zróżnicowane - prawie 70 proc. listy stanowią hosty, dla których w filtrach zidentyfikowano nie więcej niż pięć bezpośrednich adresów do zablokowania (niestety lista zawiera też powtórzenia). W indeksach filtrów znajdują się często całe witryny, które uznano za szkodliwe. Produkcja slopów jest rozproszona, nie wystarczy zablokować sobie wybranych przestrzeni Reddita, kont Pinteresta czy Twittera/X, żeby nie trafiać na tego typu wytwory w wynikach wyszukiwania.

*Jakościowe* spojrzenie na listę filtrów pozwala dostrzec, że jej twórcy chcą blokować nie tylko same slopy AI, ale też narzędzia do ich produkcji - w tym aplikacje mobilne (stąd stosunkowo wysoka pozycja hostu `play.google.com`) w zestawieniu. Filtrowane są też… książki dostępne na Amazonie (np. [taka](https://www.amazon.com/Kawaii-Sketchbook-drawing-notebook-journal/dp/B0C9S8W4PW)). Na liście filtrów zidentyfikowano ich niecałe 30, więc to zdecydowanie kropla w morzu [potrzeb](https://authorsguild.org/news/ai-driving-new-surge-of-sham-books-on-amazon/).

**Społecznościowe filtrowanie slopów**

Inne podejście do walki ze slopami i generatywnymi wytworami, zaśmiecającymi wyniki wyszukiwania, praktykowane jest w [Kagi](https://blog.humanistyka.dev/2026/02/kagi.com). Kagi oferuje wyszukiwarkę w trybie płatnej subskrypcji, dzięki temu ma udostępniać lepsze wyniki wyszukiwania, pozbawiona jest reklam i - właśnie! - posiada filtry antyslopowe. W grudniu zeszłego roku [pisano tam](https://blog.kagi.com/slopstop), że

> \[Kagi\] wdraża pierwszy społecznościowy system wykrywania i obniżania rankingu zwodniczych treści generowanych przez AI — tekstów, obrazów i wideo — w wynikach wyszukiwania. Jest rok 2025, a internet, który kochaliśmy, tonie w szumie generowanym przez AI. Farmy treści wykorzystujące AI dla zysku manipulują wynikami wyszukiwania w morderczej konkurencji ekonomii uwagi. \[...\] Od roku walczymy ze slopami AI, wtedy wprowadziliśmy filtr obrazów generowanych przez AI. Od początku aktywnie obniżaliśmy pozycje treści o niewielkiej lub żadnej wartości dla naszych użytkowników, do tego pełnych reklam i kodów śledzących, zachęcając i umożliwiając wam przejęcie kontroli nad doświadczeniem wyszukiwania. SlopStop teraz obejmuje szersze spektrum wprowadzających w błąd treści generowanych przez AI: wideo, artykuły, domeny i wszystko, co pomiędzy. Od teraz w wynikach wyszukiwania pojawi się widoczny wskaźnik AI slop score \[dla znalezionych obiektów\].

Oznaczone jako AI slop wideo, grafiki i poszczególne teksty dostępne na wybranych stronach są podstawą do negatywnej oceny całej witryny. Jeśli taka następuje, Kagi [obniża jej ranking](https://help.kagi.com/kagi/features/slopstop.html), podobnie jak robi to z pojedynczymi generowanymi grafikami czy nagraniami znajdującymi się w wynikach wyszukiwania. Wszystkie takie treści są też odpowiednio oznaczane, co pozwala później [filtrować je podczas wyszukiwania](https://help.kagi.com/kagi/features/exclude-ai-images.html). Inspiracją do badania tego, czy dana witryna udostępnia slopy albo czy dany obiekt jest tego typu wytworem, jest sygnał od użytkowników wyszukiwarki - *report \[as AI slop\]*, ale też *report as not AI slop*.

Wykorzystanie takich mechanizmów i pewnie jakiegoś algorytmu oceniającego prawdopodobieństwo tego, że mamy do czynienia ze slopem na podstawie zgłoszeń użytkowników, nie zmienia faktu, że rozpoznawanie slopów tak w przypadku DuckDuckGo jak i Kagi bazuje na indywidualnych ocenach użytkowników. Gdyby komercyjne systemy rozpoznawania wytworów maszynowych były tak skuteczne, jak czasem się o nich mówi, z pewnością zostałyby wykorzystane w opisanych wyżej, alternatywnych wobec Google wyszukiwarkach. To, że wciąż użytkownicy samodzielnie identyfikują i zgłaszają slopy dowodzi, że wciąż brakuje maszynowych rozwiązań tego problemu. Szkoda, bo ich zaletą byłby nie tylko szeroki zasięg działania i szybkość, ale też pewna obiektywność. To akurat ważny wątek, bo to, czy identyfikujemy slop czy raczej uznajemy go za pełnoprawną zawartość sieci, [może mieć związek z naszymi preferencjami estetycznymi](https://blog.humanistyka.dev/2025/07/srednia-pragnien-estetycznych).

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).
