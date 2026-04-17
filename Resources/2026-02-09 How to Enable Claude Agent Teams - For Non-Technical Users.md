---
categories:
  - "Emails"
published: 2026-02-09
created: 2026-03-06
labels:
  - AI with ALLIE
relevance: niska
tags:
  - automatyzacja
  - narzędzia-AI
  - strategia-AI
---

# How to Enable Claude Agent Teams: For Non-Technical Users

Praktyczny przewodnik po trzech podejściach do agentów AI w Claude Code: (1) sub-agenty w równoległym silosie, (2) Agent Teams — nowa funkcja Anthropic umożliwiająca współpracę agentów z współdzielonym kontekstem, (3) wiele terminali z manualnym nadzorem. Artykuł wyjaśnia architekturę Agent Teams przez analogię do planowania rodzinnego wyjazdu (Team Lead = planner parent, agenty = rodzice z zadaniami), zawiera instrukcję krok po kroku jak włączyć funkcję w terminalu oraz wskazówki takie jak planning mode, bezpośredni DM do konkretnego agenta i kolorowanie terminali.

## Wnioski
- Agent Teams to shift od "microtasking chat" do "real task completion" — agenty wykonują realne zadania w cyfrowym świecie (bookowanie, raportowanie, przetwarzanie PR), a nie tylko odpowiadają na pytania; to fundamentalna zmiana dla każdej organizacji rozważającej wdrożenie [[automatyzacja]].
- Prompt "stress-test strategii przez 4 role (CFO, analityk konkurencji, zły exec, operations lead)" to użyteczny wzorzec do recenzji strategii NGO — można zastosować do analizy planów fundraisingowych lub kampanijnych bez znajomości terminala.
- Agent Teams jest eksperymentalny i kosztowny (każdy agent = osobna sesja Claude, może kosztować setki dolarów dziennie) — realny dla zaawansowanych użytkowników, nie do masowego wdrożenia w NGO bez budżetu na API.

## Cytat
> "We are no longer in a microtasking chat world. Single chat threads are dead."

## Zastosowanie
Wzorzec "stress-test strategii przez wyspecjalizowane role agentów" można zaimplementować jako ćwiczenie warsztatowe dla NGO bez terminala — ręcznie, przez cztery osobne konwersacje z Claude z różnymi persona w prompt.
