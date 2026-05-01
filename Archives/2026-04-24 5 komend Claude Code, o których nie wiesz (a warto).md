---
type: Web
authors: '[[Krzysztof Bohaczyk]]'
url: 'https://www.youtube.com/watch?v=HRjgA_6lgaA'
published: 2026-04-24T00:00:00.000Z
created: 2026-05-01T00:00:00.000Z
tags:
  - narzędzia-AI
  - automatyzacja
  - prompt-engineering
---


![](https://www.youtube.com/watch?v=HRjgA_6lgaA)

## Transcript

### Dlaczego te komendy są warte Twojego czasu

**0:00** · W kloc są komendy, o których mało kto wie, a dają realną wartość w codziennej pracy. Wybrałem pięć najciekawszych.

**0:07** · Kilka z nich odkryłem niedawno. Zostań do finiszu, bo piąta daje ci jakość opusa za cenę Sonet. Dla każdej z tych komend wytłumaczy, co dokładnie robią i dlaczego powinieneś je znać. Także bez przedłużania przejdźmy do materiału.

**0:19** · Powiedzmy, że chcesz skopiować treść z terminala. I co zazwyczaj robisz to kopiujesz tu treść. Tak, robimy ctrol copy lub copy i przejdziemy sobie do czystego dokumentu. I teraz jak wtleisz tą treść to wydaje ci się na pierwszy rzut oka, że jest wszystko okej. Ale jak przyglądasz się temu tekstowi, to okazuje się, że jest dużo jakiś pustych spacji albo na przykład wcięcia, których nie chciałeś. I to jest też natura terminali, która wstawia po prostu takie puste spacje, żeby sformatować odpowiedni tekst.

**0:46** · I jeśli wkleisz je na jakąś inną platformę, no to będziesz musiał sobie poradzić z tymi konkretnymi spacjami, albo je usuwać, albo też widziałem metody, gdzie ktoś sobie na przykład taki plik zrzuca do markdown i wtedy dopiero przekopiowuje tą treść, żeby po prostu pozbyć się tego błędnego formatowania. Ale możemy zrobić to prościej. Jest dostępna od niedawna komenda copii/copy, która pozwala ci skopiować właśnie tą odpowiedź od Cloda prosto do terminala.

**1:14** · Także jak zrobię slash copy enter, to dostaję już skopiowaną komendę do mojego schowka i jak wrócimy z powrotem do naszego dokumentu, usunę treść, wkleję, to zauważ, już nie mamy tych spacji ani żadnych wcięć i nawet pojawiły się formatowania markdown, na przykład gwiazdki, których wcześniej nie było, tak? To są pogrubienia konkretne, też mogą być konkretne nagłówki. I dostaliśmy oryginalną treść, jaką zwrócił nam kod, bez żadnych upiększaczy, bez żadnych dodatkowych linii. Także to jest bardzo prosty tip.

### Komenda 1: /copy — czysty tekst z terminala bez numerów linii

**1:45** · On też zapisuje dodatkowo tą odpowiedź w domyśle w Markown. Jak tutaj klikniesz przez tempe cloud response, to możesz zobaczyć dokładnie, że to jest to samo co widzieliśmy wcześniej. I też jeszcze ważna rzecz to w tej komendzie możesz wskazać dokładnie którą wiadomość w kolejności od dołu chcesz skopiować.

**2:02** · Więc jeśli podasz copii samo, to on skopuje najnowszą wiadomość, ale możesz też podać numerek, czyli copi 2. Wtedy powinniśmy uzyskać tą wiadomość wcześniejszą, którą tutaj mi odpowiedział powyżej. Więc spróbujmy.

**2:14** · Proszę bardzo. I od razu dostałem zaktualizowany ten response MD w tym pliku TMP cloud. Ale jak przejdziemy do naszego dokumentu i wkleję, no to dostałem ten tekst typowo z tej wyższej wiadomości. Tak, także to też działa poprawnie. Jeszcze taka jedna rzecz.

**2:32** · Jeśli poprosimy go o wygenerowanie jakiegoś kodu albo da nam jakiś przykład właśnie kodu templateu, to co możemy zrobić? To też wykonując komendę copi, zaraz poczekajmy chwileczkę, aż nam się tutaj wykona. Mamy oprócz tego kodu też jakieś tutaj teksty, tak? Co robi ten kod? Wytłumaczenie. I zauważ, że jak przy kodzie wykonaliśmy polecenie slash copy, to dostaliśmy opcję i mamy do wyboru albo skopiować całą odpowiedź, albo właśnie od konkretnego miejsca w kodzie. Tutaj mamy 16 linek i trzy linki. To akurat nie zależy jak ten kod się sformatuje.

**3:02** · Też to co możemy zrobić to wybrać konkretny fragment i możemy też wybrać czwartą opcję, która po prostu robi to samo co pierwsza, ale już nie będzie nas pytał o ten wybór. Tak więc ja mogę sobie wybrać na przykład punkt drugi. Jak wrócimy do dokumentu, no to dostaję faktycznie skopiowany sam kod. Także polecam tą komendę, bo na pewno usprawnia przenoszenie pewnych rzeczy właśnie z terminala. Ciekawostka jeszcze dla osób pracujących z poziomu terminala, to też taki bonus, który doszedł w wersji 213.

**3:34** · To też kolumny tabel Markdown wyrównują się przy kopiowaniu, co wcześniej nie działało poprawnie i te tabele potrafiły się rozjeżdżać. To jest taka ciekawostka, więc polecam ci sprawdzić również u ciebie. Jest też taka opcja jak klawisz W, czyli zamiast entera klikniemy slop w. Jak mamy do wybrania te różne opcje, to on wtedy domyślnie skopiuje nam tą odpowiedź do pliku i też poda link. Powiedzmy, że budujesz aplikację i chciałbyś w trakcie pracy zadać jakieś konkretne pytanie, które chcesz szybko zweryfikować. Coś na boku niezwiązane z tym, co Cloud właśnie robi.

**4:05** · Jeśli zadasz mu jakieś konkretne pytanie, no to będziesz musiał poczekać, aż on po prostu przeczyta kolejne query, więc nie jesteś w stanie mu przerwać tej konkretnej akcji. Oczywiście musiałbyś anulować to konkretne wywołanie.

**4:17** · Natomiast jest też taka komenda jak by the way, która pozwala właśnie zadać nam takie poboczne pytanie. na przykład co teraz robisz. Więc by the way samo w sobie działa tylko w oparciu o to, co Clodusz ma w pamięci sesji. Nie może w tym trybie czytać nowych plików ani wykonywać żadnych skryptów. I też co ważne, by the way nie wpływa na nasz kontekst aktualny agenta, więc możesz się zapytać o cokolwiek w trakcie, nawet zadać jakieś totalnie oftopowe, niezwiązane pytanie, a on jest w stanie ci odpowiedzieć na bazie tego, co wie oraz tego, co ma w kontekście.

### Komenda 2: /btw — pytanie poboczne bez ruszania głównego wątku

**4:49** · I zobacz, zapytałem by the way, co teraz robisz?

**4:53** · On w tle oczywiście wykonywał tutaj zadania i dostałem odpowiedź. Analizuję projekt, sprawdzam co to za aplikacja i oceniam jakość kodu i następnie mogę po prostu kliknąć escape i pominąć tą wiadomość. Ona w ogóle się nie zapisuje w pamięci i zauważ, że dalej plot sobie działa w tle. Do czego może się to konkretnie przydać? Do czego ja na przykład wykorzystuję to by the way?

**5:11** · żeby dopytać się co dzieje się danej chwili jeśli chodzi o implementację, czym się dokładnie zajmuję, a czasami mam jakieś pytanie totalnie niezwiązane z danym wykonaniem zadania i nie chcę po prostu otwierać nowego terminala i zaczynać nowego wątku, ale po prostu już w jednym terminalu mogę sobie w ramach takiej komendy by the way zadać jakieś pytanie.

**5:30** · Taka moja sytuacja, gdzie faktycznie ten by the way mi się przydał, to jak agent wpisał moją aplikację, to chciałem się upewnić, czy skorzystał z konkretnego MCP Context 7 do zaciągnięcia sobie nowej dokumentacji Stripea, bo akurat nie robiłem taką integrację. No i zapytałem go, czy w tej sesji wykonał konkretnie MCP Ktex 7 i dostałem odpowiedź, że tak, skorzystał z tego MCP i dodatkowo skorzystał jeszcze z jakichś innych rzeczy źródeł.

**5:54** · To także to mi też dało znać, że po prostu nie musiałem przerywać sesji i tego weryfikować, ale Clod mógł dalej kontynuować pracę, a ja po prostu tym by the way nie przerywając wykonywania głównego wątku mogłem sprawdzić co się wydarzyło w mojej aktualnej sesji. Jest to też tanie z tego powodu, że używa cash kontekstu, więc odpowiada prawie natychmiast i też nie ma dostępu do narzędzi, czyli odpowiada z pamięci, sesji, nie czyta nowych plików. To jest też ważne. I teraz trzecia komenda.

**6:23** · Umówmy się, przelewanie myśli do cloda jest cięższe, gdy musimy pisać to ręcznie tutaj z poziomu tego terminalu.

**6:30** · Na pewno to jest po prostu wolniejsze. I co możemy zrobić? To jest budowana komenda, która pozwala nam włączyć tryb głosowy, czyli będziemy mogli dyktować tekst za pomocą naszego głosu. To jest komenda/voice, więc jak piszesz tą komendę, to z automatu włączy ci się ten tryb. Ja oczywiście go teraz wyłączyłem, więc włączę go ponownie, także jeśli wykonasz ją drugi raz, to możesz ją śmiało wyłączyć. I co ważne, domyślnie ten tryb będzie w języku angielskim.

**6:55** · Jeśli chcesz zmienić na język polski tak jak ja, to będziesz musiał wpisać slash config i znaleźć opcję language, a następnie klikamy prawy przycisk, żeby przejść do edycji i będziemy mogli wpisać konkretny język. Ja wybieram język polski, czyli literki PL i jak zapiszę, wrócimy do terminala, to będziemy mogli działać z tą komendą już głosowo w języku polskim. Jeśli chcę przetestować ten tryb, to wystarczy, że przytrzymam spację.

### Komenda 3: /voice — dyktowanie głosem zamiast klawiatury

**7:23** · Trzymam właśnie spację i mogę dyktować praktycznie real time, mówiąc po polsku.

**7:29** · Więc zauważ, że czasami ta interpunkcja może być różna. Wyłapał tutaj dobrze język angielski. Co ważne, tryb głosowy działa w oparciu o modelopic, który jest do trenowany do takiego deweloperskiego kunsztu, czyli wykorzystania go przy programowaniu. Czyli jeśli stosujesz taki slang deweloperski, używasz różnych pojęć jak Kubernetes, OAF i różne takie rzeczy, to po prostu on będzie sobie dobrze z tym radził. Co ważne jest 20 języków, w tym języki europejskie i również polski, to co pokazałem przed chwilką.

**7:59** · Ta komenda działa poprzez serwer Antropic, czyli to co dyktujemy leci na ich serwery. Także bierz pod uwagę to co podajesz w ramach tej komendy, bo może być to przetwarzane po prostu na ich serwerach, więc nie wiadomo do czego później jest to wykorzystywane. Natomiast jeśli chcesz mieć pełną prywatność, to ja polecam korzystać z lokalnych modeli. Mianowicie takim narzędziem, który aktualnie testuję i sprawdza mi się bardzo dobrze jest Voicing. Voicing to jest aplikacja, która pozwala nam ustawiać i to modele chmurowe, ale również lokalne.

**8:27** · I zauważ, że jest tutaj dużo modeli jak Paraakcet, czyli od Nvidi. Mamy też różne modele Open AI i możemy sobie je dowolnie przełączać, a nawet importować swoje jakieś inne lokalne modele. Ja mam wybrany parakiet V3. On sobie radzi bardzo dobrze. Wrócę do aplikacji Cloda i wystarczy, że przytrzymam jeden przycisk i moje dyktowanie jest włączone. Na Macu jest to Comand, a na Windowsie powinien być control.

**8:53** · On działa bardzo sprawnie i bardzo też szybko jak na lokalny model, bo zobacz, robimy to teraz na żywo i zobacz, od razu mam wynik i też bardzo ładnie wszystko jest sformatowane, nie ma żadnych błędów, także możesz osiągnąć też dużą jakość korzystając z lokalnych modeli poprzez chociażby voicing. Proszę bardzo.

**9:12** · No tu oczywiście nie nie rozpoznał tej takiej nazwy własnej, ale mogę teraz przełączyć się przykładowo do przeglądarki i też tutaj w ramach dokumentu, proszę bardzo, dyktuję teraz do dokumentu doc i mogę zapisać jakieś swoje myśli.

**9:29** · Proszę bardzo. I od razu mamy i to wszystko jest przetwarzane przez nasz lokalny model na naszym komputerze.

**9:36** · Także też polecam i link do tego, do przetestowania będzie również w opisie.

**9:39** · korzystasz z Cloud Code miesiąc, dwa, a nawet pół roku i zauważasz, że agent popełnia podobne błędy albo chciałbyś poprawić po prostu swoją jakość pracy z Clodem, polecam sprawdzić komendę Insightes, która generuje ci raport na bazie analizy twoich poprzednich sesji.

**9:56** · Ja oczywiście taki raport, żeby nie czekać, wykonałem już sobie wcześniej.

**10:00** · On jest akuratnie z lutego. I dostaniesz plik HTML, który możesz sobie otworzyć w przeglądarce i zobaczyć co tutaj ciekawego jest w podsumowaniu. Masz oczywiście za jaki okres jest ten Insights, ten raport. Masz konkretne podsumowania, co ja też robiłem, bo to jest akuratnie mój raport. Mam też nad czym pracowałem, ile sesji poświęciłem nad danym projektem i również co potrzebowałem, jakich narzędzi najczęściej używałem, w jakim języku najwięcej programowałem.

### Komenda 4: /insights — raport z Twoich sesji Claude Code

**10:25** · To jest u mnie Python i też co ważne jaki sposób używałem clot code to jest też bardzo ciekawe, bo on tutaj wskazał, że poruszam się po wielu projektach jak Generalista, z czym się totalnie zgadzam. Po prostu szybka iteracja i szybkie planowanie, przełączanie się pomiędzy różnymi sesjami. Też często porzucam pewne sesje, przyznaję się do tego i zamiast czekać na wyjaśnienia, to po prostu zaczynam nowy terminal i podejmuję akt. I też są ciekawe rzeczy, które zrobiłem tutaj.

**10:54** · Oczywiście Cloud będzie mnie chwalił, co udało się osiągnąć, ale ciekawa sekcja to jest where things go wrong, czyli co poszło nie tak. Możesz oczywiście wyciągnąć sobie pewne wnioski z tego, co było powodem jakichś błędów w twojej pracy z Clodem. I są też konkretne rady, które możesz sobie przenieść chociażby w ramach Cloud MD twojej pamięci clot coda. Dostosowane do tego, z czym działasz. Oczywiście on mi tutaj zwraca uwagę na to, że ja często poprawiałem cloda, jeśli chodzi o formatowanie i mogę dodać sobie do Cloud MD właśnie taką regułkę, że główny język to polski.

**11:26** · Jeśli generujemy jakiś tekst, to też zwracaj na to, żeby znaki UTF8, te polskie wszystkie diaretyzacje również brać pod uwagę. Oczywiście to nie znaczy, że wszystkie te reguły masz wrzucać do swojego Cloud MD. Ważne, żebyś przeanalizował i wyciągnął wnioski, które faktycznie są słuszne, a które nie. Też tutaj dostajemy customowe skille, które możemy wykorzystać. Są też hooki. Tutaj akurat nie chodziło o komitowanie, bo też często zwracałem Clodowi takie uwagi. Ja już część z tych rzeczy wdrożyłem, bo to jest stary insight.

**11:54** · Natomiast ja polecam wykonać tą komendę u siebie i polecam ci wykonywać tą komendę co parę miesięcy, żeby zobaczyć jak twoja praca polepsza się z clot codem. I piąta, jedna z nowszych funkcji, jeśli chodzi o clot code to Advisor Strategy. I już ci tłumaczę o co w tym właściwie chodzi. Jeśli korzystasz z Clota, to pewnie zauważyłeś, że Opus jest mocnym, inteligentnym modelem, ale zużywa bardzo dużo tokenów. Z kolei Sonet jest nieco tańszym modelem, ale na pewno gorszym jakościowo niż Opus. I teraz jak możemy połączyć te dwie siły?

### Komenda 5: /advisor — moc Opusa w cenie Sonneta

**12:25** · Ta metodyka nie jest nowa. Ona się pojawiała już w różnych rozwiązaniach agentowych. Natomiast Antropik wprowadził ją do siebie już domyślnie. I co my tutaj mamy? Mamy główny model Sonet, który wykonuje zadanie, pisze kod, czyta pliki i też advisora, czyli doradcę, który doradza po prostu naszemu Sonetowi jak wykonać dane zadanie.

**12:41** · Czyli Sonet może traktować takiego taki model jako dodatkowe narzędzie, które może dopytać w w razie jakiś problemów z wykonaniem zadania. jest powiedzmy mamy takiego soneta jako analogia, który jest junior programistą i jest on pisze kod, czyta pliki. Natomiast jeśli ma jakiś problem to może się dopytać senior programisty, czyli bardziej doświadczonego dewelopera, który podpowie mu jak zrobić daną implementację. Oczywiście ten advisor nie może edytować żadnych plików. On jedynie służy jako doradca.

**13:10** · I też co ważne w tej strategii, to oba te modele współdzielą kontekst, czyli i advisor ma ten sam kontekst i może też wysyłać swoje porady i executor też wykonuje, może czytać te porady i również wykonywać kod. Czemu mielibyśmy w ogóle stosować takie podejście? Antropic przetestował to na takim popularnym teście SWE Bench, który jest można powiedzieć topowym testem jeśli chodzi o programowanie ZI. I to co zauważyli to sam model Sonet działając w iteracji osiągnął wynik 72,1%.

**13:43** · Natomiast Sonet w połączeniu z tym opusem jako model doradca osiągnął wynik prawie 75% czyli to jest 2,7 punkta procentowego więcej i tym samym zrobił to 12% taniej. Yyy, jak wynika tak samo z samego wykresu, którym się chwali Antropik, to okazało się, że pomimo tego, że mamy tutaj droższy model Opus, to on jako doradca doradził, tak, to on jako doradca wraz z Sonetem zużył o wiele mniej przez to, że Sonet musiał wykonać mniej iteracji niż Sonet działający solo.

**14:13** · Także to też ciekawy wniosek i można też sobie go potestować na swoich przypadkach. Oczywiście oprócz samego Soneta, możemy też wykorzystać połączenie Sonet plus HQ albo HQ plus opus. to my decydujemy jaki model ma być advorem. Tutaj jeśli chodzi o HQ no faktycznie HQ samo z sobie będzie wychodzić taniej. Natomiast w wykorzystaniu z opusem okazało się, że osiągnął lepszy wynik w terminal benchu i też w agentic searchu. Także to są pewne wnioski. Finalnie ten koszt oczywiście był bardzo porównywany, ale większy jeśli chodzi o high plus.

**14:44** · Jak możemy ustawić takiego doradcę?

**14:48** · Wystarczy, że wpiszemy advisor, enter i następnie będziemy mogli wybrać jaki model ma być. doradcą. Ja wybieram Opusa i następnie możemy przełączyć się na modelet, tak żebyśmy korzystali domyślnie z Soneta, a tym naszym advisorem będzie opus.

**15:03** · Ja już mam przygotowany prompt typowo pod tą aplikację, natomiast ma on dokładnie zrobić kompleksowy audyt tej aplikacji, sprawdzić integralność modelu, jakość kodu, architekturę, wydajność i to dałem też z tego powodu, żeby przetestować czy Sonet po prostu zaciągnie porady do Opusa. Także będziemy zaraz widzieć. też trzeba sobie zdawać sprawę z tego, że to clotet decyduje kiedy potrzebuje tej pomocy, a kiedy nie.

**15:30** · Więc on nawet nie zdając sobie sprawy, że potrzebuje tej pomocy, może po prostu nie skorzystać z tego modelu. Także też często możemy gdzieś tam dodać to w prompcie, żeby skorzystał z tego advisora. I proszę bardzo, tak to też wygląda. Czyli po analizie wstępnej kodu, przygotowaniu dokumentu, stwierdził, że po prostu widzi, że ma konkretne dwa pytania.

**15:49** · Zanim przejdę dalej, kontekst użycia, sprint code. Czekam na odpowiedź.

**15:54** · Równolegę wywołuje advisor, żeby ocenił moje podejście do audytu. Także tak wygląda advising. Pod spodem jest model Opus. Analizuje nasz plan i następnie jak przeanalizuje wróci też z konkretnymi uwagami do Soneta, tak żeby mógł jeszcze lepiej poprawić to, co przygotował dla nas domyślnie. I to tyle z takich pięciu tipów, które chciałem ci pokazać. mieliśmy komendę copii advisor strategy, czyli sladvisor mieliśmy by the way i też komendę insight do robienia raportów do analizy po prostu twojej pracy z plot codem slashvoice czyli dyktowanie naszego tekstu.

**16:25** · Także powiedz która z tych komend jest dla ciebie najciekawsza, która to jest dla ciebie nowość i też czy zna i też i podziel się w komentarzu, ile tak naprawdę z tych pięciu komend znałeś przed oglądnięciem tego filmiku.

**16:40** · Także dzięki wielkie. Subskrybuj kanał po więcej i widzimy się w kolejnym materiale. Cześć.
