---
categories:
  - Emails
created: '2026-08-19'
labels:
  - wPraktyce
published: '2026-08-18'
relevance: wysoka
tags:
  - strategia-AI
  - narzędzia-AI
  - automatyzacja
---

# Nie korzystasz z AI, bo boisz się RODO?

Patryk Łopot z wPraktyce.AI opisuje architekturę „anonimizacji w locie" — automatycznego i odwracalnego maskowania danych osobowych przed wysłaniem dokumentu do modelu AI, dzięki czemu wrażliwe dane (nazwiska, PESEL-e, kwoty) fizycznie nie opuszczają komputera użytkownika, a model operuje wyłącznie na anonimowych etykietach. Rozwiązanie adresuje realny problem branż o wysokiej wrażliwości danych — doradztwo podatkowe, księgowość, kadry, prawo, medycyna — gdzie RODO blokuje wysyłanie danych klientów do chmury właśnie tam, gdzie AI dałoby największą oszczędność czasu. Newsletter kończy się konkretnym ćwiczeniem diagnostycznym: zidentyfikować procesy odpuszczone z powodu danych wrażliwych, wybrać ten najbardziej bolesny i wypisać dokładnie, co wymaga maskowania.

## Frameworki i metody

- **Anonimizacja w locie** — architektura w trzech krokach: (1) maskowanie lokalne — system automatycznie zamienia dane osobowe na etykiety typu „imię 1", „PESEL 1" przed wysyłką do modelu; (2) przetwarzanie w chmurze — model liczy, zestawia i analizuje wyłącznie na etykietach, nigdy nie poznając prawdziwych wartości; (3) dekodowanie lokalne — po otrzymaniu odpowiedzi system podmienia etykiety z powrotem na rzeczywiste dane, widoczne tylko u użytkownika. Autor podkreśla, że to architektura składana pod konkretny przypadek (branża, rodzaj dokumentów), nie gotowy produkt z półki.
- **Trzy pytania diagnostyczne** — do wypisania przed rozmową o wdrożeniu: które procesy dziś nie są ruszane AI wyłącznie z powodu danych wrażliwych; który z nich jest najbardziej powtarzalny i czasochłonny; co dokładnie trzeba w nim zamaskować (imiona, PESEL, kwoty, adresy).

## Kluczowe dane

- Przykład z case study: 50+ pracowników × 12 miesięcy list płac = setki dokumentów wymagających anonimizacji przy ręcznym podejściu.

## Wnioski

- Architektura maskowania lokalnego i dekodowania po stronie użytkownika to praktyczny wzorzec do proponowania wdrożeń AI tam, gdzie [[RODO]] dziś blokuje korzystanie z narzędzi chmurowych — istotne dla organizacji przetwarzających dane darczyńców, beneficjentów czy podopiecznych.
- Wybór „najbardziej bolesnego" procesu jako pierwszego kandydata do automatyzacji (a nie najprostszego) to przydatna heurystyka przy planowaniu wdrożeń AI w organizacjach.
- [[Patryk Łopot]] z [[wPraktyce.AI]] pozycjonuje się jako dostawca architektur „szytych na miarę" pod konkretną branżę, nie gotowego produktu — model usługowy warty obserwacji przy budowaniu własnej oferty wdrożeniowej AI.

## Cytat

> Marker na papierze, tylko automatyczny i odwracalny.

## Zastosowanie

Wzorzec anonimizacji w locie można zaproponować organizacjom pracującym z wrażliwymi danymi beneficjentów (pomoc społeczna, poradnictwo, ochrona zdrowia) jako sposób na bezpieczne wdrożenie AI mimo RODO. Trzy pytania diagnostyczne z newslettera nadają się jako ćwiczenie na warsztatach o wdrażaniu AI w organizacjach.
