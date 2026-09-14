---
categories:
  - LinkedIn
authors: ["[[Tomasz Karwatka]]"]
published: 2026-09-14
created: 2026-09-14
relevance: wysoka
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "szkolenia-AI"
---

Karwatka odwraca typowe podejście do wdrożeń AI: zamiast „przełamywać" opór zespołu, proponuje go obejść. Punktem wyjścia jest uznanie, że opór wobec AI w dużej części jest uzasadniony — stoją za nim bezpieczeństwo, jakość, odpowiedzialność i audytowalność, czyli te same kryteria, których organizacja broni na co dzień. Mechanizm, który nazywa **AI bypass**, polega na puszczeniu części realnej pracy równolegle dwoma torami — człowiek i agent AI — bez wypuszczania wyniku AI na produkcję, a potem porównaniu efektów. Efektem nie jest dyskusja o tym, czy AI jest bezpieczne, tylko dane: w których kategoriach zadań agent osiąga jaką skuteczność. Wartość tego ujęcia polega na przesunięciu sporu z poziomu przekonań na poziom pomiaru — i na tym, że decyzja o wdrożeniu zapada na wąskim, udowodnionym wycinku, a nie na całości procesu.

## Frameworki i metody
- **AI bypass** — mechanizm wdrożeniowy omijający opór zamiast konfrontacji z nim:
  1. Weź ok. 10% prawdziwej, bieżącej pracy (nie przypadków testowych).
  2. Puść ją równolegle dwoma torami: do człowieka i do agenta AI.
  3. Człowiek pracuje jak zwykle; wynik AI nie trafia na produkcję, więc ryzyko jest minimalne.
  4. Po tygodniu porównaj efekty obu torów.
  5. Ustal nie tylko *ile* przypadków AI obsługuje dobrze (np. 30%), ale *które* — to zwykle daje się określić precyzyjnie.
  6. W tym wycinku drąż dalej i wdrażaj; resztę na razie zostaw.
- **Rozmowa z decydentami na danych** — zamiast pytania „czy AI jest bezpieczne?" zespół przychodzi z wynikiem: „przetestowaliśmy 1200 realnych zadań, w tej kategorii agent osiąga X% skuteczności, tutaj możemy go wdrożyć".
- **Agent Orchestrator** — moduł w [[Open Mercato]] Enterprise zbudowany właśnie pod takie równoległe eksperymenty.

## Wnioski
- Opór wobec AI warto traktować jako informację o realnych ryzykach, a nie jako barierę do skruszenia — kategorie oporu (bezpieczeństwo, jakość, odpowiedzialność, audytowalność) wyznaczają kryteria, na których trzeba potem dowieść skuteczności.
- Kluczowa jest granularność: wartość eksperymentu bierze się nie z ogólnego wskaźnika skuteczności, ale z rozpoznania, *które* typy zadań agent obsługuje dobrze — to one stają się pierwszym zakresem wdrożenia.
- Równoległy tor bez wpuszczania wyników na produkcję to tani sposób na zbudowanie dowodów: obniża stawkę polityczną wdrożenia i zamienia decyzję z aktu wiary w decyzję na danych.

## Zastosowanie
Gotowy schemat pilotażu do zaproponowania organizacjom społecznym, które boją się wdrożenia AI — zwłaszcza tam, gdzie zarząd pyta o bezpieczeństwo danych i jakość. Przy szkoleniach i konsultacjach można go użyć jako ćwiczenia: wybrać jeden powtarzalny proces (np. obsługa zapytań darczyńców, wstępna redakcja treści), przez tydzień prowadzić go dwutorowo i zebrać własne dane zamiast argumentów. Dobrze uzupełnia materiały o strategii wdrażania AI w [[dobryai.pl]].
