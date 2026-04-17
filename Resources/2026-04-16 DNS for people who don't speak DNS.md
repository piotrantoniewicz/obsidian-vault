---
categories:
  - "Emails"
published: 2026-04-16
created: 2026-04-17
labels:
  - "Civic Shout"
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "organizacje-społeczne"
---

# DNS for people who don't speak DNS

Newsletter Civic Shout tłumaczy w przystępny sposób trzy kluczowe rekordy DNS odpowiedzialne za uwierzytelnianie emaili: SPF, DKIM i DMARC. Od 2024 roku Google i Yahoo, a od maja 2025 Microsoft, wymagają poprawnej konfiguracji tych rekordów od nadawców wysyłających powyżej 5000 emaili dziennie. Brak tych rekordów skutkuje trafianiem wiadomości do spamu lub ich blokowaniem, co bezpośrednio uderza w skuteczność kampanii fundraisingowych i mobilizacyjnych. Newsletter wskazuje bezpłatne narzędzie [[MXToolbox]] do audytu konfiguracji domeny i rekomenduje stopniowe zaostrzanie polityki DMARC.

## Frameworki i metody

- **SPF (Sender Policy Framework)** — lista platform uprawnionych do wysyłki emaili z twojej domeny; jeśli platforma nie jest na liście, jej wiadomości mogą być traktowane jako podejrzane.
- **DKIM (DomainKeys Identified Mail)** — cyfrowy podpis każdego wysyłanego emaila, potwierdzający że wiadomość nie była modyfikowana w trakcie transmisji; klucz generuje platforma mailingowa, trzeba go opublikować w DNS.
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** — łączy SPF i DKIM, definiując politykę dla nieskutecznie uwierzytelnionych wiadomości: `none` (tylko monitoring), `quarantine` (do spamu) lub `reject` (blokada); DMARC jest też warunkiem wstępnym wyświetlania logo przez [[BIMI]].
- **Audyt DNS** — bezpłatne narzędzie [[MXToolbox]] pozwala sprawdzić aktualne rekordy SPF, DKIM i DMARC dla dowolnej domeny.

## Kluczowe dane

- Od 2024 roku Google i Yahoo wymagają SPF, DKIM i DMARC od nadawców wysyłających ponad 5000 emaili dziennie.
- Microsoft wprowadził analogiczne wymagania dla Outlook, Hotmail i Live.com w maju 2025 roku.

## Wnioski

- Poprawna konfiguracja SPF, DKIM i DMARC to warunek konieczny skutecznych kampanii emailowych — bez tego wiadomości trafiają do spamu lub są blokowane, co może torpedować akcje [[digital-campaigning]] i zbiórki dla organizacji społecznych.
- Organizacje korzystające z wielu platform mailingowych (np. [[Make.com]], CRM, narzędzia fundraisingowe) muszą upewnić się, że każda z nich jest wpisana w rekord SPF domeny — pominięcie jednej platformy wystarczy, by jej wysyłki były traktowane jako podejrzane.
- Przejście polityki DMARC z `none` na `quarantine` i docelowo `reject` to rekomendowany kierunek — chroni reputację domeny i otwiera drogę do [[BIMI]], czyli wyświetlania logo organizacji w skrzynce odbiorcy.

## Cytat

> „Rekordy DNS to nie glamour, ale to fundament, na którym spoczywa całe twoje email marketingowe — dostarczalność, reputacja nadawcy, nawet logo BIMI."

## Zastosowanie

Dla Piotra prowadzącego kampanie emailowe dla NGO znajomość SPF, DKIM i DMARC jest niezbędna zarówno do dbania o własną dostarczalność, jak i do wsparcia klientów w audycie ich konfiguracji. Narzędzie [[MXToolbox]] warto włączyć do listy zasobów w warsztatach z email marketingu i [[digital-campaigning]] dla organizacji społecznych. Zaostrzenie polityki DMARC do `reject` i konfiguracja [[BIMI]] to konkretne, praktyczne rekomendacje do przekazania organizacjom budującym profesjonalną komunikację emailową.
