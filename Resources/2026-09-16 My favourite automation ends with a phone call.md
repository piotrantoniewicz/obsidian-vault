---
categories:
  - Clippings
authors: ["[[Kyle Behrend]]"]
url: "https://kylebehrend.substack.com/p/my-favourite-automation-ends-with"
source: "[[Archives/2026-09-16 My favourite automation ends with a phone call|2026-09-16 My favourite automation ends with a phone call]]"
published: 2026-09-16
created: 2026-09-17
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "organizacje-społeczne"
---

# My favourite automation ends with a phone call

Kyle Behrend, specjalista od automatyzacji pracujący z sektorem NGO, proponuje prosty sposób myślenia o automatyzacjach: trigger, warunki, akcje — schemat pozwalający zrozumieć cały proces bez znajomości narzędzia, którym go zbudowano. Radzi zaczynać od zadań, których się nienawidzi wykonywać — małych, powtarzalnych i łatwych do zweryfikowania — zamiast szukać efektownych, dużych projektów. Rozróżnia zastosowania osobiste i eksploracyjne (dobrze pasujące do narzędzi jak Claude czy ChatGPT) od workflow organizacyjnych wymagających wielu systemów i jasnych reguł routingu (domena Make czy n8n). Podkreśla też, że uruchomienie automatyzacji to dopiero początek — wymaga utrzymania, testowania przypadków brzegowych i jasnej odpowiedzialności za jej działanie, a zaoszczędzony czas warto świadomie przeznaczyć na pracę, na którą wcześniej nie było miejsca.

## Frameworki i metody

- **Trigger, warunki, akcje** — trzy elementy opisujące każdą automatyzację. Trigger uruchamia proces (np. wpłata darowizny, wysłanie formularza, harmonogram, ręczne kliknięcie). Warunki decydują, czy i jak proces ma przebiegać dalej (np. zgoda na maile marketingowe, przekroczenie progu kwoty darowizny). Akcje to efekt końcowy (dodanie rekordu, przeniesienie informacji między systemami, powiadomienie kogoś, przygotowanie szkicu). Warto naszkicować te trzy elementy na papierze lub w [[tldraw]], zanim otworzy się [[Make.com]], [[n8n]], Claude czy ChatGPT — samo wypisanie ich wymusza doprecyzowanie procesu (tzw. process mapping) i bywa przydatne nawet wtedy, gdy automatyzacja ostatecznie nie powstaje.
- **„Structured versus AI-led"** — spektrum określające, jaką część procesu definiuje się z góry, a jaką pozostawia interpretacji modelu. AI można umieścić wewnątrz uporządkowanego workflow, a zadanie prowadzone głównie przez AI nadal potrzebuje jasnych warunków i granic. Przykład: automatyzacja triage'u maili, w której AI kategoryzuje wiadomość, a reszta procesu (zapis, przekazanie, przygotowanie odpowiedzi do akceptacji) działa na zwykłych regułach — nie każdy krok musi angażować model językowy.

## Wnioski

- Najskuteczniejszym punktem wejścia do automatyzacji w organizacji jest zadanie, które ktoś wykonuje niechętnie i powtarzalnie — małe, łatwe do zweryfikowania, niekoniecznie codzienne.
- Wybór narzędzia zależy od kontekstu: eksperymenty osobiste i praca na danych publicznych dobrze sprawdzają się bezpośrednio w Claude czy ChatGPT, natomiast workflow organizacyjny — wymagający wielu kont, systemów i jawnych reguł routingu — lepiej budować w [[Make.com]] lub [[n8n]].
- Wdrożenie automatyzacji to początek, nie koniec procesu: modele bywają wycofywane, prompty przestają działać zgodnie z oczekiwaniami, organizacja zmienia sposób pracy — dlatego automatyzacja potrzebuje utrzymania, testowania przypadków brzegowych (także tych, w których nic nie powinno się wydarzyć) i jasno przypisanej odpowiedzialności.

## Cytat

> Błędem, który często widzę, jest założenie, że po uruchomieniu automatyzacji praca jest skończona.

## Zastosowanie

Ramka trigger–warunki–akcje to gotowe, proste narzędzie do warsztatów o automatyzacji dla organizacji społecznych — można jej użyć wprost przy szkoleniach z AI dla NGO. Rozróżnienie „kiedy wystarczy narzędzie AI, a kiedy potrzebny jest Make/n8n" ułatwia doradzanie klientom przy wyborze platformy wdrożenia. Przykład automatyzacji darowizn kończącej się telefonem do darczyńcy to gotowa ilustracja do materiałów o fundraisingu wspieranym automatyzacją.
