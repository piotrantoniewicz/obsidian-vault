---
categories:
  - "Emails"
published: 2026-06-30
created: 2026-07-09
labels:
  - "Send It Right"
relevance: średnia
tags:
  - "digital-campaigning"
  - "fundraising"
  - "content-marketing"
---

# Send It Right: Why Your Email Needs Sunscreen

Lauren Meyer wyjaśnia w przystępny sposób trzy protokoły uwierzytelniania poczty — SPF, DKIM i DMARC — i tłumaczy, dlaczego bez nich mail od 2024 roku po prostu nie wejdzie do skrzynek Google, Yahoo czy Microsoftu. Autentykacja chroni reputację nadawcy przed spoofingiem i phishingiem, a jej brak może z dnia na dzień zawalić dostarczalność, nawet jeśli wcześniej wszystko działało bez problemu. Autorka podkreśla, że wdrożenie DMARC powinno przebiegać fazowo — od monitoringu, przez kwarantannę, do pełnego odrzucania niepoprawnie uwierzytelnionej poczty — żeby nie zablokować własnych legalnych wysyłek.

## Frameworki i metody
- **SPF (Sender Policy Framework)** — publikacja listy adresów IP/serwerów uprawnionych do wysyłki z danej domeny; mail z nieautoryzowanego IP dostaje status „fail".
- **DKIM (DomainKeys Identified Mail)** — podpis kryptograficzny pozwalający serwerowi odbiorcy sprawdzić, czy treść maila nie została zmieniona w tranzycie.
- **DMARC (Domain-based Message Authentication, Reporting and Conformance)** — nadbudowany na SPF i DKIM, informuje dostawców skrzynek co robić z mailem, który nie przechodzi weryfikacji, i alarmuje o próbach podszywania się pod domenę.
- **Fazowe wdrażanie DMARC** — faza 1: `p=none` (tylko monitoring i raporty błędów, minimum kilka tygodni); faza 2: `p=quarantine` (podejrzana poczta trafia do kwarantanny/spamu); faza 3: `p=reject` (poczta niezgodna z rekordem jest odrzucana na starcie). Pomijanie wcześniejszych faz grozi zablokowaniem własnej, legalnej poczty.
- **Segmentacja domen/subdomen wg typu wysyłki** — rozdzielenie newsletterów, maili transakcyjnych i sprzedażowych na subdomeny chroni główny rekord SPF przed przekroczeniem limitu 10 zapytań DNS.

## Kluczowe dane
- Według Yahoo ok. 95% poczty, którą odbierają dostawcy skrzynek każdego dnia, to phishing, malware i inny spam — tylko ok. 5% to legalna poczta.
- Przykład z branży: domena bez poprawnej autentykacji zobaczyła spadek open rate w Gmailu z 55% do 5% z dnia na dzień, gdy Google zaczął kierować jej maile do spamu.

## Wnioski
- SPF, DKIM i DMARC są od 2024 roku wymogiem u głównych dostawców skrzynek (Google, Yahoo, Microsoft) — bez nich mail nie ma szans na [[deliverability]], niezależnie od jakości treści.
- Wdrażanie DMARC fazowo (monitoring → kwarantanna → odrzucanie) chroni przed przypadkowym zablokowaniem własnej poczty i pozwala wychwycić błędy konfiguracji, zanim zaczną szkodzić dostarczalności.
- Rozdzielenie typów wysyłki na subdomeny (newsletter, transakcyjne, sprzedażowe) to proste zabezpieczenie przed przeciążeniem rekordu SPF i utratą kontroli nad tym, kto wysyła w imieniu domeny.

## Cytat
> Dostarczalność, na którą zasługujesz, zależy od tego, jak uwierzytelnisz swoją domenę.

## Zastosowanie
Przed uruchomieniem kampanii mailowych dla klientów (np. kursu „Fundraising z AI" czy kampanii dla organizacji społecznych) warto zweryfikować konfigurację SPF/DKIM/DMARC domeny wysyłkowej — błędna autentykacja może z dnia na dzień zrujnować dostarczalność całej kampanii.
