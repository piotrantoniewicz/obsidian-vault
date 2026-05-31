---
type: "Web"
authors: "[[Przemek Jurgiel-Zyla]]"
url: "https://www.linkedin.com/pulse/17-podstawyai-czyli-spr%C3%B3bujmy-razem-stworzy%C4%87-webow%C4%85-jurgiel-zyla-7vedc/"
published: 2025-06-10
created: 2026-05-31
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "produkty-cyfrowe"
---


### Dzisiaj chciałbym Was zaprosić do wspólnego stworzenia aplikacji online - a co, zróbmy z tego startup - z wykorzystaniem narzędzi do programowania i AI. Od razu zastrzegam, że będę próbować wszystko tłumaczyć tak, żebyście na bazie niniejszej serii mogli spróbować powtórzyć.

> ale zanim zaczniemy - zaobserwuj mnie - codziennie pisze o AI, inwestycjach VC oraz technologiach / a jeśli interesuje Cię szkolenie z #podstawyAI, to zapraszam na [**https://podstawy.ai**](https://podstawy.ai/), gdzie można się zapisać na listę oczekujących (kolejna edycja wkrótce)

**I druga uwaga: pomijam konfigurację oprogramowania - gdyby była potrzebna pomoc w tym zakresie, to piszcie w komentarzach - mogę poświęcić 2-3 wpisy na opisanie narzędzi, z których będę korzystać.**

### Geneza pomysłu

Od niepamiętnych czasów mam domenę [dziekizawczoraj.pl](http://dziekizawczoraj.pl/), która powstała w wyniku dość zabawnej sytuacji na jednym z eventów starupowo-barcampowych w Trójmieście. Finalnie w pewnym gronie wszedł do potocznego użycia hashtag #dziekizawczoraj (kto pamięta czasy BLIPa?) i dość regularnie był używany w relacjach na następny dzień po różnego rodzaju imprezach (głównie networkowych i technologicznych). Tyle historii.

### Co chcemy zrobić?

Mamy nazwę projektu i na jej bazie chciałbym stworzyć prosty serwis internetowy, który... no właśnie - i tutaj zdaję się na Wasze pomysły. Który powinien w zabawny sposób nawiązywać do genezy pomysłu i pozwalać wykorzystywać jego funkcjonalność w niecnym procederze generowania podsumowań po różnego rodzaju imprezach. Do pomysłów zaraz wrócimy.

### Pierwszy krok - zaślepka na www

Mam tani hosting internetowy pozwalający przechowywać strony internetowe - póki nie zrobimy nic ładniejszego, to przyda nam się zaślepka. Zdjęcie znalazłem wśród darmowych na serwisie Unsplash\_com - ale nie stoi na przeszkodzie, żeby wygenerować za pomocą AI. Następnie z wykorzystaniem narzedzia Cursor (IDE - zintegrowane środowisko programistyczne) z podpiętymi modelami AI poprosiłem o:

> przygotuj dla mnie prostą, ale estetyczną i minimalistyczną stronę internetową, która będzie miała komunikat " [dziekizawczoraj.pl](http://dziekizawczoraj.pl/) - strona w budowie" - jako główny tytuł, poniżej opis "strona powstaje w ramach cyklu na linkedin:" i tutaj link: \[LINK DO BIULETYNU PODSTAWY AI\] oraz w kolejnej linijce: "skontaktuj się ze mną:" i link: \[LINK DO MOJEGO PROFILU NA LI\] stronę zapisz do @index.html oraz style do tej strony do @style.css, użyj grafiki @underconstruction.jpg

Efekt możecie zobaczyć na w/w stronie. Nic nie korygowałem, nie zmieniałem. Pierwszy efekt o razu wylądował tak jak widzicie.

### Drugi krok - wygenerowanie pomysłów

> prompt: zachowuj sie jak doświadczony twórca usług internetowych generujących duże zasięgi i budujących dobre efekty sieciowe, posiadam domenę [dziekizawczoraj.pl](http://dziekizawczoraj.pl/) - chciałbym stworzyć pod tym adresem jakiś zabawną usługę, z której będzie można wysłać do innej osoby podziękowanie za poprzedni dzień (personalizowaną - czyli bedzie wymagać wpisania kilku zdań kontekstu), raczej z zabawnym zabarwieniem/podtekstem oraz która pozwoli robić share wygenerowanego efektu na popularnych platformach typu X, facebook, etc, wygeneruj 5 pomysłów z największym potencjałem zasięgowym, projekt nie powinien generować video oraz opis przygotuj w skondensowanej formie

i tutaj (na tak dziwne zapytanie) modele poradziły sobie umiarkowanie. Otrzymałem wiele propozycji, które nazwałbym cringowymi. Poniżej te, które mi podeszły:

- **„Roast Gratulacyjny” (**Generator jednego zdania dziękczynienia i jednego dowcipnego „przytyku”, odbiorca czuje równocześnie docenienie i nutę żartu)
- **„Suchar za Wczoraj” (**Po wprowadzeniu sytuacji generator układa krótką, suchą puentę w stylu żartu. Przycisk automatycznego wrzucenia na tablicę znajomego)
- **Generator "Certyfikatów Przetrwania"** (Tworzenie humorystycznych certyfikatów podziękowania za "przetrwanie" konkretnego dnia. Użytkownik wpisuje kontekst (np. "spotkanie z teściową", "prezentacja dla CEO"), a system generuje oficjalnie wyglądający certyfikat z zabawnymi kategoriami jak "Zasługa za Utrzymanie Twarzy" czy "Medal za Nie Powiedzenie Tego Co Myślę".)
- **"Wczorajszy Bohater"** - Ranking Daily Heroes (nominacje znajomych za konkretne "heroiczne czyny" z poprzedniego dnia. System tworzy personalizowane grafiki z rankings lokalnych/globalnych bohaterów, kategorie jak "Bohater Kawy o 6 rano" czy "Ratownik Spotkań Teams")
- **"Wczorajszy Sędzia"** + Punktacja (System punktowy za różne "wyczyny" dnia poprzedniego. Użytkownicy przyznają punkty znajomym w kategoriach ("Przetrwanie bez kawy: +50 pkt", "Nie zabicie kolegi: +100 pkt"). Leaderboardy, streaki, achievement unlocks)

**Jeśli macie jakieś swoje pomysły, to zapraszam do komentarzy!**

### Krok trzeci, czyli PRD (project requirement description)

> PROMPT: przyjmijmy, że wybieram **Generator "Certyfikatów Przetrwania"**, zachowuj się teraz jak CPO i zaproponuj mi bardzo krótki PRD czyli project requirement description dla tego pomysłu przy założeniu, że serwis będzie działał na tanim hostingu, więc mam do dyspozycji PHP i mysql, będę korzystać z API do któregos z modeli językowych LLM i wszystkie kreatywne elementy będą generowane przez AI

wynik:

**PRD: dziekizawczoraj.pl - AI-Powered Generator Certyfikatów Przetrwania**

**Cel produktu**

Wiralowy generator humorystycznych certyfikatów za "przetrwanie" trudnych dni z AI-generated content i możliwością share'owania.

**Core Features MVP**

- **Formularz input**: Imię odbiorcy + opis sytuacji (max 300 znaków)
- **AI Content Generator**: LLM API generuje tytuł certyfikatu, kategorię i humorystyczny opis osiągnięcia
- **Certificate Builder**: PHP + GD tworzy PNG z AI-generated treścią na wybranym template wizualnym
- **Template stylistyczny**: 3-5 stylów graficznych (klasyczny, nowoczesny, retro)
- **Social share**: Auto-generated descriptions przez AI + share buttons
- **Cache system**: MySQL cache dla podobnych inputów (oszczędność API calls)

**Tech Stack**

- **AI**: OpenAI GPT-4o-mini API lub Anthropic Claude (prompt engineering)
- **Backend**: PHP 8.0+ + cURL (API calls) + GD library
- **Database**: MySQL (certificates, ai\_cache, templates)
- **Caching**: Input hash → cached AI response (7 dni TTL)

**User Flow**

1. Landing → formularz (imię + sytuacja)
2. AI processing → generowanie treści certyfikatu
3. Template selection → preview z AI content
4. Generate PNG → download + social share z AI description

### Krok czwarty - rozbudowa PRD o szczegółowe wymagania

...i to już zostawiam na kolejny krok, gdy finalnie - mam nadzieję, że pomożecie mi - wybierzemy co / jakiego rodzaju projekt robimy. **Komentarze są dla Was.**