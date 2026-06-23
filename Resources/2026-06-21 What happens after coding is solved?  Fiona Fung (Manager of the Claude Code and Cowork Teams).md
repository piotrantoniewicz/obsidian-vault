---
categories:
  - Clippings
authors: ["[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/building-the-most-ai-pilled-engineering?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
source: "[[Archives/2026-06-21 What happens after coding is solved?  Fiona Fung (Manager of the Claude Code and Cowork Teams)|2026-06-21 What happens after coding is solved?  Fiona Fung (Manager of the Claude Code and Cowork Teams)]]"
published: 2026-06-21
created: 2026-06-23
relevance: średnia
tags:
  - "automatyzacja"
  - "strategia-AI"
  - "narzędzia-AI"
---

# What happens after coding is solved? | Fiona Fung (Manager of the Claude Code and Cowork Teams)

[[Fiona Fung]], menedżerka zespołów [[Claude Code]] i [[Cowork]] w [[Anthropic]], dzieli się obserwacjami z prowadzenia najbardziej „AI-pilled" zespołu inżynierskiego na świecie — zespołu, który od 2025 roku dostarcza 8× więcej kodu kwartalnie niż przed erą AI. Najważniejszy wniosek: problem w pracy z AI przesunął się z "jak to zbudować?" na "jak zweryfikować, że to działa zgodnie z intencją?". Role się zacierają — inżynierowie, PM-owie i designerzy wszyscy commitują kod; najbardziej wartościowi stają się generaliści z product sense i zdolnością do shipowania end-to-end. Fiona sama używa Claude'owych "rutyn" — asynchronicznych agentów uruchamianych co rano — do automatyzacji swoich obowiązków menedżerskich, zapowiadając przejście z manualnego promptowania na zarządzanie pętlami agentów. Cowork powstał jako odpowiedź na "latentny popyt": niekoderzy używali [[Claude Code]] do analizy MRI i odzyskiwania weselnych zdjęć — sygnał, że narzędzie służy czemuś więcej niż kodowaniu.

## Frameworki i metody

**Framework bad vs. sad (weryfikacja doświadczenia):**
- **bad** — błąd nieodwracalny (crash, utrata danych): wymaga natychmiastowej reakcji
- **sad** — punkt bólu odwracalny (migotanie UI, spadek jakości rozmowy): monitorowany, zespół ma autonomię

**Zasady kulturowe zespołu Fiony:**
- "Masz pozwolenie zabić każdy proces, który nie działa" — dotyczy też procesów wprowadzonych przez samą Fionę
- "Co jest lepsze niż ja to robię? Że robi to [[Claude]]." — stały check: czy to da się zautomatyzować?

**Hiring managerów:** nowi managerowie zaczynają jako IC (individual contributors) — uczą się kodu, budują relacje, zanim sięgną po toolbox managera.

## Kluczowe dane

- Inżynierowie [[Anthropic]] w 2025 r. dostarczają 8× więcej kodu kwartalnie niż w latach 2021–2025
- Jeden z dashboardów mierzy częstotliwość przeklinania użytkowników na [[Claude Code]] — proxy dla frustracji evals nie potrafią uchwycić
- 26% organizacji nonprofit nie ma konta na YouTube (dane [[M+R]] Benchmarks 2025) — wzmianka w kontekście dyskutowanym w epizodzie

## Wnioski

- Weryfikacja jest największym nierozwiązanym problemem dla zespołów AI — coding jest w zasadzie rozwiązany, ale sprawdzenie, czy zbudowane doświadczenie jest tym, czym miało być, pozostaje otwarte.
- Praca przesuwa się z manualnego, synchronicznego promptowania na asynchroniczne zarządzanie agentami (pętle) — menedżer jako operator floty agentów.
- Kultura jest żywym organizmem, nie plakatem — największy strach Fiony to manager mówiący "wszystko OK", gdy sala płonie; transparentność o tym, co nie działa, jest fundamentem naprawy.

## Zastosowanie

Dla własnej pracy z [[Claude Code]] i automatyzacją: idea "rutyn" — agentów uruchamianych asynchronicznie co rano — jest bezpośrednio replikowalna do automatyzacji przeglądu feedbacku klientów, monitoringu projektów czy digests. Zasada "masz pozwolenie zabić każdy proces" przydaje się w zarządzaniu własnym workflow — regularny przegląd, co jeszcze robi się ręcznie, a można oddać agentom. Dla szkoleń: dobry case do pokazania, jak organizacja działająca na co dzień z AI zmienia swoje procesy zarządcze i kulturę pracy.
