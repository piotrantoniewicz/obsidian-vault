---
categories:
  - Emails
published: 2026-02-04
created: 2026-03-18
labels:
  - Robert Szewczyk
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - szkolenia-AI
---
# FINAŁ! 🏆 Agent zaczyna pracować dla Ciebie [6/6]

Finałowa lekcja kursu budowania agentów AI w [[n8n]] łączy wszystkie elementy w działający system. Kluczowy koncept: wyrażenia `$fromAI("fieldName", "description")` — zamiast stałych wartości agent AI dynamicznie uzupełnia pola narzędzi (adres odbiorcy, temat, treść maila, daty wydarzeń) na podstawie rozmowy przez Telegram. Fazy: (1) konfiguracja narzędzia Gmail z dynamicznymi polami To/Subject/Message; (2) narzędzie Google Calendar "Create Event" z dynamicznymi polami Start/End/Summary/Description; (3) ustawienie strefy czasowej w n8n (Warszawa); (4) zmiana nazw narzędzi na "Send mail" i "Create Event" dla czytelności System Promptu; (5) dodanie finalnego System Promptu opisującego dostępne narzędzia. Ważna zasada: każda akcja Google Workspace (wysyłanie maili, odczytywanie, tworzenie wydarzeń) = osobne narzędzie (tool) podpięte do agenta.

## Wnioski
- Wyrażenia `$fromAI()` w [[n8n]] to klucz do budowania dynamicznych agentów — zamiast twardych wartości agent sam interpretuje kontekst rozmowy i wypełnia pola API, co eliminuje konieczność tworzenia osobnych workflow dla każdego wariantu zadania.
- Zasada "każda akcja Google Workspace = osobne narzędzie" wymaga starannego planowania architektury agenta przed wdrożeniem — dla NGO obsługującego wiele procesów (email, kalendarz, Drive, Sheets) lista narzędzi może szybko rosnąć, co wpływa na jakość System Promptu.
- Nazwanie narzędzi semantycznie ("Send mail", "Create Event") zamiast pozostawienia domyślnych nazw technicznych jest kluczowe dla jakości System Promptu — agent rozumie, kiedy użyć "Send mail", a nie "Gmail Tool v2 credential 3".

## Cytat
> "Teraz nie musisz wpisywać adresu odbiorcy — możesz powiedzieć agentowi 'wyślij maila do przyklad@przyklad.com', a on sam wprowadzi wskazany adres, wybierze narzędzie i wyśle wiadomość."

## Zastosowanie
Piotr może użyć tego finalnego wzorca (Telegram → Agent AI → Gmail + Google Calendar) jako demonstracji "żywego demo" na szkoleniu dla NGO — w 20 minut pokazując, jak zbudować asystenta zarządzającego korespondencją i harmonogramem bez linii kodu.
