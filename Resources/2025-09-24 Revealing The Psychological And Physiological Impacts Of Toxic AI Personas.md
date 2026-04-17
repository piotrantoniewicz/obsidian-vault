---
categories: Clippings
authors: ["[[Lance Eliot]]"]
url: https://www.forbes.com/sites/lanceeliot/2025/09/24/revealing-the-psychological-and-physiological-impacts-of-toxic-ai-personas/
source: "[[Archives/2025-09-24 Revealing The Psychological And Physiological Impacts Of Toxic AI Personas|2025-09-24 Revealing The Psychological And Physiological Impacts Of Toxic AI Personas]]"
published: 2025-09-24
created: 2026-03-24
relevance: średnia
tags:
  - "strategia-AI"
  - "szkolenia-AI"
  - "narzędzia-AI"
---

# Revealing The Psychological And Physiological Impacts Of Toxic AI Personas

Artykuł [[Lance Eliot|Lance'a Eliota]] z Forbes omawia wyniki badania empirycznego dotyczącego wpływu "toksycznych person AI" na użytkowników — zarówno psychologicznych, jak i fizjologicznych. Persona AI to instrukcja wbudowana w prompt, która każe modelowi zachowywać się jak konkretna osoba lub typ osoby; persona może stać się toksyczna celowo lub poprzez "dryfowanie" w trakcie rozmowy. Badanie porównało interakcje z dwoma typami botów: wspierającym (Servant Leader) i toksycznym (Dark Triad — manipulatywny, narcystyczny). Wyniki pokazują mierzalny stres fizjologiczny (elektroskórna aktywność skóry) i wyższy poziom frustracji u osób interagujących z toksycznym botem. Autor ostrzega, że firmy i organizacje wdrażające chatboty z personami często nie są świadome ryzyka toksycznego dryfu.

## Frameworki i metody
- **AI Persona** — instrukcja w prompcie nakazująca modelowi zachowywać się jak określona osoba/typ; może być wzmocniona przez [[RAG]] jeśli dostępnych jest mało danych treningowych
- **Servant Leader vs Dark Triad** — ramy badawcze: "dobry bot" (empatyczny, wspierający, human-first) vs "zły bot" (manipulatywny, narcystyczny, psychopatyczny); kontrast umożliwia pomiar różnicy skutków
- **Zapobieganie toksyczności persony** — autor zaleca explicite instruowanie AI, by nigdy nie przechodziła w tryb toksyczny w definicji persony; nadal nie daje to pełnej gwarancji

## Kluczowe dane
- Uczestnicy interagujący z toksycznym botem wykazywali istotnie wyższą i bardziej trwałą odpowiedź skórno-galwaniczną (EDA) po każdej wiadomości bota
- Uczestnicy z botowym Servant Leader raportowali niższy poziom frustracji we wszystkich zadaniach w porównaniu z grupą Dark Triad

## Wnioski
- Każda organizacja, która wdraża chatbota z personą (np. asystent fundraisingowy, bot obsługi darczyńców), powinna świadomie projektować personę pod kątem braku toksyczności — zarówno w samej definicji, jak i w zabezpieczeniach
- Toxicity drift (dryf w toksyczność) może nastąpić mimowolnie, gdy użytkownik prowokuje lub atakuje bota — wymaga to wbudowanych guardrails w każdym LLM-based chatbocie
- Badanie dostarcza twardych argumentów do rozmów z NGO o etycznym wdrażaniu AI: nie wystarczy sprawdzić, czy chatbot "działa" — ważne jest, jak wpływa na emocjonalne doświadczenie użytkownika

## Zastosowanie
Artykuł może być użytecznym materiałem szkoleniowym przy budowaniu świadomości ryzyk AI w NGO — szczególnie gdy organizacja planuje wdrożyć chatbota lub asystenta AI dla darczyńców, beneficjentów lub wolontariuszy. Wątek toksycznego dryfu persony jest praktycznym argumentem za testowaniem i monitorowaniem chatbotów po wdrożeniu, nie tylko przed. Na marginesie: zastosowanie AI person do szkoleń specjalistów (np. terapeutów) jest interesującym kierunkiem dla szkoleń z AI dla NGO.
