---
categories: Clippings
authors: ["[[Colin Matthews]]"]
url: https://www.lennysnewsletter.com/p/chatgpt-apps-are-about-to-be-the
source: "[[Archives/2026-01-20 ChatGPT apps are about to be the next big distribution channel Here s how to build one|2026-01-20 ChatGPT apps are about to be the next big distribution channel Here s how to build one]]"
published: 2026-01-20
created: 2026-05-12
relevance: średnia
tags:
  - "narzędzia-AI"
  - "trendy-AI"
---

# ChatGPT apps are about to be the next big distribution channel. Here's how to build one.

[[Colin Matthews]] opisuje ChatGPT apps jako nowy kanał dystrybucji — analogiczny do App Store z 2008 roku — gdzie interaktywne widżety firm trzecich pojawiają się bezpośrednio w konwersacji z [[ChatGPT]], pozwalając użytkownikom działać bez opuszczania interfejsu czatu. Mechanizm działa przez [[MCP]] (Model Context Protocol) i umożliwia wyświetlanie kart inline, trybu pełnoekranowego lub obrazu-w-obrazie. Kluczowa przewaga dystrybucyjna polega na kontekstowym wyświetlaniu aplikacji: użytkownik nie szuka aplikacji, lecz wyraża intencję, a model sam sugeruje właściwe narzędzie. Artykuł zawiera szczegółowy przewodnik budowania pierwszej aplikacji przez [[Replit]] lub dedykowane narzędzie Chippy, z prostym backend MCP i widżetem React.

## Frameworki i metody

- **Architektura ChatGPT app** — trzy elementy: (1) konwersacja w ChatGPT, (2) "tools" — backend MCP definiujący funkcje, (3) widżet React renderowany w sandboxie; ChatGPT orkiestruje całość
- **Wersjonowanie przez agency** — [[Colin Matthews]] sugeruje wzorzec: najpierw inline cards (mała autonomia), potem fullscreen workflows, na końcu transakcje autonomiczne
- **Tool description jako nowe SEO** — opis narzędzia w MCP decyduje, kiedy ChatGPT zasugeruje aplikację; im trafniejszy opis, tym lepsza "widoczność" w konwersacjach użytkowników

## Kluczowe dane

- Partnerzy ChatGPT apps: Adobe, DoorDash, Canva, Figma, Booking.com, Coursera, Expedia, Spotify, Zillow
- Czas budowy prostej aplikacji (search + display): 1–2 dni dla znających stack
- Platforma ChatGPT: 800 milionów użytkowników

## Wnioski

- [[MCP]] staje się de facto standardem łączenia aplikacji z asystentami AI — warto rozumieć ten protokół nawet bez budowania własnych aplikacji
- Mechanizm dystrybucji oparty na intencji użytkownika to fundamentalna zmiana: zamiast aktywnie szukać narzędzia, użytkownik otrzymuje je kontekstowo w toku rozmowy
- Dla organizacji non-profit — potencjał w tworzeniu prostych aplikacji do zbierania zapisów, formularzy donacji czy chatbotów fundraisingowych wbudowanych w ChatGPT

## Zastosowanie

Wiedza o architekturze [[MCP]] i ChatGPT apps przydaje się w kontekście wdrożeń AI dla NGO — pozwala ocenić, kiedy warto budować własne integracje zamiast korzystać z gotowych narzędzi. Może też być tematem na szkolenia z [[narzędzia-AI]] dla bardziej zaawansowanych klientów zainteresowanych automatyzacją. Warto śledzić ten ekosystem jako potencjalny kanał dystrybucji kampanii i działań [[digital-campaigning]].
