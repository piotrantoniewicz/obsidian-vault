---
type: "Web"
authors: "[[Artur Jabłoński]]"
url: "https://www.youtube.com/watch?v=ba6iphKduG4"
published: 2026-08-20
created: 2026-08-25
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "content-marketing"
---


![](https://www.youtube.com/watch?v=ba6iphKduG4)

Dołącz do AI\_Marketers 3 👉 https://www.aimarketers.pl/  
  
LIVE poprowadzi:  
Artur Jabłoński: https://www.linkedin.com/in/agjablonski/  
  
Zaobserwuj nas, aby nie przegapić kolejnych webinarów:  
AI\_Marketers: https://www.linkedin.com/company/ai-marketers-pl/  
BRAVE: https://www.linkedin.com/company/brave-courses/

## Transcript

**0:01** · \[muzyka\] \[muzyka\] \[muzyka\] Dobry wieczór wszystkim. Słuchajcie, prowadzę webinary, transmisje live, podcasty i tym podobne rzeczy.

**0:29** · Zaraz będzie dekada i jeszcze sobie nie opracowałem żadnego takiego dobrego otwierającego dowcipu albo sposobu, żeby spytać osoby po drugiej stronie ekranu, was wszystkich tam o dwa standardowe pytania, czyli czy widać i czy słychać.

**0:45** · Więc dajcie proszę znać, czy widać i słychać. Jak ktoś ma pomysł na to, jak to pytanie zadać, żeby nie brzmiało za każdym razem tak samo na każdym webinarze w internecie, to chętnie przyjmę. A tymczasem widzę, że pyta, że pierwsze osoby już się z nami witają.

**1:01** · Jest z nami Tomasz, Aneta, Mariusz.

**1:04** · Teraz powinniśmy na jakiś donejtach wyczytywać, ale przede wszystkim Monika napisała, że jest okej, że widać, że słychać. Bardzo się cieszę. Słuchajcie, ja nie lubię przedługich wstępów, więc pozwolę sobie tylko pokrótce powiedzieć jaki jest plan na nasz dzisiejszy wieczór. Zgodnie z tytułem tego webinaru, czyli od zera, od słowa kluczowego do tekstu w godzinę, postaram się zamknąć część merytoryczną nawet szybciej. Myślę, że zajmie nam jakieś 30, 40 minut.

**1:31** · Potem chciałbym wam opowiedzieć chwilę o tym, dlaczego dziś się w ogóle spotykamy, ponieważ jest to kolejny z webinarów przygotowujących do trzeciej już edycji AI Marketers, mojego kursu kohortowego, przez który przeszło ponad 1200 osób w dwóch poprzednich edycjach i wszyscy niezmiennie sobie chwalą, co mnie bardzo cieszy i za co bardzo dziękuję. A potem tak zwana sekcja pytań i odpowiedzi na tematy związane z AI i marketingiem wszelakie.

**1:57** · Do upadłego zawsze zostaję do ostatniego pytania i do ostatniego żołnierza. Więc to, o której skończymy, jest de facto zależne od was. Za moim oknem warszawski zachód słońca. Nie wiem jak tam u was, jak to w tym momencie wygląda, ale możemy przejść już właśnie do rzeczy, bo ta standardowa minutka rozgrzewkowa, która ma pozwolić wszystkim dołączyć i zobaczyć, że działamy, jest już chyba za nami. Moi drodzy, dzisiejszy webinar będzie ode mnie wymagał skakania między szeregiem rzeczy, żeby pokazać wam właśnie krok po kroku co i jak.

**2:27** · I nie martwcie się, na początek będzie kilka slajdów, ale są to wyłącznie slajdy na otwarcie mające wprowadzić nas w temat, ponieważ muszę wam wprowadzić kilka pojęć, kilka narzędzi, na których będę dziś pracował, a następnie przełączę się na swojego cloud coda, żeby pokazać wam właśnie cały ten proces budowy tekstu krok po kroku w godzinę i ich optymalizowania, jak to w zasadzie wygląda i z czego taka optymalizacja się składa.

**2:55** · Ale zanim w ogóle o tym, to myślę, że najważniejszym pytaniem, które należałoby zadać jest okej, czy to w ogóle działa? Dlaczego takie pytanie na początek warto sobie postawić?

**3:07** · Słuchajcie, bo świat jest pełen gotowców z internetu, gotowców, które mają za zadanie rzekomo pomóc wam robić jakieś rzeczy i bardzo łatwo jest wziąć gotowy skill z internetu, gotowe prompty z internetu, wyprodukować coś i wrzucić. I jest pełno filmów na YouTubie na ten temat, jak opublikować 200 tekstów w 20 minut czy cokolwiek rzekomo z pomocą AI.

**3:30** · Natomiast mało kto pokazuje, czy coś takiego w ogóle daje jakiekolwiek zwroty i efekty. I powiem wam szczerze, że nie daje. Ja też zanim zacząłem publikować i tworzyć własne materiały, to długo szukałem kogoś, kto mnie zbawi, czyli takiego zewnętrznego źródła publiczne dostępnego i najlepiej za darmo, które właśnie przeprowadzi mnie przez coś takiego. Testowałem na sobie, na żywym organizmie, nie zadziałało. W końcu się wkurzyłem, zacząłem pisać własne.

**3:52** · I odkąd zacząłem pisać samodzielnie, to to tylko kilka przykładów, bo ja wszystkie eksperymenty robię na własnej domenie, w sensie na albo na arurjabłoński.com, albo digitok.pl i suasio.pl, czyli stronach moich firm. W zaledwie miesiąc, a w zasadzie no powiedzmy półtora, żeby być ścisłym, udało mi się zwiększyć widoczność organiczną mojego serwisu o blisko 30%, zwiększyć o 74 liczbę fraz w

**4:18** · top 10, to też jest praktycznie jakąś 10, w top 3 o 16 czy nowych poston w top 10 o 32 in plus i praktycznie wszystkie publikowane wówczas treści albo optymalizowane treści od tego czasu idą wyłącznie w górę praktycznie każdy nowy tekst na tematy, jak to widzicie, głównie wokół AI, no bo tym się na swojej stronie głównie przede wszystkim obecnie zajmuję, choć nie tylko, to każdy z nich ląduje praktycznie po takim procesie, który będę wam pokazywał dzisiaj w pierwszej dziesiątce.

**4:49** · A wszystko co było optymalizowane, w tym tak ważne dla mnie frazę, jak to się ładnie mówi, money pages, wdrożenie AI w firmie z pozycji na przykład czwartej nawet na jeden na 1,6, są to dane uśrednione z Senuto i Google Search Console. Zresztą co ja będę mówił? Seeing is believing. Pokażę wam po prostu ten właśnie fragment.

**5:11** · To jest mój ulubiony fragment, bo zawsze się ludzi pytam, kiedy im pokazuję ten wykres. Wskażcie mi palcem datę na wykresie, kiedy agentami AI zacząłem samodzielnie optymalizować mój serwis.

**5:23** · Myślę, że łatwo zauważyć, że ten bodajże 13 lipca, od którego te wszystkie skoki się zaczęły, to są właśnie te czasy, w których to zacząłem. Analogicznie to wygląda również na innych serwisach. Na tych agentach pracujemy również obecnie w mojej agencji i dzięki temu osiągamy coraz lepsze wyniki. I dziś pokażę wam właśnie jak tego typu system można zbudować również u siebie. Ale żeby zacząć to potrzebujemy sobie najpierw wytłumaczyć czego będziemy potrzebowali. Jak głosiło stare powiedzenie, żeby ściąć drzewo, trzeba najpierw poświęcić godzinę na ostrzenie piły.

**5:53** · I potrzebować będziemy trzech rzeczy, ale tak naprawdę w kilku odmianach.

**6:01** · Więc niby trzech, tak naprawdę ciut więcej. I czym one będą po kolei?

**6:06** · Pierwszą sprawą będzie cloud code.

**6:08** · Zakładając, że nie wszyscy z was są osobami, które na co dzień pracują jakoś mocno ze struczną inteligencją, to warto w tym momencie napomknąć, że większość tych aplikacji głównych towarzyszących LLMom jest dostępna w kilku wersjach.

**6:21** · Jest sobie po prostu czat dostępny przez internet, tak jak właśnie chatg czy cloud.ai.

**6:27** · Jest dostępny również na przykład tak zwany cork, czyli narzędzie pośrednie do wykonywania zadań oraz jest cloud code i i chat GPT Codex obecny po prostu zwany chatem GPT, czyli narzędzia do kodowania, rzekomo wydawałoby się z nazwy, ale tak naprawdę właśnie do projektowania i wykonywania dla nas zadań, w tym również zadań programistycznych, ale nie wszystkie nasze zadania muszą być programistyczne, więc jak kogoś code w nazwie przeraża, to oczywiście już nie musi i mam nadzieję, że tak właśnie nie jest.

**6:56** · A jak ktoś z CODA korzysta, to jestem bardzo ciekawy, czy korzystacie. Dajcie w tym momencie znać w komentarzu.

**7:06** · Drugą rzeczą, której będziemy potrzebowali i którą głównie będę wam prezentował przez tą pozostałą część webinaru, to są tak zwane zbudowane samodzielnie skille. Dajcie również znać, kto na co dzień ze skill korzysta, bo dla mnie tego typu webinar jest też okazją do zobaczenia, jaki jest już poziom wyjściowy wiedzy ludzi. Żeby natomiast tym z was, którzy niekoniecznie na co dzień jakoś korzystają dużo ze skil w ogóle z AI wytłumaczyć, to wyobraźcie sobie, że skill jest swego rodzaju instrukcją wykonania łańcucha promptów.

**7:35** · Czyli na przykład jeżeli opracowywalibyście właśnie tekst optymalizowany pod SEO i żeby go zoptymalizować wykorzystywalibyście 10 15 różnych komend, czyli promptów po kolei, żeby naslić słowami kluczowymi, sprawdzić coś tam, dodać link wewnętrzny i tak dalej, to jeżeli już tylko doszlifujemy to jako powtarzalny proces i będziemy chcieli następnie sobie to powtórzyć na kolejnych tekstach, to nie będziemy musieli przechodzić całego tego procesu promptowania.

**8:07** · pojedynczo, tylko zwyczajnie robimy z tego tak zwany skill i w zasadzie tworzone samodzielnie skille to najlepsza rzecz, jaką możemy dla swojego marketingu i dla wykorzystania AI w marketingu właśnie stworzyć. I wreszcie element trzeci, czyli narzędzia zewnętrzne po MCP lub API. Nie wdając się w szczegóły, chodzi po prostu o połączenie naszych modeli AI.

**8:28** · Czy to będzie chat GPT Codex, czy to będzie clot, na którym ja najczęściej pracuję z innymi zewnętrznymi narzędziami, z których będziemy na przykład pobierać dane albo z pomocą których będziemy chociażby publikować stworzone treści na naszej stronie. I tu ważna informacja.

**8:48** · Czy można się bez tych narzędzi obyć?

**8:52** · Można, bo na przykład jeżeli tworzycie materiały na konkretne słowa kluczowe, które są dla was logiczne, w branży oczywiste i tak dalej, to może nie będą potrzebne wyciągane dane z jakichś narzędzi, ale zawsze jeżeli możemy sobie tylko na to pozwolić, warto się wspierać wyspecjalizowanymi narzędziami, żeby tego typu informacje dodatkowo wyciągać.

**9:13** · Szczególnie, że pod koniec tego spotkania mam dla was taki trochę twist w tym webinarze. Informacje z tychże narzędzi mogą nam uratować, mówiąc tak kolokwialnie, tyłek. I tak naprawdę to jest wszystko, czego potrzebujemy. Trzy rzeczy w kilku smakach. I ja mogę w tym momencie wyłączyć właśnie część prezentacyjną i wejść już bezpośrednio do Cloda, żeby po kolei was przez ten cały proces przeprowadzić. A chyba jedyną rzeczą, którą w tym momencie muszę zrobić, to jest troszkę swój ekran powiększyć.

**9:43** · Dajcie proszę znać, czy jest to w miarę czytelne, bo ja widzę tutaj to na podglądzie, a niekoniecznie właśnie w takiej formie, jakiej być może widzicie to właśnie wy.

**9:56** · Teraz mała gwiazdka na końcu zdania. Nie będziemy tego promptować y na żywo, ponieważ gdybym próbował teraz cały proces przechodzić na żywo, to w tym momencie no zajęłoby to właśnie godzinę i dużo byśmy tak czekali i patrzyli jak maszyna się kręci, mieli tokeny i tak dalej. Więc ja przygotowałem to wszystko zawczasu, żebyśmy mogli sobie teraz w szczegółach całą rzecz omówić, aby ci z was, którzy chcieliby analogiczną rzecz spróbować zbudować dla siebie, po prostu to w tym momencie zrobili. I jednocześnie jednym okiem staram się monitorować na bieżąco czat.

**10:26** · Więc jeżeli będziecie mieć jakieś pytania w trakcie do rzeczy, które będę tłumaczył, to je wrzucajcie. Jeżeli coś będzie bezpośrednio wynikało z tego, co czy nawiązywało do rzeczy, o której mówię, bo niekoniecznie coś dobrze wytłumaczę i tak dalej, to od razu się odniosę. A jeżeli nie, to proszę o cierpliwość.

**10:44** · Będziemy flagowali te pytania właśnie na część questions and answers. I to powiedziawszy możemy rozpocząć od pierwszego mojego prompta w tejże sesji, tej konwersacji właśnie w Cloud Codzie, z którego korzystam, która zaczyna się od dziwnej rzeczy, od komendy Watch. Jest tam następnie link do filmu na YouTubea, na YouTubie i następnie komenda brzmi: "Obejrzyj ten film i zrób pełny transkrypt. Wypisz w trzech, czterech punktach o czym jest i jakie ma główne wątki". Czyli już pierwsze zdanie i już kilka rzeczy, którą muszę w tym momencie rozpakować.

**11:19** · Pierwsza sprawa, dlaczego tutaj w ogóle się pojawia link do YouTubea?

**11:24** · Są dwa sposoby, w jaki możemy zrealizować treści z pomocą czy tworzyć treści z pomocą AI. Pierwsze to tworzenie tych treści absolutnie od zera. I jest to rzecz, którą wszyscy chcieliby zrobić. Jest to coś takiego, wiecie, taki święty gral, nie? że w tym momencie wpiszemy po prostu komendę napisz mi artykuł na temat X i system to zrobi. I teraz czy system taki materiał zrobi? Tak, zrobi.

**11:50** · Co więcej, czy takie treści mogą się pozycjonować? Owszem, mogą, ale równie szybko, jak się pozycjonują i to mi się również udaje robić, to równie szybko mogą w tym momencie odpaść, mogą stracić pozycję. To są najszybciej fluktuujące treści, ponieważ AI bez żadnego wsadu z waszej strony tworzy po prostu materiały generyczne. Plus jednocześnie dla mnie takim bardzo ważnym wątkiem, który w tym momencie muszę poruszyć jest zwyczajnie kwestia etyczna.

**12:15** · Czy publikowanie czegoś pod swoim nazwiskiem czy pod marką swojej firmy, co powstało jako tak naprawdę patchwork z treści zebranych z internetu jest czymś, co chcecie robić i pod czym właśnie chcecie się swoją marką i nazwiskiem podpisywać. może niekoniecznie.

**12:32** · Więc zamiast tego lepiej przygotować jakiś materiał, na podstawie którego będzie mogło daną treść, w tym wypadku artykuł dla was stworzyć bądź ewentualnie będzie mogło się nią przynajmniej częściowo posiłkować bądź wspierać. I w moim wypadku, ponieważ prowadzę chociażby kanał na YouTubie, na którym właśnie to oglądacie, albo komunikację na LinkedInie, jeżeli akurat stamtąd przyszliście, to są możliwości spore, bo ja tych materiałów, odcinków mam, ale to nie musi być film na YouTubie.

**13:02** · To może być głosowa notatka, którą przygotujecie zawczasu i wrzucicie do systemu, żeby w tym momencie z tego korzystał. To mogą być na przykład transkrypcje z waszych rozmów sprzedażowych albo z waszych rozmów wewnętrznych. Mój na przykład jeden z procesu tworzenia tekstów polega na tym, że ja mam podpiętą tak zwaną aplikację Fireflies, która na bieżąco skanuje pod kątem ciekawych pytań, problemów, obiekcji i materiałów merytorycznych rozmowy zespołu z klientami.

**13:31** · Oczywiście na na nagrywanie których klienci się zgadzają. i potem wyciągam sobie z tego wątki, którymi uzupełniam materiały, które tworzę, bo pojawia się jakiś ciekawy problem czy ciekawa wypowiedź klienta albo mojego mojego pracownika.

**13:46** · Więc w tym wypadku posłużymy się YouTubem, ale nie chciałbym, żeby w waszej głowie zakłotwiczyła się taka myśl, że aha, to jak my nie tworzymy podcastów, youtubów i tak dalej, to nie jest droga dla nas. Materiały wewnętrzne, pliki wewnętrzne są do tego wystarczające, ale przydatne będzie coś, co może być po prostu próbką waszej po pierwsze merytoryki, a po drugie waszego stylu, które to AI ma taki zwyczaj nazywać tak zwanym głosem, do czego jeszcze przejdziemy. Więc to pierwsza sprawa, dlaczego w ogóle wychodzimy od filmu na YouTubie. I druga sprawa to jest ta komenda watch.

**14:18** · Ci, którzy nie znają to właśnie ukośnik i jakaś nazwa to jest sposób w jaki wywołuje się w konwersacji z AI skille. W tym wypadku a propos polecania i udostępniania skil skill watch to jeden z moich absolutnie ulubionych skil, którym polecam wszystkim i który każdy powinien sobie zainstalować. Instalacja skil nie jest szczególnie niczym trudnym. Dlatego właśnie widzę, że Remi pisze, że komenda nie jest znana tutaj nam w komentarzu.

**14:44** · No właśnie, bo to jest skill, który musisz ściągnąć i zainstalować. My w podsumowaniu tego webinaru, który otrzymacie na maila, te osoby, które zapisywały się mailem, podeślemy listę skąd te skille bezpiecznie pobrać.

**14:56** · Ten skill, moi drodzy, ogląda materiały zarówno na YouTubie, jak i na przykład na TikToku czy na Instagramie, co rozumiem przez ogląda. Czasami jak wrzucacie do Gemini czy do czata na przykład stronę z jakimś filmem z YouTubea, to on po prostu szczytuje automatyczne napisy, ale nie ma pojęcia co jest pokazywane na ekranie. Skill Watch faktycznie to ogląda i robi na przykład co kilka klatek albo co kilka sekund screeny, żeby powiązać to, co jest widoczne na ekranie z tym, co wy w tym momencie macie również w opisane.

**15:26** · Więc jeżeli ja pokazuję jakieś wykresy i tym podobne rzeczy, to on jest to w stanie uzupełnić o rzeczy, które są pokazywane na ekranie. Dlatego tak jak nasz tutaj widzę na komentator Domseo mówi, że ja mu mówię pobierz transkrypcję, to skill watch jest pod tym kątem na wyższym poziomie. bardzo się przydaje na przykład do jednej rzeczy, którą uczymy na AI Marketers i będziemy uczyli w trzeciej edycji i wykorzystywanie AI do montażu materiałów, bo skoro może je obejrzeć to może je również zmontować.

**15:56** · I to spół drugi z trzech wątków przy zaledwie pierwszym prompcie. Zobaczcie jakie to to takie rzeczy się dłużej omawia niż się je realnie robi.

**16:04** · I napisane jest to w ten sposób: "Obejrzyj ten film, zrób pełny transkrypt, no bo on go obejrzy, może go zrobić, wypisz w trzech, czterech punktach o czym jest i jakie ma główne wątki. I teraz uwaga. Dlaczego w ten sposób? Pierwszą rzeczą, którą zawsze warto zrobić w AIu jest właśnie poprosić go o podsumowanie materiału, żebyśmy wiedzieli, czy on go w ogóle rozumie. W tym wypadku on właśnie wyciągnął pełny transkrypt. To jest mój odcinek, no bo wie kim jestem, więc wie, że jest. Jest to odcinek, który nagrałem jakiś czas temu o lit magnetach w dobie AI.

**16:28** · O tak autotelicznie dzisiaj sobie o tym rozmawiamy i wyciągnął z jego kilka wątków. Żeby was nie zanucać, nie zanudzać, polecam ten materiał w ogóle tutaj wszystkim oglądającym i to jest w ogóle ten moment, że jeżeli jeszcze nie subskrybujecie mojego kanału, to gorąca prośba o suba. W każdym razie główne wątki, które się pojawiają, taka teza wyjściowa jest to, że AI zabiło klasyczne lit magnety, ebooki i tak dalej, bo nikt już nie pobiera 300 strrońcowego ebooka, skoro chat GPT Clot daje spersonalizowaną odpowiedź na to samo pytanie. od ręki.

**16:59** · Wobec tego potrzebujemy tworzyć nie ebooki, a na przykład narzędzia, które dają konkretny rezultat. Czyli jest to wątek idealny do przerobienia właśnie na jakiś artykuł.

**17:10** · Więc mogę sobie w tym momencie zobaczyć i sprawdzić i zawsze warto to zrobić, czy system zrozumiał w ogóle jaki jest przekaz, wokół którego chcę coś budować.

**17:18** · I następnie pyta mnie, co bym chciał, żebym z tym zrobił. Czy artykuł na bloga, czy karuzelę, bo na to również mam skilla, czy na przykład rzeczy gotowe pod publikację na YouTubea.

**17:27** · Natomiast ja mam drugiego prompta.

**17:30** · Na podstawie tematu tego filmu dobierz mi słowo kluczowe pod artykuł na blog.

**17:34** · No bo od słowa kluczowego musimy zacząć.

**17:37** · I uwaga, skrzyżuj senuto volumeny.pl z achrews Kadesb spokojne, zaraz wytłumaczę i daj jedną główną frazę.

**17:45** · Uzasadnij podając wolumen trudność i intencje oraz trzy, cztery frazy poboczne do wplecenia. To jest ten moment, którym zawsze lubię pokazać, w którym różni się pomiędzy osobą, która wie co robi i wykorzystuje AI kontra osobą, która nie wie co robi i wykorzystuje AI. I to jest ten powód, żeby uwierzyć, że AI wam nie zabierze pracy, jeżeli się znacie na pracę, którą wykonujecie albo potraficie tę wiedzę z pomocą AI pozyskać, bo specjalista, który AI wykorzystuje będzie zawsze lepszy od laika, który dopiero goni go również na poziomie wiedzowym.

**18:13** · I to jest ten moment, w którym wracamy do tego, co pokazywałem jakiś czas temu na slajdzie, czyli właśnie tych trzech niezbędnych nam rzeczach. Ja mam dwa ulubione narzędzia do robienia różnego rodzaju analiz, widoczności i pozycjonowania stron w internecie. Jednym jest polskie seruto oraz drugim jest Achrebs, globalny lider. Każde z nich jest lepsze pod jakim względem. Na przykład to nie jest przypadek, że powiedziałem przy Senuto volumeny.pl.

**18:42** · Po prostu Senuto ma lepsze pokrycie polskiego rynku. i potrafi lepiej na przykład zbierać frazę długiego ogona. Z kolei Achrebs ma kilka swoich takich prywatnych oznaczeń czy parametrów, które bardzo się przydają w pracy. Na przykład tak zwane KD z angielskiego keyword difficulty, czyli trudność słowa kluczowego. Wiedząc jaka jest, czy wynosi 1, 10, 30, 50, maksimum to 100, to w tym momencie mogę stwierdzić czy da się wbić moim artykułem na coś takiego.

**19:13** · A Serb to z kolei analiza wyników wyszukiwania. Nieważne. Ważne jest to, że ja w tym momencie sięgam po wiedzę z zewnętrznych narzędzi, które mam po prostu podpięte, spięte z klodem po to, żeby wyciągnąć dane. I to jest swoją drogą tak na marginesie mówiąc sposób pracy przyszłości. Ja nie muszę się teraz ręcznie logować w tych wszystkich narzędziach, żeby tego użyć, tylko te narzędzie clot naprawdę wykona w tym narzędziu pracę za mnie. Ja nawet nie muszę znać i rozumieć paneli. Ja nie pamiętam, kiedy się ostatnio raz do Sanuco zalogowałem. O, zalogowałem się dzisiaj, żeby zrobić te screeny dla was.

**19:45** · Resztę wyciągam już wyłącznie z kloda.

**19:48** · Natomiast czy moglibyśmy ten krok pominąć i zrobić to bez tych narzędzi?

**19:53** · Tak, moglibyśmy tak zrobić. Natomiast wówczas nie mielibyśmy tej pewności, która wynika z faktu, że faktycznie widzimy realny wolumen, faktyczną liczbę wyszukiwań i tak dalej. moglibyśmy bazować wyłącznie na swoich narzędziach albo darmowych narzędziach takich jak na przykład Googleowy, Google Search Consol. W każdym razie tym krokiem no może nie niezbędnym, ale na pewno wskazanym jest właśnie przejście czegoś takiego, żeby ustalić na jakie słowo kluczowe warto byłoby tutaj y celować.

**20:19** · I co jest myślę dość logiczne, system w tym momencie uważa, że właściwą frazą będzie lit magnet jako fraza główna i podaje mi informacje, o które prosiłem.

**20:33** · Trudność jest praktycznie zerowa w tym wypadku wolumenu. Widzimy porównanie.

**20:36** · Achre wskazał 500 wyszukań miesięcznie, a z kolei Senuto 590, więc 20% różnicy to już jest sporo. Temat to lit magnety.

**20:45** · Odpowiedni Serb też występuje i jest to nawet fraza, którą warto walczyć, bo generalnie biznes płaciłby za tego typu ruch. element to oczywiście uzasadnił i podpowiedział mi również kilka potencjalnych fraz pobocznych, których należałoby użyć pisąć taki tekst.

**21:04** · Teraz uwaga, trzecim promptem, bo będzie ich chyba łącznie z sześć, które trzeba zrobić, żeby cały ten proces przejść, jest kolejny skill, artykuł głos. Ale to już jest skill stworzony bezpośrednio przeze mnie, dlatego nie ma angielskiej nazwy, tylko taką dziwną. Głos, tak jak mówiłem, jest coś, z czym dawno przestałem walczyć, czyli sposób w jaki AI piszą o stylu. To jest po prostu kalka anglojęzycznego voice. I temat jest następujący. Z transkryptu tego filmu napisz artykuł na blog w moim stylu. Główna fraza lit magnet.

**21:31** · Frazy poboczne wpleś naturalnie potem odpalimy neuron writera, zaraz wyjaśnię i dokoksimy to pod SEO. I to jest moment, w którym chciałbym wam wytłumaczyć dlaczego ja tego tak naprawdę nie załatwiam jednym promptem. Skoro mam proces, o którym potem wam jeszcze szerzej powiem, czyli łańcuch skil wywołujących się po kolei, to dlaczego ja po prostu nie wszedłem i napisałem od razu wszystkich tych poleceń. Wejdź na YouTubea, zrób transkrypcję, dobierz frazę, wrzuć keywordy, napisz artykuł to, na czym jesteśmy i potem odpal tego naon w ritera, którego być może część z was nie zna i należałoby go omówić.

**22:02** · Czy mógłbym tak zrobić? Owszem, mógłbym. Co więcej, ja już tak robię i pokażę wam to pod koniec dzisiejszego spotkania, ale wam sugeruję zrobić to w rozbiciu prom po promcie, który dzisiaj pokazuje z dwóch powodów. Pierwszy jest pierwszy to, którego to zrobiłem jest to, żeby móc wam to pokazać, bo gdybym tego nie rozbił na poszczególne etapy, to nie mógłbym tego w tym momencie wyjaśnić.

**22:27** · Ale drugim powodem, dla którego to zrobiłem, jest to, że po to, że być może właśnie na jakiś innych wersjach cloda mógłby on wam się zwyczajnie wywalić, albo skończyłyby wam się tokeny, albo system zgubiłby kontekst i okazałoby się, że nie rozumie w pełni polecenia.

**22:44** · Możliwość robienia czegoś jednym skomplikowanym promptem albo wywoływanie szeregu komend łańcuchem skili jest możliwe wtedy, kiedy przeszliśmy dany proces już wielokrotnie i zbudowaliśmy sobie coś, co za chwilę wam pokażę, tak zwane bramki, że system potrafi sam siebie korygować, sam siebie poprawiać, wyłapywać swoje błędy. Za pierwszym razem lepiej taki proces rozbić na atomy, co jest generalnie bardzo podobne do nauki czegokolwiek. Nie uczymy się na gitarze naraz grać wszystkiego, tylko uczymy się jedną ręką, potem drugą, podobnie zresztą na pianinie.

**23:15** · Więc jest tutaj jak z każdą inną dzieliną nauki system też musi się w ten sposób nauczyć.

**23:24** · I jednocześnie jest też drugi powód, o którym powiem za chwilę, ponieważ system użył tego mojego skilla, odpalił go, odpalił i na czym ten skill polega, bo to bym wam chciał wyjaśnić. Pierwszą sprawą, którą dobrze zbudowany skill tego typu robi, to odpala tak zwaną bramkę głosu. Pierwszą rzeczą, którą musicie sobie przygotować i między innymi tego, jak to zrobić uczymy właśnie w AI Marketers w taki sposób, żeby było to skuteczne, to przygotować poradnik, którym dzięki któremu system zgodnie z nazwą, którą widicę tutaj wie jak pisać tak jak wy.

**23:55** · Od jakości tego poradnika jest zależne, czy system w ogóle będzie potrafił pisać waszym stylem, a nie brzmieć jak typowy AI slop. w zasadzie nie ma gotowego skilla w internecie, który potrafiłby oduczyć AI takich typowych AIowych sztuczek, które wszyscy znamy. To nie X, to Y, krótkie akapity, pełne dramatyzmu zdania i tak dalej, i tak dalej. No w zasadzie myślę, że już wszyscy powoli mamy taki radar wykrywania takich rzeczy.

**24:22** · Więc dla każdego krytycznym aspektem własnej pracy jest przygotowanie wspólnie z a dokumentu, jak wy w ogóle piszecie, takiego, którym rozumie i potrafi wytłumaczyć właśnie wasz głos.

**24:34** · Przykładowo w takich rzeczach, które system ma u mnie ma dwa rejestry. To taka ciekawostka dla z was, którzy tak pracują, bo ja na przykład inaczej piszę piszę sobie szkice pod LinkedIna, a inaczej piszę sobie artykuły na podstawie YouTubea.

**24:49** · I ciekawostka, żeby tak powiedzieć i zobaczyć co, jak bardzo AI potrafi rozumieć człowieka, o mnie pisze tak.

**24:57** · pisze, że najpierw stawiam dwa skrajne obozy, po czym oba odrzucam na rzecz trzeciej drogi, albo że mam charakterystyczne podwajanie form rodzajowych. Chciałabyś bądź chciałabyś wrzucił, wrzuciła i rzeczywiście tak robię i nigdy nie chowam się za eksperci mówią: "Nazywam konkretne źródła z autorem i rockiem albo biorę opinię na siebie". Mechanika zdań, fragmenty zdaniowe, samokorekty wmówione wpisane w styl, nie tyle atakowany, ile muszę odpierać. Słownictwo formalność 6 na1 profesjonalno potoczna, jakkolwiek dziwnie by to nie brzmiało. Na przykład dosadność kolokwializmy, ale też anglicyzmy.

**25:27** · Jak mawiają anglosasi tu jeżeli jest ktoś z mojego zespołu, to się na pewno śmieję, bo to jest coś, po czym zawsze robią. Czy system nawet rozpoznaje jakieś moje fraze sygnatury, że często mówię na przykład o życzliwej uwadze, czy używam sformułowania, co prowadzi nas do. Jest to w ogóle ciekawa sprawa. Człowiek może zrozumieć sam siebie dzięki w tym momencie AI. Więc to jest pierwszą rzeczą, którą system w tym momencie musi zrobić. Czegoś takiego właśnie uczymy w A marketersach jak to przygotować.

**25:52** · A drugą rzeczą, którą robi to czyta, a raczej dobiera z całego takiego długiego repozytorium, które mam przygotowane teksty wzorcowe i kontekstowo wybrał, że takim dobrym wzorcem z moich poprzednich tekstów do napisania tego nowego będzie tekst o remarketingu na Facebooku, jak go uruchomić, dlaczego przypalasz budżet.

**26:12** · Więc w tym momencie system nakłada sobie jakby dwie soczewki. bierze zarówno te moje reguły stylu i bierze przykład i żadna z tych rzeczy nie zadziała w pojedynkę. Dużo ludzi robi takie poradniki pisania jak my i potem próbuje je zaadaptować, ale system nie ma się czym podeprzeć i to nie wypala. Z kolei inni po prostu biorą 10 przykładów, wrzucają do AI i mówią: "Pisz tym stylem". Ale to są bardzo wymieszane style, niewiele z tego wynika i potem człowiek się dziwi, że to dalej nie brzmi tak jakby się chciało. Jak na wszystko, również na pracę tego typu Zi trzeba mieć właściwy proces.

**26:43** · W każdym razie system coś takiego przeszedł i odpalił nam artykuł, który wygląda w ten sposób. Oto jego pierwsza wersja. Lead magnet w dobie AI. Dlaczego ebook przestał działać i co daje Lidy zamiast niego. Teraz pozwolę sobie przeczytać tylko fragment, żebyście zobaczyli jak bardzo różni się to od takiego typowego AI tekstu, nawet sposobem budowania dynamiki zdań.

**27:09** · Po co mam pobierać kolejnego ebooka na 3, 30 czy 300 stron, który ma mi pomóc rozwiązać jakiś biznesowy problem, skoro mogę spytać dowolnego czata, cloda, perplexity i chat GPT wreszcie i uzyskać spersonalizowaną, dopasowaną do mnie, pamiętającą o kontekście mojej firmy odpowiedź na dokładnie to samo pytanie.

**27:25** · bardzo długie zdanie, co być może zauważyliście. Ja na tym webinarze również takie buduję, więc system się tego nauczył. normalnie AI pisze krócej, więc podłapał dokładnie moje, jak to się piękne polskie słowo mówi, idiosynkrazje, czyli dziwne rzeczy, które ja używam i właśnie też tendencje do tworzenia długich zdań, dzięki czemu nie brzmi to już na tym etapie, mimo że jeszcze nie skończyliśmy naszej reakcji i edykcji jak typowy tekst z internetu.

**27:52** · Ale co następnie system odpalił, bo ma wpisany w mojego skilla. Kolejny skill, który mogę wam polecić, ponieważ jest gotowcem do pobrania w internecie.

**28:02** · Gdybyście mieli sobie zainstalować tylko taki obok tego Watchapowy skill z internetu, to niech to będzie skill o pięknie brzmiącej nazwie humanizer. Uczłowieczacz. Co za czasy w ogóle, że maszyna musi coś napisać, a potem jeszcze musi to uczłowieczać. Jest sobie taka jedna strona na Wikipedii, którą zawsze ludziom polecam. Ta strona nazywa się Science of AI Writing.

**28:23** · Sygnały, że coś jest napisane przez AI.

**28:26** · Jest to jedna z najlepszych rzeczy, ponieważ można ją wziąć i zobaczyć właśnie rozpiskę tych wszystkich typowych, jak to się mówi po angielsku, a tells, czyli elementów w tekście, chwytów literackich, które zdradzają, że tekst jest napisany przez AI. Sztuczny dramatyzm, krótkie zdania i tym podobne.

**28:43** · To oznacza, że w tym momencie humanizer jest skillem, który jest nauczony bardzo prostej rzeczy. Pobiera tamte, tamte elementy i sprawdza, czy są w waszym tekście.

**28:56** · Więc robi po prostu sobie tak zwaną listę chwytów i tekst i elementów w tekście zakazanych i odpytuje zdaniu po zdaniu wasz tekst, czy się one w nich znajdują, żeby je poprawić i usuwać. Ale jak widzicie, ja nie użyłem tylko tego skilla z internetu. Użyłem go razem z moimi skillami.

**29:15** · Dlaczego? dlatego, że rola humanizera, co jest to napisane wprost przez samego cloda, to jest wyłapać realne tiki AI, ale nie ruszać moich cech, na przykład mówienia stęk w tym, podwajania rodzaju czy reguła trójki. Wymieniana rzeczy trójkami, co jest starym dobrym chwytem literackim, ale dzisiaj zostało uznane za typowy element AI, mimo że niekoniecznie musi być. natomiast na przykład usuwa te tak zwane długie myślniki, takie typowo wordowskie i parę innych rzeczy, żeby stworzyć taki tekst.

**29:46** · A następnie uruchamia jedną ostatnią rzecz moją rzecz, którą każdemu z was również polecam sobie zaprojektować tak zwanego u mnie polonista gate. Czym jest polonista gate? Jakkolwiek to dziwnie brzmi, ja jestem z wyksztacenia polonistą, co bardzo pomaga w komunikacji i rozumieniu komunikacji z AI i jednocześnie właśnie poprawce takiego stylu.

**30:08** · Bramka polonistyczna to po prostu kolejny skill, który system musi odpalić, co zresztą widzimy po nazwie, mój prywatny skill, który następnie tak napisany tekst rozkłada na kilku poziomach. W poziomie gramatyki, w tym na przykład błędów, rytmu zdań i na przykład sposobu prowadzenia narracji.

**30:27** · Jeżeli ktokolwiek z was próbował zmusić AI właśnie nawet takimi publicznie dostępnymi z internetu skillami do poprawy stylu, to wie, że średnio mu to wychodzi. Dlaczego? dlatego, że większość takich publicznie dostępnych skil jest robiona w oparciu o język angielski, a jednak sposób pisania tekstów po angielsku drastycznie różni się od tego, jak my jako Polacy budujemy, składamy zdania i tak dalej.

**30:53** · Więc jeżeli działacie na rynku globalnym, to jeszcze pół biedy.

**30:56** · Jesteście sobie w stanie spokojnie takie rzeczy przejść. Natomiast jeżeli działacie na rynku polskim to sprawa się w tym momencie komplikuje, bo właśnie artykuł nawet po wszystkich możliwych bramkach i skilach z internetu nie będzie spełniał. Czyś Polak spojrzy i zobaczy, że to są kalki językowe z angielskiego, a mój polonista gate właśnie tego unika. Osoby, które zapiszą się na AI Marketers 3, właśnie te wszystkie moje skille będą otrzymywały i nie będą musiały budować sobie takich bramek samodzielnie, żeby AI w tym momencie to poprawiało.

**31:26** · Więc to jest jeszcze jeden powód, żeby w tym momencie dołączyć. Możemy zobaczyć na czym polega coś takiego. Przykładowo soczewka druga sprawdzająca rytm i system czyta mój moje przykłady i wskazuje miejsca. Na przykład linia 73 napisał w artykule wyciągnij, bo wszyscy jesteśmy wiecznie zajęci. nieleniwi po prostu zajęci i zaklasyfikował to jako antytezę zamykacz. Na tej podstawie zmienił wyciągi, bo wszyscy jesteśmy wiecznie zajęci, nieleniwi. Zacznę więc od mocnej tezy. AI za biolit magnety.

**31:56** · Na przykład uznał za typowy AI fragment Sign postic opener. Nazwy nie są ważne, ale postanowił to zmiękczyć. Zrobił AI zabiolit magnety. Mocna teza. Wiem. Tak żeby wyszło to bardziej konwersacyjnie i po ludzku. Tak jak ktoś to pisałby bardziej felieton, a nie typowy artykuł.

**32:14** · Więc świetna sprawa. dobrze sobie coś takiego zbudować i tak dalej. W każdym razie system artykuł na tej podstawie przeszedł i zobaczcie dał 11 błędów językowych. W sensie system, który był nauczony na kilku skilach i tak poprawił popełnił 11 błędów językowych i pewne rzeczy ściągnął z nagrania, ale zostawił, bo to są jak to jest ładnie ujęte twoje autentyczne mówione i signaturowe domknięcia. Więc zgodnie z zasadą nadrzędną skilla zostawiam świadomie, nie spłaszczam.

**32:46** · I to jest moment, z którym chciałbym specjalnie się raz jeszcze pochylić i pokazać wam, że dlatego tak właśnie warto nie odpalać rzeczy, żeby system zrobił je od razu, tylko żeby wykonywał je po kolei.

**32:59** · Generalnie jedną z najtrudniejszych rzeczy, rozmawiałem dzisiaj o tym nawet z Tomaszem Niezgodną obecnym na webinarze, widziałem Tomku, że jesteś, więc pozdrawiam. Cieszę się, że dotarłeś. Jest zmuszenie AI do przechodzenia krok po kroku przez własne instrukcje i uwaga wykonywania ich. AI przy całej swojej inteligencji, sztucznej inteligencji czasami bywa, co jeszcze dzisiaj do nas wróci sztuczną głupotą i potem wszyscy znamy to jedno najczęstsze zdanie, które AI nam pisze: "Przepraszam, masz rację, już poprawiam, bo czegoś nie zauważy."

**33:29** · I właśnie dlatego, żeby to obejść, ja mam pewne zadania rozbite albo na prompty, albo na osobne skille i one nawzajem po sobie sprawdzają. Plus jedną rzecz, którą każdemu z was polecam w do wrzucenia w swoje prompty, w swoje skille, w swoje projekty, obojętnie na czym i w jaki sposób pracujecie, są tak zwane definicje ukończenia z angielskiego do, czyli definition of done.

**33:53** · Po czym AI ma poznać, że zadanie wykonało dobrze, jak ma zrobić autorefleksję, potrzebuje checklistę, którą może sobie odhaczyć.

**34:05** · Więc u mnie w każdym prompcie, w każdym skillu kryjącym się pod promptem jest tak naprawdę definicja ukończenia. I to co my do tej pory omawialiśmy przez te blisko pół godziny, to było 11 kroków, które system może sobie teraz odhaczyć punkt po punkcie, żeby zobaczyć, że zrobił wszystko, co powinien. zaczął od oczyszczenia transkrypcji, szlifowaniu tekstu, upewnienia się, że

**34:27** · nie ma żadnych treści, które by mi tam dohalucynował dodanych test, dodanych liczb, ponieważ ja chciałem tylko własne rzeczy, że odpowiednio rozpoczyna jakimś ciekawym hookiem sam lit, że przeszedł humanizer, którego widzieliśmy, że przeszedł kalki z angielskiego, że ponownie przeczytał wszystko przez mój styl i następnie właśnie jako ostatni wątek przeszedł raz jeszcze bramkę polonistyczną i w tym momencie wszystko naprawił. Gdyby tego zabrakło, to najprawdopodobniej system jakiegoś z tych elementów by nie wykonał.

**34:53** · I na tym etapie pracując zi często zobaczycie, że on właśnie wam powie, że o teraz muszę się cofnąć do punktu ósmego twojej listy, bo rzeczywiście tego jeszcze nie zrobiłem, nie wykonałem i dostaję właśnie element autorefleksji.

**35:10** · Więc co mamy? Mamy już gotowy artykuł, który został poprawiony.

**35:16** · Tak wygląda, jak widzicie na przykład tutaj, bo jak ktoś ma spostrzegawczy to, że teraz na przykład rozbił mi akapity na trochę krótsze, ale dalej zróżnicowane, nie takie typowe AI od linijki, więc oczywiście redakcja jest za mną. I kolejny prompt brzmi następująco: "Plikdown z tekstem zostaw jako kopię roboczą. Będę ją wyświetlał później".

**35:36** · To jest coś, do czego również wam zachęcam, bo bardzo często jest tak, że tworzymy jakiś tekst, tworzymy jakiś materiał z jaj, to często widać w grafikach, potem go poprawiamy i system nadpisuje istniejący plik i starego nie mamy, a na przykład nie idzie go już dobrze przywrócić z powodów różnych.

**35:51** · Więc generalnie zachęcam was, żebyście albo w reguły skili, albo w reguły Cloda jako takiego, albo w reguły swoich promptów, tak jak w tym wypadku, wrzucali jedną prostą zasadę, że każdy nowy plik, każda nowa wersja, przepraszam, to nowy plik. I w tym momencie będziecie mieć pewność, że jeżeli na przykład stwierdzicie, że ta edycja AI poszła za daleko, coś się zepsuło, możecie sobie zawsze cofnąć do poprzedniej wersji.

**36:14** · Więc o to poprosiłem system i następnie poprosiłem go o odpalenie kolejnego skilla, który się nazywa Neuron Writer.

**36:20** · Neuron Writer jest narzędziem, które zaraz wam pokażę. Jest to narzędzie tak jak i surfer SEO, bo to są dwa dobre polskie narzędzia pozwalające robić de facto tę samą rzecz. I akurat Tomek, który jest dzisiaj z nami i jest jednym z twórców Surfer SEO, ma swoje lekcje w naszym programie w AI Marketers 3 i jest trudno o jedną z osób, która miałaby większą wiedzę w tematyce SEO, jak nie on. Więc bardzo się cieszę, że przygotowuje dla nas właśnie lekcje, które uczą wszystkiego takie takich rzeczy związanych z tworzeniem SEO, a ja wchodzę w te segmenty wykonawcze.

**36:49** · W każdym razie niezależnie od tego czy korzystalibyście ze serfera, czy z neuronwritera, czy dowolnego innego tego typu narzędzia, neuronwriter, co za chwilę pokażę, to jest narzędzie, które sprawdza wasz tekst pod jednym bardzo prostym kątem, czy on już ma odpowiednie pokrycie na przykład dla uproszczenia skłów kluczowych. Zresztą pokażę to od razu. Będzie najłatwiej w tym momencie wyjaśnić. Więc żeby to zrobić, muszę w tej chwili na chwilkę wyłączyć tutaj nasz element i pokazać swój ekran.

**37:21** · Więc dajcie proszkę, proszę sekundę.

**37:26** · O, potwierdźcie tylko proszę, że widać w tym momencie ekran. To jest panel Neuronatera od środka, bo jest to po prostu aplikacja, którą normalnie możecie sobie wykupić i w wielkim skrócie czy Neuron, czy Writer, czy czy Surfer Seo, ich metoda działania jest podobna. Wrzuca się tam swój tekst, system go analizuje i przede wszystkim sprawdza jedną kluczową rzecz. Jakie słowa kluczowe, jakie tak zwane encje i tym podobne rzeczy powinniśmy używać w nagłówkach, w tekście oraz wskazuje rzecz bezcenną ile razy.

**37:59** · Powinniśmy ich użyć. Już samo to jest wielką pomocą, ponieważ ja regularnie próbowałem z pomocą czystego cloda czy czystego czata GPT generować teksty rzekomo wypozycjonowane, więc mu tam promptowałem, prawda? Przygotuj wszystko pod SEO, dobierz słowa kluczowe i potem wrzucałem to do neurona czy surfera i okazywało się, że po prostu używa tych wyrazów zdecydowanie zbyt wiele razy, przez co Google na przykład rozpoznałby, że jest to ewidentnie przeoptymalizowane.

**38:27** · A w tym momencie ja dostaję bardzo prostą informację. Mógłbym sobie to poprawić ręcznie albo co pokażę za chwilę robi to właśnie za mnie ręcznie czy już automatycznie właśnie clod.

**38:37** · Ważne jest to, że my możemy zobaczyć sobie swój szczęśliwy numerek. Numerek w skali od 1 do 100. Wszystko co powyżej 70 to już dobre. Dlatego świeci mi się na zielono i nie czuję potrzeby, żeby to dalej optymalizować. Po to nam mówi, że system, że uwzględniliśmy wystarczająco gęsto właściwe słowa kluczowe. A skąd system wie jakie? Otóż analizuje bodajże pierwsze 50 wyników wyszukiwania i na tej podstawie sprawdza tak maszynowo mechanicznie co jak często występuje, jakie tematy pokrywa.

**39:04** · W tym wypadku 72 spokojnie wystarczy jak widzicie, bo top 1 wynik w Google ma 78 a mediana top 10 to 68. Więc ja w ogóle jestem już cztery punkty nad tym poziomem, nie robiąc nad tym niczego zanadno więcej.

**39:22** · A zrobił to dla mnie, zrobił to dla mnie sam Clot. No i pytanie brzmi, jak on to zrobił? Już wam pokazuję, tylko ponownie przełączam się na swojego, na swojego cloda.

**39:36** · Otóż system po prostu odpalił skill ne neuronitera, którego w tym momencie już wam wyjaśniłem, więc wiecie, widząc go jak mniej więcej wygląda ci z was, którzy tego narzędzia nie znają. I następnie po prostu rozpoczął pętlę, w którym zaczął to wszystko rozpisywać.

**39:52** · zaczął się uczyć, co powinien to używać, jakich fraz. No to są dość specjalistyczne rzeczy, nie będziemy tego czytali, bo to jest po prostu nudne. W każdym razie kluczowy fragment jest tutaj. Przeszedł kilka razy pętlę tekstu. Jego pierwsza wersja, tą którą wam pokazywałem miała wynik 39. Po dwóch pętlach osiągnęła wynik 51. A po wszystkich możliwych pętlach, jak sobie jeszcze dodaliśmy trochę wyrazów, o których na początku wcisnąć nie chciał, no to doszedł właśnie do wyniku 51.

**40:23** · Ponownie właśnie dostajemy definition of done, co zrobił i jak zrobił, ale ja troszkę pomarodziłem i powiedziałem mu, żeby zaproponował dalsze poprawki.

**40:36** · I w tym momencie już long story short, żeby też nie przedłużać, zszedł do wyniku aż 83. który ja potem kazałem mu generalnie troszkę zbić do niższego, bo to by wyglądało już zbyt sztucznie. I to jest zaleta pracy Zi w tym momencie, ponieważ on nie tylko dał mi możliwość podbicia tego wyniku, bo jak widzicie, podbił go do poziomu tego top 1, czyli 83, ale następnie udzielił mi informacji zwrotnej typu Artur, część z tych rzeczy brzmi już sztucznie, część z tych rzeczy ewidentnie zarzuca wyrazy na siłę.

**41:05** · I teraz na koniec dnia i tak ja muszę podjąć decyzję, czy chcę właśnie poruszać jakieś tematy prawno-formatowe i tak dalej, bo to właśnie pozwoli ten wynik utrzymać. Czy jestem gotów zjechać i zależy mi na naturalności. Stąd jak się pewnie domyślacie, dla mnie celem była właśnie naturalność. I w ten sposób skończyliśmy po trochę zjazdu z takim wynikiem jaki mamy. I co więcej, ja mogłem go od razu poprosić uwaga o przygotowanie draftu do publikacji w WordPressie.

**41:35** · nie czym nie wiem na czym stoi wasza strona, moje strony, strony mojej firmy, moich firm i wiele stron naszych klientów stoi albo na jakichś silnikach sklepowych albo na WordPressie. No i problem do tej pory był taki, że zawsze po tym jak napisaliśmy taki tekst to potem trzeba było go ręcznie wrzucić.

**41:51** · Teraz weź pan generuj grafikę, uzupełniaj poszczególne pola w CMSie i tak dalej i tak dalej. A nobody got time for that. Jak mawiał klasyk z mema.

**42:01** · Natomiast nie istniała wtyczka i nie ma wtyczki, która łączyłaby cloda z WordPressem, taka jakaś oficjalna, przynajmniej ja nie dotarłem i pozwoliła edytować szablony, szablony stworzone specjalnie customowe pod moją firmę, więc zwyczajnie sobie taką z Clodem napisaliśmy i to jest właśnie przewaga pracy z narzędziami typu code, no bo czat by nam tego pewnie nie wykonał, a już code czy kodex również, jeżeli pracujecie czy antigravity na przykład spokojnie może to dla nas zrobić.

**42:25** · Więc w tym momencie ja mogłem go prosić od razu o przygotowanie mi rzeczy gotowej do publikacji na WordPressie i taki draft postu faktycznie się tam w tym momencie znalazł. Zresztą możemy go sobie pokazać, że istnieje i jest gotowy do opublikowania, bo jak to mówił klasyk, zobaczyć to uwierzyć. Więc w tym momencie przełączam się właśnie, żeby wam żeby wam to pokazać.

**42:51** · W wersjach roboczych mojego, mojej strony stoi właśnie dokładnie ten artykuł, dokładnie z tym tytułem i dokładnie z tym wstępem, którym kojarzycie. Ba, nawet zalinkował rozumiejąc, że taka jest struktura, w jaki jaką ja zazwyczaj takie rzeczy robię, dokładnie ten wpis, dokładnie mój film, do którego materiał przygotował. I wszystko wygląda stylistycznie, dodane jest idealnie z jakimiś linkami wewnętrznymi, o czym zresztą zaraz sobie powiemy. A gdybym cokolwiek chciał jeszcze sobie poprawić ręcznie, to wystarczy, że wejdę w edytuj wpis.

**43:23** · I to jest dokładnie ten ten numer 134487, który widzimy również w opisie mojego cloda i którym mógłbym sobie teraz jakieś rzeczy jakieś rzeczy jeszcze jeszcze poprawiać. Więc tak naprawdę od samego początku do samego końca ten proces w tym momencie możemy do publikacji przeprowadzić. Ale to nie koniec, bo jest jeszcze kilka rzeczy, które w tym momencie warto byłoby wspomnieć. Więc wracamy sobie do Claudiusza.

**43:52** · Klaudiusza, który w tym momencie jest z siebie dumny, że przygotował nam właśnie artykuł, że w WordPressie jest gotowy draft, że ma wszystkie rzeczy gotowe i że ewentualnie pyta mnie jeszcze o takie typowe rzeczy typu obrazek wyróżniający, dodanie filmu, dodanie schema od seowe rzeczy, ale w tym momencie nie będziemy się je wdawali. W każdym razie prosimy tylko o jedną rzecz, którą mógłbym napisać. Mogłem napisać publikuj i ten wpis z roboczych po prostu by nie wszedł, czy wszedłby po prostu na stronę.

**44:23** · Ale to jest ten moment, którym chciałbym wam powiedzieć i wrócić do zdania, które powiedziałem wcześniej, że bardzo często praca ze sztuczną inteligencją to jest praca ze sztuczną głupotą i że choć mogłoby się wydawać i wielu ludzi z internetu właśnie obiecuje, że wszystko się będzie robiło samo, myślało samo, robiło samo za nas,

**44:41** · to jest to bardzo niebezpieczna rzecz, bo cały ten proces, który tutaj wam pokazałem, odpalanie prąd po prompcie zajęło mniej więcej 30 minut, 40 30 do 45 minut z generowaniem i ciekawe omówienie tego bez już generowania, bez tokenów w tle zajęło nam dokładnie tyle samo czasu, ale nie ma tu jednego prompta, którego specjalnie ja przed wami ukryłem. Ukryłem w drugą, drugiej konwersacji, którą przygotowałem na potrzeby naszej dyskusji.

**45:07** · To jest tak zwany fork, czyli odgałęzienie, rozgałęzienie tej z tej samej rozmowy, zobaczcie proszę, która rozpoczyna się właśnie od artykułu o lit magnetach, ale jedyna różnica jest taka, że ja na końcu tej konwersacji zadałem jeszcze jedno pytanie.

**45:23** · I to pytanie brzmi następująco. Już wam pokazuję. Jest to złośliwy prompt tej treści.

**45:31** · Wspaniała robota. A teraz wielki finał i najważniejsze pytanie. Czy przed tym wszystkim użyłeś innych naszych skili, by sprawdzić, czy artykuł na dany temat nie jest już aby opublikowany na stronie i czy w ten sposób się nie skanibalizujemy.

**45:47** · I dostałem odpowiedź, że oczywiście, że tego nie zrobiłem. Jest to realny błąd procesu z mojej strony. I pamiętacie, kiedy mówiłem wam wcześniej, że AI może mieć coś wpisane w reguły, a i tak tego nie będzie wykonywać i to jest pewien problem, który ciężko jest obejść. Tak jest dokładnie tutaj. Zobaczcie, pominąłem krok, który moje własne skille stawiają jako obowiązkowy przed briefowaniem.

**46:10** · Footprint domeny, strategia treści krok 0. To nawet nie jest, że AI w wyniku długiej sesji zgubiło kontekst na 50 prompcie i po 30 minutach. On przeczytał instrukcję, której jest świadom, która jest wpisana na sztywno jako reguła wykonalności w każdym skillu i w każdym prompcie i ją zignorował.

**46:31** · Dlatego nie moglibyśmy tego wpuścić samopas. Teraz gdybym ja wpuścił ten artykuł na stronę to w tym momencie byśmy się kanibalizowali i w momencie, bo mamy już artykuł dokładnie na ten temat powstały dokładnie wcześniej na podstawie tego samego filmu i zrobiłem to właśnie specjalnie, żeby zobaczyć, że AI się nie zatrzyma i tego nie sprawdzi, to póku nie wskażę mu tego palcem, bo ja wiem czego chcę.

**46:57** · I to jest generalnie problem z pracy z AI. Zawsze przy takich sytuacjach, że pewne rzeczy mogą być wpisane, ale i tak należy je potem sprawdzić i albo sobie przygotować jakąś definicję kolejną ukończenia. Ja sugeruję, że jeżeli ktoś nie chce się mocno bawić w takie rzeczy, to na koniec po prostu przygotować sobie jeszcze takiego prompta kontrolnego z o rzeczy, których AI się najczęściej wywala. Czyli jeżeli to jest tak, że AI najczęściej wywala się u was właśnie, bo nie sprawdza kanibalizacji, to jako prompt ostatni w kolejności wrzyć jeszcze: "A czy sprawdziłeś kanibalizację?"

**47:28** · Bo ja teraz wykonałbym, gdybym pokazywał to na żywo, kawał dobrej, nikomu niepotrzebnej, a nawet wadliwej roboty. Dobrze napisany tekst na temat, który nigdy nie powinien powstać, bo kanibalizuje już inne rzeczy w tym momencie na serwisie. Więc to jest taka przestroga, że eksperci dalej są potrzebni i to jest te słynne human in the loop. człowiek na początku procesu, na różnych etapach procesu jako kontroler, weryfikator i orkiestrator tego co się dzieje i na końcu, żeby sprawdzić, że wszystko co się dzieje jest na pewno dobrze wykonane.

**48:03** · I moi drodzy to nas prowadzi do głównej tezy z naszego dzisiejszego spotkania, takiego wniosku kończącego, że AI samo nie zrobi, bo od prostego prompta dostaniemy badziewie, a od nie przesterowywanego i nie kierowanego dostaniemy rzeczy po prostu błędne z albo z błędnymi faktami, nawet z błędami językowymi czy innymi problemami, których część sygnalizowałem wam również po drodze, ale dobrze pokierowane zrobi na pewno i możemy sobie coś takiego przygotowywać. I to co jest ważne to, że ja pokazałem wam dzisiaj tylko jeden elementu.

**48:36** · Jeden element, jeden skill z około 15 agentów AI, bo tak naprawdę rzeczy, które my przeszliśmy, to jest w tym momencie wątek pisania w twoim głosie, który tu jest pokazany jako jeden ze skil produkcyjnych i ewentualnie optymalizacji pod Google i AI, który widzimy tutaj jako drugi z produkcyjnych. Ale po drodze czy wszystkich możliwości, które trzeba zrobić, za wszystkie są odpowiedzialni osobni agenci jest dużo więcej.

**49:00** · rozpoznanie konkurencji, audyt widoczności, obecna mapa tematów podi research przed nagraniem, materiały i fakty czy inne rzeczy, których mówiliśmy, takie właśnie jak weryfikator kanibalizacji, jeszcze są raporty czy na przykład linkowanie. Jedną z rzeczy, które zdjęliśmy z zespołu dzięki temu właśnie, że robi to AI, jest pełne pokrycie i robienie na bieżąco linkowania wewnętrznego między wszystkimi nowo powstającymi artykułami.

**49:25** · I tego typu agenci mogą pomóc w każdym obszarze marketingu. I czy za każdym razem trzeba przechodzić to od zera?

**49:31** · Oczywiście, że nie. Zresztą tak jak już widzicie, ja mam taką tendencję, że wolę pokazać niż niż mówić, że coś jest możliwe. Odpalmy sobie, bo specjalnie poprosiłem AI o podsumowanie sesji z mojej dzisiejszej pracy. Mam nadzieję, że jest to widoczne. Spytałem się system, a już dodaję. Spytałem się o system. Dokładnie o to, jakie teksty opublikowaliśmy dzisiaj. Dzisiaj na digitok.pl pl. Opublikowaliśmy 13 tekstów stworzonych wspólnie z AI dotyczących marketingu dla hoteli, motoryzacji, medycyny czy poprawki naszych stron usługowych.

**50:03** · A generalnie w tym tygodniu mamy czwartek, powstało 26 tekstów, 25 na DTKa, jeden na Arturomoński.com. Ile kosztuje szkołia z reklam na Facebooku i Google? Wszystkie są live, możecie sobie je w tym momencie zobaczyć. Sporo rzeczy poprawialiśmy, sporo optymalizowaliśmy i oczywiście na podstawie moich notatek, materiałów merytorycznych, wsadów, rzeczy z kondinąd, ale takie tempo i tyle rzeczy, które już zaczynają rankować, nie zrobiłbym tego nigdy. Albo mój zespół nie zrobiłby tego w takim tempie, jakim obecnie możemy to robić merytorycznie i szybko z pomocą sztucznej inteligencji.

**50:38** · A tego typu agentów można wdrożyć w każdym obszarze marketingu. Jeżeli oglądaliście poprzednie webinary AA Marketers, to może to widzieliście. W kolejnych również będziemy takie rzeczy mówili. Ja tylko powiem z ciekawości, że podobnych agentów, których jak zbudować pokazuje również w AAI Marketers 3, wdrożyłem na przykład do kierowania i optymalizowania wspólnie ze mną reklam płatnych. I już jest jedna sprawa odnośnie właśnie moich kursów AI, którą mogę pokazać z podsumowania tutaj nowe kreacje stworzone wspólnie ze szną inteligencją na podstawie skil i promptów, które pokazuje w Marketers 3.

**51:10** · Już teraz klikają się cztery razy lepiej, a co najważniejsze sprzedają dwa razy taniej. Przy najlepszym obecnie ROASie, to jest najlepszy wynik w całym portfelu kursowym, czyli ja plus AI jestem już w stanie pobić nawet specjalistów z mojej firmy. Czy na przykład takie rzeczy jak zapisy na webinar, dopóki robione były ręcznie, to jeden koszt kosztował, jeden zapis na webinar kosztował 10 zł, a teraz jeden zapis kosztuje 3,74, czyli kilkakrotnie mniej.

**51:38** · I jak to ładnie napisał sam Claud, miażdży resztę. Co prowadzi mnie do bardzo prostego wniosku, bardzo prostego pytania wobec tego co teraz? Teraz moi drodzy za chwilę będziemy mieli sesję questions and answers. Więc jeżeli chodzi o to, co chciałem powiedzieć odnośnie samego procesu i obiecałem wyrobić się w godzinę, to udało się to zrobić. Ja widziałem, że padało bardzo dużo pytań, ale ponieważ wiem, że często ludzie odsłuchują sobie po czasie po prostu zapis tego webinaru, to zależałoby mi, że zależało mi na tym, żeby po prostu go pokazać do do samego końca.

**52:10** · I w tym momencie zaraz sobie powiemy jak to powinno wyglądać. Ale zanim zaczniemy to właśnie chciałem poświęcić dosłownie kilka minut. Mam nadzieję, że wysłuchacie tego również na powiedzenie wam właśnie o AI Marketers 3, które startuje już niedługo. AI Marketers 3 to jest program koortowy, który z dumą prowadzę i który już niedługo, bo 5 października będzie startował ze swoją trzecią edycją. Jest to osobiście uważam najambitniejszy projekt edukacyjny jaki kiedykolwiek zrobiłem.

**52:41** · I dla tych z was, którzy nie znają tego typu idei, kurs kohortowy polega na tym, że co tydzień otrzymujecie porcje materiałów przygotowanych przeze mnie i zaproszonych ekspertów, których merytorykę i treści kontroluję. Tomku, możesz potwierdzić na czacie, bo dosłownie dzisiaj rozmawialiśmy dokładnie o tym, jak będą wyglądały twoje lekcje. I oprócz tego, że możecie przejść sobie właśnie przygotowane przez nas materiały, to dostajecie od nas cały szereg narzędzi. które pozwalają pracować od razu, tak jak między innymi te, których mówiliśmy sobie dzisiaj.

**53:09** · A oprócz tego w każdym tygodniu mamy również sesje live, na których możemy się spotkać i omawiamy tak jak dziś za chwilę będziemy omawiali wszystkie możliwe pytania, które możecie mieć i mamy tam dodatkowe livey również z zaproszonymi gośćmi w całym programie.

**53:25** · Więc jeżeli chcecie wreszcie sensownie jakby można to powiedzieć, a nie po omacku na podstawie gotowców w nieskoordynowany sposób wdrożyć procesowo AI w marketingu swojej firmie, to to jest materiał dla was. Przyznam szczerze, że tworzyliśmy go w taki sposób, żeby był to materiał, który uczy marketingu z AI, a nie samego AI, bo bez dobrego rozumienia marketingu na wszystkich jego poziomach ciężko będzie sensownie z nim pracować.

**53:51** · I to jest coś, co wiele osób stwierdziło, te ponad 1100 osób, które już przeszło ten kurs w poprzednich dwóch edycjach, że było najcenniejszym jego elementem. Zachęcam was zresztą do zapoznania się z opiniami na stronie.

**54:08** · Pokrótce tylko powiem o tym, co się dzieje w każdych tygodniach, bo uważam to w tym momencie za ważne, bo konstrukcja tego programu też jest unikatowa. W pierwszym tygodniu właśnie pod moją kuratelą zajmujemy się takim systemem wprowadzania pracy do LLMu.

**54:22** · Duża część ludzi, których ankietowaliśmy po obu edycjach powiedziała, że już ten pierwszy tydzień de facto był dla nich warty całej ceny kursu, ponieważ dał im więcej możliwości niż każdy inny program czy każdy inny system, jakiego do tej pory korzystali. A to były zaledwie lekcje z pierwszego tygodnia. W pierwszym tygodniu uczymy jak z pomocą AI naprawić albo zbudować strategię swojej organizacji.

**54:42** · Czyli co w tym momencie zrobić, żeby zbudować i zrozumieć odpowiednią buer personę opartą o nasze dane, konfigurować rzeczy prostymi agentami, budować projekty, budować kontekst, budować dobre prompty, budować skille. I jest to jednocześnie tydzień, który w cudzysłowiu nadrabia.

**54:59** · Jeżeli nigdy nie pracowaliście z A ja i nie zrozumieliście żadnego z tych specyficznych słów, których użyłem dziś.

**55:03** · skill, prompt, łańcuch, bramka ukończenia. To to jest tydzień, po którym będziecie to wszystko umieć i będziecie gotowi, żeby zmierzyć się w cudzysłowie z kolejnymi tygodniami i kolejnymi materiałami, podczas to których Łukasz Świerczyński w drugim tygodniu przerabia wątek kontentu graficznego i wideo od montażu, przez tworzenie grafik, karuzel, materiałów do postów, materiałów na stronie. Łukasz już mi pokazywał jaki element zbudował.

**55:31** · Będziemy mieli też wspólnie webinar, na którym pokażę właśnie demo, na który już was zapraszam, który już niedługo, jak z jednych przykładowych materiałów stworzyć na przykład posty, rolki i reformaty do wszystkich reklam, jakie chcielibyście stworzyć.

**55:46** · W trzecim tygodniu mamy aż dwóch gości, dwa spotkania live i zajmujemy się copywritingiem i social mediami.

**55:52** · Ponownie wracam ja, jeżeli chodzi o lekcje. Ja zresztą jestem obecny w każdym tygodniu i dla każdego tygodnia szykuję dla was materiały. Oprócz tego poruszamy kwestie prawne wraz z Aleksandrą Maciejewicz, którą livey zawsze trwają najdłużej i zawsze robią największą furorę, choć wydawałoby się, że prawo to ciężki nudny temat, to może i tak jest, ale nie wtedy, kiedy zajmuję się nim. Aleksandra i wszystkie. A widziałem już i dzisiaj na czacie takie wasze prawne pytania dotyczące korzystania z RMLMów. Niezwykle istotne, szczególnie dla większych organizacji.

**56:19** · Ola bierze na klatę i się z nimi mierzy i co ważne przygotowuje sensowne odpowiedzi inne niż tylko prawnicze. To zależy albo chyba, że ustawa stanowi inaczej. A w tej edycji dołącza do nas również gość absolutnie wyjątkowy, którym jest Robert Szewczyk, którego kanał na YouTubie bardzo wam polecam, ponieważ to co robi na swoim YouTubie to jest entry level do tego, co będzie pokazywał na AI Marketers. Będzie również gościem jednych z naszych webinarów. Również was na to zapraszam.

**56:44** · Robert zajmie się właśnie w pewnym sensie pokazywaniem automatyzacji i agentyzacji z pomocą cloud coda.

**56:51** · Wszystko w kontekście tworzenia treści pisanych i wizualnych również materiałów na social media. Tydzień czwarty to tydzień w całości poświęcony tematom SEO i obecny właśnie dzisiaj z nami również Tomasz Niezgoda też jest naszym naszym gościem w tym tygodniu oraz autorem lekcji ponieważ takie rzeczy jak pokazałem wam dzisiaj to chcemy zbudować i stworzyć tych 15 agentów a nie tylko tych dwóch do optymalizacji.

**57:16** · I wreszcie tydzień piąty reklamy i analityka, gdzie zapraszamy Karola Dzielic Dzielica, autora jednego chyba z obecnie globalnie najbardziej rozpoznawalnych narzędzi do automatyzacji reklam w Googleu. I ja oraz Karol pokażemy wam jak sami zbudowaliśmy takie narzędzia. Ja mam wewnętrzne zbudowane narzędzie pod skromną nazwą Artol. Ja bardzo lubię takie gierki językowe. System Karola potrafia potrafi automatyzować kampanię w Googleu. Mój system pozwala automatyzować kampanię na Facebooku. Ale pokażemy wam jak zbudować sobie takie narzędzia samodzielnie.

**57:47** · Dlaczego w ten sposób o tym mówię? Zapoznacie się oczywiście ze szczegółowym programem na stronie, będziecie wiedzieli. Ale ostatnie dosłownie zdanie, którym chciałbym się jeszcze podzielić, brzmi następująco, że program jest zbudowany w taki sposób, że przechodzimy trzy ścieżki za każdym razem. Pierwsza ścieżka to jest ścieżka co można zrobić w czacie. Nie każdy z was będzie chciał kodować z pomocą AI.

**58:13** · Nie każdy z was ma takie potrzeby albo ma takie potrzeby tylko do pewnych rzeczy. Ktoś może chce kodować aplikacje do reklam, ale nie chce kodować aplikacji do grafik, bo od tego ma zespół graficzny. Dlatego każdy tydzień programu ma trzy ścieżki. Jedną z tych ścieżek jest ścieżka czat. Co można zrobić i jak daleko można się posunąć w cudzysłowie pracując z czatem, ile z niego wycisnąć.

**58:32** · Druga ścieżka to ścieżka narzędziowa, która pokazuje jak zewnętrzne narzędzia AI, Fireflies właśnie neuronwriter i tym podobne bądź narzędzia wykorzystujące AI wyspecjalizowane do jakichś zadań i najczęściej nieznane ogółowi rynku wykorzystać, żeby zrobić jeszcze więcej niż ludzie robią standardowo.

**58:50** · I wreszcie trzecia ścieżka w ramach każdego tygodnia, ścieżka agent, pokazuje jak to wszystko właśnie zapiąć w powtarzalne, półautomatyczne albo w pełni automatyczne procesy. bazujące na wszystkim tym, czego nauczycie się we wcieżkach wcześniejszych. Więc z ręką na sercu mogę powiedzieć, że z każdego tygodnia wychodzicie z gotowymi agentami zbudowanymi dla siebie w oparciu o instruktaże, które pokazujemy częściowo na żywo, a częściowo na przygotowanych wcześniej materiałach.

**59:20** · A jeżeli z czymkolwiek byście sobie nie radzili, to główną wartością każdej kohorty jest to, że mamy tam właśnie społeczność uczestników, których jest zawsze kilkuset i z którymi można rozmawiać.

**59:32** · Jeżeli nam coś nie wychodzi, to może im wyszło, a jak nie wychodzi wszystkim, to próbujemy wtedy razem.

**59:39** · I normalnie już teraz dostęp indywidualny kosztuje 2990 zł netto. Ale dla was obecnych tutaj dzisiaj, tych którzy wytrzymali tę moją część sprzedażową na ją nazwać po imieniu, jeżeli wpiszecie SEO 15 w koszyku bądź po prostu klikniecie w link, który w tej chwili również pojawił się gdzieś na czacie, to macie 15% zniżki do północy. I poza taką taką takimi sytuacjami jak ten webinar, tego typu akcji promocyjnych już zwyczajnie nie ma.

**1:00:07** · A jeżeli chcecie dołączyć większą liczbą, gdzie dwóch, dwie, trzy osoby to już większa liczba w tym wypadku, czyli chcecie włączyć się jako zespół, to zachęcam do indywidualnego kontaktu właśnie w sprawie potencjalnego dostępu zespołowego.

**1:00:23** · I uf, tyle ode mnie, jeżeli chodzi o parę słów na temat EA marketers. Ja jestem już podekscytowany. Program startuje 5 października i nawet dzisiaj z Tomkiem obecnym na czacie, może zaraz też potwierdzi, rozmawialiśmy, że lekcje będziemy nagrywali jak najpóźniej, aby były jak najbardziej aktualne. W świecie AI dużo rzeczy regularnie się zmienia i trzeba być na bieżąco. Dość powiedzieć, to pozdrawiam ekipę monterską, że ja zawsze oddaję swoje lekcje na kolejny tydzień AA Marketers w tygodniu poprzedzającym.

**1:00:50** · I w pierwszej edycji było nawet tak, że pokazywałem narzędzie, które nie było dostępne publicznie. Miałem do niego dostęp tylko ja jako osoba, która weszła w pewne konszachty z ekipą je tworzącą, a które jest jednym z najbardziej zaawansowanych narzędzi do tworzenia adsów i uczestnicy AI Marketers już na tym narzędziu pracowali, podczas gdy nawet nie miało ono swojej premiery na produkt huncie, czy nie było oficjalnie zapowiedziane.

**1:01:15** · Dobrze moi drodzy i to jest ten moment w którym ja wchodzę już bezpośrednio do waszych pytań i będę sobie je wyświetlał i odpowiadał, więc dawajcie ich jak najwięcej. Im nas więcej tym weselej i możemy sobie za chwilkę porozmawiać, zobaczyć co nam tutaj wyjdzie. Więc pierwsze pytanie do Museo. Opus to nie jest overkill do tego. To było pytanie zadane wcześniej z tego co kojarzę w kontekście robienia nawet transkryptów, tekstu i tak dalej.

**1:01:47** · Nie, ja uważam, że nie ma co oszczędzać na dobrym modelu, bo może do wyciągania prostych danych, może do prostych tabel. Prostsze modele mi się sprawdzają, ale to w tym momencie dla mnie więcej mnie kosztuje czasu i nerwów niż od początku praca na opusie. Ktoś też widziałem, że pytał dlaczego korzystam z opusa 48. Potrafię korzystać nadal, bo jest po prostu tańszy, mniej tokenów zażra, a jest po prostu dobry do takich zadań. Inteligentniejszy model oszczędza wam późniejszej redakcji i korekty.

**1:02:16** · Nie ma co być aż takim tutaj cyzelantem w zakresie tokenów.

**1:02:24** · Elektroencefalografy nick. Pozdrawiam pyta. Słuchałem poprzedniego webinaru, miło mi i pojawiało się już to pytanie co z tworzeniem turyści od zera. Nie na bazie na przykład własnych filmów. Większość z nas nie ma takich materiałów bazowych.

**1:02:39** · Tak jak starałem się powiedzieć również podczas webinaru, no są dwie drogi w tym wypadku. Pierwsza droga jest taka, że nawet jak nie mamy filmów, to wbrew pozorom mamy wiedzy w firmie dużo.

**1:02:49** · Wewnętrzne pliki, wewnętrzne procedury, wewnętrzne bazy danych. zapisy, transkrypcje czy inne podsumowania rozmów z klientami, rozmów między zespołem. Podam na przykład w ten sposób. Yyy, my obecnie w firmie doszlifowaliśmy proces pisania case study. Na pisanie case study nikt nigdy nie ma czasu. Co więcej, jak nawet się napisze case study i prosi się specjalistę o zweryfikowanie faktów, to on na to też nie ma czasu. I zrobiliśmy z Asią ode mnie z zespołu marketingu, którą z tego miejsca pozdrawiam, jeżeli jakimś cudem tego wysłucha, myk następujący.

**1:03:21** · Spięliśmy naszą asanę, gdzie jest cała historia projektu klienta, naszego Slaka, gdzie odbywa się cała komunikacja wokół klienta. dan z systemów reklamowych, które i systemów typu Google Search Console i innych dokumenty projektowe wewnętrzne, czyli już cztery źródła i na razie żadnych zewnętrznych materiałów czy żadnych tworzonych dodatkowo i daliśmy troszkę przykładów stworzonych przez nas wcześniej materiałów typu case study i w tej chwili jakkolwiek to buńczusznie nie zabrzmi case study piszą się same.

**1:03:51** · Napisaliśmy takich już kilka, jak nie kilkanaście. Daliśmy do weryfikacji zespołowi i nie ma tam wyłącznie faktów w rozumieniu. Kampania wygenerowała tyle, czy zadziało się tyle. Jest cała historia. Na przykład zrobiliśmy to, to się nie udało, potem poprawiliśmy tamto, zmieniliśmy to, więc da się. Jest dużo krążącej wiedzy w organizacji, tylko trzeba mieć właśnie na to proces i strategię. I takich rzeczy również uczymy w AI Marketers. Jeżeli takich materiałów również nie mamy, to pozostają nam wtedy wyłącznie dobierane ręcznie, ze starannością jeszcze oceniane krytycznie źródła zewnętrzne.

**1:04:24** · No ale to jest ta ostatnia deska ratunku. Polecam jednak zawsze robić to samodzielnie.

**1:04:32** · Mateusz Bys pyta: "Ciekawe, a te skille tak samo działają w Chat GPTI lub Copilot?"

**1:04:37** · Tak, w sensie pod warunkiem oczywiście, że są odpowiednio zainstalowane i zrobione w kodeksie zdecydowanie. Ja mam w ogóle tak skonfigurowanego cloda, ponieważ regularnie zamykam właśnie limit tokenów i dzisiaj też dwa razy czekałem, aż mi się odblokuje. 20 kilka tekstów dziennie się nie nie robi tanio, jak se pewnie wyobrażacie, że po prostu mam backup skil. Moje skille regularnie ładują się poza folder cloda i synchronizują z kodeksem, więc ja mogę wręcz kontynuować sesję z jednego narzędzia o drugim narzędziu i z tego co wiem wiele osób tak właśnie działa.

**1:05:13** · Aro 302. No a jak jest z tym cloud code?

**1:05:16** · Wykorzystanie tokenów, jak się ma plan?

**1:05:18** · Czy lepiej przejść na max? Jeżeli możesz sobie pozwolić na bodajże 200 € miesięcznie, żeby korzystać z planu Max, to polecam. Jak zresztą nie jest to tajemnicą i było widać, ja sam z planu Max korzystam, regularnie go właśnie w cudzysłowie zamykam, ale bardzo sobie chwalę. Ale już plan pro, który jest bodajże pięciokrotnością zwykłego planu, daje bardzo dużo możliwości i większość ludzi, których znam korzysta właśnie z tego planu.

**1:05:42** · Nawet właśnie mój serdeczny kolega Karol Dzieli, którym mieliśmy jeden z ostatnich webinarów, sam mówił, że nawet przy jego zaawansowanym wykorzystywaniu Cloda do optymalizacji setek kontrklamowych z pomocą swojego narzędzia korzysta z planu Pro razy 5 za ile to 20 dolarów z tego co kojarzę, więc naprawdę warta inwestycja.

**1:06:06** · Drugie pytanie Aro 302 o AI ACT. Czy bezwzględnie muszę na stronie dodać informację, że treści były wygenerowane przez AI lub częściowo wygenerowane? Jak to jest w przypadku robienia stron www dla klientów? Odpowiedź brzmi: Z prrawnika mam wyłącznie krawat i koszulę. Do końca nie wiem. Znaczy trochę wiem, że odpowiedź brzmi w tym wypadku nie trzeba, ale takie pytania pozostawiam zawsze Oli Maciejewskiej i nie przypadkowo dołączamy ją właśnie za każdą edycją i rokrocznie można już powiedzieć do AI Marketers, żeby

**1:06:36** · powiedziała nam to wszystko wraz z paragrafami, kodeksami i mogła wziąć też pełną odpowiedzialność za taką rekomendacją, na co ja sobie nie mogę pozwolić.

**1:06:46** · Dom Seo pyta: "W neuronie można ręcznie wybierać ze stoka obrazki? Da radę go tym skillem podrasować, by dobrał sam odpowiednie grafiki. Yyy, pewnie, że da.

**1:06:55** · To będzie wymagało w tym wypadku, bo bodajże takiej funkcji w API nie ma klikania w przeglądarce. Ja to robię inaczej. Ja po prostu generuję sobie grafiki podłączonym do cloda innym narzędziem do do grafik z kolei Hixfieldem i to wychodzi mnie chyba kosztowo nawet efektywniej albo tyle samo i po prostu on sobie generuje w moim stylu okładki. Wszystkie okładki w ostatnich dziesiątkach wpisów na mojej stronie i na stronie moich firm są generowane wyłącznie na AI na podstawie poprzednich stylów i nie widać różnicy, więc nawet w ten sposób mógłbyś to zrobić.

**1:07:27** · Arteanu pyta: "No i ile ten artykuł kosztuje? y ciężko jest mi to przeliczyć w tym momencie, ponieważ no ja na kodzie powiem w ten sposób, mnie kod kosztuje te 200 € miesięcznie, czyli to jakieś 1000 zł mniej więcej, tak jak dobrze kojarzę, robię na nim miliard rzeczy, więc załóżmy, że jedna piąta z tego idzie na teksty, więc jakieś 50 € w tym wypadku, tak załóżmy.

**1:07:49** · I dzisiaj opublikowałem ich 15, więc musiałbym najpierw podzielić 50 na 30, żeby zobaczyć ile mnie kosztuje kloc dziennie na same teksty i z tego 15 część to będzie koszt jednego artykułu.

**1:08:03** · Generalnie mało, więc się naprawdę opłaca.

**1:08:09** · Maria Pająk pyta: "Jeśli AI potrafi ciąć filmy na przykład na rolki, czy może zastąpić opus?" Tak, ja na swoim na swoim YouTubie publikowałem już odcinki zmontowane całkowicie przez polecam. I praktycznie nie widać różnicy. Nie chciało mi się szlifować w pełni, a rolki montuje się jeszcze prościej, w sensie uczy się go pewnej konwencji, robienia tego i tak dalej. Będzie o tym materiał właśnie w AI Marketers 3. I zakładam, że opus, do którego się Mario odnosisz, to nie jest opus 5. W sensie opus kodowy, tylko opus clip, narzędzie od rolek.

**1:08:39** · Dokładnie takie rzeczy robię już cloud kodem, bo też mnie frustrowało płacenie praktycznie połowy kwoty Cloda Pro za jakieś osobne narzędzie, którego jedyną rolą jest zrobić napisy i pociąć rzeczy w niemalże losowych fragmentach.

**1:08:52** · Więc jak najbardziej można to już zastąpić. AI.

**1:09:00** · Dom SEO, który idzie na lidera pytań, pyta: "Tak, ten proces pokazuje przeróbkę transkrypcji wideo na tekst.

**1:09:07** · Niemniej przy pisaniu tekstów dochodzą jeszcze halucynacje. AI, oczywiście błędy w cytowaniu źródeł. Jak sobie z tym radzicie? Też jakimś skillem, nawet nie jednym. W sensie ja mam wielokrotny fakt checking, który tam w tle się odpalał. Ja nie przypadkowo nie czytałem każdego fragmentu prompta, bo byśmy umarli, ale w skrócie odpowiem ci szereg skil i bramek definicyjnych wywoływanych już jako kody w Pythonie, żeby na pewno nie popełniły błędu. Da się to obejść? I mój, no nie chcę powiedzieć, że nie halucynuję, bo bym skłamał. On haluuje, ale się poprawia. Poprawia się kolejnymi halunami i jej też poprawia.

**1:09:38** · Jest to w moim przypadku kwestia liczby pętli.

**1:09:48** · Piotr Zalewa. Czy taki skill do WordPressa trzeba stworzyć dla każdej firmy oddzielnie? Tak, w sensie, bo są różne. To nie jest kwestia skillu do WordPressa jako takiego. To jest kwestia zarządzania motywem. dość powiedzieć na przykład, że ja dzisiaj na naszych stronach firmowych, bo byłem ciekawy czy będę w stanie to zrobić bez interwencji grafiki, grafika programisty i tak dalej, chciałem dodać numer telefonu, no ale nie mieliśmy zaprojektowanej strony w taki sposób, żeby było miejsce na ten numer. Więc co by się musiało zadziać w klasycznej sytuacji?

**1:10:18** · Musiałbym najpierw iść do grafika, żeby mi przeprojektował stronę zakładki kontakt na dwóch firmach, tak żeby ten numer był. Potem, żeby przygotował widok mobilny, potem musiałbym to dać programiście do zaprojektowania i potem ktoś by to musiał stestować i trwałoby to przy dobrych wiatrach z tydzień. Dzisiaj ja sobie to wypromptowałem i AI na dwóch różnych stronach to zaprojektowało. Ale i tu wracam do twojego pytania Piotrze.

**1:10:44** · No co te dwa motywy są inaczej zbudowane? Jedno wymagało dobudowania jednej wtyczki, druga była bezpośrednią edycją w kodzie motywu, nie wdając się w szczegóły. Trzeba to było zrobić na dwa różne sposoby. Więc odpowiedź krótka brzmi dwa różne skille. Ale cuda można robić. Nie tylko publikować teksty, ale również edytować kwestie wizualne, dobudowywać podstrony dokładnie w stylu tejże marki.

**1:11:06** · Nawet chyba zainspirowaliśmy Piotrze, że jeżeli to byłby ciekawy temat dla uczestników A Marketers 3, to właśnie takiej tematyce być może poświęcę albo jakąś lekcję, albo jeden z liveów.

**1:11:20** · Arkadiusz, cena finalna per 1000 znaków jak wychodzi? Pojęcia nie mam. Trzeba by było jeszcze rozbić to o dane, do których nie mam dostępu i które szczerze mówiąc mnie no nie interesują, bo nie prowadzę takiej agencji piszącej teksty na akord tego typu, więc no nie odpowiem, nie mam pojęcia.

**1:11:36** · Maria Pająk 6061.

**1:11:39** · Na jak długo jest dostęp do kursu?

**1:11:43** · Dostęp do kursu jest na rok, więc można spokojnie przechodzić materiały w te i we FT bez żadnych ograniczeń czasowych i tak dalej, więc naprawdę naprawdę można sobie z tego skorzystać.

**1:11:57** · Wojciech, na co obecnie zwracać uwagę na kampaniach Metapodlidy? Co się zmieniło w okresie ostatnich paru miesięcy? Oj, temat zupełnie poza zakresem dzisiejszego spotkania, więc nie chcę innych zanudzać, ale skoro zadałeś te pytanie Wojtku, to tylko powiem, że ja sprawdzam, robię teraz przede wszystkim to, co już od roku jest kluczowe, czyli wymuszanie, żeby ludzie uzupełniali jakieś dodatkowe pytania. Nie ma to fizyki kwantowej. Najlepiej dać im jakąś rozwijaną, w sensie wypunktowaną listę, coś muszą wybrać. Dwa, trzy pytania, taka trochę prekwalifikacja. Lidów jest mniej, ale przynajmniej są sensowne.

**1:12:26** · No i druga sprawa, takie ustawienie tego, żeby nie dało się tej samej reklamy, tego samego formularza wypełnić dwa razy, bo inaczej się narażamy bardzo często na spamy.

**1:12:42** · Widziałem wiele razy reklamę, w której było porównanie Google Ads za 2500 doarów, a obok Soro za chyba 18. Soro z tego co widziałem chyba działa podobnie do Neuron. Czy testował pan Soro?

**1:12:55** · Pierwsze słyszę. Ja nie jestem chodzącą encyklopedią narzędzi AI. Nie mam pojęcia co to jest Soro, więc nie pomogę niestety, ale myślę, że jak już mamy narzędzie, które jest dobre, tak jak neonriter czy właśnie Surfersa, to spokojnie wystarczy.

**1:13:14** · Mateusz pyta, czy kupując dostęp do kursu należy mieć wykupiony dostęp do tych wszystkich narzędzi, cloud, neuron, inne. Żadnych zewnętrznych narzędzi nie trzeba, żeby spokojnie skorzystać z kursu, nauczyć się bardzo dużo i wiele rzeczy sobie zbudować i doprowadzić to naprawdę nawet do perfekcji w przypadku niektórych umiejętności. Natomiast no rzeczą, którą na pewno należy wykupić, w sensie byłoby wskazanym, bo inaczej bardzo szybko będą ci się kończyć tokeny i nie wszystkie funkcje będziesz mieć dostępne, jest jeden jedno konto premium na wybranym lmie.

**1:13:40** · Czy to będzie Chat GPT, czy to będzie cloud, no to wyłącznie twoja decyzja, któryś z tych oba nadadzą się równie dobrze. Jest to inwestycja rzędu kilkunastu euro czy kilkudziesięciu w przypadku niektórych i naprawdę warto. Po prostu odblokowuje te możliwości. Jakbym se miał prywatnie kupić poza firmą, to i tak bym kupował, bo nic nigdy nie oszczędziło mi tyle czasu, co praca z AI.

**1:14:06** · Czy jest jakaś opcja, żeby Cloda przyspieszyć? Nie ukrywam, że klock strasznie zamula. Czasami dużo szybciej odpowiadać można znaleźć zwykłym c GPT.

**1:14:13** · To jest kwestia modelu, którego używasz.

**1:14:14** · Natomiast można go oczywiście przyspieszyć zmieniając te ustawienia tak jak na kodeksie zresztą z high bodajże na faster po prostu zmniejszając.

**1:14:24** · A wtedy liczymy się z tym, że on nam będzie zużywał zwyczajnie więcej tokenów, więc coś za coś. To są te ustawienia w prawym dolnym rogu, które trzeba sobie wtedy przestawić.

**1:14:38** · Wojciech nas pyta, ile czasu tygodniowo trzeba poświęcić na kurs.

**1:14:46** · Hm, sam materiał zawsze celujemy w taki sposób, żeby do jego obejrzenia, żeby zamknąć się między dwie a trzy godziny, zależnie od tygodnia. No bo właśnie wiemy, że nie każdy ma non stop nie wiadomo ile godzin na obejrzenie tego, ale do każdego materiału są też podsumowania AI, gotowe materiały do powtórki, tak żeby nawet nie oglądając można było jakieś rzeczy wyciągnąć chociażby z tych podsumowań czy ekptów.

**1:15:09** · Oprócz tego zawsze mamy live'a, który trwa, którego część strict merytoryczna bez takiej części jak teraz, czyli już Q&amp;A, trwa mniej więcej godzinę, czasami półtora, ale przeważnie do godziny się zamykamy. Więc taka inwestycja czasowa, konserwatywnie mówiąc, to jest między trzy a cztery yyy godziny tygodniowo, jeżeli chce się w pełni ze wszystkiego skorzystać live.

**1:15:28** · Ale jak się nie zdąży, to właśnie adwocem pytania, które padło wcześniej jest dostęp do kursu przez rok właśnie po to, by do materiałów móc wracać, wielokrotnie przerabiać, poprawiać sobie, wynatowywać, więc nawet ktoś mógłby tylko przychodzić na livey, a potem przez kolejne miesiące przechodzić sobie rzeczy bezpośrednie w kursie.

**1:15:49** · Novium. Czy mój mój w sensie jak miałam głos skill bazuje na skillu którego używa Paweł Tkaczyk? Nie. Mamy pewne punkty wspólne, no bo wielkie umysły myślą podobnie mówiąc półżartem.

**1:16:01** · Natomiast mój jest absolutnie unikalny, stworzony przeze mnie. Zresztą mieliśmy livea właśnie z Pawłem Tkaczykiem, z którego wynikała bardzo prosta informacja, że Paweł to zbudował zupełnie inaczej niż ja, ale w obu wypadkach daje to dobre wyniki.

**1:16:15** · Piotr Konwerski pisze: "Ja już się zapisałem. Gratulacje dla pana.

**1:16:19** · Fantastyczna decyzja. Polecamy, żeby więcej osób taką decyzję również również podjęło. Yyy, a tutaj mamy pytanie Dom Seo. Chciałbym wykupić jeden moduł, da się, czy trzeba cały kurs? Sprzedajemy wyłącznie cały kurs. Nie ma opcji, żeby w żeby wykupić wyłącznie jeden moduł, ale naprawdę nawet dla jednego modułu i tak warto kupić całość, bo raz, że warto być T-shaped marketerem w dzisiejszych czasach, a dwa, kto wie, co cię jeszcze może zaskoczyć z innych rzeczy, które się w tym kursie pojawiają.

**1:16:53** · Magda pisze: "Jako uczestniczka pierwszej edycji potwierdzam jakość.

**1:16:56** · Mimo że minął niecały rok, odczuwam potrzebę odświeżenia, bo zmiany są ogromne. Magdaleno, zachęcamy do kontaktu z ekipą. Dla absolwentów mamy specjalną ofertę i bardzo ci dziękuję za publiczne pochwalenie pochwalenie kursu.

**1:17:08** · Jak wszyscy wiedzą, mi na tym szczególnie zawsze zależy. Staram się, żeby to było to na najwyższym poziomie merytorycznym, na jakim potrafię to stworzyć.

**1:17:19** · Uf, moi drodzy i dotarłem do tego. Oto koniec internetu, a przynajmniej koniec waszych pytań, więc pamiętajcie, że do dziś, do północy, jeżeli dołączycie do AAI Marketers 3, to możecie to zrobić dzięki kodowi SEO 15 z ceną o 15% niską i naprawdę warto do rozpoczęcia programu 40 dni z hakiem.

**1:17:37** · Ja już zbieram materiały i takich rzeczy, które tworzy, które pokazywałem wam dzisiaj będzie jeszcze więcej i będziemy sobie je tworzyć ramię w ramię i dzięki temu właśnie będziecie w stanie maszynowo niemalże tworzyć i ulepszać swój marketing, ale również z odpowiednim strategicznym outputem, bo generować coś to nie jest sztuką. generować dobrze zgodnie z brandem i zgodnie ze strategią. To jest prawdziwa sztuka, a to wymaga głębokiego zrozumienia materii AI, dobrego zrobienia marketingu i właściwie poukładanych procesów.

**1:18:08** · A te wszystkie rzeczy będziemy pokazywali podczas AI Marketers 3 pod moją nieskromną batutą. Już jestem podjarany.

**1:18:18** · Bardzo się cieszę. A dziś zgodnie z tym co było, a czy na dziś to już praktycznie wszystko i zgodnie z tym, co było napisane w moim poradniku stylu, chciałbym wam podziękować za życzliwą uwagę, bo tak mam w zwyczaju i raz jeszcze poprosić właśnie podziękować za to, że spędziliście ze mną tak długi czas w jeden z ostatnich wieczorów tegoż lata. Więc równie gorąco jak pogoda za oknem was pozdrawiam i co do zobaczenia w kolejnych materiałach, na kolejnych webinarach, a przede wszystkim mam nadzieję, że wewnątrz AI Marketers 3.

**1:18:50** · Dobranoc i cześć.

**1:19:00** · H