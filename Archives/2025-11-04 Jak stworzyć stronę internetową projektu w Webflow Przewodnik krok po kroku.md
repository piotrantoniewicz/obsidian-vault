---
type: Web
authors: '[[Marzena Kacprowicz]]'
url: >-
  https://sektor3-0.pl/blog/jak-stworzyc-strone-internetowa-projektu-w-webflow-przewodnik-krok-po-kroku/?utm_source=newsletter&utm_medium=email&utm_term=2026-03-24&utm_campaign=+Jak+reklamowa%C4%87+organizacj%C4%99+na+FB+i+IG+
published: 2025-11-04T00:00:00.000Z
created: 2026-03-24T00:00:00.000Z
tags:
  - organizacje-społeczne
  - produkty-cyfrowe
  - digital-campaigning
---


Ułatwienia dostępu

- Skalowanie treści 100%
- Czcionka 100%
- Wysokość linii 100%
- Odstęp liter 100%

![blog](https://sektor3-0.pl/wp-content/uploads/elementor/thumbs/blog-1-re789qqlugevtqdk3mqd5q3pl6fk6fi6rbg9w52hyu.jpg "blog")

Rozpoczynasz nowy projekt i chcesz opowiedzieć o nim światu? Jeśli szukasz narzędzia, które ułatwi ci stworzenie strony dla projektu, sprawdź Webflow – platformę, która pozwala tworzyć efektowne i funkcjonalne strony w tzw. podejściu no-code, czyli bez znajomości programowania. Z tego artykułu dowiesz się, jak krok po kroku przygotować prostą stronę startową projektu tzw. landing page z menu, opisem projektu, rekomendacjami uczestników, sekcją FAQ i formularzem zapisu.

Rozpoczynasz nowy projekt i chcesz opowiedzieć o nim światu? Jeśli szukasz narzędzia, które ułatwi ci stworzenie strony dla projektu, sprawdź Webflow – platformę, która pozwala tworzyć efektowne i funkcjonalne strony w tzw. podejściu no-code, czyli bez znajomości programowania. Z tego artykułu dowiesz się, jak krok po kroku przygotować prostą stronę startową projektu, tzw. landing page z menu, opisem projektu, rekomendacjami uczestników, sekcją FAQ i formularzem zapisu.

## Webflow – co to takiego?

[Webflow](https://webflow.com/) to platforma, która umożliwia wizualne projektowanie i tworzenie stron internetowych bez konieczności pisania kodu (jest to tzw. podejście *no-code*). W edytorze Webflow możesz stworzyć szablon strony z gotowych komponentów, korzystając z interfejsu typu „przeciągnij i upuść” (drag-and-drop), a Webflow wygeneruje dla niej zoptymalizowany kod i opublikuje ją w Internecie. Twoja strona będzie responsywna (czyli będzie się dobrze wyświetlała na różnych urządzeniach) i od razu będzie dostępna dla twoich odbiorców.

### Czym charakteryzuje się darmowa wersja Webflow?

Webflow oferuje [kilka pakietów cenowych](https://webflow.com/pricing). Darmowy plan Starter dobrze sprawdzi się jako bezpieczna „piaskownica” do nauki i testów. Możesz w nim stworzyć maksymalnie dwie strony, korzystać z większości funkcji edytora, zapisywać szkice i publikować stronę na bezpłatnej subdomenie [webflow.io](http://webflow.io/).

Jeśli zatem chcesz stworzyć prostą stronę startową (tzw. landing page) dla projektu i nie masz nic przeciwko, aby była ona opublikowana w domenie [webflow.io](http://webflow.io/) (np. [wolontariat-mlodziezowy.webflow.io](http://wolontariat-mlodziezowy.webflow.io/)), plan Starter będzie wystarczający.

## Tworzenie stron internetowych w Webflow krok po kroku

W ramach poniższej instrukcji zbudujemy stronę startową (tzw. landing page), wykorzystując gotowe komponenty (np. menu, sekcja nagłówkowa, stopka) z biblioteki Relume Library Lite. Osiągniemy następujący efekt ([zobacz w nowym oknie](https://sektor3-0.pl/wp-content/uploads/2025/10/00_Efekt_koncowy.png.pdf)):

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20750'%3E%3C/svg%3E)

### Krok 1: Załóż konto na Webflow

Wejdź na stronę [www.webflow.com](https://webflow.com/) i zarejestruj się (**Get Started**).

### Krok 2: Stwórz pusty szablon strony

Po zalogowaniu zobaczysz tzw. Dashboard – pulpit, na którym będą widoczne wszystkie stworzone przez ciebie strony. Kliknij przycisk **New site**.

![Panel startowy Webflow po zalogowaniu. To miejsce, w którym rozpoczynasz tworzenie strony internetowej. Kliknięcie przycisku „New site” uruchamia proces stworzenia strony w systemie no-code.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%20559'%3E%3C/svg%3E)

Panel startowy Webflow po zalogowaniu. To miejsce, w którym rozpoczynasz tworzenie strony internetowej. Kliknięcie przycisku „New site” uruchamia proces stworzenia strony w systemie no-code.

Dostępne są trzy sposoby tworzenia strony:

1. Za pomocą generatora bazującego na sztucznej inteligencji (**AI site builder**) – Webflow wygeneruje szablon strony na podstawie twojego polecenia (tzw. promptu).
2. Z gotowego szablonu (**Template**) – możesz wybrać jeden z gotowych szablonów, a następnie dostosować go do swoich potrzeb samodzielnie, za pomocą gotowych elementów strony (**Blank Site**).
![Ekran wyboru sposobu rozpoczęcia projektu. Webflow oferuje trzy opcje: AI Site Builder, gotowy Template lub Blank Site, pozwalający budować strony od podstaw. Dzięki temu każdy może wybrać styl tworzenia strony, który najlepiej odpowiada jego potrzebom.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%20895'%3E%3C/svg%3E)

Ekran wyboru sposobu rozpoczęcia projektu. Webflow oferuje trzy opcje: AI Site Builder, gotowy Template lub Blank Site, pozwalający budować strony od podstaw. Dzięki temu każdy może wybrać styl tworzenia strony, który najlepiej odpowiada jego potrzebom.

Wybierz opcję „ **Blank Site** ”.  
Wpisz nazwę swojej strony i kliknij przycisk „ **Create site** ”.

![Okno, w którym nadajesz nazwę projektowi – tutaj powstaje „Wolontariat Młodzieżowy”.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%20827'%3E%3C/svg%3E)

Okno, w którym nadajesz nazwę projektowi – tutaj powstaje „Wolontariat Młodzieżowy”.

Webflow wygeneruje tzw. canvas – wirtualne „płótno”, do którego będziemy dodawać elementy strony. Zostaniesz przeniesiony/przeniesiona do widoku edytora (tzw. Designer).

### Krok 3. Dodaj bibliotekę z gotowymi komponentami

Kliknij „ **+** ” znajdujący się w menu po lewej stronie – to zakładka Add Elements. Będą się w niej znajdowały elementy, z których zbudujemy stronę. Webflow oferuje kilka gotowych elementów, ale możemy też skorzystać z pakietu elementów z zewnętrznej biblioteki.

Wykorzystamy bibliotekę o nazwie **Relume Library Lite**. Aby dodać ją do projektu, kliknij zakładkę „ **Layouts** ” i w niebieski przycisk „ **Browse more libraries** ”.

![Panel boczny Webflow z zakładką Layouts. W tym miejscu można dodawać gotowe sekcje, korzystając z bibliotek komponentów.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201222%201324'%3E%3C/svg%3E)

Panel boczny Webflow z zakładką Layouts. W tym miejscu można dodawać gotowe sekcje, korzystając z bibliotek komponentów.

Zostaniesz przeniesiony/przeniesiona na stronę tzw. Webflow Marketplace. W znajdującej się tam wyszukiwarce zaznacz opcję „ **Free Libraries** ” i wyszukuj nazwę „ **Relume** ”.

![Widok strony Relume Library Lite w Webflow Marketplace. To darmowa biblioteka elementów, która wspiera tworzenie stron internetowych z gotowych komponentów. Świetna opcja dla osób, które chcą zaprojektować responsywną stronę internetową bez kodowania.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201308%201224'%3E%3C/svg%3E)

Widok strony Relume Library Lite w Webflow Marketplace. To darmowa biblioteka elementów, która wspiera tworzenie stron internetowych z gotowych komponentów. Świetna opcja dla osób, które chcą zaprojektować responsywną stronę internetową bez kodowania.

Kliknij kartę biblioteki, aby zobaczyć szczegółowe informacje na jej temat. Aby dodać bibliotekę do swojego projektu w Webflow, kliknij przycisk „ **Install library – Free** ”.

![Ekran instalacji biblioteki Relume. Wybierasz przestrzeń roboczą (Workspace), w której chcesz dodać komponenty.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201083'%3E%3C/svg%3E)

Ekran instalacji biblioteki Relume. Wybierasz przestrzeń roboczą (Workspace), w której chcesz dodać komponenty.

Zaznacz projekt, do którego chcesz dodać tę bibliotekę, i kliknij „ **Install** ”.

![Potwierdzenie instalacji Relume Library Lite w projekcie „Wolontariat Młodzieżowy”. Po kliknięciu Install, wszystkie elementy zostają dołączone do projektu, co umożliwia ich użycie przy dalszym tworzeniu strony.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201064'%3E%3C/svg%3E)

Potwierdzenie instalacji Relume Library Lite w projekcie „Wolontariat Młodzieżowy”. Po kliknięciu Install, wszystkie elementy zostają dołączone do projektu, co umożliwia ich użycie przy dalszym tworzeniu strony.

Biblioteka dodana! Teraz po ponownym wejściu do edytora strony i po kliknięciu „ **+** ” (Add Elements) w menu po lewej stronie. W zakładce Layouts będą już widoczne komponenty z biblioteki **Relume Library Lite**.

![W panelu Layouts widoczne są gotowe sekcje, które możesz przeciągać do projektu.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201210%201226'%3E%3C/svg%3E)

W panelu Layouts widoczne są gotowe sekcje, które możesz przeciągać do projektu.

Po kliknięciu kafelek Relume Library Lite zobaczysz dostępne komponenty. Zacznijmy zatem projektowanie!

### Krok 4: Dodaj komponenty do szablonu strony

Dodawanie komponentów jest bardzo proste: wystarczy wybrać gotowy komponent z biblioteki i kliknąć w niego – od razu pojawi się na „płótnie”.

1. **Dodaj menu:** kliknij element (Navbar):
![Widok dodanego komponentu Navbar 1 z biblioteki Relume. Pasek nawigacji z logo, linkami i przyciskami to pierwszy krok do budowy responsywnych stron internetowych, które dobrze wyglądają na każdym urządzeniu.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202044%20762'%3E%3C/svg%3E)

Widok dodanego komponentu Navbar 1 z biblioteki Relume. Pasek nawigacji z logo, linkami i przyciskami to pierwszy krok do budowy responsywnych stron internetowych, które dobrze wyglądają na każdym urządzeniu.

Menu jest widoczne w szablonie strony:

![Podgląd gotowego paska nawigacji w projekcie Webflow.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%20488'%3E%3C/svg%3E)

Podgląd gotowego paska nawigacji w projekcie Webflow.

1. W analogiczny sposób **dodaj sekcję główną** (Header Section):
![Dodawanie sekcji nagłówkowej w Webflow przy użyciu komponentu Header 1 z biblioteki Relume. To pierwszy widoczny element na stronie internetowej – miejsce, w którym możesz umieścić tytuł projektu i wezwanie do działania.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201299'%3E%3C/svg%3E)

Dodawanie sekcji nagłówkowej w Webflow przy użyciu komponentu Header 1 z biblioteki Relume. To pierwszy widoczny element na stronie internetowej – miejsce, w którym możesz umieścić tytuł projektu i wezwanie do działania.

1. Dodaj sekcję, w której opiszesz krótko projekt (Feature Section):
![Wybór układu Layout 239 z sekcją opisową. Tego typu moduły pomagają wyróżnić najważniejsze cechy lub korzyści projektu.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201297'%3E%3C/svg%3E)

Wybór układu Layout 239 z sekcją opisową. Tego typu moduły pomagają wyróżnić najważniejsze cechy lub korzyści projektu.

1. Dodaj sekcję z zachętą do działania (CTA – call to action):
![Dodanie sekcji CTA (Call to Action) – kluczowego elementu zachęcającego do działania. Tutaj można umieścić przycisk zapisów lub link do formularza.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201129'%3E%3C/svg%3E)

Dodanie sekcji CTA (Call to Action) – kluczowego elementu zachęcającego do działania. Tutaj można umieścić przycisk zapisów lub link do formularza.

1. Dodaj sekcję z wypowiedziami uczestników (Testimonial):
![Sekcja Testimonial 17 z opiniami uczestników. Tego typu moduł pomaga budować zaufanie odbiorców, prezentując ich doświadczenia i oceny.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202038%201312'%3E%3C/svg%3E)

Sekcja Testimonial 17 z opiniami uczestników. Tego typu moduł pomaga budować zaufanie odbiorców, prezentując ich doświadczenia i oceny.

1. Dodaj sekcję z najczęściej zadawanymi pytaniami (FAQ):
![Sekcja FAQ 1 z pytaniami i odpowiedziami. Dzięki niej możesz wyjaśnić najczęstsze wątpliwości użytkowników i skrócić ich ścieżkę decyzji. To także sposób na poprawę widoczności strony internetowej pod kątem wyszukiwarek, ponieważ sekcje FAQ często pojawiają się w wynikach Google.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201674%201308'%3E%3C/svg%3E)

Sekcja FAQ 1 z pytaniami i odpowiedziami. Dzięki niej możesz wyjaśnić najczęstsze wątpliwości użytkowników i skrócić ich ścieżkę decyzji. To także sposób na poprawę widoczności strony internetowej pod kątem wyszukiwarek, ponieważ sekcje FAQ często pojawiają się w wynikach Google.

1. Dodaj stopkę (Footer):
![Dodanie stopki Footer 4 – ostatniej sekcji każdej strony www. W tym miejscu warto umieścić dane kontaktowe, odnośniki do mediów społecznościowych oraz linki do polityki prywatności.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202030%201116'%3E%3C/svg%3E)

Dodanie stopki Footer 4 – ostatniej sekcji każdej strony www. W tym miejscu warto umieścić dane kontaktowe, odnośniki do mediów społecznościowych oraz linki do polityki prywatności.

### Krok 5: Dostosuj treści strony i poznaj zaawansowane funkcje

Komponenty zawierają przykładowe treści, ale wszystkie są edytowalne.

1. **Zmiana treści:** Aby je zmienić, kliknij dwa razy na wybrany tekst i wpisz swoją treść.
![Edytowanie tekstu w nagłówku i sekcji programu „Wolontariat Młodzieżowy”. W Webflow możesz dowolnie zmieniać treści, kolory i styl elementów, co pozwala w pełni dostosować stronę internetową do potrzeb projektu i zachowań użytkowników.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201992%201228'%3E%3C/svg%3E)

Edytowanie tekstu w nagłówku i sekcji programu „Wolontariat Młodzieżowy”. W Webflow możesz dowolnie zmieniać treści, kolory i styl elementów, co pozwala w pełni dostosować stronę internetową do potrzeb projektu i zachowań użytkowników.

1. **Zmiana grafik:** Kliknij grafikę obrazka. Pojawi się niebieski przycisk z nazwą elementu i ikona zębatki. Kliknij w nią. Wyświetli się okienko, w którym możesz dodać swoją grafikę.
![Panel Image Settings w Webflow – miejsce, gdzie możesz wgrać i podmienić grafiki w sekcjach.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201262'%3E%3C/svg%3E)

Panel Image Settings w Webflow – miejsce, gdzie możesz wgrać i podmienić grafiki w sekcjach.

1. **Usuwanie niepotrzebnych elementów:** Aby usunąć jakiś element, kliknij w niego i usuń, klikając na klawiaturze klawisz Delete.
2. **Zmiana stylowania (np. koloru tła, fontów):** Aby zmienić wygląd poszczególnych elementów, kliknij na wybrany element, a następnie zmień wybrane ustawienia w panelu po prawej stronie.

*Podpowiedź: Jeśli napotkasz na problem albo będziesz poszukiwał/poszukiwała porady, jak zmienić jakiś element strony, zapytaj AI! Możesz użyć prompta w stylu: „Korzystam z* [*Webflow.com*](http://webflow.com/) *i biblioteki Relume Linrary Light. Chcę zmienić tło sekcji Navbar 1. Jak to zrobić?”. Możesz też skorzystać z tutoriali w* [*Webflow University*](https://university.webflow.com/)*.*

### Krok 6: Skonfiguruj formularz

1. Dostosuj wygląd formularza.

Kliknij pole formularza w sekcji „Dołącz do nas”. Wyświetli się niebieska ikona zębatki. Kliknij ją. W oknie edycji formularza możesz zmienić nazwę formularza (Name) i tekst pomocniczy, który wyświetla się w polu (Placeholder).

![Ustawienia formularza zapisu w sekcji CTA. Tu możesz zdefiniować nazwę pola, jego typ (np. e-mail) i zasady obowiązkowego wypełnienia.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201264%20980'%3E%3C/svg%3E)

Ustawienia formularza zapisu w sekcji CTA. Tu możesz zdefiniować nazwę pola, jego typ (np. e-mail) i zasady obowiązkowego wypełnienia.

1. Skonfiguruj przesyłanie treści z formularza

Wejdź w ustawienia strony (Site settings), a następnie z menu po lewej stronie wybierz **Forms**.

![W ustawienia strony Webflow wejdziesz klikając ikonę zębatki.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201554%20794'%3E%3C/svg%3E)

W ustawienia strony Webflow wejdziesz klikając ikonę zębatki.

Zgłoszenia, które użytkownicy dodadzą za pośrednictwem formularza, będą wysyłane na wybrany przez ciebie adres e–mail. Możesz skonfigurować szczegóły wiadomości, którą otrzymasz od Webflow, kiedy w formularzu pojawi się nowe zgłoszenie:

- sender name: nazwa nadawcy maila;
- send form submissions to: adres e–mail, na który Weblow wyśle mail zawierający zgłoszenie z formularza;
- subject line: tytuł maila;
- email template: treść maila.
![Panel Forms w ustawieniach projektu Webflow. Tutaj konfiguruje się powiadomienia e-mailowe, adresy odbiorców oraz treść wiadomości wysyłanych po wypełnieniu formularza. To jedna z zaawansowanych funkcji, które pozwalają zautomatyzować komunikację na stronie internetowej.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201292'%3E%3C/svg%3E)

Panel Forms w ustawieniach projektu Webflow. Tutaj konfiguruje się powiadomienia e-mailowe, adresy odbiorców oraz treść wiadomości wysyłanych po wypełnieniu formularza. To jedna z zaawansowanych funkcji, które pozwalają zautomatyzować komunikację na stronie internetowej.

Porada: W planie Starter możesz odebrać maksymalnie 50 zgłoszeń z formularza.

### Krok 7: Opublikuj stronę internetową

Aby opublikować stronę, kliknij przycisk „ **Publish** ”, znajdujący się w prawym górnym rogu strony, a następnie kliknij przycisk „ **Publish to selected domains** ”.

![Ekran publikacji strony w Webflow. Użytkownik wybiera docelową domenę testową wolontariat-mlodziezowy.webflow.io i klika „Publish to selected domains”, aby udostępnić projekt online. To końcowy etap procesu tworzenia strony internetowej, który pozwala sprawdzić, jak wygląda strona www w sieci.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201370%20538'%3E%3C/svg%3E)

Ekran publikacji strony w Webflow. Użytkownik wybiera docelową domenę testową wolontariat-mlodziezowy.webflow.io i klika „Publish to selected domains”, aby udostępnić projekt online. To końcowy etap procesu tworzenia strony internetowej, który pozwala sprawdzić, jak wygląda strona www w sieci.

I gotowe! Twoja strona jest widoczna w Internecie pod wybraną domeną.

### Krok 8: Testuj i udoskonalaj!

Jeśli znajdziesz coś, co chcesz poprawić, albo jeśli zechcesz dodać lub usunąć jakiś komponent – śmiało! Stronę możesz edytować w dowolnym momencie.

Pamiętaj tylko, aby po wprowadzeniu zmian ponownie opublikować stronę!

## Plusy i minusy Webflow

Jak widzisz, budowanie stron z Webflow jest bardzo proste!

Zalety Webflow:

1. Możesz korzystać z wielu bibliotek dostępnych w Webflow Marketplace.
2. Stronę możesz zbudować z gotowych komponentów.
3. Łatwo możesz dostosować treści i styl komponentów.
4. Możesz wielokrotnie edytować, poprawiać stronę.
5. Stronę możesz szybko opublikować w Internecie na serwerze Webflow.
6. To tzw. rozwiązanie no-code – aby stworzyć stronę, nie musisz umieć programować!

Wady:

1. W wersji bezpłatnej Webflow nie pozwala na publikację strony pod własną domeną.
2. Jeśli chcesz zbudować bardziej rozbudowaną stronę (np. taką, która ma kilka podstron, albo która przez formularz przyjmuje więcej niż 50 odpowiedzi), musisz wykupić płatny pakiet.

**Chcesz nauczyć się, jak zaprojektować i stworzyć stronę www? Weź udział w bezpłatnym kursie e-learningowym pt.** [**Strona www – internetowa kwatera główna organizacji społecznej**](https://elearning.sektor3-0.pl/obszary/strony-www/) **przygotowanym przez Sektor 3.0.**

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201100%201100'%3E%3C/svg%3E)](https://elearning.sektor3-0.pl/obszary/strony-www/)

## Tworzenie profesjonalnych stron z pomocą Webflow – podsumowanie

Webflow to narzędzie, które uczy projektowania stron i pozwala błyskawicznie eksperymentować: tworzyć, publikować, sprawdzać, jak działa i zmieniać w razie potrzeby. Jeśli twój projekt dopiero startuje, Webflow w wersji darmowej może być dla niego dobrym sposobem na pokazanie się w sieci bez wysokich kosztów startowych. A kiedy twój projekt się rozwinie i plan bezpłatny okaże się niewystarczający, będziesz mógł/mogła przenieść stronę na płatny plan i podpiąć ją pod własną domenę, albo wyeksportować i opublikować na innym hostingu. Powodzenia!

**Przeczytaj także:**

- [Landing page z misją społeczną](https://sektor3-0.pl/blog/landing-page-z-misja-spoleczna/)
- [Strona internetowa NGO powinna służyć do zbierania pieniędzy. Jak stworzyć atrakcyjną i skuteczną donate page?](https://sektor3-0.pl/blog/strona-internetowa-ngo-powinna-sluzyc-do-zbierania-pieniedzy-donate-page/)
- [Ruch na stronie Sektor 3.0 spadł o 60%. Dlaczego winne są pliki cookies i co to znaczy dla NGO?](https://sektor3-0.pl/blog/ruch-na-stronie-sektor30-spadl-o-60-winne-sa-pliki-cookies/)
- [Linki, które działają: praktyczny przewodnik po linkowaniu w NGO](https://sektor3-0.pl/blog/linkowanie-w-ngo-przewodnik/)
- [Substack – co to za platforma? Newslettery jako alternatywa dla mediów społecznościowych](https://sektor3-0.pl/blog/substack-co-to-newslettery-alternatywa-dla-mediow-spolecznosciowych/)

Newsletter

Dołącz do grona ponad 10 000 zaangażowanych subskrybentów i dwa razy w miesiącu otrzymuj nieodpłatnie nową dawkę wiedzy, inspiracji oraz technologicznych recenzji i porad od ekspertów i ekspertek programu Sektor 3.0.
