---
type: Web
authors: '[[ai-leaders]]'
url: >-
  https://aileaders.pl/artykuly/dane-ksef-e-doreczenia-i-koniec-wymowek/?ref=aileaders-pl-newsletter
published: 2026-08-19
created: 2026-08-19
tags:
  - strategia-AI
  - automatyzacja
  - narzędzia-AI
---


![Dane, których nie masz, a właściwie nie wiesz, że masz. KSeF, e-Doręczenia i koniec wymówek](https://aileaders.pl/content/images/size/w2000/2026/08/ai_leaders_q_and_a-2.png)

Dane, których nie masz, a właściwie nie wiesz, że masz. KSeF, e-Doręczenia i koniec wymówek

Na webinarze powiedzieliśmy, że 20% nieudanych wdrożeń AI rozbija się o dane i brak API. W polskich firmach ta wymówka właśnie przestała działać, bo państwo wystawiło Ci ustrukturyzowaną bazę danych i nie zapytało o zdanie. W dzisiejszym newsletterze: co realnie masz w KSeF, jak się do tego dobrać, pięć pułapek i termin 1 października, o którym połowa jednoosobowych działalności zapomniała.

### Zapisz się na drugi nasz webinar: https://aileaders.pl/webinar-ai-leaders-poniedzialek-31-08-2026-19-00-online/ (Od czego zacząć realne wdrożenia AI? Małe kroczki do dużych przyrostów)

Mamy jednocześnie nadzieję, że pokazując w konkrecie zainspirujemy Cię do szukania swoich źródeł danych i sposobów na wdrażanie prostych rozwiązań opartych o AI w twojej organizacji. Uznaliśmy, że KSeF i e-Doręczniea to bardzo wdzięczny temat. Przyjemnego czytania i zapraszamy na [aileaders.pl](https://aileaders.pl/) i zapisanie się na wait listę naszego kursu AI.

Pamiętasz metaforę żarówki z webinaru? Jedna osoba w organizacji świetnie promptuje, reszta stoi. Problem w tym, że żeby przebudować fabrykę, a nie tylko wymienić żarówkę, potrzebujesz danych, a na pytanie „macie API?" najczęstszą odpowiedzią w polskim MŚP było wymowne milczenie.

I tu jest ta ciekawa rzecz, którą przegapiła większość rynku: **od 1 kwietnia 2026 r. każda faktura wystawiona przez Twoją firmę jest ustrukturyzowanym plikiem XML w centralnym systemie państwa.** Nie skanem. Nie PDF-em. Nie „Zeszytem 2 (kopia) FINAL.xlsx". Bazą danych z polami, słownikami i walidacją schematu.

Przez trzy lata rynek narzekał, że KSeF to kolejny obowiązek. Nikt nie zauważył, że przy okazji rozwiązał najczęstszy blocker wdrożeń AI w małych i średnich firmach.

## Trzy daty, które warto mieć w głowie

- **1 lutego 2026** - obowiązek wystawiania faktur w KSeF dla firm, u których sprzedaż brutto przekroczyła w 2024 r. 200 mln zł. Od tego samego dnia **wszyscy** czynni podatnicy VAT muszą faktury z KSeF *odbierać*.
- **1 kwietnia 2026** - obowiązek objął pozostałych przedsiębiorców. Czyli prawdopodobnie Ciebie.
- **1 stycznia 2027** - dołączają najmniejsi (sprzedaż udokumentowana fakturami do 10 tys. zł brutto miesięcznie) i **kończy się okres bez kar**.

To ostatnie wymaga podkreślenia, bo krąży w tej sprawie sporo optymizmu. Rok 2026 to okres przejściowy, w którym nie są nakładane **administracyjne** kary pieniężne za błędy w KSeF. To nie jest abolicja. Odpowiedzialność karnoskarbowa działa normalnie, a kary za błędy w JPK\_VAT (500 zł za każdy) nikt nie zawiesił. Od 1 stycznia 2027 wchodzą sankcje właściwe: do 100% kwoty VAT wykazanego na fakturze wystawionej poza systemem, a przy fakturach bez wykazanego podatku - do 18,7% kwoty brutto.

Innymi słowy: masz jeszcze kilka miesięcy, żeby przećwiczyć proces na koszt państwa.

## Co właściwie siedzi w FA(3), czyli dlaczego PDF i XML to dwa różne światy

Zanim ktoś powie „przecież zawsze mieliśmy faktury" - nie, nie mieliście. Mieliście obrazki faktur, z których dane trzeba było wyciągać OCR-em, a potem sprawdzać, czy OCR nie pomylił 8 z 3.

Schemat FA(3), obowiązujący dla wszystkich faktur ustrukturyzowanych wystawianych od 1 lutego 2026, daje coś zupełnie innego. W elemencie *FaWiersz* (do 1000 pozycji na fakturze) siedzą m.in.:

- nazwa towaru lub usługi, jednostka miary, ilość, cena jednostkowa netto, wartość netto pozycji,
- *Indeks* - Twój własny numer katalogowy pozycji,
- *GTIN, PKWiU, CN, PKOB* - kody klasyfikacyjne,
- *GTU* i *Procedura* - oznaczenia towarów wrażliwych i procedur szczególnych,
- a w *FaWierszCtrl* kontrolne podsumowanie: liczba wierszy i suma wartości netto.

Do tego dochodzą pełne dane kontrahenta z NIP-em, terminy i formy płatności, rabaty, rozliczenie VAT w rozbiciu na stawki (grupy P\_13, P\_14, P\_15) oraz nowość FA(3) - *IPKSeF*, identyfikator konkretnej płatności, który pozwala domknąć pętlę „faktura ↔ przelew".

I najlepsze: **faktury są przechowywane w KSeF przez 10 lat**. Twoje archiwum kosztowe i sprzedażowe stoi na serwerze Ministerstwa Finansów, uporządkowane, w jednym formacie, dla wszystkich Twoich kontrahentów jednocześnie.

Z życia: firmy, które przez lata prosiły dział IT o „raport zakupowy w rozbiciu na pozycje" i słyszały, że to trzy miesiące pracy, mają ten raport od kwietnia. Tylko nikt im nie powiedział.

## Pięć rzeczy, które możesz zrobić z tymi danymi jeszcze w tym kwartale

Zgodnie z tym, co powtarzaliśmy na webinarze: zaczynamy od pytania biznesowego i właściciela procesu, nie od modelu. Dla każdego przypadku podajemy, co mierzysz i czego **nie** robisz.

**1\. Mapa wydatków i koncentracja dostawców.** Pytanie: u ilu dostawców zostawiamy 80% pieniędzy i czy ktoś nam po cichu urósł do roli single point of failure? Dane: faktury zakupowe, NIP sprzedawcy, wartości netto, 12 miesięcy wstecz. KPI: udział top 5 dostawców w kosztach, liczba dostawców z jednym zamówieniem w roku. Czego nie robić: nie zaczynaj od LLM-a. To jest GROUP BY i tabela przestawna w arkuszu kalkulacyjnym.

**2\. Ciche podwyżki cen.** Pytanie: który dostawca podniósł cenę jednostkową tej samej pozycji i o ile? To jest możliwe dopiero teraz, bo dopiero teraz masz Indeks i cenę jednostkową w polu, a nie w akapicie. KPI: liczba pozycji z odchyleniem ceny > X% kwartał do kwartału, wartość odchylenia w złotówkach. To jest zwykle pierwszy use case, który sam się spłaca.

**3\. Prognoza cash flow z terminów płatności.** Pytanie: jak wygląda nasza pozycja gotówkowa w horyzoncie 30/60/90 dni przy obecnej strukturze należności i zobowiązań? Dane: terminy płatności z faktur sprzedażowych i zakupowych, historia opóźnień per kontrahent. KPI: DSO, odsetek faktur płaconych po terminie, prognoza vs. wykonanie. Tu klasyczny model statystyczny bije generatywną AI na głowę.

**4\. Duplikaty, anomalie i faktury-widmo.** Pytanie: czy płacimy dwa razy za to samo i czy w kosztach nie ma pozycji, których nikt nie zamawiał? KPI: liczba wykrytych duplikatów, wartość zatrzymanych płatności. Uwaga: detekcja anomalii to klasyczny machine learning sprzed 15 lat, tani i przewidywalny. Nie potrzebujesz do tego frontier modelu.

**5\. Koncentracja przychodów i struktura oferty.** Pytanie: które pozycje z naszego katalogu faktycznie generują marżę, a które tylko generują faktury? Dane: FaWiersz z faktur sprzedażowych. KPI: udział top 10 pozycji w przychodzie, rozkład wartości koszyka, rotacja indeksów.

Zauważ, że w żadnym z tych pięciu przypadków generatywna AI nie jest głównym bohaterem. To jest dokładnie ta teza, którą Inga podnosiła na webinarze: AI to nie jest wyłącznie GenAI, a największe zwroty siedzą w optymalizacji cen, zakupów i dostaw. GenAI wchodzi dopiero w kroku następnym - o tym za chwilę.

## Jak się do tych danych dobrać, nie zatrudniając software house'u?

Ministerstwo Finansów udostępniło API KSeF 2.0 jako REST z dokumentacją w standardzie OpenAPI, bibliotekami SDK dla Javy i.NET oraz publicznym repozytorium przykładów. To jest - i piszę to z pełną świadomością ironii - **lepiej udokumentowane API niż to, które oferuje większość polskich systemów ERP używanych w MŚP.**

Ścieżka minimalna:

**Krok 1 - uprawnienia.** Bez zgłoszenia ZAW-FA i nadania uprawnień nikt w firmie nie wystawi ani nie pobierze faktury w Twoim imieniu. Do odczytu potrzebujesz uprawnienia InvoiceRead. To najczęstszy punkt, w którym wdrożenie stoi tydzień, bo „pani Jola miała to zrobić".

**Krok 2 - uwierzytelnienie.** Pobierasz challenge, podpisujesz żądanie certyfikatem lub tokenem, dostajesz token dostępowy. Wszystkie kolejne operacje idą z nim.

**Krok 3 - metadane, potem treść.** Odpytujesz o metadane z filtrami: zakres dat wystawienia, NIP kontrahenta, typ (sprzedaż jako sprzedawca / zakup jako nabywca), status przetwarzania. Dopiero potem pobierasz XML konkretnych faktur albo zamawiasz eksport wsadowy.

**Krok 4 - limity.** API ma rate limity i przy pierwszym masowym zaciągu historii łatwo się o nie obić. Pobieranie robi się wsadowo, z paginacją i punktem kontynuacji, żeby dało się wznowić po przerwaniu. Zaplanuj to jako proces nocny, nie jako kliknięcie w przycisk.

**Krok 5 - parsowanie i model danych.** XML → tabela pozycji + tabela nagłówków. To jest może 200 linii kodu. Realnie: dzień pracy jednej osoby, która wie, co robi, plus tydzień na uporządkowanie tego, co wyjdzie.

Jeśli nie chcesz dotykać API, sprawdź najpierw, co potrafi Twój obecny system - większość dostawców oprogramowania księgowego dorobiła w 2026 r. moduły pobierania faktur zakupowych i eksport do XML. Pytanie do dostawcy brzmi konkretnie: *„czy mogę wyeksportować pozycje faktur, a nie tylko nagłówki?"*. Jeśli odpowiedź brzmi „tylko nagłówki", masz kwoty i nie masz analityki.

I jeszcze jedna rzecz, którą dorzucimy z perspektywy prawnej - dostęp do KSeF to dostęp uprzywilejowany do bardzo konkretnej mapy Twojego biznesu.

Jeżeli dajesz aplikacji, integratorowi, biuru rachunkowemu albo agentowi dostęp do odczytu faktur, potencjalnie dajesz mu jednocześnie informację o tym, komu płacisz, ile, za co, jak często, od kogo zarabiasz i na jakich warunkach.

Dlatego przy integracji nadal warto pytać: kto dokładnie ma dostęp, do czego, gdzie przechowujemy certyfikaty i sekrety, jak odbieramy dostęp po zmianie pracownika albo dostawcy i czy później potrafimy ustalić, kto faktycznie pobierał dane.

## Pięć pułapek, na których się potkniesz

**PDF przestał być fakturą.** Od momentu objęcia obowiązkiem plik PDF jest wizualizacją dokumentu, nie dokumentem. Jeśli ktoś w firmie nadal wysyła PDF-y „bo klient prosił", nie robicie e-fakturowania - robicie dwa obiegi naraz.

**Brak kar to nie brak obowiązku.** Powtarzam, bo to najczęstsze nieporozumienie tego roku. Zawieszone są konkretne administracyjne kary pieniężne, nie cały system odpowiedzialności.

**Hybryda mści się w JPK.** Jeśli część faktur ma numer KSeF, a część nie, Twoja ewidencja staje się dwutorowa, a ryzyko błędu w JPK\_VAT rośnie skokowo. To akurat kara, która nie została zawieszona.

**Załącznik w FA(3) to nie jest miejsce na PDF.** Element załącznika służy danym ustrukturyzowanym. Pliki binarne - zdjęcia, skany, specyfikacje w XLS - nadal wymieniacie poza systemem. Jeśli Twój proces zakłada, że „wrzucimy wszystko do KSeF", zaplanuj go jeszcze raz.

**XML ≠ dobre dane.** I to jest pułapka najbardziej bolesna dla wdrożeń AI. Masz strukturę, ale nadal masz dostawcę, który 40% pozycji opisuje jako „usługa transportowa", i drugiego, który każdą pozycję nazywa inaczej. Ustrukturyzowany bałagan to wciąż bałagan - tyle że łatwiej go teraz zmierzyć. I dopiero **tutaj** LLM zaczyna zarabiać na siebie: normalizacja nazw pozycji, mapowanie na wspólny katalog, kategoryzacja kosztów. Nie do liczenia. Do porządkowania.

## Termin, o którym połowa rynku zapomniała: 1 października 2026

Drugi strumień danych, który właśnie wpada do polskich firm, to e-Doręczenia - elektroniczny odpowiednik listu poleconego za potwierdzeniem odbioru, o tej samej mocy prawnej.

Harmonogram, w skrócie:

- podmioty z KRS zarejestrowane przed 1 stycznia 2025 - obowiązek **od 1 kwietnia 2025** (czyli już),
- firmy rejestrowane w CEIDG i KRS od 1 stycznia 2025 - adres zakładany przy rejestracji,
- **jednoosobowe działalności wpisane do CEIDG przed 1 stycznia 2025 - do 1 października 2026.**

Ten ostatni termin to za chwilę. I jest przy nim haczyk, który zaskakuje ludzi: jeśli między 1 lipca 2025 a 30 września 2026 składasz **jakikolwiek** wniosek o zmianę wpisu w CEIDG - zmiana adresu, aktualizacja danych kontaktowych, dorzucenie kodu PKD, zawieszenie albo wznowienie działalności - musisz przy tej okazji założyć adres do e-Doręczeń albo wskazać już posiadany. Zawieszenie działalności obowiązku nie zdejmuje.

I teraz część, która dotyczy nie prawnika, tylko lidera AI: **skoro to ma skutek listu poleconego, ktoś w firmie musi tę skrzynkę faktycznie czytać.** Nie „zaglądać czasem". Nie „pani Jola sprawdzi, jak wróci z urlopu". Pytania, które warto sobie zadać dzisiaj:

- kto imiennie odpowiada za monitorowanie skrzynki i kto go zastępuje?
- które kategorie pism wymagają reakcji w ciągu 24 godzin, a które trafiają do zwykłego obiegu?
- czy powiadomienia trafiają na adres, który ktoś sprawdza codziennie?
- czy pisma z e-Doręczeń wpadają do tego samego rejestru korespondencji, co reszta, czy tworzą osobną wysepkę?

Bo tu jest ta sama pułapka, o której mówiliśmy przy OCR-ze: możesz mieć doskonale zautomatyzowane wczytywanie dokumentu, a i tak przegrać, jeśli na końcu procesu siedzi człowiek, który o swojej roli nie wie.

Oczywiście ktoś za chwilę wpadnie na pomysł: „to niech agent AI czyta e-Doręczenia, streszcza pisma, rozpoznaje sprawę i wrzuca terminy do kalendarza”. To jest całkiem sensowny use case. Pod jednym warunkiem: nie pomylimy automatyzacji pracy **z** automatyzacją odpowiedzialności**.** Pismo źródłowe musi pozostać dostępne, człowiek powinien móc sprawdzić, skąd system wyciągnął termin albo kwalifikację sprawy, a organizacja musi wiedzieć, w którym momencie AI tylko proponuje, a w którym jego wynik zaczyna wywoływać realne działanie.

## Zanim wrzucisz pierwszy XML do modelu - trzy pytania

Dane z KSeF wyglądają niewinnie. To wciąż faktury. Ale to również:

- **dane osobowe** - w Polsce ogromna część kontrahentów to jednoosobowe działalności, więc NIP, adres i nazwa firmy to jednocześnie dane osoby fizycznej,
- **tajemnica przedsiębiorstwa** - Twoja i Twoich kontrahentów, łącznie z cenami zakupu, marżami i strukturą dostawców,
- **komplet informacji o Twoim biznesie** - czyli dokładnie to, czego nie chcesz przypadkiem oddać do trenowania cudzego modelu.

Zanim pierwsza paczka XML pojedzie do zewnętrznego API, odpowiedz sobie na trzy pytania:

1. **Dokąd to leci?** Który dostawca, który region, czy dane służą do treningu, jaka jest retencja, kto jest podprocesorem. Konfiguracja bez retencji i region UE to ustawienia, nie deklaracje marketingowe - sprawdź je w umowie.
2. **Czy musi lecieć w całości?** W większości analiz cenowych nie potrzebujesz nazw kontrahentów. Pseudonimizacja przed wysyłką rozwiązuje 80% problemu za 20% wysiłku.
3. **Kto to zatwierdził?** Jeśli odpowiedź brzmi „nikt, po prostu wrzuciłem do czata, żeby zobaczyć, czy to w ogóle zadziała" - masz właśnie klasyczny przypadek shadow AI, tyle że na danych finansowych całej firmy.

To nie jest argument za nierobieniem niczego. To argument za tym, żeby polityka korzystania z AI była - jak mówiliśmy na webinarze - warstwą decyzyjną, a nie dokumentem, który leży w segregatorze u prawników. Trzy zdania, które ludzie zapamiętają, biją trzydzieści stron, których nikt nie przeczyta.

## Checklista na 30 dni

1. Sprawdź, czy masz nadane uprawnienia do odczytu faktur w KSeF (i czy nie ma ich wyłącznie jedna osoba na urlopie).
2. Wyeksportuj X miesięcy faktur zakupowych i sprzedażowych do XML. Nie analizuj, najpierw po prostu miej.
3. Przykładowo policz dwie liczby: udział top 5 dostawców w kosztach i liczbę unikalnych nazw pozycji na fakturach zakupowych. Druga powie Ci, ile pracy czeka Cię przy normalizacji.
4. Wybierz **jeden** use case z listy pięciu powyżej, przypisz mu właściciela biznesowego i jeden KPI. Jeden, nie pięć.
5. Zweryfikuj status e-Doręczeń: czy adres jest założony, aktywowany i czy ktoś imiennie odpowiada za skrzynkę.
6. Zapytaj dostawcę swojego systemu księgowego wprost: „czy eksportujecie pozycje faktur, czy tylko nagłówki?".
7. Pamiętaj - to, że masz dane lub technicznie możesz je pobrać, nie oznacza, że możesz z nimi zrobić co chcesz.
