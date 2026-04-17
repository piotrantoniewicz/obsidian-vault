---
categories: Clippings
authors:
  - '[[Chase AI]]'
url: 'https://www.youtube.com/watch?v=7q_rbT1a9dE'
source: >-
  [[Archives/2026-03-31 These Claude Code Automations Got Me 10M Views in 1
  Month|2026-03-31 These Claude Code Automations Got Me 10M Views in 1 Month]]
published: '2026-03-31'
created: '2026-04-11'
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - content-marketing
---
# These Claude Code Automations Got Me 10M Views in 1 Month

Chase AI opisuje system 7 skilli [[Claude Code]], które pozwoliły mu wyprodukować 90 filmów w 30 dni i osiągnąć 10 milionów wyświetleń jako jednoosobowy twórca bez redaktorów ani asystentów. System opiera się na 4 fazach procesu tworzenia treści: badania (research z [[Notebook LM]] i własny scraper Twittera), ideacja (mapowanie konkurencji i luk), skrypty (hooki, outline, tytuły) oraz dystrybucja (content cascade do 6 platform). Kluczową obserwacją jest to, że wynik 10 milionów wyświetleń nie wynikał z pojedynczych viralowych hitów, lecz z konsekwentnego wolumenu — 90 solidnych filmów. AI sprawdza się tu jako koproducent na każdym etapie, ale twórca musi pozostawać w pętli decyzyjnej — pełna automatyzacja bez ludzkiego nadzoru daje generyczne, słabe rezultaty.

## Frameworki i metody

**4-fazowy system tworzenia treści z [[Claude Code]]:**

1. **Research** — skill YT Pipeline: [[Notebook LM]] przez terminal via Notebook LM PI CLI (analiza YouTube URL-i, PDFs, docs na serwerach Google bez zużycia tokenów Claude); własny scraper Twittera (Telegram + scoring: velocity, authority, timing, opportunity, replyability; dane do [[Supabase]]; wyniki co 30-45 min); skrypt GitHub Trending Repos (top 10 repo AI z ostatnich 7 dni + top 5 miesiąca → codziennie do [[Obsidian]] vault)
2. **Ideacja** — skill ideacji: analiza competitive landscape (kąty nasycone, luki, outliers), rankingowane propozycje wideo z tytułami i kątami; Claude jako koproducent, nie autopilot — twórca zatwierdza kierunek przed przejściem dalej
3. **Skrypty** — skill hooków (5 wariantów: spoken hook + visual hook + text overlay); skill outline (sekcje + talking points + visual aids + source material); skill tytułów (porównanie z historią wyników; tier 1: bezpieczne, tier 2: ryzykowne)
4. **Dystrybucja (Content Cascade)** — YouTube → automatyczny blog post (SEO, embed wideo) + Twitter thread (7 replies, auto-post po zatwierdzeniu) + LinkedIn draft; skill short form: hooki i outline skrócone do formatów 30/60/90 sek. → Shorts, Reels, TikTok

**Identyfikacja "fountain head of knowledge" dla niszy:**
- Dla AI/tech: GitHub Trending + Twitter jako punkt zero; z nich content trafia potem na YouTube i dalej
- Zasada: zidentyfikuj, gdzie informacja powstaje w Twojej niszy → zbuduj automatyczne narzędzie monitorujące → podłącz do systemu produkcji

## Wnioski

- Klucz do skalowalnego systemu contentu to zidentyfikowanie "fountain head of knowledge" dla swojej niszy i podłączenie zautomatyzowanych narzędzi monitorujących — bez tego nie ma świeżych tematów
- [[Claude Code]] działa najlepiej jako koproducent, nie autopilot — twórca musi zatwierdzać każdy etap (ideacja → outline → hook → tytuł), inaczej output jest generyczny i traci autentyczny głos
- Dystrybucja wielokanałowa (6 platform z jednego materiału) nie wymaga dodatkowej pracy, gdy system repurposingu jest zautomatyzowany — to content cascade, nie ręczna praca na każdej platformie

## Zastosowanie

System 4-fazowego workflow można zaadaptować do tworzenia treści dla dobryai.pl i materiałów szkoleniowych — szczególnie przydatna jest idea "content cascade" i automatycznego repurposingu. To wartościowy case study do pokazania podczas szkoleń z AI dla organizacji i firm jako przykład jednoosobowego twórcy z systemem zastępującym cały zespół. Skrypt GitHub Trending Repos → [[Obsidian]] może być bezpośrednio użyteczny do monitorowania nowości AI na potrzeby własnych projektów i kursów.
