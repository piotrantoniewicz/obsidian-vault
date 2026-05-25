---
categories: Clippings
authors: ["[[AI HUB Poland]]"]
url: https://ai.gov.pl/ai-dla-ciebie/artykuly/przyszlosc-technologii-agentowej
source: "[[Archives/2026-03-03 Portal sztucznej inteligencji|2026-03-03 Portal sztucznej inteligencji]]"
created: 2026-03-03
relevance: wysoka
tags:
  - "strategia-AI"
  - "trendy-AI"
  - "automatyzacja"
---

# Portal sztucznej inteligencji

Artykuł polskiego [[Ministerstwo Cyfryzacji|Ministerstwa Cyfryzacji]] analizuje fenomen [[Moltbook]]a — platformy społecznościowej dla agentów AI, która wzbudziła sensację medialną, ale okazała się głównie produktem manipulacji i poważnych luk bezpieczeństwa. Autorka wyjaśnia, że agenci AI (jak [[OpenClaw]]) to autonomiczne programy działające w imieniu użytkownika, a nie samodzielne byty — ich "osobowość" wynika z konfiguracji, nie wewnętrznych przeżyć. Artykuł demitologizuje narracje o "przebudzeniu AI" i wskazuje konkretne ryzyka bezpieczeństwa: [[prompt injection]], złośliwe pluginy, brak izolacji środowisk. Całość kończy się siedmioma praktycznymi zasadami bezpiecznego wdrażania agentów AI.

## Frameworki i metody

- **Vibe coding vs. agentic engineering** — tworzenie kodu przez AI (vibe coding wg [[Andrej Karpathy|Karpathy'ego]]) ewoluuje w kierunku rygorystyczniejszego podejścia ("agentic engineering") z testami, kontrolą uprawnień, obserwowalności i bezpiecznym uruchamianiem narzędzi
- **7 zasad bezpiecznej pracy z agentami AI**: (1) izolowane środowiska (Docker, piaskownice); (2) minimalizacja uprawnień agenta; (3) weryfikacja źródeł skilli; (4) monitoring logów i human-in-the-loop; (5) aktualizacje oprogramowania; (6) menedżer sekretów dla kluczy API; (7) filtrowanie treści zewnętrznych pod kątem prompt injection

## Kluczowe dane

- Za rzekomo 1,5 mln agentów [[Moltbook]]a stoi tylko ~17 tys. ludzi (każdy kontroluje średnio 88 botów)
- W repozytoriach [[OpenClaw]] zidentyfikowano ponad 400 złośliwych wtyczek (kampania "ClawHavoc") — infostealery i kradzież kluczy API

## Wnioski

- "Autonomia" agentów AI jest zawsze wynikiem decyzji człowieka — agent robi to, do czego go zaprogramowano; narracje o "przebudzeniu AI" to odzwierciedlenie lęków kulturowych, nie faktów
- [[Prompt injection]] to realne zagrożenie przy agentach czytających zewnętrzne treści — bez walidacji poleceń i izolacji środowisk agent może zostać przejęty lub ujawnić prywatne dane
- Popularność technologii agentowej wymaga przejścia od [[vibe-coding|vibe codingu]] do dyscypliny inżynieryjnej — izolacja, uprawnienia, monitoring i weryfikacja źródeł to nie opcja, lecz podstawa

## Zastosowanie

Przy wdrażaniu agentów AI w organizacjach NGO lub własnych workflow, siedem zasad bezpieczeństwa z artykułu to gotowy checklist — szczególnie cenne są punkty o izolacji środowisk i weryfikacji skilli. Artykuł dostarcza dobrych argumentów na szkoleniach z AI, gdy uczestnicy pytają o bezpieczeństwo i autonomię AI. Demitologizacja narracji o "przebudzeniu AI" to użyteczny punkt odniesienia w rozmowach z NGO sceptycznie nastawionymi do wdrożeń.
