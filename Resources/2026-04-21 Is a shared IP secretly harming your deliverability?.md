---
categories: Clippings
authors: ["[[Sara Cederberg]]"]
url: "https://www.civicshoutnewsletter.com/p/is-a-shared-ip-secretly-harming-your-deliverability?utm_source=www.civicshoutnewsletter.com&utm_medium=newsletter&utm_campaign=why-your-fundraising-emails-need-their-own-subdomain&_bhlid=270d76d9e8629520aad616daed2f5789644014e4"
source: "[[Archives/2026-04-21 Is a shared IP secretly harming your deliverability?|2026-04-21 Is a shared IP secretly harming your deliverability?]]"
published: 2026-04-21
created: 2026-05-29
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
---

# Is a shared IP secretly harming your deliverability?

Artykuł opisuje case study Humane Society of Utah, które przez długi czas zmagało się ze stagnacją przychodów z emaili — mimo testowania treści i landing page'y. Okazało się, że problem tkwił nie w kreatywności, lecz w dostarczalności: platforma emailowa umieściła ich IP w słabo performującym puli współdzielonej. Rozwiązaniem była migracja na dedykowane IP w Mailchimp, uprzednie wyczyszczenie listy przez [[BriteVerify]] oraz ostrożne rozgrzanie IP przez wysyłanie najpierw do najbardziej zaangażowanych odbiorców. Wynik: prawie podwojenie przychodów z emaili rok do roku.

## Frameworki i metody

- **Email hygiene review przed migracją** — zamiast audytu treści, HSU zleciło przegląd higieny listy ([[RKD Group]]); usunięto nieaktywne i nieprawidłowe adresy przez [[BriteVerify]] przed importem na nowe IP
- **Warm-up IP** — staggerowane onboarding: welcome series dla nowych, reactivation series dla połowy listy, która wygasła; pierwsze wysyłki do segmentów o najwyższym zaangażowaniu

## Kluczowe dane

- HSU zebrało więcej przychodów z emaili w ciągu 7 miesięcy 2023 roku (styczeń–lipiec) niż przez cały rok 2022
- Do końca roku prawie podwoiło wynik z 2022

## Wnioski

- Stagnacja przychodów z emaili jest często problemem widoczności, nie jakości treści — warto najpierw sprawdzić seed testy w Gmailu, Yahoo i Outlooku
- Nagły spadek zaangażowania całego segmentu w tym samym oknie czasowym to sygnał dostarczalnościowy, nie sygnał braku zainteresowania
- Migracja na dedykowane IP bez uprzedniego wyczyszczenia listy to szybka droga do uszkodzenia reputacji nadawcy

## Cytat

> Płaska krzywa przychodów z emaili to problem widoczności udający problem kreatywny — częściej niż lubimy przyznać.

## Zastosowanie

Dla organizacji prowadzących fundraising emailowy — w tym NGO szkolonych przeze mnie — ten artykuł daje prosty schemat diagnozy: zanim zmienisz copy, sprawdź, czy emaile w ogóle trafiają do skrzynki odbiorczej. Case study HSU można wykorzystać jako przykład w kursie mailowym, żeby pokazać wagę infrastruktury nad kreatywnością.
