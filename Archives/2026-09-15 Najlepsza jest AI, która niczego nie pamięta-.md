---
type: "Web"
authors: "[[Krzysztof Mirończuk]]"
url: "https://haimagazine.com/pl/ai_branza/bezpieczenstwo-pl/najlepsza-jest-ai-ktora-niczego-nie-pamieta/"
published: 2026-09-15
created: 2026-09-28
tags:
  - "strategia-AI"
  - "LLM"
  - "trendy-AI"
---


Jeszcze niedawno najważniejsze pytanie przy wyborze modelu AI brzmiało: który jest najlepszy? Który lepiej pisze kod, analizuje dokumenty, rozwiązuje problemy i radzi sobie z coraz bardziej złożonymi zadaniami?

Dziś niektóre firmy zaczynają zadawać inne pytanie: co dokładnie stanie się z informacją, którą przekażemy temu modelowi?

Palantir nie chce udostępnić części najbardziej zaawansowanych modeli Anthropic swoim klientom bez dodatkowych gwarancji dotyczących przechowywania danych. Nvidia ogranicza używanie Claude przy bardziej wrażliwych zadaniach. Booz Allen Hamilton zabronił wykorzystywania komercyjnych wersji Claude przy części własnych prac z obszaru cyberbezpieczeństwa. Jak [==podał Reuters==](https://www.reuters.com/business/palantir-nvidia-curb-ai-model-use-over-data-fears-information-reports-2026-09-14/), wspólnym powodem są obawy dotyczące bezpieczeństwa danych i ochrony własności intelektualnej.

To nie oznacza nagłego kryzysu zaufania do sztucznej inteligencji. Pokazuje jednak problem, który wraz z rozwojem AI prawdopodobnie będzie stawał się coraz ważniejszy.

Bo im więcej AI potrafi zrobić dla firmy, tym więcej firma musi jej najpierw powiedzieć.

#### AI, której nie można pokazać wszystkiego

Spór nabrał znaczenia po zmianie zasad dotyczących najbardziej zaawansowanych modeli Anthropic. Firma wprowadziła kategorię tzw. Covered Models. W ich przypadku prompty przesyłane przez użytkowników biznesowych i odpowiedzi modelu są przechowywane przez 30 dni. Zasada obejmuje również organizacje, które wcześniej korzystały z rozwiązania Zero Data Retention, czyli ZDR. W takim trybie dane nie są zachowywane przez dostawcę po obsłużeniu zapytania.

Anthropic tłumaczy w swojej ==[dokumentacji dotyczącej Covered Models](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)==, że zmiana obejmuje organizacje korzystające z ZDR bezpośrednio przez Claude, ale także przez wybrane platformy chmurowe.

Dla większości użytkowników różnica może wydawać się technicznym szczegółem. Dla firmy pracującej z poufnymi informacjami jest jednak zasadnicza.

Jeżeli pracownik prosi model o poprawienie zwykłego maila, trzydziestodniowa retencja prawdopodobnie nie będzie kluczowym problemem. Jeżeli jednak programista przesyła fragment kodu projektowanego produktu, analityk pracuje na niepublicznych danych finansowych, a specjalista bezpieczeństwa przekazuje modelowi opis niewykrytej jeszcze podatności, sytuacja wygląda zupełnie inaczej.

Prompt przestaje być tylko pytaniem. Staje się częścią firmowej dokumentacji.

Według Reutersa Nvidia właśnie dlatego ogranicza zastosowanie modeli Anthropic przy bardziej wrażliwych zadaniach. Palantir poszedł dalej i oczekuje od Anthropic gwarancji ZDR, której dostawca nie mógłby później jednostronnie wycofać. Booz Allen zakazał natomiast stosowania komercyjnego Claude do części własnych prac związanych z cyberbezpieczeństwem.

Firmy nie rezygnują więc z AI. Zaczynają natomiast określać, czego AI nie może zobaczyć.

#### Prompt może być wart więcej niż odpowiedź

Przez pierwsze lata boomu na generatywną AI dyskusja o danych koncentrowała się przede wszystkim na ryzyku, że pracownik bez zastanowienia wklei do publicznego czata fragment umowy, dane klienta albo poufny dokument. Problem nie zniknął, ale skala wykorzystania AI się zmieniła.

Modele nie służą już tylko do pisania tekstów czy podsumowywania dokumentów. Dostają kod źródłowy, projekty produktów, wyniki badań, dane finansowe, wewnętrzne procedury i informacje o klientach. Coraz częściej podłączane są również do innych systemów firmy, a agenci AI otrzymują możliwość korzystania z baz danych, aplikacji czy repozytoriów kodu.

W takim układzie wartość informacji przekazywanych modelowi może być znacznie większa niż wartość jego odpowiedzi. Co istotne, przechowywanie danych nie jest tym samym, co wykorzystywanie ich do trenowania modelu.

Anthropic deklaruje w ==[polityce dotyczącej produktów komercyjnych](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)==, że dane wejściowe i odpowiedzi pochodzące z Claude for Work, API czy Claude Gov domyślnie nie są wykorzystywane do trenowania modeli. Może się to zmienić, jeżeli klient sam wyrazi zgodę, między innymi przekazując rozmowę jako feedback. To rozróżnienie jest ważne, bo w publicznej dyskusji często miesza się kilka różnych kwestii.

Pierwsza to retencja: czy dostawca zachowuje treść promptu i odpowiedzi, a jeśli tak, to jak długo. Druga to trening: czy te dane mogą później zostać wykorzystane do ulepszania modeli. Trzecia to dostęp: kto i w jakich okolicznościach może zobaczyć przechowywaną treść. I wreszcie czwarta kwestia: monitoring bezpieczeństwa, czyli analiza sposobu korzystania z modeli w celu wykrywania nadużyć.

Dopiero po rozdzieleniu tych elementów widać, gdzie naprawdę leży problem.

#### Dlaczego AI chce pamiętać?

Najprostsze rozwiązanie brzmiałaby: skoro firmy nie chcą, żeby ich dane były przechowywane, dostawca powinien po prostu ich nie zapisywać. Tyle że z perspektywy Anthropic właśnie tutaj zaczyna się problem.

Firma tłumaczy, że poważne nadużycia mogą ujawniać się dopiero wtedy, gdy system bezpieczeństwa analizuje wiele kolejnych interakcji. Jako przykłady podaje między innymi kampanie szpiegowskie i próby wymuszenia danych. Pojedynczy prompt może wyglądać niewinnie. Dopiero seria zapytań pokazuje, co właściwie próbuje zrobić użytkownik.

Dlatego Anthropic wymaga dla Covered Models trzydziestodniowej retencji promptów i odpowiedzi.

Według firmy jej pracownicy domyślnie nie mogą czytać takich rozmów. Dostęp człowieka ma następować tylko kontrolowaną ścieżką, na przykład wtedy, gdy automatyczne systemy bezpieczeństwa oznaczą treść jako potencjalnie niebezpieczną. Mogą ją przeglądać tylko zatwierdzeni pracownicy, a każde uzyskanie dostępu jest rejestrowane. Po 30 dniach dane są automatycznie usuwane, chyba że zostały oznaczone w związku z kwestiami bezpieczeństwa albo firma musi zachować je ze względów prawnych.

Z perspektywy bezpieczeństwa modeli ma to sens. Problem polega na tym, że z perspektywy bezpieczeństwa klienta równie logiczne może być dokładnie przeciwne podejście.

#### Bezpieczeństwo kontra bezpieczeństwo

Wyobraźmy sobie firmę, która opracowuje technologię wartą miliardy dolarów. Jej pracownicy chcą użyć najlepszego dostępnego modelu do analizy kodu. Dostawca AI mówi: muszę przez pewien czas zachować te dane, ponieważ tylko w ten sposób mogę wykrywać poważne nadużycia. Klient odpowiada: właśnie dlatego, że ten kod jest tak cenny, nie chcę, żeby istniała jego dodatkowa kopia poza środowiskiem, nad którym mam kontrolę.

Obie strony próbują zwiększyć bezpieczeństwo. Ale nie tego samego.

Anthropic chce ograniczać ryzyko niebezpiecznego wykorzystania swoich modeli. Przedsiębiorstwo chroni własność intelektualną, tajemnice handlowe i dane klientów przed utratą kontroli. Każde dodatkowe miejsce przechowywania informacji oznacza bowiem dodatkowy element infrastruktury, który trzeba zabezpieczyć. Nawet jeśli dostawca deklaruje bardzo wysoki poziom ochrony, dla części organizacji może obowiązywać prosta zasada: najbardziej wrażliwej informacji najlepiej nie przechowywać poza własnym środowiskiem w ogóle.

I właśnie dlatego ZDR przestaje być niezrozumiałym skrótem z umowy z dostawcą technologii a może stać się jednym z warunków wdrożenia AI.

## Pamięć jako problem, nie zaleta

Paradoks jest tym większy, że rozwój sztucznej inteligencji zmierza w przeciwnym kierunku.

Modele mają pamiętać kontekst, wykonywać coraz dłuższe zadania, korzystać z wielu narzędzi i obserwować kolejne etapy procesu. To właśnie dzięki temu mogą przejmować bardziej skomplikowaną pracę.

Jednocześnie najwięksi klienci biznesowi mogą coraz częściej oczekiwać, aby dostawca modelu pamiętał możliwie najmniej.

Nie jest to problem wyłącznie Anthropic. OpenAI ogłosiło w sierpniu rozszerzenie dostępu do Zero Data Retention dla najbardziej zaawansowanych modeli. Firma deklaruje, że w przypadku kwalifikujących się klientów API nie zachowuje promptów ani odpowiedzi po obsłużeniu żądania, a dane klientów biznesowych nie są używane do treningu bez ich wyraźnej zgody. ==[OpenAI zapowiedziało również Private Safety Processing](https://openai.com/pl-PL/index/offering-zero-data-retention-for-frontier-models/)==, czyli mechanizm pozwalający wykrywać niebezpieczne wzorce obejmujące wiele interakcji bez udostępniania ich treści pracownikom firmy.

To interesujący kierunek, bo próbuje pogodzić dwa sprzeczne wymagania: analizować zachowanie użytkownika w czasie, a jednocześnie nie odbierać przedsiębiorstwu kontroli nad danymi.

Podobny problem można rozwiązywać na poziomie infrastruktury. Microsoft deklaruje w ==[dokumentacji usługi Foundry](https://learn.microsoft.com/pl-pl/azure/foundry/responsible-ai/openai/data-privacy)==, że prompty, odpowiedzi i dane treningowe klientów korzystających z modeli hostowanych przez Azure nie są dostępne dla dostawcy bazowego modelu i bez zgody klienta nie są wykorzystywane do treningu modeli. Same modele są hostowane w środowisku Microsoft Azure, a nie w infrastrukturze ich pierwotnych dostawców.

Wyścig producentów AI zaczyna więc obejmować coś więcej niż samą inteligencję modeli.

#### Benchmark bezpieczeństwa danych

Przez kilka lat modele porównywano według stosunkowo prostych parametrów. Który lepiej programuje? Który ma większe okno kontekstowe? Który popełnia mniej błędów? Który jest szybszy i tańszy? Dla części przedsiębiorstw równie ważna może stać się nowa lista pytań: Gdzie przetwarzane są nasze informacje? Jak długo są przechowywane? Kto może otrzymać do nich dostęp? Co dzieje się z nimi po zakończeniu zadania? Czy zasady mogą zostać później zmienione? Czy możliwe jest zastosowanie własnych kluczy szyfrujących? Czy informacje pozostają w środowisku kontrolowanym przez klienta?

To może prowadzić do sytuacji, która jeszcze niedawno wydawałaby się dziwna: firma ma dostęp do modelu wyraźnie lepszego w benchmarkach, ale świadomie wybiera model nieco słabszy.

Powód nie musi mieć nic wspólnego z ceną.

Słabszy model może działać w środowisku, w którym organizacja zachowuje większą kontrolę nad swoimi informacjami. Dzięki temu firma może bezpiecznie przekazać mu pełny zestaw danych potrzebnych do wykonania zadania, podczas gdy lepszemu modelowi mogłaby udostępnić tylko ich część albo nie mogłaby użyć go w tym procesie w ogóle.

#### Nie jedna AI, ale kilka

Z tego wynika jeszcze jedna konsekwencja.

Firmy być może nie będą wybierały jednego „firmowego modelu AI” w taki sam sposób, w jaki wybierają pakiet biurowy czy komunikator. Znacznie bardziej prawdopodobny wydaje się podział według rodzaju zadania i poziomu wrażliwości informacji.

Jeden model może obsługiwać zwykłą komunikację, research czy pracę na publicznych materiałach. Inny trafi do programistów. Jeszcze inne rozwiązanie będzie wykorzystywane do pracy z najbardziej poufnymi danymi, być może w prywatnej chmurze albo infrastrukturze pozostającej pod pełniejszą kontrolą organizacji.

Pytanie „który model jest najlepszy?” może w takim układzie stracić część znaczenia. W jego miejsce pojawi się inne: **któremu modelowi możemy pokazać konkretne dane?**

To podejście może być szczególnie istotne wraz z rozwojem agentów AI. Model, który tylko odpowiada na pytanie, otrzymuje ograniczony fragment informacji. Agent wykonujący dłuższe zadanie może przeczytać dokumenty, przeszukać skrzynkę pocztową, zajrzeć do repozytorium i połączyć informacje z kilku systemów.

Im większą otrzymuje samodzielność, tym większy fragment organizacji zaczyna widzieć.

#### Najlepszy nie zawsze znaczy najlepszy dla firmy

Historia Palantira, Nvidii i Booz Allen nie pokazuje, że przedsiębiorstwa przestają ufać AI. Pokazuje coś bardziej interesującego: kryteria tego zaufania zaczynają się zmieniać. Możliwości modeli rosną. Jednocześnie coraz częściej są one używane dokładnie tam, gdzie znajdują się najcenniejsze informacje przedsiębiorstwa. Kod. Dane klientów. Strategie. Projekty nowych produktów. Wyniki badań. Wiedza, która stanowi o przewadze nad konkurencją.

Dlatego następny etap wdrażania AI może nie polegać wyłącznie na otwieraniu przed modelami kolejnych drzwi. Czasem trzeba będzie zdecydować, które pozostawić zamknięte.