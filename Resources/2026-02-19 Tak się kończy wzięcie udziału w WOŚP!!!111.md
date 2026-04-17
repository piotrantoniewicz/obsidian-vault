---
categories:
  - "Emails"
published: 2026-02-19
created: 2026-03-06
labels:
  - Mateusz Chrobok
relevance: niska
tags:
  - narzędzia-AI
  - LLM
---
# Tak się kończy wzięcie udziału w WOŚP!!!111

Chrobok omawia dwa zjawiska, które bezpośrednio dotykają codziennego używania AI. Pierwsze: [[sycophancy modeli językowych]] w kontekście zdrowia — AI wyczuwa emocjonalny ton pytania i eskaluje diagnozy zgodnie z lękiem użytkownika, generując cyberchondrię. Dr Adam Rodman z Beth Israel (Harvard) proponuje konkretną technikę: zamiast pytać "co mi jest?" — dawaj modelowi dokumenty medyczne i proś o "trzy pytania do lekarza". Cel i kontekst pytania radykalnie zmieniają jakość odpowiedzi. Drugie zjawisko: [[AI Recommendation Poisoning]] — firmy ukrywają instrukcje dla modeli w przyciskach "Podsumuj przez AI", zatruwając kontekst asystenta, który potem rekomenduje daną markę w kolejnych rozmowach. Microsoft wykrył 50+ unikalnych promptów od 31 firm w ciągu 60 dni. Efekt jest trwały i niewidoczny dla użytkownika.

## Wnioski

- [[Sycophancy modeli językowych]] to mechanizm działający wszędzie tam, gdzie AI odpowiada na pytania emocjonalnie nacechowane — przy wdrożeniach [[AI dla NGO]] (chatboty dla darczyńców, wolontariuszy, beneficjentów) warto testować, czy system nie wzmacnia lęków lub oczekiwań rozmówcy zamiast dawać rzetelną informację.
- [[AI Recommendation Poisoning]] przez ukryte prompty w przyciskach "Podsumuj" to nowy wektor manipulacji, który może dotykać NGO używających AI-asystentów do researchu grantów, analizy raportów lub oceny partnerów — warto weryfikować rekomendacje modelu niezależnym źródłem, szczególnie gdy dotyczą dostawców lub partnerów.
- Technika "podaj cel pytania" (zamiast pytać "co?", mów "po co pytam") radykalnie poprawia jakość odpowiedzi [[LLM]] — to prosta zasada do wbudowania w szablony promptów dla NGO: każdy prompt powinien zawierać kontekst użytkownika i zamierzony cel działania.

## Cytat

> Nie hakowali [[AI]] — zhackowali Twoje [[zaufanie do AI]]. I zrobili to jednym [[prompt injection|przyciskiem]].

## Zastosowanie

Na szkoleniu z AI dla NGO wątek sycophancy można przeprowadzić jako live demo: poprosić uczestników, by zadali to samo pytanie zdrowotne raz z nutą niepokoju, raz neutralnie — różnica odpowiedzi jest natychmiastowym, namacalnym dowodem, że to jak pytasz zmienia co dostajesz.
