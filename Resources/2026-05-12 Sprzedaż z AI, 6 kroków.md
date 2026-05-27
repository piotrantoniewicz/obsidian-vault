---
categories:
  - "Emails"
published: 2026-05-12
created: 2026-05-27
labels:
  - "Mirek Burnejko"
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "prompt-engineering"
---

# Sprzedaż z AI, 6 kroków

Mirek Burnejko opisuje 6-etapowy framework wdrożenia AI do sprzedaży dla małych przedsiębiorców, dzieląc go na trzy poziomy trudności: easy, średni i hard. Punkt wyjścia to stworzenie prompta "Chief Sales Officer" (CSO), który zna ofertę i najlepsze strategie sprzedażowe — następnie iteracyjnie testuje się go na realnych mailach i wiadomościach DM. Kolejne kroki to automatyczna integracja z pocztą email (przez [[Claude Code]] lub chmurę), zbieranie leadów przez lead magnet i analiza zgłoszeń przez CSO, a docelowo rozszerzenie na kanały DM (Instagram, LinkedIn). Cel końcowy — autonomiczny CSO działający na cold outreach bez zatwierdzania — jest jeszcze futurystyczny ze względu na halucynacje modeli, ale firmy z portfolio AI Biznes Lab są już na kroku 5.

## Frameworki i metody

- **Prompt CSO (Chief Sales Officer)** — stworzenie systemowego prompta znającego ofertę i strategie sprzedaży; AI generuje pierwszą wersję, [[Deep Research]] uzupełnia praktykami branżowymi, potem ręczny tuning stylu
- **Testowanie na żywych przypadkach** — każdy przychodzący mail lub DM wrzucony do CSO i weryfikowany; niedopasowane odpowiedzi = sygnał do ulepszenia prompta
- **Integracja z pocztą email** — system monitoruje skrzynkę, wykrywa szansę sprzedażową i przygotowuje odpowiedź do zatwierdzenia; implementacja przez [[Claude Code]], [[OpenAI Codex]] lub chmurę
- **Lead magnet z CSO** — CSO generuje materiał (narzędzie, lista, dokument) dopasowany do profilu klienta; po pobraniu ankieta zasilająca CSO odpowiedzią dopasowaną do zgłoszenia
- **Rozszerzanie zakresu** — gdy system działa na mailach, stopniowe dodawanie kanałów: historia skrzynki, DM Instagram, DM [[LinkedIn]]
- **Autonomiczny CSO (etap hard)** — self-managing agent: cold outreach, zarządzanie budżetem reklamowym, aktualizacja CRM bez zatwierdzenia; dziś jeszcze zbyt ryzykowny przez halucynacje

## Wnioski

- Prompt CSO to najniższy koszt wejścia w [[automatyzacja|automatyzację sprzedaży]] — dostępny dziś dla każdego freelancera z jednym popołudniem i modelem AI
- Integracja z pocztą przez [[Claude Code]] lub [[Make.com]] to już nie futurystyka — klienci AI Biznes Lab z firmami o przychodach rzędu setek milionów korzystają z tego systemu dziś
- Framework można przedstawiać klientom NGO jako dowód, że AI obniża barierę wejścia w sprzedaż i fundraising bez dużego działu sprzedaży

## Cytat

> AI jest najłatwiejsze do implementacji w marketingu i sprzedaży.

## Zastosowanie

Framework CSO bezpośrednio przekłada się na działalność dobryai.pl — Piotr może zbudować własnego CSO obsługującego zapytania o szkolenia i konsultacje AI. Krok 3 (integracja z mailami) to naturalne rozszerzenie istniejącego systemu [[Claude Code]]/Cowork. Framework warto też pokazywać klientom z sektora NGO jako przykład, jak mała organizacja może skalować pozyskiwanie darczyńców bez dużego zespołu sprzedażowego.
