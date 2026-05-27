---
categories:
  - "Emails"
published: 2026-05-22
created: 2026-05-27
labels:
  - "Send It Right"
relevance: wysoka
tags:
  - "digital-campaigning"
  - "content-marketing"
  - "fundraising"
---

# Why Good Senders Still End Up on Blocklists

Lauren Meyer z Send It Right opisuje, jak przygotowanie do webinaru ze [[Spamhaus]] zmieniło jej podejście do diagnostyki dostarczalności — większość zespołów rozwiązuje problemy zbyt wąską metodą, skupiając się wyłącznie na treści i zachowaniu własnych kampanii. Tymczasem wokół programu mailowego istnieje cały ekosystem (wspólna infrastruktura, przejęte firmy, inne działy, Account Takeover), który wpływa na to, jak reputacja nadawcy jest postrzegana przez dostawców skrzynek. Dodatkowo tradycyjne metryki monitoringu — open rates (zniekształcone przez Apple MPP), seed tests, wskaźniki skarg — są coraz mniej wiarygodne, co tworzy fałszywe poczucie bezpieczeństwa. Problemy z dostarczalnością często narastają przez miesiące, zanim staną się widoczne — do tego czasu naprawa jest już trudna i kosztowna.

## Frameworki i metody

- **Rozszerzony model diagnostyki dostarczalności** — zamiast ograniczać się do pytań "czy zmieniliśmy treść?/wolumen?/zaangażowanie?", należy zbadać sześć dodatkowych obszarów: (1) wspólna infrastruktura IP/domen i sąsiedzi w puli, (2) inne działy/systemy/dostawcy mający dostęp do programu mailowego, (3) podejrzana aktywność (Account Takeover, niespodziane wolumeny), (4) przekierowania i pośrednie serwery mail zaburzające uwierzytelnienie, (5) fałszywe poczucie kontroli z dashboardów, (6) skumulowane problemy narastające przez miesiące
- **Weryfikacja sygnałów monitoringu** — open rates (zniekształcone przez [[Apple]] MPP), seed tests (wartość kierunkowa, nie faktyczna), wskaźniki skarg (tylko zmotywowani użytkownicy), spam trapy (wskaźniki opóźnione, lagging) — wszystkie nadal przydatne, ale nie mogą być traktowane jako pełny obraz rzeczywistości; [[Google Postmaster Tools]] jako jedno z nielicznych miejsc, gdzie dostawcy skrzynek ujawniają sygnały reputacji nadawcy
- **Diagnostyka skumulowanych problemów** — "nic nie zmieniliśmy" może być technicznie prawdą, ale problemy budują się stopniowo: degradacja listy, spadające zaangażowanie, luzowanie standardów pozyskiwania subskrybentów, stare systemy żyjące zbyt długo, odziedziczone praktyki po przejęciach firm

## Wnioski

- Nowoczesne systemy filtrowania [[Google]] i [[Yahoo]] oceniają wzorce w całym ekosystemie — infrastruktura, historia zachowań, środowisko reputacyjne — nie tylko zgodność bieżącej kampanii z best practices, co oznacza, że nadawca może robić wszystko "dobrze" i nadal mieć problem
- Tradycyjne metryki dostarczalności stały się mniej wiarygodne: [[Apple]] MPP zniekształca open rates, seed tests nie odzwierciedlają konsekwentnie doświadczenia realnych użytkowników, a wskaźniki skarg rejestrują tylko ułamek faktycznych negatywnych reakcji
- Problem z dostarczalnością zazwyczaj zaczyna się miesiące wcześniej, zanim stanie się widoczny — co sprawia, że organizacje działające reactywnie (czekające na alert) mają znacznie trudniejszą i kosztowniejszą naprawę niż te monitorujące długoterminowe trendy

## Cytat

> "Do czasu gdy większość organizacji zauważy problem, warunki, które do niego doprowadziły, mogą istnieć od miesięcy." — Lauren Meyer

## Zastosowanie

Przy pracy z NGO nad kampaniami mailingowymi warto wdrożyć monitoring długoterminowych trendów reputacji domeny w [[Google Postmaster Tools]], a nie tylko metryki kampanijne. Organizacje po fuzjach lub zmianach platform powinny audytować odziedziczone listy i praktyki wysyłania zanim zauważą problemy. W kursie "Fundraising z AI" warto poświęcić osobny moduł świadomości ekosystemowej dostarczalności — "robię wszystko dobrze" to za mało, jeśli nie wiesz, kto dzieli z tobą infrastrukturę wysyłkową.
