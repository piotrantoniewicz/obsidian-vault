---
categories: Clippings
authors: ["[[Andrew Ng]]"]
url: https://www.deeplearning.ai/the-batch/why-we-need-more-compute-for-inference/
published: 2024-04-24
created: 2026-04-24
relevance: średnia
tags:
  - "trendy-AI"
  - "LLM"
  - "strategia-AI"
source: "[[Archives/2024-04-24 Why We Need More Compute for Inference|2024-04-24 Why We Need More Compute for Inference]]"
---

# Why We Need More Compute for Inference

[[Andrew Ng]] argumentuje, że dyskusja o potrzebie większego compute skupia się na trenowaniu modeli, podczas gdy równie pilny — i niedoceniany — problem dotyczy inferencji. W klasycznym użyciu [[LLM]] generuje tokeny z prędkością wystarczającą dla człowieka (ok. 6 tokenów/s), ale w przepływach agentycznych modele generują setki tysięcy tokenów zanim cokolwiek zobaczy użytkownik — co czyni szybkość inferencji kluczowym wąskim gardłem. Ng prognozuje, że zarówno koszty trenowania, jak i inferencji będą dalej spadać gwałtownie (wg ARK Invest koszty inferencji enterprise maleją o ~86% rocznie), co odblokuje nową falę zastosowań agentycznych. To zmiana fundamentalna dla wszystkich, którzy budują produkty i automatyzacje oparte na modelach językowych.

## Kluczowe dane

- Człowiek czyta ~250 słów/min, co odpowiada ~6 tokenom/sekundę — próg wystarczający dla klasycznego chatbota, ale niewystarczający dla agentów
- ARK Invest szacuje spadek kosztów trenowania AI o 75% rocznie
- Koszty inferencji enterprise spadają wg ARK Invest o ~86% rocznie

## Wnioski

- Szybkość i koszt inferencji to obecnie bardziej praktyczne ograniczenie dla zastosowań agentycznych niż samo trenowanie modeli — ma to bezpośrednie przełożenie na wybór dostawcy API przy budowaniu automatyzacji
- Wraz ze spadkiem kosztów inferencji uruchamianie złożonych, wielokrokowych agentów (np. w [[Make.com]] lub [[Langflow]]) staje się ekonomicznie coraz bardziej uzasadnione
- Tańsza inferencja obniży też koszty ewaluacji modeli — co ułatwi iterowanie i doskonalenie promptów w projektach opartych na [[LLM]]

## Zastosowanie

Artykuł dostarcza solidnego uzasadnienia dla klientów NGO sceptycznych wobec kosztów wdrożeń AI — warto przytoczyć dane o tempie spadku kosztów, żeby pokazać horyzont opłacalności. Dla własnych projektów automatyzacji warto monitorować ofertę szybkich dostawców inferencji jak [[Groq]], bo szybkie generowanie tokenów bezpośrednio wpływa na użyteczność agentycznych workflows. Wiedza o tym, jak działają przepływy agentyczne na poziomie compute, może też pomóc w projektowaniu szkoleń pokazujących realne możliwości i ograniczenia narzędzi AI.
