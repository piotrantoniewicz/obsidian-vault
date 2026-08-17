---
categories:
  - "Emails"
published: 2026-06-23
created: 2026-06-23
labels:
  - "wPraktyce"
relevance: wysoka
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "szkolenia-AI"
---

# "A to nie wycieknie?" - na ile ufasz AI

Patryk Łopot z wPraktyce.AI opisuje, dlaczego obawa przed wyciekiem danych przy wdrożeniu AI jest często skierowana w złą stronę. Autor wyróżnia dwie warstwy systemu: miejsce, gdzie AI "myśli" (model na serwerach europejskich pod RODO), oraz miejsce przechowywania firmowej wiedzy (baza [[RAG]] wyłącznie u klienta, niedostępna dla innych). Ironią jest, że dane firmowe są zwykle mniej bezpieczne w obecnym rozproszeniu — skrzynki mailowe, prywatne dyski, niekontrolowane użycie publicznych czatów — niż w dobrze postawionym systemie AI z logami i kontrolą dostępu. Newsletter kończy się praktycznym ćwiczeniem: policz miejsca, w których leżą wrażliwe dane, i sprawdź, czy ktoś już nie wrzuca firmowych plików do publicznego [[ChatGPT]].

## Frameworki i metody

- **Model vs. wiedza** — kluczowe rozróżnienie: model ([[Claude AI|Claude]]/Gemini) na serwerach europejskich pod DPA i RODO ≠ publiczny czat; wiedza firmowa w bazie [[RAG]] wyłącznie u klienta, niedostępna innym
- **Anonimizacja** — do modelu trafia tylko niezbędne minimum; dane wrażliwe są podstawiane lub zaciemniane przed wysłaniem do modelu
- **Deployment offline** — opcja "zamkniętej puszki": model postawiony na własnym serwerze klienta, bez dostępu do internetu
- **Baza RAG odcięta od sieci** — karmiona wyłącznie dokumentami i regułami klienta; eliminuje ryzyko "halucynowania z internetu"

## Wnioski

- Paradoks bezpieczeństwa: dane firmowe w rozproszeniu (skrzynki byłych pracowników, prywatne dyski, publiczne czaty) są bardziej narażone niż w dobrze skonfigurowanym systemie AI z logami i Kill Switchem
- RODO nie blokuje AI — blokuje *źle postawione* AI; dobrze skonfigurowane wdrożenie daje większą kontrolę nad danymi, nie mniejszą
- Największe ryzyko wycieku pochodzi często nie od formalnych wdrożeń AI, lecz od niekontrolowanego użycia publicznego [[ChatGPT]] przez pracowników "po cichu"

## Zastosowanie

Argument o bezpieczeństwie danych to najczęstszy bloker przy wdrożeniach AI w NGO, kancelariach i biurach rachunkowych. Framework "model vs. wiedza" plus opcja offline pozwala konkretnie odpowiadać na obiekcje organizacji działających pod NDA lub przetwarzających dane darczyńców. Ćwiczenie "policz miejsca, gdzie leżą Twoje dane" można wykorzystać jako otwierające ćwiczenie na szkoleniu z AI — by uczestnicy sami zauważyli bieżące ryzyko przed rozmową o ryzyku AI.
