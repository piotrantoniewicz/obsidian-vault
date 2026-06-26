---
categories:
  - "Emails"
published: 2026-06-26
created: 2026-06-26
labels:
  - "The Batch"
relevance: wysoka
tags:
  - "automatyzacja"
  - "vibe-coding"
  - "strategia-AI"
---

# A New Generation Studies AI, Apple's Recipe for On-Device Models, GLM5.2 Tackles Open-Ended Problems

Andrew Ng opisuje koncepcję „loop engineering" — podejścia do budowania produktów z AI, które organizuje pracę wokół trzech zagnieżdżonych pętli informacji zwrotnej. Buzzphrase spopularyzowali Boris Cherney (twórca [[Claude Code]]) i Peter Steinberger (twórca OpenClaw), wskazując pętle jako kluczowy mechanizm pozwalający agentom AI pracować produktywnie przez dłuższy czas bez interwencji człowieka. Ng traktuje te pętle nie tylko jako sposób pisania kodu, ale jako narzędzie do decydowania, co w ogóle budować.

## Frameworki i metody

- **Agentic coding loop (pętla kodowania agentycznego)** — agent AI pisze kod, testuje go i iteruje samodzielnie, aż kod jest wolny od błędów i spełnia specyfikację. Pętla działa szybko: nowa wersja oprogramowania co kilka minut. Agent może samodzielnie korzystać z przeglądarki, żeby sprawdzić rezultaty, bez potrzeby angażowania dewelopera.
- **Developer feedback loop (pętla dewelopera)** — deweloper przegląda gotowy produkt i kierunkuje agenta na poprawki. Działa w interwałach od kilkudziesięciu minut do kilku godzin. Rola dewelopera przesuwa się z QA (ręczne szukanie błędów) ku decyzjom produktowym wyższego rzędu: kluczowe funkcje, UX, flow użytkownika. Człowiek wnosi „context advantage" — zna użytkowników i kontekst lepiej niż AI.
- **External feedback loop (pętla zewnętrzna)** — feedback od znajomych, testerów alfa, testy A/B w produkcji. Najwolniejsza pętla (godziny do tygodni), ale zasila wizję dewelopera i specyfikację dla agenta.

## Wnioski

- Szybsze kodowanie agentyczne sprawia, że inżynierowie wchodzą częściowo w rolę product managerów — najtrudniejszym elementem jest kształtowanie wizji produktu i balans między budowaniem a zbieraniem feedbacku od użytkowników.
- Człowiek pozostaje niezbędny w pętli tak długo, jak dysponuje wiedzą kontekstową, której AI nie posiada — Ng nazywa to „context advantage" zamiast „taste", bo to daje klarowniejszą ścieżkę doskonalenia systemów AI.
- Pisanie specyfikacji dla agenta to nadal duży wysiłek; gdy system napotyka powtarzające się problemy, warto zbudować zestaw evals (dataset do mierzenia jakości), który pozwoli agentowi automatycznie weryfikować postęp.

## Cytat

> „So long as the human knows something the AI does not, human-in-the-loop is needed to inject that knowledge into the system."

## Zastosowanie

Dla Piotra pracującego z NGO nad wdrożeniami AI — koncepcja trzech pętli daje praktyczny framework do tłumaczenia vibe-codingu organizacjom: zamiast mówić „AI pisze kod", można pokazać strukturę pętli i wyjaśnić, gdzie człowiek pozostaje decydujący. Pętla zewnętrzna (feedback od darczyńców, testerów kampanii) bezpośrednio przekłada się na digital campaigning. Podejście do loop engineering można też zaadaptować do automatyzacji procesów NGO w [[Make.com]] — zamknięcie pętli testowania to kluczowy krok każdej automatyzacji.
