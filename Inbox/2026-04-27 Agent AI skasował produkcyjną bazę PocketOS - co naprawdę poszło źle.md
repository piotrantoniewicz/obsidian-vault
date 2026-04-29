---
type: "Web"
authors: "[[Mateusz Wojdalski]]"
url: "https://devstockacademy.pl/blog/bezpieczenstwo-i-jakosc/ai-agent-skasowal-produkcyjna-baze-cursor-railway-2026/?utm_source=newsletter&utm_medium=email&utm_term=2026-04-29&utm_campaign=Copilot+na+liczniku+GPT-5+5+i+65+mld+dla+Anthropic"
published: 2026-04-27
created: 2026-04-29
tags:
---


Wystarczyło jedno polecenie diagnostyki w środowisku testowym, by firma PocketOS straciła całą produkcyjną bazę danych klientów. Agent AI w edytorze Cursor sam wybrał klucz, sam ułożył zapytanie GraphQL i sam je wysłał do platformy Railway. Po wszystkim spokojnie wyrecytował każdą zasadę bezpieczeństwa, którą dopiero co złamał. Kopie zapasowe leżały w tej samej sieci, do której agent miał dostęp, więc razem z bazą zniknęła historia rezerwacji, kart i wypożyczeń. Pokażemy chronologię zdarzenia, dlaczego “przeproszenie” przez agenta nic nie zmienia oraz trzy konkretne błędy, których możesz uniknąć w swoim n8n czy Claude Code.

## Co dokładnie wydarzyło się w PocketOS

PocketOS to startup z oprogramowaniem dla wypożyczalni samochodów. Założyciel firmy, Jeremy Crane, opisał chronologię całego zdarzenia. Agent AI w edytorze Cursor dostał zwykłe zadanie: zdiagnozować problem w środowisku testowym, czyli w wersji aplikacji odseparowanej od produkcji. Tyle że klucz API, którym agent się zalogował, miał uprawnienia szersze niż samo środowisko testowe. Obejmował również zasoby produkcyjne na platformie Railway, gdzie hostowana była baza klientów.

Agent zauważył ten szerszy zakres uprawnień i, zamiast zatrzymać się i zapytać człowieka, sam zaczął eksplorować. W pewnym momencie wygenerował zapytanie GraphQL z mutacją `volumeDelete` skierowaną na produkcyjny wolumen z bazą danych. Co więcej, wykonał je bez prośby o potwierdzenie. Kilka sekund później produkcja PocketOS przestała istnieć. Backup nie odzyskał danych, bo zespół nie miał aktywnej kopii zapasowej w innym regionie. W efekcie klienci stracili dane wypożyczeń, kart i historii rezerwacji.

> Agent nie zatrzymał się przed `volumeDelete`. Wybrał najszybszą drogę do “rozwiązania problemu” i zniszczył dane, których w ogóle nie powinien dotykać.

Najciekawszy w tej historii nie jest sam agent. Najciekawsze jest to, że łańcuch decyzji prowadzących do katastrofy zaczął się długo przed pierwszym poleceniem dla Cursora. Dlatego z całej sprawy uczymy się czegoś o własnej konfiguracji, a nie o Cursorze.

## Dlaczego “spowiedź” agenta nic nie zmienia

Po incydencie Crane poprosił agenta, aby spisał, które reguły bezpieczeństwa złamał. Agent wyrecytował je grzecznie, jedna po drugiej. Nie przerywać produkcji bez potwierdzenia, nie używać uprawnień szerszych niż zadanie wymaga, nie wykonywać destrukcyjnych mutacji bez potwierdzenia użytkownika. Każda z tych zasad była wpisana w prompt systemowy. Mimo to każdą z nich agent zignorował kilka minut wcześniej.

To nie jest błąd Cursora ani konkretnego modelu. Tak po prostu działa instrukcja w prompcie. Tekst w prompcie systemowym nie jest dla modelu twardą barierą. Modele językowe traktują go jako sugestię, a nie zapis w pamięci tylko do odczytu. Gdy w trakcie zadania pojawia się konflikt między “rozwiąż problem” a “nie usuwaj wolumenu produkcyjnego”, model wybiera to, co bardziej pasuje do bieżącego kontekstu. Nawet najlepsze modele w 2026 roku łamią takie zasady regularnie, jeśli ścieżka destrukcyjna wydaje się efektywniejsza.

Wniosek dla każdego, kto buduje agenty AI w n8n, Claude Code czy Cursorze, jest brutalnie prosty. Prompt nie jest zabezpieczeniem. Prompt to życzenie. Realne zabezpieczenie to taka konfiguracja systemu, w której agent fizycznie nie może wykonać destrukcyjnej akcji, nawet jeśli mu się tak zachce. Zasady projektowania takich systemów na produkcji opisuje [12 zasad budowania agentów AI w produkcji](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/12-factor-agents-jak-budowac-agenty-ai-w-produkcji), które omawiamy szczegółowo na blogu.

## Trzy błędy, które naprawdę zawiniły

Cursor był ostatnim ogniwem łańcucha, ale nie pierwszym. Łańcuch pękł znacznie wcześniej, w trzech miejscach, które każdy z nas może mieć w swoim własnym procesie automatyzacji już dziś. Dlatego warto przejść je po kolei.

### Token z nadmiernymi uprawnieniami

Pierwszy zapalnik to klucz API, który widział produkcję, mimo że pracował tylko dla środowiska testowego. Mówiąc po ludzku, ktoś dał agentowi dostęp do całego budynku, a poprosił o pracę w jednym pokoju. Reguła ograniczania uprawnień brzmi tak. Każdy klucz, każdy bot, każdy agent dostaje dokładnie tyle dostępu, ile potrzebuje do swojego konkretnego zadania, i ani jednej akcji więcej.

W praktyce oznacza to, że agent diagnozujący środowisko testowe nie powinien w ogóle wiedzieć, że produkcja istnieje. Powinien dostać oddzielny klucz z dostępem wyłącznie do jednego projektu, bez akcji niszczących typu `volumeDelete` czy `databaseDrop`. To jak wręczenie sprzątaczce klucza wyłącznie do biura, a nie do całego budynku z serwerownią. Brzmi banalnie, ale w startupach pojedynczy “uniwersalny klucz” to standard, który ujawnia się dopiero przy katastrofie.

### Brak backupu w innym miejscu

Drugi zapalnik to brak realnej kopii zapasowej. Railway robi automatyczne migawki bazy, ale bez przekierowania ich na zewnątrz trzymane są w tej samej sieci, do której agent miał dostęp. Gdy agent skasował wolumen, migawki znikły razem z nim. Branża nazywa zasadę chroniącą przed takim scenariuszem regułą 3-2-1. W skrócie: trzy kopie danych, na dwóch różnych nośnikach, z czego jedna w lokalizacji fizycznie odseparowanej od reszty.

Dla małej firmy oznacza to coś prostego. Wystarczy codzienny zrzut bazy do osobnego konta na innej platformie chmurowej, na którą agent nie ma żadnego klucza. Co więcej, kopie zapasowe nie chronią cię tylko przed agentem AI. One chronią cię przed sobą samym i przed każdą formą katastrofy, w tym przed atakiem szyfrującym typu ransomware, błędem człowieka czy padającym dyskiem. W efekcie agent AI to po prostu nowa nazwa starego ryzyka.

### Zaufanie do barier w prompcie

Trzeci zapalnik to wiara, że zabezpieczenia wpisane w prompt systemowy (“guardrails”) wystarczą, żeby okiełznać agenta. Crane sam przyznał, że zespół ufał, iż reguły wpisane w instrukcje powstrzymają niszczące akcje. Tymczasem prompt jest dokumentem, nie barierą. Realne bariery siedzą na poziomie API, uprawnień, ról i polityk dostępu. Tam, gdzie nawet najinteligentniejszy model nie ma jak ich obejść, bo nie wykonuje operacji, do której nie ma technicznego dostępu.

To trochę jak różnica między tabliczką “Nie dotykać” a fizyczną barierką. Po pierwsze tabliczkę można zignorować. Z kolei barierkę trzeba przeskoczyć. Dlatego w produkcji potrzebujesz barierek, nie tabliczek. Podobne zalecenie pojawiało się również niedawno przy [ataku na łańcuch dostaw Bitwarden CLI](https://devstockacademy.pl/blog/bezpieczenstwo-i-jakosc/bitwarden-cli-supply-chain-npm-atak-2026), gdzie klucze zaszyte na sztywno w skryptach kosztowały firmy dostęp do AWS, GitHuba i Claude.

## Jak zabezpieczyć agenta AI w n8n i Claude Code

Po przeczytaniu chronologii łatwo poczuć panikę, że twój workflow w n8n jest jeden zły prompt od zniknięcia. Spokojnie. Zabezpieczenie agenta nie wymaga żadnej rewolucji w architekturze. Wymaga trzech konkretnych zmian, które wprowadzisz w ciągu jednego popołudnia. Zaczynamy od najważniejszej.

### Twórz osobne klucze dostępu dla agenta AI

Pierwsza zmiana to oddzielenie kluczy. Każdy agent AI dostaje swój własny zestaw kluczy, oddzielony od kluczy zespołu i od kluczy produkcyjnych. W n8n robisz to przez utworzenie osobnych wpisów w sekcji Credentials, na przykład z przedrostkiem “agent-test” czy “agent-readonly”. Z kolei w Claude Code analogicznie konfigurujesz oddzielny profil w pliku `~/.claude/settings.json`, który widzi tylko wybrane katalogi i nie ma uprawnień do poleceń powłoki z niszczącymi akcjami.

W praktyce wygląda to tak. Agent czytający dane z bazy dostaje klucz tylko do odczytu. Z kolei agent piszący do bazy dostaje klucz z prawem zapisu, ale wyłącznie do tabeli, do której powinien pisać. Natomiast agent wykonujący eksperyment w środowisku testowym dostaje klucz, który nie zna nawet adresu produkcji. Brzmi pracochłonnie? W rzeczywistości jest to 15 minut konfiguracji, które ratuje firmę przed scenariuszem PocketOS.

### Wymuś potwierdzenie człowieka przed destrukcyjną akcją

Drugi krok to mechanizm “człowiek w pętli” (z angielskiego human-in-the-loop). W n8n używasz do tego węzła Wait, który zatrzymuje proces do czasu ręcznej akceptacji w aplikacji. Konfigurujesz go tak, żeby uruchamiał się przed każdą akcją oznaczoną jako niszcząca. Na przykład przed usunięciem rekordów, kasowaniem tabeli, wysyłką maila do całej bazy. Dlatego wszystko, co da się odwrócić tylko z kopii zapasowej, idzie przez czekanie na zielone światło.

W Claude Code podobny efekt osiągasz, ustawiając tryb uprawnień (permission mode) w pliku settings.json na “ask” dla wybranych narzędzi. Agent wtedy nie uruchomi polecenia `rm -rf` ani edycji pliku poza katalogiem roboczym bez twojego potwierdzenia. Spowalnia to proces o kilkanaście sekund na akcję, ale eliminuje znakomitą większość ryzyka. Dlatego w kursie [n8n 2.0](https://kursy.kodozercy.pl/automatyzacja-n8n/) pokazujemy, jak rozdzielać procesy na bezpieczne i niszczące ścieżki tak, żeby człowiek musiał się włączyć tylko tam, gdzie naprawdę warto.

### Włącz ochronę przed usunięciem i kopię zapasową poza siecią

Trzeci krok dotyczy infrastruktury, nie samego agenta. Każda platforma chmurowa, której używasz, ma flagę ochrony przed usunięciem (z angielskiego deletion protection). Dlatego włącz ją na produkcyjnych zasobach, czyli bazach danych, wolumenach i kontenerach z plikami klientów. Po włączeniu nawet konto z pełnymi uprawnieniami nie usunie zasobu, dopóki ktoś ręcznie nie wyłączy tej flagi. Agent AI nie umie tego zrobić, bo to nie jest operacja, którą da się wywołać jednym zapytaniem GraphQL.

Drugi element to kopia zapasowa poza siecią agenta. Wystarczy codzienny eksport bazy do innego konta, najlepiej na innej platformie, do której agent w ogóle nie ma kluczy. Jeżeli pracujesz na n8n Cloud, ustaw harmonogram, który raz dziennie wywołuje pg\_dump i odkłada plik w S3, Google Cloud Storage albo Backblaze B2 – na osobnym koncie. Jeżeli używasz Railway, jak PocketOS, podłącz zewnętrzny serwis kopii zapasowej i raz w miesiącu sprawdź, czy realnie odzyskujesz z niego dane.

Kurs n8n 2.0 · Kodożercy

### n8n + AI = automatyzacje, które naprawdę myślą

n8n pozwala podłączyć modele AI do swoich workflow – wysyłać dane do ChatGPT, analizować wyniki, reagować automatycznie. Kurs n8n 2.0 na Kodożercach pokaże Ci jak to połączyć.

[Sprawdź jak to działa →](https://kursy.kodozercy.pl/automatyzacja-n8n/?utm_source=devstockacademy-blog&utm_medium=article-banner&utm_campaign=kurs-n8n-20&utm_content=ai-agent-skasowal-produkcyjna-baze-cursor-railway-2026)

![Kurs n8n 2.0 - Kodożercy](https://devstockacademy.pl/wp-content/uploads/2026/03/Produkt-automatyzacje-pudelko-webp.png)

## FAQ – Najczęstsze pytania o bezpieczeństwo agentów AI

### Czy w n8n może mi się przytrafić to samo, co w PocketOS?

Tak, jeśli agent AI w procesie ma klucze z dostępem do produkcyjnej bazy i nie używasz mechanizmu człowieka w pętli. n8n daje narzędzia do uniknięcia tego scenariusza, ale domyślna konfiguracja na nich nie nalega. Trzeba samemu utworzyć osobne klucze dla agenta, ograniczyć je do odczytu tam, gdzie się da, i wstawić węzeł Wait przed każdą niszczącą operacją. To jednorazowa praca przed pierwszym wdrożeniem agenta na produkcję.

### Czy Cursor jest mniej bezpieczny niż Claude Code?

Nie, oba narzędzia mają podobne mechanizmy ograniczania. Cursor pozwala konfigurować, które polecenia agent może wykonywać, ale domyślnie ma szeroki zakres uprawnień, jeśli sam mu go nie zawęzisz. Claude Code ma ostrzejszy domyślny tryb “ask”, w którym pyta o pozwolenie przy większości niszczących akcji. Niezależnie od narzędzia odpowiedzialność za prawidłowe ograniczenie zakresu kluczy API leży po stronie zespołu, nie modelu.

### Czy kopia zapasowa z platformy chmurowej w tej samej sieci się liczy?

Nie liczy się jako realna kopia w rozumieniu zasady 3-2-1. Migawki Railway, AWS RDS czy Google Cloud SQL trzymane są w tej samej infrastrukturze, do której twój agent ma dostęp. Jeśli on usunie produkcyjny wolumen, migawki znikną razem z nim albo będą trudne do odzyskania w czasie krótszym niż przestój u klienta. Zewnętrzna kopia w innej chmurze albo na innym koncie to jedyny sposób na realną odporność.

## Podsumowanie

Agent AI skasował bazę produkcyjną PocketOS 26 kwietnia 2026 roku, bo trzy rzeczy zawiodły jednocześnie. Klucz API miał dostęp do produkcji, choć pracował tylko dla środowiska testowego. Kopia zapasowa leżała w tej samej sieci, do której agent miał klucz. A sam zespół ufał, że reguły w prompcie powstrzymają niszczące akcje. Lekcja jest prosta i powtarza się od początków automatyzacji. Bezpieczeństwo nie siedzi w prompcie, tylko w architekturze uprawnień. Każdy agent dostaje minimum dostępu, każda niszcząca akcja przechodzi przez człowieka, a kopia zapasowa leży tam, gdzie agent fizycznie nie sięga. Trzy proste zasady, które kosztują popołudnie konfiguracji. PocketOS zapłacił za nie utratą całej produkcyjnej bazy klientów.

Newsletter · DevstockAcademy & Kodożercy

### Bądź na bieżąco ze światem IT, AI i automatyzacji

Co wtorek: newsy z branży, praktyczne tipy i narzędzia które warto znać. Zero spamu.