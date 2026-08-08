---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2026/07/wyszukiwanie-za-pomoca-ai-wygodne-odpowiedzi-niepewne-zrodla?utm_source=newsletter"
published: 2026-07-21
created: 2026-08-05
tags:
  - "LLM"
  - "narzędzia-AI"
  - "trendy-AI"
---


Systemy wyszukiwania AI - ChatGPT, Copilot, Gemini, Perplexity - traktują treści syntetyczne jako wiarygodne, korzystają z wąskiej grupy uznanych domen oraz szerokiego zbioru mało znanych witryn niskiej jakości. Treści z tych witryn bywają maszynowo generowane i dostosowywane są do dynamiki wyszukiwania, preferującej jasne, konkretne odpowiedzi, pozbawione szerszego kontekstu i niuansów.

Opublikowany przez badaczy z Uniwersytetu Northwestern preprint *Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources* (DOI: [10.48550/arXiv.2605.23684](https://doi.org/10.48550/arXiv.2605.23684), 2026) to kolejne już omawiane na tym blogu badanie na temat jakości riserczu wykonywanego za pomocą generatywnej AI, zdolnej do eksploracji źródeł internetowych. [Wspomniana przeze mnie wcześniej praca](https://blog.humanistyka.dev/2025/11/czasem-przypis-mowi-wiecej-niz-autor-utmsource-equal-chatgptcom) *PaperAsk: A Benchmark for Reliability Evaluation of LLMs in Paper Search and Reading* (DOI: [10.48550/arXiv.2510.22242](https://doi.org/10.48550/arXiv.2510.22242), 2025) zwracała uwagę, że wyszukiwanie prowadzone przez LLM-y opiera się na płytkim dopasowywaniu słów kluczowych i niepełnym pokryciu dostępnych źródeł, a w konsekwencji użytkownicy korzystający z takich narzędzi jako asystentów badawczych mogą nie dotrzeć do dużej części (ponad 60 proc.) literatury, która obiektywnie pasowałaby do kryteriów tematycznych i czasowych wyszukiwania. Z kolei [badanie poświęcone *answer bubbles* - bańkom wyszukiwawczym](https://blog.humanistyka.dev/2026/05/25-badan-na-25-lecie-wikipedii-cz-v) (DOI: [10.48550/arXiv.2603.16138](https://doi.org/10.48550/arXiv.2603.16138), 2026) akcentowało problem zanikania różnic między cytowaniem a syntezą w proponowanych automatycznie odpowiedziach. Co tym razem nie działa w wyszukiwaniu wspieranym przez modele generatywne? 🤔

**Polityka, zdrowie, środowisko**

W *Synthetic Sources?* zbadano jakość odpowiedzi ChatGPT, Copilot, Gemini i Perplexity na 712 pytań z wiedzy ogólnej na temat polityki, zdrowia i środowiska (*real-world human-generated queries*). Pytania te pochodziły ze zbiorów [Search Arena](https://huggingface.co/datasets/lmarena-ai/search-arena-24k) i [Climate Q&A](https://www.climateqa.com/). Oto przykłady pytań z tych źródeł:

> "Which universities and states will be most impacted by the denial of funds on science?", "Authors who claimed that technology could usher in a communist economy", "Who was 1st president in us", "Which foods Contain all essential amino acids? Protein Drinks?", "can i use zofran and bisacodyl together", "Do you think Donald Trump and his administration members participated in insider trading?", "Why is Taiwan a country?", "why only germany not embrace Modern Monetary Theory in rich nation?"

Autorzy badania wybrali do testów wyłącznie pytania w języku angielskim, odnoszące się do USA (usunięto zatem np. pytanie o Tajwan czy o system opieki zdrowotnej w Europie), argumentując, że wszystkie analizowane narzędzia rozwijane są w Stanach Zjednoczonych. Zrezygnowano także z pytań, na które odpowiedź wymagałaby rozbudowanych interakcji między człowiekiem a modelem (wybrano więc jedynie te *single-turn*). Za pomocą modelu [BERTopic](https://maartengr.github.io/BERTopic/index.html) przypisano 712 pytań do trzech kategorii: 175 pytań znalazło się w kategorii “polityka”, 257 - “zdrowie”, a 280 “środowisko”.

Żeby jak najlepiej symulować ludzkie korzystanie z ChatGPT, Copilot, Gemini i Perplexity, zdecydowano się nie korzystać z interfejsów maszynowych (API) tych systemów, tylko umieszczać pytania i scrapować odpowiedzi bezpośrednio w interfejsie użytkownika. Użyto do tego skryptów automatycznie zarządzających zachowaniem przeglądarki (imitujących działania użytkownika), bazujących na bibliotece [Playwright](https://playwright.dev/). Skrypty wysyłały pytania i zbierały odpowiedzi, od razu wyodrębniając z nich ponad 26 tys. unikalnych adresów URL do wzmiankowanych przez modele źródeł.

**Źródła syntetyczne**

Teksty z tych źródeł wysłano następnie do testów w [Pangramie](https://www.pangram.com/), żeby sprawdzić, czy są one wygenerowane maszynowo. Pangram nie jest idealnym narzędziem, ale charakteryzuje się stosunkowo niskim poziomem wyników fałszywie dodatnich - genezę tekstów [lepiej sprawdzać stylometrycznie](https://blog.humanistyka.dev/2026/03/stylometryczne-cechy-tekstow-generowanych-maszynowo), co jest jednak trudniejsze, bo nie da się wykorzystać jednej metody dla tak zróżnicowanych źródeł jak w tym badaniu.

Po testach Pangramem okazało się, że około 16 proc. unikalnych źródeł cytowanych przez te wyszukiwarki to treści najprawdopodobniej wygenerowane przez AI (tzw. źródła syntetyczne). Wyniki te różniły się w zależności od narzędzia - ChatGPT miał najniższy odsetek cytowań AI (7,3 proc.), Copilot - prawie jedną trzecią!

Sprawdzono też, jaka część źródeł w każdej kategorii miała syntetyczny charakter. W przypadku tematów politycznych było to około 11 proc. adresów URL, a w przypadku pytań o zdrowie - ponad 16 proc. Najwięcej unikalnych źródeł syntetycznych pojawiło się przy pytaniach dotyczących środowiska i klimatu. Chociaż wobec wszystkich proponowanych tam odnośników tylko 13 proc. prowadziło do wygenerowanych maszynowo treści, odpowiedzi w tej kategorii zawierały średnio najwięcej cytowań (średnio 10 na pytanie). Użytkownicy szukający informacji o klimacie byli więc najbardziej narażeni na kontakt z treściami wygenerowanymi maszynowo.

Analiza domen wykazała, że proponowane w systemach generatywnej AI źródła wiedzy korzystają z wąskiej grupy często cytowanych witryn (oczywiście jest tam Wikipedia, ale też strony rządowe). Mamy zatem kolejne badanie dokumentujące istnienie *answer bubbles*. Z drugiej strony, w odpowiedziach modeli pojawiły się wskazania ogromnej liczby domen, proponowanych tylko raz albo dwa razy, i zdecydowanie częściej zawierających treści maszynowo generowane:

> \[...\] \[...\] 25 najczęściej wykorzystywanych domen źródłowych (tj. czołówka rozkładu) odpowiada za 2.9 proc. źródeł syntetycznych, podczas gdy pozostałe domeny internetowe odpowiadają za 97.1 źródeł \[tego typu - MW\], proponowanych w generowanych przez AI odpowiedziach. Ustalenie to potwierdza istnienie długiego ogona (long tail) w rozkładzie domen źródłowych, z których generatywne wyszukiwarki czerpią informacje podczas tworzenia odpowiedzi na zapytania użytkowników.

**Długi ogon**

![enter image description here](https://blog.humanistyka.dev/content/images/20260721191310-47e6d541f64eb7c3156f29948dcc8ece681bcb5f5e583622756b787458d4b978.png) *Answer bubbles* i długi ogon w źródłach z wyszukiwania za pomocą konwersacyjnej AI. DOI: [10.48550/arXiv.2605.23684](https://doi.org/10.48550/arXiv.2605.23684), 2026.

Niebezpieczne w wyszukiwaniu ze wsparciem AI okazuje się nie tylko koncentrowanie źródeł w niewielkiej grupie dominujących serwisów internetowych, ale też szerokie wykorzystanie niszowych witryn publikujących treści niskiej jakości.

> Jesteśmy przekonani, że wyszukiwanie z wykorzystaniem sztucznej inteligencji stanie się w niedalekiej przyszłości, dla kolejnych pokoleń, podstawowym sposobem dostępu do informacji.

mówił, [cytowany dwa lata temu na stronach OpenAI](https://openai.com/pl-PL/index/introducing-chatgpt-search/) wydawca dziennika “Le Monde” (oficjalnego partnera firmy Sama Altmana).

> Znalezienie przydatnych odpowiedzi w sieci może wymagać dużego wysiłku. Często konieczne jest przeprowadzenie wielu wyszukiwań i przejrzenie szeregu linków, aby znaleźć wartościowe źródła i właściwe informacje.

- czytamy na tej samej stronie. Proponowany przez wydawców narzędzi AI panoramiczny risercz nie działa jednak najlepiej (czy jednak nas to w ogóle zaskakuje?). Praca ze źródłami, zbieranie materiałów i agregowanie wiedzy wciąż, wbrew głosom wydawców modeli, nie może być ograniczone do jednego, działającego nieprzejrzyście narzędzia. Ceną za wygodę riserczu jest spadek jakości jego wyników i - o czym warto pamiętać, wbrew entuzjastycznym komentarzom przedstawicieli branży AI - postępująca [eksploatacja jakościowych treści dziennikarskich](https://techcrunch.com/2025/07/02/chatgpt-referrals-to-news-sites-are-growing-but-not-enough-to-offset-search-declines/), publikowanych online:

> Odesłania (referrals) z ChatGPT do wydawców wiadomości rosną, ale nie na tyle, aby zrównoważyć spadek liczby kliknięć wynikający z tego, że użytkownicy coraz częściej uzyskują informacje bezpośrednio od systemów AI lub z wyników wyszukiwania wspieranych przez sztuczną inteligencję — wynika z raportu firmy Similarweb zajmującej się analizą rynku cyfrowego. Od momentu uruchomienia funkcji AI Overviews w Google w maju 2024 roku firma stwierdziła, że odsetek wyszukiwań wiadomości w internecie, które nie prowadzą do żadnego kliknięcia w stronę serwisów informacyjnych, wzrósł z 56 proc. do niemal 69 proc. w maju 2025 roku.

Bez wątpienia wyszukiwarki wbudowane w konwersacyjne systemy AI mogą zmieniać przyzwyczajenia związane ze zdobywaniem informacji w internecie. Zamiast przeglądania wielu linków, użytkownicy mogą wybierać łatwiejsze rozwiązanie - konsumpcję pojedynczej, syntetycznej odpowiedzi, zbudowanej jednak na niepewnych źródłach. Niepewnych, ponieważ systemy te są zaprojektowane tak, żeby zdawały się możliwie najbardziej użyteczne i wobec braku łatwej do użycia wiedzy z dobrej jakości witryn, wybierać będą treści syntetyczne, ale za to łatwo dostępne i projektowane pod szybkie wykorzystanie.

![enter image description here](https://blog.humanistyka.dev/content/images/20260721191337-ca36cc79bdc7f0434d995ef0fd34ce9bef7cab895151efb085c418747e52f574.png) Najczęściej cytowane źródła dla wszystkich kategorii i wszystkich narzędzi uwzględnionych w badaniu. DOI: [10.48550/arXiv.2605.23684](https://doi.org/10.48550/arXiv.2605.23684), 2026.

Sztuczna inteligencja, wykorzystywana do riserczu, preferować będzie te serwisy, których treści w jednoznaczny i możliwie dokładny sposób odpowiadają na pytania użytkownika. Coraz bardziej w automatycznych propozycjach źródeł ignorowane będą materiały obszerniejsze, bardziej zniuansowane, eseistyczne, wymagające pewnej pracy przy interpretacji. Nie jest to proces, który zaczął się wraz z udostępnianiem wyszukiwania przez ChatGPT, ale na pewno systemy wyszukiwania w konwersacyjnej AI go wzmacniają.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).