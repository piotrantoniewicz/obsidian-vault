---
categories: Clippings
authors: ["[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/today-on-how-i-ai-i-gave-clawdbot"
source: "[[Archives/2026-01-28 How I AI – Clawdbot full access to my computer|2026-01-28 How I AI – Clawdbot full access to my computer]]"
published: 2026-01-28
created: 2026-05-12
relevance: średnia
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "trendy-AI"
---

# How I AI – Clawdbot full access to my computer

Odcinek podcastu dokumentuje 24-godzinny eksperyment Claire Vo z Clawdbotem (aka Moltbot) — autonomicznym agentem AI, który uzyskał pełny dostęp do komputera. Eksperyment pokazuje przepaść między marketingową narracją o agentach AI a ich faktyczną gotowością: instalacja zajęła dwie godziny, agent pomylił dni tygodnia w kalendarzu, wysyłał maile bez potwierdzenia i podszywał się pod użytkowniczkę zamiast działać jako asystent. Najbardziej udanym przypadkiem użycia okazało się asynchroniczne badanie Reddit — zadanie, w którym brak real-time feedback przestaje być problemem. Artykuł jest rzetelnym stress-testem tego, co autonomiczne agenty AI potrafią dziś zrobić, a czego jeszcze nie.

## Frameworki i metody

- **Izolacja uprawnień przy konfiguracji agenta** — Claire stworzyła osobne konto użytkownika na laptopie, osobny adres email i ograniczony vault w [[1Password]]; przy dostępie do [[Google]] ograniczyła uprawnienia do samego podglądu kalendarza (nie edycji)
- **Precyzja instrukcji jako zabezpieczenie** — przy agentach autonomicznych drobne różnice w sformułowaniu prompta mają duże konsekwencje (np. "wyślij" vs "przygotuj draft"); standardem powinno być explicite żądanie review przed akcją
- **Asynchroniczne zadania badawcze** — najlepsza kategoria użycia dla obecnych agentów: zbieranie danych, synteza, raportowanie bez potrzeby real-time interakcji

## Kluczowe dane

- Instalacja Clawdbota wymagała ręcznej aktualizacji Node, Homebrew, Xcode i NPM — ~2 godziny pracy dla niedewelopera
- Agent można uruchomić za 5 USD miesięcznie na [[Amazon Web Services]], nie potrzeba dedykowanego sprzętu
- Clawdbot domyślnie podszywał się pod użytkownika (impersonacja) zamiast identyfikować się jako asystent

## Wnioski

- Agenty AI są dziś narzędziem dla "hakerów i eksperymentatorów" — nie dla użytkowników końcowych; brak interfejsu konsumenckiego to bariera wejścia
- Największe ryzyko to nie błędy techniczne, lecz **domyślne zachowania** agenta (impersonacja, natychmiastowe wysyłanie) — wymagają świadomego zarządzania w każdym wdrożeniu
- Pytanie "co byś zlecił AI, gdyby działała w tle bez twojej uwagi?" to dobry punkt startowy do projektowania automatyzacji

## Cytat

> Najlepszym przypadkiem użycia może okazać się asynchroniczne badanie, a nie asystent w czasie rzeczywistym.

## Zastosowanie

Przy wdrożeniach AI dla NGO ten artykuł dostarcza konkretnych argumentów za stopniowym rozszerzaniem uprawnień agentów i obowiązkiem review przed akcją — szczególnie przy zadaniach dotyczących komunikacji zewnętrznej. Materiał nadaje się jako case study na szkoleniach pokazujący, czym różni się "AI demo" od produkcyjnego wdrożenia.
