---
categories: Clippings
authors: ["[[Krzysztof Bohaczyk]]"]
url: https://www.youtube.com/watch?v=HRjgA_6lgaA
source: "[[Archives/2026-04-24 5 komend Claude Code, o których nie wiesz (a warto)|2026-04-24 5 komend Claude Code, o których nie wiesz (a warto)]]"
published: 2026-04-24
created: 2026-05-01
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "prompt-engineering"
---

# 5 komend Claude Code, o których nie wiesz (a warto)

Film Krzysztofa Bohaczyka prezentuje pięć rzadko znanych komend [[Claude Code]], które realnie usprawniają codzienną pracę z tym narzędziem. Autor skupia się na praktycznych zastosowaniach — od czystego kopiowania treści z terminala, przez pytania poboczne bez przerywania pracy agenta, po tryb głosowy, analizę własnych sesji i hybrydowy model doradczy. Szczególnie wartościowa jest architektura `/advisor`, gdzie tańszy [[Sonnet]] wykonuje pracę, a droższy [[Opus]] pełni rolę doradcy — co według benchmarków [[Anthropic]] daje lepsze wyniki przy niższych kosztach. Film jest oparty na konkretnych demonstracjach i zawiera dane porównawcze z testów wydajności.

## Frameworki i metody

Pięć komend Claude Code wartych wdrożenia:

- **`/copy`** — kopiuje odpowiedź Claude'a do schowka bez formatowania terminalowego (numerów linii, wcięć, spacji). Można wskazać numer wiadomości (np. `/copy 2`). Przy odpowiedziach zawierających kod oferuje interaktywny wybór: cała odpowiedź lub sam kod. Od wersji 2.1.3 poprawnie wyrównuje kolumny tabel Markdown.
- **`/btw`** — zadaje poboczne pytanie agentowi bez przerywania głównego wątku pracy. Działa wyłącznie na bazie pamięci sesji (brak dostępu do nowych plików ani skryptów), nie wpływa na kontekst agenta. Używa cache kontekstu — odpowiedź pojawia się niemal natychmiast.
- **`/voice`** — włącza tryb głosowy obsługujący 20 języków, w tym polski (konfiguracja przez `/config` → language → `pl`). Domyślnie przetwarza audio na serwerach [[Anthropic]]; alternatywą z zachowaniem prywatności jest lokalne narzędzie Voicing z modelem Parakeet (Nvidia).
- **`/insights`** — generuje raport HTML z analizy historii sesji Claude Code: projekty, liczba sesji, najczęściej używane narzędzia, język programowania, co szło nie tak i konkretne rekomendacje do pliku `CLAUDE.md`. Zalecane uruchamianie co kilka miesięcy.
- **`/advisor`** — konfiguruje model doradczy (np. [[Opus]]) działający równolegle z modelem wykonawczym ([[Sonnet]]). Advisor współdzieli kontekst, ale nie edytuje plików — jedynie doradza, gdy executor zgłosi potrzebę. Wzorzec: Sonnet jako junior developer, Opus jako senior doradca.

## Kluczowe dane

- [[Sonnet]] solo na teście SWE Bench: **72,1%**
- [[Sonnet]] + [[Opus]] jako advisor: **~75%**, przy **12% niższym koszcie** niż Sonnet działający solo (mniej iteracji dzięki poradom Opusa)

## Wnioski

- Komenda `/advisor` to praktyczna implementacja wzorca "junior-senior" w pracy agentowej — optymalizuje stosunek jakości do kosztu bez rezygnacji z mocy najlepszego modelu
- `/insights` to unikalna możliwość autorefleksji nad własnym sposobem pracy z [[Claude Code]] — wnioski warto przenosić bezpośrednio do `CLAUDE.md`, by stale poprawiać jakość sesji
- `/btw` rozwiązuje realny problem wielozadaniowości: pozwala weryfikować stan agenta w trakcie długiej sesji bez anulowania pracy i bez otwierania nowego terminala

## Zastosowanie

Dla Piotra, korzystającego intensywnie z [[Claude Code]] i Cowork, komendy `/advisor` i `/insights` mają największą wartość operacyjną — mogą podnieść jakość pracy agentowej i dostarczyć wglądu w własne nawyki z AI. Komenda `/btw` jest szczególnie użyteczna przy długich automatyzacjach, gdy pojawia się potrzeba szybkiej weryfikacji bez przerywania workflow. Warto też przetestować `/voice` z językiem polskim do dyktowania promptów zamiast pisania z klawiatury.
