---
categories: Clippings
authors: ["[[ngo.pl]]"]
url: https://publicystyka.ngo.pl/formularz-odporny-na-bledy-wypelniajacych-poznaj-wyrazenia-regularne-regex-w-google-forms-tau
source: "[[Archives/2025-08-20 Formularz odporny na błędy wypełniających. Poznaj wyrażenia regularne RegEx w Google Forms|2025-08-20 Formularz odporny na błędy wypełniających. Poznaj wyrażenia regularne RegEx w Google Forms]]"
published: 2025-08-20
created: 2026-03-24
relevance: średnia
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "organizacje-społeczne"
---

# Formularz odporny na błędy wypełniających. Poznaj wyrażenia regularne RegEx w Google Forms

Artykuł z [[ngo.pl]] (autorstwa pracowników [[FRSI]]) pokazuje, jak używać wyrażeń regularnych (RegEx) w [[Google Forms]] i [[Google Sheets]] do walidacji danych zbieranych od uczestników projektów NGO. Problem jest konkretny i częsty: niepoprawne numery telefonów, źle wpisane kody pocztowe czy niespójna struktura danych blokująca automatyczne przetwarzanie. Artykuł podkreśla, że chatboty AI generują wyrażenia regularne na żądanie, co obniża barierę wejścia do minimum. Zawiera gotowe wyrażenia do natychmiastowego użycia w formularzach rejestracyjnych i bazach danych.

## Frameworki i metody

- **Wyrażenia regularne (RegEx) w [[Google Forms]]** — wzorce do walidacji pól otwartych:
  - `^\d{9}$` — numer telefonu (9 cyfr)
  - `^+\d{1,3}\d{9}$` — numer telefonu z prefiksem kraju
  - `^\d{11}$` — PESEL
  - `^\d{10}$` — NIP
  - `^\d{2}-\d{3}$` — kod pocztowy
  - `^[A-Z]{3}\d{6}$` — numer dowodu osobistego
  - `(gmail.com|email.com|email.pl)` — blokowanie konkretnych domen e-mail (z opcją "nie zawiera")
- **RegEx w [[Google Sheets]]** — weryfikacja danych na poziomie arkusza; możliwość blokowania błędnych wpisów lub wyświetlania ostrzeżeń przy błędnych komórkach.

## Cytat
> Wyrażenie regularne pozwala określić wzorzec tekstu, a Formularze Google zweryfikują, czy wpis użytkownika pasuje do określonego schematu — a jeśli nie będzie pasował, nie pozwoli na jego wpisanie.

## Wnioski
- Chatboty AI (w tym [[Claude]]) generują wyrażenia regularne na żądanie i od razu pokazują, jakie ciągi przyjmą lub odrzucą — bariera wdrożenia RegEx jest dziś minimalna nawet dla niekoderów.
- Walidacja formularzy rejestracyjnych za pomocą RegEx oszczędza godziny czyszczenia danych po wydarzeniu — szczególnie ważne przy projektach z dużą liczbą uczestników.
- Ten sam mechanizm działa retroaktywnie w [[Google Sheets]] do wyszukiwania błędnych wpisów w istniejących bazach danych — np. przy czyszczeniu baz darczyńców NGO.

## Zastosowanie
RegEx w formularzach Google to konkretne, bezkosztowe narzędzie automatyzacji jakości danych dla NGO — idealne do wdrożenia przy rejestracji na szkolenia, zbieraniu danych darczyńców lub sprawozdawczości projektowej. Warto włączyć ten temat do szkoleń z automatyzacji dla organizacji jako przykład, gdzie AI pomaga generować wyrażenia bez znajomości składni.
