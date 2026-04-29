---
type: "Web"
authors: "[[Mateusz Wojdalski]]"
url: "https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/claude-md-karpathy-78k-gwiazdek-claude-code-2026/?utm_source=newsletter&utm_medium=email&utm_term=2026-04-29&utm_campaign=Copilot+na+liczniku+GPT-5+5+i+65+mld+dla+Anthropic"
published: 2026-04-24
created: 2026-04-29
tags:
---


Zwykły plik w formacie markdown w tydzień zebrał 81 tysięcy gwiazdek na GitHubie. Bez kodu, bez funkcji, bez frameworka. Siedemdziesiąt linii instrukcji dla Claude Code: co model ma robić, czego nie wolno mu ruszać i kiedy zamiast pisać ma zadać pytanie. Autorem jest Forrest Chang, który wydestylował te zasady z postów Andreja Karpathy’ego. Karpathy to były szef AI w Tesli i współzałożyciel OpenAI, który od miesięcy otwarcie pisze, że modele AI kodują jak stażyści po tygodniu stażu. Dlatego warto sprawdzić, co dokładnie siedzi w tym pliku, skąd nagle taka popularność i czy ma sens kopiowanie go do własnych projektów.

## Co to w ogóle jest plik CLAUDE.md

CLAUDE.md to plik z instrukcjami, który Claude Code czyta automatycznie na początku każdej sesji w danym projekcie. Wystarczy wrzucić go do katalogu roboczego, a model traktuje zawarte tam reguły jako swoje stałe wytyczne – niezależnie od tego, o co akurat prosisz w oknie czatu.

W praktyce pełni rolę, którą w nowej firmie pełni instrukcja dla świeżo zatrudnionego pracownika. Nie opisujesz każdej prośby od zera, tylko raz uzgadniasz czego zawsze trzymać się mamy i czego nigdy nie robimy. [Więcej o tym jak Claude Code zarządza limitami i kontekstem](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/claude-code-limity-tokeny-jak-nie-tracic-quota) – to jest osobny temat, ale wpływa na to, jak dobrze taki plik w ogóle działa.

Tu ważne rozróżnienie. W świecie Claude Code krąży dziś kilka pojęć, które brzmią podobnie i łatwo je pomylić. Oficjalne **skille** Anthropic (katalog `.claude/skills/`) to specjalizowane polecenia, które model odpala dopiero wtedy, gdy uzna że pasują do kontekstu. **Plik CLAUDE.md** działa inaczej – jest czytany zawsze, na starcie, dla każdej rozmowy. Dwa różne mechanizmy, dwie różne role. Kto chce przy okazji zrozumieć trzeci z rodziny – [porównanie MCP i skilli tłumaczy te warstwy po kolei](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/mcp-vs-skills-agenty-ai-claude-code-2026).

## Skąd nagle 81 tysięcy gwiazdek w tydzień

Historia jest krótka, ale pokazuje głód społeczności lepiej niż jakakolwiek ankieta. Karpathy opublikował na platformie X serię obserwacji o tym, gdzie modele AI wywalają się przy kodowaniu. Zgadują zamiast pytać. Produkują tysiąc linii tam, gdzie wystarczy sto. Przy okazji jednej naprawy refaktorują połowę pliku. Ignorują instrukcje i realizują coś, co sobie dośpiewują.

Forrest Chang, developer budujący platformę Multica do zarządzania agentami kodującymi, zebrał te obserwacje i zamienił je w jeden plik CLAUDE.md z czterema zasadami. Wrzucił go na GitHub jako repozytorium [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills). **13 kwietnia 2026 plik zebrał 5 828 gwiazdek w ciągu jednego dnia, stając się drugim najczęściej gwiazdkowanym repozytorium na platformie tego dnia** – zaraz po jądrze Linuksa. Tydzień później licznik wskazywał 78 tysięcy. W chwili pisania tego artykułu jest już 81 500.

> Trudno o lepszy dowód, że problem z kodowaniem przez AI nie leży w mocy modeli, tylko w instrukcji, jaką im dajemy.

Co w tej historii jest ciekawe. Nie powstał nowy framework, nie wypuszczono modelu, nie ogłoszono benchmarku. Popularność osiągnął zwykły plik tekstowy, który po prostu mówi modelowi, jak się ma zachowywać. Efekt? Dla społeczności programistów rozczarowanych tym, że Claude Code “z automatu” przepisuje pół projektu, ten plik zadziałał jak objawienie.

## Cztery zasady Karpathy’ego – co naprawiają w Claude Code

Cały plik mieści się na dwóch ekranach. Cztery zasady, każda z krótkim opisem i testem kontrolnym, czy jesteś zgodny z regułą. Struktura jest prosta, bo ma być prosta – plik zużywa miejsce w oknie kontekstu modelu, a im dłuższy, tym mniej zostaje na prawdziwą pracę.

### Think Before Coding – przestań zgadywać

Motto tej zasady brzmi: *“Don’t assume. Don’t hide confusion. Surface tradeoffs.”* – nie zakładaj, nie ukrywaj wątpliwości, pokazuj kompromisy. Cel jest bezpośredni: model ma przestać zgadywać interpretację prośby użytkownika i zamiast tego wyłożyć co rozumie, a czego nie.

Klasyczny przykład z poradników Changa: użytkownik pisze “wyeksportuj użytkowników”. Bez tej zasady Claude Code sam decyduje – wszystkich, w formacie JSON, ze wszystkimi polami. Z zasadą – zadaje trzy pytania: których użytkowników, w jakim formacie, które pola. To jak kurier, który dzwoni zamiast zostawiać paczkę pod drzwiami na deszczu. Dokładnie tam, gdzie chciałeś i dokładnie to, co zamawiałeś.

### Simplicity First – 200 linii tam gdzie wystarczy 50 to bug

Motto: *“Minimum code that solves the problem. Nothing speculative.”* Tłumaczenie jest proste – napisz minimum, które rozwiązuje problem, nic poza tym. Bez abstrakcji na zapas, bez konfigurowalności “na wypadek”, bez obsługi błędów, które nie mogą się zdarzyć.

Przykład w materiałach Changa jest brutalny. Claude Code poproszony o funkcję liczącą rabat produkuje Strategy Pattern z pięcioma klasami, interfejsem i fabryką. Dobrze napisany, wszystko zgodnie ze sztuką. Po wdrożeniu zasady – dwuliniowa funkcja, która po prostu zwraca wynik. Różnica w utrzymaniu? Gigantyczna, bo każda zbędna warstwa to coś, co ktoś musi zrozumieć, zanim cokolwiek zmieni. Test kontrolny z pliku jest prosty: *czy doświadczony inżynier powiedziałby, że to jest przekombinowane?*

### Surgical Changes – tylko to, o co prosiłem

Motto: *“Touch only what you must. Clean up only your own mess.”* – ruszaj tylko to, co musisz, sprzątaj po sobie, nie po innych. Ta zasada wprost zakazuje poprawiania kodu obok, zmiany formatowania czy dodawania “lepszych” komentarzy przy okazji innego zadania.

To jest bolączka, którą zna każdy, kto pracuje z Claude Code dłużej niż tydzień. Prosisz o poprawkę w jednej funkcji, a w `git diff` widzisz zmiany w dziesięciu plikach, bo model przy okazji “poprawił” formatowanie cudzysłowów, dodał typy i zrefaktorował pętle. Zasada Karpathy’ego mówi jasno: każda zmieniona linia musi wynikać bezpośrednio z prośby użytkownika. Kropka.

W praktyce to jak dentysta, który leczy wyznaczonego zęba. Nie “przy okazji” nie rusza sąsiednich, bo mu się wydają podejrzane. Najpierw pokazuje pacjentowi, że coś widzi, prosi o zgodę i dopiero wtedy działa.

### Goal-Driven Execution – kryteria sukcesu, nie instrukcje

Motto: *“Define success criteria. Loop until verified.”* Wskaż cel i sposób weryfikacji, a nie konkretną ścieżkę. Zamiast prosić “popraw ten kod”, lepiej: “napisz test, który obecnie nie przechodzi, potem zmień kod tak, żeby przechodził”. Model sam iteruje aż do osiągnięcia celu.

Dlaczego to działa? Bo LLM-y są okropnie dobre w pracy pod weryfikowalne kryterium, a okropnie słabe w abstrakcyjnych prośbach. “Poprawa” to zbyt mgliste zadanie, ale “testy mają przechodzić” – to model rozumie i potrafi wytrwale sprawdzać, czy już są zielone.

Kurs n8n 2.0 · Kodożercy

### Automatyzacja to dziś jedna z najbardziej poszukiwanych umiejętności

Firmy szukają ludzi którzy łączą procesy z narzędziami. Kurs n8n 2.0 na Kodożercach da Ci praktyczne umiejętności – webhooki, API, automatyczne przepływy danych – które możesz pokazać już jutro.

[Zobacz program kursu →](https://kursy.kodozercy.pl/automatyzacja-n8n/?utm_source=devstockacademy-blog&utm_medium=article-banner&utm_campaign=kurs-n8n-20&utm_content=claude-md-karpathy-78k-gwiazdek-claude-code-2026)

![Kurs n8n 2.0 - Kodożercy](https://devstockacademy.pl/wp-content/uploads/2026/03/Produkt-automatyzacje-pudelko-webp.png)

## Jak zainstalować plik CLAUDE.md u siebie

Forrest Chang zostawił trzy drogi wdrożenia i każda z nich zajmuje mniej niż minutę. Warto na początek zacząć od globalnej instalacji, a jeśli plik zacznie działać zbyt agresywnie w konkretnym projekcie – podmienić go na wersję lokalną.

**Instalacja globalna przez plugin Claude Code** to najprostszy wariant. Wystarczy polecenie `/plugin marketplace add forrestchang/andrej-karpathy-skills`, a następnie `/plugin install andrej-karpathy-skills@karpathy-skills`. Od tej chwili każda sesja Claude Code w każdym projekcie rusza z wgranymi czterema zasadami.

**Per projekt** to opcja dla tych, którzy chcą mieć kontrolę nad tym, gdzie ten plik się pojawia. Wystarczy pobrać oryginalny plik z repozytorium i wrzucić go do katalogu głównego projektu pod nazwą `CLAUDE.md`. Claude Code wykrywa go automatycznie, bez żadnej konfiguracji.

**Dla Cursor** Chang dodał też folder `.cursor/rules/` z bliźniaczą wersją zasad. Dwa edytory, te same cztery reguły. Działa też z innymi narzędziami czytającymi pliki typu `*rules.md`.

Warto pamiętać, że to nie jest “ostateczna prawda”, tylko punkt startowy. Autor celowo zostawił plik krótki – około siedemdziesięciu linii – żeby zmieścił się obok twoich własnych zasad projektowych. Konwencje typowania w TypeScripcie, standardy API, wymagania testów – dopisuj je poniżej sekcji Karpathy’ego i wszystko dalej działa.

## Czego plik CLAUDE.md nie rozwiązuje

Entuzjazm społeczności wokół tych zasad nie oznacza, że są one lekiem na wszystko. W tygodniu po wybuchu popularności pojawiła się ciekawa krytyka na blogu “Mastering Product HQ”, którą warto przyswoić zanim zainstalujesz plik i odetchniesz z ulgą.

Autor wprost nazywa ograniczenie: *“plik Karpathy’ego jest napisany dla inżyniera, który pracuje sam nad kodem”*. Cztery zasady świetnie tłumią tendencję modelu do nadgorliwości – zgadywania, przekombinowywania, refaktoryzowania wszystkiego dookoła. Ale nie tłumią problemu, który w produktach cyfrowych jest droższy. Pisanie świetnego kodu do problemu, którego nikt nie ma.

> AI nie zatrzyma Cię i nie zapyta, czyj problem tak naprawdę rozwiązujesz. Jeśli prośba brzmi mętnie, po prostu wykona coś, co brzmi podobnie.

Zasady Karpathy’ego pomagają pisać mniej, precyzyjniej i czysto. Nie pomagają ocenić, czy w ogóle warto to pisać. Dla zespołu produktowego to jest druga, tak samo ważna warstwa, która wymaga osobnych reguł – walidacji założeń, definicji sukcesu mierzonego wpływem na użytkownika, dokumentowania decyzji. Wbijając sobie CLAUDE.md do projektu warto pamiętać, co on załatwia, a co zostaje po twojej stronie.

## FAQ – najczęstsze pytania o plik CLAUDE.md

### Czy plik CLAUDE.md działa z każdym modelem Anthropic?

Tak. CLAUDE.md czyta nie konkretny model, tylko narzędzie Claude Code, niezależnie od tego, czy pod spodem pracuje Haiku, Sonnet czy Opus. Zasady zachowują się tak samo na każdej wersji. Różnica dotyczy raczej tego, jak wiernie model ich przestrzega – nowsze i większe modele trzymają się instrukcji ściślej niż mniejsze. Jeśli korzystasz z Haiku dla oszczędności, warto monitorować czy zasady faktycznie są respektowane w trudniejszych zadaniach.

### Czy mogę połączyć zasady Karpathy’ego z moimi własnymi regułami projektu?

Oczywiście i o to chodzi. Chang celowo zrobił plik krótki, żeby zmieścił się obok lokalnych wytycznych. W praktyce najczęstszy układ wygląda tak: na górze pliku cztery zasady z pliku Karpathy’ego, pod spodem twoja sekcja “Zasady projektu” z konwencjami nazewnictwa, stackiem technologicznym, wymaganiami testów. Claude Code czyta cały plik jako jeden kontekst, więc zasady się nie konkurują, tylko dopełniają.

### Czy ten plik działa też z Cursor, Windsurf lub innymi narzędziami?

Tak, z zastrzeżeniem formatu. Dla Cursor w repozytorium jest gotowy folder `.cursor/rules/` z tymi samymi zasadami przetłumaczonymi na format, którego używa ten edytor. Windsurf, Cline i inne narzędzia czytają zwykle pliki typu `*rules.md` lub `.clinerules` – dla nich wystarczy skopiować treść pliku Karpathy’ego i zapisać pod odpowiednią nazwą. Mechanika “jawnych instrukcji systemowych” działa tak samo w każdym z tych narzędzi.

### Czy muszę instalować cały plugin, czy wystarczy sam plik?

Wystarczy sam plik. Plugin to wygodniejsza droga, bo Claude Code synchronizuje zasady globalnie – raz zainstalowany, działa we wszystkich projektach bez kopiowania. Jeśli jednak wolisz pełną kontrolę nad lokalizacją i wersją zasad, pobierz sam plik `CLAUDE.md` z repozytorium Forresta Changa i wrzuć go do katalogu głównego projektu. Claude Code wykryje go automatycznie przy następnym starcie sesji.

## Podsumowanie

Plik CLAUDE.md od Forresta Changa zebrał 81 tysięcy gwiazdek na GitHubie w tydzień, bo wypełnił konkretną lukę. Claude Code potrafi świetnie pisać kod, ale bez jasnych zasad ma tendencję do nadgorliwości – zgaduje, przekombinowuje i refaktoruje kod, o który nikt nie prosił. Cztery zasady Karpathy’ego, ubrane w krótki plik markdown, wpisują się idealnie jako przeciwwaga: pomyśl zanim napiszesz, pisz minimum, nie ruszaj cudzego kodu, działaj pod weryfikowalny cel.

To nie jest lek na wszystko. Zasady pomagają pisać precyzyjnie, ale nie pomogą ocenić, czy w ogóle warto daną rzecz pisać. Dlatego najlepiej traktować je jako punkt startowy: zainstaluj, dopisz własne konwencje projektowe i dostosuj do tego, jak pracuje twój zespół. W sumie siedemdziesiąt linii tekstu, godzina wdrożenia i realna zmiana w tym, jak Claude Code przestaje Cię zaskakiwać.

Newsletter · DevstockAcademy & Kodożercy

### Bądź na bieżąco ze światem IT, AI i automatyzacji

Co wtorek: newsy z branży, praktyczne tipy i narzędzia które warto znać. Zero spamu.