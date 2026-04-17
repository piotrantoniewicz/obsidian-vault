---
categories:
  - Emails
published: 2026-02-01
created: 2026-03-18
labels:
  - Robert Szewczyk
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - LLM
---
# 🧠 czas na mózg agenta AI! [3/6]

Trzecia lekcja kursu budowania agentów AI w [[n8n]] dodaje do agenta dwa kluczowe komponenty: "mózg" (model językowy) i "pamięć". Krok 1: klucz API [[OpenAI]] Platform (uwaga: to osobne konto niż ChatGPT Plus — model pay-as-you-go, ~5 USD wystarczy na miesiąc testów). Krok 2: node "AI Agent" w n8n z modelem gpt-4.1-mini (szybki, tani, wystarczający na start) połączony z Telegram Trigger. Krok 3: "Simple Memory" z Session ID pobranym z Telegram — agent pamięta do 10-20 ostatnich wiadomości w kontekście rozmowy. Krok 4: zamknięcie pętli — node "Telegram: Send a text message" odsyłający odpowiedź agenta z powrotem do użytkownika. Efekt: w pełni działający agent konwersacyjny na Telegramie z pamięcią sesji, bez napisania ani jednej linii kodu.

## Wnioski
- Architektura Telegram Trigger → AI Agent (gpt-4.1-mini) → Simple Memory → Telegram Send to kompletny, działający wzorzec bota FAQ dla NGO — od złożenia zamówienia u darczyńcy po odesłanie spersonalizowanej odpowiedzi, wszystko zautomatyzowane przez [[n8n]] bez kodu.
- Klucz API [[OpenAI]] Platform (pay-as-you-go, oddzielny od subskrypcji ChatGPT) to ważna distinkcja w edukacji NGO — wiele organizacji myśli, że "mają ChatGPT" ale nie mają dostępu do API, co blokuje im możliwość budowania integracji.
- Parametr "Context Window Length" w Simple Memory (domyślnie 5, można zwiększyć do 10-20 wiadomości) to kluczowy element projektowania jakości rozmowy agenta — zbyt mały kontekst = "złota rybka", zbyt duży = wyższe koszty API; wartość warto dostosować do charakteru aplikacji.

## Cytat
> "Nie chcemy, aby nasz agent był złotą rybką — bez pamięci każde pytanie traktowałby jako zupełnie nową rozmowę, bez żadnego kontekstu."

## Zastosowanie
Piotr może zbudować demo agenta konwersacyjnego na [[Telegram]] dla klienta NGO: bot oparty na gpt-4.1-mini z pamięcią sesji odpowiadający na pytania darczyńców — proof of concept gotowy w ciągu jednego popołudniowego warsztatu z uczestnikami kursu.
