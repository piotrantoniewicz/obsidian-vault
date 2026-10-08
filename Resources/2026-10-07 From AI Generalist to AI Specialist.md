---
categories:
  - Clippings
authors: ["[[Bryan Neider]]"]
url: "https://www.linkedin.com/pulse/from-ai-generalist-specialist-bryan-neider-arxbc/"
source: "[[Archives/2026-10-07 From AI Generalist to AI Specialist|2026-10-07 From AI Generalist to AI Specialist]]"
published: 2026-10-07
created: 2026-10-07
relevance: wysoka
tags:
  - "strategia-AI"
  - "organizacje-społeczne"
  - "context-engineering"
---

# From AI Generalist to AI Specialist

[[Bryan Neider]] z organizacji AbilityPath przekłada na język sektora społecznego wnioski z warsztatu [[AWS]] o budowie domenowych agentów AI. Główna teza: model ogólnego przeznaczenia jest płynny i szeroki, ale nie jest niezawodny w konkretnej dziedzinie (przepisy, polityki, reguły finansowania) — błędy bywają wiarygodne, a przez to trudne do wychwycenia. Specjalizacji nie da się „włączyć przełącznikiem”; trzeba ją zaprojektować świadomie: instrukcje, wiedza, narzędzia, zabezpieczenia, z góry ustalony poziom wiarygodności i obowiązkowe przekazanie sprawy człowiekowi. Dla NGO to ważne, bo pracują na zaufaniu i często na wrażliwych danych, a szybkość wdrożeń zapewnia dobre zarządzanie, nie duży budżet.

## Frameworki i metody

**4 dźwignie dostosowania AI do domeny (bez wiedzy technicznej):**

1. **Instrukcje** — „opis stanowiska” dla AI: kim jest, za co odpowiada, jak działa i czego mu nie wolno. AbilityPath przygotowuje AI Prompt Playbook dla pracowników.
2. **Wiedza** — z czego AI wolno korzystać: aktualne, kompletne dane programowe i polityki organizacji, a nie ogólne wyobrażenie o tym, „jak to się robi”. AbilityPath ujednolicił dane z różnych programów.
3. **Narzędzia** — co AI może robić: dostęp tylko do systemów potrzebnych w zadaniu; pytanie kontrolne: co to narzędzie widzi i co może zmienić?
4. **Zabezpieczenia (guardrails)** — czego nie wolno: AI potrafi obejść instrukcje, więc przy bezpieczeństwie, prywatności i odpowiedzialności prawnej regułę musi egzekwować sam system (np. umowy powierzenia, protokoły bezpieczeństwa, zgodność z HIPAA).

**Docelowy poziom wiarygodności ustalany przed budową:**
- narzędzia wewnętrzne, w których człowiek poprawia błędy: 80–85%
- treści widoczne publicznie: 90–95%
- informacje medyczne, prawne i finansowe: 99%, z człowiekiem kontrolującym sprawy zdrowia i bezpieczeństwa

**Dobre praktyki wdrożeniowe:**
- Przekazanie sprawy człowiekowi (handoff) z pełnym kontekstem, zanim chatbot dla klientów trafi na produkcję — bez konieczności powtarzania historii.
- Testy na prawdziwych pytaniach i przypadkach brzegowych, które piszą pracownicy pierwszej linii, przed publicznym startem.
- Właściwe narzędzie do właściwego zadania (np. optymalizacja tras w dedykowanym oprogramowaniu, nie w [[LLM]]) oraz prawdziwa wielojęzyczność (baza wiedzy i odpowiedzi w języku użytkownika, nie tylko przetłumaczone powitanie).
- Fundament zarządczy: Board AI Governance Charter, grupa robocza ds. nadzoru, program budowania AI literacy personelu.

## Wnioski
- Dla NGO wiarygodność domenowa jest ważniejsza niż ogólna „inteligencja” modelu — wdrożenie AI to projektowanie [[context engineering]] (instrukcje + wiedza + narzędzia), nie wybór „najlepszego” narzędzia.
- Poziom dopuszczalnego błędu powinien zależeć od stawki: notatki ze spotkań mogą być niedoskonałe, komunikacja z darczyńcami i beneficjentami — nie; to użyteczna reguła do polityk AI w organizacjach.
- Szybkość wdrożeń bierze się z governance: jasne zasady, ograniczony dostęp, uporządkowana wiedza i ludzie najbliżsi misji w centrum procesu.

## Cytat
> Różnica między ogólną zdolnością a niezawodnością w danej dziedzinie.

## Zastosowanie
Cztery dźwignie i progi wiarygodności (80–85% / 90–95% / 99%) mogą stać się gotowym szkieletem do audytu gotowości AI i polityki AI w projektach dla NGO oraz slajdem w szkoleniach. Lista „instrukcje–wiedza–narzędzia–zabezpieczenia” dobrze pasuje też jako checklista przy budowie chatbotów, np. przy [[Asystent Wniosków Grantowych]].
