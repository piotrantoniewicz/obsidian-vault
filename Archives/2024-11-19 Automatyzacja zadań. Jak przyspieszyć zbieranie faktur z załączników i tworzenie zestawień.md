---
type: Web
authors: '[[Marzena Kacprowicz]]'
url: >-
  https://sektor3-0.pl/blog/automatyzacja-zadan-jak-przyspieszyc-zbieranie-faktur/?utm_source=newsletter&utm_medium=email&utm_term=2026-03-24&utm_campaign=+Automatyzacja+w+NGO+krok+po+kroku
published: 2024-11-19T00:00:00.000Z
created: 2026-03-24T00:00:00.000Z
tags:
  - automatyzacja
  - narzędzia-AI
  - organizacje-społeczne
---


Ułatwienia dostępu

- Skalowanie treści 100%
- Czcionka 100%
- Wysokość linii 100%
- Odstęp liter 100%

![Automatyzacja zadań. Jak przyspieszyć zbieranie faktur z załączników i tworzenie zestawienia?](https://sektor3-0.pl/wp-content/uploads/elementor/thumbs/blog-qx8e9rnl3yyuvhlwjeaoltci413pp4oi18jg5bjtrq.jpg "blog")

Wyobraź sobie, że prowadzisz projekt. W ciągu miesiąca do twojej skrzynki przychodzi wiele e-maili z fakturami. Każdą wiadomość musisz otworzyć, przeczytać, pobrać faktury z załączników, zapisać je na dysku, a potem stworzyć tabelę z zestawieniem wszystkich faktur i przekazać ją do księgowości. Brzmi jak mnóstwo pracy, prawda? Na szczęście są to zadania i proces, które da się automatyzować! Dziś pokażę ci, na czym polega automatyzacja i w jaki sposób z wykorzystaniem bezpłatnych narzędzi możesz zautomatyzować zbieranie faktur lub innych dokumentów i robienie zestawień.

**Wyobraź sobie, że prowadzisz projekt. W ciągu miesiąca do twojej skrzynki przychodzi wiele e-maili z fakturami. Każdą wiadomość musisz otworzyć, przeczytać, pobrać faktury z załączników, zapisać je na dysku, a potem stworzyć tabelę z zestawieniem wszystkich faktur i przekazać ją do księgowości. Brzmi jak mnóstwo pracy, prawda? Na szczęście są to zadania i proces, które da się automatyzować! Dziś pokażę ci, na czym polega automatyzacja i w jaki sposób z wykorzystaniem bezpłatnych narzędzi możesz zautomatyzować zbieranie faktur lub innych dokumentów i robienie zestawień.**

Uwaga! Tę automatyzację możesz wykorzystać również do innych zadań, nie tylko do zbierania faktur! Przykłady takich zadań znajdziesz na końcu artykułu, w części „Inne pomysły na wykorzystanie tej automatyzacji”.

## Automatyzacja: co to takiego?

Automatyzacja to proces, który pozwala oszczędzać czas: zamiast wykonywać jakieś zadania manualnie, wykorzystujemy specjalne oprogramowanie, które (częściowo lub całkowicie) wykonuje za nas jakąś sekwencję zadań. Innymi słowy: określamy, co ma zostać wykonane i kiedy, a potem cieszymy się z efektu i uwolnionego czasu.

## Automatyzacja procesu zbierania faktur krok po kroku

W dzisiejszym artykule pokażę ci, w jaki sposób krok po kroku zbudować automatyzację, która zrealizuje następujący proces:

1. Do skrzynki Gmail przychodzi e-mail z fakturą w załączniku.
2. Oznaczasz e-mail etykietą „faktura”.
3. Etykieta uruchamia automatyzację, która:
	1. Pobiera załącznik z fakturą i zapisuje go w wybranym folderze na Dysku Google.
		2. W zestawieniu faktur zlokalizowanym na Dysku Google tworzony jest rekord dla tej faktury. W rekordzie w kolumnach zapisują się najważniejsze informacje takie jak: nazwa pliku, data wpływu, nadawca, link do faktury na Dysku.
4. Potem tylko przekazujesz osobie z księgowości link do arkusza z zestawieniem faktur i *voila.*

Wystarczy jedno kliknięcie, aby faktura trafiła z maila na dysk i do zestawienia faktur. Zyskasz dzięki temu czas, który będziesz mógł/mogła wykorzystać na bardziej kreatywne zadania… albo na odpoczynek!

**Do zbudowania automatyzacji wykorzystamy cztery narzędzia:**

- **[Make](https://make.com/)** – narzędzie, w którym zaprojektujemy automatyzację,
- **Gmail** – skrzynka e-mailowa,
- **Dysk Google** – dysk w chmurze, na którym będą zapisywane faktury.
- **Google Sheets** – arkusz kalkulacyjny, w którym zostanie stworzone zestawienie faktur.

### Krok 1: Stwórz folder, w którym będą przechowywane faktury

Zaloguj się na swój Dysk Google i stwórz w nim folder, w którym chcesz gromadzić faktury. Na przykład:

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201915%20583'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/01_Automatyzacja_FV_dysk_google.png)

### Krok 2: Stwórz arkusz kalkulacyjny, w którym będzie przechowywane zestawienie faktur

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201913%20591'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/02_Automatyzacja_FV_dysk_google_Zestawienie.png)Załóżmy, że chcemy w nim zbierać następujące informacje:

1. Data wpływu (czyli dzień otrzymania maila z fakturą).
2. Nadawca.
3. E-mail nadawcy.
4. Nazwa pliku z fakturą.
5. Link do faktury (aby umożliwić pobranie faktury z Dysku Google).

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201204%20456'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/03_Automatyzacja_FV_dysk_google_Zestawienie_zawartosc.png)

### Krok 3: Skonfiguruj automatyzację w serwisie Make

Zaloguj się na swoje konto w [Make](https://www.make.com/en). Do przygotowania automatyzacji wykorzystamy gotowy szablon. Aby go znaleźć, z menu po lewej stronie wybierz zakładkę „ **Templates** ”, a następnie w okienku wyszukiwania (znajdującym się w prawym górnym rogu ekranu) wpisz „ **Save Gmail emails and attachments to Google Sheets and Google Drive** ”.

Kliknij kartę znalezionego szablonu:

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201734%20900'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/SCR-20241118-jrod.png)Z menu po lewej stronie wybierz opcję „ **Create new scenario from template** ”. Otworzy się strona, na której będziemy mogli rozpocząć konfigurację automatyzacji. Zobaczysz cztery ikonki, które obrazują cztery kroki naszej automatyzacji:

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201913%20859'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/05_Make-4ikony.png)

1. Pierwszy krok to skrzynka Gmail: Make sprawdza, czy w skrzynce pojawiły się jakieś wiadomości oznaczone etykietą „faktura”.
2. Drugi krok to ponownie skrzynka Gmail: w ramach tego kroku Make pobierze dane załączników.
3. Trzeci krok odpowiada za zapisanie pobranych załączników na Dysku Google.
4. A czwarty krok – za uzupełnienie informacji o załączniku w zestawieniu w arkuszu Google Sheets.

Pozostaje nam teraz skonfigurowanie poszczególnych kroków. Na początku zmień nazwę automatyzacji (możesz to zrobić w lewym górnym rogu), a następnie kliknij pierwszą ikonkę.

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201782%20931'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/SCR-20241118-jxym.png)W oknie konfiguracji uzupełnij:

1. **Connection**: połączenie z twoją skrzynką Gmail. Jeśli korzystasz z Make po raz pierwszy, skonfiguruj połączenie ze swoim kontem Google za pomocą tej instrukcji: [Instrukcja konfiguracji połączenia między Make i kontem Google](https://sektor3-0.pl/wp-content/uploads/2024/11/Instrukcja_konfiguracji_polaczenia_miedzy_Make_i_kontem_Google.pdf) (lub skorzystaj [z instrukcji w języku angielskim](https://www.make.com/en/help/connections/connecting-to-google-services-using-a-custom-oauth-client)).
2. **Folder**: wybierz nazwę folderu z twojej skrzynki Gmail, w której Make będzie szukał e-maili oznaczonych etykietą „faktura”.
3. **Filter type**: wybierz „Gmail filter”.
4. **Query**: wpisz instrukcję, której Make będzie używał do odszukania odpowiednich e-maili. W naszym przypadku będzie to: *has:attachment label:faktura*, co oznacza:
	1. has:attachment – wiadomości, które posiadają załącznik,
		2. label:faktura – wiadomości, które są oznaczone etykietą „faktura”.
5. **Mark email message(s) as read when fetched**: decyzja, czy wiadomość powinna zostać oznaczona jako „odczytana”, kiedy zostanie pobrana przez Make.
6. **Maximum number of results**: maksymalna liczba wiadomości, które zostaną jednorazowo pobrane.

Kliknij „OK”, aby zapisać.

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201912%20946'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/06_Automatyzacja_FV_Make_01_Gmail.png)W drugim kroku niczego nie musimy konfigurować:

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201915%20950'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/07_Automatyzacja_FV_Make_02_Gmail.png)W trzecim kroku wybieramy folder, w którym Make ma zapisywać pobrane załączniki:

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20579'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/Screenshot-2024-11-18-at-10.57.27.png)W ostatnim kroku skonfigurujemy zapisywanie danych o załącznikach w zestawieniu. Zobacz jak to zrobić na poniższym filmie.

Odtwarzacz video  <video width="800" height="433" src="https://sektor3-0.pl/wp-content/uploads/2024/11/09_Make-Google_Sheet.mp4?_=1"><source type="video/mp4" src="https://sektor3-0.pl/wp-content/uploads/2024/11/09_Make-Google_Sheet.mp4?_=1"> <a href="https://sektor3-0.pl/wp-content/uploads/2024/11/09_Make-Google_Sheet.mp4">https://sektor3-0.pl/wp-content/uploads/2024/11/09_Make-Google_Sheet.mp4</a></video>

00:00

00:51

Prawidłowa konfiguracja powinna wyglądać następująco:

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201907%20948'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/10_Automatyzacja_FV_Make_04_GoogleSheet-1.png)

I gotowe!

### Krok 4: Testowanie

Teraz możemy przetestować działanie automatyzacji.

Odtwarzacz video  <video width="800" height="433" src="https://sektor3-0.pl/wp-content/uploads/2024/11/11_Make-Testowanie.mp4?_=2"><source type="video/mp4" src="https://sektor3-0.pl/wp-content/uploads/2024/11/11_Make-Testowanie.mp4?_=2"> <a href="https://sektor3-0.pl/wp-content/uploads/2024/11/11_Make-Testowanie.mp4">https://sektor3-0.pl/wp-content/uploads/2024/11/11_Make-Testowanie.mp4</a></video>

00:00

00:28

1. Na początku folder „ **\_\_FAKTURY”** jest pusty.
2. Tabela w pliku „ **Projekt\_XYZ\_Zestawienie\_faktur** ” również jest pusta.
3. Na moją skrzynkę e-mailową przyszła wiadomość.
4. Oznaczam ją etykietą „faktura”.
5. W Make klikam w przycisk „ **Run Once** ”, znajdujący się w lewej dolnej części ekranu.
6. Kiedy proces w Make się zakończy, sprawdzam, czy plik z fakturą został zapisany na Dysku Google.
7. Sprawdzam, czy dane załącznika zapisały się w zestawieniu.

Automatyzacja działa!

### Krok 5: Ustawienie częstotliwości automatyzacji

Pozostaje tylko ustawić częstotliwość, z jaką automatyzacja ma się uruchamiać:

 [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201035%20678'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/Screenshot-2024-11-18-at-11.03.52.png)*Uwaga! Nie ustawiaj zbyt dużej częstotliwości, jeśli chcesz korzystać z bezpłatnego planu Make.*

Jednostką rozliczeniową w Make są tzw. operacje (ang. *operations*) – czyli działania, które Make wykonuje, żeby zrealizować daną automatyzację. Automatyzacja opisana w tym artykule wykorzystuje:

- 1 operację na sprawdzenie, czy w skrzynce mailowej pojawiły się maile oznaczone etykietą “faktura”,
- 1 operację na pobranie 1 załącznika,
- 1 operację na zapisane 1 załącznika,
- 1 operację na dodanie 1 rekordu do arkusza kalkulacyjnego.

Przykładowo:

- Jeśli po uruchomieniu automatyzacji zostanie znaleziony 1 mail z 1 załącznikiem, automatyzacja „zużyje” **4** operacje. Jeśli automatyzacja będzie uruchamiana 1 raz dziennie codziennie, w ciągu miesiąca automatyzacja „zużyje” ok. **120** operacji.
- Jeśli zostaną znalezione 2 maile, z których każdy będzie miał 1 załącznik, automatyzacja „zużyje” **7** operacji. Uruchamiana 1 raz dziennie codziennie w ciągu miesiąca „zużyje” ok. **210** operacji.
- Jeśli zostaną znalezione 3 maile, z których każdy będzie miał 1 załącznik, automatyzacja „zużyje” **10** operacji. Uruchamiana 1 raz dziennie codziennie w ciągu miesiąca „zużyje” ok. **300** operacji.
- etc.

Liczba operacji wykorzystanych podczas danego uruchomienia automatyzacji jest oznaczona cyfrą znajdującą się w chmurce nad ikoną danego etapu procesu. Na przykład:

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201912%20949'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2024/11/14_Make-Operacje-1.png)

W [planie bezpłatnym](https://www.make.com/en/pricing) w ciągu miesiąca mamy do dyspozycji 1000 operacji. Po przekroczeniu tego limitu w danym miesiącu uruchomienie automatyzacji zostanie wstrzymane. Możesz wtedy przejść na wyższy pakiet w Make albo dokupić pakiet dodatkowych operacji (bez przechodzenia na wyższy plan).

Dlatego warto sprawdzać, ile operacji wykorzystuje nasza automatyzacja i rozsądnie ustawiać częstotliwość jej uruchamiania (np. raz dziennie, zamiast co minutę).

## Co jeszcze można zautomatyzować? Inne pomysły na wykorzystanie tej automatyzacji

Automatyzacja przedstawiona w tym artykule jest uniwersalna – możesz wykorzystać ją również do optymalizacji ss automation innych procesów, które polegają na pobraniu załącznika z maila i zapisaniu jakichś informacji na jego temat.

Na przykład:

- zbieranie prac nadsyłanych na konkurs;
- zbieranie zgód na wykorzystanie wizerunku od uczestniczek i uczestników warsztatów;
- zbieranie kart obiegowych od pracowniczek i pracowników organizacji;
- tworzenie zestawienia rachunków do zapłacenia w danym miesiącu (np. rachunek za Internet, telefon, prąd, czynsz, etc.).

## A jeśli nie korzystam z Google?

Aplikacje, które zostały wykorzystane w tej automatyzacji, są przykładowe. Jeśli nie korzystasz z Gmaila, możesz, zamiast niego wykorzystać np. [integrację z Outlook](https://www.make.com/en/integrations/microsoft-email). Jeśli nie korzystasz z Dysku Google – możesz wykorzystać np. [integrację z OneDrive](https://www.make.com/en/integrations/onedrive). [Katalog aplikacji](https://www.make.com/en/integrations?community=1&verified=1), które można wykorzysta w automatyzacjach w Make, jest bardzo szeroki!

## Koniec wykonywania powtarzalnych zadań. Podsumowanie!

Jeśli zdarza ci się wykonywać powtarzalne zadania i chcesz sobie tę pracę ułatwić, spróbuj wykorzystać automatyzacje! Zaoszczędzony czas będziesz mogła/mógł wykorzystać na ciekawsze zadania, wymagające kreatywności i skupienia, albo na… odpoczynek!

A jakie zadania ty chciałabyś/chciałbyś zautomatyzować?

**Dodatkowe materiały:**

- [Jak AI może ci pomóc w odpowiadaniu na często zadawane pytania?](https://sektor3-0.pl/blog/ai-pomoc-w-odpowiadaniu-na-czeste-pytania-faq/)
- [Jak sztuczna inteligencja może ci pomóc w nauce?](https://sektor3-0.pl/blog/sztuczna-inteligencja-pomoc-w-nauce/)
- [Smart notes – inteligentne notatki, które zwiększą twoją produktywność](https://sektor3-0.pl/blog/smart-notes-inteligentne-notatki-ktore-zwieksza-twoja-produktywnosc/)
- [Mapy myśli, czyli uczenie się przez skojarzenia](https://sektor3-0.pl/blog/mapy-mysli-czyli-uczenie-sie-przez-skojarzenia/)
- [Jak się efektywnie uczyć? Przydatne techniki i narzędzia](https://sektor3-0.pl/blog/jak-sie-efektywnie-uczyc-techniki-narzedzia/)
- [Make Academy](https://academy.make.com/) – bezpłatny kurs e-learningowy pozwalający lepiej poznać działanie Make

Newsletter

Dołącz do grona ponad 10 000 zaangażowanych subskrybentów i dwa razy w miesiącu otrzymuj nieodpłatnie nową dawkę wiedzy, inspiracji oraz technologicznych recenzji i porad od ekspertów i ekspertek programu Sektor 3.0.
