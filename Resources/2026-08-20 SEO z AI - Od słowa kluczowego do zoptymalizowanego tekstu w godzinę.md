---
categories:
  - Clippings
authors: ["[[Artur Jabłoński]]"]
url: "https://www.youtube.com/watch?v=ba6iphKduG4"
source: "[[Archives/2026-08-20 SEO z AI - Od słowa kluczowego do zoptymalizowanego tekstu w godzinę|2026-08-20 SEO z AI - Od słowa kluczowego do zoptymalizowanego tekstu w godzinę]]"
published: 2026-08-20
created: 2026-08-25
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "content-marketing"
---

# SEO z AI - Od słowa kluczowego do zoptymalizowanego tekstu w godzinę

Artur Jabłoński pokazuje na żywym przykładzie pełny proces produkcji zoptymalizowanego pod SEO artykułu blogowego w [[Claude Code]] — od transkrypcji filmu na YouTube, przez dobór słowa kluczowego ([[Senuto]] + [[Ahrefs]]), po napisanie tekstu w jego stylu i publikację jako draft w WordPressie — w około 30-45 minut pracy promptami. Kluczowa teza: samo AI nic nie zrobi dobrze bez rozbicia procesu na łańcuch wyspecjalizowanych "bramek" (skilli) — głosu, humanizacji, korekty językowej i weryfikacji SEO — z ludzkim nadzorem na każdym etapie. Autor demonstruje też realny błąd procesu (pominięcie sprawdzenia kanibalizacji treści), żeby pokazać, że AI ignoruje nawet zapisane na sztywno reguły, jeśli nikt tego nie wymusi. Materiał promuje kurs AI Marketers 3, ale sam proces i lista narzędzi są konkretne i możliwe do odtworzenia samodzielnie.

## Frameworki i metody

- **Trzy filary procesu**: [[Claude Code]] (lub inny agent kodujący) do wykonywania łańcucha zadań, samodzielnie zbudowane skille (powtarzalne instrukcje-łańcuchy promptów) oraz narzędzia zewnętrzne podpięte przez MCP/API (np. [[Senuto]], [[Ahrefs]], [[Neuronwriter]]).
- **Łańcuch skilli do napisania artykułu**: 1) skill Watch — obejrzenie filmu (screeny co kilka sekund, nie tylko transkrypcja) i podsumowanie w punktach; 2) dobór słowa kluczowego przez skrzyżowanie danych z Senuto i Ahrefs (wolumen, trudność, intencja); 3) skill "głos" — napisanie artykułu na bazie transkryptu i przygotowanego wcześniej poradnika stylu autora + przykładowych tekstów wzorcowych; 4) skill [[Humanizer]] — usuwanie typowych "AI tells" (sztuczny dramatyzm, krótkie zdania, myślniki) bez ruszania indywidualnych cech stylu; 5) autorski skill "polonista gate" — korekta gramatyki, rytmu zdań i kalek językowych z angielskiego, których nie wyłapują publiczne skille pisane pod język angielski; 6) skill [[Neuronwriter]] — dogęszczanie tekstu pod pokrycie słów kluczowych do wyniku powyżej 70/100; 7) generowanie gotowego draftu do publikacji w WordPressie.
- **"Definicja ukończenia" (definition of done)** wpisana w każdy prompt/skill — checklista, po której AI rozpoznaje, że zadanie wykonało poprawnie, i robi autorefleksję.
- **Rozbijanie procesu na atomy** zamiast jednego megapromptu — ułatwia debugowanie, unika gubienia kontekstu i pozwala budować "bramki" samokorekty; łączenie wszystkiego w jeden prompt ma sens dopiero, gdy proces jest już wielokrotnie przetestowany.
- **Zasada "nowy plik = nowa wersja"** zamiast nadpisywania — zachowuje możliwość cofnięcia się do poprzedniej wersji tekstu.
- **Trzy ścieżki pracy z AI** (struktura kursu): ścieżka czat (co da się zrobić samym czatem), ścieżka narzędziowa (wyspecjalizowane narzędzia AI) i ścieżka agentowa (spięcie wszystkiego w powtarzalny, automatyczny proces).

## Kluczowe dane

- Po wdrożeniu własnych agentów AI: wzrost widoczności organicznej serwisu autora o blisko 30% w półtora miesiąca, +74 frazy w top 10, +16 w top 3.
- Wynik optymalizacji Neuronwriter dla przykładowego tekstu: pierwsza wersja 39/100 → po kilku pętlach 51/100 → po pełnej optymalizacji 83/100 (celowo obniżony dla naturalności; top 1 w Google ma 78, mediana top 10 to 68).
- Koszt jednego zapisu na webinar spadł z 10 zł (kreacje robione ręcznie) do 3,74 zł (kreacje tworzone z AI) — CTR czterokrotnie wyższy, sprzedaż dwukrotnie tańsza.
- W tygodniu nagrania webinaru opublikowano 26 tekstów stworzonych wspólnie z AI (w tym 13 jednego dnia).

## Wnioski

- Skuteczna praca z AI nad treścią wymaga rozbicia procesu na łańcuch wyspecjalizowanych skilli z jasną "definicją ukończenia", a nie jednego ogólnego prompta — dotyczy to też pracy poza SEO, np. przy pisaniu tekstów dla NGO czy newsletterów.
- Sam dobry poradnik stylu ("głos") nie wystarczy, podobnie jak sam zestaw przykładowych tekstów — dopiero połączenie obu daje tekst brzmiący autentycznie, co ma bezpośrednie zastosowanie przy budowaniu własnego głosu do ghostwritingu.
- AI ignoruje nawet twardo zapisane reguły (np. obowiązkowe sprawdzenie kanibalizacji treści), jeśli proces nie wymusza ich wykonania — human in the loop jako kontroler na każdym etapie procesu pozostaje konieczny, nie tylko na jego końcu.

## Cytat

> AI samo nic nie zrobi dobrze — od prostego prompta dostaniemy badziewie, a od niekierowanego dostaniemy rzeczy błędne; dobrze pokierowane zrobi to jednak naprawdę dobrze.

## Zastosowanie

Proces (skill "głos" + humanizer + bramka korekty językowej + definicja ukończenia) można bezpośrednio przenieść na warsztat ghostwritingowy i pisanie tekstów dla klientów NGO — zwłaszcza budowa własnego poradnika stylu z przykładowymi tekstami jako baza pod skille w Claude Code. Podejście "rozbij proces na atomy i wymuś checklistę" pasuje też do budowania własnych pluginów/skilli Claude Code. Warto rozważyć zbudowanie analogicznego łańcucha (transkrypcja → research słów kluczowych → szkic w swoim głosie → korekta → publikacja) do przetwarzania własnych materiałów szkoleniowych i webinarów na artykuły blogowe czy odcinki newslettera.
