---
categories:
  - "Emails"
published: 2026-08-01
created: 2026-08-02
labels:
  - "The Batch"
relevance: niska
tags:
  - "LLM"
  - "trendy-AI"
  - "narzędzia-AI"
---

# A Full Accounting of Models' GPU Use

Badacze z [[University of Washington]], [[Allen Institute for AI]] i [[Carnegie Mellon University]] policzyli pełny ślad środowiskowy rozwoju rodziny modeli [[Olmo 3]] — nie tylko finalny trening, ale wszystkie etapy: pretraining, midtraining, SFT, DPO, RL oraz generowanie danych syntetycznych. Okazało się, że to eksperymentowanie i generowanie danych syntetycznych, a nie sam finalny trening, pochłaniają większość zasobów. Wersje modeli dostrojone do rozumowania (reasoning) zużywają znacznie więcej mocy obliczeniowej niż wersje instrukcyjne. Wniosek badaczy podważa dotychczasowe raporty o śladzie AI, które liczyły niemal wyłącznie koszt finalnego treningu.

## Frameworki i metody

- Pomiar śladu środowiskowego modelu AI w 5 fazach — badacze śledzili zużycie energii osobno dla: (i) pretrainingu, (ii) midtrainingu, (iii) SFT, (iv) DPO, (v) RL, a dodatkowo osobno dla generowania danych syntetycznych i filtrowania promptów do RL. Zużycie energii GPU mierzyli z rozdzielczością poniżej sekundy, a następnie przeliczali je na całkowite zużycie centrum danych (uwzględniając CPU, pamięć, sieć, chłodzenie), emisje gazów cieplarnianych (na podstawie intensywności węglowej lokalnej sieci energetycznej) i zużycie wody (na podstawie zużycia wody przez lokalne elektrownie).

## Kluczowe dane

- Rozwój rodziny modeli [[Olmo 3]] zużył ok. 12,3 GWh energii elektrycznej — tyle, ile roczne zużycie ok. 1200 przeciętnych amerykańskich gospodarstw domowych.
- Wyemitowano ok. 4250 ton gazów cieplarnianych i zużyto blisko 16 mln litrów wody (odpowiednik dziennego zużycia wody przez 50 000 mieszkańców USA).
- Eksperymentowanie pochłonęło 82,2% godzin GPU poświęconych na aktywności treningowe (bez generowania danych syntetycznych), a sam finalny trening tylko 17,8%. Generowanie danych syntetycznych to aż 36,9% wszystkich godzin GPU.
- Wersja rozumująca Olmo 3 32B Think wymagała 14 razy więcej godzin GPU na etapach fine-tuningu niż wersja instrukcyjna.

## Wnioski

- Raporty o śladzie środowiskowym AI, które liczą wyłącznie finalny trening, systematycznie zaniżają rzeczywisty koszt — eksperymentowanie i przygotowanie danych syntetycznych to główne źródło zużycia zasobów, nie sam trening.
- Modele dostrojone do rozumowania (reasoning) mają wyraźnie wyższy ślad środowiskowy niż modele instrukcyjne — w miarę jak modele będą generować dłuższe łańcuchy rozumowania i częściej korzystać z narzędzi, ten koszt będzie rósł.
- Dla organizacji rozważających wdrażanie AI to argument do dyskusji o zrównoważonym rozwoju: koszt środowiskowy modelu nie kończy się na jego wytrenowaniu — cały proces R&D za kulisami waży więcej, niż sugerują popularne szacunki.

## Cytat
> Kiedy eksperymentowanie jest kosztowne — środowiskowo i finansowo — ludzie, którzy potrafią ocenić, które eksperymenty warto przeprowadzić, są szczególnie cenni.

## Zastosowanie
Przydatne jako kontrargument lub kontekst w rozmowach o etyce i zrównoważonym stosowaniu AI w organizacjach społecznych — pokazuje, że ślad środowiskowy modeli jest większy i bardziej złożony, niż sugerują popularne uproszczone szacunki ograniczone do samego treningu.
