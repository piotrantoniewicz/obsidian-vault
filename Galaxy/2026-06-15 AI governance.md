---
categories: Concept
tags:
  - strategia-AI
  - organizacje-społeczne
  - strategia-organizacji
created: 2026-06-15
updated: 2026-07-24
relevance: wysoka
sources:
  - "[[2024-08-12 AI Governance Framework for Nonprofits]]"
  - "[[2025-10-29 Sztuczna inteligencja w NGO. Jak wprowadzać AI w zgodzie z wartościami i misją organizacji]]"
  - "[[2026-03-26 Twój zespół już używa AI Czas na politykę korzystania!]]"
  - "[[2025-10-20 Human-centered AI Practical insights for nonprofit boards]]"
  - "[[2025-06-24 How to build an ethical AI culture From values to practice]]"
  - "[[2026-04-08 Who owns AI's mistake when no one signed off]]"
  - "[[2026-02-20 The business advantage of strong AI governance]]"
  - "[[2026-06-17 Humanistic by Design. Transparent by Default. Values-Led Always.]]"
  - "[[2026-06-16 Suwerenność na wynajem]]"
  - "[[2025-12-08 Guidance for using artificial intelligence in fundraising]]"
  - "[[2026-05-20 EU AI Act Update Timeline Relief, Targeted Simplification, and New Prohibitions]]"
  - "[[2026-07-22 The Runway Before the Flight]]"
  - "[[2026-07-24 Still In Control]]"
---

# AI governance (zarządzanie AI w organizacji)

AI governance to **zestaw zasad, ról i procesów, które nadają używaniu AI w organizacji ramy: kto, do czego, na jakich danych i z czyją weryfikacją może z niej korzystać**. To nie jednorazowy audyt ani dokument do odhaczenia, lecz ciągły proces wbudowany w codzienne decyzje — od projektowania zastosowania, przez politykę, po przegląd po wdrożeniu. Punktem wyjścia nie jest narzędzie, tylko **misja i wartości organizacji społecznej**: governance odpowiada na pytanie „jak korzystać z AI, nie podkopując zaufania, na którym organizacja stoi". Sektor jest tu boleśnie nieprzygotowany — szacunki zgodnie wskazują, że **mniej niż 1% organizacji** wdrożyło AI (i odpowiedzialne praktyki) systemowo, a reszta używa jej *ad hoc*, bez wspólnych reguł. Governance to filar etyki w modelu [[2026-06-13 Wdrażanie AI w organizacji społecznej|świadomego wdrożenia AI]] — warunek wstępny, nie formalność dopisana po fakcie.

---

## Kluczowe mechanizmy

**1. Domyślny stan to „BYO AI" — i to jest problem**
Większość organizacji społecznych jest już w sytuacji, w której część zespołu korzysta z AI bez zasad (*Bring Your Own AI*). To generuje konkretne ryzyka: **wyciek danych beneficjentów** do zewnętrznych serwerów (potencjalny incydent RODO wymagający zgłoszenia do UODO), decyzje oparte na halucynacjach i niespójna komunikacja zewnętrzna. Governance nie jest więc wyborem „czy", lecz nadrobieniem stanu, który już istnieje. Alternatywa dla intencjonalnego wdrożenia to nie „brak AI", lecz chaos.

**2. Lekka polityka AI bije obszerny regulamin**
Praktyczne minimum to **dwustronicowa polityka**, którą organizacja tworzy w jedno popołudnie — nie 20-stronicowy dokument, którego nikt nie czyta. Powinna pokryć trzy obszary (TechSoup): **Operacje** (które procesy wspiera AI, kto weryfikuje wyniki, co gdy AI się myli), **Komunikacja** (co oznaczamy jako AI, jak chronimy dane, jaki ton), **Narzędzia** (które dopuszczone, kto decyduje o nowych, jak często przegląd). Kluczowe dla utrzymania przy życiu: **jeden właściciel dokumentu, przegląd roczny, powiązanie z onboardingiem i biblioteką promptów**. Polityka ma być ramą nadającą reguły, nie zakazem.

**3. Współautorstwo zamiast odgórnego nakazu**
Polityka powstaje *razem z zespołem*, nie spuszczana z góry — inaczej nie działa. Sprawdzony format warsztatu (60–90 min): rundka „kto używa AI i do czego" → karteczki „co ułatwia / co niepokoi / czego nie wiemy" → wspólne przejście przez szablon → ustalenie właściciela i terminu przeglądu. Efekt podwójny: dokument **i** poczucie współwłasności, które przekłada się na realne przestrzeganie.

**4. Najpierw ryzyko, potem kontrole — właściwa sekwencja**
Typowy błąd (Responsible AI Institute): definiowanie kontroli, zanim scharakteryzuje się ryzyko. Trzy luki governance ujawniają się szczególnie przy [[2026-06-15 Agentic AI|agentic AI]]: (a) **zrozumienie ryzyka** — najpierw charakterystyka, potem kontrole, nie równolegle; (b) **polityki zatwierdzania** — klasyczne procesy nie działają dla systemów zmieniających zachowanie *po* wdrożeniu; (c) **gotowość ludzi** — zespół musi być przygotowany *przed* uruchomieniem, nie po. Governance to także gotowość organizacyjna, nie tylko frameworki.

**5. Wrażliwość na ryzyko zależy od misji**
Nie ma jednej polityki dla wszystkich — każda organizacja ma inną wrażliwość (Sektor 3.0): ekologiczna na **koszt środowiskowy**, edukacyjna na **wiarygodność**, pomocowa na **bias w danych** uderzający w grupy wrażliwe. Trzy obszary ryzyka etycznego jako schemat audytu: **wiarygodność** (halucynacje podważają autorytet — wymagany cross-check każdej treści; kazus AI-generowanych obrazów protestów wycofanych po krytyce), **tożsamość** (uzależnienie od Big Techu → potrzebny „exit plan"), **zależność** (wartości wyznaczają granice: czy narzędzie nie wyklucza grup docelowych?). Wymiar geopolityczny zależności ([[Dariusz Jemielniak]], „Suwerenność na wynajem"): model AI w chmurze to **infrastruktura krytyczna pod jurysdykcją kraju serwera** — dostęp może zostać odcięty decyzją polityczną, nie techniczną (kazus wyłączenia modelu Fable 5 przez kontrolę eksportową USA „w piątek po południu, bez ostrzeżenia"). Dla polskich NGO uzależnienie kluczowych procesów od jednego dostawcy z USA to luka w planie ciągłości działania — stąd dywersyfikacja narzędzi i unikanie single-vendor lock-in jako konkretny element „exit planu".

**6. Od deklaracji wartości do struktur — dojrzałość etyczna**
Etyka AI zaczyna się od projektowania, nie od audytu po fakcie. Pięć etapów dojrzałości: **ewangelizacja → polityki → dokumentacja** (model cards) **→ systematyczne przeglądy** (Algorithm Review Boards) **→ realne działania** (modyfikacja lub wycofanie rozwiązań). Formalne struktury biją deklaracje — i nie wymagają korporacyjnych budżetów: mała organizacja zaczyna od regularnych spotkań i analizy konkretnych przypadków. Bariera to nie technologia, lecz **nawyk zadawania właściwych pytań**.

**7. Filtr wartości przed adopcją — Reguła Trzech ([[Bryan Neider]])**
Technologia nie jest neutralna: każdy system niesie wartości i ślepe punkty twórców. Dlatego każde narzędzie AI przechodzi przez trzy filtry, **zanim** dotknie klientów, danych lub workflow personelu: **Human Dignity** (jeśli kompromituje godność — odpada), **Algorithmic Transparency** (architektura danych i relacje z dostawcą muszą być zrozumiałe — żadnych „czarnych skrzynek" wobec grup wrażliwych), **Values-Based Governance** (narzędzia podlegają tym samym standardom etycznym co pracownicy — bez wyjątków dla technologii). Mechanizmem jest **AI Governance Working Group** — nie komitet spowalniający, lecz brama zachowująca tożsamość organizacji po adopcji. Pułapka do nazwania: **„human-in-the-loop paradox"** — ludzki podpis pod rekomendacją AI to nie to samo co ludzki osąd; governance musi to rozróżniać.

**8. „Pas startowy" zamiast zakazu — odpowiedź na shadow AI ([[Bryan Neider]])**
Domyślny stan z mechanizmu 1 ma już nazwę operacyjną: **shadow AI** — pracownicy wklejający dane klientów i darczyńców do darmowych narzędzi. Odpowiedzią nie jest zakaz (nieegzekwowalny), lecz zbudowanie pasa startowego przed startem: (a) **opublikowanie granicy danych** — darmowe narzędzia AI nigdy nie dotykają nazwiska klienta, diagnozy ani danych darczyńcy; (b) **bezstresowy, anonimowy audyt użycia** — zapytaj zespół, czego już używa, bez konsekwencji; (c) **przejście na licencje enterprise z umową** — IT formalnie podpisuje umowę o ochronie danych i wyłącza trenowanie na modelach publicznych; (d) interdyscyplinarny **zespół przeglądowy** (program, IT, compliance, przedstawiciel zarządu) zatwierdzający każde nowe zastosowanie; (e) test biasu na realnych przypadkach; (f) jawna komunikacja zasad zarządowi i społeczności. **Trzy pytania przed podpisaniem umowy z dostawcą AI:** czy nasze dane będą trenować wasze publiczne modele, czy podpiszecie formalną umowę o ochronie danych obejmującą dane zdrowotne/klienckie, czy nasze IT będzie widzieć i kontrolować, kto używa narzędzia i jak. Teza mocniejsza niż sama procedura: **poziom licencji (darmowa vs enterprise) to sygnał tego, jak bardzo organizacja szanuje dane osób, którym służy** — strategia AI wymaga budżetu na wersje enterprise, nie tylko na eksperymenty.

**9. Zatwierdzenie to początek, nie meta — Tri-Pillar i HITL jako praktyka stała**
Domknięcie luki z mechanizmu 4 (polityki zatwierdzania nie działają dla systemów zmieniających zachowanie po wdrożeniu): akceptacja narzędzia przez zarząd otwiera odpowiedzialność, a nie ją zamyka — zwłaszcza przy systemach agentowych, które po uruchomieniu działają samodzielnie, bez przerwy sprawdzającej, czy warunki się zmieniły. **Tri-Pillar Governance Framework** kotwiczy każde wdrożenie w trzech filarach: **Etyka / Koszt / Nadzór**. **Human-in-the-Loop** przestaje być jednorazowym zabezpieczeniem, a staje się praktyką stałą: przy każdym zadaniu krytycznym lub dotykającym darczyńcy/podopiecznego wykwalifikowana osoba przegląda i zatwierdza output, zanim cokolwiek się wydarzy. Najczęstszy błąd to system, który dalej działa, gdy nikt już go nie obserwuje. Do tego decyzja **build vs buy** jako element governance, nie tylko IT: własny system = pełna kontrola nad danymi przy koszcie kapitału i kompetencji; gotowa platforma = szybkość przy ograniczonej kontroli nad praktykami prywatnościowymi dostawcy. Uwaga: to mechanizm-lustro dla „human-in-the-loop paradox" z mechanizmu 7 — HITL działa tylko wtedy, gdy człowiek realnie osądza, a nie podpisuje.

---

## Frameworki-kotwice

- **AI Governance Framework for Nonprofits (Afua Bruce / Microsoft)** — 6-modułowy, bezpłatny zestaw: szablony polityk AI, przykłady zastosowań, materiały do dyskusji zarządu; modułowy — organizacja bierze to, co pasuje do jej etapu.
- **Trzy obszary polityki AI (TechSoup)** — Operacje / Komunikacja / Narzędzia; szablon 7 sekcji: Cel i zakres → Dopuszczone narzędzia → Dane i poufność → Weryfikacja wyników → Transparentność → Odpowiedzialność → Szkolenie.
- **Trzy obszary ryzyka etycznego (Sektor 3.0)** — wiarygodność / tożsamość / zależność; gotowy schemat audytu bez technicznego żargonu.
- **Trzy luki governance (Responsible AI Institute)** — zrozumienie ryzyka / polityki zatwierdzania / gotowość ludzi; „najpierw ryzyko, potem kontrole".
- **Pięć etapów dojrzałości etycznej (Davenport)** — ewangelizacja → polityki → dokumentacja → przeglądy → działania.
- **Reguła Trzech + AI Governance Working Group (Neider)** — Human Dignity / Algorithmic Transparency / Values-Based Governance; brama, przez którą przechodzi każde narzędzie przed kontaktem z danymi/klientami. Uwaga: „human-in-the-loop paradox".
- **Proces wdrożenia AI w fundraisingu (Fundraising Regulator UK)** — trzy etapy: *eksploracja* (ocena ryzyka i zaangażowanie zarządu przed użyciem narzędzia) → *przygotowanie* (polityka AI, kompetencje, pilotaż w zamkniętym środowisku, audyt danych) → *użycie* (transparentność wobec darczyńców *proporcjonalna do ryzyka wprowadzenia w błąd*, nadzór ludzki nad każdym outputem, dokumentacja kontroli). Reguła nadrzędna: **organizacja ponosi pełną odpowiedzialność za każdy output AI — także halucynacje i bias narzędzia zewnętrznego, którego nie wygenerowała sama.**
- **EU AI Act — stan regulacji (Digital Omnibus, 7 maja 2026)** — pierwsza nowelizacja od 2024: termin compliance dla systemów wysokiego ryzyka (Annex III) przesunięty na **2 grudnia 2027**; nowe zakazy (niekonsensualny content intymny, CSAM przez AI) od 2 grudnia 2026; **Art. 25** nakłada obowiązki informacyjne na *każdego, kto integruje lub modyfikuje modele* (kara do 3% obrotu / 15 mln EUR); nadzór nad GPAI centralizuje **AI Office**. Praktycznie: organizacja budująca narzędzia na zewnętrznych LLM-ach wchodzi w łańcuch obowiązków, nie tylko dostawca.
- **Liczby-kotwice**: <1% organizacji wdrożyło AI systemowo (Klon/Jawor + Sektor 3.0); ~99% organizacji społecznych nie ma polityki AI (Heyman); 53% pracowników nie wie, jak korzystać z AI, 22% to power users (Microsoft).
- **Cytat-kotwica**: „Governance, które pojawia się zbyt późno, to jak wylewanie betonu, gdy mieszkańcy się już wprowadzili" (WEF).

---

## Powiązane pojęcia

- [[2026-06-13 Wdrażanie AI w organizacji społecznej]] — AI governance to filar **etyki** tego wdrożenia: „AI odsłania istniejące słabości", a governance jest mechanizmem, który nie pozwala słabościom (bałagan w danych, brak zasad) skalować się razem z narzędziem. Czerwony link stąd zrealizowany.
- [[2026-06-13 Transparentność operacyjna]] — bliźniaczy filar zaufania: governance wymaga informowania o użyciu AI (92% darczyńców tego oczekuje), a transparentność operacyjna to szersza zasada, której polityka AI jest konkretnym przypadkiem.
- [[2026-06-14 RAG]] — techniczna realizacja jednej z reguł governance: lokalny/hybrydowy RAG trzyma dane beneficjentów na własnej infrastrukturze, odpowiadając na ryzyko wycieku do zewnętrznych modeli (podział Admin/Program Zone to operacyjny język governance).
- [[2026-06-15 Prompt engineering]] — kompetencja, bez której polityka „weryfikuj wyniki" jest pusta: zespół musi umieć wymusić rolę krytyka i rozpoznać halucynację, by realnie kontrolować output.
- [[2026-07-06 RODO i dane wrażliwe|RODO i dane wrażliwe]] — prawny rdzeń ryzyka (dane beneficjentów, AI Act, zgoda): governance to procesy i role, RODO/AI Act wyznaczają twarde minimum, którego te procesy pilnują.
- [[2026-06-15 Agentic AI]] — przesuwa governance z „rekomendacji" na „samodzielne działanie": klasyczne polityki zatwierdzania przestają wystarczać, gdy system zmienia zachowanie po wdrożeniu.
- [[2026-06-23 Widoczność w AI search]] — governance ma drugą, zewnętrzną twarz: monitoring **dryftu narracyjnego** (jak AI opisuje organizację) i krótka **polityka wobec AI search** to element ładu — nie tylko *jak my używamy AI*, ale *jak AI reprezentuje nas*.
- [[2026-07-06 Evale|Evale]] — operacjonalizacja zasady „weryfikuj wyniki": governance definiuje odpowiedzialność za output AI, evale dają mierzalny proces, którym tę odpowiedzialność się wykonuje.

---

## Zastosowanie w kontekście organizacji społecznych

- **Moduł doradczy „polityka AI w jedno popołudnie"**: gotowa usługa oparta na szablonie TechSoup + formacie warsztatu — organizacja wychodzi z dwustronicową polityką i właścicielem dokumentu. Niska bariera, wysoka wartość: szybki, namacalny efekt.
- **Audyt etyczny przez schemat 3 obszarów ryzyka** (wiarygodność / tożsamość / zależność) — struktura rozmowy o etyce bez żargonu, dopasowana do wrażliwości konkretnej organizacji (ekologiczna, edukacyjna, pomocowa).
- **Argument sprzedażowy oparty na danych**: <1% systemowych wdrożeń i ~99% bez polityki to gotowa nisza; do tego rosnąca presja grantodawców (szczególnie zagranicznych), którzy pytają o podejście do AI i ochrony danych — polityka AI buduje zaufanie wobec fundratorów.
- **Argument RODO dla sceptyków**: „wklejanie danych beneficjentów do zewnętrznego AI może być incydentem wymagającym zgłoszenia do UODO" — najskuteczniej przekonuje oporne organizacje do podjęcia tematu.
- **Compliance-check przy doradztwie (EU AI Act)**: sprawdź, czy używane przez organizację systemy nie wpadają w kategorię wysokiego ryzyka (Annex III, termin 2 grudnia 2027) i czy budując narzędzie na zewnętrznym LLM-ie nie przejmujesz obowiązków informacyjnych z Art. 25 — element do wpisania w umowy z dostawcami modeli. „Organizacja odpowiada za każdy output AI" (Fundraising Regulator) to mocny argument za polityką, szczególnie wobec grantodawców zagranicznych.
- **Governance dla zarządu**: zasada „low touch, high value" + dashboard misji (zielony/żółty/czerwony) jako sposób, by rada nadzorcza ogarnęła AI bez wchodzenia w szczegóły techniczne; „najpierw ryzyko, potem kontrole" jako reguła kolejności dla organizacji bez zasobów na kosztowne błędy.
- **Playbook pierwszego kwartału (Neider)**: granica danych opublikowana w tym tygodniu → anonimowy audyt użycia → migracja na licencje enterprise z umową → zespół przeglądowy → test biasu → komunikat do zarządu i społeczności. Gotowa checklista do sprzedania jako pakiet wdrożeniowy — konkretniejsza niż „napiszmy politykę".
- **Trzy pytania do dostawcy AI** jako załącznik do każdej umowy: trenowanie na naszych danych, formalna umowa o ochronie danych, widoczność i kontrola po stronie IT. Krótkie, zrozumiałe dla zarządu, weryfikowalne.
- **Element kursu „Fundraising z AI"**: moduł o odpowiedzialnym wdrożeniu — pięć etapów dojrzałości + szablon polityki jako praca domowa uczestników.

---

## Otwarte pytania

- Jak skłonić organizację społeczną do napisania polityki AI *zanim* dojdzie do incydentu z danymi — skoro motywacja zwykle przychodzi dopiero po wycieku albo pytaniu grantodawcy?
- Gdzie przebiega minimum, poniżej którego polityka jest fasadą (dwie strony „dla grantodawcy"), a powyżej którego realnie zmienia zachowania zespołu — i czym to mierzyć?
- Jak governance ma nadążyć za [[2026-06-15 Agentic AI|agentic AI]] w organizacji bez kompetencji technicznych, skoro klasyczne procesy zatwierdzania zawodzą dla systemów zmieniających zachowanie po wdrożeniu?
- Czy „exit plan" od Big Techu jest dla małej organizacji realny, czy to postulat życzeniowy — jaki jest najtańszy poziom niezależności (lokalny model? eksport danych?), który da się utrzymać?
- Jak pogodzić wymóg transparentności („oznaczamy treści AI") z obawą, że ujawnienie użycia AI samo w sobie podkopie wiarygodność organizacji w oczach darczyńców?
