---
categories:
  - "Emails"
published: 2025-09-22
created: 2026-03-26
labels:
  - "ECF"
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "organizacje-społeczne"
---

# Scoping AI platforms for communications - any advice

Wątek z listy dyskusyjnej [[ECF]] (European Campaigning Forum) dotyczący wyboru płatnej platformy AI dla organizacji pozarządowej [[Womankind Worldwide]]. Kluczowym tematem jest napięcie między wygodą komercyjnych narzędzi (ChatGPT, Claude) a ryzykami związanymi z prywatnością danych i zgodnością z GDPR. [[Geeks for Social Change]] (Kim Foale) przekonuje, że jedyną drogą do prawdziwej ochrony danych jest self-hosting modeli AI na własnych serwerach. Konkluzja jest taka, że żadna płatna platforma komercyjna nie gwarantuje bezpieczeństwa danych NGO, a budowa własnego rozwiązania jest kosztowna i wymaga współpracy wielu organizacji.

## Frameworki i metody

- **Self-hosting modeli AI** — instalacja dedykowanego serwera w siedzibie organizacji, wybór modelu open-source (np. Qwen, Ollama), stworzenie interfejsu za pomocą [[n8n]]; dane nigdy nie opuszczają infrastruktury organizacji
- **Model współdzielony (10 org × koszt)** — propozycja podziału kosztów self-hostingu między kilka organizacji pozarządowych jako alternatywa dla indywidualnych wdrożeń; analogia do spółdzielczego podejścia do technologii
- **Polityka AI** — wewnętrzny dokument regulujący użycie AI w organizacji, obejmujący zasady prywatności danych, zgodność z GDPR i kontrolę jakości outputów

## Kluczowe dane

- Szacunkowy koszt wdrożenia własnego serwera AI: niski pięciocyfrowy przedział (pound sterling)
- Trzy główne ryzyka identyfikowane przez NGO przy darmowych platformach AI: ochrona danych osobowych, zgodność z GDPR, wiarygodność outputów

## Wnioski

- Komercyjne [[LLM]] — nawet płatne — niekoniecznie chronią dane organizacji; Kim Foale wprost stwierdza, że informacje "almost certainly going directly to Palantir", co dla NGO o progresywnej misji może być sprzeczne z teorią zmiany organizacji
- [[n8n]] i modele open-source (Qwen, Ollama) tworzą realny stack techniczny do self-hostingu AI w NGO, ale wdrożenie wymaga kompetencji technicznych i znacznego budżetu, co przekracza możliwości większości pojedynczych organizacji
- Kolektywne podejście do wdrożeń technologicznych — kilka NGO dzielących koszty infrastruktury AI — jest kierunkiem wartym eksploracji w kontekście sektora społecznego, analogicznym do modelu [[Tech To The Rescue]]

## Cytat

> „Korporacyjne modele językowe są dla wielu organizacji skrajnie niebezpieczne i prawdopodobnie sprzeczne z ich teorią zmiany."

## Zastosowanie

W pracy z klientami NGO wdrażającymi AI Piotr może używać tej dyskusji jako case study ilustrującego dylematy privacy-vs-convenience przy wyborze platformy. Przy tworzeniu polityk AI dla organizacji warto uwzględnić model ryzyk (prywatność, GDPR, wiarygodność). Temat self-hostingu i współdzielonej infrastruktury może być inspiracją do propozycji konsorcjalnych dla sieci NGO lub LGD.
