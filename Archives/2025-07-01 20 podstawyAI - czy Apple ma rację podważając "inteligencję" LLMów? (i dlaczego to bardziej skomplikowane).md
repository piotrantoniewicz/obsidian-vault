---
type: "Web"
authors: "[[Przemek Jurgiel-Zyla]]"
url: "https://www.linkedin.com/pulse/20-podstawyai-czy-apple-ma-racj%C4%99-podwa%C5%BCaj%C4%85c-llm%C3%B3w-i-jurgiel-zyla-spu7f/"
published: 2025-07-01
created: 2026-05-31
tags:
  - "LLM"
  - "trendy-AI"
  - "strategia-AI"
---


### tl;dr Apple podważyło "inteligencję" obecnie działających modeli językowych - przedstawiło badania, które przekonują odbiorcę, że wystarczy zadać trudniejsze zadanie, a większość LLMów się pogubi. Ale czy to prawda i jaka jest druga strona medalu - o tym poniżej.

> zachęcam do odwiedzin na [podstawy.ai](http://podstawy.ai/) - zbieramy tam zapisy na listę oczekujących na kolejne warsztaty

> jeśli podoba Ci się to jak i o czym piszę - wyślij to swoim znajomym, to będzie największe podziękowanie dla mnie

> jeśli jesteś "tym znajomym" co otrzymał niniejszy artykuł - dzien dobry, wejdź na mój profil i zobacz co robię - może znasz fajny startup z obszaru tech/AI, który byłby zainteresowany finansowaniem od [Movens Capital](https://www.linkedin.com/company/movenscapital/) - chętnie porozmawiam

## Apple wobec ograniczeń modeli językowych: badania, kontrowersje i strategia

Apple opublikował w okresie październik 2024 - czerwiec 2025 serię badań naukowych argumentujących, że modele językowe wykazują fundamentalne ograniczenia w rozumowaniu i jedynie naśladują wzorce z danych treningowych. Publikacje te, szczególnie "GSM-Symbolic" i "The Illusion of Thinking", wywołały intensywną debatę w branży AI, z krytykami wskazującymi zarówno na błędy metodologiczne, jak i potencjalne strategiczne motywacje związane z opóźnieniem Apple w wyścigu AI.

### Przełomowe badania Apple demonstrują krytyczne ograniczenia LLM

Zespół badaczy Apple pod kierownictwem **Imana Mirzadeha** i **Samy'ego Bengio** opublikował 7 października 2024 roku na arXiv pracę "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models" (arXiv:2410.05229). Badanie wykazało, że dodanie pojedynczej nieistotnej klauzuli do zadań matematycznych powoduje **spadek wydajności do 65%** we wszystkich testowanych modelach state-of-the-art, włączając GPT-4, Claude i Gemini.

Kluczowym odkryciem było stwierdzenie, że *"current LLMs cannot perform genuine logical reasoning; they replicate reasoning steps from their training data"*. Badacze stworzyli nowy benchmark GSM-Symbolic oparty na szablonach symbolicznych, który ujawnił niestabilność odpowiedzi LLM - modele dawały różne odpowiedzi na różne instancje tego samego pytania, wykazując wrażliwość na minimalne zmiany w formułowaniu.

Druga kluczowa publikacja, "The Illusion of Thinking" z 7 czerwca 2025 roku, pogłębiła analizę używając kontrolowanych środowisk puzzli (Tower of Hanoi, Blocks World). **Parshin Shojaee** i zespół zidentyfikowali trzy reżimy wydajności:

- Przy niskiej złożoności standardowe LLM przewyższają Large Reasoning Models
- Przy średniej złożoności LRM zyskują przewagę
- Przy wysokiej złożoności następuje **"całkowite załamanie dokładności"** w obu typach modeli

Szczególnie intrygujące było odkrycie zjawiska "overthinking" - modele znajdowały prawidłowe odpowiedzi wcześnie w procesie rozumowania, ale kontynuując analizę dochodziły do błędnych wniosków. Paradoksalnie, przy wzroście złożoności zadań wysiłek rozumowania malał pomimo dostępnego budżetu tokenów. Badacze zauważyli także, że **modele rezygnowały z dalszych prób rozumowania** w obliczu narastającej trudności, jakby "poddawały się" przed wykorzystaniem wszystkich zasobów.

Co najważniejsze, zaobserwowano **duże różnice w działaniu modeli dla znanych vs. nieznanych zadań**. Gdy układanka była w formie, którą model prawdopodobnie "widział" w danych treningowych, radził sobie zdecydowanie lepiej. Sukces modelu często wynikał ze znajomości wzorców z treningu, a nie z prawdziwie uniwersalnej umiejętności rozumowania. Modele wykazały się także **niezdolnością do wykonywania jawnie podanych algorytmów** - nawet gdy dostarczono im poprawny przepis na rozwiązanie, nie potrafiły go konsekwentnie zastosować.

### Apple dramatycznie opóźnione w wyścigu AI pomimo masywnych inwestycji

Z drugiej strony analiza pozycji rynkowej ujawnia, że Apple jest **18-24 miesiące** za konkurencją w rozwoju AI. Podczas gdy ChatGPT (OpenAI) zadebiutował w 2022, Apple ogłosiło Apple Intelligence dopiero w czerwcu 2024 na WWDC, z pierwszymi funkcjami publicznymi udostępnionymi w październiku 2024.

Porównanie techniczne jest miażdżące:

- Apple Intelligence wykorzystuje model o **3 miliardach parametrów**
- GPT-4 ma **1.76 tryliona parametrów**
- Google Gemini 2.5 Pro oferuje 2 miliony tokenów kontekstu i osiąga 63.8% w benchmarku SWE-bench Verified
- Apple musi polegać na partnerstwie z OpenAI, integrując ChatGPT jako "backup" dla Siri w iOS 18.2

Udział w rynku potwierdza opóźnienie: **OpenAI i Meta** kontrolują po 31% rynku USA, Google Gemini ma 27%, podczas gdy Apple Intelligence dopiero wchodzi na rynek. OpenAI osiągnęło już **10 miliardów dolarów przychodu rocznego** dzięki swoim modelom, podczas gdy Apple dopiero próbuje wejść na ten rynek.

W lutym 2025 Apple ogłosiło plan inwestycji **500 miliardów USD** w USA przez kolejne 4 lata, włączając:

- Nową fabrykę serwerów AI w Houston (250,000 stóp kwadratowych (sorry za taką jednostkę - to ok 23 tys. m2), otwarcie w 2026)
- Zatrudnienie 20,000 nowych pracowników, głównie w obszarach R&D, silicon engineering, AI i ML
- Podwojenie Advanced Manufacturing Fund z 5 do 10 miliardów USD
- Rozbudowę centrów danych w Arizonie, Kalifornii, Iowa, Nevadzie, Północnej Karolinie, Oregonie i Waszyngtonie

Tim Cook stwierdził: *"Wydaliśmy 100 miliardów dolarów w ciągu ostatnich pięciu lat na R&D"*, ale fakty pokazują, że pieniądze nie przełożyły się na konkurencyjne produkty AI (R&D w Apple to głównie sprzęt użytkowy i oprogramowanie systemowe). Źródła eksperckie, jak Stratechery, oceniają, że "Apple ma podstawowe możliwości LLM on-device, ale jest daleko od cutting-edge w modelach i produktach".

### Krytyka czy kalkulacja? Dwuznaczność strategii Apple

Na konferencji WWDC 2025 Apple nie zaprezentowało żadnego przełomowego LLM czy asystenta AI. Craig Federighi wspomniał jedynie o dalszych pracach nad Siri, zaznaczając że potrzebują więcej czasu. Firma skupiła się na **drobniejszych usprawnieniach** - transkrypcji rozmów, tłumaczeniach na żywo - zamiast na spektakularnych nowinkach generatywnej AI.

Po WWDC 2025 **akcje Apple spadły o 1.2%**, a od początku roku notowania były niższe o 17%, co pokazuje rozczarowanie rynku. Analitycy podkreślają, że **"czas dla Apple biegnie coraz szybciej"** i okno czasowe może się zamykać. Co nie zmienia faktu, że w trendzie wieloletnim Apple dało sporo zarobić swoim inwestorom.

Jednocześnie firma ogłosiła ostrożne otwarcie niektórych narzędzi Apple Intelligence dla deweloperów - udostępniając model językowy działający na urządzeniu (btw nawet polski Bielik ma więcej parametrów:P). Samo Apple przyznaje, że to uproszczona wersja nieporównywalna z gigantycznymi modelami chmurowymi konkurencji.

Taka zachowawcza postawa budzi pytania o motywacje. Z jednej strony Apple rzeczywiście **priorytetyzuje jakość i prywatność**, mając historię sukcesów wchodzenia na rynek później, ale z dopracowanymi produktami. Z drugiej strony, **publiczne umniejszanie osiągnięć LLM przez firmę, która nie ma własnego konkurencyjnego modelu**, może być strategicznym posunięciem. Jak zauważył Gary Marcus: *"wiele firm bije na alarm o potędze AI i ściga się w drodze do hipotetycznej sztucznej ogólnej inteligencji, podczas gdy wyniki badań (takich jak Apple) studzą ten entuzjazm"*.

### Branża AI ostro krytykuje metodologię i motywacje Apple

Reakcja społeczności AI na badania Apple była gwałtowna i podzielona. **Alex Lawsen** z Open Philanthropy wraz z Claude Opus opublikowali ripostę zatytułowaną "The Illusion of the Illusion of Thinking", bezpośrednio podważającą wnioski Apple. Kluczowym argumentem było, że *"What Apple's team interpreted as a reasoning limitation was actually a physical constraint on output length"*.

Lawsen wykazał, że gdy modelom pozwolono generować algorytmy zamiast szczegółowych kroków, rozwiązywały problemy Tower of Hanoi z 15 dyskami - zadania, które według Apple powodowały "kompletny kolaps". **23% problemów River Crossing** w testach Apple było matematycznie nierozwiązywalnych, ale modele były karane za rozpoznanie tego faktu.

**Pedro Domingos** z University of Washington sarkastycznie skomentował: *"Apple's brilliant new AI strategy is to prove it doesn't exist"*, sugerując strategiczne motywacje badań. Wielu krytyków wskazuje na timing publikacji - tuż przed WWDC 2025, gdzie Apple skupiło się na designie oprogramowania zamiast przełomów w AI.

Jednak niektórzy eksperci bronili badań. **Gary Marcus** stwierdził, że wyniki potwierdzają jego długoletnie argumenty o ograniczeniach LLM i że *"każdy, kto myśli, że LLM-y są bezpośrednią drogą do sztucznej inteligencji ogólnej mogącej fundamentalnie zmienić społeczeństwo na lepsze, oszukuje samego siebie"*. **Yann LeCun** z Meta również widzi w badaniach potwierdzenie swojej tezy, że "entirely new ideas are needed to reach AGI rather than simply scaling current technologies".

Paradoksalnie, podczas gdy badacze Apple krytykują zdolności rozumowania LLM, firma jednocześnie promuje Apple Intelligence jako posiadające "improved tool-use and reasoning capabilities". Ta sprzeczność dodatkowo podsyca spekulacje o strategicznych motywacjach publikacji.

### Rzetelność naukowa badań Apple pozostaje kontrowersyjna

Ocena rzetelności badań Apple ujawnia zarówno mocne strony, jak i poważne słabości metodologiczne. Pozytywnie wyróżnia się nowatorska metodologia wykorzystująca kontrolowane środowiska puzzli (Tower of Hanoi, Blocks World), co pozwoliło uniknąć problemów z kontaminacją danych. Zespół systematycznie zidentyfikował trzy różne reżimy wydajności w zależności od poziomu złożoności zadań.

Jednak krytycy wskazują na fundamentalne błędy:

- Apple zignorowało ograniczenia budżetu tokenów, mylnie interpretując (i moje pytanie brzmi, czy świadomie?) fizyczne ograniczenia jako niezdolność do rozumowania
- Około **23% zadań River Crossing było matematycznie nierozwiązywalnych**, co sztucznie zaniżało wyniki modeli
- Wymuszanie na modelach generowania wyczerpujących tekstowych odpowiedzi zamiast algorytmicznych rozwiązań wprowadzało sztuczne ograniczenia

Istotne jest, że publikacje Apple ukazały się jedynie na arXiv jako pre-printy i **nie przeszły jeszcze recenzji** w głównych czasopismach naukowych. Brak jest również dowodów na niezależną replikację wyników przez inne instytucje badawcze. Anthropic przedstawił kontrargumenty pokazujące, że modele mogą rozwiązywać problemy uznane przez Apple za niemożliwe, gdy usuniemy sztuczne ograniczenia (choć z drugiej strony samo wielokrotnie testowało i podawało benchmarki ze "sztucznym" wkładem i działającym modelem w "piaskownicy").

Mimo kontrowersji, zespół Apple ma poważne referencje naukowe - Samy Bengio był wcześniej dyrektorem w Google Brain, a publikacje wykazują wysoką jakość techniczną sugerującą autentyczne zainteresowanie naukowe.

### Wnioski: między nauką a strategią biznesową

Badania Apple o ograniczeniach LLM stanowią mieszankę wartościowych obserwacji naukowych i potencjalnie strategicznie motywowanej krytyki. Podczas gdy niektóre odkrycia - jak wrażliwość modeli na drobne zmiany w formułowaniu, tendencja do "overthinking" czy brak prawdziwego uogólnienia wiedzy - są cenne dla rozwoju AI, błędy metodologiczne i timing publikacji rodzą uzasadnione pytania o motywacje.

Niezaprzeczalnym faktem pozostaje dramatyczne opóźnienie Apple w wyścigu AI, co może tłumaczyć zarówno ton badań, jak i masywny plan inwestycyjny 500 miliardów dolarów. Paradoks jednoczesnej krytyki LLM i promocji Apple Intelligence dodatkowo komplikuje obraz.

Apple zdaje się pełnić rolę **"głosu ostrożności"** w branży przepełnionej hype'em, co może być podyktowane zarówno realnymi ograniczeniami technologicznymi, jak i chłodną kalkulacją biznesową - firma spóźniona w wyścigu może zyskiwać na narracji, że obecne rozwiązania rywali i tak nie są tak przełomowe. Strategia "szybciej nie znaczy lepiej" może przygotowywać grunt pod własne, być może bardziej dopracowane rozwiązania AI w przyszłości.

Ostatecznie, debata wywołana przez badania Apple, niezależnie od motywacji, przyczynia się do lepszego zrozumienia rzeczywistych możliwości i ograniczeń współczesnych systemów AI. Jak podsumował Gary Marcus: *"przynajmniej przez następną dekadę duże modele językowe znajdą swoje zastosowania (...), ale każdy, kto myśli, że LLM-y są bezpośrednią drogą do sztucznej inteligencji ogólnej mogącej fundamentalnie zmienić społeczeństwo na lepsze, oszukuje samego siebie"*.

Zgadzasz się z powyższą wypowiedzią? zostaw komentarz