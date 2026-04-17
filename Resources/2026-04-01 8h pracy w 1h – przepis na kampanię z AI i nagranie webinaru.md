---
categories:
  - "Emails"
published: 2026-04-01
created: 2026-04-12
labels:
  - "AI Marketers"
relevance: średnia
tags:
  - "content-marketing"
  - "narzędzia-AI"
  - "automatyzacja"
---

# 8h pracy w 1h – przepis na kampanię z AI i nagranie webinaru

Artur Jabłoński z [[AI_Marketers]] przedstawia 6-krokowy proces tworzenia kampanii reklamowej w [[Meta Ads]] z użyciem AI — od researchu po automatyzację ustawiania kampanii przez API. Kluczową tezą jest prymat procesu nad wyborem konkretnego modelu (GPT vs [[Claude]]). Newsletter towarzyszył nagraniu webinaru, na którym cały workflow został przeprowadzony na żywo, redukując 8 godzin pracy do 1 godziny. Promocja paid programu stanowi drugoplanowy element komunikatu.

## Frameworki i metody

- **Krok 1 – Research** — najpierw ułóż ramy strategiczne, zanim sięgniesz po narzędzia; wybór modelu AI jest wtórny wobec procesu myślowego
- **Krok 2 – Generowanie idei** — podaj modelowi link do strony produktu; AI wyciągnie grupę docelową, wyróżniki, cenę i styl pisania, a następnie dobierze formaty reklam; ułóż sekwencję (prospecting/remarketing) przed tworzeniem wariantów
- **Krok 3 – Copywriting** — zasada „przykład ważniejszy od instrukcji": nasycenie modelu próbkami najlepszych tekstów sprawia, że replikuje on styl bez generycznej treści
- **Krok 4 – Kreacja graficzna** — technika **JSON prompting**: kodowy opis układu, kolorystyki i elementów wizualnych zapewnia spójność wizualną między wariantami
- **Krok 5 – Automatyzacja ustawiania kampanii** — użycie [[Claude Code]] przez API do skonfigurowania struktury kampanii bezpośrednio na koncie reklamowym, z pominięciem Menadżera Reklam
- **Krok 6 – Weryfikacja** — uwaga na „rady z kosmosu": AI jest tendencyjne i może mylić się w analizie danych; wiedza analityczna człowieka to kluczowy bezpiecznik

## Wnioski

- Wyłączanie pamięci modelu i rozpoczynanie nowych rozmów poprawia jakość odpowiedzi i zmniejsza ryzyko halucynacji — szczególnie ważne przy wieloetapowych procesach produkcyjnych z [[LLM]]
- [[AI]] jako sparing partner powinien proponować rozwiązania spoza marketingowej rutyny — jeśli model replikuje tylko znane schematy, traci swoją główną wartość dodaną w procesie ideacji
- Na końcu i tak liczy się pomysł — [[automatyzacja]] przyspiesza wdrożenie, ale nie zastępuje kreatywnej decyzji i oceny jakości; to istotne ograniczenie w kontekście wdrożeń AI dla organizacji

## Cytat

> „Proces jest ważniejszy niż wybór konkretnego modelu — ułóż ramy strategiczne, zanim dotkniesz narzędzi."

## Zastosowanie

Framework 6-kroków może posłużyć jako struktura warsztatu lub modułu szkoleniowego w ramach kursów AI dla organizacji społecznych — szczególnie kroki 2–3 (generowanie idei i copywriting) mają bezpośrednie przełożenie na kampanie fundraisingowe i digital campaigning dla NGO. Technika JSON prompting do kreacji graficznej warta przetestowania przy produkcji materiałów kampanijnych dla klientów. Automatyzacja przez API ([[Claude Code]]) to potencjalny element oferty wdrożeniowej dla bardziej zaawansowanych klientów dobryai.pl.
