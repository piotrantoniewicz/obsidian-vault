---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2026/06/banalny-nacjonalizm-i-duze-modele-jezykowe-jako-miejsca-pamieci?utm_source=newsletter"
published: 2026-06-25
created: 2026-08-05
tags:
  - "LLM"
  - "framing"
  - "trendy-AI"
---


Kto wynalazł telefon - Bell czy Meucci? Odpowiedzi dużych modeli językowych różnią się w zależności od języka zapytania, nawet jeśli pytanie dotyczy tego samego zagadnienia. Rozpoznanie “wewnątrzjęzykowej przewagi” danych postaci względem innych pozwoliło autorom omawianej pracy opisać LLM-y jako przestrzenie, w których ujawniać się mogą narodowe “miejsca pamięci” (w myśl koncepcji Pierre’a Nory).

Publikowałem już na blogu notki, opisujące badania, w perspektywie których duże modele językowe interesujące są przede wszystkim jako pewne reprezentacje języka, kultury czy historii, a nie narzędzia generatywne (były to m.in. badania [zmian semantycznych pojęć](https://blog.humanistyka.dev/2026/06/relacja-ma-znaczenie-od-firtha-do-wektorowych-reprezentacji-jezyka), propozycje [symulowania nieistniejących źródeł historycznych](https://blog.humanistyka.dev/2026/05/nie-fotografie-ale-portrety-algorytmiczne-fikcje-literackie) czy [nowego spojrzenia na historię intelektualną](https://blog.humanistyka.dev/2026/05/vintage-large-language-models-nowe-narzedzia-badania-historii-intelektualnej)). W takim ujęciu, co ważne, dobrze znane ograniczenia LLM-ów (stronniczość czy generyczność) nie są wcale przeszkodą - można je nawet wykorzystać jako punkt zaczepienia w analizie modelu jako reprezentacji!

Interesujący przykład znajdziemy w opublikowanym kilka dni temu preprincie *Same question, different history: language, national identity, and credit in large language models* (DOI: [10.48550/arXiv.2606.23164](https://doi.org/10.48550/arXiv.2606.23164), 2026). Stronniczość w wiedzy modeli językowych, wynikająca oczywiście z tekstów treningowych w językach narodowych, jest dla autorów - tak! - miejscem pamięci (*lieu de mémoire*) w myśl [propozycji Pierre'a Nory](https://en.wikipedia.org/wiki/Lieu_de_m%C3%A9moire). Wiedzą, wobec której ujawniać się mają w modelach miejsca pamięci, są tutaj fakty dotyczące znanych wynalazców (*wynalazców*, bo wszystkie 49 postaci wymienianych w promptach wysyłanych do modeli to mężczyźni).

Pomysł na badanie jest prosty. Kto wynalazł radio - Rosjanin Popow czy Włoch Marconi? Czy skonstruowanie telefonu było osiągnięciem Bella (USA), czy Meucciego (Włochy)? Do kogo należy pierwszeństwo w wynalezieniu ruchomej czcionki - do Bi Shenga (X-XI w. w Chinach) czy do Gutenberga (XV w. w Niemczech)? Wybór tej a nie innej osoby może wynikać z narodowej dumy i uprzedzeń - jeśli jest ona wyrażana przez dane treningowe, to modele łatwo ją powielą.

Jak widać, nie interesuje nas tu w ogóle *kreatywność* modeli czy ich zdolność do tworzenia logicznych wypowiedzi. Szukamy raczej głęboko ukrytych uprzedzeń, które ujawniają się na poziomie odpowiedzi na wysyłane prompty i mogą świadczyć o istnieniu określonych miejsc pamięci w kulturach narodowych.

Jak jednak wyodrębnić tę stronniczość i zdefiniować narodowe miejsca pamięci uobecniające się w modelach? Autorzy omawianego tekstu przygotowali listę wynalazców i naukowców oraz związanych z nimi wynalazków i odkryć. Prompty wyrażały pytania otwarte (*kto wynalazł X?*) i porównawcze (*kto wynalazł X: A czy B?*) na temat 21 wynalazków i odkryć. Wysłano do jedenastu modeli, rozwijanych w trzech regionach: USA (m.in. GPT-4o, Claude, Gemini), Chiny (np. DeepSeek, Qwen) i Europa (Mistral). Zredagowano je w dwunastu językach: duńskim, niemieckim, angielskim, francuskim, hindi, włoskim, koreańskim, portugalskim, rumuńskim, rosyjskim, szwedzkim oraz chińskim. Ten sam badany model, po otrzymaniu tych samych pytań, ale wyrażonych w różnych językach, mógł wskazywać lub pomijać wybrane postaci wynalazców i uczonych.

**Kto wynalazł ruchomą czcionkę?**

Zobaczmy wyniki dla postaci Bi Shenga. Wyrażone w języku chińskim pytanie o wynalazcę ruchomej czcionki wygeneruje w przypadku każdego testowanego modelu odpowiedź ze wskazaniem na niego (98 proc.). Jeśli to pytanie zadamy w innym języku z puli badawczej, wskazania będą wciąż częste, ale już nie tak często (79 proc.). Różnica wynosząca 19 p.p. wskazywać ma na istnienie miejsca pamięci. Pamiętajmy przy tym, że wśród jedenastu modeli wykorzystanych w badaniu pięć zostało opracowanych w Chinach.

Profilowanie wiedzy modelu przez język zapytania daje - jak piszą autorzy opracowania - *wewnątrzjęzykową przewagę* (*in-language advantage*) dla Bi Shenga w porównaniu z innymi językami. Oczywiście, nie ma w tym żadnej intencjonalności - modele są trenowane na tekstach w różnych językach narodowych i odtwarzają statystyczne korelacje w nich występujące, np. w tekstach chińskich w kontekście ruchomej czcionki Bi Sheng może być częściej wspominany wraz z Gutenbergiem niż w tekstach w innych językach. Sam Gutenberg wymieniany jest w 81 proc. odpowiedzi, kiedy pytanie zostaje zadane w języku niemieckim. W odpowiedzi na pytania wyrażone w pozostałych językach, jego nazwisko pojawia się średnio w 76 proc. przypadków.

Podobnie, wewnątrzjęzykowa przewaga obserwowana jest w przypadku wynalazców radia. Oto Aleksandr Popow wymieniany jest w 48 proc. odpowiedzi, kiedy pytanie zadawane jest w języku innym niż rosyjski. Dla promptu napisanego po rosyjsku jego nazwisko pojawi się już 85 proc. przypadków. Co ciekawe, Guglielmo Marconi wymieniany jest w tym kontekście niemal zawsze, nawet jeśli pytanie zadawane jest po rosyjsku - modele rzadko podawały tylko jedno nazwisko w przypadku spornych wynalazków (dla pytań o radio prawie zawsze podawały więcej niż jedno nazwisko).

![enter image description here](https://blog.humanistyka.dev/content/images/20260625215028-fa2d1eb190a17c97e34204902da39bbd30658fbbb259e54dce9ce9364a8409e1.png) Wskaźnik pojawiania się wybranych postaci w pytaniach na temat wynalazków, w zależności od języka zapytania. Źródło: *Same question, different history: language, national identity, and credit in large language models* (DOI: [10.48550/arXiv.2606.23164](https://doi.org/10.48550/arXiv.2606.23164), 2026)

Marconi należy do grupy wynalazców, którzy w badanych modelach, niezależnie od języka promptu, uzyskali uniwersalny status. Podobnie jak Newton, Bell czy bracia Wright w korpusach treningowych są nierozerwalnie związani z frazami opisującymi wybrane wynalazki i odkrycia, dlatego

> postaci o niższym statusie \[mniej znani - MW\], nieanglojęzyczni są wymieniani wyraźnie częściej w powiązanym z nimi języku, podczas gdy globalnie rozpoznawane w zachodniej kulturze postaci wymieniane są z częstością na poziomie bliskim maksimum niezależnie od języka.

**Ślad instytucjonalny i jego odbicie w wiedzy modelu**

Oczywiście narodowe znaczenie postaci historycznych nie bazuje wyłącznie na ich obecności w tekstach. Teksty są jednak odbiciem tego, jak w poszczególnych kulturach buduje się znaczenie wynalazców i odkrywców. Przykładowo, jeśli Bi Sheng miałby zacząć pojawiać się częściej w niechińskich tekstach poświęconych wynalazkowi druku, jego postać powinna być wspominana w podręcznikach historycznych, w przewodnikach po muzeach, trafić na pomniki itp. Ponieważ wiedza modeli językowych bazuje na tekstach, to one są pośrednikiem, za pomocą którego podkreślać można (lub umniejszać) niektóre postaci czy wątki historyczne.

Autorzy opracowania postanowili zbadać korelację między określanym liczbowo na podstawie ośmiu kryteriów *śladem instytucjonalnym* (*institutional footprint*) danej osoby dla danego kraju. Kryteriami, na podstawie których przyznawano punkty, było obchodzenie świąt narodowych poświęconych tej postaci, obecność jej wizerunków na banknotach i znaczkach pocztowych, istnienie pomników i muzeów jej poświęconych, a nawet nazywanie jej nazwiskiem ulic i miejsc publicznych. Okazało się (trudno też się temu dziwić), że im bardziej intensywnie dana postać upamiętniana jest w swoim kraju, tym większa szansa, że model przywoła jej nazwisko, szczególnie jeśli zada się pytanie w jej ojczystym języku.

Oczywiście odpytywane w badaniu modele nie informowały, że proponowane nazwiska są specyficzne dla danego kręgu językowego. Wzrost widoczności, wynikający z instytucjonalnych form upamiętnienia, przekłada się na wiedzę modelu i kształt odpowiedzi. Zdaniem autorów opracowania w taki sposób ujawniać się ma [banalny nacjonalizm](https://pl.wikipedia.org/wiki/Nacjonalizm_banalny) (*banal nationalism*).

**Duże modele i banalny nacjonalizm**

Pojęcie to zaproponował brytyjski socjolog Michael Billig. Banalny nacjonalizm to rutynowe, popularne, niekoniecznie instytucjonalne i niemal niezauważalne przywoływanie narodu i identyfikowanie się jako naród w codziennym życiu. Jego przykładem jest kibicowanie narodowej drużynie piłki nożnej, używanie flag i symboli narodowych w przestrzeni domowej i publicznej, promocja narodowej tradycji kulinarnej, a nawet napisy "Made in..." na rozmaitych produktach. Omawiane badanie ujawniło, że duże modele językowe, trenowane na tekstach w językach narodowych, powielają zawarte w nich wzorce i przypisują atrybucję wynalazków zgodnie z preferencjami wynikającymi z perspektywy narodowej, przez co właśnie współkształtują banalny nacjonalizm.

*Same question, different history: language, national identity, and credit in large language models* (DOI: [10.48550/arXiv.2606.23164](https://doi.org/10.48550/arXiv.2606.23164), 2026) to ciekawe opracowanie problemu przenoszenia schematów i uprzedzeń z lokalnego charakteru danych treningowych na uniwersalnie przecież wykorzystywane modele językowe. Modele traktowane są tutaj jako pewne reprezentacje kultury czy pamięci poszczególnych narodów, a benchmark pozwala uchwycić pewne ich cechy. Z powodzeniem można wyobrazić sobie podobne badanie, które na podstawie analizy wiedzy modeli opisałoby sprzeczne interpretacje wybranych faktów historycznych czy nawet cechy kanonu literatur narodowych. Oczywiście, projektując takie badania, pamiętać należy, że teksty powstałe w określonym kręgu kulturowym, będące podstawą danych treningowych, nigdy nie są obiektywne - powstają w specyficznym kontekście, mają określone cele, są wspierane lub cenzurowane, mogą być też narzędziem propagandy.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).