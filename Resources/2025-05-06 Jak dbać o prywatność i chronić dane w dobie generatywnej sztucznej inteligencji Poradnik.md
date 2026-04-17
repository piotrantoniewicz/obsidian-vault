---
categories: Clippings
authors: ["[[Kamil Śliwowski]]"]
url: https://sektor3-0.pl/blog/jak-dbac-o-prywatnosc-i-chronic-dane-w-dobie-generatywnej-sztucznej-inteligencji-poradnik/
source: "[[Archives/2025-05-06 Jak dbać o prywatność i chronić dane w dobie generatywnej sztucznej inteligencji Poradnik|2025-05-06 Jak dbać o prywatność i chronić dane w dobie generatywnej sztucznej inteligencji Poradnik]]"
published: 2025-05-06
created: 2026-03-24
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "organizacje-społeczne"
---

# Jak dbać o prywatność i chronić dane w dobie generatywnej sztucznej inteligencji? Poradnik

[[Kamil Śliwowski]] z [[Sektor 3.0]] stawia tezę, że bezpieczeństwo pracy z generatywną AI zależy przede wszystkim od świadomości użytkowników, a nie od regulacji prawnych czy dobrej woli dostawców. Artykuł systematyzuje zagrożenia (prompt injection, wycieki danych, wypalenie czujności, naruszenia RODO) i proponuje konkretne praktyki minimalizacji ryzyka: anonimizację danych, ograniczenie liczby narzędzi i wspólne audyty zespołowe. Kluczową informacją praktyczną są instrukcje ustawień prywatności w [[ChatGPT]], [[Perplexity]] i [[Google Gemini]] oraz omówienie lokalnych modeli AI jako alternatywy dla chmury. Poradnik jest pisany z perspektywy organizacji społecznych.

## Frameworki i metody

**Główne kategorie zagrożeń przy pracy z generatywną AI:**
- **Prompt injection** — manipulacja instrukcjami w celu uzyskania nieautoryzowanego dostępu do modelu lub danych
- **Luki w zabezpieczeniach danych** — ataki typu model extraction mogą ujawnić dane osobowe użyte do treningu
- **Nieświadome udostępnianie poufnych danych** — łatwość pracy z AI zwiększa ryzyko przekazania wrażliwych informacji (case: Samsung + ChatGPT, 2023)
- **Nieautoryzowany dostęp** — utrata kontroli nad kontem = dostęp do historii konwersacji i załączników
- **Błędne/stronnicze wyniki** — modele trenowane na niekompletnych danych generują ryzyko dezinformacji
- **Naruszenia praw autorskich** — AI-generated content może nieświadomie plagiatować chronione dzieła

**Trzy praktyki ograniczania ryzyka:**
1. **Minimalizacja danych i narzędzi** — skupienie na zadaniach faktycznie podnoszących produktywność; ograniczenie liczby równocześnie używanych narzędzi
2. **Anonimizacja danych** przed przekazaniem do modelu:
   - Pseudonimizacja (RANDBETWEEN w Excel, Znajdź i zamień w Word)
   - Maskowanie danych (funkcje TEXT, LEFT/RIGHT w Excel)
   - Uogólnianie (np. wiek → przedział wiekowy)
   - Zamiana danych (data swapping)
   - Dodawanie szumu
3. **Wspólne audyty zespołowe** — regularne przeglądy praktyk, wymiana promptów, transparentność w zespole dot. używanych narzędzi

**Ustawienia prywatności w kluczowych narzędziach:**
- [[ChatGPT]]: Tymczasowy czat (lewy górny róg) lub Ustawienia > Kontrola danych > wyłącz "Ulepsz model dla wszystkich"; pełne gwarancje dopiero na planie Enterprise
- [[Perplexity]]: Tryb incognito (Ustawienia) + Ustawienia > Preferencje > wyłącz Retencja danych
- [[Google Gemini]]: Wyłączenie Aktywności aplikacji Gemini przez profil; ograniczone opcje powiązane z kontem Google

**Lokalne modele AI jako alternatywa:**
- Narzędzia: [[jan.ai]], LMStudio, [[Ollama]] — prosta konfiguracja bez wiedzy technicznej
- Wymóg: min. 32 GB RAM dla modeli jak Llama3, Deepseek R1, Google Gemma
- Alternatywa chmurowa: [[Microsoft Azure]] lub [[Google Vertex]] — własne środowisko z pełną kontrolą danych

## Wnioski
- Regulacje prawne (RODO) i ustawienia narzędzi to dwa różne poziomy ochrony — organizacje NGO muszą rozumieć oba, a gwarancje bezpieczeństwa często dostępne są dopiero na planach Enterprise, nie indywidualnych płatnych.
- Lokalne modele AI (Llama3, Deepseek, Gemma) uruchamiane na własnym sprzęcie eliminują ryzyko wycieku danych do chmury dostawcy — dla organizacji pracujących z wrażliwymi danymi beneficjentów to kluczowa alternatywa.
- Świadome zarządzanie ryzykiem wymaga polityki AI w zespole + praktycznych kompetencji anonimizacji + regularnych audytów — to trójnóg bezpiecznego wdrożenia AI w NGO.

## Zastosowanie
Artykuł stanowi gotowy materiał do modułu o bezpieczeństwie danych w szkoleniu "Fundraising z AI" — sekcje o anonimizacji i ustawieniach narzędzi można bezpośrednio zaadaptować jako ćwiczenia. Przy wdrożeniach AI w NGO warto uwzględnić obowiązkowy krok: audyt wrażliwości danych i określenie, które procesy nie powinny trafiać do narzędzi chmurowych. Lokalne modele AI (przez Ollama) to propozycja dla organizacji przetwarzających dane osobowe beneficjentów, którą warto mieć w ofercie konsultingowej.
