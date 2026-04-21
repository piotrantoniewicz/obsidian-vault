---
categories:
  - Emails
published: '2026-04-21'
created: '2026-04-21'
labels:
  - Civic Shout
relevance: wysoka
tags:
  - digital-campaigning
  - fundraising
  - organizacje-społeczne
---
# Is a shared IP secretly harming your deliverability?

Newsletter prezentuje case study [[Humane Society of Utah]] (HSU), która przez miesiące notowała stagnację przychodów z emaili mimo testowania różnych wersji kreacji. Diagnoza ujawniła, że problem leżał nie w treści, lecz w dostarczalności — platforma przypisała HSU do puli współdzielonych IP o złej reputacji, przez co wiadomości trafiały do spamu. Rozwiązaniem była migracja do [[Mailchimp]] z dedykowanym IP, poprzedzona czyszczeniem listy przez [[BriteVerify]] oraz ociepleniem (warm-up) nowego adresu poprzez stopniowane wysyłki do najbardziej zaangażowanych segmentów. Efekt: HSU podwoiła całoroczny wynik emailowy z 2022 roku już do końca 2023.

## Frameworki i metody

- **Audyt dostarczalności przed optymalizacją kreacji** — zamiast przepisywać copy, HSU z pomocą [[RKD Group]] najpierw uruchomiła przegląd higieny email (email hygiene review), który zidentyfikował słabą inbox placement jako rzeczywistą przyczynę problemu
- **Oczyszczenie listy przez [[BriteVerify]]** — przed migracją usunięto nieprawidłowe adresy; importowanie brudnej listy na nowe IP to szybki sposób na zniszczenie reputacji nadawcy jeszcze przed pierwszą wysyłką
- **IP warm-up z segmentacją zaangażowania** — staggered onboarding: najpierw wysyłki do najbardziej aktywnych subskrybentów, welcome series dla nowych, reactivation series dla nieaktywnych od dłuższego czasu; zaangażowane grupy pierwsze budują pozytywny sygnał reputacyjny
- **Seed test dostarczalności** — sprawdzenie inbox placement w Gmail, Yahoo i Outlook jako pierwszy krok diagnostyczny przy stagnujących wynikach

## Kluczowe dane

- Od stycznia do lipca 2023 HSU zebrała więcej przychodów z emaili niż przez cały rok 2022
- Do końca 2023 niemal podwoiła wynik z całego 2022 roku
- Połowa bazy HSU była nieaktywna przed migracją — potencjalnie z powodu problemu dostarczalności, nie braku zainteresowania

## Wnioski

- Stagnacja przychodów z emaili to często problem widoczności (dostarczalności), nie kreacji — seed test w Gmail, Yahoo i Outlook powinien być pierwszym krokiem diagnostycznym, zanim zmieni się jakikolwiek element treści
- Segment „nieaktywnych" subskrybentów może być fałszywie nieaktywny — jeśli wiele osób przestało otwierać maile w tym samym 30-dniowym oknie, to sygnał dostarczalności, nie braku zainteresowania
- Migracja na dedykowany IP wymaga wcześniejszego czyszczenia listy (np. przez [[BriteVerify]]) i planu warm-up opartego na segmentacji zaangażowania — bez tego nowy IP może odziedziczyć złą reputację

## Cytat

> "Płaskie przychody z emaili to problem widoczności udający problem kreacji — częściej niż chcielibyśmy przyznać."

## Zastosowanie

Przy kampaniach emailowych dla NGO, gdy testy kreatywne nie przynoszą rezultatów, warto zacząć diagnozę od sprawdzenia dostarczalności, a nie przepisywania copy. Metodologia HSU — audyt → czyszczenie listy → migracja → warm-up z segmentacją zaangażowania — może służyć jako gotowy szablon procesu dla organizacji rozwijających email fundraising. Wiedza o dedykowanych IP, seed testach i reactivation series jest bezpośrednio przydatna przy wdrożeniach i szkoleniach dla klientów Piotra.
