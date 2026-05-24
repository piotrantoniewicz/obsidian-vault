---
categories:
  - Emails
published: 2026-02-03
created: 2026-03-18
labels:
  - Robert Szewczyk
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - szkolenia-AI
---
# Agent AI przejmuje Twój kalendarz 🗓️ [5/6]

Piąta lekcja kursu n8n poświęcona jest integracji agenta z Google Calendar i Gmail przez OAuth — najważniejszy technicznie krok całego kursu. Trzy fazy: (1) Google Cloud Console — tworzenie projektu, włączenie Google Calendar API i Gmail API; (2) konfiguracja OAuth — ekran zgody, dodanie siebie jako "użytkownik testowy" (krok krytyczny!), wygenerowanie Client ID i Client Secret; (3) połączenie w [[n8n]] — wklejenie Authorization URL (`accounts.google.com/o/oauth2/v2/auth`), Access Token URL (`oauth2.googleapis.com/token`), Client ID i Client Secret, następnie "Sign in with Google". Ten sam proces powtarzany dla Gmaila. Efektem jest agent z dostępem do kalendarza i skrzynki mailowej przez autoryzowane API. To jedyna lekcja wymagająca skupienia technicznego — reszta jest intuicyjna.

## Wnioski
- Wzorzec "Google Cloud Console → OAuth → n8n Credential" jest standardowym protokołem integracji Google z dowolnym narzędziem automatyzacji — Piotr może używać tej samej procedury do podłączania Google Workspace (Docs, Sheets, Drive) do [[n8n]] w projektach dla NGO.
- Krok "dodaj siebie jako użytkownika testowego w OAuth" jest często pomijanym detalem, który blokuje całą integrację — warto go wyodrębnić jako osobny checkpoint przy projektowaniu szkoleń z [[n8n]] dla NGO, aby uniknąć frustracji uczestników.
- Dostęp agenta AI do Gmail przez OAuth otwiera możliwość budowania asystenta obsługującego korespondencję fundraisingową — np. kategoryzowanie zapytań darczyńców, drafty odpowiedzi lub powiadomienia o nowych wiadomościach przez Telegram.

## Cytat
> "Musimy stworzyć 'cyfrowy dowód osobisty' dla naszej aplikacji — dzięki OAuth Google wie, kogo wpuszcza do Twoich danych, a Ty zachowujesz pełną kontrolę nad dostępem."

## Zastosowanie
Piotr może zastosować ten wzorzec integracji Google OAuth w projektach dla NGO, gdzie agent AI zarządza kalendarzem spotkań z darczyńcami lub automatycznie odpowiada na maile z pytaniami o kampanię — gotowy tutorial do adaptacji na warsztat praktyczny.
