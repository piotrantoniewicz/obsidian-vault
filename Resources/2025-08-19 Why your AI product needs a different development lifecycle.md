---
categories: Clippings
authors: ["[[Aishwarya Naresh Reganti]]"]
url: https://www.lennysnewsletter.com/p/why-your-ai-product-needs-a-different
source: "[[Archives/2025-08-19 Why your AI product needs a different development lifecycle|2025-08-19 Why your AI product needs a different development lifecycle]]"
published: 2025-08-19
created: 2026-05-11
relevance: średnia
tags:
  - "strategia-AI"
  - "produkty-cyfrowe"
---

# Why your AI product needs a different development lifecycle

[[Aishwarya Naresh Reganti]] i Kiriti Badam, bazując na doświadczeniu z ponad 50 wdrożeń AI w firmach takich jak [[OpenAI]], Google i Amazon, opisują dlaczego tradycyjny cykl wytwarzania oprogramowania nie działa dla produktów AI. Dwie właściwości AI fundamentalnie łamią założenia klasycznego CI/CD: niedeterminizm (zarówno po stronie użytkownika jak i odpowiedzi systemu) oraz konieczność zarządzania kompromisem między autonomią (agency) a kontrolą. W odpowiedzi autorzy proponują framework CC/CD — Continuous Calibration/Continuous Development — gdzie każda wersja produktu zdobywa więcej autonomii stopniowo, a nie od razu.

## Frameworki i metody

**CC/CD — Continuous Calibration/Continuous Development**

Pętla ciągłego doskonalenia produktu AI, złożona z sześciu kroków:

- **CD 1. Scope capability & curate data** — określ zakres wersji przez pryzmat agency/control (nie listy funkcji); zacznij od high control/low agency; zbierz 20–100 przykładów referencyjnych (reference dataset)
- **CD 2. Set up application** — buduj tylko to, co potrzebne na daną wersję; nie overengineeruj; wbuduj mechanizmy control handoff (człowiek może przejąć sterowanie)
- **CD 3. Design evals** — zdefiniuj metryki oceny zanim wdrożysz; evals są specyficzne dla zadania (np. routing accuracy dla klasyfikacji zgłoszeń)
- **Deploy** — wdrożenie jako przejście, nie cel; zacznij od małej grupy użytkowników
- **CC 4. Run evals** — oceń system na danych z produkcji; wybierz reprezentatywną próbkę
- **CC 5. Analyze & spot error patterns** — ręcznie przejrzyj 20–50 błędnych przypadków na kategorię; udokumentuj powtarzające się błędy
- **CC 6. Apply fixes** — naprawiaj architekturę, prompty lub dane na podstawie wzorców błędów; dopiero teraz inżynieruj więcej

**Zasada gradualnego agency:**
v1 (wysoka kontrola) → v2 (sugestie, human review) → v3 (autonomia z fallback)

## Wnioski

- Agenci AI powinni "zasłużyć" na autonomię przez udowodnienie działania pod kontrolą — skoki do pełnej autonomii bez etapu testowania kończą się awariami trudnymi do debugowania
- Evals (metryki oceny) to odpowiednik testów jednostkowych w klasycznym SW — ale muszą być projektowane przez pryzmat zadania, nie ogólne
- Framework CC/CD można adaptować do wdrożeń [[automatyzacja|automatyzacji procesów]] w NGO: zamiast od razu automatyzować całe procesy, zaczynać od asystowania człowiekowi

## Zastosowanie

Przy wdrażaniu automatyzacji w organizacjach pozarządowych warto stosować logikę CC/CD: zaczynać od prostych funkcji z pełną kontrolą człowieka, stopniowo rozszerzać autonomię w miarę budowania zaufania. Framework pomaga też w rozmowach z klientami sceptycznymi wobec AI — pokazuje, że można wdrażać AI ostrożnie i kontrolowanie. Użyteczny przy projektowaniu szkoleń z wdrażania AI dla [[organizacje-społeczne|organizacji społecznych]].
