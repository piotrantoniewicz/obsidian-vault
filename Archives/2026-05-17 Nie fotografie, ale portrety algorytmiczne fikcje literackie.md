---
type: Web
authors: '[[Marcin Wilkowski]]'
url: >-
  https://blog.humanistyka.dev/2026/05/nie-fotografie-ale-portrety-algorytmiczne-fikcje-literackie?utm_source=newsletter&utm_medium=email&utm_term=2026-06-14&utm_campaign=Zapraszamy+do+s%C5%82uchania+naszego+podkastu+Pisanie+zdystansowane+300+tys+nowych+tytu%C5%82%C3%B3w+miesi%C4%99cznie+Algorytmiczne+fikcje+literackie+25+bada%C5%84+na+25-lecie+Wikipedii
published: 2026-05-17T00:00:00.000Z
created: 2026-06-14T00:00:00.000Z
tags:
  - LLM
  - trendy-AI
---


Czy duże modele językowe mogą służyć jako generatory treści reprezentujących kultury, społeczności i okresy historyczne, dla których nie mamy dużych zbiorów oryginalnych źródeł, i to dzięki umiejętnemu wykorzystaniu ich ograniczeń?

> W zeszłym tygodniu w Operze Królewskiej w Pałacu Wersalskim miała miejsce premiera komedii w trzech aktach pod tytułem “L’Astrologue ou les Faux Présages” (“Astrolog, czyli fałszywe znaki”). Ta dwugodzinna sztuka opowiada historię zamożnego paryskiego mieszczanina, który pod wpływem sugestii astrologa-szarlatana o imieniu Pseudoramus stara się doprowadzić do tego, żeby jego córka Lucile poślubiła starszego od niej, zadłużonego perukarza.

Przedstawienie na Wersalu było efektem projektu [Molière Ex Machina](https://www.sorbonne-universite.fr/en/news/moliere-ex-machina-when-ai-lends-its-pen-17th-century). Grupa lingwistów, literaturoznawców i historyków z Sorbony pracowała z konwersacyjną AI, określaną jako *Le Chat*. Użyty model dotrenowany został na XVII-wiecznych tekstach z epoki i fragmentach sztuk Moliera. Praca nad nową sztuką miała mieć postać "intelektualnego ping-ponga" - każda scena była przepisywana nawet kilkanaście razy, a badacze nieustannie poprawiali propozycje modelu. Do projektowania kostiumów wykorzystano model wizualny, trenowany na szkicach [Henriego de Gissey](https://en.wikipedia.org/wiki/Henri_de_Gissey), twórcy strojów dla dworu Ludwika XIV.

“Sztuka nie tyle pisana przez AI, co współtworzona przez AI” - [tłumaczyli](https://www.theguardian.com/stage/2026/may/11/moliere-ex-machina-ai-create-new-work-france-equivalent-shakespeare) badacze. "Celem projektu jest demistyfikacja AI i pokazanie, jak można ją wykorzystać w sensowny i rozważny sposób, jeśli tylko korzysta się z ludzkiej wiedzy i AI jest przez nią kierowana i inspirowana". W jednej z recenzji czytamy, że wkład AI był "uderzający, niemal niepokojący", ale dialogi "całkowicie wiarygodne".

**Model jako archiwum**

Molière Ex Machina to ciekawe wykorzystanie modelu językowego jako pewnej reprezentacji rzeczywistości tekstowej. Wydaje się, że podstawą wartości sztuki “Astrolog, czyli fałszywe znaki” (w końcu widzom się podobała!) jest intensywna praca jej twórców i kreatywne wykorzystanie modelu jako reprezentacji właśnie: mniej czerpano tu z jego zdolności do generowania tekstu, więcej ze zdolności do oddania uśrednionego stylu Moliera i literatury francuskiej z epoki. Pisałem już [o podobnym użyciu](https://blog.humanistyka.dev/2026/05/vintage-large-language-models-nowe-narzedzia-badania-historii-intelektualnej) w kontekście badań nad historią intelektualną. Wykorzystanie modeli przede wszystkim jako reprezentacji, a nie jako generatora, to podstawa idącej nieco dalej propozycji, jaką składa Wael Hassan Nasr Youssef Ashry, egipski badacz literatury światowej z Uniwersytetu Port Said.

W preprincie "Synthesizing The Past: Technical Challenges And Aesthetic Possibilities Of Ai-Generated Historical Narratives In World Literature" (SSRN: [6528518](https://ssrn.com/abstract=6528518), 2026) autor proponuje nową metodę badań kultury, będącą syntezą tekstów [literatury światowej](https://en.wikipedia.org/wiki/World_literature) z maszynowo generowanymi treściami.

Nie chodzi tu jednak o proste uzupełnienie luk w zbiorach i tekstach, które chcielibyśmy badać, żeby złapać globalną perspektywę na interesujące nas wątki. Po pierwsze, fundamentalną rolę mają pełnić w tym planie eksperci i ekspertki ([Human in the Loop](https://en.wikipedia.org/wiki/Human-in-the-loop)), ograniczający autonomię narzędzi AI, a osoby reprezentujące lokalne kultury i społeczności koordynować miałyby gromadzenie danych treningowych i dbać o kierunek rozwoju modeli, będących w założeniu open source. Po drugie, błędy i halucynacje obecne w generowanych treściach mają być specjalnie oznaczane, tak aby ograniczenia modeli inspirowały do krytycznej refleksji nad narracjami o kulturze. Błędy i uproszczenia modeli miałyby być nie tyle problemem, ale potencjalnym źródłem wartości. Generowanie treści miałoby być też dokumentowane co do użytych oryginalnych źródeł.

Zobaczmy, jak mogłoby to wyglądać w praktyce.

**Jeanne z Lyonu**

W latach 1831 i 1834 tkacze i tkaczki zakładów jedwabniczych w Lyonie [występowali zbrojnie w obronie swoich interesów](https://pl.wikipedia.org/wiki/Powstania_tkaczy_w_Lyonie), przeciwko uderzającym w rodzący się ruch robotniczy zmianom w prawie oraz wobec ograniczania praw politycznych w państwie Ludwika Filipa. Jak pisze autor omawianego opracowania, mamy do dyspozycji pewne dane historyczne dotyczące społeczności robotników tego miasta, centrum życia gospodarczego ówczesnej Francji. Dostępne są dane takie jak wskaźniki śmiertelności, wiek zawierania małżeństw, ale też ceny jedwabiu czy liczby krosen. Skorzystać możemy też z raportów policyjnych, identyfikujących poszczególnych przywódców powstań. Brakuje jednak - zauważa Wael Hassan Nasr Youssef Ashry - przekazów o życiu codziennym tkaczy: *o tym, co jedli, jak spali, jak rozmawiali z dziećmi i o czym śnili*. Taką wiedzę dałyby nam źródła narracyjne (choćby pamiętniki), tych niestety nie mamy z oczywistych względów.

Lukę tę uzupełniać miałyby więc generatywne narracje. Na podstawie dostępnych danych statystycznych oraz innych źródeł z epoki, moglibyśmy wytworzyć syntetyczne źródła, przy czym to, co zostałoby wypracowane

> nie jest prawdziwą biografią (dana osoba nigdy nie istniała), lecz typologiczną fikcją: narracją ucieleśniającą typowe doświadczenie pewnej grupy, bez roszczenia do dokumentalnej ścisłości. Jest to estetyczny odpowiednik socjologicznego typu idealnego: nie fotografia, lecz portret, nie indeks, ale ikona.

Na podstawie źródłowych danych statystycznych model mógłby wytwarzać prawdopodobne, ale fikcyjne biografie.

> Jeanne, lat 32, matka czworga dzieci, wstaje o czwartej rano, by przygotować krosno. Jej dłonie są poplamione barwnikiem, którego nie da się zmyć. Nuci piosenkę, pieśń z czasów ostatniego powstania, której nauczyła ją matka, choć nie potrafi już przypomnieć sobie słów…

Tego typu materiał nie byłby źródłem, ale algorytmiczną fikcją literacką (algorithmic historical fiction):

> jej prawda nie ma charakteru faktograficznego, lecz typologiczny: oddaje strukturę życia, jakie prowadziły tysiące ludzi, nawet jeśli żadna konkretna Jeanne nigdy nie istniała.

**Literackie podejście do historii**

Z punktu widzenia praktyki historycznej propozycja algorytmicznej fikcji literackiej nie może być zaakceptowana - prowadzenie badań i proponowanie interpretacji na podstawie wygenerowanych (nawet jeśli prawdopodobnych) źródeł przypominałoby badanie przeszłości na podstawie fabularnych filmów historycznych. Oczywiście w badaniach używać możemy tekstów literackich (czy też filmów z epoki), nie jest to jednak nigdy proste sięgnięcie po nieprzetworzoną wiedzę, bez zwracania uwagi na cechy gatunkowe czy okoliczności powstania danego dzieła.

Wael Hassan Nasr Youssef Ashry proponuje nie tyle faktograficzne, ile literackie podejście do historii. Algorytmiczne fikcje nigdy nie będą źródłem wiedzy i faktów, ale to nie jest ich rola. Mają przede wszystkim narzędziem budowania empatii, *wczuwania się* w historię, która nie pozostawiła za sobą źródeł, przypominać o tym, że anonimowi aktorzy wielkich wydarzeń historycznych mieli swoje biografie. To działanie tożsame z budowaniem alternatywnego archiwum i rozwijaniem [przeciw-pamięci](https://cbh.pan.pl/pl/przeciw-pami%C4%99%C4%87) (*contre-mémoire*).

**Bez pytań o fakty**

Omawiana praca dostępna jest na razie w postaci preprintu. Być może dopiero opublikowanie jej (po recenzjach) w dobrym czasopiśmie pozwoli bardziej zaufać propozycji autora. Bardzo sceptycznie podchodzę do tej koncepcji, obawiając się przede wszystkim niebezpieczeństwa zrównywania generatywnych fikcji z autentycznymi źródłami. Kluczowe mogą być też kwestie etyczne: jakie prawo mamy do występowania w imieniu ludzi, którzy nie pozostawili po sobie żadnych przekazów? Czy generując źródła w ich imieniu nie nadużywamy naszej pozycji? Łatwość w tworzeniu algorytmicznej fikcji literackiej może też negatywnie wpływać na poszukiwania autentycznych źródeł - skoro mielibyśmy interesujący materiał już po kilku kliknięciach, pójście do archiwum mogłoby wydawać się stratą czasu.

To, co interesuje mnie w tej propozycji, to pewne techniczne ujęcie modeli językowych. Tak jak [pisałem już wcześniej](https://blog.humanistyka.dev/2026/05/vintage-large-language-models-nowe-narzedzia-badania-historii-intelektualnej), możemy je traktować jako pewną postać archiwum, reprezentację (z konieczności ograniczoną i sformatowaną) pewnej rzeczywistości tekstowej. Wagi modelu można uznać za jakąś formę przechowywania wiedzy dostępnej w treściach treningowych, a sposób pracy z modelami daje nam nowe możliwości zadawania pytań. Jest jednak oczywiste, że nigdy nie mogą to być pytania o fakty.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).
