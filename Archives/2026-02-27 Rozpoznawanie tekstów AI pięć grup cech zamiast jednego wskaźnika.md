---
type: Web
authors: '[[Marcin Wilkowski]]'
url: >-
  https://blog.humanistyka.dev/2026/02/rozpoznawanie-tekstow-ai-piec-grup-cech-zamiast-jednego-wskaznika?utm_source=newsletter&utm_medium=email&utm_term=2026-06-14&utm_campaign=Jak+filtrowa%C4%87+slopy+AI+w+wyszukiwarce+Technologia+venture+capital+i+hype+wojenny+Rozpoznawanie+tekst%C3%B3w+AI+Cyfryzacja+domowego+archiwum+Teologiczny+benchmark+modeli+generatywnych+Nagrania+z+webinari%C3%B3w+o+danych+dziedzictwa
published: 2026-02-27
created: 2026-06-14
tags:
  - LLM
  - narzędzia-AI
  - ghostwriting
---


Student przesyła podejrzaną pracę zaliczeniową, a znana dziennikarka–celebrytka w krótkim czasie publikuje kolejną książkę, której temat wymaga zaawansowanego researchu. Pojawiają się podejrzenia, że to wszystko może być możliwe tylko dzięki zastosowaniu sztucznej inteligencji, jednak trudno to jednoznacznie udowodnić. Kolejne badania dotyczące cech tekstów wytwarzanych maszynowo sugerują, że nie pojawi się jedna, uniwersalnie skuteczna i automatyczna metoda wykrywania tego typu treści. Zamiast tego analizować należy poszczególne warstwy tekstu.

Identyfikacja tekstów generatywnych jest kluczową sprawą między innymi dlatego, że autorstwo jest ściśle związane z ocenianiem, braniem odpowiedzialności za słowo i zaufaniem między autorką a czytelnikiem. Doskonale widać to w dyskusji o użyciu sztucznej inteligencji w tworzeniu treści Wikipedii. Plany dodania automatycznych streszczeń [zostały jednoznacznie odrzucone przez społeczność](https://mashable.com/article/wikipedia-halts-ai-plans-as-editors-revolt), ponieważ w systemie Wikipedii wartością jest możliwość przypisania każdej zmiany w treści hasła do konkretnego autora-edytora, który bierze za nią odpowiedzialność. Wartość autorstwa rośnie też wobec zalewu treści generowanych maszynowo, które często [charakteryzują się specyficzną generycznością](https://blog.humanistyka.dev/2025/09/syntetyczny-prababkizm-czyli-gleboki-wymiar-uprzedzen-duzych-modeli-jezykowych).

Korzystanie z systemów mających umożliwić wykrycie tekstu maszynowego ma chronić wartość autorstwa. Skuteczności tych detekcji nie bazuje jednak wyłącznie na trafności takich analiz, ale też na rzetelności ewaluacji i sprawiedliwej ocenie. W przypadku korzystania z popularnych komercyjnych detektorów niezwykle często uzyskać można wynik fałszywie pozytywny, co prowadzi do niesprawiedliwej oceny twórczości konkretnych osób. Dostępne badania dowodzą zresztą, że detektory [fałszywie klasyfikują jako generowane przez AI teksty pisane przez osoby, które nie są rodzimymi użytkownikami języka angielskiego](https://blog.humanistyka.dev/2025/08/jak-rozpoznac-czy-tekst-zostal-wygenerowany-przez-ai-ograniczenia-perpleksji-i-propozycja-wikipedii).

Jednoznaczna ocena wystawiona przez detektor nie uwzględnia też *natury* pracy z tekstem. Od lat możliwe i dozwolone jest tam przecież korzystanie z racjonalnego wsparcia maszynowego na różnych poziomach, takich jak słowniki, korekta językowa czy nawet automatyczna redakcja tekstu. Wsparcie takie nie zawsze musi oznaczać, że autor lub autorka nie włożyli w swój tekst odpowiedniej ilości pracy albo że tekst nie jest oryginalny.

Wobec ograniczonej skuteczności automatycznych ocen pozostaje nam jedynie samodzielne opracowywanie heurystyk do rozpoznawania tekstów wytwarzanych maszynowo. Muszą one być tworzone z myślą o konkretnych zadaniach i stosowane w określonych warunkach oraz w ramach jasno określonych celów, jak przekonują Georgios Georgiou w pracy *What Distinguishes AI-Generated from Human Writing? A Rapid Review of the Literature* (DOI: [10.3390/bdcc10020055](https://doi.org/10.3390/bdcc10020055), 2025).

Autor, analizując 40 tekstów naukowych, w których przedstawiono konkretne zalecenia i charakterystyki tekstów generowanych maszynowo, nie proponuje jednej uniwersalnej metody badania. Zamiast tego grupuje wyodrębnione z tych prac metody i perspektywy. Dzięki pracy Georgiou możemy zbudować własny system rozpoznawania wytworów maszynowych, definiując odpowiednie klucze, parametry i wartości w ramach zidentyfikowanych przez niego grup (określanych jako grupy wskazówek, *cue families*). Taki ogólny schemat, wypracowany tu na podstawie literatury przedmiotu, wypełniać mielibyśmy własnymi metodami i cechami, dopasowanymi do konkretnego celu naszej analizy i charakterystyki analizowanego materiału.

Dlaczego konieczne jest takie profilowanie i dlaczego nie możemy polegać [na ogólnych zaleceniach](https://blog.humanistyka.dev/2025/08/jak-rozpoznac-czy-tekst-zostal-wygenerowany-przez-ai-ograniczenia-perpleksji-i-propozycja-wikipedii)? Jeśli nie będzie uniwersalnych metod, być może nigdy nie zostanie udostępniony w pełni skuteczny i uniwersalny detektor, na bazie którego dałoby się zbudować system ochrony do stosowania na uczelniach, w redakcjach czy wydawnictwach 😔.

Wyzwaniem jest na przykład gatunkowość tekstu. Wiadomo, że teksty różnych gatunków różnią się między sobą specyficznymi cechami. Abstrakt naukowy, opowiadanie czy przepis na ciasto narzucają konkretne ograniczenia dotyczące struktury, retoryki i stylu. Dopiero w odniesieniu do tych cech możemy ocenić, czy dany fragment lub cały tekst ma charakter wytworu maszynowego. Nikogo nie zdziwi brak fabuły w abstrakcie czy przepisie, nikt też nie będzie narzekał, że w opowiadaniu brakuje przypisów, chyba że to akurat opowiadanie DFW, który [uznawał, że przypisy mają](https://lithub.com/the-fine-art-of-the-footnote/)

> …uczynić tekst główny łatwiejszym w lekturze, a jednocześnie 1. dopuścić dyskursywny, autorsko-intruzywny styl, bez “finneganizowania” opowieści, 2. naśladować zalew informacji i konieczność ich selekcji, które, jak się spodziewałem, miały stać się jeszcze większą częścią życia w USA 15 lat później, 3. nadać całości znacznie więcej technicznej i medycznej wiarygodności, 4. pozwolić / zmusić czytelnika do dosłownego, fizycznego “przemieszczania się tam i z powrotem” w sposób, który być może żartobliwie odzwierciedla \[symuluje - MW\] niektóre trudności wyrażane w opowieści… 5. sprawić, by emocjonalnie było to odczuwalne jako spełnienie twojej prośby o kompresję tekstu bez wyrzucania ogromnych ilości materiału.

Zagranie z przypisami jako częścią (czasem równoległą) fabuły to dość dalekie odejście od generycznego pisania. Paradoksalnie, działający na uniwersalnych regułach detektor mógłby opisać tekst z takimi przypisami jako maszynowy, ponieważ 1) zinterpretowałby je jako przejaw niskiej jakości tekstu (a przecież modele tworzą teksty niskiej jakości), 2) uznałby je jako przejaw niepotrzebnego strukturyzowania treści (podobnie zrobiłby to z wypunktowaną listą, którą modele mają zbyt często umieszczać w generowanych tekstach).

Podobnie miałaby się sprawa z interpretowaniem rejestrów językowych, np. w tekstach, w których język korporacyjny czy techniczny używany jest do opisu stanów emocjonalnych albo prowadzenia fabuły.

Cóż, nie wygląda to najlepiej. Dlatego zamiast polegać na detektorach, lepiej wypracować sobie własne filtry. Georgios Georgiou pokazuje w swojej pracy, wobec jakich warstw tekstu można je zastosować:

![enter image description here](https://blog.humanistyka.dev/content/images/20260227170946-692d914475cbc00c5b16e7543c873080efd99e085267f707c9fd8490b2f02319.png)

**1\. Cechy powierzchniowe**

Co jest analizowane:

- rozkład leksykalny i składniowy,
- statystyki stylometryczne,
- wskaźniki czytelności.

Ta grupa wskaźników odwołuje się do zauważalnych różnic między tekstami ludzkimi i maszynowymi w dystrybucji leksykalnej, morfoskładni i formie stylistycznej. Brzmi to mocno skomplikowanie, ale wcale takie nie jest: chodzi tu po prostu o zbadanie, w jaki sposób tekst jest skonstruowany językowo, jak różnorodne i złożone jest wykorzystywane w nim słownictwo, jaka jest statystyka części mowy itp.

Jedną z głównych metod takiego powierzchniowego badania jest stylometria, a więc maszynowe wyliczanie statystyk określonych rodzajów słów (np. n-gramów albo interpunkcji) i porównywanie ich ze statystykami wyliczanymi z tekstów ludzkiego autorstwa.

W analizie powierzchniowej użyć można także wskaźników czytelności - narzędzia pozwalające na wyliczanie tych wskaźników dostępne są także [dla języka polskiego](https://jasnopis.pl/oferta/aplikacja/).

**2\. Cechy dyskursywne i pragmatyczne**

Co jest analizowane:

- konstrukcja tekstu,
- *organizacja* retoryczna,
- postawa autora wyrażająca się w tekście.

Georgiou pisze, że teksty generowane w AI często powielają szablony gatunkowe, ale w inny niż ludzie sposób konstruują wypowiedź. Badać można także to, jak w tekście ujawnia się postać autora, np. czy wyraża on jakieś zaangażowanie w poruszany temat, jaką postawę przyjmuje wobec tego, o czym pisze itp.

**3\. Cechy epistemiczne i treściowe**

Co jest analizowane:

- ugruntowanie tekstu w rzeczywistości (faktach) - obecność halucynacji,
- odwoływanie się autora do własnych doświadczeń i ich wiarygodność,
- jakość uzasadniania twierdzeń i przywoływanych dowodów (głównie w tekstach naukowych).

Badanie odwołujące się do cech epistemicznych i treściowych tekstu pozwala sprawdzić jakość informacji i wiarygodność przekazu. Przykładowo, analiza maszynowo wygenerowanych recenzji filmów może odwoływać się do tego, jak w tych recenzjach opisane są wrażenia widza i jak są wiarygodne, ale też do tego, czy przywoływane w nich wybrane sceny rzeczywiście znajdują się w ocenianej produkcji.

**4\. Cechy przewidywalności i probabilistyczne**

Co jest analizowane:

- statystyczna regularność w wyborze kolejnych słów.

Badania tej warstwy tekstów wymagają użycia oprogramowania. Jak pisze Georgiou, teksty AI charakteryzują się statystyczną regularnością w wyborze kolejnych słów (niską entropią i specyficznym rozkładem prawdopodobieństwa), co odróżnia je od bardziej nieprzewidywalnego języka ludzkiego.

**5\. Cechy pochodzenia**

Co jest analizowane:

- zaburzenia we wzorcu występowania kolejnych słów w tekście.

Niektóre narzędzia do generowania tekstów pozwalają już na zapisywanie w wytworzonych treściach specyficznego znaku wodnego. Nie jest to - tak jak w przypadku klasycznych obrazków - widoczny w treści element, ale [pewne sprofilowanie wzoraca wyboru kolejnych słów](https://blog.humanistyka.dev/2025/09/synthid-daje-sie-skutecznie-oznaczac-i-wykrywac-teksty-generowane-maszynowo). Detektory AI mogą korzystać z takich znaków wodnych, od niedawna każdy użytkownik Google Gemini może wykrywać teksty maszynowe [oznaczane SynthID](https://deepmind.google/models/synthid/) - informacje, jak to zrobić, dostępne są [na stronie pomocy Google](https://support.google.com/gemini/answer/16722517).

Niestety, test zbudowany na podstawie tych pięciu grup wskaźników niekoniecznie musi być skuteczny. Wspomniałem już o problemie zależnym od gatunku tekstu, ale dotyczy on właściwie wszystkich grup wskaźników. Innym czynnikiem, który może obniżać wartość testów w poszczególnych grupach, jest na przykład długość tekstu lub parafrazowanie. Wykorzystanie stylometrii, jak zauważa autor, może być skuteczne nawet w przypadku krótkich tekstów. Natomiast stosowanie metod probabilistycznych ma sens głównie w tekstach o większej długości. Parafrazowanie może także znacząco osłabiać analizę cech dyskursywnych i pragmatycznych, ponieważ nieuczciwy autor może za pomocą określonych zabiegów ukrywać charakterystyczne dla tekstów generowanych maszynowo frazy, zbitki słów i inne cechy typowe dla generowanych automatycznie treści.

> włączone do analizy badania oraz szersza literatura przedmiotu pozwalają na sformułowanie jednego praktycznego wniosku: nie istnieje pojedynczy, stabilny “podpis” AI. Możliwość wykrycia tekstów generowanych maszynowo wynika z warstwowych grup wskazówek, których przydatność zależy od ograniczeń gatunkowych, procesu rewizji oraz warunków adwersarialnych \[czyli od tego, czy autor próbuje obejść system wykrywania - MW\].

Ten pesymistyczny wniosek nie musi oznaczać, że w wykrywaniu tekstów maszynowych czekają nas wyłącznie porażki. W rzeczywistości tekst jako forma komunikacji okazuje się stosunkowo odporny na kategoryzację i wyróżnianie jednoznacznych cech. Wiadomo o tym od dawna i zostało to wielokrotnie przebadane, na przykład w kontekście pojęcia autorstwa - tekst jest przecież czymś głębszym niż struktura zdań i statystyka używanych słów. Brak znaczącego postępu w skutecznym rozpoznawaniu tekstów generowanych maszynowo to jedynie konsekwencja tej złożoności.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).
