---
categories: Clippings
authors: ["[[Mateusz Wojdalski]]"]
url: https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/claude-md-karpathy-78k-gwiazdek-claude-code-2026/?utm_source=newsletter&utm_medium=email&utm_term=2026-04-29&utm_campaign=Copilot+na+liczniku+GPT-5+5+i+65+mld+dla+Anthropic
source: "[[Archives/2026-04-24 Plik CLAUDE.md z 81 tysiącami gwiazdek - zasady Karpathy ego dla Claude Code|2026-04-24 Plik CLAUDE.md z 81 tysiącami gwiazdek - zasady Karpathy ego dla Claude Code]]"
published: 2026-04-24
created: 2026-04-29
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "prompt-engineering"
  - "context-engineering"
---

# Plik CLAUDE.md z 81 tysiącami gwiazdek — zasady Karpathy'ego dla Claude Code

Artykuł opisuje fenomen pliku CLAUDE.md autorstwa Forresta Changa, opartego na obserwacjach [[Andrej Karpathy|Andreja Karpathy'ego]], który zebrał 81 tysięcy gwiazdek na GitHubie w zaledwie tydzień. Plik zawiera cztery zasady dla [[Claude Code]], które eliminują typowe problemy z automatycznym kodowaniem: zgadywanie zamiast pytania, nadmierną złożoność kodu, niepotrzebne modyfikacje cudzych plików i brak weryfikowalnych celów. Autor tłumaczy, jak zainstalować plik i dostosować go do własnych projektów, ale też precyzuje, czego cztery zasady nie rozwiązują — oceny, czy dane rozwiązanie w ogóle warto budować.

## Frameworki i metody

Cztery zasady Karpathy'ego dla [[Claude Code]]:

- **Think Before Coding** — nie zgaduj, nie ukrywaj wątpliwości, ujawniaj kompromisy. Model ma pytać o intencje użytkownika zanim napisze kod.
- **Simplicity First** — minimum kodu rozwiązującego problem, bez abstrakcji na zapas, bez konfigurowalności „na wypadek". Jeśli doświadczony inżynier powie, że to przekombinowane — to przekombinowane.
- **Surgical Changes** — modyfikuj tylko to, o co poproszono. Nie poprawiaj formatowania, cudzych pętli ani „podejrzanych" sąsiednich plików bez zgody.
- **Goal-Driven Execution** — definiuj weryfikowalne kryterium sukcesu (np. testy, które mają przejść), a nie konkretne kroki. Model iteruje sam aż do spełnienia kryterium.

## Kluczowe dane

- 81 500 gwiazdek na GitHubie w tydzień od publikacji
- 5 828 gwiazdek w jednym dniu (13 kwietnia 2026) — drugie najczęściej gwiazdkowane repozytorium na platformie tamtego dnia
- Plik ma ~70 linii — celowo krótki, by nie zajmować zbyt dużo miejsca w oknie kontekstu

## Wnioski

- Plik CLAUDE.md to najskuteczniejszy sposób na kontrolowanie domyślnego zachowania [[Claude Code]] w projektach — czytany automatycznie przy każdej sesji, działa jak onboarding dla modelu, niezależnie od używanej wersji (Haiku, Sonnet, Opus).
- Zasady Karpathy'ego redukują nadgorliwość AI (zgadywanie, przekombinowanie, nieproszone zmiany), ale nie zastępują oceny, czy warto dany problem w ogóle rozwiązywać kodem — to osobna warstwa wymagająca osobnych reguł.
- Popularność prostego pliku tekstowego pokazuje, że problem z AI w kodowaniu nie leży w mocy modeli, lecz w jakości instrukcji — to obszar [[context-engineering]], nie tylko [[prompt-engineering]].

## Cytat

> Trudno o lepszy dowód, że problem z kodowaniem przez AI nie leży w mocy modeli, tylko w instrukcji, jaką im dajemy.

## Zastosowanie

Piotr może zainstalować plik CLAUDE.md globalnie w [[Claude Code]] przez `/plugin install andrej-karpathy-skills@karpathy-skills` i dopisać pod zasadami Karpathy'ego własne konwencje projektowe — to natychmiastowa poprawa jakości wdrożeń AI. Przy budowaniu własnych pluginów do [[Claude Code]] zasada Think Before Coding bezpośrednio przekłada się na lepsze skille i komendy, które pytają o intencje zamiast zgadywać. Cztery zasady stanowią też gotowy materiał dydaktyczny na szkoleniach z AI dla NGO — konkretny przykład tego, jak instrukcja dla modelu kształtuje jakość jego pracy.
