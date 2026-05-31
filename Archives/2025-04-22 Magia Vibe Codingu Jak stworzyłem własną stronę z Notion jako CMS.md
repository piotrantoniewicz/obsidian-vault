---
type: "Web"
authors: "[[Przemek Jurgiel-Zyla]]"
url: "https://www.linkedin.com/pulse/magia-vibe-codingu-jak-stworzy%C5%82em-w%C5%82asn%C4%85-stron%C4%99-z-cms-jurgiel-zyla-tuehf/"
published: 2025-04-22
created: 2026-05-31
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "automatyzacja"
---


*"Vibe coding to nie tylko pisanie kodu - to tworzenie czegoś fajnego przy minimalnym wysiłku, z wykorzystaniem nowoczesnych narzędzi i własnej inwencji."*

### Początki mojej przygody z Notion jako CMS

Kilka dni temu zderzyłem się z dość trywialnym problemem. Potrzebowałem stworzyć stronę internetową, która będzie dostarczać treści dla uczestników warsztatów pod prostymi do zapamiętania adresami www oraz która będzie prosta w zarządzaniu, ponieważ treści się tworzą i na pewno będą wielokrotnie zmieniane i uzupełniane. Z dodatkowych wymagań: tanio, estetycznie, najlepiej pod własną domeną www. Teoretycznie proste rozwiązanie - postawić system wordpress i gotowe. Ale wydało mi się to lekko jednak strzelaniem z armaty do muchy. Wybór padł więc na Notion (można współdzielić projekt - nawet w wersji bezpłatnej), ale i tutaj pojawił się inny problem: adres URL wyglądał jak losowo wygenerowany ciąg znaków, a ja jednak chciałem profesjonalnej, własnej domeny. Są też rozwiązania płatne, które pozwalają użyć Notion jako hostingu do własnej strony, jednak w większości przypadków kosztują $15-20/msc. Sporo (a miało być tanio).

**\>> pamiętaj, że warto mnie obserwować -> codziennie piszę o (podstawach)AI, VC, a od kilku dni również o bardzo praktycznych sposobach na wykorzystanie AI w codziennych zadaniach <<**

"Musi istnieć inny sposób, żeby połączyć elastyczność Notion z profesjonalizmem własnej strony internetowej" - pomyślałem, i tak zaczęła się moja przygoda.

Dziś chcę podzielić się z Tobą historią, jak stworzyłem własną stronę internetową korzystającą z Notion jako systemu zarządzania treścią (CMS). Nie jest to poradnik typu "krok po kroku", ale opowieść o procesie, wyzwaniach i rozwiązaniach, które spotkałem na swojej drodze.

Ale od początku…

### Czym właściwie jest to "vibe coding"?

Zanim wejdziemy głębiej, pozwól że wyjaśnię pojęcie "vibe coding". To podejście do programowania, które przenosi ciężar z samego kodu na doświadczenie i końcowy efekt. Zamiast spędzać godziny na pisaniu złożonych funkcji, koncentrujesz się na szybkim osiągnięciu celu, często z pomocą narzędzi AI i gotowych komponentów. Dla doświadczonych programistów to radykalne przyspieszenie pracy, zaś dla mniej doświadczonych (tak się pozwolę nazwać), to w ogóle możliwość pisania własnego kodu (z bardzo dużą asystą AI).

W przypadku niniejszego projektu, vibe coding oznaczało:

- Wykorzystanie istniejącej platformy (Notion) do zarządzania treścią
- Użycie AI (Claude) do generowania kodu
- Skupienie się na efekcie końcowym, a nie na idealnej implementacji
- Szybkie prototypowanie i iteracyjne ulepszanie

### Dlaczego Notion jako CMS? Moja motywacja

Uwielbiam Notion. Intuicyjny interfejs, elastyczność w organizowaniu treści, możliwość współpracy z innymi - wszystkie te cechy sprawiły, że stał się moim cyfrowym mózgiem (obok Obsidian - ale to opowieść na inny wpis). Myśl o prowadzeniu strony internetowej w tradycyjnym CMS, takim jak WordPress, gdzie musiałbym poświęcić dużo czasu na konfigurację, wydawała mi się niepotrzebną komplikacją oraz niepotrzebnym obciążeniem mojego małego konta hostingowego.

Jednocześnie chciałem mieć pełną kontrolę nad swoją stroną - bez ograniczeń, opłat miesięcznych czy uzależnienia od zewnętrznej platformy.

Tak dotarłem do momentu, w którym stwierdziłem, że wykorzystam jedno ze środowisk programistycznych ([cursor.sh](http://cursor.sh/)) i spróbuję stworzyć swój system od zera. Zawsze, gdyby się nie udało, miałem możliwość powrotu do pomysłu z wordpressem. Dodam, że wspomniane środowowisko (IDE) tylko pomogło/przyspieszyło proces, ale równie dobrze można to zrobić za pomocą chatu Anthropic Claude czy OpenAI.

### Planowanie z wizją: przygotowanie do projektu

Każda dobra przygoda zaczyna się od mapy. W moim przypadku była to wizja tego, jak powinna działać moja strona. Wyobraziłem sobie prosty, elegancki blog z własnym adresem URL, gdzie cała treść byłaby zarządzana przez Notion.

### Wybór odpowiedniego hostingu (dość prosty)

Miałem już konto na zenbox, gdzie hostowałem inne projekty, więc było to naturalne miejsce do rozpoczęcia. Plusem (ale i ograniczeniem) była obsługa PHP. (tutaj mały disclaimer: jeśli w którymś miejscu używam zbyt trudnego języka, to wybczaczcie - polecam wrzucić kawałek w któregoś z czatów i spytać o wyjaśnienie).

### Organizacja treści w Notion

Następnie zacząłem planować, jak zorganizować treść w Notion, aby ułatwić jej przeniesienie na stronę internetową. Stworzyłem bazę danych z kolumnami:

- Obsługa integracji z Notion (API?)
- Tytuł (dla nagłówków stron)
- Treść (dla właściwej zawartości)
- Prosty URL - automatyczne odzwierciedlenie z Notion (tytuł: “1” = url/1)
- Obsługa cover photo
- Obsługa wyświetlania tabel

To było jak projektowanie nowego domu (a właściwie namiotu, bo to jednak dość proste zadanie) - ekscytujące, choć trochę (w pierwszym momencie) przytłaczające. Ale z każdym wpisem w moim projekcie widziałem, jak moja wizja nabiera kształtów.

### Bezpieczeństwo przede wszystkim: ochrona danych API

Gdy przyszedł czas na implementację, pierwszą rzeczą, która zaniepokoiła mnie, było bezpieczeństwo. Notion API wymaga klucza API, a jego wyciek mógłby dać komuś dostęp do mojej bazy danych.

Pamiętam, jak czytałem artykuł o bezpieczeństwie aplikacji webowych i natrafiłem na ten fragment: "Jedną z najlepszych praktyk jest używanie plików środowiskowych (.env) do przechowywania wrażliwych danych, takich jak klucze API."

To miało sens. Zamiast umieszczać klucz API bezpośrednio w kodzie, stworzyłem plik.env, który nie byłby przesyłany do repozytorium Git. Dodatkowo, umieściłem ten plik poza katalogiem publicznym i dodałem reguły w.htaccess, aby zabezpieczyć go przed dostępem z zewnątrz.

Potem dowiedziałem się, że pliki.env wciąż mogą być podatne na ataki typu local file include, więc dodatkowe zabezpieczenia, jak użycie zmiennych środowiskowych Apache, mogą być wskazane w bardziej wrażliwych zastosowaniach.

Potem okazało się, że dostęp do zmiennych środowiskowych jest ograniczony, więc klucz trafił do pliku config poza powiązaniem do katalogu root (głównego katalogu użytkownika podpiętego pod domenę).

### Nawiązywanie połączenia: konfiguracja Notion API

Pierwszą rzeczą, którą musiałem zrobić, było uzyskanie klucza API Notion. Proces był zaskakująco prosty:

1. Zalogowałem się na konto Notion
2. Odwiedziłem stronę [developers.notion.com](http://developers.notion.com/)
3. Utworzyłem nową integrację o nazwie "Moja Strona CMS"
4. Przyznałem jej uprawnienia do odczytu treści
5. Skopiowałem wygenerowany klucz API

Potem przyszedł czas na udostępnienie integracji. Otworzyłem stronę w Notion, kliknąłem przycisk "Share" i dodałem moją integrację. To był moment "Eureka!" - moja integracja mogła teraz komunikować się z moją “stroną www”..

### Współpraca z AI: tworzenie skryptu z pomocą Claude

Teraz przyszedł czas na najtrudniejszą część - stworzenie skryptu PHP, który będzie pobierał dane z Notion i wyświetlał je na mojej stronie. Wcześniej napisanie takiego skryptu zajęłoby mi wiele godzin, ale tym razem miałem pomocnika - Claude.

Poprosiłem Claude o pomoc w generowaniu kodu, tłumacząc, czego potrzebuję. To było fascynujące doświadczenie - zadawałem pytania, uściślałem wymagania, a Claude tworzył fragmenty kodu, które łączyłem w całość.

Na przykład, potrzebowałem funkcji do pobierania danych z API Notion. Claude zaproponował klasę klienta API:

// Przykładowy fragment kodu generowanego przez Claude

class NotionClient {

private $apiKey;

private $baseUrl = ' [https://api.notion.com/v1/](https://api.notion.com/v1/) ';

…

Kiedy miałem wątpliwości, jak przekształcić bloki Notion na HTML, Claude zaproponował rozwiązanie do renderowania różnych typów bloków. Stopniowo, kawałek po kawałku, składałem elementy układanki.

Najbardziej satysfakcjonującym momentem było, gdy zrozumiałem, że nie muszę być ekspertem w API Notion - Claude dostarczał mi wystarczająco dużo wskazówek, abym mógł tworzyć działający kod, nawet jeśli nie znałem wszystkich niuansów.

### Ożywianie projektu: implementacja i pierwsze testy

Po około 2h intensywnej pracy miałem gotowy skrypt. Przesłałem pliki na serwer przez SFTP i przyszedł czas na pierwszą próbę.

I zadziałało! Na ekranie pojawiła się moja strona główna, z treścią pobraną bezpośrednio z Notion. To było jak magia - zmieniłem coś w Notion, odświeżyłem stronę i zmiana była widoczna. Czułem się jak dziecko, które właśnie odkryło, jak działa nowa zabawka.

Oczywiście, nie wszystko było idealne od razu. Niektóre elementy formatowania nie wyświetlały się poprawnie, obrazy czasami nie ładowały się, a system routingu miał problemy z niektórymi adresami URL. Ale to była część procesu - iteracyjne ulepszanie, poprawianie błędów, dodawanie funkcji.

### Rozwiązywanie problemów: wyzwania i ich przezwyciężanie

W miarę testowania pojawiały się różne wyzwania. Jednym z większych problemów był sposób renderowania różnych typów bloków z Notion. Notion używa bogatego systemu bloków - paragrafów, nagłówków, list, bloków kodu, obrazów i wielu innych.

Początkowo mój skrypt obsługiwał tylko podstawowe bloki tekstu. Stopniowo dodawałem obsługę kolejnych typów, ucząc się struktury API Notion w trakcie. Claude był nieocenionym pomocnikiem, sugerując rozwiązania dla każdego typu bloku.

Innym wyzwaniem była wydajność. Za każdym razem, gdy ktoś odwiedzał stronę, skrypt wykonywał zapytanie do API Notion, co przy większym ruchu mogło prowadzić do przekroczenia limitów API. Rozwiązaniem było zaimplementowanie prostego systemu buforowania - zapisywanie pobranych danych w pamięci podręcznej i odświeżanie ich co określony czas.

### Radość tworzenia: korzyści z własnego rozwiązania

Po kilku godzinach (ciągle w ten sam weekend) dopracowywania, moja strona działała płynnie i wyglądała profesjonalnie. Mogłem zarządzać całą treścią przez Notion - dodawać nowe artykuły, aktualizować istniejące, zmieniać układ - a wszystko automatycznie synchronizowało się z moją stroną.

Największą korzyścią było uproszczenie mojego workflow. Nie musiałem logować się do panelu administracyjnego strony, konfigurować nowego interfejsu czy martwić o aktualizacje CMS. Wszystko działo się w Notion, którego używałem codziennie do innych celów.

Dodatkowo, miałem pełną kontrolę nad swoją stroną - mogłem dostosować jej wygląd, dodać niestandardowe funkcje, zintegrować z innymi narzędziami. Nie byłem ograniczony funkcjami dostępnymi w gotowych rozwiązaniach.

### Aktualizacje i usprawnienia

Rozwijając projekt dodałem kilka swoich usprawnień. Pobawiłem się trochę stylowaniem (wyglądem) oraz dodałem własne “tagi” <hide>, które pozwalają ukryć część strony Notion (np Notion na końcu strony generuje listę linków, plików, której nie chcę pokazywać na www).

Następnie stworzyłem z tego projekt na github wraz z prostą dokumentacją - polecam spojrzeć: [auditlog/notion-to-own-domain](https://github.com/auditlog/notion-to-own-domain)

### Moje refleksje i wnioski dla początkujących

Patrząc wstecz na cały proces, widzę, jak podejście "vibe coding" zmieniło moje nastawienie do tworzenia stron internetowych (i generalnie programowania). Zamiast koncentrować się na pisaniu idealnego kodu, skupiłem się na osiągnięciu celu - stworzeniu funkcjonalnej, estetycznej strony zarządzanej przez Notion.

Dla początkujących, którzy chcieliby podążyć podobną ścieżką, mam kilka przemyśleń:

1. **Zacznij od jasnej wizji** - wyobraź sobie, jak powinna działać twoja strona, jakie problemy ma rozwiązywać.
2. **Wykorzystaj istniejące narzędzia** - nie próbuj wymyślać koła na nowo. Notion, hosting PHP, narzędzia AI - wszystkie one istnieją, aby ułatwić ci pracę.
3. **Nie bój się eksperymentować** - niektóre rzeczy zadziałają od razu, inne będą wymagały poprawek. To normalny proces tworzenia.
4. **Pamiętaj o bezpieczeństwie** - ochrona danych, zwłaszcza kluczy API, powinna być priorytetem od samego początku.
5. **Doceniaj małe zwycięstwa** - każdy działający fragment kodu, każda poprawnie wyświetlona strona to powód do radości i motywacja do dalszej pracy.

### Podsumowanie: moja podróż z Notion do własnej strony

Stworzenie własnej strony internetowej z Notion jako CMS było fascynującą przygodą. Od pierwszego pomysłu, przez planowanie, implementację, aż do finalnych testów - każdy etap uczył mnie czegoś nowego.

A najlepsze jest to, że dzięki podejściu "vibe coding" cały proces był przyjemny i satysfakcjonujący. Zamiast frustracji związanej z godzinami pisania kodu, doświadczyłem radości tworzenia czegoś użytecznego i estetycznego.

Zachęcam cię, abyś spróbował/-a podobnego podejścia w swoich projektach. Połączenie istniejących narzędzi z odrobiną kreatywności może prowadzić do wspaniałych rezultatów, nawet jeśli nie jesteś ekspertem w programowaniu.

Pamiętaj, że najważniejsze nie jest to, ile kodu napiszesz, ale to, co ten kod umożliwia. W przypadku mojej strony z Notion jako CMS, umożliwił mi on tworzenie i dzielenie się treścią na moich warunkach - i to jest prawdziwa magia vibe codingu.