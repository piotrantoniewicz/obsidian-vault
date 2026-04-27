---
categories: Clippings
authors: ["[[Brian Godiksen]]"]
url: https://www.socketlabs.com/blog/google-postmaster-tools/
source: "[[Archives/2024-03-15 Guide to Check Your Domain Reputation|2024-03-15 Guide to Check Your Domain Reputation]]"
published: 2024-03-15
created: 2026-04-27
relevance: średnia
tags:
  - "digital-campaigning"
  - "fundraising"
---

# Guide to Check Your Domain Reputation with Google Postmaster Tools

[[Google Postmaster Tools]] (GPT) to bezpłatne narzędzie Google umożliwiające nadawcom emaili monitorowanie kluczowych metryk dostarczalności — reputacji domeny i IP, wskaźnika spamu, błędów dostarczania, uwierzytelnienia i szyfrowania. Artykuł szczegółowo opisuje konfigurację GPT przez weryfikację DNS, interpretację czterech progów reputacji (High, Medium, Low, Bad) oraz zasady dzielenia dostępu z członkami zespołu. GPT raportuje dane zagregowane z jednodniowym opóźnieniem, co czyni go narzędziem do śledzenia trendów, a nie oceny pojedynczych kampanii. Kluczowa obserwacja: reputacja domeny — nie IP — jest najważniejszym czynnikiem wpływającym na dostarczalność do skrzynki [[Gmail]], a wszystkie strumienie mailowe (transakcyjne, marketingowe, newslettery) agregują się do tej samej reputacji domeny.

## Kluczowe dane
- Dane w GPT generują się dla domen wysyłających ok. 100+ wiadomości dziennie do unikalnych użytkowników @gmail.com
- Adresy Google Workspace (dawne G Suite) nie są wliczane do metryk GPT
- Reputacja IP "Bad" = praktycznie brak dostarczalności; "Medium" osiąga ok. 17% unikalnych otwarć wg badań SocketLabs

## Wnioski
- Reputacja domeny jest ważniejsza niż reputacja IP w decyzjach filtrów spamu [[Gmail]] — każda kampania email agreguje się do tej samej oceny domeny i wpływa na dostarczalność wszystkich wysyłek.
- Nie wolno usuwać weryfikacyjnego rekordu DNS po konfiguracji GPT — Google co miesiąc sprawdza jego obecność i odbiera dostęp przy jego braku, co oznacza utratę widoczności problemu.
- GPT posiada API umożliwiające automatyczne monitorowanie metryk dostarczalności — otwiera to możliwość integracji np. przez [[Make.com]] do alertów przy spadku reputacji.

## Zastosowanie
Przy prowadzeniu kampanii emailowych (fundraising, advocacy, newslettery) dla organizacji warto skonfigurować [[Google Postmaster Tools]] dla własnej domeny wysyłkowej, by wcześnie wykrywać problemy z dostarczalnością — narzędzie jest bezpłatne i dostarcza danych niewidocznych w standardowych statystykach ESP. Możliwość połączenia GPT z automatyzacją przez API pozwala budować system wczesnego ostrzegania, szczególnie wartościowy przy intensywnych kampaniach fundraisingowych, gdzie każdy mail musi dotrzeć do inbox.