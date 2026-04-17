---
categories: Clippings
authors: ["[[Heather Mansfield]]"]
url: https://www.nptechforgood.com/2026/03/26/ripples-of-a-click-the-anatomy-of-a-nonprofit-donation/
source: "[[Archives/2026-03-26 Ripples of a Click The Anatomy of a Nonprofit Donation|2026-03-26 Ripples of a Click The Anatomy of a Nonprofit Donation]]"
published: 2026-03-26
created: 2026-04-13
relevance: wysoka
tags:
  - "fundraising"
  - "automatyzacja"
  - "organizacje-społeczne"
---

# Ripples of a Click: The Anatomy of a Nonprofit Donation

Artykuł [[Heather Mansfield]] (sponsorowany przez [[Click & Pledge]]) demistyfikuje technologiczną i finansową architekturę, przez którą przechodzi każda darowizna online. Autorka rozkłada donację na trzy warstwy — bramka płatności, warstwa aplikacji i kwestia powiernictwa środków — i argumentuje, że większość organizacji traci przychody nie na standardowych opłatach kartowych, lecz na ukrytych prowizjach, domyślnych napiwkach i ryzykownych modelach agregatorów. Artykuł jest wprost reklamą [[Click & Pledge]], ale framework "trzech fal" jest analitycznie użyteczny i niezależny od platformy.

## Frameworki i metody

- **Ripple 1 — Toll Booth (bramka płatności)**: Koszt bazowy infrastruktury — [[Stripe]], [[PayPal]], Square pobierają ok. 2,9% + 0,30 USD za kartę lub 0,8% (max 5 USD) za przelew ACH; to koszt stały, zcentralizowany, trudny do negocjacji — "opłata autostradowa"
- **Ripple 2 — Application Layer (warstwa aplikacji)**: Oprogramowanie, z którym kontaktuje się donator — formularze, strony kampanii, zarządzanie darowiznami cyklicznymi, CRM; trzy modele:
  - *Rower* — bezpośredni link płatniczy ([[Stripe]] / [[PayPal]] donate button) bez żadnych narzędzi campaignowych
  - *Frankenstein Stack* — DIY z niezintegrowanych narzędzi generujący ukryte podatki: podatek czasu (ręczne synchronizacje danych), podatek tarcia (porzucanie formularzy) i podatek zgodności (PCI compliance w rozproszonym środowisku)
  - *Platforma dedykowana* — zintegrowane środowisko z formularzami, CRM, peer-to-peer, recurring giving; wyższy koszt subskrypcji, wyższy ROI netto
- **Ripple 3 — Custody Question (powiernictwo środków)**: Kluczowe pytanie: kto fizycznie trzyma pieniądze?
  - *Model agregatora* — środki przepływają przez konta platformy (opóźnienia 7–15 dni, ryzyko upadłości platformy = brak dostępu do środków)
  - *Model direct settlement* — pieniądze trafiają bezpośrednio na konto bankowe organizacji; platforma tylko orkiestruje transakcję, nie dotyka środków

- **4 pytania kontrolne do dostawcy platformy**:
  1. Czy środki trafiają bezpośrednio na nasze konto, czy przechodzą przez wasze?
  2. Czy możemy zobaczyć osobno opłatę autostradową i koszt pojazdu (platformy)?
  3. Czy w procesie donacji są domyślnie zaznaczone napiwki lub dodatkowe opłaty?
  4. Co stanie się z naszymi środkami i danymi, jeśli wasza platforma zniknie jutro?

## Kluczowe dane

- Standardowy koszt transakcji kartowej: 2,9% + 0,30 USD ([[Stripe]], [[PayPal]], Square)
- Przelew ACH: 0,8%, maksymalnie 5 USD za transakcję
- Część platform pobiera łącznie ponad 18% darowizny przez stos opłat ukrytych pod domyślnymi napiwkami

## Wnioski

- Największe ryzyko finansowe nie leży w standardowych opłatach kartowych, lecz w ukrytych strukturach opłat i modelu powiernictwa — organizacje często nie wiedzą, że ich środki przechodzą przez konta platformy i są narażone na ryzyko jej upadłości.
- ROI platformy fundraisingowej powinno być mierzone zyskiem netto (konwersja donatorów, oszczędność czasu pracy), a nie procentem opłaty platformowej — "bezpłatne" platformy mogą wyciągać więcej niż płatne dzięki ukrytym mechanizmom.
- Przy wyborze narzędzia fundraisingowego dla klienta NGO kluczowe jest oddzielenie kosztu infrastruktury płatności od kosztu aplikacji i zbadanie modelu powiernictwa — szczególnie ważne przy kampaniach z dużym wolumenem.

## Zastosowanie

Przy doradztwie organizacjom w wyborze narzędzi fundraisingowych warto stosować framework "trzech fal" jako strukturę audytu — pozwala zadać właściwe pytania zanim organizacja podpisze umowę z platformą. Wiedza o ryzyku modelu agregatora może być elementem szkolenia z digital fundraisingu dla NGO, zwłaszcza w kontekście bezpieczeństwa środków. Cztery pytania kontrolne nadają się bezpośrednio jako lista kontrolna do materiałów kursowych lub konsultacyjnych.
