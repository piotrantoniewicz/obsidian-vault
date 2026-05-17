---
categories: Clippings
authors: ["[[Sander Schulhoff]]"]
url: https://www.youtube.com/watch?v=J9982NLmTXg
source: "[[Archives/2025-12-21 Why securing AI is harder than anyone expected and guardrails are failing HackAPrompt CEO|2025-12-21 Why securing AI is harder than anyone expected and guardrails are failing HackAPrompt CEO]]"
published: 2025-12-21
created: 2026-05-12
relevance: niska
tags:
  - "strategia-AI"
  - "LLM"
  - "narzędzia-AI"
---

# Why securing AI is harder than anyone expected and guardrails are failing. HackAPrompt CEO.

[[Sander Schulhoff]] — badacz bezpieczeństwa AI i organizator największych konkursów red teamingu — stawia tezę, że guardrails AI po prostu nie działają. Przestrzeń możliwych ataków na modele językowe jest praktycznie nieskończona (10 do potęgi miliona), a więc żaden guardrail nie może statystycznie pokryć jej w sposób znaczący. Jedyne skuteczne zabezpieczenie to klasyczne praktyki cyberbezpieczeństwa: właściwe permissioning akcji i danych, izolacja wykonania kodu oraz zasada minimalnych uprawnień — nie warstwy filtrujące oparte na kolejnych [[LLM]].

## Frameworki i metody

- **Jailbreak vs. prompt injection** — rozróżnienie: jailbreak to atak bezpośrednio na model (użytkownik + model), prompt injection to atak na aplikację zbudowaną na modelu (użytkownik + prompt systemowy + model); oba są nierozwiązywalne przez guardrails
- **CAMEL (Contextual Awareness for Minimizing Exploits with LLMs)** — framework Google: przed wykonaniem zadania agent dostaje tylko minimalne uprawnienia potrzebne do danego żądania; skuteczny tam, gdzie nie zachodzi połączenie read + write; częściowe, ale sensowne technicznie rozwiązanie
- **Zasada: „you can patch a bug, but you can't patch a brain"** — klucz do zrozumienia różnicy między klasycznym cyberbezpieczeństwem a AI security; naprawienie podatności w kodzie jest weryfikowalne, w modelu językowym — nie

## Kluczowe dane

- Ludzie potrafią złamać wszystkie znane guardrails i modele w 10–30 próbach
- Zautomatyzowane systemy ataku potrzebują kilku rzędów wielkości więcej prób i pokrywają ok. 90% przypadków — ludzie wciąż są lepszymi atakującymi
- Przestrzeń ataków na GPT-5 to 10^(1 000 000) możliwych promptów

## Wnioski

- Guardrails i automatyczny red teaming wywołują fałszywe poczucie bezpieczeństwa — lepiej ich nie wdrażać niż wdrożyć i zakładać, że chronią
- Jeśli agent AI może wykonać szkodliwą akcję (wysłać email, zmienić bazę danych), użytkownik może go do tego skłonić — permissioning akcji ważniejszy niż filtrowanie promptów
- Prawdziwe ryzyko pojawi się, gdy agenty AI uzyskają realne możliwości działania w świecie — dopiero wtedy exploity staną się problemem operacyjnym

## Zastosowanie

Przy wdrażaniu chatbotów lub agentów AI w kontekście NGO warto stosować zasadę minimalnych uprawnień: agent odpowiadający na pytania nie powinien mieć dostępu do zapisu danych. Artykuł uzasadnia brak sensu rekomendowania drogich rozwiązań guardrails organizacjom — zamiast tego lepiej skupić się na poprawnym projektowaniu systemu od podstaw.
