---
categories:
  - Clippings
authors: ["[[Marek Staniszewski]]"]
url: "https://www.linkedin.com/pulse/pu%C5%82apka-kontynuacji-czyli-dlaczego-ai-nie-zbuduje-marek-staniszewski-1d0gf/"
source: "[[Archives/2026-08-28 Pułapka kontynuacji – czyli dlaczego AI raczej nie zbuduje dobrego scenariusza strategicznego|2026-08-28 Pułapka kontynuacji – czyli dlaczego AI raczej nie zbuduje dobrego scenariusza strategicznego]]"
published: 2026-08-28
created: 2026-08-29
relevance: wysoka
tags:
  - "strategia-AI"
  - "LLM"
  - "trendy-AI"
---

# Pułapka kontynuacji – czyli dlaczego AI raczej nie zbuduje dobrego scenariusza strategicznego

Marek Staniszewski przeprowadza eksperyment „wehikuł czasu": cofa GPT-4o do wiedzy sprzed knowledge cutoff (wrzesień 2023) i pyta model o wydarzenia, które faktycznie zaszły później (przełom DeepSeek R1, spadek kapitalizacji Nvidii), sprawdzając mierzalnie — przez Brier score, a nie opinię — jak dobrze LLM radzi sobie z prognozowaniem nieciągłości. Wniosek: model świetnie ekstrapoluje istniejące trendy (L1), ale konsekwentnie odrzuca scenariusze łamiące dziś obowiązujące reguły — zjawisko nazwane „pułapką kontynuacji" (continuity trap). Sto niezależnych wywołań modelu nie daje panelu stu opinii, tylko jedną opinię powtórzoną sto razy z niewielkim szumem sformułowań. Tekst jest czwartym w serii eksperymentów autora pokazujących, że LLM-y systematycznie regresują do konsensusu zapisanego w danych treningowych — w kreatywności, pozycjonowaniu marki i teraz w prognozowaniu.

## Frameworki i metody

**Cztery poziomy pytań strategicznych (drabina L1–L4):** model radzi sobie dobrze na poziomie ekstrapolacji trendu (L1) i umiarkowanie na poziomie wypełniania zadanej ramy wariantami (L2), słabiej przy kwestionowaniu założeń (L3), a na poziomie przeformułowania samej ramy przyczynowej (L4) zawodzi niemal całkowicie.

**Stożek możliwych przyszłości (futures cone) i „rozwieranie stożka":** planowanie scenariuszowe polega na budowaniu wielu wzajemnie wykluczających się, ale wiarygodnych światów (S1 = kontynuacja trendu, S2/S3 = scenariusze łamiące dziś obowiązującą regułę) — najcenniejszy jest scenariusz sprzeczny z konsensusem, bo o tym zgodnym z konsensusem myślą też konkurenci.

**Pięć zaleceń praktycznych do pracy z LLM w planowaniu scenariuszowym:**
1. Nie pytaj „co się wydarzy?" — to zwraca konsensus. Narzuć trajektorię wprost: „opisz świat, w którym teza X upada".
2. Proś o atak na własną hipotezę (stress-test), nie o samą hipotezę — w tej roli model sprawdza się dobrze.
3. Wymuś łamanie założeń proceduralnie: każ modelowi wypisać założenia kategorii, a potem każde po kolei zanegować lub podmienić na założenie z odległej domeny.
4. Nie uśredniaj wielu wywołań modelu — to jedna opinia z szumem, nie rozkład poglądów panelu ekspertów.
5. Nie traktuj pewności językowej jako wskaźnika trafności — model potrafi brzmieć kompetentnie, mając rację jedynie w 27%.

**Odwrócenie perspektywy — model jako mapa konsensusu:** zamiast pytać „czy X się wydarzy?", warto pytać „co obecnie uchodzi za oczywiste?" — w tej roli LLM jest precyzyjnym narzędziem do pomiaru granic dominującego konsensusu rynkowego, czyli wskazania, gdzie warto szukać scenariuszy S2/S3.

## Kluczowe dane
- Sto niezależnych wywołań GPT-4o o prawdopodobieństwo przełomu DeepSeek: średnia 27,6% (odchylenie std. 3,7 pkt proc.), model odpowiedział „NIE" 100 razy na 100.
- Test kontrolny (upadłość WeWork, czysta ekstrapolacja trendu L1): model trafił, przypisując 77% prawdopodobieństwa — niemal dziesięciokrotnie wyższa trafność niż przy zdarzeniu przełomowym.
- 27 stycznia 2025 r. akcje Nvidii spadły o ok. 17% w ciągu jednej sesji (ok. 600 mld USD kapitalizacji) po publikacji DeepSeek R1 — zdarzenie, którego model nie przewidział w żadnym z 100 wywołań.

## Wnioski
- „Pułapka kontynuacji" to konkretne ryzyko przy używaniu [[LLM]] do pracy strategicznej dla organizacji: model nie zbuduje samodzielnie scenariusza łamiącego dziś obowiązujące reguły, więc scenariuszowanie transformacji sektora (np. finansowania NGO, technologii, regulacji) wymaga narzucenia mu założenia wprost, a nie pytania otwartego.
- Wielokrotne odpytywanie modelu nie zastępuje panelu eksperckiego — sto wywołań daje złudzenie różnorodności opinii, a w rzeczywistości jest to jeden pogląd zapisany na sto sposobów; to bezpośrednio podważa praktykę „ankietowania" LLM jako substytutu konsultacji z ludźmi.
- Model najlepiej sprawdza się jako „lustro konsensusu" — narzędzie do mapowania tego, co dziś uchodzi za oczywiste, a nie jako wyrocznia przewidująca przyszłość; to praktyczna wskazówka do formułowania promptów w pracy doradczej i szkoleniowej z AI.

## Cytat
> Model językowy ma tendencję do generowania odpowiedzi bliższych temu, co częste, typowe i statystycznie „środkowe" — zamiast eksplorować to, co skrajne, rzadkie i nietypowe.

## Zastosowanie
Przy pracy nad strategiami dla organizacji społecznych i wdrożeniami AI warto wprost ostrzegać klientów przed traktowaniem LLM jako generatora nieoczywistych scenariuszy przyszłości — model lepiej sprawdzi się jako narzędzie do mapowania obecnego konsensusu branżowego niż do przewidywania przełomów. Pięć zaleceń praktycznych (zwłaszcza „proś o atak na hipotezę" i „wymuś łamanie założeń proceduralnie") można wykorzystać wprost w szkoleniach z prompt engineeringu dla zespołów NGO przy budowaniu scenariuszy strategicznych czy planów rozwoju.
