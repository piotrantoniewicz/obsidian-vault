---
categories: Concept
tags:
  - prompt-engineering
  - narzędzia-AI
  - szkolenia-AI
created: 2026-06-15
updated: 2026-07-07
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
