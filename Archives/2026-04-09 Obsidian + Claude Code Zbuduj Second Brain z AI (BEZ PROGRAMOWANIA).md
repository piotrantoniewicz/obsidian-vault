---
type: Web
authors: '[[Robert Szewczyk]]'
url: 'https://www.youtube.com/watch?v=7i85dqtkptU'
published: 2026-04-09T00:00:00.000Z
created: 2026-04-24T00:00:00.000Z
tags:
  - automatyzacja
  - narzędzia-AI
  - strategia-AI
---


![](https://www.youtube.com/watch?v=7i85dqtkptU)

## Transcript

### Wprowadzenie do lekcji

**0:00** · Wpisuję jedną komendę i mój chaos z notatek zamienia się w uporządkowaną fazę wiedzy. Andrew Kpati, współzałożyciel modeli GPT, w jednym ze swoich ostatnich tweetów opisał podobny system. Pliki w Markown, lokalna baza wiedzy, zero chmury. Zainspirowałem się tym i nieco podrasowałem mój drugi mózg w Obsidian, który jest zasilany Cloud Codem. A dzisiaj pokażę ci jak to działa i jak w prosty sposób możesz zrobić podobną bazę wiedzy u siebie. W dodatku za darmo i bez programowania.

**0:31** · Tak więc bez zbędnego przedłużania lecimy z tematem. Większość ludzi traktuje notatki jak cmentarzysko dobrych pomysłów. Zbierasz wiedzę w trzech różnych apkach, masz 50 otwartych kart i nic z tego nie korzystasz. Andrej Karpati, a więc człowiek, który współtworzył Chat GPT i autopilota Tesli, napisał tweeta czy Tamexa, w którym opisał koncept lokalnej bazy wiedzy. 400 000 słów markdown, Obsidian jako frontend, LLM jako backend do przetwarzania danych.

### Karpathy i lokalny drugi mózg

**1:04** · Bez chmury czy skomplikowanego raga. Czyste pliki w formacie Markdown lokalnie na twoim dysku. Zainspirowałem się tym i zacząłem budować coś podobnego i nie jestem jedyny, bo w ciągu kilku dni po tym tweecie pojawiło się kilkanaście filmów na angielskim YouTubie. Ale jest pewien haczyk. Większość z nich pokazuje bazowy setup. Zainstaluj plugin, wrzuć Cloud MD i zadawaj pytania. Taki Obsidian Asa Chatbo ja podszedłem do tego nieco inaczej.

**1:34** · Zbudowałem system z kilkoma komendami, który nie tylko odpowiada na pytania, ale sam przetwarza chaos, krystalizuje wiedzę i wyłapuje połączenia, o których nie miałem pojęcia. Karpati ma około 400 000 słów w swoim wiki. Ja mam no troszeczkę mniej, ale mam komendy, które robią za mnie robotę. I dzisiaj pokażę ci jak to wygląda od środka. A teraz przejdźmy do konkretów.

**1:58** · Jeśli szukasz sprawdzonego serwera VPS, na którym uruchomisz Nightena Clot Code, OpenClow czy inne aplikacje Open Source, to niezmiennie polecam ten od głównego partnera technologicznego mojego kanału, a więc firmy Hostinger. Jeśli chodzi o mnie, to na co dzień korzystam z planu KVM2, ponieważ jest na tyle tani, że nie zrujnuje mojego miesięcznego budżetu i na tyle mocny, że wszystkie moje automaty czy aplikacje śmigają na nim na najwyższych obrotach. Sprawa jest prosta. Klikasz link w opisie, wybierasz interesujący cię plan, na przykład KVM2.

### Fragment sponsorowany

**2:29** · Teraz wybierasz interesujący cię okres.

**2:31** · Im dłużej, tym taniej. Wiadomo. Klikasz, posiadasz kod rabatowy, wpisujesz wielkimi literami Robert host. Klikasz zastosuj i cyk. Taki serwer na 2 lata wychodzi ci niecały 1000 zł. Moim zdaniem warto. W dodatku korzystając z linku i kodu w opisie wspierasz mój kanał. To co przekonało mnie do oferty od Hostinger to po pierwsze bezpłatne cotygodniowe kopie zapasowe, które potrafią uratować tyłek. A po drugie to, że Hostinger dba zarówno o osoby, które są techniczne i znają się na konfiguracji serwerów, jak i te osoby, które nie są techniczne, jak chociażby ja.

**3:01** · Dzięki temu możesz instalować całą masę narzędzi jednym kliknięciem, jak chociażby tutaj Naten, ale możemy kliknąć sobie tutaj, wyszukać chociażby clot code, kliknąć sobie tutaj, kliknąć potwierdź. Teraz wystarczy, że klikniesz kontynuuj. opłacić swój serwer, a system sam zainstaluje wybraną aplikację na twoim serwerze. Mój specjalny link oraz kod działają na wszystkie plany 12 miiesięczne. Jednak pamiętaj, że nic co dobre nie trwa wiecznie. Ja ci bardzo dziękuję, a teraz wracajmy do odcinka.

### Jak połączyć Obsidian z Claude Code

**3:30** · Czym jest Obsidian i jak połączyć go z Cloud Codem? Już tłumaczę. Obsidian to narzędzie, które widzisz swoją drogą na ekranie, które jest darmowe i zostało stworzone do zbierania wiedzy czy tworzenia notatek w formacie markdown, czyli formacie, który nadaje się idealnie do pracy z clot codem czy innymi agentowymi narzędziami, tak je nazwijmy. Jeśli chodzi o sam Obsidian, to link do niego znajdziesz w opisie.

**3:54** · Tak jak mówiłem jest darmowy, więc pobierz go i zainstaluj na swoim komputerze. I aby móc korzystać z terminala, a tym samym z clot codea w Obsidianie, w pierwszej kolejności klikamy sobie tutaj na Obsidian, przechodzimy do preferences. Następnie w menu po lewej stronie wybieramy wtyczki społeczności.

**4:12** · To co będziesz musiał zrobić to tutaj w zakładce tryb ograniczony wyłączyć go klikając tutaj. Ja mam wyłączone, teraz mogę włączyć i odświeżyć. Gdybym to, gdy to zrobię, to po prostu wtyczki się wyłączą i będą nas interesowały dwie wtyczki.

**4:29** · Mianowicie pierwsza wtyczka, ta o której mowa, to wtyczka terminal. Marzym tutaj mamy autorstwa poli ipse iti, nie wiem jak się to czyta, sorry. Więc jak przejdziemy sobie ją tutaj, całość wygląda tak. Link do tej wtyczki też zostawię w opisie. Nie będziesz musiał daleko szukać. Więc instalujesz ten terminal i następne to co musisz zrobić to uruchomić tą wtyczkę. O tutaj. Gdy to zrobisz terminal powinien pojawić się na pasku z lewej strony. O tutaj. Open terminal.

**5:00** · Teraz wybieramy sobie external. Będzie zewnętrzny. My chcemy ten zintegrowany.

**5:05** · Klikamy sobie tutaj. Hop. Terminal się nam odpalił. Teraz wystarczy uruchomić cloda komendą clot, co już pewnie doskonale znasz. i całość śmiga. Druga wtyczka, którą polecam ci zainstalować, nazywa się show hidden files. Co ciekawe, jest tego samego autora.

**5:21** · Dopiero teraz to zauważyłem. Jednak nie znajdziesz jej bezpośrednio tutaj w markecie z pluginami. Po co ci ta wtyczka i jak ją zainstalować? Zacznijmy od tego, po co ci ta wtyczka. Ta wtyczka służy do tego, że w obsydianie domyślnie jest tak, że jak mamy strukturę tutaj plików, co pewnie doskonale znasz z Cloud Codea, no to wszystkie foldery, które mają w nazwie kropkę z początku są ukryte, więc mamy kropkę obsidian kr cl clot i normalnie ich nie widać.

**5:50** · No i dzięki tej wtyczce, tak jak sama nazwa wskazuje, show hidden files, widzimy te foldery i pliki, które są ukryte w naszym wolcie, bo tak się nazywa miejsce, w którym przechowujemy te pliki w naszym drugim mózgu, second brainie. I aby skorzystać z tej wtyczki będzie potrzebne ci repozytorium na GitHubie, które widzisz teraz na ekranie. Mamy Obsidian Show Hidden Files. Link do niego będzie w opisie.

**6:16** · I to co polecam ci zrobić to kopiujesz ten link, wracasz do Obsydiana i mówisz Clodowi: "Zainstaluj ten plugin w moim obsidianie". Wklejasz link, klikasz enter i clot powinien zająć się całą resztą. I gdy clot zainstaluje ci już ten plugin show hidden files, jak tutaj, to musisz go oczywiście włączyć tutaj, przejść do ustawień i zaznaczyć ten checkbox show hidden files, tak jak jest tutaj.

**6:46** · W kolejnym kroku to, co polecam ci zrobić to stworzyć plik cloud.m, czyli taką instrukcję systemową dla cloda w ramach tego projektu. I u mnie on jest tutaj. Jak przejdziemy sobie do kropka clot, mam tutaj clot, to jest clot. Pyk. I w moim przypadku jest coś takiego. Mamy tutaj personę, język.

**7:10** · Tutaj mam rozpisany home MD, czyli taki mój dashboard. Do tego zaraz przejdziemy. To na razie cię nie interesuje. To jest taki system zbierania notatek w obsydianie, który powoli sobie wdrażam. Mam tu opisaną strategię single source of truth. Mamy tutaj strategię mojej marki, profil osobisty, brand strategy. Mamy tu wyniki mojego testu galupa. Mamy strukturę całego Volta, którą widzisz tutaj, czyli co w jakim miejscu się znajduje w tym projekcie. Co ty możesz wprowadzić to to formatin rules, wiki link do linkowania notatek zawsze używaj. Hop.

**7:40** · Kontekst relacyjny. Tworzysz notatkę. Sprawdź, czy pojęcia mają istniejące notatki.

**7:46** · Linkuj je. Tagowanie.

**7:49** · Format, analiza wiedzy, hop, concept notes, concept ideas. Wzór tego clot.md znajdziesz w mojej zamkniętej społeczności Operatorzy AI, do której link standardowo zostawiam w opisie.

**8:02** · Możesz dołączyć ze specjalną zniżką specjalnie dla moich subskrybentów, więc jeżeli chcesz, nie chce ci się tego przepisywać i chcesz mieć gotowca, to zapraszam. Mamy file naming, notatki dzienne, research analiza, materiały edukacyjne, selfde. Gdy Robert powie: "Zaktualizuj kod MD, przeczytaj obecny clot.md, przeanalizuj ostatnie pliki i konwersacje. Zaproponuj konkretne zmiany. Dodaj, usuń, zmień linię, poczekaj na akceptację przed napisaniem.

**8:27** · Ogólnie jeśli nie wiesz jak coś zrobić, to polecam odpalić Cloda i go o to zapytać. Właśnie znajdujemy się w repozytorium Obsydian Skills, gdzie znajdziemy oficjalne, z tego co się orientuje skille, czyli umiejętności dla Cloud Code od Obsidian. Repytorium będzie w opisie. Jak widzisz, ma 21 000 gwiazdek, niedawno miało 17000, więc całkiem dobrze to idzie. I możesz zainstalować te skills za pomocą tych komend tutaj albo za pomocą tych komend.

### Instalowanie Obsidian Skills dla Claude Code

**8:56** · Hop. Mamy tutaj instrukcję dla clota. To co ja ci polecam zrobić to skopiować sobie link, wrócić do obsidiana i znowu powiedzieć: "Hej, chciałbym zainstalować w naszym dokładnie w tym projekcie skills do Obsidian dla Cloud Code." Hop, wklejamy link, mamy coś takiego i Clot za chwilę powinien zainstalować pakiet skills na twoim komputerze. Jeśli chodzi o skills, to jak widzisz tutaj po lewej mamy kropka clot folder. Mamy tutaj skills i mamy różne skille do obsidiana.

**9:30** · Teraz dla przykładu, żeby ci pokazać, że Cloud widzi te pliki w tym projekcie, no to zapytajmy się go, jakie skills mam tutaj zainstalowane i co dokładnie robię. Stwórz taką prostą listę. Narzędzie Whisperflow, ono się jeszcze pojawi.

**9:48** · Klikam enter. Obsidian formaty, czyli formatowanie. Obsidian Markdown pomoc Obsidian Flavored Markdown Vikilinks Properties Obsidian Basis Stworzenie edycja plików krop base database views.

**10:01** · Filtry formuły Obsidian CLI interakcja z voltem przez Obsidian CLI search task properties. Jason Canvas, stworzenie plików krvas, mindmapy, flowcharty, wizualne połączenia i dlaczego Obsydian jest fajny jeżeli chodzi o współpracę chociażby Cloud Colda z tym narzędziem i dlaczego Andrew Carpati tak nim się zachwyca i zresztą wiele osób w tym również ja, ponieważ ten obsydian służy

### Graf wiedzy w Obsidianie

**10:27** · mi również jako takie jedno źródło prawdy dla innych projektów w cloud codzie, z których korzystam już w warpie, czyli w moim normalnym IDE, w innych projektach, jeżeli potrzebuję na przykład sięgnąć pod strategię, to tam w cloud.md mam opisane, że tutaj zbierają się wszystkie rzeczy. I to co jest fajne w obsydianie to jak przejdziemy sobie tutaj po lewej mamy graf wiedzy, czyli możemy łączyć ze sobą różne notatki i powstają nam, a zresztą sam zobacz.

**10:53** · Hop, klikam sobie tutaj i widzimy jak powstają połączenia z moich wszystkich notatek. Wygląda to kozacko.

**11:04** · Widzimy co ze sobą i jak się łączy. A czy w ogóle się łączy? Powstaje nam taki fajny grafik, który możemy sobie przesuwać. Powstaje taka całkiem niezła siatka. Dzięki temu Clot, gdy go zapytam o jakąś rzecz, może szybko sprawdzić tą rzecz w obsydianie plus może sprawdzić wszystkie połączenia z tą rzeczą, dzięki czemu może udzielać nam dużo precyzyjnych, dużo bardziej precyzyjnych i takich konkretnych odpowiedzi. Dobra, mamy środowisko, ale sam setup to dopiero początek.

**11:34** · Teraz pokażę ci komendę, która robi prawdziwą robotę.

### Krystalizacja wiedzy na bazie notatek

**11:39** · Teraz czas przedstawić ci komendę Brainsweep. To mój taki cotygodniowy rytuał, który zamienia chaotyczną skrzynkę z chaotyczny inbox z wszystkimi linkami, rzeczami, które sobie zapisuję w uporządkowaną bazę wiedzy. Mój problem był taki, że zbieram linki, zbieram różne jakieś rzeczy, zapisuję różne rzeczy, a później już do tego nie wracam. Więc tutaj mam rozwiązanie mojego problemu i zarazem serce mojego systemu.

**12:03** · Mamy tutaj opis Brain Swip inbox 0 dla IDS i ID Ideaverse to mój inbox, czyli folder, do którego wpadają notatki głosowe z Whisper Flow, skopiowane artykuły i rzeczy, które dodam, czy szybkie myśli. Po tygodniu mam ich tam z 20, 30 i to wszystko są nieobrobione notatki, do których nie wracam. Jeśli chodzi o Whisper Flow, to narzędzie, które zamienia mowę na tekst jest dostępne zarówno na telefonie, jak i na komputerze, co jest mega wygodne.

**12:34** · Polecam je, jeżeli chcesz je przetestować przez miesiąc ze Frico, to na dole masz link i ja tutaj zapisuję sobie notatki albo na telefonie, albo na komputerze. I te notatki później lądują tutaj w folderze ID ver. Jak sobie otworzymy, mamy tutaj archiwum jakichś starych notatek. Tutaj mamy świeże notatki, które dodałem w ostatnim czasie. Mamy tu jedną notatkę, która została, bo nic z nią nie robiłem, ale jak przejdziemy sobie tutaj do cloda, mogę wpisać brain myślnik swip. Hop, klikam enter.

**13:07** · Korzystam z opusa 46 z milionowym kontekstem. Tu mamy mojego tamagochi slashbody, jakbyś sobie chciał takiego wygenerować. Jest ich chyba 16. Każdy ma jakiegoś swojego z różnym poziomem rzadkości. Ja mam żówia, rinda, comona.

**13:22** · Więc pochwal się, jeżeli masz legendarnego albo epickiego Tamago czy Buddiego w clotzie. Daj znać w komentarzu. Jak coś to ta komenda body, ale można jeszcze wpisać body pet. I tu pojawiają się serduszka. Widzimy, że clot odpala brain swep, zaczyna od state file i skanowania inbox. I żeby ci pokazać jak to działa, to mogę wejść dla testu w Whisper Flow, kliknąć sobie tutaj, podyktować coś w stylu test.

**13:53** · Raz, dwa, trzy, kliknąć save. Hop, tu się nam dodało.

**14:01** · Widzimy, że tutaj też się dodało. Test raz, dwa, trzy. Więc nasza notatka jest.

**14:06** · Tak samo to działa, gdy korzystam z telefonu. Jeśli chodzi o to, jak te notatki się zapisują, to stworzyłem skrypt. W zasadzie kod stworzył. Do tego sobie jeszcze przejdziemy. Usuńmy sobie tą notatkę. Jeśli chodzi o to, jak działa Brain Swip, to klasyfikuje on każdą notatkę statusem Watch. Są to filmy do obejrzenia.

**14:25** · Read, czyli linki do strony artykułu, posta, obadać, sprawdzić, check. Idea content, czyli jakiś pomysł na film, nagrać odcinek post na live na następnym spotkaniu. Idea project zrobić system, zrobić program, aplikację, narzędzie Insight, refleksja, obserwacja przekminiłem. Ciekawa km, dłuższy tekst bez linku i bez zrobić task, zrobić konkretna akcja dodać, poprawić, naprawić krótkie, imperatywne. I widzimy, że Clot wrócił.

**14:51** · Brain Sweep tydzień 15 2026 047 i mamy informację, że w Inboxie jest dziewięć notatek, siedem nowych, dwie zachowane z poprzedniego swapu, swipu linków jest sześć, pomysłów na content trzy, do sprawdzenia cztery. Lecimy po kolei, zaczynamy od nowych, potem wrócę do zachowywanych. Teraz mogę zdecydować, co zrobić z tą wiedzą, czyli tu jest ten moment, którego mi wcześniej brakowało.

**15:18** · Mamy notatka 1 na 9. Zrobić odcinek o drugim mózgu, połączenie Obsidian X klotke. Tu dodatkowo powołać się na Karpatiego. Co z tym? Robimy tutaj 1 przecinek. Następnie mamy dwa nagrać odcinek połączen połączeniu clot code zapy 22. możemy albo ustawić przytworzono, hop, nieprzetworzono, przekierować, zachować w ID wersie albo skipnąć notatka 9. Chciałbym zrobić napisy w stylu co na ekranie. Dajmy tutaj 9 Kacper. Hop. Teraz klikam enter i zadzieje się cała magia.

**15:52** · Teraz działa to tak, że filmy na YouTube lecą automatycznie do Notebook LM, który pokazywałem w jednym z poprzednich odcinków. Tam jest tworzona transkrypcja i podsumowanie.

**16:05** · Linki lecą do CW for AI. On scrapuje, o nim też był odcinek na moim kanale. Te materiały podlinkuję w opisie. Po krystalizacji surowe notatki przechodzą z IDA verse do archiwum. Nic nie ginie.

**16:18** · Mam pełną historię, jakbym chciał do czegoś wrócić. Przez przypadek wyłączyłem tutaj dobre rada dla ciebie.

**16:24** · Jak pracujesz z klodem w terminalu i nie chcesz, żeby terminal się wyłączył. Na przykład klikniesz sobie tutaj, klikasz sobie tutaj prawy i dajesz tutaj przypnij. Ja już przypiąłem. Mam ten fioletowy znaczek. Bez tego jak klikniesz na coś, to terminal się wyłączy, przełączy się na inną kartę.

**16:39** · Tak więc wróciłem sobie do tego okienka.

**16:42** · Tutaj kolejna wskazówka dla ciebie.

**16:45** · Jak odpalimy sobie terminal, możesz wpisać sobie tutaj clot, dwie kreseczki, resume, hop, tak jak widzisz tutaj, kliknąć enter i możesz wrócić do jednej z poprzednich rozmów, które miałeś w terminalu. Mamy archive, istnieje. Oto podsumowanie przed czyszczeniem. Cleanup gotowe do wyczyszczenia. Skrystalizowano trzy pomysły na content. Content ideas Notes. Film Obsidian X Clot Code. Drugi mózg. Film Cloud Code plus Apify, film BMAT Method. Tu ktoś podesłał. Dzięki.

**17:19** · Czytam komentarze, zapisuję. Cztery linki. CW AI, Sumaris, BMAT Method, Super Shrimp apka CloudHut, Plugin, Ultraplan, Docs. Dwa przekierowane.

**17:31** · Kacper montaż info, napisy, styl referencji. Do archiwizacji osiem notatek. Pozostaje w ID jedna notatka zachowana z poprzednie na niego sweb.

**17:40** · Potwierdzasz czyszczenie? Tak, w tym momencie jak sobie przejdziemy tutaj to te notatki zaraz przejdą do archiwum. W ten sposób mam porządek i wszystkie są zdyponowane w odpowiednie miejsca. Tutaj mam AI zone, czyli to strefa, gdzie są rzeczy generowane przez AI.

**17:59** · Widzimy, że tworzę teraz Brainswepe, aktualizuję home.md i state file równolegle.

**18:05** · Home to jest taki dashboard. On jest tutaj. Hop. Mamy tutaj datę, kiedy był aktualizowany. Mamy tutaj second brain Robert Szewczyk. Widzimy, że się pojawia content pipeline. Mamy tutaj instrukcję jak korzystać z tych komend. Mamy tu różne projekty ostatnio przetworzone.

**18:21** · Hop. Mamy tutaj te rzeczy, które pokazywałem. Możemy sobie wejść na przykład tutaj. Ultra plan, plan mode 2.0 w cloud codzie w źródło. TLDR research preview. To jest nowa funkcjonalność, która powstała. Cloud draftuje plan w chmurze, review w przeglądarce z inline comments i emoji reactions. Execute w chmurze lub teleport z powrotem do terminala.

**18:41** · Kluczowe featery. Mogę dodać notatki, pogłębić te rzeczy. Tutaj mamy brain sweep tydzień 15 okres. Widzimy od kiedy. Przetworzono dziewięć notatek, sześć linków, trzy pomysły content.

**18:51** · Inbox 9 do0, zarchiwizowano 9. Mamy krótki opis. Wid przesłał open source framework z 12 agentami, party mode, pełny life cycle. alternatywa do naszego, czyli już widzi połączenia je samodzielnie to sugeruje. Ultraplan, hop, cloud, hop, skrystalizowane filmy.

**19:11** · Możemy sobie to przejść tutaj widzimy format YouTube, odcinek o tym. Hop.

**19:17** · Brainwip to fundament mojego systemu, ale skąd biorą się te notatki w moim inboxie? Zaraz ci pokażę pipeline, który sprawia, że nawet jak gadasz do telefonu, wiedza ląduje w obsydianie. No dobrze, jak to się dzieje, że notatki z Whisper Flow na moim komputerze bądź też telefonie zapisują się w moim obsydianie? Działa to tak, że Whisper Flow zapisuje te wszystkie notatki w jednym folderze i całość synchronizuje się przez chmurę. Tak więc masz do tego dostęp zarówno z poziomu telefonu, jak i komputera.

### Automatyczne zapisywanie notatek w Obsidian

**19:50** · Jeżeli mówisz do telefonu, tekst automatycznie ląduje w moim przypadku idea ver, czyli w inboxie Volta w obsidianie. Jeżeli chodzi o to, jak to technicznie wygląda, to przygotował dla mnie cloud code. Ja nie znam się na programowaniu, ale krok po kroku, co dzieje się pod maską. Trigger, co odpala skrypt. MacOS ma wbudowany system zadań w tle. Launched, taki chron, ale lepszy.

**20:13** · Nasz agent. Hop. Mamy tutaj, mamy tutaj skrypt. Odpala skrypt na dwa sposoby. Co 15 minut regularny interwał watch puffs reaguje na zmianę pliku. Baza whisper flow. Edytujesz notatkę. Magos mówi: "Hej, plik się zmienił, skrypt startuje.

**20:27** · Tutaj mamy log. Tylko jedna instancja, to nie wiem o co chodzi. Odczyt bazy whisper flow. Whisper flow trzyma notatki w SQL Lite. Tu mamy lokalizację.

**20:35** · Script podłącza się w trybie read only.

**20:38** · pobiera id title content created ad modified ad is deleted jeśli baza jest zajęta whisper flow akurat pisze trzy próby z dwusekundową przerwą state filę co już zrobione plik whisper state jason trzyma mapę dla każdej notatki z bazy skrypt sprawdz nie ma w stanie nowa notatka jest ale zmodyfikowana coś się zmieniło edytowana nadpisz plik jest to samo plik istnieje. Skip, nic nie rób.

**21:05** · Jest, ale plik ktoś ręcznie usunął.

**21:07** · Szanuj decyzję, nie reeksportuj.

**21:09** · Następnie taka notatka jest zapisywana jako markdown. Polityka kasowania, hop, zapis state i zwolnienie locka. Na końcu automatyczny zapis state. Jak mówię, nie, nie wiem co tu się dzieje.

**21:19** · Generalnie jeżeli jesteś w mojej zamkniętej społeczności, to podrzucę ci po prostu do tego dostęp. Będziesz mógł sobie to przerobić pod siebie, zapytać się Cloda jak to działa i zrobić coś takiego u siebie. Ja tylko przekmiłem, że Whisperflow zapisuje te rzeczy na moim kompie i że to się synchronizuje.

**21:34** · Powiedziałem o tym Clodowi, on wyszukał i zrobił tak naprawdę całą robotę za mnie. Jeszcze tu ci pokażę jak wygląda ten skrypt pythonowy. Jest to coś takiego. Hop. Wygląda to tak. I tak jak mówiłem ja nic przy tym nie kodowałem.

**21:49** · Ja tylko mówiłem co działa, a co nie.

### Dodatkowe komendy

**21:51** · Okej, mamy dane w volcie, ale co jeśli twoje notatki same mogłyby powiedzieć ci, co z czym się łączy? Dobra, czas na kolejną komendę. I ta komenda skanuje cały Volt, analizuje gęstość linków, znajduje klastry tematyczne, sugeruje mi połączenia między notatkami, które jeszcze nie są zlinkowane. Więc korzystam z komendy emerge i zobaczymy, co się stanie. Odpalam scan Volta, zaczynam od zbierania wszystkich notatek z każdego źródła. Hop, widzimy, że jest zbierane dosłownie wszystko, co mam. Mam listę plików.

**22:23** · Teraz czytam wszystko równolegle. Zacznę od najważniejszych źródeł. Więc niech to się dzieje w tle i zaraz pokażę ci raport, który otrzymam.

**22:31** · I w międzyczasie, gdy to się robi, odpalam sobie kolejny terminal. Hop, znowu odpalam cloda i pokażę ci inną komendę. Tym razem będzie to komenda ask i Ask pozwala zadać dowolne pytanie do całego Volta. Więc mamy komendę ask. Co wiemy o clot codzie? Teraz clot przeszuka notatki i odpowie cytatami ze źródeł. Hop. Widzimy, że przeszukuje wszystko. Co Volt wie o Cloud Codzie? Volt jest nasycony clot codem. Pojawia się w 42 plikach. To nie jest jeden z tematów.

**23:02** · To rdzeń całej bazy wiedzy. Masz pełny trce ewolucji od narzędzia do filozofii w pi tygodni.

**23:08** · Skrystalizowana wiedza. Hop. Widzimy koncept.

**23:13** · Widzimy jakieś moje przekminki. Vol zbiera techniczne nowości o ekosystemie clot coda. Pipeline contentu. Sześć pomysłów na filmy. Livey, wszystko o clot codezie.

**23:22** · projekty, wzorce i napięcia. Mam jeszcze komendę/depen, która pogłębia i kilka innych komend. W ogóle jeżeli chciałbyś inny odcinek o tym, gdzie pokazuje jak to działa, jak z tego korzystam, to zostaw proszę komentarz # obsidian.

**23:37** · Widzimy, zapisano AI zone. Przejdźmy sobie tutaj mamy tutaj unswares, co wiem o cloud codzie i mamy tutaj całą przekminkę. Mamy wzorce i napięcia, źródła z volta. Hop. Powiązane pytanie.

**23:53** · Jak wygląda architektura MCP? Jakie serwery najlepiej integrują się z Code codem? Jaki jest realny rol używania Cloud Code w produkcji kontentu? Jak wygląda konkurencja i gdzie cloud code wygrywa? I to co ciekawe, Cloud się pyta co dalej? Czy chcę pogłębić temat? Mogę wybrać ten jeden z zaproponowanych, zbadać luki, zrobi research albo nic.

**24:11** · Idę dalej. Dajmy nic. Tu ciągle trwa ta komenda emerge. Widzimy, że trudne się wylosowało. Mam teraz pełny obraz. Pora na analizę topologiczną. muszę policzyć backlinki. Jak widzę ile tego jest, no to sam bym się w tym zakopał. To jest właśnie moc tego narzędzia, połączenia tych narzędzi, ponieważ ludzie robili takie rzeczy wcześniej bez połączenia z Cloud Codem. Wymagało to niesamowitej wiedzy i na pewno zaangażowania i czasu, żeby się tego nauczyć. Teraz jest to o wiele prostsze.

**24:37** · Ja też nie jestem jakimś ekspertem, bo się dopiero uczę, raczkuję, pokazuję ci to, czego się nauczyłem, żebyś mógł się ewentualnie jakoś zainspirować, bo uważam, że jest to fajne rozwiązanie. Ale dobra, zaraz wracam do ciebie z gotowym raportem.

**24:52** · Zobaczymy, co tu otrzymamy. W tym momencie mamy taki raport. On jeszcze będzie przeredagowany przez Jemina CLI, ale mamy emerge, ukryte wzorce. Możemy sobie zobaczyć drugi raport. Poprzedni jest tutaj. Od tamtego czasu volt urół z 20 do 44 przeanalizowanych notatek. Trzy z sześciu wzorców z poprzedniego raportu zostały skrystalizowane w concept notes.

**25:12** · Co nowego? Mamy Volt jako produkt, metan narracja.

**25:17** · Widzowie jako współtwórcy roadmapy mam jakieś interpretacje. Warto się zastanowić. Potencjał. Delegowanie przyspiesza, potwierdzenie ewolucja jakieś małe rzeczy. Content pipeline gęstnieje, ale brak priorytyzacji.

**25:32** · Gdzie konsumuje bez tworzenia, gdzie tworzy bez konsumowania? Napięcia i sprzeczności. Topologia grafu.

**25:39** · Hop. Widzimy co się z czym łączy.

**25:42** · Widzimy rekomendacje, moglibyśmy to pogłębić, ale no nie będziemy teraz się tym zajmować. Mówię, chciałem ci pokazać jak ja do tego podchodzę. Na początku obiecałem ci pipeline z telefonem.

**25:53** · Widzisz, mówisz do telefonu, Whisper Flow transkrybuje, skrypt eksportuje moje notatki prosto do Obsydiana. Brin Swep krystalizuje wiedzę. Zero ręcznej roboty po drodze. Kluczowe wnioski dla ciebie. Obsidian plus Clot Code to lokalna baza wiedzy. Twoje pliki, twój dysk, pełna kontrola. Nie musisz mieć 400 000 słów czy tam znaków w Volcie.

**26:15** · Zacznij od dwóch pluginów, które ci pokazałem, jednego skilla i jednego Clot MD. Koniecznie napisz mi w komentarzu, jak ty ogarniasz swoją wiedzę i czy w ogóle to robisz. Może korzystałeś do tej pory z obsidiana, ale w tradycyjnej formie. Może korzystasz z Notion, a może z czegoś zupełnie innego. Podziel się w komentarzu. Przypominam, że wszystkie najważniejsze linki znajdziesz w opisie.

**26:35** · A jeśli ten materiał był dla ciebie wartościowy, to będzie mi miło, jeśli zostawisz łapkę w górę, bo to nic cię nie kosztuje, a w ten sposób wspierasz mój kanał. Moje filmy mogą docierać do większej ilości osób, a ja mam większą motywację do ich tworzenia. Jeśli z kolei jesteś nowy na tym kanale, to zachęcam cię do zostawienia suba, bo w ten sposób nie przegapisz żadnych nowych materiałów o praktycznym wykorzystaniu AI w codziennej życiu czy pracy. Ja ci bardzo dziękuję za uwagę. Do zobaczenia w kolejnym odcinku. Cześć.
