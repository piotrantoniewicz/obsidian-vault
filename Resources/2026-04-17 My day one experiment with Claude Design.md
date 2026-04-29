---
categories:
  - "Emails"
published: 2026-04-17
created: 2026-04-29
labels:
  - "Ryan Carr"
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "content-marketing"
---

# My day one experiment with Claude Design 🎨

Anthropic wypuściło Claude Design — nowe narzędzie w fazie research preview (dla subskrybentów Pro, Max, Team i Enterprise), które na podstawie opisu i opcjonalnie kodu strony lub plików designowych buduje prototypy, slajdy i inne materiały wizualne zgodne z systemem brandingowym. Ryan Carr przetestował je pierwszego dnia dostępu, budując system brandingowy z kodu strony Tailwind oraz sales deck dla agencji. Narzędzie zaskoczyło go poziomem samodzielności — rozpoznaje i kategoryzuje każdy komponent strony, prowadzi użytkownika przez kwestionariusz zamiast zgadywać intencje, a błędy w layoutzie wychwytuje i poprawia samodzielnie przez analizę własnych screenshotów. Autor udostępnia prompt „Slide Deck Outline Wizard", który rozdziela strategiczne planowanie struktury od etapu wizualnego budowania w Claude Design.

## Frameworki i metody

- **Design System z kodu** — [[Claude Design]] analizuje kod strony i indeksuje wszystkie komponenty (kolory, fonty, moduły, styl layoutu), tworząc reużywalny system brandingowy automatycznie aplikowany do każdego kolejnego materiału
- **Slide Deck Outline Wizard** — prompt-workflow rozdzielający myślenie (wywiad o celach, odbiorcach i narracji → strukturowany outline slide po slajdzie) od budowania (Claude Design lub Claude Chat przejmuje outline i wizualizuje); użyteczny też bez dostępu do Claude Design
- **Dynamiczne przełączniki w prezentacjach** — funkcja pozwalająca budować jeden deck z toggleami ukrywającymi/pokazującymi sekcje (np. cennik) zależnie od odbiorcy — pozwala prezentować ten sam deck różnym grupom

## Wnioski

- [[Claude Design]] reprezentuje wyraźny upgrade w generowaniu brandowanych materiałów wizualnych i front-end UI w porównaniu do standardowego [[Claude]] Chat — warto śledzić jego rozwój jako narzędzia do tworzenia materiałów dla klientów z NGO
- Separacja strategii od wykonania (wizard → Claude Design) to użyteczny pattern do wdrożenia w szkoleniach z AI — uczy myślenia etapami i ogranicza ryzyko błędów w długich, złożonych materiałach
- Narzędzie samodzielnie wykrywa i poprawia błędy wizualne przez robienie i analizowanie screenshotów własnej pracy — sygnał dojrzałości agentycznej, istotny przy ocenie narzędzi AI do pracy z klientem

## Cytat

> „Claude Design to wyraźny upgrade możliwości Claude'a w generowaniu brandowanych materiałów wizualnych i front-end UI."

## Zastosowanie

Claude Design może przyspieszyć tworzenie materiałów wizualnych (prezentacje, one-pagery) dla klientów z sektora NGO — warto przetestować go przy kolejnym projekcie dla Dolnośląskiej Sieci Partnerstw LGD lub PNRWI. Slide Deck Outline Wizard nadaje się bezpośrednio jako przykład do kursu Fundraising z AI — pokazuje, jak rozdzielać zadania między etapy myślenia i wykonania. Dynamiczne przełączniki w decku to technika warta omówienia w kontekście prezentacji kierowanych do różnych grup darczyńców.
