---
categories:
  - Clippings
authors: ["[[Procesy Jutra]]"]
url: "https://www.youtube.com/watch?v=QFBWr-5Aw_4"
source: "[[Archives/2026-06-29 Jak zacząć automatyzację w firmie? Które procesy warto usprawnić? Brunka&Aniserowicz Procesy Jutra|2026-06-29 Jak zacząć automatyzację w firmie? Które procesy warto usprawnić? Brunka&Aniserowicz Procesy Jutra]]"
published: 2026-06-29
created: 2026-06-30
relevance: wysoka
tags:
  - "automatyzacja"
  - "strategia-AI"
  - "szkolenia-AI"
---

# Jak zacząć automatyzację w firmie? Które procesy warto usprawnić? Brunka&Aniserowicz Procesy Jutra

Webinar Mikołaja Brunki (Procesy Jutra / agencja automatyzacji) o świadomym podejściu do automatyzacji w firmie. Główna teza: większość firm błędnie zaczyna od narzędzia, a powinna zaczynać od celu — potem dobierać dział, proces i dopiero narzędzie. Framework "lejka wyboru" prowadzi od celu biznesowego przez cztery kryteria selekcji procesu do pierwszej automatyzacji. Kluczowa przestroga oparta na prawdziwym case study: automatyzowanie chaosu prowadzi do zautomatyzowanego chaosu — organizacja, która "wdrożyła AI" bez przygotowania, skończyła z botem obiecującym rabaty i robiącym zwroty bez autoryzacji.

## Frameworki i metody

**Framework lejka wyboru — od celu do narzędzia:**

1. **Cel** — co chcemy osiągnąć?
   - Odzyskanie czasu zespołu (mniej ręcznej pracy, powtarzalne zadania)
   - Większa sprzedaż (szybszy czas reakcji na leady, powtarzalny proces)
   - Standaryzacja (mniej błędów, koniec z pomyłkami w fakturach i zamówieniach)
   - Niższe koszty operacyjne / szybsza obsługa klienta

2. **Dział** — z którego celu wynika obszar: marketing, sprzedaż, obsługa klienta, administracja/finanse, HR

3. **Jeden proces** — wybierz po czterech kryteriach:
   - Co denerwuje zespół? (niewidoczna, powtarzalna robota, której nikt nie chce robić)
   - Co daje dźwignię przychodową? (ofertowanie, follow-upy, reaktywacja klientów)
   - Co nam zabiera pieniądze? (błędy, reklamacje, pomyłki w fakturach, przeprosiny)
   - Co zjada czas? (czynność z największą liczbą godzin miesięcznie)

4. **Narzędzie** — dopasowane do procesu, nie odwrotnie

**Mapowanie procesu (jak jest, nie jak powinno być):**
- Idź do ludzi, którzy faktycznie wykonują czynność — sprawdź, jak to naprawdę robią, nie jak zakładano 10 lat temu
- Oceń, które kroki wymagają człowieka (decyzja, relacja, empatia), a które można oddać technologii
- Nie automatyzuj całego procesu naraz — rozbij na czynności i automatyzuj pojedynczo
- Iteracja: najpierw drafty/podpowiedzi → zbierasz feedback → dopiero pełen automat

**Cztery poziomy automatyzacji:**
1. **Automatyzacje wbudowane w narzędzia** (CRM, mailing, e-commerce) — start bez kodowania
2. **Automatyzacja procesów** ([[Make.com]], [[n8n]]) — łączenie systemów A→B, przepływ danych
3. **Automatyzacja z AI** — dodanie modelu (Claude, OpenAI, Gemini) do konkretnych kroków automatyzacji
4. **Agent AI** — samodzielnie dobiera narzędzia i podejmuje decyzje w ramach wyznaczonych parametrów

**Czego NIE automatyzować:**
- Decyzji wymagających osądu, empatii lub znajomości kontekstu relacji
- Procesów rzadkich (raz na kwartał) — koszt wdrożenia > zaoszczędzony czas
- Procesów niezmapowanych i chaotycznych — automatyzacja chaosu = szybszy chaos

**Demo: głos → mapa procesu w Mermaid → lista automatyzacji w n8n:**
- Super Whisper (transkrypcja mowy → tekst, offline, bezpłatny)
- Claude Code / Claude → diagram w składni Mermaid (każdy krok = węzeł, decyzje = gałęzie)
- Dopisz narzędzia do każdego kroku → poproś AI o wylistowanie potencjalnych automatyzacji w [[n8n]]
- n8n MCP podłączony do Claude → budowanie i testowanie workflow głosem/czatem

## Wnioski

- Technologia jest na końcu, nie na początku — złe pytanie: "mam [[Make.com]], co by tu zautomatyzować?"; właściwe: "co chcę osiągnąć i który proces mnie tam przybliży?"
- Jedna działająca automatyzacja generuje kolejne pomysły w całej organizacji — najważniejszy jest pozytywny start, bo nieudane wdrożenie zniechęca cały zespół na długo
- Przed budowaniem automatyzacji z AI warto poznać narzędzie ([[n8n]], [[Make.com]]) — żeby rozumieć błędy i nie tworzyć kosztownych pętli (np. 1000 wywołań API z jednego leada)

## Cytat

> Automatyzowanie chaosu prowadzi do tego, że mamy zautomatyzowany chaos.

## Zastosowanie

Framework lejka wyboru (cel → dział → proces → narzędzie) to gotowe narzędzie do warsztatów dla klientów NGO — konkretyzuje, dlaczego nie zaczynamy od narzędzia i jak wybrać pierwszy proces do automatyzacji. Cztery kryteria selekcji (co denerwuje / co daje pieniądze / co zabiera pieniądze / co zjada czas) można użyć bezpośrednio jako ćwiczenie w sesji konsultacyjnej. Demo z [[n8n]] MCP podłączonym do Claude potwierdza kierunek budowania własnych narzędzi Piotra i daje konkretny przykład do pokazania klientom.
