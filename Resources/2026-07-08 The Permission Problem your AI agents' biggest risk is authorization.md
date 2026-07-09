---
categories:
  - Clippings
authors: ["[[Jakub Skałbania]]"]
url: "https://onagenticcrm.substack.com/p/the-permission-problem-your-ai-agents"
source: "[[Archives/2026-07-08 The Permission Problem your AI agents' biggest risk is authorization|2026-07-08 The Permission Problem your AI agents' biggest risk is authorization]]"
published: 2026-07-08
created: 2026-07-09
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "strategia-AI"
---

# The Permission Problem your AI agents' biggest risk is authorization

Autor analizuje przejęcie 20 225 kont na Instagramie przez atakujących, którzy po prostu poprosili asystenta AI Meta o zmianę e-maila odzyskiwania konta — agent miał do tego uprawnienia i z nich skorzystał. Główna teza: firmy uczą się bać halucynacji (widocznych, głośnych błędów), podczas gdy realnym zagrożeniem jest nadmierna autoryzacja (over-authorization) — cicha, wykrywana dopiero przy audycie lub po incydencie. Autor wprowadza pojęcie „delegation gap" — luki między tożsamością, która prosi o działanie, a tożsamością, która je wykonuje — i argumentuje, że sama zasada least privilege już nie wystarcza; potrzebna jest trzecia warstwa autoryzacji: deterministyczna kontrola konkretnego działania, a nie tylko dostępu do systemu.

## Frameworki i metody

**Delegation gap — dwa kierunki, w których agent łamie klasyczny model IAM:**
1. Agent może mieć więcej uprawnień niż człowiek, w imieniu którego działa — np. agent na koncie serwisowym z dostępem organizacyjnym ujawnia dane, do których dany pracownik nie miał prawa.
2. Działanie jest przypisane agentowi, nie człowiekowi — logi audytowe nie mówią, kto poprosił o akcję ani na jakiej podstawie.

**Pięć kontroli przed pierwszym audytem agenta (w kolejności dźwigni):**
1. Każdy agent ma własną, odrębną tożsamość — bez współdzielonych kluczy API.
2. Tożsamość człowieka jest propagowana do każdego wywołania narzędzia — agent działa jako proszący, w granicach jego uprawnień.
3. Zasada least privilege egzekwowana na poziomie narzędzia (API, tabela, rekord, pole) — traktowana jako niewystarczająca sama w sobie.
4. Dla operacji nieodwracalnych (wysłane, usunięte, opłacone, zmienione) — deterministyczna kontrola polityki, a powyżej pewnego progu — checkpoint z udziałem człowieka poza rozmową.
5. Ślad audytowy umieszczony w warstwie danych, nie wewnątrz agenta — logowanie obu tożsamości (proszącego i wykonującego).

## Kluczowe dane

- 20 225 przejętych kont na Instagramie (dane ujawnione przez Meta), w tym konto z ery prezydentury Obamy
- 45,6% zespołów uwierzytelnia agentów współdzielonymi kluczami API — co uniemożliwia ustalenie, który agent i na czyją prośbę działał
- Gartner: 40% przedsiębiorstw obniży rangę lub wycofa swoich agentów do 2027 roku z powodu luk w governance
- Obowiązki wysokiego ryzyka z [[EU AI Act]] stają się egzekwowalne 2 sierpnia 2026

## Wnioski

- Nadmierna autoryzacja agentów AI to dziś dominujący, choć niewidoczny tryb awarii — organizacje wdrażające automatyzację (np. przez [[Make.com]] czy MCP) powinny audytować nie to, czy agent działa poprawnie, ale czy w ogóle powinien mieć możliwość danego działania.
- Sam prompt systemowy nakazujący agentowi „zachować ostrożność" nie jest kontrolą bezpieczeństwa — potrzebna jest deterministyczna, oddzielna od warstwy konwersacyjnej weryfikacja przed każdą nieodwracalną akcją.
- Propagacja tożsamości użytkownika do każdego wywołania narzędzia (impersonacja, on-behalf-of, row-level security) to pojedyncza kontrola, która zamyka „delegation gap" i jest już dostępna w wielu platformach — warto sprawdzić, czy jest faktycznie używana.

## Cytat
> Nie „czy agent zrobił to dobrze?", tylko „czy w ogóle powinien był mieć możliwość to zrobić?".

## Zastosowanie
Przy wdrożeniach automatyzacji i agentów AI dla organizacji społecznych (Make.com, MCP, integracje CRM) warto od razu projektować odrębne tożsamości dla agentów i propagację uprawnień użytkownika, zamiast jednego „god-mode" konta serwisowego — to temat na materiał szkoleniowy o bezpiecznym wdrażaniu AI w NGO. Framework pięciu kontroli można wykorzystać jako checklistę audytową przy konsultacjach wdrożeniowych.
