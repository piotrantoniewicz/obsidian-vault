---
categories:
  - Clippings
authors:
  - "[[Allie K Miller]]"
  - "[[Andrea Jones-Rooy]]"
url: "https://www.youtube.com/watch?v=gVMAbiQYMh8"
source: "[[Archives/2026-06-24 How a Former NYU Professor Uses Claude Code|2026-06-24 How a Former NYU Professor Uses Claude Code]]"
published: 2026-06-24
created: 2026-06-26
relevance: wysoka
tags:
  - strategia-AI
  - szkolenia-AI
  - context-engineering
---

# How a Former NYU Professor Uses Claude Code

Rozmowa [[Allie K Miller]] z dr [[Andrea Jones-Rooy]] (była profesorka NYU, data scientist, doradczyni fintechów i rządów) o tym, jak faktycznie używać AI, gdzie hype się rozsypuje i co odróżnia realne użycie od teatru. Główna teza Andrei: bariera wejścia w agentów AI jest psychologiczna, nie techniczna — świat technologii przesadza z żargonem i marketingiem do poziomu zastraszenia, choć on-ramp (np. przez [[Claude Code]] + [[MCP]]) jest łagodniejszy, niż się wydaje. Drugą osią rozmowy jest przejście od AI jako „spinacza biurowego do produktywności" do AI jako współpracownika i samouczącego się systemu — gdzie kluczowe stają się dwie rzeczy: budowanie warstwy kontekstu (context layer) i evale, czyli wiedza o tym, *co* jest dobre. Dla pracy z NGO to mocny, oparty na autorytecie (nie na hype'ie) materiał szkoleniowy i strategiczny.

## Frameworki i metody
- **Pipeline researchowy w [[Claude Code]] + [[MCP]] + Gmail** — agent regularnie wysyła zwykłego maila ze streszczeniem nowości z dziedziny użytkownika; zbudowany „needs-based", nie pod efekt. To ten sam wzorzec, co pluginy `...to-notes` w tym vaultcie.
- **Meta-prompting / agent budujący agentów** — zamiast budować 34 agenty ręcznie, najpierw powstaje „agent builder", który generuje prompty/JD dla pozostałych (analogicznie do `/skill creator`). „Moje życzenie do dżina: więcej życzeń".
- **Warstwa kontekstu (context layer)** — nagrywaj i archiwizuj wszystko (spotkania, transkrypty, tickety, maile), nie kuruj perfekcyjnie, „zalej ocean". Wartość wyciągasz później przez odpytywanie: „jakie 5 skarg klientów wraca?", „jakie 3 błędy powtarzam?". Zachowuj też porażki — z nich się uczysz.
- **AI watchdog / sensor** — agent, który nie wykonuje pracy, tylko *obserwuje* wzorce (np. dwa zespoły robiące to samo) i flaguje je człowiekowi powyżej progu ryzyka. Andrea uogólnia to do „sensorów": AI jako narzędzie do *mierzenia* problemu, zanim zaczniesz go rozwiązywać.
- **Urgency is poison** — im wyższa stawka, tym bardziej trzeba zwolnić: wygeneruj pomysły, oceń je grupowo, dopiero potem działaj. Rekomendacja Scotta Page'a dot. spotkań: pierwsze 10 min wszyscy dyktują pomysły, AI je syntetyzuje, resztę czasu grupa pracuje na zagregowanych ideach.
- **Codzienne voice memo jako osobisty context layer** — nagrywaj 5–40 min refleksji dziennie do notatnika, po miesiącach przepuść przez [[Claude Code]]: „gdzie mam blind spoty? czy realizuję cele? jaki nawyk rzucić?".
- **Evals = „czy liczba jest dobra"** — sama liczba nic nie znaczy bez benchmarku i kontekstu; bez zdefiniowania, co znaczy „dobrze", AI tylko szybciej kopie nieważny dół.

## Kluczowe dane
- 34 agenty AI w „digital workforce" Allie (chief of staff + 6 dyrektorów + zespoły + watchdog)
- 2/3 ze 200-osobowej grupy studentów używało ChatGPT (bez polityki w sylabusie) — prawdopodobnie zaniżone
- 60% zużycia tokenów na Open Router przechodzi przez chińskie modele open-source (Deep Seek, Qwen, MiniMax)
- Akcje Allbirds wzrosły 6x po samej wzmiance o AI — sygnał, że nagłówki „zwolnienia przez AI" trzeba czytać krytycznie

## Wnioski
- Bariera adopcji agentów jest psychologiczna — to samo, co [[Allie K Miller]] pisze o perfekcjonizmie w newsletterze o [[AI workforce]]; dobry argument otwierający szkolenie AI dla [[organizacje społeczne|NGO]].
- Context layer + evale to dwa filary, na których warto budować — pokrywają się 1:1 z filozofią vaultu `Galaxy/` (metoda Karpathy'ego: LLM jako bibliotekarz budujący encyklopedię).
- Token maxing mierzy inputy, nie outputy — to powrót „mentalności fabryki" (premiowanie linijek kodu, godzin przy biurku); realna wartość wymaga „human as a judge" obok „AI as a judge".
- Umiejętności, które przetrwają każdą zmianę narzędzi: ciekawość → krytyczne myślenie → kreatywność → wyobraźnia; jeśli jedno, to ciekawość.

## Cytat
> Nie obchodzi mnie liczba — obchodzi mnie, czy ta liczba jest dobra.

## Zastosowanie
Gotowy materiał na warsztat AI dla NGO oparty na autorytecie (była prof. NYU), nie na hype'ie: tezy „bariera jest psychologiczna", „urgency is poison", „zacznij od problemu i pomiaru", „ciekawość przetrwa". Wątki context layer, AI jako sensor i evale warto przenieść do `Galaxy/` jako osobne strony i podpiąć pod strategię budowania Second Brain (EPARAX) oraz wdrożenia AI w organizacjach.
