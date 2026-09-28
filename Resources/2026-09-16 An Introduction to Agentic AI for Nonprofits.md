---
categories:
  - Clippings
authors: ["[[CharityEngine]]"]
url: "https://www.youtube.com/watch?v=DGga1aVtu_I"
source: "[[Archives/2026-09-16 An Introduction to Agentic AI for Nonprofits|2026-09-16 An Introduction to Agentic AI for Nonprofits]]"
published: 2026-09-16
created: 2026-09-22
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "strategia-AI"
---

# An Introduction to Agentic AI for Nonprofits

Webinar TechSoup (prowadzący Stephen Jackson) sponsorowany przez CharityEngine wyjaśnia różnicę między chatbotem, asystentem AI a agentic AI oraz argumentuje, że najrozsądniejszym pierwszym krokiem dla małych i średnich organizacji nie jest wdrażanie agentów, lecz dobrze skonfigurowanych asystentów. Asystenci (np. projekty w Claude, Gemini, Copilot) budowane są na kontekście — dokumentach, transkryptach, briefach — i pozostają w pełni pod kontrolą użytkownika, podczas gdy agent samodzielnie planuje i wykonuje wieloetapowy proces w kierunku zadanego celu. Kluczowa teza: agenci działają wiarygodnie tylko na czystych, uporządkowanych danych, przy jasnych barierach ochronnych (guardrails) i z osobą odpowiedzialną za wynik — a praca z asystentami jest poligonem treningowym budującym te właśnie kompetencje przed przejściem do pełnej autonomii.

## Frameworki i metody

**Trzy narzędzia na spektrum autonomii:**
- **Chatbot** — statyczna biblioteka odpowiedzi na konkretne pytania (FAQ, formularz darowizny, wskazywanie zasobów); szybki, ale ograniczony do tego, co zostało wcześniej zaprogramowane.
- **Asystent AI** — narzędzie kierowane przez użytkownika, budowane wokół kontekstu (np. „projekt” w Claude/Gemini/Copilot); produkuje szkice, które użytkownik dopracowuje krok po kroku, pozostając w pętli decyzyjnej na każdym etapie.
- **Agentic AI** — oprogramowanie realizujące zadany cel wieloetapowo i coraz bardziej autonomicznie, samodzielnie decydujące, z jakich narzędzi skorzystać (CRM, skrzynka mailowa, kalendarz), w granicach ustalonych barier ochronnych.

**Budowanie asystenta (projektu) — zasada kontekstu:**
- Wgraj dane kontekstowe: raport roczny, dokument marki/stylu, fact sheet organizacji, briefy dużych darczyńców, transkrypty rozmów.
- Dodaj jasne instrukcje: cel, teza przewodnia kampanii, sposób działania.
- Format markdown ułatwia narzędziu efektywniejsze przetwarzanie danych przy zachowaniu czytelności dla człowieka.
- Im więcej trafnego kontekstu, tym bardziej autentyczne odpowiedzi — bez niego narzędzie sięga po ogólną wiedzę z internetu.

**Pięć pytań gotowości przed przejściem z asystenta do agenta:**
1. **Dane** — czy są czyste, aktualne i wystarczająco uporządkowane, by agent mógł na nich bezpiecznie działać?
2. **Systemy** — czy narzędzia są połączone (np. przez [[MCP]]) tak, by agent mógł z nich wiarygodnie czytać i do nich zapisywać?
3. **Governance** — kto zatwierdza działania agenta, kto odpowiada za błędy, kto ustala zasady dotyczące danych i autonomicznych działań publicznych?
4. **Zaufanie darczyńców** — jaki jest poziom transparentności wobec darczyńców co do użycia AI w komunikacji?
5. **Model kosztowy** — ile będzie kosztować utrzymanie systemu (zużycie tokenów) i czy organizację będzie na to stać długoterminowo.

## Kluczowe dane
- Wg benchmarku TechSoup i TAP Network z 2025 r. (1500 organizacji w USA): 50% pracowników NGO już korzysta z narzędzi AI w pracy.
- Widoczna luka między zamiarem korzystania z AI a realną zdolnością — brak zasobów, dostępu do szkoleń i umiejętności.

## Wnioski
- Droga do agentic AI prowadzi przez dobrze skonfigurowane asystenty — to buduje nawyki porządkowania danych, ustalania barier ochronnych i rozliczalności, zanim organizacja odda agentowi realną autonomię.
- [[Model Context Protocol]] i połączenie narzędzi (CRM, workspace, kalendarz) to techniczny warunek konieczny, by agent mógł działać wiarygodnie — bez tego pozostaje na etapie asystenta.
- Zaufanie darczyńców jest kruche: jeden nienadzorowany błąd AI może zaważyć na reputacji budowanej latami, więc governance i transparentność muszą wyprzedzać wdrożenie autonomii.

## Cytat
> Agentic AI potrzebuje czystych danych, bardzo jasnych barier ochronnych i osoby odpowiedzialnej za wynik.

## Zastosowanie
Bezpośrednio przydatne przy doradztwie wdrożeniowym AI dla NGO — framework „pięciu pytań gotowości” i rozróżnienie chatbot/asystent/agent to gotowy szkielet warsztatu lub konsultacji dla organizacji zastanawiających się nad automatyzacją. Praktyczny przykład budowania „projektu” z kontekstem (raport roczny, brief marki, transkrypty) można wykorzystać jako ćwiczenie w szkoleniach z AI dla sektora społecznego.
