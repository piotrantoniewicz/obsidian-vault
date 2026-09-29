---
categories:
  - Clippings
authors: ["[[Krzysztof Mirończuk]]"]
url: "https://haimagazine.com/pl/ai_branza/bezpieczenstwo-pl/najlepsza-jest-ai-ktora-niczego-nie-pamieta/"
source: "[[Archives/2026-09-15 Najlepsza jest AI, która niczego nie pamięta-|2026-09-15 Najlepsza jest AI, która niczego nie pamięta-]]"
published: 2026-09-15
created: 2026-09-28
relevance: średnia
tags:
  - "strategia-AI"
  - "LLM"
  - "trendy-AI"
---

# Najlepsza jest AI, która niczego nie pamięta?

[[Krzysztof Mirończuk]] pokazuje, że przy wyborze modelu AI pytanie „który jest najlepszy?" ustępuje pytaniu „któremu modelowi możemy pokazać konkretne dane?". Punktem wyjścia jest wprowadzenie przez [[Anthropic]] kategorii Covered Models z 30-dniową retencją promptów i odpowiedzi (także dla klientów z Zero Data Retention), co według [[Reuters]] skłoniło [[Palantir]], [[Nvidia]] i [[Booz Allen Hamilton]] do ograniczeń w używaniu Claude. Autor rozdziela retencję, trening, dostęp i monitoring bezpieczeństwa oraz pokazuje konflikt dwóch „bezpieczeństw": dostawcy (wykrywanie nadużyć w seriach zapytań) i klienta (kontrola nad własnymi danymi). Wniosek: firmy będą dobierać modele według wrażliwości danych, a nie jednego „firmowego modelu".

## Kluczowe dane
- Covered Models: prompty i odpowiedzi przechowywane 30 dni, potem automatycznie usuwane (chyba że oznaczone ze względów bezpieczeństwa lub prawnych)
- Domyślnie dane z produktów komercyjnych (Claude for Work, API, Claude Gov) nie są używane do trenowania modeli, chyba że klient wyrazi zgodę
- [[OpenAI]] w sierpniu rozszerzyło dostęp do Zero Data Retention dla modeli frontier i zapowiada Private Safety Processing

## Wnioski
- Cztery osobne kwestie — retencja, trening, dostęp, monitoring bezpieczeństwa — warto rozdzielać w każdej rozmowie z organizacją o ryzykach AI; ich mieszanie zaciemnia debatę.
- Dla wrażliwych danych (dane beneficjentów, darczyńców, sygnalistów) sensowny może być podział na kilka modeli według poziomu wrażliwości, a nie jeden model dla wszystkich; agent z dostępem do skrzynki i dokumentów widzi tym więcej, im większą ma samodzielność.
- Lista pytań do dostawcy (gdzie przetwarzane są dane, jak długo, kto ma dostęp, czy zasady można zmienić jednostronnie, czy możliwe własne klucze szyfrujące) to gotowa checklista wyboru narzędzia; [[Microsoft]] Foundry oferuje alternatywę hostowania modeli w środowisku klienta.

## Cytat
> Firmy nie rezygnują więc z AI. Zaczynają natomiast określać, czego AI nie może zobaczyć.

## Zastosowanie
Artykuł nadaje się jako materiał do szkoleń i konsultacji o strategii wdrażania AI w organizacjach społecznych, zwłaszcza tych pracujących z danymi wrażliwymi (beneficjenci, darczyńcy). Cztery pytania o retencję, trening, dostęp i monitoring można wpisać do checklisty wyboru narzędzi AI. Przy okazji pluginów i integracji MCP warto pamiętać, że im szerszy dostęp agenta do systemów klienta, tym ważniejsze zasady przechowywania danych.
