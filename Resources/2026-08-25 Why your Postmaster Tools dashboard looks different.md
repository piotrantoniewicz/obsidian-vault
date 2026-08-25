---
categories:
  - "Emails"
published: 2026-08-25
created: 2026-08-25
labels:
  - "Civic Shout"
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "organizacje-społeczne"
---

# Why your Postmaster Tools dashboard looks different

Newsletter Civic Shout opisuje wycofanie przez Google starej wersji Postmaster Tools (v1) i zastąpienie jej wersją v2, w której zniknął dotychczasowy prosty wskaźnik reputacji domeny i IP (High/Medium/Low/Bad). W jego miejsce pojawia się bardziej szczegółowa analiza deliverability, oparta na realnym zachowaniu odbiorców (otwarcia, oznaczanie jako spam) i formułowana w postaci werdyktu z konkretną rekomendacją działania. Dla zespołów prowadzących kampanie mailowe (fundraising, digital campaigning) oznacza to konieczność zmiany nawyku monitorowania — zamiast jednego zbiorczego wskaźnika trzeba śledzić kilka osobnych metryk. Tekst jest praktycznym przewodnikiem po tym, co obserwować w nowym interfejsie przed dużymi kampaniami mailingowymi.

## Frameworki i metody
- **Trzy wskaźniki do monitorowania w Postmaster Tools v2** — wskaźnik skarg spamowych (spam complaint rate) jako najważniejsza liczba; status zgodności (compliance status), pokazujący punkt po punkcie błędy w konfiguracji (np. DMARC, tempo obsługi wypisów); analiza deliverability — werdykt słowny oparty na zachowaniu odbiorców, z rekomendacją naprawczą.

## Kluczowe dane
- Google zaleca utrzymanie wskaźnika skarg spamowych poniżej 0,10%
- 0,30% skarg spamowych to twardy próg — po jego przekroczeniu Gmail może zacząć odrzucać wiadomości
- Sekcja analizy deliverability została dodana do Postmaster Tools w czerwcu 2026

## Wnioski
- Zniknięcie prostego wskaźnika reputacji domeny w [[Google Postmaster Tools]] wymusza bardziej rozdrobnione monitorowanie deliverability przy kampaniach e-mail fundraisingowych i advocacy
- Wskaźnik skarg spamowych (0,10% / 0,30%) to konkretny, łatwy do wdrożenia próg alarmowy dla list mailingowych organizacji społecznych
- Nowa analiza deliverability ocenia realne zaangażowanie odbiorców, a nie tylko formalną poprawność wysyłki — to przesuwa uwagę z technicznej konfiguracji na jakość i trafność treści maila

## Zastosowanie
Warto sprawdzić dostęp do nowego dashboardu Postmaster Tools dla domen używanych w kampaniach mailowych klientów NGO i włączyć monitorowanie wskaźnika skarg spamowych jako stały element przed dużymi wysyłkami (np. kampanie końcoworoczne). Może się to przydać jako element checklisty w kursie mailowym o fundraisingu z AI.
