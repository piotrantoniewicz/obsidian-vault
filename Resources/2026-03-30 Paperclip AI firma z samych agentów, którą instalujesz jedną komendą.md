---
categories: Clippings
authors: ["[[Mateusz Wojdalski]]"]
url: https://devstockacademy.pl/blog/aktualnosci-i-wydarzenia/paperclip-ai-zero-human-company/?utm_source=newsletter&utm_medium=email&utm_term=2026-04-12&utm_campaign=Firma%20bez%20pracownik%C3%B3w%20Dos%C5%82ownie%20
source: "[[Archives/2026-03-30 Paperclip AI firma z samych agentów, którą instalujesz jedną komendą|2026-03-30 Paperclip AI firma z samych agentów, którą instalujesz jedną komendą]]"
published: 2026-03-30
created: 2026-04-12
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "strategia-AI"
---

# Paperclip AI — firma z samych agentów, którą instalujesz jedną komendą

Paperclip AI to open-source platforma do orkiestracji agentów AI zorganizowanych jak prawdziwa firma — z hierarchią ról, budżetami tokenów, audit logiem i bramami akceptacyjnymi. Projekt zebrał 40 000 gwiazdek GitHub w trzy tygodnie, co jest silnym sygnałem rynkowym: tysiące zespołów miały ten sam problem z zarządzaniem wieloma równoległymi sesjami agentów. Towarzyszący ekosystem companies.sh pozwala instalować gotowe konfiguracje „firm agentów" jedną komendą npm — jak pakiet z kompletną strukturą organizacyjną i zestawem ról. Platforma integruje się z [[Claude Code]], Codex, Cursor oraz dowolnym endpointem HTTP, co oznacza że istniejące agenty można podpiąć bez przepisywania.

## Frameworki i metody

- **Org chart jako schemat agentów** — każdy agent ma przypisaną rolę (CEO, CTO, QA, Developer), zakres odpowiedzialności i miesięczny budżet tokenów; nadrzędne agenty mogą wywoływać podrzędne jak przełożony deleguje zadanie
- **Budżety tokenów jako kontrola kosztów** — gdy agent zbliża się do limitu, platforma wymaga zatwierdzenia przed kontynuacją; analogia do pracownika przekraczającego budżet projektu
- **Audit trail + rollback + bramy akceptacyjne** — wszystkie działania logowane, zmiany konfiguracji możliwe do cofnięcia, krytyczne operacje wymagają zatwierdzenia przez człowieka lub agenta nadrzędnego
- **companies.sh** — katalog gotowych konfiguracji firm agentów instalowanych komendą `npx companies.sh add paperclipai/companies/[nazwa]`; dostępne: studio gamingowe, firma audytu bezpieczeństwa, full-stack software house

## Kluczowe dane

- 40 000 gwiazdek GitHub w 3 tygodnie od premiery
- 16 gotowych konfiguracji firm, 440 wyspecjalizowanych agentów, 500 skili w katalogu companies.sh
- Licencja MIT, self-hosted — brak kosztów platformy, tylko koszty tokenów API

## Wnioski

- Orkiestracja wielu agentów staje się kluczową kompetencją — [[Paperclip AI]] daje do tego strukturę i governance, której brakowało przy intensywnym używaniu [[Claude Code]]
- Model „firma jako kod" otwiera nowy sposób skalowania pracy: zamiast zatrudniać, konfigurujesz strukturę organizacyjną agentów z budżetami i nadzorem
- Integracja z dowolnym endpointem HTTP oznacza kompatybilność z [[Make.com]] i istniejącymi workflow automatyzacji

## Cytat

> „Jeśli [[Claude Code]] to pracownik, [[Paperclip AI]] to firma."

## Zastosowanie

Dla Piotra, który prowadzi wiele równoległych sesji [[Claude Code]] i buduje pluginy AI, Paperclip to naturalna warstwa zarządzania agentami przy projektach dla klientów NGO. Gotowe konfiguracje z companies.sh mogą posłużyć jako punkt startowy dla demonstracji i szkoleń z AI. Warto śledzić planowany marketplace Clipmart jako potencjalny kanał dystrybucji własnych konfiguracji agentów.
