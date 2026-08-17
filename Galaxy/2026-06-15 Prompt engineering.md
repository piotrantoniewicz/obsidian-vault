---
categories: Concept
tags:
  - prompt-engineering
  - narzędzia-AI
  - szkolenia-AI
created: 2026-06-15
updated: 2026-08-17
relevance: wysoka
sources:
  - "[[2025-06-22 9 ChatGPT & Claude Writing Tips (to get CRAZY GOOD outputs)]]"
  - "[[2026-01-24 How to use AI as a ghostwriter in 2026]]"
  - "[[2026-02-24 Day 2 - Writing Prompts for Best Results]]"
  - "[[2025-10-19 An Opinionated Guide to Using AI Right Now]]"
  - "[[2025-09-29 Effective context engineering for AI agents]]"
  - "[[2025-07-28 Beyond Prompts How Context Engineering Could Revolutionize Your Nonprofit AI Workflows]]"
  - "[[2025-12-02 AI, która doskonali twoją pracę z AI]]"
  - "[[2025-07-31 A prompt that builds your landing page (by asking the right questions)]]"
  - "[[2026-08-10 Claude Code for normal people skills, voice mode, and how to collaborate with AI]]"
  - "[[2026-08-12 AI w zarządzaniu projektami Asana i Claude w tandemie]]"
  - "[[2026-06-18 Answers to your FAQ on funding AI]]"
  - "[[2026-08-04 5 hacks I used to build a profitable app]]"
  - "[[2026-07-27 Robots Dating Robots]]"
  - "[[2026-07-29 How I Use AI to Research Funders Before I Write the Grant]]"
---

# Prompt engineering (projektowanie promptów)

Prompt engineering to **rzemiosło formułowania instrukcji (promptu) dla modelu językowego tak, by zmaksymalizować jakość odpowiedzi**. To atomowa, najstarsza warstwa pracy z [[LLM]] — skupia się na *treści i strukturze samego polecenia*: co napisać, jak to ułożyć, jakie przykłady i format dołączyć. Centralna diagnoza powtarzająca się we wszystkich źródłach jest jedna i kontrintuicyjna: **kiepski output to niemal zawsze błąd promptu, nie słabość modelu** (*garbage in, garbage out*). Trzy najczęstsze błędy to: instrukcje zbyt ogólne, wiele zadań upchniętych w jeden prompt i brak kontekstu. Pojęcie jest węższym poprzednikiem [[2026-06-15 Context engineering|context engineeringu]]: prompt engineering pisze *instrukcję*, context engineering zarządza *całym oknem*. Choć bywa ogłaszane jako „przestarzałe" (modele coraz lepiej domyślają się intencji), pozostaje **kompetencją operacyjną** — bez umiejętności precyzyjnego zwerbalizowania zadania nie da się ani zbudować dobrego kontekstu, ani niczego zautomatyzować.

---

## Kluczowe mechanizmy

**1. Trzy tryby promptowania (Cole) — najpierw cel, potem technika**
Nicolas Cole rozróżnia trzy *zasadniczo różne* tryby, bo każdy wymaga innego promptu:
- **Rabbit Hole** — eksploracja tematu, AI jak wyszukiwarka; dobre do nauki, słabe do produkcji treści.
- **Brainstorming** — AI jako partner do testowania pomysłów; wymaga dużo kontekstu o projekcie, firmie, odbiorcy.
- **Automation** — odwrotna inżynieria opanowanego procesu w powtarzalny prompt; największa dźwignia, ale i największy nakład na start.
Mylenie trybów to częsta przyczyna rozczarowań — prompt do eksploracji nie nadaje się do produkcji.

**2. Język obiektywny i nazwane formaty**
Słowa subiektywne („napisz *świetny* post", „*angażujący*") są dla modelu bezużyteczne — nie niosą sygnału. Zamiast tego: instrukcja obiektywna („napisz myśl przywódczą w max 280 znakach w formacie X"). Każdy powtarzalny format treści powinien mieć **nazwę** (*Problem/Solution*, *Contrarian Take*, *Story Framework*) — to wymusza klarowność i zapobiega mieszaniu stylów przez model.

**3. Prompty pojedyncze vs modularne (singular vs modular)**
Nie łącz 8 zadań w jednym prompcie. Złożone zadanie rozbij na **sekwencję małych, osobnych promptów** (research → tytuł → outline → moduły → styl). Zlecanie AI całej książki jednym promptem to błąd; łańcuch precyzyjnych kroków daje kontrolę i jakość. To prompt-engineeringowy odpowiednik dekompozycji i wczesna intuicja architektur wieloagentowych.

**4. Struktura, przykłady i instrukcje dostarczania**
- **Struktura XML** (`task / audience / format / tone / requirements`) drastycznie podnosi jakość — najszybszy sposób na lepszy output bez dodatkowych narzędzi.
- **Przykłady muszą być zgodne z regułami** — niespójność reguł i przykładów daje *formatting soup* (mieszaninę stylów).
- **Wyraźna instrukcja formatu na końcu** — dokładnie opisz oczekiwaną strukturę, kolejność, liczbę elementów.

**5. Iteracja promptu *razem z* modelem (meta-prompting)**
Gdy output jest słaby, nie zgaduj — zapytaj model: „Zauważyłem [konkretny problem]. Co dodać do promptu, by to wyeliminować?". AI potrafi zdiagnozować własne błędy i zaproponować poprawki, które wbudowujesz z powrotem. Narzędziowo: **meta-prompter w [[Anthropic Console]]** generuje zoptymalizowany prompt XML z opisu w prostym języku i ma tryb „improve existing prompt"; analogicznie działają **Claude Prompt Improver** i **ChatGPT Prompt Optimizer**. Lekcja nadrzędna (Śliwowski): śledzenie list „100 najlepszych promptów" to zbędna praca — zamiast kolekcjonować cudze prompty, zrozum dwa procesy (instrukcja + [[2026-06-15 Context engineering|kontekst]]) i **używaj AI do poprawiania własnych**. To zamienia kiepski prompt w niezawodny system.

**7. Meta-prompt procesowy — najpierw wywiad, potem generacja (Carr)**
Odwrotność „jednego wielkiego promptu": zamiast wrzucać wszystkie wymagania naraz, każ modelowi **przeprowadzić ustrukturyzowany wywiad** — AI zadaje 5–6 pytań pojedynczo (co, dla kogo, korzyści, USP, cena, CTA), a dopiero na końcu składa gotowy prompt/efekt. Sekwencja wymusza klarowność i eliminuje generyczne copy, bo model pracuje na konkretach, nie na domysłach. Wzorzec jest przenośny (ten sam meta-prompt działa dla różnych klientów/produktów) i łączy się z singular/modular: pytania to dekompozycja *przed* wykonaniem. Voice-to-text przyspiesza odpowiadanie w trybie wywiadu — rozmowa naturalniejsza niż pisanie.

**6. Framing delegowania i role — w tym walka z sycophancy**
Skuteczny framing: „deleguj jak bardzo zdolnemu członkowi zespołu — im jaśniejsze instrukcje i więcej tła, tym lepszy wynik". Przypisanie modelowi **roli** kieruje zachowaniem. Ważne nowe ryzyko ([[Ethan Mollick]]): **sycophancy** — model potakuje użytkownikowi zamiast krytykować, co szczególnie szkodzi przy recenzji dokumentów. Antidotum jest promptowe: *wprost* poproś AI o rolę krytyka.

---

**8. „Intent engineering" — od układania promptu do opisania problemu**
Kontrapunkt dla domyślnej ramy całej strony, z praktyki jednoosobowego biznesu zbudowanego na [[Claude Code]] przez osobę bez zaplecza technicznego (Grace Clarke): **„prompt engineering umiera na rzecz *intent engineering*"** — zamiast pisać rozbudowaną instrukcję, autorka mówi do modelu przez 2–3 minuty (np. na spacerze), opisując problem, i **pozwala modelowi zaproponować rozwiązanie**. Trzy filary jej systemu pokazują, dokąd przenosi się wtedy praca: **voice guide** jako plik-skill opisujący sposób myślenia, słownictwo i to, czego autorka unika („AI slop"), dołączany automatycznie do niemal każdego zadania; **proposal maker** ze zmiennym change logiem i zasadami rozróżniającymi typy zleceń; **pipeline operator** uruchamiany co godzinę. Dwie obserwacje warte przeniesienia: (a) **skille trzeba aktualizować na bieżąco, bo model dryfuje** — każda nowa wersja modelu przynosi nowe „tells" AI slopu, więc voice guide wymaga ciągłego doszlifowywania (spina się z [[2026-07-06 LLM Wiki|LLM Wiki]], mech. 7); (b) największą barierą adopcji nie jest brak korzyści, tylko **brak nawyku otwierania narzędzia** — stąd dwustopniowa *forcing function*: przypomnienie każące zrobić zrzut ekranu problemu i wkleić go z pytaniem „możesz mi z tym pomóc?", a potem zbudowanie razem z modelem **jednego** skilla. Praktyczna zasada anty-halucynacyjna z innego wdrożenia, działająca niezależnie od stylu promptowania (Ciach): w instrukcji zapisz wprost **„jeśli czegoś brakuje, zapytaj — nie zgaduj"**.

**Napięcie do rozstrzygnięcia:** mechanizm 7 tej strony („meta-prompt procesowy", Carr) każe modelowi **najpierw przeprowadzić wywiad**, a dopiero potem generować. Clarke twierdzi odwrotnie — przy budowie skilla **nie należy interviewować użytkownika**: model powinien sam przestudiować kontekst i wrócić z **gotową propozycją do reakcji**, bo pytania męczą i spowalniają. Obie techniki są sprawdzone w praktyce, ale w innych warunkach: wywiad ma sens, gdy kontekstu **nie ma zapisanego** (nowy klient, nowy temat); propozycja-do-reakcji, gdy model ma dostęp do bogatej warstwy kontekstu ([[2026-07-06 Context layer organizacji|Context layer]]) i może z niej wyciągnąć odpowiedzi sam. Rozstrzygnięcie, czy przyjąć to jako regułę („wywiad tylko przy pustym kontekście"), należy do Piotra.

**9. Biblioteka promptów zamiast aplikacji — i prompt, który zwraca pytania, nie odpowiedzi**
Wzorzec dystrybucji i wzorzec projektowy w jednym ([[Shannon Farley]], [[Fast Forward]], *AI Proposal Assessment Tool* — narzędzie dla fundatorów oceniających wnioski grantowe organizacji wykorzystujących AI). **Forma:** nie aplikacja webowa, lecz **biblioteka gotowych promptów**, które użytkownik wkleja **do własnego, zaufanego środowiska AI** — takiego, które zna już misję i strategię jego organizacji. To rozwiązanie odwraca typową logikę produktu: zamiast budować narzędzie z własnym kontekstem, dostarcza się *instrukcję*, która wpina się w cudzy istniejący [[2026-07-06 Context layer organizacji|context layer]]. Konsekwencje są praktyczne: zero kosztu utrzymania, zero problemu z powierzeniem danych ([[2026-07-06 RODO i dane wrażliwe|RODO i dane wrażliwe]]) i pełna modyfikowalność po stronie odbiorcy — to najtańszy sposób dystrybuowania eksperckiej metody, jaki ma organizacja bez zespołu produktowego. **Wzorzec projektowy:** pierwszy prompt nie ocenia wniosku, tylko brzmi „*napisz pytania do wnioskodawcy, żeby lepiej zrozumieć dowody stojące za problemem i dlaczego AI jest właściwą interwencją*" — model **generuje pytania, nie rekomendacje**, a decyzja zostaje w całości po stronie człowieka, który pozostaje ekspertem tematycznym. To materialny głos w sporze z mechanizmu 7 (meta-prompt procesowy Carra: „najpierw wywiad") przeciw stanowisku „nie interviewuj, wróć z gotową propozycją": tutaj **wywiad jest całym produktem**, bo obiektem oceny jest cudzy, nieznany modelowi kontekst. Odwrotne zastosowanie dla piszącego wniosek: przepuść własny wniosek przez tę samą bibliotekę, żeby **z wyprzedzeniem zobaczyć pytania fundatora** i odpowiedzieć na nie w samym dokumencie.

**10. Interfejs zamiast opisu — i głos zamiast klawiatury**
Dwie techniki interakcji z modelem, które nie są promptowaniem w klasycznym sensie, ale rozstrzygają o jakości kontekstu ([[Allie K Miller]], na materiale z samodzielnego zbudowania działającej aplikacji bez umiejętności inżynierskich). **(a) Dyktowanie zamiast pisania** — mowa jest szybsza i **niesie więcej kontekstu**, bo omija filtr, który spłaszcza myśl podczas pisania; rekomendacja wdrożeniowa jest ilościowa: przenieś na dyktowanie **choćby połowę** dziś pisanych dokumentów, maili i wiadomości. **(b) „Zbuduj mi interfejs" zamiast długiego opisu** — gdy feedback albo decyzja są z natury wizualne, taniej jest poprosić model o **jednorazowy, wyrzucany interfejs** niż opisywać rzecz słowami: *design annotator* (wklejasz zrzut ekranu, zakreślasz elementy, dopisujesz komentarze, eksportujesz wszystko jednym przyciskiem z powrotem do modelu), tablica zadań, plan finansowy z suwakami, kalendarz, plan podróży. Autorka stosuje ten wzorzec w **ok. 30% swoich rozmów z AI** — to praktyczne rozwinięcie „nazwanych formatów" z mech. 2: formatem wyjściowym bywa **narzędzie**, nie tekst. Trzy zasady towarzyszące, spójne z [[2026-06-15 Context engineering|Context engineeringiem]] (mech. 4, zadania długodystansowe): **zaczynaj od najmniejszego kroku** (jedna strona testowa, zanim powstanie dwadzieścia podstron — *„gdybyś spróbował zrobić to wszystko za jednym razem, zwinąłbyś się w kłębek i się rozpłakał"*), **iteruj lokalnie** w podglądzie przed wdrożeniem, a przy realnych użytkownikach pracuj na **branchach testowych**, nie na głównym. Kontekst skali dla rozmowy z klientem: zbudowanie tej aplikacji bez AI wymagałoby zespołu 3–4 osób i „dziesiątek tysięcy dolarów".

**11. „Nudge, don't judge" — prompt, który generuje pytania, nie werdykty**
Wzorzec projektowy dla promptów wspierających **decyzje o ludziach i pieniądzach** (Kevin Barenblat i Scott J. Kleper, Fast Forward — narzędzia do oceny wniosków grantowych). Punkt wyjścia to ryzyko nazwane *„roboty randkujące z robotami"*: gdy AI pisze wniosek, a AI go ocenia, obie strony zaczynają grać w system, a ludzie tylko udają, że czytają i piszą. Odpowiedź projektowa: **nie proś modelu o werdykt** (czerwony/żółty/zielony, „czy zespół jest adekwatny"), tylko o **konkretne obszary do omówienia** — np. „warto omówić relację z kontraktorami i czy tę kompetencję rozwijać wewnętrznie". Najciekawsze rozstrzygnięcie iteracji: dążenie do **zgodności ocen między modelami** (Claude, Gemini, ChatGPT) było błędem — modele różniły się werdyktami, ale **zgadzały się w rozumowaniu i argumentach**; rozbieżność jest wadą tylko wtedy, gdy oczekujesz oceny, a zaletą, gdy oczekujesz **pokrycia tematu** (różne modele wychwytują różne aspekty). To rozszerza mech. 9 („prompt, który zwraca pytania, nie odpowiedzi") z pracy własnej na sytuacje, w których output promptu wpływa na cudze finansowanie. Zasada nadrzędna: **AI ma prowadzić do refleksji człowieka, nie zastępować jego osąd**. *(Źródło: [[2026-07-27 Robots Dating Robots]])*

**12. Prompt adwersaryjny — „załóż odmowę i argumentuj przeciwko mnie"**
Najmocniejsza operacyjna postać antidotum na sycophancy z mech. 6, sprawdzona na researchu funderów przed pisaniem wniosku ([[Wendy Clow]]). Ten sam funder i ten sam materiał źródłowy dają **przeciwne rekomendacje** zależnie od tego, czy model ma szukać dopasowania, czy powodów odmowy — więc sformułowanie polecenia, a nie jakość danych, przesądza o decyzji. Instrukcja wzorcowa: *„Załóż, że będę aplikować, i argumentuj przeciwko mnie. Podaj trzy najbardziej prawdopodobne powody, dla których ten funder nas odrzuci"*. Trzy elementy obudowy, bez których prompt adwersaryjny nie działa: **(a) profil własnej organizacji napisany raz** (nazwa, status, budżet, geografia, populacje, obszary programowe) — bez punktu odniesienia model jest bezkrytycznie entuzjastyczny; **(b) stała lista siedmiu faktów** wyciąganych dla każdego fundera (priorytety, geografia, kwalifikowalność, zakres grantu, terminy, czego nie finansują, zasady ponownej aplikacji) — porównywalność zamiast eseju; **(c) wymuszone „nie podano"** tam, gdzie danych brak, jako bezpiecznik przeciw halucynowanym terminom. Argument ekonomiczny dla organizacji: poważny wniosek to **15–40 godzin** pracy, więc przy liście 30 funderów cztery nietrafione aplikacje to **~100 godzin** włożonych w budżety, których własne wytyczne wykluczyły organizację na starcie — dwudziestominutowy research adwersaryjny jest tu najtańszą możliwą inwestycją. Granica pozostaje ta sama co w mech. 9 i 11: model czyta i porządkuje długie, nudne dokumenty (wytyczne, FAQ, listy wykluczeń), ale **każdy fakt gatekeepingowy trzeba zweryfikować u źródła** — halucynowany termin jest gorszy niż brak researchu. *(Źródło: [[2026-07-29 How I Use AI to Research Funders Before I Write the Grant]])*

---

## Frameworki-kotwice

- **9 technik pisania z AI (Cole)** / **8 technik dla ghostwritera** — pokrywający się rdzeń: 3 tryby promptowania, język obiektywny, nazwane formaty, singular/modular, zgodne przykłady, instrukcje formatu, iteracja z AI.
- **Schemat XML promptu** — `task / audience / format / tone / requirements`; gotowy template warsztatowy.
- **Garbage in, garbage out** — „kiepskie outputy to zwykle błąd promptu, nie modelu"; najmocniejszy przekaz dydaktyczny.
- **„Nie zautomatyzujesz tego, czego nie umiesz zwerbalizować"** — automatyzacja promptem to konsekwencja zrozumienia własnego procesu; u Cole'a → ponad 50% pracy twórczej zautomatyzowane.
- **Analogia pracownika** (wspólna z context engineeringiem): prompting = stażysta; Custom GPT = freelancer; pełny kontekst = wieloletni pracownik. Prompt engineering to poziom „dobrej odprawy dla stażysty".
- **Typologia modeli (Mollick)** — chat / agent / wizard; domyślny model rzadko jest najlepszy — wybór modelu i trybu myślenia to część rzemiosła, nie tylko treść promptu.

---

## Powiązane pojęcia

- [[2026-06-15 Context engineering]] — szerszy następca: prompt engineering to *treść instrukcji*, context engineering zarządza *całym oknem* (system prompt, narzędzia, historia, pobrana wiedza). Prompt to atom, kontekst to architektura wokół niego — para parasol↔przypadek odwrotna do tej z [[2026-06-14 RAG|RAG]].
- [[2026-06-13 Wdrażanie AI w organizacji społecznej]] — prompt engineering to kompetencja operacyjna warunkująca poziom *Better/New*; bez niej zespół utyka na *Faster*. Czerwony link stąd zrealizowany.
- [[2026-06-14 RAG]] — RAG *dostarcza* zaufany kontekst do okna, ale prompt wciąż musi poprawnie poinstruować, co z tym kontekstem zrobić; dobry retrieval + zły prompt = zły output.
- [[2026-06-14 Framing]] — bliźniacze rzemiosło precyzji języka: framing dobiera słowa, by wywołać reakcję *człowieka*, prompt — by wywołać zachowanie *modelu*. Oba karzą abstrakcję i nagradzają konkret.
- [[Claude Projects]] — „kontener kontekstu": biblioteka materiałów stale przybliżająca model do stylu klienta; pomost od prompt engineeringu do context engineeringu (czerwony link — backlog).

---

## Zastosowanie w kontekście NGO

- **Szkolenia z AI dla organizacji**: schemat XML jako konkretny *deliverable* warsztatu — uczestnik wychodzi z gotowym templatem promptów dla swoich zadań (komunikacja, fundraising, raportowanie). Trzy tryby promptowania porządkują „dlaczego ten sam prompt raz działa, raz nie".
- **[[2026-07-07 Ghostwriting|Ghostwriting]]**: singular/modular prompts + [[Claude Projects]] jako biblioteka stylu klienta + automation prompting to gotowy system powtarzalnego pisania; bezpośrednio przekładalne na własne pluginy [[Claude Code]].
- **Ćwiczenie meta-promptingu**: na warsztacie pokaż meta-prompter w [[Anthropic Console]] (darmowe kredyty) i tryb „improve existing prompt" — uczestnicy poprawiają własne, realne prompty.
- **Recenzja dokumentów (granty, strategie)**: naucz zespół promptu „bądź krytykiem, wskaż 3 najsłabsze miejsca" jako antidotum na sycophancy — inaczej AI potwierdzi słaby wniosek grantowy.
- **Próg wejścia**: prompt engineering to najtańsza dźwignia („lepszy output bez dodatkowych narzędzi") — idealny pierwszy moduł, zanim organizacja sięgnie po RAG czy automatyzacje.

---

## Otwarte pytania

- Gdzie przebiega granica, za którą doszlifowywanie promptu przestaje się opłacać i trzeba przejść do context engineeringu (stały kontekst, retrieval) albo zmiany modelu — jak rozpoznać ją zawczasu?
- Czy prompt engineering to trwała kompetencja, czy umiejętność przejściowa, którą modele „zjedzą", coraz lepiej domyślając się intencji z lakonicznego polecenia? Sygnał kierunku (Śliwowski): w modelach rozumujących sama instrukcja jest „coraz mniej decydująca", a ciężar przesuwa się na [[2026-06-15 Context engineering|kontekst]] i grounding — co sugeruje, że *werbalizacja zadania* zostaje, ale *mikrooptymalizacja sformułowań* faktycznie się dewaluuje.
- Jak nauczyć pracownika NGO „werbalizować własny proces", skoro wiele zadań wykonuje się wiedzą milczącą (tacit) — od czego zacząć dekompozycję?
- Jak odróżnić prompt, który *naprawdę* poprawił wynik, od złudzenia poprawy wzmocnionego przez sycophancy modelu chwalącego każdą zmianę?
