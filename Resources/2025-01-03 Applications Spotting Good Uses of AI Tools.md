---
categories: Clippings
authors: "[[Joshua Essex]]"
url: https://technicallyoptimistic.substack.com/p/applications-spotting-good-uses-of
source: "[[2025-01-03 Applications Spotting Good Uses of AI Tools]]"
published: 2025-01-03
created: 2026-03-04
relevance: wysoka
tags:
  - strategia-AI
  - organizacje-społeczne
  - narzędzia-AI
---

# Applications: Spotting Good Uses of AI Tools

Joshua Essex, CTO platformy danych wymiaru sprawiedliwości [[Recidiviz]], przedstawia praktyczny framework do oceny, czy dane zastosowanie AI jest właściwe dla organizacji misyjnej. Główna teza: presja na wdrażanie AI — w tym ze strony darczyńców — wyprzedza rozumienie jej implikacji, co jest szczególnie groźne w pracy z wrażliwymi grupami. Essex nie odradza AI, ale proponuje cztery pytania filtrujące, które powinny poprzedzać każdą decyzję o adopcji. Framework ma szerokie zastosowanie dla NGO: od systemu rejestracji wolontariuszy po automatyzację raportowania i obsługę darczyńców.

## Frameworki i metody

### 4 pytania do oceny zastosowania AI w organizacji:

**1. Jakie jest kryterium dokładności?**
- Jeśli dokładność jest absolutna i konieczna — nie używaj [[LLM]]
- LLM-y to przybliżenia podatne na halucynacje; koszty błędu mogą być realne (utrata wolności, zdrowia, wiarygodności)
- Zasada: "Czy mógłbym zamiast tego użyć czegoś prostszego?" → użyj najprostszego skutecznego podejścia
- Human-in-the-loop jako minimalne zabezpieczenie przy zadaniach wymagających dokładności

**2. Jak ważna jest interpretowalność?**
- Niektóre konteksty (prawny, kontrakt, decyzje o życiu jednostki) wymagają możliwości wyjaśnienia decyzji modelu
- Brak interpretowalności = brak instytucjonalnego zaufania i brak możliwości doskonalenia modelu
- Organizacje misyjne szczególnie powinny umieć tłumaczyć decyzje podejmowane "w imieniu" beneficjentów

**3. Czy to problem, że przyszłość będzie wyglądać jak przeszłość?**
- Modele AI uczą się z danych historycznych — odtwarzają historyczne błędy, uprzedzenia i luki
- Pytania do sprawdzenia: Czy dane reprezentują przyszły kontekst? Czy są kompletne? Czy zawierają wzorce dyskryminacyjne?
- Przykład: trening na rozmowach exit interview pomija głosy najbardziej niezadowolonych pracowników

**4. Czy organizacja jest gotowa wdrożyć AI?**
- Kluczowe zasoby: czyste i scentralizowane dane + ekspertyza domenowa + zdolności techniczne
- Build vs. Buy: oblicz koszt własnego modelu vs. API call do dostawcy
- Wiele NGO lepiej obsłuży swoje potrzeby przez ludzi niż przez zdobycie kompetencji AI

## Wnioski

- Darczyńcy coraz częściej pytają NGO o AI — wdrożenie pod presją zewnętrzną bez wewnętrznej gotowości to przepis na szkodę dla beneficjentów i misji organizacji.
- Framework Essexa jest bezpośrednio użyteczny w pracy Piotra jako konsultanta: daje konkretne pytania do postawienia organizacji przed rekomendacją narzędzia [[LLM]] lub automatyzacji.
- W pracy z danymi wrażliwymi (np. beneficjenci NGO społecznych, grupy wykluczone) interpretowalność modelu i unikanie historycznych uprzedzeń są krytyczne — "garbage in, garbage out" to nie metafora.

## Zastosowanie

Ten framework 4 pytań może służyć jako narzędzie diagnostyczne na warsztatach z [[LGD Kraina Łęgów Odrzańskich]] lub innych NGO, które rozważają wdrożenie AI — zanim przejdzie się do rekomendacji konkretnych narzędzi.
