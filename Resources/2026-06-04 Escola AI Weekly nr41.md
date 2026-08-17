---
categories:
  - "Emails"
published: 2026-06-04
created: 2026-06-09
labels:
  - "Krzysztof Wojewodzic"
relevance: wysoka
tags:
  - "trendy-AI"
  - "strategia-AI"
  - "narzędzia-AI"
---

# Escola AI Weekly #41

Tygodniowy przegląd Krzysztofa Wojewodzica obejmuje siedem tematów, które łączy jeden mianownik: AI przestaje być abstrakcją, a zaczyna być kwestią kosztów, kompetencji i odpowiedzialności. Encyklika papieska "Magnifica Humanitas" okazała się głębszą analizą ryzyk AI niż większość dokumentów z laboratoriów badawczych, a raport PARP i UJ pokazał, że polskie firmy mają problem nie z dostępem do technologii, lecz z dostępem do ludzi, którzy ją rozumieją. Równolegle Uber spalił roczny budżet tokenów w cztery miesiące, demonstrując skalę zjawiska określanego jako "token maxing" — wdrażania AI bez mierzenia efektów.

## Frameworki i metody

- **Token maxing** — wdrażanie [[AI]] do wszystkiego bez analizy opłacalności; antidotum to mierzenie zużycia tokenów per use case i eliminacja agentów bez mierzalnego ROI
- **Effort control w [[Claude AI|Claude]]** — mechanizm pozwalający użytkownikowi określić poziom wysiłku modelu (oszczędny vs maksymalny); model szacuje zużycie tokenów i pyta o zgodę przy dużych zadaniach
- **Kompresja kontekstu** — zamiast trzymania pełnych dokumentów model ekstrahuje najważniejsze ~10% informacji podtrzymujących wątek; sprawdzalne przez eksport pamięci z Claude, ChatGPT lub Gemini
- **Lokalny deployment modeli** — [[Plum]] (70B parametrów) można uruchomić lokalnie na 16 GB RAM bez wysyłania danych do zewnętrznych serwerów; ważne dla instytucji przetwarzających wrażliwe dane

## Kluczowe dane

- 25% polskich firm ma dostęp do wykwalifikowanych ekspertów AI (raport PARP/UJ, edycja 3)
- 60% zużycia tokenów na [[OpenRouter]] to modele chińskie (Kimi, DeepSeek, GLM, Qwen)
- [[Anthropic]] rośnie 130% kwartał do kwartału; zużycie tokenów przez płacących użytkowników [[Claude AI|Claude]] ponad 10× wyższe niż [[ChatGPT]]

## Wnioski

- Dokument papieski "Magnifica Humanitas" trafnie identyfikuje trzy ryzyka AI: nowe formy niewolnictwa (adnotatorzy danych), koncentrację władzy w rękach wąskiej elity technologicznej oraz autonomiczne systemy zbrojne — ale teoria gier (konkurencja firm) jest silniejsza niż etyczne apele
- Polski rynek AI ma lukę kompetencyjną, nie technologiczną: połowa firm nie robi nic zamiast inwestować w szkolenia własnych pracowników, co oznacza rosnącą premię za ekspertów AI
- [[Plum]] jako open-source model z uregulowanym statusem prawnym danych treningowych może być realną opcją dla polskiej administracji i organizacji przetwarzających wrażliwe dane obywateli

## Cytat

> Kompetencji AI nie nabywa się w kilka tygodni. Narzędzi można się nauczyć stosunkowo szybko. Sposobu myślenia, który pozwala ocenić, kiedy AI pomaga a kiedy szkodzi, uczy się latami.

## Zastosowanie

Luka kompetencji AI w Polsce (tylko 25% firm z dostępem do ekspertów) to konkretny argument w rozmowach z NGO o wartości szkoleń z AI — organizacje, które zbudują wewnętrzne kompetencje teraz, zyskają trudną do nadrobienia przewagę. Zjawisko token maxingu i effort control w [[Claude AI|Claude]] są bezpośrednio przydatne przy projektowaniu automatyzacji dla klientów: warto od razu mierzyć koszty tokenów i unikać wdrożeń bez mierzalnego efektu. [[Plum]] warto monitorować jako opcję dla NGO z wymogami RODO, które nie chcą wysyłać danych do zewnętrznych dostawców.
