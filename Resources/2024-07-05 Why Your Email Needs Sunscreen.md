---
categories: Clippings
authors: ["[[Lauren Meyer]]"]
url: https://send-it-right.com/blog/intro-to-email-authentication
source: "[[Archives/2024-07-05 Why Your Email Needs Sunscreen|2024-07-05 Why Your Email Needs Sunscreen]]"
published: 2024-07-05
created: 2026-04-27
relevance: średnia
tags:
  - "digital-campaigning"
---

# Why Your Email Needs Sunscreen

Lekki, przystępny przewodnik po email authentication — SPF, DKIM i DMARC — napisany jako newsletter przez eksperta dostarczalności. Autorka wyjaśnia, że uwierzytelnienie poczty jest dziś wymagane przez głównych dostawców skrzynek (Google, Yahoo, Microsoft) i chroni reputację nadawcy przed fałszowaniem. Artykuł tłumaczy działanie każdego protokołu na poziomie operacyjnym i opisuje fazowy plan wdrożenia DMARC. Kluczowy wniosek: brak uwierzytelnienia prowadzi bezpośrednio do lądowania w folderze spam.

## Frameworki i metody

- **SPF (Sender Policy Framework)** — lista adresów IP uprawnionych do wysyłania w imieniu domeny. Zapobiega fałszowaniu adresu nadawcy. Ograniczenie: nie chroni przed modyfikacją treści wiadomości w trakcie transmisji.
- **DKIM (DomainKeys Identified Mail)** — podpis kryptograficzny pozwalający serwerowi odbiorczemu sprawdzić, czy wiadomość nie została zmieniona w trakcie dostarczania. Chroni przed przechwyceniem i modyfikacją treści.
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** — faza wdrożenia:
  - Faza 0: SPF i DKIM już skonfigurowane
  - Faza 1: `p=none` — tryb monitorowania, zbieranie raportów
  - Faza 2: `p=quarantine` — mail niespełniający wymogów trafia do folderu spam
  - Faza 3: `p=reject` — mail niespełniający wymogów jest odrzucany
  - Faza 4: ciągłe monitorowanie raportów DMARC i reagowanie na błędy

## Kluczowe dane

- Yahoo szacuje, że ~95% całej przychodzacej poczty to mail złośliwy lub spam — uwierzytelnienie pozwala wyróżnić się spośród pozostałych 5%.
- Brak uwierzytelnienia może obniżyć wskaźnik otwarć z ~55% do 5% (przykład z Google Gmail).

## Wnioski

- Email authentication nie jest opcją — jest wymagany przez Google, Yahoo i Microsoft jako warunek dostarczenia wiadomości do skrzynki odbiorcy.
- Reputacja nadawcy jest powiązana z domeną, nie z adresem IP — zmiana ESP nie wystarczy, jeśli domenowe praktyki wysyłkowe są złe.
- Rekordy SPF i DKIM wymagają sporadycznej konserwacji: reorganizacje IT, zmiany dostawców lub nowe integracje mogą nieświadomie uszkodzić konfigurację i zablokować dostarczanie.

## Zastosowanie

Dla organizacji NGO prowadzących kampanie emailowe (fundraising, advocacy) poprawna konfiguracja SPF, DKIM i DMARC to techniczny warunek wstępny skuteczności kampanii — warto upewnić się, że jest ona zrobiona przy wdrożeniu nowego ESP lub CRM. Przy szkoleniu "Fundraising z AI" warto uwzględnić ten temat jako element modułu o higienie listy i dostarczalności. Wdrożenie DMARC w trybie monitorowania (p=none) to bezpieczny pierwszy krok dla organizacji, które nigdy wcześniej tego nie robiły.
