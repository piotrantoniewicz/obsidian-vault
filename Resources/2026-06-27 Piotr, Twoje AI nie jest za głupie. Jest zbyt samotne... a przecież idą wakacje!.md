---
categories:
  - "Emails"
published: 2026-06-27
created: 2026-07-09
labels:
  - "Tomasz Woliński"
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "context-engineering"
---

# Piotr, Twoje AI nie jest za głupie. Jest zbyt samotne... a przecież idą wakacje!

Tomasz Woliński rozbiera cztery najczęstsze skargi na AI zebrane od czytelników newslettera i pokazuje, że żadna z nich nie jest wadą modelu — każda wynika z braku w systemie zbudowanym wokół AI (brak narzędzi do weryfikacji, brak zapisanej pamięci, brak podziału pracy, brak punktu zatrzymania na decyzję człowieka). Ilustruje to własnym agentem, który planował mu rodzinne wakacje. Do tego dorzuca konkretny quick win: trzy pliki `.md` (profil, firma, cele), które w 15 minut dają AI trwałą pamięć kontekstu zamiast tłumaczenia od nowa w każdej sesji.

## Frameworki i metody

Rozbiór: 4 rzeczy, które AI "psuje" — i recepta na każdą:

- **1. Zmyśla (brzmi pewnie, podaje bzdurę)** — model nie ma jak zweryfikować danych. Recepta: nie oczekuj mądrzejszego modelu, tylko daj mu narzędzia do sprawdzenia (mapa, baza, oficjalna strona) — wtedy agent nie zgaduje, tylko sprawdza u źródła.
- **2. Nie pamięta (tłumaczysz to samo w kółko)** — kontekst siedzi w głowie użytkownika, nie w systemie. Recepta: zapisz kontekst raz, w systemie ([[drugi mózg]]) — wtedy każdy agent korzysta z niego za darmo.
- **3. Robi średnią papkę (nie to, o co prosiłeś)** — jeden model dostaje zbyt wiele celów naraz i uśrednia wynik. Recepta: dekompozycja — mały zespół wyspecjalizowanych agentów pracujących równolegle bije jednego przeciążonego generalistę.
- **4. Wyrywa stery (robi za dużo na własną rękę)** — brak punktu, w którym system ma się zatrzymać i zapytać. Recepta: [[human-in-the-loop]] (HITL) na krytycznych krokach — AI proponuje, człowiek zatwierdza.

Quick Win tygodnia — pamięć i narzędzia w 15 minut:

- Zapisz raz do trzech plików: `profil.md` (kim jesteś, jak pracujesz), `firma.md` (co robisz, dla kogo, jak brzmisz), `cele.md` (co jest ważne teraz).
- Wrzucaj te pliki na start rozmowy zamiast tłumaczyć AI od zera — to pierwszy kamień systemu pamięci (recepta nr 2).
- Poziom wyżej: podłącz narzędzia przez [[MCP]] lub API (kalendarz, mail, baza, mapy) — wtedy AI przestaje zgadywać i zaczyna weryfikować (recepta nr 1).

## Wnioski

- Skargi na AI ("zmyśla", "nie pamięta", "robi papkę", "wyrywa stery") to niemal zawsze objaw braku w [[context-engineering|systemie wokół modelu]], nie wada samego modelu — a braki systemowe da się uzupełnić.
- Trzy proste pliki `.md` z profilem, kontekstem firmy i aktualnymi celami to tani, natychmiastowy sposób na budowanie trwałej pamięci AI bez dodatkowych narzędzi.
- Podział pracy na wyspecjalizowanych agentów działających równolegle daje głębsze, bardziej precyzyjne wyniki niż jeden model próbujący ogarnąć wszystko naraz.

## Zastosowanie

Bezpośrednio przekłada się na budowę własnego "drugiego mózgu" (Obsidian + Claude Cowork) oraz na projektowanie wdrożeń AI dla organizacji społecznych — te same cztery recepty (weryfikacja, pamięć, dekompozycja, HITL) tłumaczą się na checklistę do audytu procesów klienta przed wdrożeniem automatyzacji.
