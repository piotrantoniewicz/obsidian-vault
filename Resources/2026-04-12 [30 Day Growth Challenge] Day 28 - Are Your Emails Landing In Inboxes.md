---
categories:
  - Emails
published: '2026-04-12'
created: '2026-04-25'
labels:
  - Jess Campbell
relevance: wysoka
tags:
  - fundraising
  - digital-campaigning
  - narzędzia-AI
---
# [30 Day Growth Challenge] Day 28: Are Your Emails Landing In Inboxes?

Jess Campbell omawia techniczny, ale fundamentalny aspekt email marketingu dla NGO — dostarczalność wiadomości. Kluczowa teza: nawet najlepszy email jest bezużyteczny, jeśli nie trafia do skrzynki odbiorcy. Autorka proponuje trójkrokowy proces weryfikacji i naprawy, który powinien być wykonywany co kwartał. Szczególnie istotne dla organizacji przygotowujących kampanie fundraisingowe przed Q4.

## Frameworki i metody

- **Scrubbing listy mailingowej** — usuwanie subskrybentów, którzy nie otwierali żadnych maili przez 6–12 miesięcy; nieaktywni odbiorcy obniżają wskaźnik dostarczalności w oczach dostawców usług email
- **Test "spammyness"** — sprawdzenie technicznej konfiguracji domeny za pomocą [[dmarcian]] (weryfikacja DMARC), a następnie wysłanie testowego maila przez [[Mail-Tester]] i ocena wyniku w skali 10/10
- **Naprawa konfiguracji** — jeśli wynik testu nie jest 10/10, należy poprawić znalezione błędy (SPF, DKIM, DMARC) zanim wyśle się kolejną kampanię

## Kluczowe dane

- Czyszczenie listy warto wykonywać kilka razy w roku
- Docelowy wynik w Mail-Tester: 10/10

## Wnioski

- Dostarczalność emaili to fundament każdej strategii [[digital-campaigning]] — organizacje NGO często pomijają ten aspekt techniczny, skupiając się tylko na treści
- Regularne czyszczenie listy mailingowej jest kluczowe dla [[fundraising]]u: nieaktywni subskrybenci obniżają reputację domeny i mogą zablokować dotarcie do aktywnych darczyńców
- Narzędzia takie jak [[dmarcian]] i [[Mail-Tester]] pozwalają szybko zidentyfikować problemy techniczne bez specjalistycznej wiedzy IT — przydatne dla małych zespołów NGO

## Cytat

> Możesz wysyłać najlepsze emaile na świecie, ale jeśli nie trafiają do skrzynek — jaki ma to sens?

## Zastosowanie

W pracy z NGO warto wprowadzić kwartalny audyt dostarczalności jako element standardowej higieny email marketingu — szczególnie przed kampaniami fundraisingowymi Q3/Q4. Narzędzia [[dmarcian]] i [[Mail-Tester]] można uwzględnić w checkliście wdrożeniowej dla organizacji korzystających z systemów jak Mailchimp czy [[Ecomail]]. Warto też uwzględnić ten temat w kursie "Fundraising z AI" jako moduł techniczny poprzedzający budowanie listy.
