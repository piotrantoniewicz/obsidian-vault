---
categories: Clippings
authors: ["[[Lauren Meyer]]"]
url: https://send-it-right.com/blog/inbox-placement-rates-explained
source: "[[Archives/2026-03-14 Inbox Placement Rates Aren t What You Think|2026-03-14 Inbox Placement Rates Aren t What You Think]]"
published: 2026-03-14
created: 2026-04-18
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "content-marketing"
---

# Inbox Placement Rates Aren't What You Think

Autorka demistyfikuje jeden z najczęściej cytowanych wskaźników email marketingu — inbox placement rate (IPR) — wskazując, że jest to sygnał pochodny (derived signal), czyli estymata zbudowana na podstawie testów seed list, a nie bezpośredni pomiar. Dostawcy skrzynek pocztowych nie informują nadawców, gdzie trafiają wiadomości po akceptacji — czy do inboxa, spamu, zakładki, czy "czarnej dziury" (szczególnie Microsoft). IPR jest więc prognozą, nie odczytem rzeczywistości. Kluczowy argument: adresy seed nie zachowują się jak realni subskrybenci — nie otwierają, nie klikają, nie zgłaszają spamu — przez co estymaty IPR mogą być fałszywie pozytywne lub negatywne. Zamiast polegać wyłącznie na IPR, marketerzy powinni analizować wiele sygnałów łącznie, priorytetyzując dane bezpośrednie od dostawców i realnych odbiorców.

## Frameworki i metody

**Podział sygnałów deliverability na dwie kategorie:**

- **Sygnały bezpośrednie (direct signals)** — "termometry": dane obserwowane bezpośrednio przez dostawców skrzynek lub realnych odbiorców
  - Bounce rates i komunikaty odrzucenia
  - Skargi na spam przez feedback loops (FBL)
  - Dane z [[Gmail Postmaster Tools]] (reputacja domeny i IP)
  - Dane z [[Microsoft SNDS]] (Smart Network Data Services)
  - Unsubscribes, CTR, reply rates, konwersje
  - Rzeczywista akceptacja/odrzucenie wiadomości

- **Sygnały pochodne (derived signals)** — "prognozy pogody": estymaty budowane na modelu, nie na bezpośredniej obserwacji
  - Inbox Placement Rate (IPR)
  - Spam Placement Rate (SPR)
  - Deliverability rate (w wielu narzędziach)
  - Reputation scores
  - Wyniki seed testów

**Reguła diagnostyczna:** Anomalia open rate na poziomie jednego dostawcy (np. 4% na Microsoft vs 25% na Gmail przy tym samym kampanii) to silny sygnał, że mail trafia do spamu u tego dostawcy — wiarygodniejszy niż wyniki seed testów.

## Kluczowe dane

- Gmail: open rate przykładowy 32,64% | Yahoo: 26,78% | Microsoft: 3,95% — tak drastyczna różnica to sygnał problemu z dostarczalnością u jednego dostawcy
- Filtrowanie spamu jest wysoce spersonalizowane — ten sam email może trafić do inboxa jednego subskrybenta i do spamu innego

## Wnioski

- IPR to estymata, nie fakt — używaj go jako sygnał ostrzegawczy do wychwytywania trendów, ale nigdy jako jedyną miarę dostarczalności
- [[Gmail Postmaster Tools]] i [[Microsoft SNDS]] to bezpłatne, bezpośrednie źródła danych o reputacji nadawcy — powinny być standardem przy każdej większej kampanii email
- Żaden pojedynczy wskaźnik nie opowie pełnej historii o dostarczalności — skargi, bounce patterns, provider-level opens i reputacja muszą być analizowane razem

## Cytat

> "Inbox placement rate to prognoza pogody, nie odczyt termometru — estymata zbudowana z danych testowych, które nie zachowują się jak prawdziwi subskrybenci."

## Zastosowanie

Ta wiedza jest bezpośrednio przydatna przy prowadzeniu email kampanii fundraisingowych dla NGO — zwłaszcza przy interpretowaniu raportów dostarczalności w narzędziach ESP. Warto uwzględnić distinkcję direct/derived signals w module o email deliverability w kursie mailowym dla organizacji. Monitorowanie [[Gmail Postmaster Tools]] i [[Microsoft SNDS]] powinno być standardową procedurą dla każdej organizacji prowadzącej regularne kampanie mailowe do większych list.
