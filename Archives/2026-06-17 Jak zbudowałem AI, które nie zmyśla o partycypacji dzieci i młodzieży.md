---
type: Web
authors: '[[Rafał Szymański]]'
url: 'https://rafalszymanski.pl/blog/ai-rag-ktore-nie-zmysla-partycypacja/'
published: null
created: 2026-06-17T00:00:00.000Z
tags:
  - narzędzia-AI
  - LLM
  - organizacje-społeczne
---


## Jak zbudowałem AI, które nie zmyśla o partycypacji dzieci i młodzieży

Przewodnik dla nieinżynierów: jak działa PIA — prywatna baza wiedzy z asystentem AI opartym na RAG. Dlaczego model „nie zmyśla”, czym jest embedding, po co dzielić dokumenty na fragmenty i dlaczego polski tekst kosztuje 2–3 razy więcej niż angielski.

![Rafał Szymański](https://rafalszymanski.pl/_astro/rafal-szymanski.oIVgdvWG_2lIDMU.webp)

Rafał Szymański

Wdrażam LinkedIn i Sales Navigator firmach B2B

![Jak zbudowałem AI, które nie zmyśla o partycypacji dzieci i młodzieży](https://rafalszymanski.pl/_astro/22-pia-dashboard.CPVDuRhe_Z1FG9iP.webp)

*Ten artykuł to przewodnik dla nieinżynierów: dla badaczek i badaczy nauk społecznych oraz młodych aktywistów, którzy chcą zrozumieć, jak naprawdę działa „Partycypacyjny Inteligentny Asystent” — i dlaczego akurat tak.*

W skrócie

PIA to prywatna baza wiedzy z asystentem AI zbudowanym na architekturze **RAG**. W przeciwieństwie do ChatGPT odpowiada **wyłącznie na podstawie dokumentów w Twojej bazie** i **cytuje źródła**, zamiast zmyślać. Poniżej tłumaczę bez żargonu, jak to działa: czym jest embedding, po co dzielić dokumenty na fragmenty i dlaczego polski tekst zmusił mnie do konkretnych decyzji technicznych.

## Problem, który zna każdy, kto śledzi temat

Wyobraź sobie, że zajmujesz się partycypacją dzieci i młodzieży lub jakimkolwiek innym tematem — jako badaczka, jako działacz organizacji, jako członek zespołu doradczego.

Codziennie przybywa materiałów: raport UNICEF, opracowanie uniwersyteckie, dokument rządowy, jakaś polityka krajowa po czesku, diagnoza NGO, briefing Rzeczniczki Praw Dziecka.

Część po polsku, część po angielsku, ale większość w innych językach. Część jako PDF, część jako strona internetowa, a do tego masz jeszcze swoją książkę lub wewnętrzne badanie w Wordzie.

Ręcznie nie ma szans, że to ogarniesz — ja nie ogarniałem. Przeczytanie wszystkiego po kolei jest nieefektywne, a `Ctrl+F` po kilkudziesięciu plikach — niemal bezużyteczne. Problem z prostym wyszukiwaniem za pomocą `Ctrl+F` jest taki, że znajdzie ono dokładnie to słowo, które wpiszesz. Jeśli szukasz „uczestnictwa nastolatków”, a w dokumencie jest „rady młodzieżowe” albo angielskie „youth empowerment” — nie znajdzie nic, choć mówią dokładnie o tym samym.

PIA — **Partycypacyjny Inteligentny Asystent** — powstała właśnie z tej potrzeby. Nazwa PIA jest roboczo wymyślona przeze mnie, bo jak z czymś rozmawiam, to lubię nadać mu nazwę. „Zapytaj PIA” brzmi lepiej w mojej głowie niż „Zapytaj RAG”, bo PIA takim RAG-iem właśnie jest.

Stworzyłem ją dla zespołu doradczego przy Rzeczniczce Praw Dziecka, w którym pracują obok siebie naukowcy i aktywiści o bardzo różnym przygotowaniu — zarówno do partycypacji jako takiej, jak i do wykorzystania AI. Kiedy zostałem powołany do tego zespołu, miałem bardzo ogólne pojęcie o tym, czym jest partycypacja dzieci i młodzieży, a do tego problem, by szybko tę wiedzę uzupełnić.

Z kolei inne osoby z zespołu miały wiedzę i materiały, ale wyzwaniem było współdzielenie tej wiedzy i szybka analiza dużej ilości danych. Przykład: mój podzespół miał za zadanie przeanalizować 13 znanych nam polityk prawnych z krajów UE oraz wzorcowy dokument UNICEF i przygotować wnioski, które z tych praktyk możemy zaproponować dla Polski i dlaczego.

Rok temu wziąłem kilka osób z zespołu na szkolenie z podstaw AI dla organizacji pozarządowych, ale stało się dla nas jasne, że wiele osób słyszy słowa „RAG”, „embedding” czy „LLM” pierwszy raz w życiu. A żeby korzystać z AI **dobrze**, warto rozumieć, jak i dlaczego ona działa tak, a nie inaczej. Ten tekst jest właśnie o tym.

Kiedy w maju miałem przygotować wewnętrzne szkolenie, stwierdziłem, że lepiej będzie pracować na czymś, co zespół zna i rozumie, i na tym tłumaczyć wszystkie te pojęcia.

## Czym PIA jest — i czym na pewno nie jest

W skrócie: PIA to **prywatna baza wiedzy z asystentem AI**, która robi trzy rzeczy.

1. **Codziennie sama szuka nowych materiałów** w sieci (o 7:00 rano) i dokłada je do bazy.
2. **Pozwala wgrywać źródła ręcznie** — przeciągasz plik, a AI samo wyciąga tytuł, autorów, datę i tagi. Sprawdza najpierw, czy nie ma tego już w bazie, nawet jeśli pliki zostały inaczej nazwane.
3. **Daje wyszukiwarkę i czat jak ChatGPT, ale lepszy** — pytasz po polsku *„co badania mówią o partycypacji uczniów w szkole średniej?”*, a system odpowiada, **cytując konkretne źródła**, w które możesz kliknąć i skopiować je potem do Worda.
![Ekran czatu PIA z pytaniem „O co chcesz zapytać?” i informacją, że odpowiedzi powstają na podstawie źródeł w bazie wiedzy o partycypacji dzieci i młodzieży](https://rafalszymanski.pl/_astro/22-pia-chat-empty.C2sBy7Z-_1lDcSh.webp)

Ekran startowy czatu PIA. Już tu widać kluczową obietnicę: „Odpowiem na podstawie źródeł w bazie wiedzy o partycypacji dzieci i młodzieży”.

I tu najważniejsze rozróżnienie, bo przesądza o wszystkim:

> **PIA to nie ChatGPT.**

ChatGPT odpowiada na podstawie tego, co „zapamiętał” z internetu do pewnej daty. Nie zna Twojego raportu z zeszłego tygodnia ani PDF-a z konsultacji, który właśnie wgrałeś. A gdy o coś takiego zapytasz — potrafi **wymyślić odpowiedź z pełnym przekonaniem**: nieistniejącego autora, zmyśloną datę, fikcyjny raport. To nie jest „błąd” — to wynika z natury tych modeli, o czym za chwilę.

PIA jest inna: odpowiada **wyłącznie na podstawie dokumentów, które są w Twojej bazie**. Jeśli czegoś tam nie ma — powie „brak danych”, zamiast zmyślać. To fundament całej konstrukcji. Nie da Ci też przepisu na stek z grilla, mimo że modele AI, z których jest zbudowana, pewnie ten przepis znają.

![PIA odmawia napisania przepisu na stek z grilla, tłumacząc, że pytanie wykracza poza zakres dostępnych źródeł o partycypacji dzieci i młodzieży](https://rafalszymanski.pl/_astro/22-pia-stek.VZ1MztP-_Z2fwyT3.webp)

Test w praktyce: na prośbę o przepis na stek z grilla PIA nie zmyśla — odpowiada „nie jestem w stanie udzielić odpowiedzi w oparciu o dostępne źródła”, bo w bazie nie ma nic o gotowaniu.

Dla porządku, czym PIA też nie jest: nie jest publiczną wyszukiwarką (dostęp ma tylko wąska, zatwierdzona grupa osób) ani systemem recenzji naukowej. To narzędzie do **briefingu i odkrywania** wiedzy, nie do oceniania jej jakości — tę ocenę zostawiamy człowiekowi.

## RAG — czyli jak sprawić, żeby AI nie zmyślała

Tu dochodzimy do serca sprawy. Skrót **RAG** oznacza *Retrieval-Augmented Generation* — „generowanie wspomagane wyszukiwaniem”. Brzmi technicznie, ale idea jest prosta.

Model językowy (taki jak Claude czy ChatGPT) to genialny pisarz. O cokolwiek go zapytasz, zawsze odpowie, bo tak właśnie działają modele językowe.

Gdybym chciał to opisać prościej: wyobraź sobie wyjątkowo elokwentnego absolwenta socjologii. Poproszony o esej o najnowszych badaniach, napisze go płynnie i przekonująco. Problem w tym, że jeśli nie zna źródeł na bieżąco, **zacznie zmyślać autorów i daty** — bo jego zadaniem jest „brzmieć sensownie”, a nie „mówić prawdę”. Stąd tyle memów o halucynacjach AI.

RAG to instrukcja: *„Najpierw weź z półki te konkretne książki, przeczytaj odpowiednie fragmenty i dopiero potem pisz — a przy każdym zdaniu podaj, z której książki pochodzi”.*

Co dzieje się naprawdę, gdy zadajesz PIA pytanie:

1. **System rozumie pytanie.** Jeśli rozmawiacie od kilku tur i dopytujesz „a co z gminami?”, tani, szybki model najpierw przepisuje to w samodzielne zapytanie na podstawie kontekstu rozmowy: *„partycypacja młodzieży na poziomie gminy”*.
2. **System szuka pasujących fragmentów** w Twojej bazie — nie po słowach kluczowych, lecz po **znaczeniu** (jak dokładnie, wyjaśniam w następnej sekcji).
3. **Buduje „ściągę” dla modelu** — wkleja znalezione fragmenty do polecenia, ponumerowane: `[1]`, `[2]`, `[3]` …
4. **Model pisze odpowiedź** wyłącznie na podstawie tej ściągi, wstawiając numery cytowań: *„Poziom realnej partycypacji w szkołach średnich jest niski \[1\]. Diagnoza Młodzieży 2026 wskazuje, że tylko 23% uczniów… \[1\]”*.
5. **Cytaty stają się klikalne** — `[1]` to link do dokładnego źródła, które możesz otworzyć i sprawdzić.
![Diagram pięciu kroków RAG: pytanie, embedding pytania na wektor 3072 liczb, szukanie najbliższych fragmentów w bazie, wklejenie ich do polecenia jako ponumerowana ściąga, odpowiedź modelu z klikalnymi cytatami](https://rafalszymanski.pl/_astro/22-pia-rag-flow.BfDgJJ76_2qK1Jj.svg)

Pięć kroków RAG — od pytania do odpowiedzi opartej wyłącznie na znalezionych fragmentach, z klikalnym przypisem przy każdym zdaniu.

Dlaczego ta architektura jest tak mocna? Z czterech powodów, które badacz doceni od razu:

- **Wiarygodność** — każde stwierdzenie ma przypis. Nie ma „jak powszechnie wiadomo”, jest „\[1\] wskazuje”. Możesz kliknąć i ocenić źródło sam.
- **Aktualność** — żeby PIA znała nowy raport, wystarczy go dodać do bazy. Nie trzeba „przetrenowywać” modelu (to byłaby operacja za setki tysięcy dolarów).
- **Trzymanie się tematu** — zapytasz o stolicę Argentyny lub coś niezwiązanego z tematem, a dostaniesz „brak danych w bazie”, bo modelowi wprost zabraniam korzystać z wiedzy spoza Twoich dokumentów.
- **Audytowalność** — system zapisuje każde pytanie, każdą odpowiedź i każde cytowane źródło. Da się odtworzyć, co dokładnie odpowiedział i na jakiej podstawie.

Na hot-path, czyli tam, gdzie jakość odpowiedzi liczy się najbardziej, używamy obecnie najmocniejszego dostępnego modelu (Claude Opus 4.8), a do tańszych, pomocniczych zadań — modeli lżejszych. To też świadoma decyzja: drogi model tam, gdzie czytelnik to odczuje; tani tam, gdzie nie. Jak mówił Ferdek Kiepski w jednym z seriali: „Tanie to nie jest, ale jest dobrze”.

## Dlaczego „wyszukiwanie po znaczeniu” — i jak to w ogóle możliwe

Wróćmy do kroku 2: skąd system wie, że „rady młodzieżowe” i „youth empowerment” mówią o tym samym, skoro nie mają wspólnego słowa?

Odpowiedź to **embedding**. To zamiana każdego fragmentu tekstu na **wektor liczb** — u nas na ciąg **3072 liczb** — w taki sposób, że teksty o podobnym znaczeniu dostają liczbowo **bliskie sobie** wektory, nawet jeśli słownictwo jest zupełnie inne.

Tu pomaga analogia, którą docenią osoby z nauk społecznych. Pomyśl o **wielowymiarowej skali Likerta**. W badaniu postaw wobec demokracji młodzieżowej masz np. 20 itemów: zaufanie do instytucji, poczucie sprawczości, stosunek do autorytetów… Każdy respondent staje się **wektorem 20 liczb**. Dwoje respondentów o podobnych wynikach na tych 20 wymiarach ma podobne postawy — nawet jeśli na pojedyncze pytania odpowiedzieli inaczej.

Embedding to dokładnie to samo, tylko z **3072 wymiarami zamiast 20** — i z jedną kluczową różnicą: tych wymiarów nie zdefiniował badacz. Model sam „nauczył się” ich z ogromnego korpusu tekstów. Nie da się ich nazwać („wymiar 47 to formalność”), ale **odległość między dwoma wektorami** wiarygodnie mówi, jak blisko tematycznie są dwa teksty. Pytanie też zamieniamy na taki wektor i szukamy fragmentów, których wektory są najbliżej — i to działa również **między językami**: angielski dokument potrafi „dopasować się” do polskiego pytania.

![Diagram embeddingu: zdanie zamieniane na wektor 3072 liczb, analogia do wielowymiarowej skali Likerta z 3072 wymiarami oraz skala podobieństwa kosinusowego od 0.0 do 1.0](https://rafalszymanski.pl/_astro/22-pia-embedding.DZhjrv_I_Zrlahg.svg)

Embedding zamienia tekst na wektor 3072 liczb. Im bliżej siebie dwa wektory, tym bliższe tematycznie teksty — niezależnie od użytych słów, a nawet języka.

Dlaczego akurat ten model i 3072 wymiary? Bo w testach lepiej radził sobie z niuansami niż lżejsze warianty, a koszt policzenia jednego zapytania jest znikomy. Ale jest jeden haczyk, który zmusił mnie do konkretnej decyzji programistycznej:

> **Polski tekst „kosztuje” około 1,5–2 razy więcej niż angielski.**

![Porównanie tokenizacji: angielskie „participation” to 1 token (~4 znaki na token), polskie „partycypacja” to 4 tokeny (~2–3 znaki na token); limit embeddingu 14 000 znaków dla polskiego zamiast 24 000 dla angielskiego](https://rafalszymanski.pl/_astro/22-pia-tokeny.DqAjyOco_IGebX.webp)

To samo pojęcie: po angielsku jeden token, po polsku cztery. Stąd niższy limit znaków na fragment dla polskiego — i wyższy koszt. (Slajd z mojej prezentacji „AI w służbie partycypacji”.)

Modele tną tekst na „tokeny” (kawałki słów). Język angielski dzieli się na tokeny oszczędnie (~4 znaki na token), polski — przez odmianę, ogonki i dłuższe wyrazy — znacznie gęściej (~2–3 znaki na token). Model embeddingu ma twardy limit, ile tokenów przyjmie naraz. Dlatego ustawiłem, na podstawie mojej wiedzy, granicę **14 000 znaków** na jeden fragment do embedowania: dla polskiego to bezpieczny zapas, żeby tekst zmieścił się w limicie modelu i nie został „obcięty w pół zdania”. To dobry przykład tego, jak realia języka polskiego wymuszają decyzje, których w anglojęzycznym projekcie by nie było — albo byłyby mniej istotne. Jednocześnie odrzuciłem pomysł, by wszystko tłumaczyć na angielski, tak embedować, a potem tłumaczyć na polski z powrotem — bo zależało mi na języku i jego niuansach.

## Dlaczego AI dzieli dokumenty tak, a nie inaczej

Skoro embedujemy fragmenty „do 14 000 znaków”, to co z całą resztą? Bo dokumenty są przeróżne: jedne mają jedną stronę, inne to całe książki — w naszej bazie zdarzają się teksty po **ponad milion znaków**. Nie da się (i nie ma sensu) zamieniać takiej książki na jeden wektor — wektor „o wszystkim” jest tak naprawdę „o niczym”. Stąd **chunking**: dzielenie dokumentu na kawałki.

Moje AI robi to **hierarchicznie**, na dwóch poziomach:

- **Fragment-dziecko** (~1000 znaków, z lekkim zakładem na granicach) — to po nim szukamy. Mały, precyzyjny, „o jednej myśli”. Dzięki temu trafienie jest celne: zamiast „ten dokument gdzieś o tym wspomina”, dostajemy „dokładnie ten akapit o tym mówi”.
- **Fragment-rodzic** (~5000 znaków) — szerszy kontekst wokół trafionego dziecka. To **jego** podajemy modelowi do napisania odpowiedzi.

Analogia: **fiszka indeksowa kontra rozdział**. Szukasz po fiszkach — są małe i łatwo wśród nich znaleźć właściwą. Ale gdy już znajdziesz fiszkę, do napisania mądrej odpowiedzi czytasz cały rozdział, z którego pochodzi, żeby nie wyrwać zdania z kontekstu. Małe fragmenty dają **celność wyszukiwania**, duże dają **bogactwo kontekstu** — bierzemy jedno i drugie.

Do tego dochodzi jeszcze druga ścieżka wyszukiwania: klasyczne wyszukiwanie po słowach kluczowych (full-text search), ale w wersji, która **rozumie polską odmianę** — żeby „partycypacją”, „partycypacji” i „partycypacja” traktować jako to samo słowo. Standardowe narzędzia bazodanowe tego po polsku nie potrafią, więc użyliśmy wyspecjalizowanego rozszerzenia. Najlepsze wyniki daje **połączenie obu metod** — semantycznej i słów kluczowych — bo każda łapie coś, co druga gubi.

## Co z tego jest dla Ciebie?

Jeśli jesteś **badaczką lub badaczem**: PIA działa jak zautomatyzowany **przegląd systematyczny literatury**. Te same etapy, które znasz — definicja zapytań, pierwsza selekcja po tytule i abstrakcie, pełne czytanie, kodowanie/tagowanie, synteza — system wykonuje sam, w ~30 sekund na dokument zamiast tygodni. Ale **kuratorstwo zostaje po Twojej stronie**: każdy wpis możesz odrzucić, zarchiwizować, oznaczyć gwiazdką jako ważny, poprawić tagi. To świadomy kompromis: stawiam na **szybkość**, bo wąskim gardłem nie jest precyzja metadanych, tylko Twój czas na czytanie.

![Widok pojedynczego źródła w PIA: automatycznie wyciągnięte metadane (autorzy, wydawnictwo, język, liczba słów), sekcja „Dlaczego warto”, opis, tagi oraz przyciski weryfikacji Zatwierdź i Odrzuć](https://rafalszymanski.pl/_astro/22-pia-zrodlo-detail.rLE_mTQ0_20BpeN.webp)

Widok źródła: AI samo wyciąga metadane, tagi i streszczenie „Dlaczego warto”, ale ostatnie słowo należy do człowieka — Zatwierdź, Odrzuć, popraw tagi, dopisz notatkę.

Jeśli jesteś **młodym aktywistą**: zamiast „gdzieś czytałem, że młodzież chce być pytana o sprawy szkoły”, dostajesz konkretne zdanie z numerem źródła, w które możesz kliknąć i pokazać decydentowi. Argument poparty cytowalnym źródłem waży nieporównanie więcej niż wrażenie.

I uczciwie o **granicach** — bo zrozumienie ich to też część dobrego korzystania z AI:

- **Nie ma dokumentu — nie ma odpowiedzi.** PIA nie zna świata poza Twoją bazą. To zaleta (nie zmyśla), ale i ograniczenie (jest tak dobra, jak to, co do niej wrzucisz).
- **Złe pytanie — słabe trafienia.** Im konkretniejsze pytanie, tym celniejsze fragmenty. Jedno słowo „partycypacja” znajdzie cokolwiek; pełne zdanie — to, o co naprawdę chodzi.
- **Patrz na cytaty.** Jeśli `[1]` dotyczy innej kwestii niż zdanie, przy którym stoi — to sygnał, że model nadinterpretował. Klikalne cytaty są właśnie po to, żeby dało się to wychwycić.
- **To nie peer-review.** PIA pomaga znaleźć i streścić, ale ocena wartości naukowej źródła należy do Ciebie.

## Na koniec

Nie chodziło mi o to, żeby zbudować „magiczne pudełko, które wie wszystko”. Chodziło o narzędzie, któremu **można zaufać, bo widać, na czym opiera każde zdanie** — i które zespół o bardzo różnym przygotowaniu jest w stanie zrozumieć i sensownie używać.

Dlatego każda decyzja, którą tu opisałem — RAG zamiast „gołego” czatu, embedding po znaczeniu, limit 14 000 znaków podyktowany specyfiką języka polskiego, dwupoziomowy chunking, łączenie wyszukiwania semantycznego z fleksyjnym — nie jest przypadkowa. To odpowiedzi na konkretne pytania: *jak nie pozwolić AI zmyślać, jak poradzić sobie z polskim, jak ogarnąć i jednostronicowy briefing, i całą książkę.*

Bo dobre korzystanie z AI nie polega na ślepej wierze w odpowiedź. Polega na rozumieniu, **jak** i **dlaczego** ona powstała.

Przy tym projekcie sam dużo się nauczyłem o budowaniu małych, wyspecjalizowanych modeli AI z konkretną wiedzą domenową. Dość łatwo teraz wdrożyć identyczny system, ale z inną wiedzą — np. o socjologii, problemach psychicznych nastolatków czy czymkolwiek innym. Wykorzystałem swoją wiedzę o analizie NLP języka polskiego, bo bez tego nie udałoby się dobrze zrobić tokenizacji (dzielenia tekstu na mniejsze części), lematyzacji i stemmingu (sprowadzania wyrazów do ich podstawowej formy, np. „biegł”, „biegniesz” do „biec”) oraz rozpoznawania znaczenia. Mam nadzieję, że PIA będzie też przydatnym narzędziem dla osób z zespołu.

Skontaktuj się ze mną

## Może zrobimy coś wspólnie?

Jesli podoba Ci się to co piszę, może mogę napisać coś dla Ciebie?

![Może zrobimy coś wspólnie?](https://rafalszymanski.pl/_astro/cta-spoleczne.pGy09HRO_Z1ObF1z.webp)
