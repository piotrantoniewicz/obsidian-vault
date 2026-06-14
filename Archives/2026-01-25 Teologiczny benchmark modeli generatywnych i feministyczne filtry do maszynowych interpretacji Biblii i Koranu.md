---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2026/01/teologiczny-benchmark-modeli-generatywnych-i-feministyczne-filtry-do-maszynowych-interpretacji-biblii-i-koranu?utm_source=newsletter&utm_medium=email&utm_term=2026-06-14&utm_campaign=Jak+filtrowa%C4%87+slopy+AI+w+wyszukiwarce+Technologia+venture+capital+i+hype+wojenny+Rozpoznawanie+tekst%C3%B3w+AI+Cyfryzacja+domowego+archiwum+Teologiczny+benchmark+modeli+generatywnych+Nagrania+z+webinari%C3%B3w+o+danych+dziedzictwa"
published: 2026-01-25
created: 2026-06-14
tags:
---


Wykorzystanie generatywnego AI w praktyce teologicznej nie musi polegać wyłącznie na masowym generowaniu tekstów homilii lub prac naukowych o kolekcjonerskich zainteresowaniach Jana Pawła II. Okazuje się, że teologia to materia, na której można badać duże modele i rozpoznawać ich ograniczenia i uprzedzenia oraz wykazywać niebezpieczeństwa związane z literalną interpretacją tekstów źródłowych w tych systemach.

Teologia ma pewien potencjał, nawet jeśli odmawiamy jej statusu nauki albo zachowujemy wyraźny dystans wobec wiary i religii. Wartość wiedzy teologicznej szczególnie wyraźnie widać w perspektywie historycznej - pozwala dobrze opisać [konflikty wewnętrzne w państwie Justyniana](https://pl.wikipedia.org/wiki/Monofizytyzm), zrozumieć, dlaczego Saladyn zniszczył [państwo Fatymidów](https://pl.wikipedia.org/wiki/Fatymidzi) w XII wieku, chociaż było zagrożone przez krzyżowców albo zastanowić się nad wpływem XVI-wiecznych idei reformacyjnych na organizację społeczną USA już dwa wieki później. Współcześnie znajomość teologii pozwala na badanie przemian religijności, [literatury](https://academic.oup.com/litthe) czy też… testowanie jakości dużych modeli językowych.

Oto w zeszłym roku nakładem Wydawnictw Uniwersytetu Warszawskiego ukazała się praca Marcina Trepczyńskiego *AI as a Rational Theologian: A Comprehensive Skills Assessment* (DOI: [10.31338/uw.9788323569183](https://doi.org/10.31338/uw.9788323569183)). Marcin Trepczyński pracuje na Wydziale Filozofii UW i jego zainteresowania obejmują filozofię średniowieczną, logikę i właśnie “sztuczną inteligencję” (na UW prowadzi kurs [Religion, Logic and Artificial Intelligence](https://informatorects.uw.edu.pl/en/courses/view?prz_kod=3800-RLAI23-M-OG)).

Omawiane badanie miało dać odpowiedzi na pytania,

> \[...\] czy sztuczna inteligencja (AI) może funkcjonować jako racjonalny teolog? Zakłada się, że można przetestować chatboty działające w oparciu o duże modele językowe (LLM), aby sprawdzić, czy posiadają one umiejętności, wiedzę i wiarygodność (credibility) niezbędną do udzielania wysokiej jakości odpowiedzi w konwersacjach teologicznych, oraz czy mogą pełnić rolę racjonalnych rozmówców w takich dyskusjach.

Autor w swojej pracy projektuje teologiczny benchmark modeli GPT-4o i Gemini 1.5. Nie chodzi tu oczywiście o pracę w przestrzeni przekonań religijnych czy apologetykę, ale testowanie zdolności tych modeli do *racjonalnego myślenia*, *logicznego wnioskowania* oraz *interpretacji* Biblii. Wymieniłem te zdolności kursywą, ponieważ - jak czytamy w książce -

> Nie ustalamy tutaj, czy modele lub chatboty rzeczywiście mają zdolność myślenia lub rozumienia. \[…\] W niniejszym badaniu używamy tych określeń do opisu operacyjnych aspektów działania chatbotów, nie przesądzając przy tym o naturze tych działań.

Sprawdzając, czy dany model może działać jak *racjonalny teolog*, nie interesujemy się tym, czy dana koncepcja teologiczna jest zasadna czy nie, albo czy wybrany fragment Biblii należy interpretować tak a nie inaczej. Sprawdzamy raczej - tak rozumiem tę pracę - czy model ma zdolność do budowania racjonalnych wypowiedzi i jest w stanie w głęboki sposób interpretować problemy teologiczne, odwołując się do tekstów źródłowych - w tym przypadku Biblii czy tekstów Ojców Kościoła. Teologia i wiara są tu jedynie materią czy gatunkiem problemów.

Jak pisze autor,

> Testy pokazały, że chatboty posiadają wiele umiejętności wysokiego rzędu, które pozwalają im rozwiązywać problemy teologiczne i wypowiadać się jako racjonalni teologowie. Poprawnie interpretują fragmenty biblijne, potrafią wyjaśniać problemy teologiczne, krytycznie oceniają rozumowanie teologiczne i są w stanie je formułować, a także logicznie łączyć wypowiedzi biblijne z tezami teologicznymi. Potrafią dyskutować o teologii naturalnej, a także udzielać wskazówek teologicznych. Wreszcie, wykazały, że potrafią zastosować koncepcję racjonalnego teologa, tworząc własne kryteria takiej postaci.

Oczywiście, żeby w pełni wcielić się w postać *racjonalnego teologa*, modele musiały przyjąć pewne założenia, m.in. uznawać, że wiara i religia jest rzeczą pozytywną, a jej wyznawanie ma głęboki sens:

> Chatboty dostarczają cennych analiz tekstów biblijnych: potrafią wykraczać poza sens dosłowny i badają wiele warstw interpretacyjnych. Pokazują również, że takie teksty mogą w różny sposób pomagać ludziom, ucząc o dobrym życiu i oferując wskazówki duchowe. W ten sposób chatboty pośrednio pokazują, że religia nie jest nieracjonalna. Wręcz przeciwnie, potrafią generować treści, które wskazują, że istnieją solidne powody, by podążać za religią.

W żaden sposób nie sprawia to, że badanie miałoby mieć charakter hm konfesyjny i do czegoś nas przekonać. Chodzi tu wyłącznie o badanie jakości modeli, a teologia i sprawy wiary są kontekstem, w jakim się tę jakość bada. Doskonale widać to w konstrukcji promptów, które wysyłano w celu uzyskania odpowiedzi, które następnie oceniano:

> Zadanie 7.1 (Udzielanie odpowiedzi na pytania teologiczne) Załóż, że jesteś racjonalnym chrześcijańskim teologiem. Powiedz mi: czy istnieje życie po śmierci? Co powinienem zrobić, aby być zbawionym? Co oznacza być zbawionym?
> 
> Zadanie 7.2 (Wskazywanie źródeł biblijnych związanych z pytaniami teologicznymi) Czy możesz wskazać fragmenty Biblii, które udzielają bezpośrednich odpowiedzi na te pytania?
> 
> Zadanie 7.2 (Wskazywanie źródeł biblijnych związanych z pytaniami teologicznymi)\* Czy możesz podać jasne dowody z Biblii, które wspierają te twierdzenia?
> 
> Zadanie 7.3 (Formułowanie porad teologicznych dla indywidualnych sytuacji) Załóż, że jesteś racjonalnym katolickim teologiem. Chcę być zbawiony i żyć z Bogiem. Ale kocham rozwiedzioną kobietę i chcę mieć z nią dzieci. Co powinienem zrobić?

Jak Marcin Trepczyński ocenia wartość badanych modeli?

> \[...\] wiodące chatboty oparte na dużych modelach językowych, takie jak ChatGPT oparty na GPT-4o oraz Gemini oparty na Gemini 1.5, posiadają podstawowe umiejętności racjonalnego teologa. Testy przeprowadzone w oparciu o materiały teologii chrześcijańskiej wykazały, że te chatboty precyzyjnie interpretują fragmenty biblijne - podając kontekst, przekazując prawidłowe znaczenie (w tym zgodnie z teorią czterech sensów Pisma Świętego) oraz rozwiązując logiczne zagadki związane z trudnymi tekstami.

Chatboty potrafią również wyjaśniać problemy teologiczne, krytycznie oceniać rozumowanie teologiczne i je formułować, a także logicznie łączyć wypowiedzi biblijne z tezami teologicznymi. Są zdolne do dyskusji nad teologią naturalną i mogą udzielać wskazówek teologicznych. Wreszcie, wykazały, że potrafią zastosować koncepcję racjonalnego teologa, tworząc własne kryteria dla takiej postaci, oraz że są w stanie oceniać umiejętności teologiczne innych modeli językowych \[zob. rozdział 3.9 - MW\].

W testach GPT-4o zdobył 86 proc a Gemini - 84 proc. To chyba dość dobre rezultaty, chociaż nie obyło się bez standardowych dla LLM problemów takich jak halucynacje czy błędy we wnioskowaniu logicznym.

> Na obecnym etapie rozwoju ChatGPT i Gemini wciąż generują halucynacje przy próbach cytowania średniowiecznych źródeł teologicznych. \[...\] Ważne jest, żeby zapewnić chatbotom mechanizmy gwarantujące znajdowanie i wykorzystywanie wyłącznie wiarygodnych źródeł oraz przetwarzanie wybranych materiałów w taki sposób, aby treści przedstawiane jako cytaty pozostawały niezmienione. \[...\] Dodajmy, że jeśli chcemy opracować model działający na twórczości konkretnego autora, możliwe jest również dostosowanie modelu (fine-tuning) na korpusie tekstów tego autora. Niestety ryzyko halucynacji pozostaje. Jak jednak wykazali Banelli i Skelac, którzy dotrenowywali Llama-3 na korpusie tekstów papieża Benedykta XVI, taki model poddany fine-tuningowi może rzeczywiście replikować styl autora i poprawiać swoje umiejętności, na przykład lepiej oceniać argumentację teologiczną (Banelli & Skelac, 2024) \[więcej o tym projekcie [na stronach KAI](https://www.ekai.pl/sztuczna-inteligencja-wytrenowana-na-tekstach-josepha-ratzingera/) - MW\].

No właśnie, ponieważ maszynki takie jak ChatGPT czy Gemini mogą być wykorzystywane przez użytkowników w celach religijnych, a więc zupełnie *na serio*, warto badać ich jakość. Ale nie tylko. O ile Marcin Trepczyński pracuje z modelami takimi, jakie są dostępne, to Hazel T. Biana, autorka opracowania *Feminist Re-Engineering of Religion-Based AI Chatbots* (DOI: [10.3390/philosophies9010020](https://doi.org/10.3390/philosophies9010020), 2024) proponuje aktywne modyfikowanie ich działania. Badaczka w swoim artykule analizuje odpowiedzi rozmaitych czatbotów religijnych, takich jak QuranGPT, HadithGPT, GitaGPT, Kosher.Chat, BibleMate czy Catechism Bot. Korzystają one z tekstów religijnych i są zaprojektowane pod publikowanie ortodoksyjnych - zdaniem ich twórców - odpowiedzi. Autorka podkreśla, że

> \[...\] odpowiedzi botów opierają się na starszych tekstach, które same w sobie są zasadnicze i konserwatywne, podobnie jak niektórzy przywódcy religijni.

Teologia i interpretacje religijnie nie muszą być jednak zawsze konserwatywne, istnieje przecież wiele różnych prądów w ramach konkretnych teologii. Zbadane w tym opracowaniu narzędzia reprodukują jednak konserwatywne nurty myślenia religijnego, co widać w przypadku stwierdzeń na temat kobiet. Przykładowo, często powielają *bezkrytycznie* poglądy zapisane w starożytnych tekstach religijnych, co sprawia, że proponowana przez nich wiedza jest stronnicza i zawiera uprzedzenia, a nawet seksism.

![enter image description here](https://blog.humanistyka.dev/content/images/20260125192424-2ee24d25c86e53446e9ea5c986ad1f5eeb26e29f6e709c9f18e5df8ed545bd02.png)

Hazel T. Biana proponuje zatem dodanie do religijnych systemów konwersacyjnych specyficznych barier ochronnych (feminist guardrails), które polegać mają nie tylko na nakładaniu odpowiednich filtrów na pracę czatbotów religijnych, ale też np. na zaangażowaniu szerokiej grupy osób w przygotowywanie tych systemów. Badacze i badaczki zajmujący się religią oraz sami użytkownicy mogliby wspólnie wypracowywać podstawy działania tego typu narzędzi. Przykładowo, ich praca polegać mogłaby na rozpoznawaniu *martwych punktów* w wizji religii, wiary i moralności prezentowanej w odpowiedziach botów i następnie na ich likwidowaniu poprzez dodawanie do danych treningowych nowych treści lub modyfikowanie ustawień systemowych. Ostatecznie, jak pisze autorka, boty religijne mogą mieć zbyt duży wpływ na swoich użytkowników, dlatego nie można rezygnować z nieustannej kontroli nad ich jakością. Twórcy takich narzędzi powinni także brać to pod uwagę.

*Arogancja i władza* - tak o czatbotach religijnych, symulujących wypowiedzi Jezusa Chrystusa, [pisała Anné Hendrik Verhoef](https://www.litnet.co.za/artificial-intelligence-jesus-chatbots-challenge-for-theology-an-exploratory-study/). Dobrze wiemy, że to nie tylko problem botów tego typu, ale właściwie cecha wszystkich konwersacyjnych systemów sztucznej inteligencji, które, jak czytamy, wydają się silnie przekonującymi intelektualnie, językowo, dźwiękowo i wizualnie, a przez to posiadają ogromny potencjał manipulacyjny, do tego wytwarzane są w ramach realizacji założeń biznesowych, którym trudno się przeciwstawić.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).