---
categories:
  - "Emails"
published: 2026-06-17
created: 2026-06-23
labels:
  - "AI with ALLIE"
relevance: wysoka
tags:
  - "automatyzacja"
  - "strategia-AI"
  - "narzędzia-AI"
---

# How I built my AI agent workforce

Allie Miller opisuje, jak zbudowała zespół 34 agentów AI zarządzający jej biznesem — z szefem sztabu Simonem, sześcioma dyrektorami nazwanymi po postaciach z Przyjaciół i asystentem Tobym, którego jedynym zadaniem jest robienie notatek i budowanie pamięci systemu. Każdy agent to plik tekstowy (markdown) z opisem roli, celów, narzędzi i zasad działania. Kluczową tezą jest przejście od roli „pojedynczego operatora" do roli CEO systemu, który sam się uczy i iteruje. Newsletter dokumentuje ewolucję pracy z AI: od ręcznego promptowania w 2023 r. do w pełni autonomicznych, wieloagentowych przepływów pracy w 2026 r.

## Frameworki i metody

- **Hierarchia agentów** — Chief of Staff (Simon) deleguje do dyrektorów funkcyjnych (marketing, produkt, edukacja, operacje, klienci, kreatywność), każdy zarządza własnym benchem specjalistów; Toby jako agent pamięci i uczenia się systemu
- **Job Description jako system prompt** — zamiast promptowania każdego zadania: pisz opisy stanowisk z celami, kryteriami sukcesu, kryteriami porażki i zasadami eskalacji; agent otrzymuje cel, sam rozumuje przez „jak"
- **Pętla samonauki** — Simon → delegacja do dyrektorów → realizacja → aktualizacja pamięci → Toby przegląda system → zatwierdzenie przez Allie → aktualizacja systemu; organizacja doskonali się bez ręcznej interwencji
- **Progresja od czatu do zarządzania** — 2022: ręczne działanie; 2023: pojedyncze promptowanie; 2024: powtarzalność przez GPT; 2025: agenci inicjują pracę; 2026: wieloagentowy system samouczący się
- **Pierwsze zatrudnienie AI** — wybierz jedną funkcję (nie zadanie!), którą ciągle powtarzasz → nazwij agenta → napisz JD z celami i kryteriami → onboarding przez tydzień, strojenie przez miesiąc

## Wnioski

- Największy odblokowanie Allie to Toby — agent zajmujący się wyłącznie notatkami i pamięcią systemu; rola nieistniejąca w ludzkim zespole, ale kluczowa dla ciągłego doskonalenia — analogia do budowania [[Second Brain]] na poziomie organizacji
- Barierą wejścia w pracę wieloagentową nie są umiejętności techniczne, lecz psychologiczne — konieczność porzucenia perfekcjonizmu i nawyku robienia wszystkiego samodzielnie; nową kompetencją jest delegacja przez systemy, nie promptowanie
- Efekt procentu składanego: agenci pracujący nawet z 30% skuteczności człowieka, przez całą dobę, generują równowartość dodatkowego 1,26 pracownika tygodniowo — przewaga kompetencyjna w kolejnych latach rośnie wykładniczo

## Cytat

> „Nie jestem już pojedynczym operatorem. Jestem CEO systemu."

## Zastosowanie

Schemat hierarchii agentów (Chief of Staff → dyrektorzy → specjaliści + agent pamięci) można bezpośrednio zaadaptować w pracy konsultanta: Simon jako koordynator projektów NGO, Toby jako agent budujący bazę wiedzy o klientach i skutecznych interwencjach. Podejście JD-first (cel + kryteria sukcesu/porażki) to gotowy szablon do onboardingu własnych agentów w [[Claude AI|Claude]] i [[Make.com]]. Dla kursów szkoleniowych (dobryai.pl) — ewolucja 2022–2026 to gotowa oś narracyjna pokazująca, gdzie uczestnik jest dziś i dokąd zmierza.
