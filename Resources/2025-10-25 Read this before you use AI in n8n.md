---
categories:
  - "Emails"
published: 2025-10-25
created: 2026-03-06
labels:
  - Simon Scrapes
relevance: średnia
tags:
  - automatyzacja
  - narzędzia-AI
  - prompt-engineering
---
# Read this before you use AI in n8n

Simon Hollingsworth identyfikuje trzy krytyczne błędy przy integracji AI z [[n8n]], które prowadzą do niestabilnych workflow i nieprzewidywalnych kosztów. Pierwszy to niespecyficzne prompty — vague prompts generują losowe, niespójne wyniki i są głównym powodem awarii automatyzacji opartych na AI. Drugi to brak limitu tokenów w odpowiedziach, co przy intensywnym użyciu prowadzi do eksplodujących rachunków za API. Trzeci, i być może najważniejszy, to używanie agenta AI z pętlą decyzyjną tam, gdzie wystarczyłby prostszy łańcuch [[LLM]] — zbędna złożoność podnosi koszt i obniża niezawodność. Lekcja uczy wybierać właściwe narzędzie dla danego zadania.

## Wnioski
- [[Prompt-engineering]] w automatyzacjach to konieczność, nie opcja — precyzyjne instrukcje są fundamentem niezawodnych workflow AI w [[n8n]], szczególnie przy automatyzacjach obsługujących dane wrażliwe klientów NGO.
- Rozróżnienie agent vs. łańcuch [[LLM]] to kluczowa decyzja architektoniczna: agenci z pętlą decyzyjną tam, gdzie faktycznie potrzebna jest autonomia; proste łańcuchy wszędzie indziej — bezpośrednio wpływa to na koszty i przewidywalność wyników.
- Kontrola kosztów tokenów wymaga aktywnego projektowania: limity odpowiedzi, zwięzłe prompty i właściwy wybór modelu to trzy filary efektywnej automatyzacji AI — istotne przy wdrożeniach dla organizacji z ograniczonym budżetem.

## Cytat
> Większość ludzi traci pieniądze i psuje workflow z tych samych 3 powodów: nieokreślone prompty, nieograniczone odpowiedzi i używanie agenta AI tam, gdzie wystarczyłby łańcuch [[LLM]].

## Zastosowanie
Przy projektowaniu automatyzacji AI dla NGO warto stosować zasadę: najpierw łańcuch [[LLM]] z dobrym promptem, agent tylko gdy logika biznesowa faktycznie wymaga pętli decyzyjnej — to obniża koszty i podnosi niezawodność wdrożenia.
