---
categories: Clippings
authors: "[[Aakash Gupta]]"
url: https://www.news.aakashg.com/p/context-engineering
source: "[[2025-11-26 The Ultimate Guide to Context Engineering for PMs]]"
published: 2025-11-26
created: 2026-03-03
relevance: wysoka
tags:
  - prompt-engineering
  - LLM
  - narzędzia-AI
---

# The Ultimate Guide to Context Engineering for PMs

Context engineering to dyscyplina polegająca na precyzyjnym dobieraniu informacji trafiających do okna kontekstowego modelu językowego — i według autora jest ważniejsza niż wybór samego modelu. [[LLM]]-y nie inferują kontekstu automatycznie: nie wiedzą kim jest użytkownik, co robił chwilę temu, jakie dokumenty są istotne ani jakie reguły obowiązują w danym systemie. Autor na przykładzie asystenta mailowego [[Apollo]] pokazuje, że każda dodatkowa warstwa kontekstu (wątek → CRM → ton marki → historia relacji) radykalnie podnosi jakość outputu — od ogólnikowego do gotowego do wysyłki. Przewaga konkurencyjna [[Cursor]] nad innymi narzędziami do kodowania leży właśnie w warstwie kontekstu, nie w samym modelu — co Google wycenił na 2,4 mld dolarów, kupując [[Windsurf]].

## Frameworki i metody

- **Warstwowy kontekst dla asystenta mailowego** — ilustracja tego jak kolejne warstwy kontekstu transformują jakość outputu:
  1. Tylko ostatnia wiadomość → output ogólny
  2. Cały wątek mailowy → output spójny
  3. Wątek + notatki z [[CRM]] → output spersonalizowany
  4. Wątek + CRM + ton marki → output zgodny z wizerunkiem
  5. Wątek + CRM + ton + kontekst relacji → output gotowy do wysyłki

- **6 warstw kontekstu dla PM** — co LLM musi otrzymać explicite: tożsamość użytkownika, historia działań, istotne dokumenty, dane systemowe, reguły biznesowe, relacje między encjami w workspace'ie

## Kluczowe dane
- [[Cursor]] osiągnął 1 mld USD ARR dzięki warstwie kontekstu, nie jakości modelu
- [[Google]] zapłacił 2,4 mld USD za [[Windsurf]] zamiast konkurować z Cursor'em

## Wnioski
- Jakość outputu [[LLM]] zależy przede wszystkim od jakości i kompletności kontekstu — nie od wyboru modelu; zmiana modelu bez poprawy kontekstu rzadko cokolwiek zmienia
- [[Cursor]] zbudował przewagę rynkową przez lepszą warstwę indeksowania i wyszukiwania kontekstu — to wzorzec dla każdego narzędzia AI, które chce być trudne do zastąpienia
- Context engineering to kompetencja PM-owska, nie inżynierska — decyzje o tym co trafia do kontekstu powinny wynikać ze zrozumienia użytkownika i produktu

## Cytat
> „Warstwa kontekstu to fosa obronna — przewaga, której sama jakość modelu nie jest w stanie odtworzyć."

## Zastosowanie
Przy budowaniu pluginów i narzędzi AI dla NGO warto inwestować w precyzyjne definiowanie kontekstu — profile organizacji, dane projektowe, instrukcje systemowe — zamiast szukać mocniejszego modelu.
