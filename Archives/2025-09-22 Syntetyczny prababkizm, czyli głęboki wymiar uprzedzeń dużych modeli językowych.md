---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2025/09/syntetyczny-prababkizm-czyli-gleboki-wymiar-uprzedzen-duzych-modeli-jezykowych"
published: 2025-09-22
created: 2026-06-14
tags:
  - "LLM"
  - "trendy-AI"
  - "strategia-AI"
---


Czy fikcje w całości generowane przez duże modele językowe mogą nawiązywać do tradycji narodowych i uwzględniać rzeczywistość poszczególnych krajów? Aby to sprawdzić, badacze z Uniwersytetu w Bergen wygenerowali i przeanalizowali niemal 12 tys. opowiadań, przedstawiających historie dla 236 krajów, w tym dla Polski.

Wiemy to aż za dobrze, że wytwory sztucznej inteligencji, które chcemy z jakiegoś powodu analizować jako teksty kultury, mają w sobie pewną niepokojącą generyczność i ogólność. Badanie Jill Walker Rettberg i Hermanna Wigersa (DOI: [10.48550/arXiv.2507.22445](https://doi.org/10.48550/arXiv.2507.22445), 2025) pokazuje, że w dużych modelach językowych ta niepokojąca cecha ujawnia się nie tylko w proponowanych nam nazwach własnych czy użytym języku, nawet jeśli różni się on w zależności od gatunku tekstu. Ta wada LLM-ów zaszyta jest w samej strukturze narracji i propozycjach fabularnych w wytwarzanych przez nich tekstach.

Jak to zbadano? Za pomocą modelu `gpt-4o-mini` postanowiono wygenerować po 50 opowiadań, charakterystycznych dla 236 krajów (w tym Tajwanu i Palestyny), zidentyfikowanych na liście Urzędu Statystycznego Norwegii, o ile tylko mieszkańcy tych krajów posiadali własny demonim. Z listy wypadli mieszkańcy Wyspy Heard czy Wysp McDonalda, bo o ile w ogóle istnieją, nie doczekali się jeszcze właściwego im określenia.

W pracy z modelem użyto prompt, w którym wskazywano nazwę własną (demonim) danej narodowości, np:

> Write a 1500 word potential *Polish* story

Użycie słowa *potential* było zabezpieczeniem przed generowaniem tekstów będących prostym podsumowaniem istniejących już fabuł, o których model *mógł mieć wiedzę*. Dodatkowo wygenerowano też 50 historii bez wskazania demonimu, żeby zebrać materiał porównawczy.

Wygenerowanie pół setki opowiadań dla 236 demonimów dało zbiór liczący 11800 tekstów. 20 milionów słów, zestawionych przez `gpt-4o-mini`, nie dało się oczywiście sprawdzić w trybie uważnego czytania (close reading). Trzeba było zrobić to maszynowo, pozostawiając jedynie niewielki zbiór do ręcznego przejrzenia i oceny (historie norweskie, amerykańskie, palestyńskie i izraelskie):

> po pierwszych dziesięciu opowieściach z każdego kraju osiągnęliśmy punkt nasycenia, w którym powtarzały się te same typy treści.

**Szumiące sosny z Andory**

Maszynowe analizy robiono w Pythonie, cały kod, dane źródłowe i wynikowe dostępne są na [GitHubie](https://github.com/AI-STORIES-ERC/GPT_stories), Zenodo ([10.5281/zenodo.14939000](https://doi.org/10.5281/zenodo.14939000)) i Dataverse [10.18710/VM2K4O](https://doi.org/10.18710/VM2K4O).

Po wygenerowaniu opowiadań, znów skorzystano z `gpt-4o-mini`, aby wyodrębnić z nich głównego bohatera/bohaterkę oraz to, jak jest identyfikowany. Użyto następującego prompta, podając jako kontekst treść wygenerowanej wcześniej historii:

> Identify the name of the main character and only the name of the main character within this story: {STORY}”

Przeprowadzono też analizę sentymentu za pomocą modelu `distilbert-base-uncased-emotion` (dostępnego na [Hugging Face](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion)). Model ten ma jednak spore ograniczenia kontekstu - jest w stanie poddać analizie 300-400 słów (około 512 tokenów), dlatego wszystkie opowiadania przetworzono - znów za pomocą `gpt-4o-mini` - na streszczenia w języku angielskim o objętości 50 słów.

Standardowymi narzędziami przetwarzania języka naturalnego dla Pythona (`spaCy, TextBlob`) sprowadzono wszystkie słowa do form podstawowych, usunięto *stop words* i policzono frekwencję. Użycie `TextBlob` pozwoliło wyznaczyć wszystkie frazy rzeczownikowe i zbadać ich popularność - np. fraza *szumiące sosny* najczęściej pojawiała się w opowiadaniach generowanych dla Andory.

> Zapoznaliśmy się z danymi, korzystając z szeregu strategii obliczeniowych: wizualizując częstość występowania słów w różnych krajach i regionach, używając wizualizacji analizy sentymentu do identyfikacji krajów o nietypowych nastrojach, a także wgrywając pliki CSV z opowieściami z różnych krajów do ChatGPT i prosząc go o przygotowanie wizualizacji lub zasugerowanie strategii analizy.

Zliczenie częstości słów we wszystkich opowieściach sugeruje, jak piszą badacze, że proza generowana w ChatGPT jest nieco *cukierkowa* (saccharine):

> najczęściej występującym słowem jest *serce* a tuż za nim *opowieść*, *uczucie/odczuwać*, *duch*, *wioska*, *dzielić się* i *głos*.

Okazuje się, że podobny charakter mają generowane w ChatGPT teksty poetyckie, o czym pisze Melanie Walsh i współautorki ([10.48550/arXiv.2410.15299](https://doi.org/10.48550/arXiv.2410.15299), 2024).

![Chmura słów kluczowych wygenerowanych z korpusu tekstów](https://blog.humanistyka.dev/content/images/20250922170840-wck4234_min.png)

Wyniki analizy sentymentu nie zostały szeroko wykorzystane w badaniu, użyto je głównie do wyznaczania historii, które mogłyby odbiegać od standardowego wzorca.

**Fałszywa globalność**

Cechy opowiadań, wyznaczane na podstawie słów, były dla badaczy jednak mniej istotne niż ogólne schematy fabularne. Jak czytamy w opracowaniu,

> generatywna AI domyślnie odwołuje się do bardzo określonego schematu fabularnego, w którym rozwiązanie problemu następuje poprzez to, że bohater / bohaterka przywraca utracone tradycje i wspólnotę w małych miasteczkach i wsiach.

Fabuły proponowane przez `gpt-4o-mini` okazują się być podobnie sformatowane jak *gatunki narracji korporacyjnych* (corporate storytelling genres ), takie jak np. filmy romantyczne z kanału Hallmark.

> Oto amerykańska opowieść według modelu generatywnej AI OpenAI gpt-4o-mini: kobieta wraca do swojego małego rodzinnego miasteczka po kilku stresujących latach pracy w wielkim mieście. Spotyka przyjaciela z dzieciństwa albo starszego sąsiada, który opowiada jej o problemie: mieszkańcy stracili więź ze swoją historią, ludzie wyjeżdżają, panuje susza albo deweloper chce zburzyć stare budynki. Bohaterka organizuje wydarzenie społecznościowe, które ożywia wspólnotę i pozwala jej stawić czoła wyzwaniu. Historia kończy się decyzją kobiety, by pozostać w rodzinnym miasteczku i pracować jako artystka/pisarka/animatorka społeczna zamiast wracać do zabieganego życia w wielkim mieście.

Czasem bohaterem w takim generycznym opowiadaniu jest dziecko, mężczyzna albo babcia. Protagonista może gromadzić historie mieszkańców, organizować ogrody społeczne czy remontować opuszczoną stację kolejową, tworząc centrum kultury. W każdej z tych amerykańskich opowieści bohater ożywia prowincję i budzi dumę w lokalnej społeczności.

Opowiadania generowane dla krajów europejskich mają podobny schemat, wypełniają je jednak elementy nadprzyrodzone:

> W norweskich historiach młode dziewczyny z małych wiosek, które często właśnie wróciły z wielkiego miasta, wędrują do lasu i spotykają duchy. Duchy mówią im, że wiosce/naturze/społeczności grozi niebezpieczeństwo, wynikające z braku równowagi między ludźmi a naturą, z działań deweloperów albo z nadciągających ekstremalnych zjawisk pogodowych. W większości tych historii bohaterki rozwiązują problem, organizując wspólnotę, podobnie jak w amerykańskich opowieściach.

Podobnie w opowiadaniu wytworzonym dla Ghany, młodzi ludzie zapomnieli o tradycjach, “pochłonięci przez smartfony i urok miasta”. Wobec bezsilności starszyzny młody bohater organizuje festiwal i ożywia lokalną tradycję, ucząc wszystkich dawnych tańców. W niektórych indyjskich opowieściach celem bohatera nie jest uzdrowienie wioski, ale jej opuszczenie w celu znalezienia wykształcenia, chociaż to nie wyklucza późniejszego powrotu i odbudowy społeczności.

**Od fiordu do *Frozen***

Prawie 12 tys. historii wygenerowanych przez `gpt-4o-mini` różni więc nie tyle fabuła, ale symbole i klisze, które model stosuje, odwołując się do tradycji i kontekstu danego kraju. Oto jeśli Norwegia, to fiordy, jeśli drzewa oliwne, to Izrael i Palestyna:

> Do tego właśnie LLM-y nadają się najlepiej: modelują dane treningowe, identyfikując słowa i pojęcia, które często współwystępują, takie jak *fjord* i *Norwegia*. Te współwystąpienia lub skojarzenia są modelowane jako wektory (wyobraźmy sobie strzałkę od *fjord* do *Norwegia*) w tzw. przestrzeni semantycznej modelu, przestrzeni ukrytej albo przestrzeni wektorowej. Model ma miliardy wektorów w miliardach wymiarów, więc *fjord* wskazuje nie tylko na Norwegię, lecz także na *wodę* i *głęboki*. Jeśli większość danych treningowych pochodzi z USA, model prawdopodobnie skojarzy *fjord* także z Elsą i Anną z filmu *Frozen* oraz z „rejsami wycieczkowymi”, z powodu setek stron internetowych reklamujących takie rejsy amerykańskim turystom. Natomiast model wytrenowany na lokalnej gazecie z miasteczka nad fiordem raczej nie wspomniałby o filmie Disneya, ale kojarzyłby fiord z transportem, mostem, promem, turystami, fabryką i rybołówstwem.

Wartość omawianego badania nie leży w wyodrębnieniu generycznego schematu opowiadania, ale w pokazaniu, że skojarzenia modelu OpenAI z większością krajów mają charakter **zewnętrzny**. Duży model językowy, często przedstawiany jako globalny (międzynarodowy), a więc obejmujący wszystkie kultury i konteksty, jest tak naprawdę sprofilowany. Jego stronniczość wynika z danych treningowych, pozyskiwanych głównie z krajów Zachodu i przemysłu kulturalnego. Stąd *fiord* kojarzony jest statystycznie raczej z *Frozen* niż mostami czy hodowlą łososia. Model, chociaż wytrenowany na tekstach tworzonych przez człowieka, nie jest - jak czytamy - ekspresją kolektywnej wyobraźni, ale modelowaniem specyficznego, wyselekcjonowanego i zamkniętego zbioru tekstów.

Spróbujmy rozpoznać tę stronniczość `gpt-4o-mini` wobec polskiej kultury i tradycji literackiej. Teksty i dane dla Polski [znaleźć można na GitHubie](https://github.com/AI-STORIES-ERC/GPT_stories/tree/main/data/PL).

**Syntetyczny prababkizm**

Ponieważ też nie chciało mi się czytać wszystkich 50 opowiadań, wykorzystałem Google Gemini do podsumowania ich streszczeń, dostępnych [tutaj](https://github.com/AI-STORIES-ERC/GPT_stories/blob/v1.0.1/data/PL/PL_summaries.csv):

> Historie te często łączą elementy magicznego realizmu, folkloru i osobistych poszukiwań, osadzone w polskich sceneriach, takich jak Puszcza Białowieska, Kraków czy mazowieckie wioski. Wiele opowieści koncentruje się na postaciach, które odkrywają swoje dziedzictwo, podejmując się ochrony natury, przekazywania historii przodków lub inspirowania społeczności.

Kluczowe wątki można automatycznie zestawić w tabeli:

| Wątek | Opis | Przykładowe historie |
| --- | --- | --- |
| Ochrona natury | Bohaterowie odkrywają magiczne połączenie z przyrodą i podejmują się walki o jej przetrwanie przed zagrożeniami. Często są to botanicy lub młodzi odkrywcy, którzy współpracują z mistycznymi istotami, takimi jak strażnicy lasu czy nimfy. | PL\_1, PL\_49, PL\_50 |
| Dziedzictwo przodków | Historie skupiają się na odkrywaniu ukrytej historii rodzinnej i tradycji. Postacie poznają swoje korzenie, często za pomocą magicznych artefaktów lub istot, i uczą się, jak ważne jest przekazywanie tych opowieści kolejnym pokoleniom. | PL\_2, PL\_4, PL\_48 |
| Poszukiwanie tożsamości i odwaga | Młodzi bohaterowie wyruszają w fantastyczne podróże, aby stawić czoła swoim lękom i odkryć swoją prawdziwą siłę. Ich doświadczenia prowadzą do głębokiej przemiany, inspirując innych. | PL\_3 |
| Wspólnota i jedność | Pojedynczy bohater inicjuje zmiany, które zjednoczą całą społeczność. Poprzez dzielenie się historiami, organizowanie działań lub po prostu przypominanie o wspólnych wartościach, budują poczucie wspólnoty i wzajemnego wsparcia. | PL\_1, PL\_48, PL\_49 |

Czy w *polskich* tekstach widać tę stronniczość, o której wspominają autorzy opracowania? Czy są tam owe zewnętrzne skojarzenia, które wcześniej widzieliśmy na przykładzie *fiordu* i *Frozen*?

Bohaterką opowiadania PL\_45 jest Zofia Kowalska. *Po dekadzie spędzonej na zatłoczonych ulicach Warszawy* przyjeżdża do wioski, w której mieszkała jej niedawno zmarła babcia. Odkrywa tam *zbiór listów związanych pożółkłą wstążką*, wysyłanych przez Jakuba Nowaka, *młodego i utalentowanego artystę, \[który\] zdobył serce babci w samym środku chaosu wojny*, ale został powołany na front w 1944 i *zginął wkrótce po zakończeniu wojny*.

Ten straszny slop, który niepokojąco nawiązuje do powieści z nurtu powrotów na prowinicję czy odkrywania własnej chłopskiej przeszłości, jest pozbawiony wszelkich odniesień do polskiej rzeczywistości historycznej. Oto młody i utalentowany artysta z małej wsi (jak się tam znalazł?), maluje z przyjaciółmi obrazy w opuszczonym młynie, chociaż kraj jest pod okupacją i brakuje wszystkiego. Utalentowany biedny artysta to klisza, która mogła z powodzeniem zmieścić się w generycznym opowiadaniu ze Stanów z czasu pokoju, ale w polskiej rzeczywistości okupacyjnej jest raczej nie do pomyślenia. Model zignorował jednak ten kontekst i połączył dwie, raczej niemożliwe do połączenia ze sobą elementy. Takich błędów należałoby poszukać także w innych tekstach (do czego serdecznie zachęcam).

Badacze, analizujący cały korpus danych, zauważyli, że model pomija przemoc i radykalne tematy w generowanych przez siebie narracjach. Może to wynikać zarówno ze specyficznego wyboru danych treningowych, jak i celowego filtrowania i cenzury treści podczas trenowania, tak aby uniknąć sytuacji, w której odpowiedź modelu może podżegać do przemocy. Konsekwencją tego jest jednak wyczyszczenie generowanych fabuł z wątków przemocowych, historycznie przecież obecnych w doświadczeniach wielu krajów.

**Cechy literackiego slopu**

Literackie slopy, które wygenerowano do badania, charakteryzują się powierzchowną narracją (surface narration), są spójne na poziomie zdań i słów, ale brakuje im głębi fabularnej. Postaci nie są dynamiczne, nie podlegają zmianom, podobnie się ma ze społecznościami, wobec których podejmują działania. Brakuje wątków miłosnych, być może także z powodu nałożenia pewnych ograniczeń podczas trenowania modelu. Fabuła opowiadań preferuje stabilność (czy powrót do stabilności) nad zmianę i nostalgię nad innowacją, a szczegóły świata przedstawionego budowane są na podstawie stereotypów (model *widzi* dany kraj czy region jakby z zewnątrz, nie zna kontekstu lokalnego).

Badacze opisują te slopy, odwołując się do koncepcji syntetycznego imaginarium (synthetic imaginaries). Właśnie “syntetyczne” a nie “kolektywne”, ponieważ model nie reprezentuje wszystkich kultur, a jedynie interpretuje je w sposób scentralizowany i generyczny. Ostatecznie, wraz z modelem językowym nie dostajemy reprezentacji wszystkich tekstów, użytych do jego wytrenowania, ale uogólnione statystycznie, wyobrażone ich wersje, które zależą od dominacji pewnych wątków czy słów w danych treningowych. Efektem tego jest homogenizacja narracyjna - wystarczy podmienić nazwy własne, żeby teksty generowane dla Polski były nie do odróżnienia od tekstów dla Andory.

Jakie są wnioski z badania dla osób, które chciałyby wykorzystywać LLM-y w pracy literackiej? Źródłem kreatywności nie może być sam model, ale to, jak autor konfrontuje jego syntetyczne imaginarium z własnym doświadczeniem, stylem i wiedzą. Aby uniknąć homogenizacji warto traktować je wyłącznie jako narzędzie warsztatowe albo liczyć [na potencjał jego błędów](https://blog.humanistyka.dev/2025/07/poezja-bez-ryzyka-to-tylko-skladnia-dlaczego-chatgpt-nie-sprawdzi-sie-w-tworzeniu-poezji).

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).