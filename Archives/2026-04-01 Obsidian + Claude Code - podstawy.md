---
type: Web
authors: '[[Wojtek Woźniak]]'
url: 'https://www.youtube.com/watch?v=EzYcoPPlLxE'
published: 2026-04-01T00:00:00.000Z
created: 2026-04-15T00:00:00.000Z
tags:
  - narzędzia-AI
  - context-engineering
  - automatyzacja
---


![](https://www.youtube.com/watch?v=EzYcoPPlLxE)

## Transcript

**0:02** · Dobra, to dzisiaj przejdziemy sobie przez cały setup takiego secondu. Na to ludzie mówią różnie, nie? Gdzieś tam PKM też może wam gdzieś trafić. To to nie jest PKM kolej kolej miejska czy jak tam się nazywa tylko personal knowledge management chyba coś takiego. I ogólnie w tym wszystkim chodzi o to, żeby zebrać sobie kontekst na swój temat gdzieś w jednym miejscu i później ten kontekst wykorzystywać w pracy z AIem, nie? I jak wygląda moje podejście do tego i dlaczego korzystam z tego systemu? To tak.

**0:37** · Po pierwsze korzystam z aplikacji, która się nazywa Obsidian. Tu sobie zaraz pozamykam taby i wam pokażę.

**0:48** · Obsyian to jest taka apka do notatek po prostu w wielkim skrócie.

**0:54** · I tutaj mam jakieś ustawienia. W obsydianie można mieć różne jakby sejfy i każdy sejf zawiera zestaw notatek i te notatki to są po prostu pliki w waszym komputerze. Jak wejdziemy sobie tutaj do plików to zobaczycie, że dokładnie te same co są tutaj 00 inbox, 1.0 journal i tak dalej to są zwykłe foldery i zwykłe pliki krmd na kompie. Więc każdy mogę sobie podejrzeć tutaj skopiować, edytować, usunąć. Po prostu obsidian pomaga wyświetlać i edytować te pliki.

**1:25** · Więc jak wejdziemy sobie teraz do jakiegoś takiego pierwszego pliku tutaj, który mógłbym wam pokazać, to będzie na przykład ten, to zobaczycie, że mam tutaj różnego rodzaju jakby kategorie, elementy i tak dalej. I to jest projekt, który dotyczy apki, którą buduję, która się nazywa Event Corner. Ja ją będę wykorzystywał do do Vibecfu i będzie tam po prostu lista prelegentów, lista speakerów i tak dalej. I tu w środku sobie trzymam cały kontekst na temat tej apki. I dzisiaj rano miałem spotkanie z Rafałem, więc przed spotkaniem, ale też podczas spotkania mogłem cały czas mieć tutaj sobie otwarty terminal, w którym odpalam sobie cloda. Po prostu piszę tutaj clod.

**2:08** · Jak to skonfigurować? To sobie za chwilę jeszcze pokażemy. Pokażę wam.

**2:13** · Odpalił mi się tutaj clod. Jak widzicie, tu jest napisane, jaki model jest aktualnie wykorzystywany.

**2:19** · I do takich codziennych zadań zazwyczam zazwyczaj korzystam z tego takiego drugiego najlepszego. Chyba teraz już nie wiem, już mi się myli Opus albo Sonet. Jeden z nich jest lepszy, a jeden gorszy, ale no oba są i tak spoko. Ale w każdym bądź razie jak dzisiaj pracowaliśmy nad Event Cornerem, to przygotowaliśmy takiego testowego prompta do wysyłania wiadomości do ludzi, bo tam będziemy chcieli sprzedawać to przez LinkedIna, nie? I z Rafałem sobie przygotowaliśmy taki framework, w którym po kolei, krok po kroku przechodzimy sobie przez jakiś tam kontekst, nie? I tutaj stworzyliśmy takiego agenta, asystenta do walidacji i on ma tutaj informacje po prostu takie ogólne. To by zadziałało do każdej aplikacji. Czyli masz pełny kontekst aplikacji, którą współtworzyłeś, jakie jest jego zadanie, jakie ma cele po kolei i tak dalej. I teraz dzięki temu, że ja mam tą aplikację tutaj w środku gdzieś w notatkach i dzięki temu, że mam tego prompta, o tutaj, to mogę po prostu napisać, żeby run to można też po polsku napisać, czyli from inbox. Zaraz wyjaśnię, co to znaczy.

**3:28** · Czyli mówię mu teraz tak: "Wykonaj jakby zadanie z tego pliku, który znajduje się w folderze inbox dla projektu event corner". Nie klikam sobie enter i on zaczyna pracę. I tutaj widzimy co robi. Po pierwsze szuka sobie rzeczy, szuka sobie event corner, sprawdza różne pliki, które mamy, nie tylko tutaj w projects, ale też w innych miejscach, które są powiązane z tą aplikacją. i na tej podstawie zaraz przygotuje mi treść, czy to wykona po prostu jakieś zadanie, nie? I fajne jest w tym to, że on też może edytować pliki i dodawać nowe i zmieniać, bo clot code ma dostęp do naszego komputera i to nie musi być koniecznie clot code, to może być też kodex albo Gemini CLI. Ważne, żeby to było jakieś narzędzie, które się właśnie nazywa CLI, CLI i wtedy może mieć dostęp po prostu do waszego kompa i wykonywać rzeczy jakby w terminalu. Więc tak jak widzicie, jak on już sobie powykonywał rzeczy i pokminił, to wrócił do mnie z informacją, czyli mam pełny kontekst event corner, ruszam bez rozgrzewki, cokolwiek to oznacza. No i krok pierwszy, hipoteza, bo tak jest napisane tutaj, żeby w pierwszym kroku zaproponował strategię na podstawie kontekstu. I pierwszy punkt to jest operacyjne ICP. No i dokładnie to tutaj ma, nie? ICP pierwszy segment główny problem drugie główny problem czyli wykonuje te zadania i ja nie musiałem mu teraz opisywać wszystkiego, czym jest ten projekt. To jakby jest spoko do zrobienia też jako projekt w czacie GPT czy tam jako GEM w Geminiu. No ale tutaj różnica jest taka, że on widzi jakby te wszystkie rzeczy i na przykład teraz jak już mamy to zrobione to ja po prostu na przykład dzisiaj po tym callu z Rafałem podzieliłem się zadaniami. Wszystkie zadania związane z Rachoutem na na LinkedInie wykonuje Rafał, więc ja mu mogę teraz napisać już w tym kontekście, że dobra, jestem po kolu z Rafałem, on ma się tym zająć. Już ma listę kontaktów i wszystko, czego potrzebuję.

**5:40** · Przypomnij mi w piątek, żebym do niego zrobił followup.

**5:54** · Dobra.

**6:01** · I teraz sobie zaczął myśleć i ogólnie to tak poprosiłem go teraz o to, że już wszystko jest ogarnięte i chciałbym, żeby on mi gdzieś zapisał informacje o tym, żeby mi przypomniał, że w piątek będę sobie pracował i tego dnia powinienem odezwać się do Rafała z pytaniem o te rzeczy. Więc co on zrobił?

**6:20** · Zapisał informacje w coworklogu, zapisał co dzisiaj robiliśmy, czym jest ten plik. jeszcze potem powiem, yyy, pozwalam mu na wprowadzenie tej edycji i po prostu tutaj w pliku odpowiednim, który sobie tam edytował, pojawił się tam nowy nowy element, nie? Czyli 2026 027 w piątek dudyst to on sam sobie zobaczył zrobił jakby jakiegoś rodzaju notatkę na potem i później jak już nadejdzie piątek to ja będę po prostu właśnie przy porannym przeglądzie bo to jest takie zadanie po prostu sprawdzał jakie mam zadania zrobić nie i gdzieś tam dzięki temu to przypomnienie mi zostanie wyświetlone i będzie w całym kontekście tego co co się wydarzyło nie brzmi na razie prosto ale jakby na Na co dzień to sprawdza się super przy budowaniu właśnie aplikacji, przy takiej codziennej pracy z ludźmi, jak musicie przygotowywać jakieś podsumowania, notatki wpisywać i tak dalej, bo gdy jestem na callu, to teraz mogę po prostu spisać sobie jakieś notatki w formie zwykłego dokumentu i na końcu powiedzieć po prostu clodowi, żeby to przerobił i ogarnął, nie? I dzięki temu ja mam tutaj już taki system, który jest dosyć rozbudowany. Dzisiaj wam pokażę jak zbudować takie podstawy pod swój system i potem go rozbudowywać we własnym zakresie. Więc od tego wszystkiego nie ruszymy, ale jakby każdy system, który będziecie tworzyć będzie bardziej dopasowany do was. I opowiem wam też trochę o takich ogólnych zasadach. Jak zwykle notatki do wszystkiego znajdziecie tutaj w TL Draw.

**7:55** · To będzie pod nagraniem dostępne w linku. Będziecie mogli sobie wszystko podejrzeć. Tutaj do materiałów jeszcze potem dodam jakieś tam rzeczy dodatkowe, prompty i tak dalej. A my sobie przechodzimy do do jeszcze jednej części, czyli takie główne problemy zwykłych czatów. Dlaczego ja w ogóle zacząłem to organizować w ten sposób? Bo zauważyłem, że jak zaczynam gdzieś nowy czat, to zaczynam praktycznie od zera za każdym razem. Co jest fajne w tym systemie to to, że mogę też zmieniać czaty. Nie muszę korzystać tylko z cloda. Mogę korzystać sobie z Gemini, mogę korzystać też z czata GPT właśnie w formie tego kodeksa i za każdym razem on będzie miał po prostu pełny kontekst tego, co ja robię. Nie będę musiał kopiować, wklejać plików w różne miejsca. Wszystko mam zawsze u siebie.

**8:35** · Oprócz tego, jak padnie nam AI, w co na razie nie wierzę, ale na przykład może mega zdrożeć, to też te pliki nigdzie nam nie zaginą. One dalej będą z nami dostępne i po prostu mamy je u siebie na kompie, nie?

**8:47** · Dodatkowo jak pracujemy z AI to ostatnio pojawiły się takie opcje właśnie jak projekty czy też jak po prostu takie zapisywanie w formie memory na przykład w czacie GPT i w Geminiu też z tego co kojarzę ale problem tam jest taki że nie kontrolujemy do końca tego kontekstu nie mamy wpływu na to jak on znajduje różne informacje jak on je wykrywa i potem jak je wykorzystuje co jest problemem dodatkowo jakby w kontroli tego kontekstu też chodzi o to żeby czy trzymać taki czysty kontekst i tylko to, co jest najważniejsze. Więc w przypadku, oj, tu mi zniknął ten, w przypadku gdy ja sobie z nim rozmawiam, to duża część wiadomości, w których tylko sobie gadamy, zostaje w czacie i znika na zawsze. Tylko te rzeczy, które były najważniejsze, są zapisywane do kontekstu. Dzięki temu nie mamy miliona rozpraszaczy dla AI i zostawiamy mu dużo więcej przestrzeni na działanie, a nie tylko na jakby czytanie tego, co my mu właściwie wysłaliśmy, nie? i on sobie ten kontekst dobiera po prostu w locie też często po prostu wie co co ma znaleźć, nie? Jeśli chodzi jeszcze o tą kontrolę kontekstu, to każdy z tych plików możemy sobie ręcznie zedytować, nie? Jak wejdę sobie tutaj na przykład do zasad, które znajdują się w pliku cloud.

**10:02** · Tutaj sobie to na razie schowam.

**10:06** · Jak przejdziemy sobie do zasad i tu mam zapisane zasady dla cloda, jest opis kim ja jestem, jakie rzeczy buduję, czym się zajmuję, jak myślę, jak pracuję, jakie tutaj te informacje rozpisać, to wam jeszcze dam znać, nie? Struktura naszego właśnie całego systemu i jakieś tam dodatkowe zasady. I teraz jak ja bym chciał zmienić te zasady albo na przykład stwierdzam, że już nie pracuję nad YouTubem, zamknąłem ten kanał, po prostu to wycinam i tyle jest to zrobione. Ja nie muszę nigdzie w kontekście potem aktualizować tych informacji. Po prostu to jest ogarnięte, nie? To samo yyy jak przechodzę sobie tutaj na na homea, tu codziennie sobie widzę jakieś rzeczy, które mam zrobić, informacje, które mam ogarnąć. Więc w tym tygodniu na przykład mam, czekajcie, bo spróbuję tutaj trochę mniejsze okienko zrobić.

**10:54** · Okej.

**10:56** · Tutaj mam jakieś informacje, co mam wykonać. Jak wykonam zadanie z VPC konfa, po prostu je sobie odznaczam, a później Cloud mi to czyści na ten tydzień, nie? Więc ja tutaj też nie muszę jakby zachowywać takiego, takich codziennych porządków i i usuwać rzeczy.

**11:10** · Oprócz tego, no właśnie to było to ostatnie. Trudno go aktualizować i zarządzać nim. I oprócz tego jakby ważne jest to, że ten kontekst, z którym my pracujemy, on cały czas powinien być żywy. A na ten moment nie do końca pozwalają nam na to te narzędzia, żeby on był żywy i żeby był aktualny. Dlatego ja dużo bardziej wolę pracować sobie w takim systemie notatek, bo zawsze mogę mieć ten aktualny i żywy kontekst. I według mnie ten kontekst to jest po prostu jak takie drzewko bonzai, które trzeba sobie po prostu przycinać ciągle, żeby ładnie wyglądało. Będzie cały czas sobie obrastało. No ale musimy dbać o to, nie? po prostu, żeby nie było tam dodatkowych niepotrzebnych informacji.

**11:49** · Yyy, no i demo tego, jak to wygląda i działa, już pokazałem wam przed chwilą. Jeśli chodzi o taki quick po wolcie, po tym jak ja sobie to ustawiłem, to tak mam plik inbox, w którym wrzucam jakieś takie codzienne sprawy, rzeczy, że jeszcze nie wiem, gdzie one mają trafić i tak dalej. I na przykład dzisiaj zrobiłem tutaj jakieś dodatkowe informacje typu tak dodaliśmy te dwa prompty o event cornerze i dodałem jakiś tam pomysł, który mi wpadł do głowy i jak już mam te rzeczy tutaj ogarnięte i wiem, że już chcę się nimi ich pozbyć, po prostu coś z nimi zrobić, to mówię mu po prostu, że inbox we have free files, clean it Dobra, zobaczymy co zrobi na przykład z tym ID, bo te dwa prompty są do przerzucenia do projektu event corner, a tutaj zapisałem sobie taki pomysł na to w ogóle na jakąś taką rozkminę, którą miałem w głowie dzisiaj, która mnie naszła, że prompty nie są dobre, bo jakby tworzenie w ogóle promptów edytow promptów, kopiowanie promptów skąd jakby nie ma aż takiego znaczenia, bo prompty nie są dobre dlatego, że jakby podążacie za jakąś formułą magiczną, którą ktoś wymyślił, że na górze kontekst, niżej przykłady, a potem antyprzykłady albo pisz mu, że jest ten ex coachzem i tak dalej. To w ogóle nie ma znaczenia według mnie w pracy. Ja często jak przygotowuję jakieś prompty i tak samo jak oj robię kurde przerzuciłem folder tak samo jak robię tutaj po prostu przygotowuję jakieś informacje żeby dla ai później było jasne to co ma zrobić czyli prąpty tak naprawdę a właściwie kontekst jest dobry gdy jest właściwy. Więc jak mamy właściwy kontekst, to często ja na przykład wdrażając jakieś funkcje do aplikacji, nie muszę pisać co tam się ma wydarzyć i tak dalej, tylko wklejam konkretną specyfikację, czyli daję cał kontekst i po prostu mówię zbuduj to.

**13:51** · Nie muszę mu mówić, że on jest ekspertem, programistą, że pracuje w stacku NextJS i tak dalej. Po prostu ważny jest kontekst. On sobie już tam resztę dogra, nie? Dobra. I teraz tak.

**14:02** · Ja tutaj przed chwilą napisałem, że w inbox, czyli tutaj mamy te takie puste pliki. Puste, no w sensie nie wiadomo co z nimi zrobić teraz. I to są takie robocze, żebyście dzisiaj do nich sięgali w tym tygodniu, takie najważniejsze, nie? I on mówi, że może przerzucić je tu i tu i tu. Więc ja klikam po prostu okej, zgadzam się na to. No i te pliki zaraz stąd znikną i jak one znikną to i już je przyniesie, to zrobi nam podsumowanie. Czyli tak, oba prompty dodał do systems working.

**14:30** · Systems to gdzie on trzyma swoje pliki, które sam wykorzystuje, a idea dodał do pliku ID. Mamy taki specjalny folder na to. Więc znalazł sobie ten folder i dodał go tutaj, gdzie mam jeszcze jakieś inne pomysły po prostu na rzeczy, nie?

**14:44** · Oprócz tego, oprócz takiego inboxu, gdzie trzymam te pliki na co dzień, mam też journal i tutaj w journalu trzymam coś, co nazywam AI journalingiem, czyli robię sobie tutaj taki brain dump i na podstawie tego brain duma wyrzucam wszystko z głowy, jak potrzebuję. Nie robię tego codziennie, ani jakoś ultra często, ale raz na jakiś czas muszę z siebie wszystko wyrzucić. robię to tutaj i później korzystam z takiej funkcji, która się nazywa AI journal journal session i ona pomaga po prostu mi przekminić po prostu te rzeczy i na końcu zapisuję wszystkie najważniejsze insighty tutaj w AI Insights sobie, nie? Dobra, potem mam projects. Tu w Projectsach trzymam wszystkie moje projekty, nad którymi pracuję. Później mam yyy dział def.

**15:30** · Tutaj trzymam jakieś takie zasady deweloperskie, których się trzymać.

**15:33** · Czyli na przykład w Lowablu ostatnio wdróżyłem popupa i miałem problemy z tym, żeby on zadziałał, więc na końcu już w LVablu jak na stronie zrobiłem tą ten element, poprosiłem Aaja, żeby podsumował co zadziałało i co zrobiliśmy i tak dalej i on mi powiedział jak integrować z w popupie właśnie formularz Mailer Le. I tu buduję sobie taką wiedzę na potem, gdybym chciał to dodawać gdzieś indziej.

**15:57** · tu gdzieś mam współpracę z klientami, to są już moje takie prywatne, które powstały później, nie? Mentoring z ludźmi, no i później pomysły i jakieś tam szablony na różnego rodzaju rzeczy, bo na przykład IDa ma konkretny swój szablon do wykorzystania, nie? No i na końcu mamy systems. Tutaj trzymamy wszystkie pliki systemowe, jakieś tam archiwum, mamy working, czyli te pliki, które gdzieś tam AI sobie wykorzystuje, one są w miarę aktywne i i attachments, bo jakby Obsidian nie wyświetla plików, które wyglądają, które są inne niż kropka MD.

**16:30** · Więc yyy tutaj w attachments mamy na przykład jakieś tam Jasony, PPTX, PPTX znowu, czyli jakieś tam prezentacje, co tworzyłem sobie wcześniej i tego tutaj nie widzę, ale zawsze mogę sobie tu kliknąć prawym przyciskiem reveal infinder i zobaczyć te rzeczy, nie? No i co? Potem mam na końcu cztery najważniejsze dla mnie pliki. Po pierwsze home, gdzie mam wszystkie zadania na teraz, linki do tych najważniejszych miejsc. Mam zasady dla cloda, mam analytics, którego wam nie mogę teraz otworzyć, bo nie wiem, czy tam mam jakieś prywatne dane w sumie i mam weekly rhythm, gdzie też mam prywatne dane, ale pokażę wam to potem na pustym pliku, jak to wygląda. Tam jest po prostu co robić w poniedziałek, we wtorek, w środę, w czwartek i jaki jest dzisiaj dzień, żeby ja wiedziało po prostu gdzie jesteśmy i i czym się zajmujemy, nie?

**17:17** · Dobra, to taki był tur i teraz budujemy to sobie na żywo, czyli zrobimy i wdrożymy sobie ten ten system.

**17:27** · Czekajcie, bo gdzieś tutaj sobie przygotowałem prompt second i tutaj jest, czekajcie. Finding product Ideas. Co to jest?

**17:43** · Zgubiłem gdzieś prompta tutaj, ale ten prompt jest za długi.

**17:57** · E, dobra. No właśnie. I teraz mam problem ze znalezieniem jednego prompta, więc w sumie zapytam po prostu AI o to.

**18:06** · Aha. I co jest ważne jeszcze w kodzie to od razu to powiem to czyszczenie czatu, czyli jak już skończycie coś robić to robicie po prostu clear taką komendę i wtedy możecie zacząć gadać od nowa i on wtedy nie ma kontentu. Wszystko na nowo sobie szuka, ale ma dużo lepiej działa, bo nie zapychamy jego pamięci, nie? Więc jak teraz sobie zaczynam od nowa, to mu mówię po prostu I need the starter setup short prompt for today workshop on.

**18:35** · Ja do niego piszę po angielsku w sumie, na pewno nie poprawnym angielskim, ale ale jakoś tak z przyzwyczajenia, nie wiem czemu w sumie, ale można po polsku.

**18:44** · Jak widzicie, dużo z tych plików jest tutaj po polsku i to nie ma jakiegoś znaczenia. Mieszam czasami też to. M.

**18:53** · Dobra, to to musi być ten prompt, ale to nie jest ten prąd. Już widzę.

**19:01** · Aha, bo tu jest ta struktura. Dobra, dobra. To zaraz wam to pokażę. Te te prompty wszystkie, które tu są, to są właśnie te, które przygotowałem wam do wykorzystania później do zbudowania swojego AI, nie? Ale my sobie zrobimy tutaj prostszego prompta, bo ten jest jeszcze bardziej skomplikowany, a my na początek potrzebujemy prostszy, czyli tutaj sobie z tego po prostu zrobimy tak.

**19:36** · To na razie usuniemy.

**19:53** · Dobra, tu już zostawiam wam na potem. To jest ten prompt startowy, od którego w ogóle zaczniecie budowanie wszystkiego, co macie, nie? Więc pierwszą rzeczą, jaką zobaczycie po zainstalowaniu Lovaba, Lowabla, sorry, już z automatu, Obsidiana, w ogóle jakbyście mieli pytania od razu, to dawajcie znać też, bo w sumie wiecie, dzisiaj jest tak trochę dziko, jest dużo tych rzeczy i jakbyście mieli jakieś pytania, rozkminne, to dawajcie znać. A jeszcze sobie tu czat otworzę na boku, tylko żeby nie zapomnieć sprawdzać.

**20:21** · Ja mam pytanie, jak otworzyć ten terminal, bo ja nie mogę w tym obsydianie.

**20:24** · Zaraz pokażę, bo go nie ma w obsydianie. Trzeba go zainstalować. To zaraz, zaraz pokażę.

**20:30** · Więc tak, tu jak otworzycie sobie Obsidiana po raz pierwszy, on jest oczywiście za darmo do ściągnięcia, jakby co. Obsidian jest na Maca, jest chyba na Windowsa normalnie i tutaj w zakładce pobierz. U mnie się od razu pobiera. Jak zainstalujecie go na swoim kompie, to prawdopodobnie na początku zobaczycie taki ekran, czyli ten ten pusty tutaj z prawej. I możemy sobie wewnątrz tworzyć różne volty. Czyli ja mam tutaj już swój wozu Volt z poprzedni jakiś tam inny jeszcze, który budowałem wcześniej i tutaj ten budowany za jajem. Zaraz, zaraz na końcu wam powiem, dlaczego mam dwa osobne w ogóle, bo to też jest mega ważne. I teraz tak, ten zejem jest tutaj, ale my sobie stworzymy nowy. Jak tworzycie nowy Volt, to wam się też jakby resetuje ustawienie obsydiana i on jest czysty, więc każdy ten osobny volt, save ma swoje własne ustawienia.

**21:24** · Więc klikamy tutaj create, wpisujemy nazwę i wybieramy gdzie on ma być, gdzie mają być te wszystkie pliki, nie? Ja tutaj mam folder na w swoim głównym folderze, co się nazywa Obsidian Volts i w środku tutaj zrobię AI Vibe Hero i tutaj kliknę open i klikamy create. I co się wydarzy?

**21:55** · Otworzy się nam całkiem nowa instancja obsidiana, która jest właściwie pusta.

**22:01** · I teraz na początek trzeba zrobić dwie rzeczy, czyli zainstalować dwie wtyczki, które będą wam potrzebne. I ja sobie pozamykam na razie wszystko. I w środku macie tylko plik welcome. Można go po prostu usunąć. Y i zaczynamy od pustego ekranu. Po tym jak macie ten pusty ekran, to klikacie sobie tutaj w tą ikonkę ustawień na dole albo u góry Obsidian i settings, czy tam ustawienia i przechodzicie do community plugins i teraz tak zapyta was czy włączyć community plugins. Ja mówię tak, włącz restri tu, tu powinno być restricted mode. Powinno być właśnie tak jak teraz jest turn on and reload, czyli powinno być teraz wyłączone. I wchodzimy do browse plugins i szukamy na początek dwóch pluginów. Pierwszy to terminal, czyli po prostu on się nazywa terminal i to jest ten co ma 118 000 instalacji.

**23:00** · Więc kurczę nie zauważyłem kto pytał, bo się nie odwróciłem, ale to tutaj możesz sobie zainstalować w pluginach od community ten plugin termina.

**23:08** · Tak, już widzę. Mam to.

**23:10** · Dobra.

**23:13** · A jesteś w ogóle podpisany jako użytkownik Zoom? Jak masz na imię?

**23:17** · Bo cię pogłosia jeszcze Łukasz. Dobra, jeszcze pogłosie cię też nie poznaję. Dobra, więc tak. Tutaj terminal sobie instal wchodzicie, klikacie install, plugin jest zainstalowany i klikacie enable, czyli odblokuj. I na razie tyle. I drugi to jest kalendar. Kalendar zaraz wam powiem do czego się przyda, ale to jest ten co ma 2 milion 400 000.

**23:39** · Patrzcie ile ludzi w ogóle korzysta z obsidiana, nie? 2 miliony instalacji pluginu. To też instalujemy, to się przyda na potem. I też klikamy enable.

**23:49** · Jak już to mamy odpalone, to Obsidian właściwie jest ustawiony i od tego momentu możemy już sobie gadać z AIem. Z lewej strony tutaj pojawi wam się ta ikonka terminalu na dole i klikamy w nią. I teraz ja nie wiem do końca o co chodzi z tymi trzema opcjami, ale zawsze wybieram integrated z jakiegoś powodu i wam też polecam to. Nie, nie pamiętam dlaczego, ale ten jest ten jest najlepszy i otworzy się wam tutaj na dole terminal.

**24:19** · No i teraz możemy tutaj skorzystać z cloda albo z Gemini CLI. Ważne, żebyście skorzystali z czegoś co się nazywa CLI, czyli to sobie będzie działało wam o tutaj. Ewentualnie jeśli nie chcecie bardzo działać w terminalu, to taki setup Obsidiana możecie też otworzyć sobie w antygravity albo w kursorze i też wam to zadziała i wtedy tam sobie w czacie działacie, nie? Bo jak otworzycie sobie kursora i w kursorze otworzycie sobie folder, gdzie tutaj jest open folder, file open folder i tutaj otworzę sobie obsidian i tutaj otworzę se ten vibe hero.

**25:11** · to po prostu będziecie mieli znowu tutaj clot koda, czy tam Grock koda czy cokolwiek chcecie. Tu będziecie mogli sobie z nim gadać. A search files nie, gdzie tutaj jest ten to jest browser. Nie wyświetla mi się ten z boku element, nie wiem czemu tutaj chyba. O, a tutaj zawierają się, oj, jeszcze raz. A tu zawierają się te wszystkie pliki. Jak zaczniemy je dodawać teraz, to tutaj też możecie w czacie gadać, więc nie musicie koniecznie cloud koda instalować. Może to być antygravity i tak dalej. Po prostu to otwieracie jak projekt do kodowania, nie?

**25:47** · I jak zainstalować Cloud Coda? No to wchodzicie sobie po prostu w cloud kod, macie tutaj docsy i yyy na quickstart znajdziecie informację jak zainstalować kod coda. Na macOSie wpisujecie to do terminala, czyli otwieracie sobie apkę terminal albo w tym terminalu w obsidianie kopiujecie to, wklejacie i tam już kontynuujecie z tymi różnymi krokami, o które was poprosi i będziecie musieli się zautoryzować. Dokładnie tak samo to działa z Geminajem. Nie słychać mnie? Halo, halo.

**26:26** · Czy tylko u Waltka?

**26:27** · Ja słyszę.

**26:28** · A dobra, to tylko Waldek u ciebie.

**26:30** · Sorry.

**26:33** · A nie, to Ania pyta. Ojej. No to może się gdzieś przestawiło ci. Wiesz co tutaj nie wiem czy wy widzicie to, ale w audio możliwe, że ci się speaker zmienił na coś innego, bo mi się czasami zmienia na iPhona sam z siebie i wtedy nic nie mogę mówić. O ani też nie słyszę. yy Dobra, lecimy dalej. Gemini, cloud code i tak dalej. Jak będziecie mieli problem, żeby to zainstalować, dajcie mi znać na DM.

**26:57** · Pomogę wam to po prostu ogarnąć. Więc jak już mamy Obsidiana i mamy CLI zainstalowane, to wtedy je odpalamy i terminalu. Po prostu dzięki temu, że otwieramy ten terminal o stąd, to od razu jesteśmy w odpowiednim folderze. Może to się wam inaczej wyświetlać, bo ja tu mam jakieś wtyczki pewnie.

**27:17** · I tu piszę sobie po prostu cloud, nie? I jak napiszę cloud, to on mnie zapyta, czy ufam tym plikom. Tak, ufam. I dzięki temu, o, jest tutaj ten słodki obrazek. Nasz klot się odpalił i teraz on prosi o to, żeby na początek odpalić init i stworzyć plik clodem D. Więc od tego zaczynamy. Robimy init po prostu i on teraz wykona swoją pierwszą robotę, pierwszą funkcję.

**27:46** · I jak mamy już tą pierwszą funkcję wykonaną, to kopiujemy sobie tego prompta i wklejamy go. Gdzie zniknęło to? Tutaj. Poczekamy teraz chwilunie. On sobie stworzy ten swój plik clodem D. Tu nas zapyta, czy może sobie wypisać ls. To jest listi, które się znajdują w środku i tak dalej.

**28:12** · Chyba możecie sobie sprawdzać jakby też co to, co oznaczają te komendy albo dopytywać. Po prostu pamiętajcie, że on będzie miał dostęp do waszego komputera, więc y uważajcie na to, gdyby chciał coś. O, dziwne tutaj allow. Nie widzę, że on tutaj za dużo coś kmin. Widzicie? Za szeroko zaczął. E.

**28:42** · documents. Tak, no będzie mi teraz pytał o te wszystkie pliki. Ja mu wyrażę zgodę, bo ja często z nich coś wysyłam, ale powiem mu od razu just focus on this folder and obsidian. A dobra, on już wyczaił zanim to napisałem. Dobra, I me to run it here. Czyli chciałem O, dobra, super. Możć dostępu tylko do do jakiejś części.

**29:18** · Można mu dać dostęp. Jakbym wszędzie teraz kliknął den, to by nie miał dostępu do tych innych rzeczy. On musi zapytać o dostęp, nie?

**29:24** · Bo wiem, że on ma do tych, które tutaj ma mieć dostęp. Tak, tak.

**29:30** · I może mieć też jak chcecie, ja teraz kliknąłem na przykład allow dla desktopa i dla downloads, bo jak widzicie mam tu jakieś screenshoty albo eksportuje jakieś rzeczy, które potem chcę załączać jemu, więc wtedy mówię mu weź wejdź se na pulpit i przenieś se ten plik albo coś tam, nie? E, więc ja mu akurat daję dostęp do downloads i desktop zawsze.

**29:49** · Dobra, ale on mi powiedział, że to jest puste i tak dalej, więc dobra, to powiedzmy mu po prostu, że tak chciałem to odpalić tutaj i wklejam tego prompta i set it up. Tutaj na początku zrobię tak set it up, żeby wam też było to od razu wklejone, czyli żeby ustawił na początek nam ustawienie cloda i obsydiana i stworzy te pierwsze pliki, które ja proponuję i tutaj przygotował listę. W odpowiedzi pokazał to, co mu tam wysłaliśmy. Pyta nas, czy potwierdzamy, że takie jest cloud MD. Powiedziałem: "Tak, potwierdzam".

**30:33** · On powiedział, dobra, stworzyłem ten MD, no to powiem mu teraz, okej, teraz stwórz strukturę.

**30:45** · I on ma teraz w swojej strukturze tutaj w środku w clodzie napisane, że struktura naszego sejfu jest taka 00 inbox, 1. Journal 2.0 projects, 99 systems. Te cyfry są tu na początku dlatego, że sortowanie plików w obsidianie jest według nazwy. Dlatego dodajemy 00 na początku, żeby on inbox na górze wyświetlał 1.0, potem journal projects i tak dalej, nie?

**31:14** · Dobra. I on tutaj napisał, że może stworzyć te pliki, czy chce kontynuować.

**31:18** · Klikam jest.

**31:20** · Jak widzicie, z lewej dodały się te wszystkie pliki.

**31:25** · I od tego momentu właściwie zaczyna się już wasza praca i wasza rozkmina z tym, co chcecie zrobić, nie? Ja wam polecam jeszcze tutaj stworzyć później sobie właśnie na przykład te pliki Home czy tam Weekly Rhythm, ale to już nie chciałem tego dodawać tutaj, bo to od was zależy. Może nie będziecie tego w ogóle potrzebować i będziecie chcieli sobie jakoś inaczej z tym pracować, więc na przykład niektórzy pracują tylko na tym inboxie, także zróbcie to już jak uważacie. I gdy macie ten pierwszy zestaw, zestaw plików, to drugą rzecz, którą od razu potem robicie, to jest uzupełnienie kontekstu. I ten kontekst, który uzupełniacie, to jest kontekst o was, czyli czym się zajmujecie, co robicie i tak dalej, nie? Więc tu wam wysyłam taki taką templatkę do uzupełnienia, czyli te cztery rzeczy.

**32:13** · Właściwie tu trochę więcej ich będzie.

**32:20** · Oj, tu wklejam kolejny prompt i tego prompta musicie sobie pouzupełniać, czyli tutaj how I think, how I work, struktura Volta, to akurat możemy usunąć. Zasady już też są. Możecie opisać dokładnie jak chcecie, żeby z wami współpracował, nie?

**32:37** · To też są ważne zasady. I na koniec najważniejsza rzecz, druga rzecz i trzecia rzecz, czyli nad czym pracujecie, co jest dla was najważniejsze, nie? jakieś jakaś taka struktura, żeby on rozumiał jak potem wam pomagać. No i teraz tak, jak już macie te prompty, no to uzupełniacie kontekst. I teraz z fajnych rzeczy dzisiaj po tym callu, albo może nawet zaraz, nawet mi się uda niedługo, wrzucam na Eltona, na tą apkę, co wam już zajawiałem na Vibe Hero, taką zajawkę tego, co się będzie pojawiało i działało w przyszłym tygodniu. I pojawi się tutaj z lewej strony oj prompt builder.

**33:09** · I ten prompt builder to jest prompt builder do budowania historii o was, nie? Gdybyście chcieli sobie gdzieś tam to wykorzystywać później łatwo mieć dostępne w innych miejscach, ale też żeby na przyszły tydzień w sprincie czy w ogóle we pracy z AIem i w pracy tutaj z Eltonem, żeby Elton też trochę więcej się o was dowiedział, nie? Także tutaj wpisujecie sobie rzeczy, to jest podzielone na etapy i teraz tak wpiszecie tutaj kim jesteście, czym się zajmujecie. Mogę sobie tutaj wypisać stąd pozaznaczać rzeczy albo sobie coś jeszcze dopisać i tak dalej.

**33:47** · I później mamy kolejną zakładkę, która jest my project. Czyli tu możecie sobie w taki wizualny sposób, o to usunę jeszcze dodać swoje projekty, czyli na przykład tam Elton, tutaj bym sobie dodał Vipe Hero i tak dalej, nie? i to się wszystko wam aktualizuje w tym prompcie po prawej i zapisuje się. Natomiast na ten moment zapisywanie jest tylko lokalne, więc sobie potem po pracy skopiujcie lepiej tego prompta w razie gdyby wam miało to uciec, nie? No i jest tutaj więcej działów, które ja zidentyfikowałem jako takie, które uważam, że bardzo usprawniają pracę AIaja, gdy ma je w kontekście. Więc opiszcie też jak wy w ogóle myślicie i działacie.

**34:28** · Tutaj możecie dać znać, że korzystacie z tego systemu. On jest już tutaj wgrany, więc będzie będzie działał wam jakby automatycznie. Możecie to też pominąć, bo już będziecie mieli to w jaju. Tutaj jakieś podstawowe zasady. Możecie dodać kolejne zasady jak chcecie do tego, jak on ma z wami działać. Jak widzicie, ten prompt po prawej cały czas się aktualizuje, więc jak już z tym skończycie, to będziecie mieli pełny prompt, który bierzecie i wklejacie mu tutaj i mówicie: "Tutaj jest info o mnie".

**34:58** · zaktualizuj cloud MD, nie?

**35:04** · I zaproponuj jak zacząć pracę nad tym secondem. Okej. i po prostu on sobie teraz poaktualizuje te wszystkie rzeczy, powrzuca je i na końcu wam dać znać od czego zacząć, jeśli sami nie wiecie, ale myślę, że będziecie wiedzieli. Po prostu zaczniecie sobie tutaj sami dodawać te projekty, jakieś nowe foldery, w których będziecie trzymali jakieś osobne rzeczy.

**35:33** · Możecie pytać o to cloda, Gemini i tak dalej, jak to robić. I teraz jeszcze jedna fajna funkcja, którą polecam, ale też jest dosyć niebezpieczna.

**35:42** · Jak klikniecie shift i tab, to włącza się taka yyy opcja fast forward, accept edits on. Czyli on sam może sobie tworzyć pliki, zmieniać rzeczy bez pytania, więc będzie pytał tylko raz, a potem może już kolejne rzeczy zrobić y za was, nie?

**36:01** · Dobra, on was już tutaj dalej poprowadzi. No to to wszystko będzie zależało od tego, co tam chcecie zrobić i zbudować sobie w takim systemie, ale to są takie maksymalne podstawy, nie?

**36:12** · Dodatkowo jeszcze jeśli chodzi Dian, to polecam wam robić coś co nazywa się skille, czyli to już wam pokażę na tym moim gotowym projekcie, w którym ja sobie działam i wam też potem te skille przekażę. I mam tutaj dwa skille czy trzy, które są mega fajne i w sumie teraz przejdziemy sobie przez jeden z nich. Więc znowu sobie wchodzę tutaj. Clear. Znowu jesteśmy w tym moim prawdziwym systemie, który działa na co dzień ze mną i zrobimy sobie może skilla z journalem. I teraz tak w ustawieniach coś co powinniście zrobić jeśli chcecie skill do journala i żeby działał wam łatwo kalendarz to wchodzicie w ustawienia wchodzicie w Daily Notes tu z lewej i w Daily Notes zaznaczacie new file location na journal, żeby się pojawiało tutaj. Co wtedy się wydarzy? Dzięki temu, że zainstalowaliście wcześniej plugin kalendarz, to tutaj w tej zakładce możecie kliknąć open today's daily note. Jak to kliknę, to się automatycznie dodało do folderu journal z dzisiejszą datą i dzięki temu tutaj mogę zapisać jakiś brain dump, nie? I na przykład teraz zrobię sobie tutaj info, co by tu mu napisać, żeby to fajnie pokazać na przykładzie.

**37:42** · Mam dzisiaj trzy projekty do zrobienia. Nie wiem od którego zacząć. Czy najpierw ogarnąć materiały na community.

**37:58** · Weltonie czy zrobić do końca landing na dla nowego klienta. Nie wiem, coś takiego. Tu bym sobie ogólnie wypisał z mojego mózgu rzeczy. Kiedyś postaram się wam pokazać jakąś taką prawdziwą notatkę, ale to musiałbym najpierw ją zweryfikować, czy tu jest coś, z czym chce się dzielić. Ale dobra, mamy coś takiego i teraz ja mam tutaj ukośnik po prostu i moje różne skille nie są tutaj bardzo różne, już też niektóre wbudowane. No i mam tak jak poranny przegląd, czyli rano sobie tutaj zaczynam od sprawdzenia tego, co tam dzisiaj na tapecie. Mam LinkedIn post, to za chwilę sobie też zobaczymy, ale właśnie mam też journal i mam tutaj dwie journalowe sesje i obie są zarąbiste. Po pierwsze, journal session, zawsze od tego zaczynam. On zadaje dodatkowe pytania i rozkminy. Pomaga po prostu pogłębić to, co napisaliście. Czyli jak klikniemy journal session, zobaczymy teraz w sumie dla którego się odpali.

**38:58** · Czy on z czai, że dzisiaj to dzisiaj yyy zdejmę to na chwilę, w razie gdyby coś tu miało wyciec, co nie chcę.

**39:08** · M o dobra ogarnął od razu, który z tych trzech projektów siedzi ci teraz najgłębiej w głowie. Nie ten, od którego nie możesz się uwolnić. No i właśnie to są takie pytania uzupełniające, więc to jest ogólnie, no teraz napisaliśmy trochę z czapy ten przykład, ale te pytania są bardzo fajne i później jak przejdziecie sobie przez takie pytania, to robicie podsumowanie i uzupełnienie do tego, co spisaliście, nie? To takie o AI journalingu o tym będę jeszcze mówił.

**39:35** · To teraz sobie w skrócie przejdziemy przez to, nie?

**39:38** · No to mogę mu powiedzieć, że cały czas rozkminiam Eltona. Chciałbym to zrobić najpierw, nie? I on teraz sobie to obczai i zada takie pogłębiające pytania. Czasami jak jestem taki zablokowany i właśnie nie wiem co zrobić w tym journalu, a czuję, że chcę coś z siebie wyrzucić, to mega dobrze na mnie działa, nie? Tutaj mu napiszę, że dobra, koniec pytań, zaktualizuj notatkę.

**40:07** · To już mu tak utnę. Normalnie bym odpowiedział trochę dłużej mu na te pytania, żeby zrobić Eltona od razu. Dobra. I jak widzicie, on to zaktualizował. I teraz gdy mam taką zaktualizowaną notatkę, o coś się tutaj wydarzyło z edytowaniem. Zaraz zobaczymy.

**40:34** · Okej.

**40:36** · jest. Jak wrócimy sobie do tej notatki, no to on tutaj jakby zrobił podsumowanie. I teraz co jest fajne w obsydianie, to że ja mogę sobie od razu wywalić ten tytuł, bo go tutaj nie potrzebuję, bo mamy go tutaj na górze.

**40:47** · Mamy do czego doszedłem i mam to zadanie, a tu na dole jest ta moja oryginalna notatka, nie? I teraz jak jeszcze głębiej chcę sobie z tym pracować, wyciągnąć jakieś wnioski, no to mega super promptem jest ten journal stoik. Ja sobie jego odpalam. To też jest taki skill. w ogóle ultra fajnie działa. Też wam go prześlę i będziecie mogli go też dodać do swojego projektu.

**41:08** · I on po prostu ma taką stoicki ogląd z właśnie tej filozofii stoickiej i podaje jakieś takie fajne cytaty, rozkminy i tak dalej, nie? gdzieś tam z Insightów wcześniej właśnie yyy miałem mega problem z takim skupieniem się na jednym projekcie, że strasznie się rozpraszałem, robiłem 10 rzeczy na raz i właśnie podał mi takie fajne notatki od Aureliusza na przykład, że to co jest tutaj napisane, nie? albo jakieś tam od Seneki i one są wtedy tak jakoś do mnie mocno mocno uderzają. Często są fajne.

**41:45** · No i on tu zaczyna też dopytywać jakieś rzeczy i tak dalej. No i potem wam przygotuję feedback po prostu. Dobra, bo widzę, że już tam dużo czasu leci. Ja chcę wam pokazać jeszcze jedną rzecz. Tu jak sobie przez niego potem przejdziecie, to zobaczycie. Naprawdę do fajnych rzeczy można dojść, ale to jest już taka prywata trochę, więc w sumie czyszczę kontekst. Zaczynamy kolejną rzecz.

**42:08** · I co teraz? Wejdziemy sobie do IDA, które to było? Prompt philosophy. Dobra, wejdziemy sobie do tego. Czyli tak, piszę mu, chcę napisać posta na LinkedIna o prompt philosophy z ideas. Czyli ogólnie zaczynam posty często jak piszę posty na LinkedIna, to staram się o to.

**42:32** · Widzicie, on już sobie sam załadował skilla, LinkedIn post i ten LinkedIn Post jest rozpisany na sześć kroków, nie? O czym chcę napisać?

**42:41** · o tym, co jest w pliku prompt philosophy i on mi pomaga po prostu rozbudować ten proces na podstawie moich myśli, czyli bierze jakieś moje rozkminy z całego tego Volta albo z tej idei i zaczyna to ubierać w jakąś strukturę, którą ja na końcu sobie biorę i trochę przepisuję i na jej podstawie powstaje post, nie?

**43:03** · Więc on sobie przeczytał teraz co jest w tym pliku i mamy na przykład okej mam lecimy do etapu drugiego, czyli wybór hooka. Mamy trzy hooki nie większość ludzi pisze prompty źle i to nie dlatego, że są za krótkie, słabe. Przez miesiące myślałem, że dobry prompt, słabe. Akt ST nie robi różnicy. Kont robi całą robotę. Nie wiem. Wszystkie słabe. Daje więcej.

**43:27** · M to nie jest też tak zawsze, że musicie wybierać z tych trzech, nie? Więc ja poprosiłem go teraz o więcej, więc on przygotuję kolejne hooki.

**43:36** · Dobra.

**43:40** · Y, ten mi się podoba. E, dobra, pójdźmy w e na razie mniej więcej, bo to też jest jeszcze tylko początek. Będziemy pisali to lepszym językiem i tak dalej w kolejnych krokach, nie? Więc tutaj mu dałem znać, że wybrałem e i on przygotował na tej podstawie strukturę posta, czyli mamy ten hook. AI nie jest głupie. Ty ty nie dajesz odpowiedniego info.

**44:03** · Potem proponuję napisać o prom przykład złego promptu dobrego. Potem wyjaśnienie co to znaczy kontekst w praktyce, twoja zasada. Y i pytanie do osób, które będą widziały tego posta. Stwierdzam, że dobra, pasuje. Lecimy dalej.

**44:24** · I on teraz rozkminia i zaraz przygotuje nam kolejny krok. Więc po prostu ja już te posty na LinkedIna ręcznie pisałem w ten sposób wiele razy. Miałem taki proces, który sobie gdzieś tam rozpisałem, że przygotowywałem najpierw hooka, potem jakąś mniej więcej strukturę, co ja w ogóle chcę powiedzieć. Wklejałem tam to podstawowe info i potem dopiero przygotowałem taki pierwszy draft, nie? To jest pierwszy draft. jakby. Dobra, jest spoko. Kolejny krok. Nie czytam go teraz, ale normalnie bym przeczytał, tylko chcę wam pokazać jakby jak jak to się kończy i czy co tu się będzie działo, nie?

**45:02** · Dobra. I on teraz znalazł jakby jakieś tam przykłady elementów, które są słabe w tym poście. Przerobił to.

**45:13** · Git. Leć dalej.

**45:16** · To już chyba będzie ostatni krok albo przedostatni. Teraz no i teraz jest mega fajny element. Jak już mamy całą strukturę, to zazwyczaj ludzie na tym etapie kopiują sobie taki pościg i wrzucają i on wtedy mega brzmi jak AI. A ja wrzucam jeszcze jeden krok zawsze, który sprawdza taki mój ton of voice i żeby brzmiał właśnie jak jak wozu bardziej i on zaproponował to zmienić na to, nie?

**45:48** · Ja mu mówię dodajmy i wtedy on to dodaje i ja na końcu dopiero takiego posta już jest gotowy.

**46:00** · Dobra tutaj to mi pozrobił jakieś tam statystyki checklista i tak dalej. Mówię mu teraz stwórz mi MD z tym postem. No i właśnie teraz to jest fajne, że jakbym w AIU to miał, to bym musiał to gdzieś skopiować, potem gdzieś to wkleić, trzymać to nie wiadomo gdzie, po prostu w jakimś edytorze. Jakby ja zawsze miałem z tym mega związany yy chaos po prostu, nie? A teraz on sobie po prostu dodał ten plik tutaj jako LinkedIn prompt yyy philosophy i tutaj mamy post cały i ja już tu w środku mogę sobie go edytować.

**46:40** · No i po prostu czytam sobie, co tu jest napisane i wszystko zmieniam tak po swojemu po prostu, nie? I całego tego posta bym sobie przerobił. I teraz powiedzmy, że usunąłbym to, to bym usunął, to bym rozbił i tak dalej. I na końcu ląduje z postem. Mogę go sobie skopiować i wrzucić na LinkedIna. Ważne, że pozmieniałem sobie tutaj różne rzeczy i zrobiłem, żeby brzmiało to nie jak AI.

**47:03** · Czyli na przykład to zdanie mega brzmi jak AI, to brzmi mega jak AI, taki krótki zestaw tych słów brzmi jak AI, więc ja to wszystko biorę i przepisuję i zmieniam, żeby to nie brzmiało jak AI, żeby brzmiało tak jak ja, bo ja chciałem tylko mniej więcej strukturę z AIem ogarnąć, mniej więcej jakieś słowa, żeby mieć inspirację, ale potem i tak to przerobić na swoje, nie? Więc gdy to wszystko sobie poprzerabiam, to dopiero to kopiuję i wklejam na LinkedIna. A co jest najważniejsze, aktualny post na temat yyy tego co jest tutaj napisane jest już tutaj w kontekście, czyli w przyszłości jak będziemy pisać kolejne LinkedInowe posty, to on będzie już lepiej znał moje yyy sformułowania i tak dalej. I na przykład mógłbym sobie tutaj rozkminić, żeby stworzyć sobie jakieś źródło do t of voice i wrzucać tam wszystkie linkedinowe posty i on wtedy z nich by odczytywał. Więc to jest jakiś tam powiedzmy dodatkowe info na temat tych skill. Te skile wam też podeślę. Tutaj będą dostępne. Żeby dodać skilla, po prostu napiszcie do Cloda. Ja wam wkleję po prostu informacje z czego się taki skill składa. On sobie sam umie dodawać swoje skille.

**48:11** · Jak wygląda taka praca na co dzień?

**48:13** · System ogólnie tak jak widzicie sobie rośnie. Nieem zaczynałem od tego, nawet jeszcze prościej. Nie miałem tych cyfr, ale polecam je dodawać, bo to wtedy od razu jest trochę bardziej zorganizowane.

**48:24** · No i zacząłem sobie dodawać te kolejne foldery i tak dalej. Mega kluczową cechą tego systemu jest to, że żeby stworzyć sobie, o, widzę, że się nie dodał ten plik, więc będę musiał to zaktualizować, stworzyć taki plik, który się nazywa cowork log. I tutaj mamy w systemie plik, który się nazywa cowork log. I za każdym razem jak skończę coś robić, to mówię mu: "Zaktualizuj cwork log". podsumuj co zrobiliśmy.

**48:52** · I dzięki temu po każdej wymianie wiadomości i zadań ja zapisuję podsumowanie do corloga tutaj tego co robiłem. Tu są te wszystkie informacje i rzeczy jakimi się tam zajmowałem w ostatnim czasie. No i gdzie to zostało?

**49:06** · I on sobie teraz edytuje ten plik i go podsumuję. Powie, że zrobiliśmy tego posta i raz w tygodniu robię sobie taki sprawdzenie. Mówię mu: "Przeczytaj coworklock i zobacz, czy powinniśmy coś zautomatyzować, stworzyć jakieś skile, albo może mogę robić coś lepiej". Nie. I on wtedy potrafi przeanalizować mój tydzień pracy i rozkminić, które rzeczy są fajne, a które nie. Nie. Dodał teraz to do corklogga. Klikam zapisz.

**49:33** · Corkl zaktualizowany. No i tak jak mówię, pod koniec tygodnia przejdę sobie i obczaję, co tam mogę poprawić, nie?

**49:40** · Jak zaczynam dzień? do zaczynania dnia mam właśnie taki prąd poranny. Yyy, nie tutaj nie ma go tutaj, tylko w tym, sorry. Yyy, poranny przegląd. On po prostu sprawdza jakie mam zadania na dzisiaj, co zrobiłem wczoraj, czy są jakieś spotkania, rutyny do zrobienia, czy miałem o czymś pamiętać i tak dalej.

**50:00** · Nie. Albo na przykład ostatnio robiłem długo landing pagea na Lovable i właśnie doś mega ciekawej interakcji doszło za jajem, bo zobaczył, że już tam od tygodnia kończę ten landing page, nie mogę go kończyć i po prostu pytałem go o jakieś tam rzeczy z czapy i mi sam napisał Cloud, że ej skończ ten landing page i dopiero wtedy pytaj o te kolejne rzeczy, nie? Bo to już trwa tydzień i za długo. Więc też jest trochę takim moim coachem w sumie śmiesznie i sam ewoluował w tą stronę.

**50:27** · Co robić po wykonaniu zadania? to zrobić cork log i na już skończycie zadanie to po prostu ukośnik clear czyścimy sesję i zaczynamy od nowa, nie?

**50:40** · No i raz w tygodniu szukajcie optymalizacji, czyli co możecie zrobić, żeby usprawnić działanie cloda waszego waszego systemu i i wasze działanie po prostu, nie?

**50:52** · Dobra, mega dużo informacji, mega mocno. Ja wam przygotuję te dodatkowe prompty. Jutro pewnie się pojawią tutaj w w tej zakładce materiały dodatkowe.

**51:02** · Oprócz tego dzisiaj się pojawi prompt builder, gdzie będziecie mogli zbudować cały kontekst o sobie i potem pobrać go od razu jako plik MD, skopiować i se go gdzieś wkleić. I dopóki nie będziecie usuwać pamięci z przeglądarki, to zostanie wam w pamięci tutaj wasze ustawienia. Później dodam zapisywanie w bazie danych, ale jeszcze teraz nie chciałem tego robić. Tu też można sobie edytować po prostu ten ten MD.

**51:31** · No i będzie to dostępne tu z lewej strony pod tymi pod tymi pomysłami, nie?

**51:34** · Bo na razie była baza pomysłów i tak dalej. Podobne rzeczy takie jak to pojawią się w przyszłym tygodniu w poniedziałek tutaj w w niedzielę chyba nawet już w Eltonie. Tylko, że dotyczące sprintu, który będziemy sobie tam przechodzić, nie?

**51:47** · Dobra, dajcie znać, czy macie jakieś pytania. zminy. Może chcecie jakieś więcej przykładów, jakieś konkrety w ogóle z tego, co tutaj się dzieje w w tym ustawieniu? Jakieś może inne elementy całej układanki?

**51:59** · Ja nie mogę gemila podpiąć pod terminal jakoś.

**52:04** · Dobra, a co, co się dzieje?

**52:08** · Nie wiem jak to zrobić po prostu.

**52:09** · A bo widzę, że też Gemine. Dobra, Gemini CL. A masz zalogowa, masz konto płatne na Y.

**52:18** · A nain dobra.

**52:28** · Dobra, to tu jest dokumentacja. Ja też już nie pamiętam jak to było. Przejdźmy sobie do instalacji.

**52:36** · A czy wiesz czy masz na komputerze coś takiego jak Hombru?

**52:43** · Raczej jeżeli trzeba było to instalować to nie mam.

**52:48** · Dobra. A masz może a i jakby, bo też nie wiem w sumie, czy masz może, robiłeś jakieś apki na kompie, masz npma?

**52:55** · Mam.

**52:56** · A no to to możesz to wkleić po prostu w terminalu, w tym folderze w obsydianie. Okej, wrzucam na czacie i tam powinno cię już dalej poprowadzić po tym, co masz zrobić, jak się zalogować, zaautoryzować jeminaja i tak dalej.

**53:22** · Czy dostęp do Eltona to mamy wszyscy?

**53:25** · Jak to jest?

**53:26** · Tak.

**53:28** · App.

**53:31** · So tutaj znajdziesz Eltona.

**53:36** · Ja muszę ręcznie autoryzować maila, więc nie wiem czy dodałem już wszystkich maile. Musiałbym sprawdzić, ale jak ci nie zadziała, to daj znać, to po prostu dam twojego maila. Ważne, żeby dodać tego maila z Vibe Hero, bo to po nich szukam, ale to od razu dodam. Mogę nawet teraz w sumie, bo Elton jest zamknięty i na razie długo zostanie zamknięty dla ludzi ze społeczności. Tylko ogólnie to będzie taka platforma edukacyjna, tu też będą filmy i kursy i tak dalej. Y, ale nie zamierzam teraz tego jakoś otwierać dla ludzi, więc y tylko wy będziecie mieli dostęp jakby co.

**54:13** · M i w Eltonie na razie jest na tej wersji online baza pomysłów, nie? Tutaj do tych pomysłów też w środku są prompty w razie gdybyście tam nie widzieli.

**54:22** · Można sobie skopiować, poobczajać. Ja będę w przyszłym tygodniu kolejne pomysły dodawał. Można se zapisać na potem wasze ulubione. No i ta trzecia zakładka, którą ja mam jeszcze na kompie tylko tutaj, no prompt builder to będzie po prostu ta zakładka z tym budowaniem promptów. Ja ją dzisiaj wieczorem wrzucę na Eltona.

**54:42** · Wiesz co, bo ja mam informację, że czeka na zatwierdzenie, nie, na Eltonie. Tak, tak.

**54:49** · A jakiego maila użyłeś? To ja cię od razu może dodam. lelenukasz gmail.com.

**54:56** · Dobra, dobra, muszę wejść do bazy.

**55:09** · Nie wiem, czy mogę wam pokazać bazę, czy nie. W sumie to może wyłączę już nagrywanie i stop. M
