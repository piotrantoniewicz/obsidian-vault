---
categories:
  - Clippings
authors: ["[[Konrad Krawczuk]]"]
url: "https://chcedointernetu.pl/blog/framework-prosto-jak-rozmawiac-z-ai"
source: "[[Archives/2026-08-18 Framework PROSTO - jak rozmawiać z AI żeby działało|2026-08-18 Framework PROSTO - jak rozmawiać z AI żeby działało]]"
published: 2026-08-18
created: 2026-08-28
relevance: wysoka
tags:
  - "prompt-engineering"
  - "szkolenia-AI"
  - "narzędzia-AI"
---

# Framework PROSTO - jak rozmawiać z AI żeby działało

Konrad Krawczuk opisuje autorski framework PROSTO (Profil, Rezultat, Odbiorca, Styl, Tło lokalne, Ocena) — polskojęzyczny szablon promptu dla właścicieli lokalnych firm, zbudowany na doświadczeniu z klientami wdrożeniowymi z Trójmiasta. Kluczowa różnica względem znanych frameworków (CLARITY, SOCRATES) to szósty krok — karta oceny 8 kryteriów, która zamienia pisanie promptów w mierzalny, powtarzalny proces zamiast publikowania "na ślepo". Autor przetestował framework na benchmarku 10 000 syntetycznych promptów i pokazał liczbowo, gdzie ludzie najczęściej tracą jakość: brak wyróżnienia od konkurencji i brak lokalnego/organizacyjnego kontekstu. To konkretny, oparty na danych argument za tym, że szkolenie z promptowania powinno uczyć nie tylko formułowania promptów, ale też ich oceny.

## Frameworki i metody

**Framework PROSTO — 6 kroków:**
1. **P – Profil** — kim jestem, co robię, skąd jestem, co mnie wyróżnia.
2. **R – Rezultat** — konkretny cel działania (nie "napisz post", tylko np. "chcę, żeby dzwonili").
3. **O – Odbiorca** — kto ma to zobaczyć, jaki ma problem, gdzie to zobaczy.
4. **S – Styl** — ton, długość, format, czego unikać.
5. **T – Tło lokalne** — sezon, konkurencja, lokalne wydarzenia, specyfika miejsca.
6. **O – Ocena** — karta 8 kryteriów (cel mierzalny, odbiorca się rozpozna, lokalny kontekst widoczny, ton pasuje do marki, konkretne CTA, brak "napompowanego" języka, odpowiednia długość, wyróżnienie od konkurencji), punktacja 0-2 za kryterium, suma 0-16.

**Interpretacja wyniku karty oceny:** 14-16 pkt — publikuj; 10-13 pkt — popraw słabe punkty; 6-9 pkt — wróć do promptu i uzupełnij kontekst; 0-5 pkt — zacznij od nowa od kroku Profil.

## Kluczowe dane

- 80% z 10 000 testowanych promptów dostało 0 punktów za kryterium "wyróżnienie się od konkurencji"
- 55% promptów nie definiuje odbiorcy ani lokalnego kontekstu
- Samo dodanie kroku oceny wyniku (bez zmiany promptu) podnosi finalną jakość treści o 18%
- Prompty z konkretnym lokalnym tłem (miasto, sezon, wydarzenie) mają średnio o 3,4 punktu wyższy wynik

## Wnioski

- Krok Ocena domyka pętlę prompt → wynik → ocena → poprawa, czego brakuje w popularnych anglojęzycznych frameworkach — to gotowy wzorzec do przeniesienia na warsztaty AI dla NGO.
- Największym słabym punktem promptów jest brak wyróżnienia się od organizacji podobnych oraz brak kontekstu (lokalnego, organizacyjnego, programowego) — wniosek wprost przekładalny na promptowanie w kontekście misji i grupy docelowej NGO.
- Sama karta oceny (8 kryteriów, skala 0-16) to gotowe narzędzie dydaktyczne — łatwe do zaadaptowania jako checklist w kursie lub warsztacie z AI.

## Cytat

> Framework nie gwarantuje, że zawsze będzie excellent — gwarantuje, że wiesz na czym stoisz i widzisz, co poprawić.

## Zastosowanie

Gotowy, przetestowany na danych wzorzec do adaptacji na szkolenia AI dla NGO — PROSTO można przełożyć na kontekst organizacji społecznej (misja, grupa docelowa, ton komunikacji, kontekst programowy/lokalny) i wykorzystać kartę oceny jako narzędzie w kursie mailowym "Fundraising z AI" lub warsztatach wdrożeniowych. Sam pomysł na benchmark (testowanie promptów na dużej próbie i mierzenie, gdzie ludzie tracą jakość) to też inspiracja do własnej ewaluacji skuteczności szkoleń.
