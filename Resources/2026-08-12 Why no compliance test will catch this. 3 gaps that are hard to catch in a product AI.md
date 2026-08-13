---
authors:
  - '[[Kasia Szczesna]]'
categories:
  - Clippings
created: '2026-08-13'
published: '2026-08-12'
relevance: wysoka
source: >-
  [[Archives/2026-08-12 Why no compliance test will catch this. 3 gaps that are
  hard to catch in a product AI|2026-08-12 Why no compliance test will catch
  this. 3 gaps that are hard to catch in a product AI]]
tags:
  - strategia-AI
  - produkty-cyfrowe
  - LLM
url: >-
  https://behavioralinsight.substack.com/p/why-no-compliance-test-will-catch?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true
---

# Why no compliance test will catch this. 3 gaps that are hard to catch in a product AI

Kasia Szczesna (BehaviorAI) pokazuje, że etykieta „to jest AI” wymagana przez art. 50 AI Act może być formalnie zgodna z prawem i jednocześnie kompletnie nieskuteczna w praktyce — bo prawo pyta tylko, czy komunikat istnieje, a nie jak długo jest widoczny, jak często się powtarza i z jak silnym kontekstem konkuruje. Autorka opisuje trzy behawioralne luki: zbyt krótki czas ekspozycji komunikatu, habituację (mózg przestaje go rejestrować już po kilku ekspozycjach) oraz niedopasowanie kontekstu, gdy AI pełni rolę „towarzysza” i cała reszta doświadczenia produktu działa przeciwko jednej etykiecie transparentności. To ważny głos w dyskusji o AI Act, bo pokazuje różnicę między literą przepisu a realną ochroną użytkownika — istotne przy projektowaniu i audycie chatbotów/voicebotów AI, temat blisko związany z checklistą compliance z artykułu „Nowe przepisy i pozwy dotyczące AI”.

## Frameworki i metody

**3 luki, których nie wyłapie standardowy test zgodności:**
1. **Czas ekspozycji** — krótka widoczność komunikatu (np. 7 sekund) wystarcza formalnie, ale nie wystarcza, by informacja została świadomie przetworzona; umiejscowienie komunikatu decyduje o skuteczności silniej niż sama treść.
2. **Habituacja** — ten sam komunikat w tej samej formie przestaje być realnie rejestrowany już po kilku pierwszych ekspozycjach; komunikaty zmieniające formę (polimorficzne) są znacznie bardziej odporne na spadek uwagi niż statyczne.
3. **Niedopasowanie kontekstu** — zgodnie z paradygmatem „Computers Are Social Actors” ludzie automatycznie stosują wobec AI te same reguły społeczne co wobec ludzi, nawet wiedząc, że rozmawiają z maszyną; im silniej produkt buduje wrażenie relacji, tym mocniej pracuje przeciwko własnej etykiecie transparentności.

**2 wzorce projektowe wynikające z tych luk:**
- **Ekspozycja skalowana do ryzyka** — im poważniejsza potencjalna konsekwencja interakcji, tym dłużej i bardziej widocznie komunikat o AI powinien pozostawać na ekranie (np. chwilowe spowolnienie przejścia do rozmowy, minimalny wymagany kontakt wzrokowy z komunikatem).
- **Sygnał zmienny w czasie** — zamiast jednej statycznej etykiety pokazanej raz na starcie, forma, miejsce i sformułowanie komunikatu rotują przy kolejnych powrotach użytkownika, żeby nie stały się częścią tła.

Autorka rozwija te mechanizmy w [[BehaviorAI Design Framework]].

## Kluczowe dane

- Przeniesienie ostrzeżenia z dołu na górę opakowania papierosów zwiększyło jego rozpoznawalność wśród palaczy z 20% do 95% (badanie w Kanadzie) — ta sama treść, inne miejsce.
- Aktywność mózgu odpowiadająca za przetwarzanie komunikatów bezpieczeństwa gwałtownie spada już po pierwszych kilku ekspozycjach (badanie fMRI).
- W 3-tygodniowym eksperymencie terenowym przestrzeganie ostrzeżeń systematycznie spadało z każdym kolejnym dniem korzystania z aplikacji.

## Wnioski

- Zgodność z literą prawa (np. art. 50 AI Act) i realna ochrona użytkownika to dwie osobne rzeczy — checklisty compliance nie zadają pytań o czas ekspozycji, powtarzalność czy kontekst komunikatu, więc produkt może przejść każdy test prawny i wciąż zawieść w realnym użyciu.
- Statyczna, jednorazowa etykieta „to jest AI” słabnie z czasem — projektując chatboty/voiceboty dla klientów warto od razu zakładać rotację formy komunikatu, a nie jednorazowe wdrożenie disclaimera.
- W produktach AI budujących relację z użytkownikiem (towarzysz, asystent, powiernik) sama etykieta nie wystarczy — potrzebna jest decyzja produktowa o granicach personalizacji i emocjonalnej responsywności, bo żadna etykieta nie odwróci automatycznej reakcji społecznej człowieka na system.

## Cytat

> Im silniej produkt buduje wrażenie relacji, tym mocniej pracuje przeciwko własnej etykiecie transparentności, niezależnie od tego, jak jasno ta etykieta jest sformułowana.

## Zastosowanie

Dobre uzupełnienie checklisty compliance z art. 50 AI Act (por. notatka „Nowe przepisy i pozwy dotyczące AI”) — przy doradztwie wdrożeń chatbotów/voicebotów dla klientów warto oceniać nie tylko formalną zgodność etykiety AI, ale też jej realną skuteczność (czas ekspozycji, rotację formy, poziom personalizacji produktu). Przydatne jako argument w rozmowach z organizacjami planującymi AI-owe narzędzia budujące bliższą relację z użytkownikiem (np. asystenci dla podopiecznych).
