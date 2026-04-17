---
categories:
  - "Emails"
published: 2025-07-17
created: 2026-03-26
labels:
  - "ECF"
relevance: średnia
tags:
  - "fundraising"
  - "digital-campaigning"
  - "organizacje-społeczne"
---

# Stripe accounts

Krótki wątek z pytaniem praktycznym dotyczącym konfiguracji płatności w NGO: czy jedno konto [[Stripe]] można podłączyć do wielu kont bankowych przy zbieraniu darowizn przez [[Action Network]]. Odpowiedź społeczności jest jednoznaczna — [[Stripe]] obsługuje tylko jedno konto bankowe na jeden account. Jako obejście zaproponowano tworzenie wielu kont Stripe lub użycie [[Wise]] do dystrybucji środków po ich wpłynięciu na jedno konto. Josef Davies-Coates dodatkowo opisał model fiskalnego hostingu przez [[Open Collective]], gdzie płatności trafiają na jedno konto przez Stripe, a następnie są rozdzielane dalej za pomocą Wise.

## Frameworki i metody

- **Model fiskalnego hostingu NGO** — [[Open Collective]] pełni rolę hosta finansowego: darowizny i płatności spływają przez [[Stripe]] na jedno konto bankowe (np. [[Starling Bank]]), a następnie są rozdzielane do kolejnych podmiotów lub kont za pomocą [[Wise]]
- **Obejście limitu Stripe** — zamiast podłączać jeden Stripe account do wielu banków, można: (a) założyć wiele oddzielnych kont Stripe lub (b) przyjąć środki na jedno konto i dystrybować je zewnętrznym narzędziem (Wise, Open Collective)

## Kluczowe dane

- [[Stripe]]: 1 konto = 1 konto bankowe — nie ma możliwości podłączenia wielu banków do jednego Stripe account
- [[Open Collective]] zmienia model cenowy w 2026 r. — integracja z [[Wise]] będzie wymagała planu za $59/mies., co może uczynić ten model nieopłacalnym dla małych hostów fiskalnych

## Wnioski

- Przy planowaniu infrastruktury płatniczej dla NGO zbierającej środki dla wielu podmiotów warto uwzględnić [[Open Collective]] + [[Wise]] jako alternatywę dla tworzenia wielu kont Stripe
- [[Action Network]] nie zmienia ograniczeń Stripe — pytanie o platformę campaignową jest tu drugorzędne; ważniejsza jest architektura systemu płatniczego
- Zmiana cennika [[Open Collective]] w 2026 r. może wymusić szukanie alternatywnych modeli fiskalnego hostingu dla małych organizacji i kolektywów

## Cytat

> „Możesz oczywiście mieć wiele kont Stripe, jeśli to rozwiązuje twój problem."

## Zastosowanie

Przy doradzaniu organizacjom w zakresie cyfrowego fundraisingu warto pamiętać o architekturze systemu płatniczego — szczególnie gdy organizacja obsługuje środki dla wielu podmiotów lub prowadzi hosting fiskalny. Model Stripe + Wise jest dobrym, prostym rozwiązaniem do dystrybucji środków. Zmiany cennika Open Collective warto monitorować — mogą wpłynąć na organizacje, które korzystają z tego modelu w Polsce.
