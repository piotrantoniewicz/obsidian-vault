---
categories:
  - "Emails"
published: 2026-05-30
created: 2026-05-30
labels:
  - "Tomasz Woliński"
relevance: wysoka
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "narzędzia-AI"
---

# 49% polskich firm rozczarowanych AI. Wszyscy robią te same 5 rzeczy...

Newsletter Tomka Wolińskiego analizuje wyniki sondażu EY, według którego 49% polskich firm jest rozczarowanych wdrożeniem AI (globalnie: średni ROI 1,7x, jedynie 29% firm raportuje istotny zwrot). Autor identyfikuje 5 powtarzających się błędów wdrożeniowych, które obserwuje u 9 na 10 firm-klientów. Kluczowy wniosek: problem nie leży w technologii, lecz w podejściu do implementacji — brak właściciela procesu, wybór zadań "na intuicję", zła architektura agentów, brak mierzalnych KPI i porzucenie iteracji po pierwszym nieudanym promptcie. Uzupełnieniem jest Quick Win z anty-sycophancy promptem oraz newsy: AI Act przesunięty o 16 miesięcy, [[n8n]] wchodzi do SAP Joule Studio, OpenAI uruchamia spółkę wdrożeniową.

## Frameworki i metody

- **Zakres przed licencją** — najpierw określ: kto, jaki proces, KPI, deadline; wyznacz jedną osobę odpowiedzialną z mandatem na 3 miesiące; bez właściciela procesu AI pozostaje abonamentem, nie narzędziem
- **Tabela ROI procesów** — prosta macierz: proces × częstotliwość × czas pracownika × stawka godzinowa; sortuj malejąco i zacznij od najwyższego, nie od "trendowego"
- **Wzorzec "mózg + ręce"** — [[LLM]] jako mózg (rozumowanie, ocena, generowanie); warstwa narzędzi ([[n8n]], integracje, baza kryteriów) jako ręce (auth, filtrowanie danych, wykonywanie akcji); mózg dostaje tylko przetworzone dane od rąk — eliminuje halucynacje
- **Pomiar before/after** — loguj 2 tygodnie aktualnego czasu pracownika na proces przed wdrożeniem i 2 tygodnie po; różnica × stawka × 12 miesięcy = mierzalny ROI
- **Iteracyjne doskonalenie agentów** — test 10 promptów, mierz wyniki, popraw najsłabszy, retest; agenci to mikro-software, który rozwijasz w czasie, nie jednorazowy zakup
- **Anty-sycophancy prompt (Quick Win)** — zamiast pytać "czy ten plan jest dobry?", pytaj: "Co Cię niepokoi w tej decyzji? Wskaż 3 konkretne ryzyka i 1 najgorszy scenariusz za 3 miesiące"; zmienia tonalność modelu z pochlebnej na krytyczną

## Kluczowe dane

- 49% polskich firm rozczarowanych AI (sondaż EY, maj 2026)
- Globalny średni ROI z AI: 1,7x; tylko 29% firm raportuje istotny zwrot
- 79% organizacji ma trudności z adopcją AI
- AI Act: termin egzekwowania dla systemów high-risk przesunięty z 2 sierpnia 2026 na 2 grudnia 2027 (Digital Omnibus)

## Wnioski

- Bez wyznaczonego właściciela wdrożenia z mandatem [[strategia-AI]] degeneruje się do płaconego abonamentu — każdy pilotaż potrzebuje jednej osoby odpowiedzialnej, nie "całego zespołu"
- Wzorzec "mózg + ręce" jest kluczem do eliminacji halucynacji [[LLM]] — model nie powinien dostać surowych, nieustrukturyzowanych danych; [[n8n]] lub [[Make.com]] jako warstwa "rąk" to praktyczna implementacja
- SAP wbudowuje [[n8n]] w Joule Studio — automatyzacja open-source wchodzi do enterprise klasy Fortune 100; skill [[automatyzacja]] + LLM przestaje być niszową ciekawostką, staje się standardem rynkowym

## Cytat

> "AI w 2026 jest gotowe. Większość wdrożeń — nie."

## Zastosowanie

Te 5 błędów to gotowa struktura warsztatu diagnostycznego lub checklisty przed pilotażem AI dla organizacji — Piotr może ją wykorzystać bezpośrednio w szkoleniach dla NGO i firm. Wzorzec "mózg + ręce" jest bezpośrednio aplikowalny przy budowaniu agentów w [[Make.com]] lub [[Langflow]] dla klientów z sektora społecznego. Anty-sycophancy prompt (`/pre-mortem`) można wdrożyć natychmiast jako stały element szkoleń z [[prompt-engineering]].
