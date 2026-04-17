---
type: Web
authors: '[[Przemek Jurgiel-Zyla]]'
url: >-
  https://www.linkedin.com/pulse/po-co-ten-tekst-w-og%C3%B3le-powsta%C5%82-przemek-jurgiel-zyla-fkkvf/
published: 2026-04-07T00:00:00.000Z
created: 2026-04-11T00:00:00.000Z
tags:
  - strategia-AI
  - LLM
  - prompt-engineering
---


Jednego ze znajomych zapytałem niedawno, dlaczego tak rzadko zabiera głos na spotkaniach, gdy rozmowa schodzi na AI. Odpowiedź mnie rozbroiła: "Wiesz, ja już się trochę pogubiłem. Wszyscy gadają o RAG-ach, embeddingach, MCP, agentach, a ja nie chcę wyjść na takiego, który nie rozumie. To wolę nic nie mówić."

**\>> jeśli mnie jeszcze nie obserwujesz, to polecam się - codziennie piszę o AI, VC i technologiach <<**

I to nie był nikt przypadkowy. Facet z wieloletnim stażem, ogarnia produkt, ogarnia GTM, w dwa kwartały ustawił sprzedaż na nowo (z nowym produktem). Po prostu w jednym konkretnym obszarze ostatnie dwa lata mu uciekły. Ten tekst jest dla niego. I dla wszystkich, którzy mają podobnie.

\>> aaaa, no i razem z [Artur ✨ Kurasiński](https://www.linkedin.com/in/artur-kurasinski/) i [Paula Skrzypecka](https://www.linkedin.com/in/paula-skrzypecka/) robimy przekozacki kurs - więcej info znajdziesz tutaj: [AI LEADERS - szkolenie AI dla firm i organizacji](https://beaileader.pl/) <<

Postanowiłem zebrać clue w jednym miejscu. Nie tutorial, tylko przewodnik po klockach (AI): czym są, do czego służą, gdzie się ze sobą łączą, i, co dla mnie jako inwestora i operatora najważniejsze, co z tego wynika dla biznesu.

Wziąłem sobie taki wymyślony case: średniej wielkości firma, nazwijmy ją Januszex. Ma 300 GB dokumentów wewnętrznych: polityki HR, kontrakty, baza wiedzy, zgłoszenia supportu. Pracownicy szukają ręcznie, mediana czasu znalezienia odpowiedzi to 30 minut.

**Cel: zbudować asystenta AI, który zna firmę od środka i odpowiada w 30 sekund. Na tym przykładzie pokażę wszystkie klocki po kolei.**

### 1\. LLM i okno kontekstowe - od czego się to zaczyna

Zaczynamy od fundamentu, czyli LLM-a. Large Language Model to silnik stojący za ChatGPT, Claude'em, Gemini i resztą. Pod spodem wszystkie są transformerami (nazwa technologii przetwarzania danych) wytrenowanymi na ogromnych korpusach (danych), dziesiątki trylionów tokenów z tysięcy dziedzin: medycyna, prawo, kod, nauka, marketing, podobne rzeczy.

Pierwsza rzecz, której wielu nie łapie: trening to jest jednorazowa sprawa. Model raz nauczony nic nowego sam z siebie nie wie. Twoja firma Januszex z 300 GB dokumentów wewnętrznych nigdy nie była częścią danych treningowych. Model o nich nie wie nic.

Skoro nie zna, to jak mu je podać? Najprostszy sposób to wkleić do rozmowy. **Tutaj wchodzi pojęcie, które wraca właściwie w każdej dalszej rozmowie o AI: okno kontekstowe (context window).**

Okno kontekstowe to pamięć krótkoterminowa modelu. Wszystko, co wkleisz w rozmowie, zostaje tam, dopóki rozmowa trwa. Mierzy się to w tokenach (token to z grubsza 3/4 angielskiego słowa, w polskim trochę gorzej - ja często porównuję do sylaby). Różnice między modelami są spore. Małe „flash" i „nano" modele mają okna rzędu 2-4 tysięcy tokenów, czyli parę stron tekstu. Claude Opus z Anthropic ma 200 tysięcy tokenów (a od niedawna w płatnej wersji 1 milion tokenów), xAI Grok 4 około 256 tysięcy, a Gemini 3 Pro nawet milion tokenów, czyli parę set tysięcy słów albo jakieś 100-150 tysięcy linii kodu (choć często dużo mniej).

Wybór modelu robi różnicę. Powieść w formacie txt do zmiany zakończenia? Bierzesz duży kontekst. Szybkie odpowiedzi na proste pytania? Bierzesz małego „flasha", bo tańszy i szybszy.

Jest tu jednak pułapka, w którą wpada większość ludzi wierzących, że jak okno większe, to po prostu lepiej. Im więcej szumu w kontekście, tym gorzej model myśli. Daję ulubiony przykład: „Ania i Andrzej mają plantację truskawek. Ania ma (zebrała) 14 łubinek. Truskawki są często czerwone. 12 to ładna liczba. Andrzej nie ma czerwonych truskawek w łubinkach, ale ma dwa zielone. Zielone truskawki mają gorszy smak. Ile mają łubinek razem?". Odpowiedź to 16, ale żeby ją wyłuskać, model (i Ty zresztą) musi zignorować zalew nieistotnych informacji o kolorach i smakach. Im więcej szumu, tym większe ryzyko, że model się gubi.

A teraz pomyśl, co się dzieje, jak wkleisz mu 200 tysięcy tokenów dokumentów Januszex i poprosisz o jedną konkretną odpowiedź. Otóż nawet największe okno nie zmieści całej firmowej bazy. Gemini z milionem tokenów to mniej więcej 50 typowych dokumentów. A my mamy 300 GB. Matematyka się nie spina.

Trzeba więc rozwiązać dwa problemy naraz. Po pierwsze, jak nauczyć model rozumieć dane Januszex, których nie było w treningu. Po drugie, jak przy każdym pytaniu wybierać tylko te kawałki, które naprawdę są potrzebne. Od tego zaczyna się cała reszta tego artykułu.

### 2\. Embeddingi, czyli jak zamienić znaczenie na liczby

Pierwsza koncepcja, bez której dalej nic nie zrozumiesz: embeddingi.

Embedding to wektor liczb reprezentujący znaczenie tekstu. Bierzesz zdanie, przepuszczasz przez embedding model, dostajesz listę liczb, typowo 1536 wymiarów. Podobne znaczeniowo zdania mają podobne wektory, niezależnie od tego, jakich słów użyłeś.

Klasyczny przykład: „polityka urlopowa pracowników" i „zasady czasu wolnego dla zespołu". Dwa różne zestawy słów, znaczenie praktycznie identyczne. Wektory leżą blisko siebie w wielowymiarowej przestrzeni. Pracownik Januszex pyta „mogę przyjść w jeansach do biura?". Klasyczna wyszukiwarka szuka „jeansy" i nie znajduje, bo dokument nazywa się „dress code". Embeddingowo trafia od razu.

Druga rzecz, której nie da się przeskoczyć, to wymiarowość. 1536 to dziś standard, bo jest balansem między rozdzielczością a kosztem. Można więcej (3072), można mniej. W portfolio [Movens Capital](https://www.linkedin.com/company/movenscapital/) znam foundera, który wszystko hostował lokalnie na małym embeddingowym modelu i miał świetne wyniki, bo zadania były wąskie. Nie zawsze trzeba więcej, trade-off jak w każdym engineeringu.

Jedna rzecz, o której nikt nie mówi na pierwszych slajdach: embedding to nie „rozumienie" w ludzkim sensie. To podobieństwo geometryczne. Czasem dwa zdania są semantycznie blisko, ale niosą sprzeczne treści („można wejść w jeansach" vs „nie można wejść w jeansach"), a embedding sam z siebie tego nie odróżni. Naprawia się to potem resztą architektury.

### 3\. Vector database — szukanie po znaczeniu, nie po słowach

Mamy embeddingi. Co teraz? Trzeba je gdzieś trzymać. I szybko po nich szukać.

Klasyczna baza danych typu SQL nie wystarczy. Bo w SQL szukasz po wartości — SELECT \* FROM documents WHERE content LIKE '%urlop%'. To Ci znajdzie wszystko, gdzie literalnie pojawia się słowo „urlop". A nas już nie interesuje literalne dopasowanie. Nas interesuje znaczenie.

Vector database to baza, która zamiast wartości przechowuje wektory i pozwala szukać po podobieństwie. Mówisz jej: „mam zapytanie, też zamienione na wektor, znajdź mi 5 najbardziej podobnych dokumentów". Ona to robi w milisekundach, nawet jak masz miliony rekordów. Najpopularniejsze implementacje to Pinecone, ChromaDB, Weaviate, Qdrant.

Jest tu jednak twardy trade-off, którego nikt na początku nie chce uznać: vector database przerzuca robotę z osoby szukającej na osobę zasilającą bazę. W SQL ja, jako użytkownik, muszę umieć napisać dobry WHERE (i sam zgadnąć, jak są zapisane dane). W vector DB setupowanie bazy jest skomplikowane, ale potem każdy może pytać normalnym ludzkim językiem.

**Na to setupowanie składa się kilka rzeczy, z którymi trzeba się zmierzyć.**

**Najpierw chunking**, czyli krojenie dokumentów na kawałki, np. po 500-1000 znaków. Nie wrzucisz 50-stronicowej polityki HR jako jednego embeddingu, bo niuanse umrą. Ale jak tylko pokroisz dokument na sztywno co 500 znaków, to zdanie potrafi zostać przecięte w połowie i kontekst się zrywa. Dlatego robi się nakładkę, tzw. chunk overlap: każdy chunk zachodzi na poprzedni o powiedzmy 100 znaków. Trochę nadmiarowości, ale dużo lepszy retrieval. W jednym z eksperymentów, które widziałem, sam dobry overlap poprawił trafność o 40%.

Druga sprawa to scoring, czyli próg, od którego uznajesz wynik za „pasujący". Wyobraź sobie pytanie „czy mogę wziąć laptopa służbowego do Radomia?". Wektor tego zdania będzie miał jakieś podobieństwo do dokumentu o polityce wakacyjnej, bo Radom = wakacje, ma sens. Ale to nie ten dokument, którego chcesz, bo chcesz polityki sprzętu w podróży międzymiastowej. Threshold: poniżej 0.75 odrzucamy i już.

I jeszcze jedna rzecz: strategia chunkingu zależy od typu dokumentu. Prawne trzymasz w długich, ustrukturyzowanych akapitach w całości. Transkrypty rozmów możesz ciąć zdaniami z dużym overlapem. Tech docs najczęściej rozdziałami. To nie jest jeden best practice, to za każdym razem osobna robota.

W paru firmach widziałem ze trzydzieści POC na vector database w ostatnim roku. Co najmniej połowa miała problemy nie dlatego, że technologia nie działa, tylko dlatego, że ktoś nie poświęcił czasu na chunking i scoring. To jest ta „nudna część", którą wszyscy chcą przeskoczyć, i właśnie tam rozstrzyga się, czy system serwuje sens, czy śmieci.

Pro tip: zanim pójdziesz na produkcję, zrób retrieval evaluation set. 50-100 par „pytanie + dokument, który powinien być zwrócony". Mierz trafność. Poniżej 80% nie wypuszczasz. Patrzę na to przy każdym DD w Movens i to jest najszybszy filtr na to, czy founder rozumie, co robi, czy składa demo.

### 4\. RAG — czyli sztuka wciągania własnych danych do rozmowy z modelem

OK, mamy LLM, mamy embeddingi, mamy vector DB. Jak to się składa w jedno?

Nazywa się to RAG, czyli Retrieval Augmented Generation. Trzy słowa, trzy fazy.

Zacznijmy od retrievalu, czyli wyszukania. Pracownik Januszex zadaje pytanie: „Jaka jest nasza polityka pracy zdalnej dla pracowników międzynarodowych?". To pytanie zamieniamy na embedding. Z tym embeddingiem idziemy do vector DB i mówimy: znajdź mi top 5 chunków najbardziej podobnych. Dostajemy pięć fragmentów z dokumentów Januszex, np. kawałek polityki HR, kawałek handbooka, kawałek umowy o pracę.

Następnie augmentation, czyli wzbogacenie. Te pięć fragmentów wstrzykujemy do promptu jako kontekst. Budujemy taki super-prompt: „Jesteś asystentem firmy Januszex. Tu masz fragmenty dokumentów wewnętrznych: \[fragmenty\]. Odpowiedz na pytanie pracownika: \[pytanie\]. Odpowiadaj wyłącznie na podstawie dostarczonego kontekstu. Jeśli nie ma odpowiedzi, powiedz, że nie ma."

Na końcu generation, czyli wygenerowanie odpowiedzi. Wysyłamy to wszystko do LLM-a. Model generuje odpowiedź na podstawie tego, co dostał w prompcie, a nie na podstawie tego, co kiedyś przeczytał w internecie.

**Tutaj jest clue, którego wielu nie chwyta od razu: RAG nie zmienia modelu. Nie trenujesz go, nie fine-tunujesz, nic. Przy każdym pytaniu po prostu dostarczasz mu świeży, sprawdzony kontekst.**

Co to daje w praktyce? Aktualność, bo dane w vector DB możesz odświeżać codziennie. Prywatność, bo dane Januszex nigdy nie idą do treningu modelu. Kontrolę halucynacji, bo masz w prompcie instrukcję „odpowiadaj wyłącznie na podstawie dostarczonego kontekstu", a dobrze zrobiony RAG potrafi powiedzieć „nie wiem, w tym dokumencie tego nie ma" (co dla biznesu jest złotem). I atrybucję źródeł, bo przy każdej odpowiedzi pokazujesz, z którego dokumentu pochodzi. W branżach regulowanych (legal, medical, finance) to jest non-negotiable.

Ale RAG to nie magia. RAG działa tak dobrze, jak dobry jest Twój retrieval. Jeśli vector DB zwróci pięć nieistotnych fragmentów, to LLM wygeneruje bzdurę albo powie „nie wiem". GIGO (garbage in harbage out) w czystej postaci. Druga rzecz: RAG dla bazy prawnej będzie wyglądał inaczej niż RAG dla supportu klienta. Inny chunking, inny embedding, inny prompt. Widziałem zespoły, które wpadały w pułapkę „zrobiliśmy RAG, lecimy z nim wszędzie", a potem nie rozumiały, czemu dla drugiego use case'a wyniki są dramat.

Alternatywy? Fine-tuning jest drogi i długi, ale daje głębszą integrację wiedzy. Duże okno kontekstowe jest proste, ale drogie i nieskalowalne. Agentic search, gdzie model sam decyduje, kiedy szukać, jest modny ostatnio i robi się coraz ciekawszy. W większości przypadków biznesowych, które widzę w portfolio Movens, RAG i tak wygrywa, bo jest prosty, tani i odwracalny.

### 5\. Prompt engineering — bo dobre pytanie to połowa odpowiedzi

Zatrzymam się chwilę przy promptowaniu, bo to temat, który wszyscy mają w nosie, dopóki pierwszy raz nie spróbują wyciągnąć z modelu konkretu i nie wyjdzie.

Klasyczny błąd: pytasz „jaka jest polityka?", dostajesz długi, ogólny esej. Pytasz „jaka jest polityka pracy zdalnej dla pracowników międzynarodowych z kontraktem B2B na okres dłuższy niż 90 dni?", dostajesz konkretną odpowiedź. Specyfika płaci.

Dobry prompt zwykle mówi modelowi trzy rzeczy: kim jest (rola, np. „jesteś ekspertem od HR firmy Januszex"), co ma zrobić (zadanie) i jak ma to zrobić (format, styl, ograniczenia, np. „odpowiadaj w bullet points, max 3 zdania na bullet, jak nie wiesz, powiedz wprost").

Do tego cztery techniki, które wracają w każdej rozmowie o promptach. Zero-shot to sytuacja, kiedy nie dajesz żadnego przykładu, tylko zadanie. Model leci wtedy ze swojej wiedzy treningowej, szybko, ale jakość jest loterią. One-shot oznacza, że dorzucasz jeden przykład wyniku, żeby model trzymał się formatu. Few-shot to już 3-5 przykładów, dzięki którym model widzi nie tylko format, ale też ton, niuanse i edge case'y, a to jest najlepsze do zadań stylistycznych, typu obsługa klienta. No i chain of thought, gdzie mówisz modelowi „myśl krok po kroku, najpierw zrób A, potem B", przez co model nie skacze do odpowiedzi, tylko pokazuje rozumowanie. Tańsze i głupsze modele potrafią się w tym trybie zrobić dwa razy lepsze.

Z mojej obserwacji, prompt engineering to najtańsza i najbardziej niedoceniana inwestycja, jaką zespoły mogą zrobić. W naszych spółkach portfelowych widzę regularnie sytuacje typu „zmieniliśmy model na droższy, bo poprzedni był słaby". W połowie przypadków słaby był nie model, tylko prompt. Pro tip: trzymajcie prompty w repo, traktujcie je jak kod. Wersjonujcie, testujcie, mierzcie regresje.

### 6\. LangChain - klej, który skleja klocki

Mamy embeddingi, vector DB, prompty, RAG. Trzeba to teraz spiąć w działającą aplikację. Można to zrobić ręcznie - pisać własne integracje z OpenAI, własne wrappery na vector DB, własne zarządzanie historią rozmowy, własne tool routing. Można. Tylko po co.

**LangChain to abstrakcja, która sprowadza spinanie tych klocków do kilku linii kodu. Główne komponenty:**

\- **Chat models** - jednolity interfejs do dowolnego LLM-a. Chcesz GPT? ChatOpenAI (model="gpt-5"). Chcesz Claude? ChatAnthropic (...). Zmieniasz jedną linijkę.

\- **Memory** - automatyczne trzymanie historii rozmowy, bez własnej bazy.

\- **Vector store integrations** - jeden interfejs do Pinecone, Chroma, Weaviate.

\- **Tools** - pozwalają agentowi wywołać zewnętrzne funkcje (zapytanie do bazy, web search, własne API).

\- **Output parsers** - wyciąganie ze swobodnej odpowiedzi strukturalnych obiektów (JSON, listy).

\- **Prompt templates** - wielokrotnego użytku szablony z placeholderami.

Co LangChain robi pod spodem to zwykła robota integracyjna. Jak zrobisz ją sam i 6 miesięcy później chcesz zmienić providera - zostają Ci dwa tygodnie refaktoringu. Z LangChainem to jedna linijka.

Ważne zastrzeżenie, bo coraz więcej osób ma do LangChaina mieszane uczucia (ja częściowo też): LangChain ma ogromną powierzchnię API i czasem bywa over-engineered. Dla bardzo prostych przypadków można spokojnie wziąć surowe SDK od OpenAI/Anthropic. Ale w momencie, kiedy wchodzisz w wielo-providerowy setup z agentami, RAG-iem, tools i memory - LangChain zaczyna mieć sens. Alternatywy: LlamaIndex (lepszy do retrievalu), Haystack, własne klocki.

### 7\. LangGraph - kiedy AI musi przejść przez kilka kroków, a nie tylko odpowiedzieć

LangChain dobrze radzi sobie z prostym schematem „pytanie → odpowiedź". Ale realne procesy biznesowe rzadko tak wyglądają. Realny proces to: „Klient pyta → sprawdź jego status → sprawdź historię zamówień → zweryfikuj politykę zwrotów → wygeneruj odpowiedź → zaproponuj follow-up". Krok, decyzja, następny krok, czasem pętla, czasem rozgałęzienie.

I tutaj wchodzi LangGraph - rozszerzenie LangChaina do budowania workflowów wielokrokowych jako grafów.

Przykład z naszej Januszex: pracownik pyta „chcę zrozumieć naszą politykę prywatności danych dla klientów z UE". To brzmi jak proste pytanie, ale jeśli chcesz je zrobić porządnie, musisz:

\- znaleźć i zebrać dokumenty dotyczące polityki prywatności,

\- wyciągnąć i oczyścić ich treść,

\- zweryfikować zgodność z GDPR,

\- przekrosować z lokalnymi regulacjami unijnymi,

\- zidentyfikować luki i wygenerować rekomendacje.

W LangGraphie każdy z tych kroków to **node** - pojedyncza funkcja w Pythonie, która bierze stan na wejściu i zwraca jego update. Nodes łączysz **edge'ami** (krawędziami), które definiują, w jakiej kolejności coś się wykonuje. Możesz mieć **conditional edges**, czyli „jeśli wynik node'a 3 ma compliance score poniżej 75%, to wracaj do node'a 1 po więcej dokumentów; jeśli powyżej, idź do node'a 5 z generowaniem raportu". To są pętle, rozgałęzienia, decyzje warunkowe - wszystko, co znamy z normalnego programowania, tylko że stan jest współdzielony i każdy node może coś do niego dorzucić.

Trzecie pojęcie: **shared state**. Czyli taki słownik (TypedDict), który wędruje przez cały graf i zbiera dane. Jeden node wrzuca tam listę dokumentów, drugi compliance score, trzeci listę luk, czwarty rekomendacje. Na końcu masz pełny obraz przejścia - co się działo, jakie były decyzje, jakie wyniki.

Dlaczego to jest ważne dla biznesu? Bo realne use case'y AI w firmach to rzadko „zapytaj i odpowiedz". Realne use case'y to: zbierz dane z trzech systemów, zrób analizę, podejmij decyzję, zaproponuj akcję, zaktualizuj system, powiadom człowieka. To jest workflow, nie chat. I dopóki nie umiesz tego zaprojektować jako graf — będziesz to robił ręcznie w kodzie i wyjdzie spaghetti.

Z mojej praktyki w Movens: 90% spółek portfolio, które pracują z agentami AI na produkcji, prędzej czy później kończy z czymś, co przypomina LangGraph (albo używają go wprost). Bo bez explicit state i explicit transitions to się nie skaluje. A jak nie skaluje się architektura - nie skaluje się produkt.

### 8\. MCP: Model Context Protocol, czyli uniwersalny port do świata zewnętrznego

I jeszcze jeden klocek, który w 2024 i 2025 zrobił dużo szumu, a w 2026 wszedł na dobre do produkcji: MCP, czyli Model Context Protocol. Wymyśliło to Anthropic. To standard definiujący, jak AI agent ma rozmawiać z zewnętrznymi narzędziami i danymi. Brzmi nudno - protokół, standard. A to jest kawałek infrastruktury, który zmienia reguły gry.

Januszex ma już asystenta na własnej bazie wiedzy. Działa. Ale teraz pracownicy chcą, żeby miał też dostęp do CRM-a, systemu ticketów, bazy klientów, fakturowania, kalendarza, JIRA, GitHuba. Każde narzędzie ma swoje API, swoje sposoby autentykacji, swoje schematy. Bez standardu - robisz dziesięć osobnych integracji, każda na kilka tygodni, każda potem do utrzymania.

MCP to USB do świata AI. Ktoś raz pisze MCP server dla GitHuba, ktoś inny dla SQL bazy, ktoś trzeci dla Slacka. Twój agent (zbudowany w czymkolwiek - LangGraph, własny scaffold, Claude Code, Cursor) podłącza się do nich. Nie musi rozumieć, jak GitHub API działa pod spodem - MCP server wystawia self-describing interface, agent czyta opis, wie co może zrobić, wybiera narzędzie sam.

Klucz: MCP **przerzuca brzemię integracji z developera na agenta**. W tradycyjnym API to ja, developer, muszę wiedzieć endpoint, parametry, format odpowiedzi. W MCP agent czyta schemat narzędzia i sam decyduje, kiedy go użyć. Definicja po stronie servera jest zwykle dosłownie kilka linijek - funkcja z dekoratorem @mcp.tool(), opis, parametry, return type. To cały kontrakt.

Co najlepsze, istnieje już dojrzały ekosystem gotowych serverów. GitHub, GitLab, Slack, Notion, Linear, Postgres, MongoDB, Google Drive, S3, kalendarz, mail. Większości nie musisz pisać sam. Bierzesz, podłączasz, działasz. I tutaj coś, co mnie jako inwestora fascynuje. MCP to wczesny moment standardu, podobny trochę do tego, jak REST wygryzł SOAP. Standardy infrastrukturalne wygrywają adoption. W portfolio Movens widzę, że founderzy, którzy stawiają na MCP-first, mają dużo szybszy time-to-integration niż ci, którzy klepią to po staremu.

### 9\. OK, i co Ty z tym wszystkim masz zrobić

Jeśli doczytałeś do tego miejsca, gratuluję samozaparcia. Teraz najtrudniejsza część: jak to przekuć z wiedzy w decyzję biznesową.

Z perspektywy przedsiębiorstw, z którymi mam okazję rozmawiać, widzę trzy typowe pułapki, w które ludzie wpadają, kiedy zaczynają wdrażać AI:

**Pułapka pierwsza: zachłyśnięcie się demo.** Ktoś klika w ChatGPT, dostaje wow-efekt, mówi „chcemy to u nas". Tylko że ChatGPT odpowiada na pytania o świat. Twoja firma potrzebuje odpowiedzi o swój wewnętrzny kontekst - i tutaj sam ChatGPT na nic. Potrzebujesz RAG-a na własnych danych. Demo to nie produkcja.

**Pułapka druga: lekceważenie data plumbingu.** Ludzie myślą, że AI to model. AI to w 80% jest robota wokół modelu - chunking, embeddingi, vector DB, prompt engineering, eval, monitoring, security, kontrola halucynacji. Przedsiębiorcę, który mówi „my użyjemy GPT-5 i mamy z głowy", traktuję z lekkim sceptycyzmem. Właściciela, który mówi „spędziliśmy trzy tygodnie na tuningu retrievalu i mamy 92% accuracy na evaluation set" - z dużo większą uwagą.

**Pułapka trzecia: brak ludzkiego loopa.** Pierwsza wersja każdego AI w firmie powinna mieć człowieka w pętli. Asystent proponuje, człowiek zatwierdza. Asystent szkicuje, człowiek wysyła. Asystent analizuje, człowiek decyduje. Dopiero kiedy zbierzesz bazę feedbacku - zaczynasz delikatnie zdejmować człowieka z prostszych decyzji. Każdy, kto chce od razu w pełni zautomatyzować proces, wcześniej czy później kupuje sobie incydent.

A teraz dobra wiadomość: jeśli zrobisz to z głową - zwroty są naprawdę duże. W kilku znajomych spółkach widziałem skoki w produktywności rzędu 30-50% na konkretnych procesach (support pierwszej linii, generowanie ofert, onboarding pracowników, analiza dokumentów). To nie są wyniki marketingowe, to są twarde liczby z dashboardów. Przy czym kluczowe słowo to „konkretne procesy". AI wdrożone „ogólnie" daje ogólny impakt, czyli żaden. AI wdrożone w jednym konkretnym procesie z jasno zdefiniowanym KPI daje wyniki, które dają się obronić przed zarządem i przed CFO.

Mój playbook dla leadera AI, który dziś chce zacząć z sztuczną inteligencją w firmie:

1\. **Wybierz jeden proces.** Nie pięć. Jeden. Najlepiej taki, gdzie ludzie tracą najwięcej czasu na powtarzalne zadania albo gdzie czas reakcji jest kluczowy.

2\. **Zmierz go przed.** Średni czas obsługi, satysfakcja klienta, jakość outputu. Cokolwiek, co jest mierzalne. Bez baseline'u nigdy nie będziesz w stanie powiedzieć, czy AI pomogło.

3\. **Zacznij od najprostszego klocka, który zadanie rozwiązuje.** Nie buduj agentów, jak wystarczy RAG. Nie buduj RAG-a, jak wystarczy dobry prompt. Nie wybieraj LangGraph, jak wystarczy LangChain. Schodź na bardziej zaawansowane klocki dopiero jak proste się wyczerpią.

4\. **Postaw eval set zanim postawisz produkcję.** 50-100 par „input + oczekiwany output" + automat, który przy każdej zmianie sprawdza, czy nie pogorszyło. To nie jest fanaberia inżynierska, to jest minimum higieny.

5\. **Pętla z człowiekiem przez pierwsze 3 miesiące.** Bez wyjątków.

6\. **Po 3 miesiącach - review.** Co się sprawdziło, co nie, co automatyzować dalej, co cofnąć.

Najważniejsze, co chciałbym, żebyś wyniósł z tego tekstu: **AI w biznesie to nie jest jeden duży model, to są klocki**. Klocki są nudne, niewdzięczne, mało efektowne na konferencjach. Ale to one decydują, czy Twój wdrożony asystent jest dumą zarządu, czy żartem dla zespołu. I jak to z fundamentami w każdej innej dziedzinie inżynierii: wygrywa nie ten, który zna najwięcej buzzwordów, tylko ten, który najpierw zrozumiał, co robi, a dopiero potem to zrobił.

A jeżeli czujesz, że Twoja firma jest gotowa, żeby przejść z fazy „rozmawiamy o AI" do fazy „mamy AI na produkcji", z wielką chęcią porozmawiam. W Movens Capital sporo czasu poświęcamy spółkom, które na bazie tych klocków budują realne produkty.

PS Ten artykuł powstał z jednej rozmowy, powiedziałem znajomemu: „dobra, daj mi tydzień, zbiorę Ci to wszystko w jedno miejsce". Tydzień się rozciągnął jak to zwykle, miało być na 200-dzień z podstaw - nie wyszło:P. Jeśli czujesz, że ktoś z Twoich znajomych pasuje do roli, o której piszę -> podeślij mu link. Tekst z premedytacją jest długi, żeby był jednorazową lekturą zamiast szukania po dwudziestu artykułach.
