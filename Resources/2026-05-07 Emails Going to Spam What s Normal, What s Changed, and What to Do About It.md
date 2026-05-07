---
categories: Clippings
authors:
  - '[[Beth OMalley]]'
url: >-
  https://weareastral.co.uk/thevault/emails-going-to-spam-whats-normal-whats-changed-and-what-to-do-about-it
source: >-
  "[[Archives/2026-05-07 Emails Going to Spam What s Normal, What s Changed, and
  What to Do About It|2026-05-07 Emails Going to Spam What s Normal, What s
  Changed, and What to Do About It]]"
published: '2026-05-07'
created: '2026-05-07'
relevance: wysoka
tags:
  - digital-campaigning
  - fundraising
  - content-marketing
---
# Emails Going to Spam: What's Normal, What's Changed, and What to Do About It

Artykuł kompleksowo omawia temat dostarczalności emaili — odróżnia normalne poziomy spam placement (0–15% to norma) od strukturalnych problemów wymagających interwencji, i wyjaśnia kluczową różnicę: delivery rate widoczna w panelu ESP to nie to samo co inbox placement. Email może być "dostarczony" do folderu spam, a ESP pokaże 98–99% skuteczności. Autorka prezentuje benchmarki dla głównych dostawców skrzynek za 2025 rok, wyjaśnia zmiany jakie zaszły z wprowadzeniem obowiązkowych wymagań dla nadawców masowych (DMARC, SPF, DKIM, one-click unsubscribe) i opisuje strategie monitorowania i naprawy reputacji nadawcy. Kluczowa teza: deliverability to nie problem techniczny, który rozwiązuje się raz — to dyscyplina, którą się utrzymuje.

## Frameworki i metody

- **Trzy typy spam placement** (różniące się powagą i reakcją):
  - Typ 1 — algorytmiczna decyzja dostawcy skrzynki (najczęstszy, mierzalny, zarządzalny)
  - Typ 2 — zgłoszenie spam przez odbiorcę (poważniejszy — bezpośrednio niszczy reputację)
  - Typ 3 — odrzucenie wiadomości przez serwer (email nie dotarł wcale)
- **Tabela progów spam placement rate**:
  - 0–15%: zdrowy program — kontynuuj, monitoruj
  - 15–25%: warto obserwować — sprawdź czy to trend czy jednorazowy skok
  - 26–50%: potrzebna uwaga — audyt programu, lista, reputacja
  - 50%+: poważny problem — pełna interwencja, zatrzymaj wysyłki do niezaangażowanych
- **Rozróżnienie: sustained vs. short-term problem** — patrzeć na trendy tygodniowe, 30-dniowe i 90-dniowe; odpowiedź na skok jednorazowy jest zupełnie inna niż na problem strukturalny
- **Narzędzia do monitorowania inbox placement**: [[GlockApps]], [[Mail Tester]], [[Validity]], [[Google Postmaster Tools]] (reputacja domeny + wskaźnik skarg), Yahoo Sender Hub, Microsoft SNDS

## Kluczowe dane

- Gmail: 89.8% inbox rate, 6.4% spam (2025) — najszybszy w karaniu i w recovery
- Microsoft (Outlook/Hotmail): 77.4% inbox rate, 15.1% spam (2025) — najtrudniejszy dostawca, powolne recovery; problem zwielokrotniony w B2B przez korporacyjne filtry bezpieczeństwa ([[Proofpoint]], [[Mimecast]])
- Yahoo: 87.3% inbox rate, 6.4% spam (2025)
- Globalny inbox placement 2025: 87.2% (wzrost 3.7% r/r) — dzięki wymogom dla nadawców masowych
- Średni wskaźnik skarg spam w 2025: 0.06%; oczekiwany próg to poniżej 0.1% (próg 0.3% jest już nieakceptowalny)

## Wnioski

- Dashboard ESP pokazujący 98–99% "dostarczenia" nie mierzy inbox placement — do monitorowania faktycznej dostarczalności potrzebne są dedykowane narzędzia zewnętrzne; bez nich organizacja jest ślepa na realne problemy.
- [[Microsoft]] (Outlook/Hotmail) to najtrudniejszy dostawca dla email marketingu — spam placement 15.1% i powolne recovery; szczególnie ważne dla NGO z bazą darczyńców korporacyjnych lub partnerów biznesowych, gdzie dominuje środowisko B2B.
- Od 2025 DMARC, SPF, DKIM i one-click unsubscribe to obowiązkowe standardy u wszystkich głównych dostawców — nie opcjonalne, a infrastrukturalny warunek skutecznej komunikacji emailowej.

## Zastosowanie

W kursie mailowym dla NGO warto uwzględnić moduł o deliverability — szczególnie rozróżnienie między delivery rate a inbox placement oraz obowiązkowe wymagania techniczne (DMARC, SPF, DKIM). Minimum dla każdej organizacji prowadzącej kampanie fundraisingowe to [[Google Postmaster Tools]] — darmowe narzędzie Google dające bezpośredni wgląd w reputację domeny i wskaźnik skarg. Przy diagnozie słabych wyników kampanii emailowych warto zacząć właśnie od sprawdzenia inbox placement, a nie od treści czy designu.
