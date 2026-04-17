---
type: Web
authors: '[[ngo.pl]]'
url: >-
  https://publicystyka.ngo.pl/formularz-odporny-na-bledy-wypelniajacych-poznaj-wyrazenia-regularne-regex-w-google-forms-tau?utm_source=newsletter&utm_medium=email&utm_term=2026-03-24&utm_campaign=Koniec+z+b%C5%82%C4%99dami+w+formularzach+
published: 2025-08-20T00:00:00.000Z
created: 2026-03-24T00:00:00.000Z
tags:
  - automatyzacja
  - narzędzia-AI
  - organizacje-społeczne
---


**Przeglądarka Internet Explorer, której używasz, uniemożliwia skorzystanie z większości funkcji portalu ngo.pl.** Aby mieć dostęp do wszystkich funkcji portalu ngo.pl, zmień przeglądarkę na inną (np. Chrome, Firefox, Safari, Opera, Edge).

**ngo.pl używa plików cookies, żeby ułatwić Ci korzystanie z serwisu** Ten komunikat zniknie przy Twojej następnej wizycie. [Dowiedz się więcej o plikach cookies](https://www.ngo.pl/prywatnosc)

[![Prośba o wpłatę darowizny na Twój portal ngo.pl prowadzony przez Stowarzyszenie Klon/Jawor.](https://api.ngo.pl/media/get/260293)](https://www.ngo.pl/wesprzyj?utm_source=publicystyka&utm_medium=przyciskgorny&utm_campaign=darowiznakj)

Znasz tę sytuację, gdy w formularzu kontaktowym ktoś podał numer telefonu składający się z 8 lub 10 cyfr i nie da się z tą osobą skontaktować? A może zdarzyło Ci się stracić godziny na znalezienie niepoprawnych wpisów, a następnie korespondencję, żeby uzyskać poprawne dane? Istnieje rozwiązanie, dzięki któremu to same osoby wypełniające będą szukały błędów, zanim wyślą formularz – to wyrażenia regularne (RegEx) w Formularzach i Arkuszach Google.

![](https://api.ngo.pl/media/get/262814?w=1200&h=800)

### Czym są i jak stosować wyrażenia regularne Formularzach Google?

Formularze Google (Google Forms) w pytaniach otwartych pozwalają zastosować kilka prostych sposobów weryfikacji wpisywanych przez osoby ankietowane danych, np.:

- wyłącznie e-maila, więc nie pozwolą wpisać ciągu bez małpy czy ciągu ze spacją,
- tekstu zawierającego jakiś sprecyzowany ciąg znaków lub właśnie niezawierający go,
- wartości liczbowej mniejszej / większej od zadanej, co jest przydatne np. jeśli chcemy się upewnić, że wszystkie osoby wypełniające podadzą czas w tej samej jednostce – minutach (nie akceptujemy długości zajęć krótszej niż 30) lub godzinach (nie akceptujemy długości zajęć dłuższej niż np. 5),
- minimalnej / maksymalnej liczby znaków wpisu.

Ale co, jeśli informacja, której potrzebujemy, ma jakąś inną, specyficzną strukturę? Np. chcemy, żeby osoby podały numer telefonu albo np. sygnaturę jakiegoś dokumentu w ramach wewnętrznej sprawozdawczości.

Powiedzmy, że podpisywane w organizacji umowy mają strukturę składającą z numeru umowy, trzech liter wskazujących na projekt oraz roku podpisania – 123/ABC/2024. Chcemy więc dopuścić wszystkie wpisy, które będą się składały z ciągu od 1 do 4 cyfr, a następnie ukośnika, a następnie 3 liter, a następnie ukośnika, a następnie 4 cyfr.

**Wyrażenie regularne pozwala określić wzorzec tekstu, a Formularze Google zweryfikują, czy wpis użytkownika\_czki pasuje do określonego schematu, a jeśli nie będzie pasował – nie pozwoli na jego wpisanie.**

Wyrażenie regularne będzie w tym konkretnym przypadku wyglądało następująco:

**^\\d{1,4}/\[ A-Z\]{1,3}/\\d{4}$**

Przeanalizujmy teraz cały ciąg i wytłumaczmy, co oznaczają poszczególne znaki:

- Daszek – start wyrażenia
- /d cyfra
- {1,4} informacja, że cyfr może być od 1 do 4
- / - tak jak widać
- \[A-Z\] – wielka litera
- {1-3} informacja, że liter może być od 1 do 3
- /
- \\d cyfra
- Informacja, że cyfr ma być dokładnie 4
- $ - koniec wyrażenia.

Przykłady, o których czytasz w tym tekście, pokazuje również wideo. Poniżej znajdziesz wideo-tutorial, który pomoże Ci krok po kroku przejść ze mną przez proces tworzenia Formularzy Google i pracy z Arkuszami Google z wyrażeniami regularnymi RegEx. Sugeruję przeczytać do końca tekst, a następnie oglądnąć wideo, by poukładać sobie nową wiedzę i proces działania.

![](https://www.youtube.com/watch?v=El3KIqDNtfc)

### RegEx – przykłady wykorzystania wyrażeń regularnych w Formularzach Google

**Przykład pierwszy: tylko adresy służbowe**

Chcemy, żeby osoby rejestrowały się na wydarzenie z adresów służbowych. W takiej sytuacji formułą regex możemy zablokować wpisy kończące się na „gmail.com” i kilka innych najpopularniejszych polskich domen. Prostsza opcja „tekst nie zawiera” umożliwiałaby zablokowanie tylko jednej domeny, a my chcemy wskazać kilka. Na pewno nie damy rady zablokować wszystkich, ale prawdopodobnie w wielu przypadkach osoby dostaną prośbę o wpisanie adresu służbowego.

**Przykład drugi: lista obecności o precyzyjnej strukturze**

Przeanalizujmy teraz realny przykład wdrożenia z projektu „Biblioteka dla Wszystkich”, który realizujemy w Fundacji Rozwoju Społeczeństwa Informacyjnego (FRSI). To lista obecności, która będzie potem przetwarzana przez automat, więc musi mieć zachowaną idealnie strukturę:

**Id osoby, przecinek, id osoby, przecinek**

Formularz nie przepuszcza wypełnień, gdzie np.:

- ciąg cyfr jest dłuższy niż 3 (co by wskazywało, że zmieszały się dwa numery ID bez przecinka – bo nie ma dłuższych niż 3-cyfrowe),
- ani wypełnień, gdzie zamiast przecinka jest inny separator,
- ani ciągów, w których przypadkowo pojawia się litera lub znak specjalny.

### Tworzenie i sprawdzanie wyrażeń regularnych RegEx z pomocą chatbotów AI

Jeśli chcesz poznać i przyswoić sobie najważniejsze elementy składni wyrażeń regularnych zaglądnij do tego zestawienia: [Składnia wyrażeń regularnych – Administrator Google Workspace](https://support.google.com/a/answer/1371415?hl=pl).

W tym miejscu warto zaznaczyć, że z przygotowaniem wyrażenia znakomicie radzą sobie chatboty AI, które nie tylko generują wyrażenie regularne, ale od razu na przykładach pokazują, jakie ciągi ono przyjmie, a jakie zablokuje. Mogą być również bardzo przydatne podczas uczenia się składni, ponieważ jeśli wyrażenie napisane przez nas nie działa zgodnie z oczekiwaniami, szybko wskażą, w których miejscach popełniony jest błąd.

**Przykładowe wyrażenia do wykorzystania w codziennej pracy**

- **Numer telefonu – 9 cyfr:** ^\\d{9}$
- **Numer telefonu – z prefixem kraju:** ^+\\d{1,3}\\d{9}$
- **PESEL:** ^\\d{11}$
- **NIP:** ^\\d{10}$
- **Kod pocztowy:** ^\\d{2}-\\d{3}$
- **Numer dowody osobistego:** ^\[A-Z\]{3}\\d{6}$
- **Określone domeny e-mail:** (gmail.com|email.com|email.pl) – jeśli chcesz je wykluczyć, pamiętaj, żeby w Formularza Google przestawić opcję wyrażenia regularnego z „zawiera” na „nie zawiera”.

### Jak korzystać z wyrażeń regularnych (RegEx) w Arkuszach Google?

Jeśli zdarza Wam się pracować w wiele osób na jednym Arkuszu kalkulacyjnym Google (Google Spreadsheets), również mogą Wam się przydać wyrażenia regularne. Być może osoba, która rzadziej musi coś wpisywać do tego pliku, czasem zapomina o ustaleniach dotyczących struktury danych, które mają być wprowadzane w którejś kolumnie? Być może ktoś pisze na klawiaturze bardzo szybko, ale często trafiają mu się literówki?

W takich sytuacjach ustalenie weryfikacji danych sprawi, że ostrzeżenie pojawi się natychmiast i nie będzie trzeba szukać błędnych komórek po dłuższym czasie, kiedy plik znacznie się rozrośnie.

Arkusze Google dają prostsze metody dbania o jakość danych (zablokowanie edycji części kolumn) czy możliwość wybrania wyłącznie wartości z listy (podobnie jak w pytaniu zamkniętym w ankiecie). Czasem jednak te metody mogą być niewystarczające.

Chcesz zobaczyć, jak w praktyce działa weryfikacja danych z użyciem wyrażeń regularnych w Arkuszach Google? W poniższej części wideo-tutorialu pokażę Ci krok po kroku, jak ustawić sprawdzanie poprawności wpisów, tak aby formularz mógł całkowicie blokować błędne dane lub – w wersji bardziej elastycznej – jedynie wyświetlać ostrzeżenie i poprosić o ich sprawdzenie. Zobaczysz też różnicę między składnią z użyciem znaków ^ i $ (dopasowanie całej zawartości komórki), a tą, która pozwala wyszukiwać jedynie fragment pasujący do wzorca.

Zobacz jak korzystać z wyrażeń regularnych w Arkuszach Google w [naszym wideo-tutorialu](https://www.youtube.com/watch?v=El3KIqDNtfc&t=815s).

### RegEx Bonus zamiast zakończenia

Na koniec mam dla Ciebie przykład, jak regex przydaje się w analizie i czyszczeniu danych. Wyobraź sobie, że masz plik Excel z 1200 wierszami, a w każdym dane adresowe, które były zbierane wiele lat temu i zostały odpowiednio zwalidowane na etapie zbierania.

Zazwyczaj, kiedy sięgacie do podobnego pliku, okazuje się, że część adresów zawiera tylko nazwę ulicy, bez numeru domu. Plik tej długości da się jeszcze przejrzeć i samem znaleźć nieprawidłowe adresu, ale pewnie zajmie to ok. 20-30 minut.

Dlaczego więc nie użyć formuły regex, która sprawdzi, w których komórkach nie została użyta żadna cyfra? Dzięki temu problematyczne wiersze zostaną znalezione w 2 minuty (wliczając czas na poproszenie chatbota, żeby napisał odpowiednie wyrażenie regularne).

### Przeczytaj inne przydatne artykuły

- [11 bezpłatnych narzędzi cyfrowych dla NGO: praca biurowa, komunikacja i zarządzanie projektami](https://publicystyka.ngo.pl/11-bezplatnych-narzedzi-cyfrowych-dla-ngo-praca-biurowa-komunikacja-i-zarzadzanie-projektami-tau)
- [Airtable: przyjazna baza danych z funkcją formularzy online i automatyzacji](https://sektor3-0.pl/wideo/airtable-narzedzie-do-zarzadzania-bazami-danych-automatyzacji/)
- [Wypróbuj Gemy w Google Gemini i spraw sobie wirtualnego asystenta AI](https://publicystyka.ngo.pl/wyprobuj-gemy-w-google-gemini-i-spraw-sobie-wirtualnego-asystenta-ai-tau)
- [Porządki w Gmailu. Jak korzystać z kategorii, etykiet i narzędzi do porządkowania informacji z sieci](https://publicystyka.ngo.pl/porzadki-w-gmailu-jak-korzystac-z-kategorii-etykiet-i-narzedzi-do-porzadkowania-informacji-z-sieci)
- [Analizujesz dane organizacji? Uważaj na te 3 pułapki](https://sektor3-0.pl/blog/analiza-danych-ngo-3-pulapki/)

---

**Interesujesz się nowymi technologiami i chcesz w oparciu o nie rozwijać swoją organizację? Zajrzyj również na** [**blog Sektora 3.0**](https://sektor3-0.pl/blog) **i dołącz do naszego** [**newslettera**](https://sektor3-0.pl/newsletter)**, by nie przegapić kolejnych przydatnych tekstów. Zapraszamy!**

Źródło: [Sektor 3.0](https://sektor3-0.pl/)

![](https://api.ngo.pl/media/get/254826)

Tekst opublikowany dzięki [Sektor 3.0](http://sektor3-0.pl/). Sektor 3.0 to przedsięwzięcie [Polsko-Amerykańskiej Fundacji Wolności](http://pafw.pl/). Jego realizację powierzono specjalistom z [Fundacji Rozwoju Społeczeństwa Informacyjnego](http://frsi.org.pl/). Treść na licencji [CC BY-NC-SA 3.0 PL](https://creativecommons.org/licenses/by-nc-sa/3.0/pl/).

Artykuły opublikowane w portalu ngo.pl prezentują wyłącznie poglądy ich autorów, autorek. Wyrażone w nich opinie, komentarze nie muszą być tożsame z poglądami redakcji.

[![Prośba o wpłatę darowizny. Wesprzyj Twój portal ngo.pl prowadzony przez Stowarzyszenie Klon/Jawor](https://api.ngo.pl/media/get/197944)](https://www.ngo.pl/wesprzyj?utm_source=publicystyka&utm_medium=przyciskartykul_dol&utm_campaign=darowiznakj)
