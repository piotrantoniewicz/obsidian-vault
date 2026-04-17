---
categories: Clippings
authors:
  - "[[Eileen Guo]]"
url: https://www.technologyreview.com/2025/06/11/1118233/amsterdam-fair-welfare-ai-discriminatory-algorithms-failure/
source: "[[2025-06-11 Inside Amsterdam s high-stakes experiment to create fair welfare AI]]"
published: 2025-06-11T00:00:00.000Z
created: 2026-03-19T00:00:00.000Z
relevance: wysoka
tags:
  - strategia-AI
  - organizacje-społeczne
---

# Inside Amsterdam's High-Stakes Experiment to Create Fair Welfare AI

Eileen Guo (MIT Technology Review) dokumentuje wieloletni eksperyment Amsterdamu z systemem "Smart Check" — algorytmem AI do wykrywania potencjalnych oszustw w systemie świadczeń socjalnych. Miasto zrobiło wszystko "dobrze": konsultacje z ekspertami, audyty stronniczości, testy bias, dialog z interesariuszami, reweighting danych. Mimo to pilot zakończył się klęską: algorytm był stronniczy (najpierw wobec migrantów i mężczyzn, po korekcji — wobec Holenderek i kobiet), a efektywność nie przewyższała ludzkich pracowników. Wniosek: "odpowiedzialna AI" jako zestaw narzędzi technicznych nie rozwiązuje fundamentalnie złych założeń.

## Kluczowe dane
- Szacunkowy koszt projektu: €500,000 + €35,000 (Deloitte) — przy budżecie "jednego eksperta od TV"
- Wstępny model: o 14% wyższe prawdopodobieństwo błędnego flagowania mężczyzn; ~2x wyższe dla osób z obywatelstwem spoza Zachodu
- Po reweightingu: nowe biasy (Holenderki, kobiety z dziećmi) pojawiły się w pilotażu na żywych danych
- 3,400 historycznych spraw użytych do trenowania modelu
- 1,600 wniosków o świadczenia przetworzonych w pilotażu przed zatrzymaniem

## Frameworki i metody
- **Explainable Boosting Machine** — algorytm interpretable ML używany przez Amsterdam zamiast black box; 15 zmiennych bez danych demograficznych (bez płci, narodowości, wieku, kodów pocztowych)
- **Training-data reweighting** — technika korekcji biasów: zmiana wag danych treningowych tak, by zmniejszyć disparytety; Amsterdam zastosował ją po wykryciu biasów w pierwszej wersji — ale to ujawniło nowe biasy w danych na żywo
- **Responsible AI toolkit critique** — de Zwart (Bits of Freedom): Amsterdam użył wszystkich narzędzi odpowiedzialnego AI (ocena bias, HRA, audyt) i mimo to realizował "fundamentalnie zły pomysł"

## Wnioski
- "Odpowiedzialna AI" to za mało: techniczne narzędzia korekcji bias nie mogą naprawić systemów zbudowanych na złych założeniach filozoficznych i politycznych
- Historyczne dane zawierają historyczne biasy — trenowanie na nich perpetuuje stare niesprawiedliwości, nawet po korekcie
- Kluczowe pytania są polityczne, nie techniczne: "czym jest bias?", "kto ma prawo profilować obywateli?" — tego nie da się wsadzić w checkbox
- Powrót do "systemu analogowego" nie jest rozwiązaniem — ludzcy pracownicy też są stronniczy, ale przynajmniej wymagają uzasadnienia
- Koszt alternatywny: €500k na algorytm vs. zatrudnienie ludzi do pracy z beneficjentami

## Cytat
> „Miasto użyło wszystkich narzędzi z zestawu odpowiedzialnej AI. Mimo to kontynuowało coś, co jest fundamentalnie złym pomysłem." — Hans de Zwart, Bits of Freedom

## Zastosowanie
Przed wdrożeniem AI do decyzji dotyczących życia ludzi (kwalifikowanie do świadczeń, ocena ryzyka, selekcja) organizacje powinny zadać pytanie filozoficzne: *czy jest to w ogóle właściwe zastosowanie AI?* — zanim przejdą do pytania technicznego *jak to zrobić fair*.
