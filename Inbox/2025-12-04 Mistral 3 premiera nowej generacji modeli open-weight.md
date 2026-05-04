---
type: "Web"
authors: "[[Karolina Ceroń]]"
url: "https://haimagazine.com/pl/ai_news/mistral-3-premiera-nowej-generacji-modeli-open-weight/?utm_source=ActiveCampaign&utm_medium=email&utm_content=AI%20Flash%20%2365%3A%20%20UNDP%20ostrzega%20przed%20nier%C3%B3wno%C5%9Bci%C4%85%20cyfrow%C4%85%2C%20AI%20skraca%20drog%C4%99%20na%20plac%20budowy%2C%20a%20Micha%C5%82%20Anio%C5%82%20maluje%20tarcz%C4%99%20dla%20NATO&utm_campaign=AI%20Flash%20%2364%20%28Kopiuj%29"
published: 2025-12-04
created: 2026-05-04
tags:
---


Modele o otwartych wagach (*open-weights*) coraz skuteczniej rywalizują z zamkniętymi rozwiązaniami komercyjnymi. Firma Mistral AI zaprezentowała właśnie trzecią generację swoich produktów – rodzinę Mistral 3. Jej premiera to krok w stronę realizacji wizji „rozproszonej inteligencji” (*distributed intelligence*).

Co to oznacza w praktyce? Do tej pory, aby skorzystać z AI o najwyższej jakości, zazwyczaj musieliśmy łączyć się z potężnym serwerem w chmurze. Wizja „rozproszonej inteligencji” zmienia to podejście. Chodzi o to, by sztuczna inteligencja działała tam, gdzie jest akurat potrzebna, a nie tylko w odległej serwerowni. Dzięki różnym rozmiarom modeli Mistral 3, programiści mogą dobrać odpowiednie narzędzie do zadania: gigantyczny model do skomplikowanych analiz w chmurze lub mały, szybki model, który zadziała bezpośrednio na Twoim laptopie – nawet bez dostępu do internetu.

#### Mistral Large 3 – waga ciężka w otwartej architekturze

Model Mistral Large 3 stanowi istotny skok technologiczny, wykraczający poza standardowe aktualizacje. Oparto go na architekturze *Sparse Mixture-of-Experts*. Choć całkowita liczba parametrów wynosi imponujące 675 miliardów, w danym momencie (dla każdego tokena) aktywowanych jest jedynie 41 miliardów. Dzięki temu model zachowuje potężną wiedzę i możliwości, pozostając zaskakująco lekkim w obsłudze.

Model trenowano od podstaw na klastrze złożonym z 3000 najnowocześniejszych procesorów graficznych NVIDIA H200. Efekty?

- **Wydajność:** Mistral Large 3 osiąga parytet z najlepszymi na rynku modelami *instruction-tuned* o otwartych wagach.
- **Rankingi:** W prestiżowym zestawieniu LMArena zadebiutował na drugim miejscu w kategorii modeli open source (z wyłączeniem modeli wnioskujących) i szóstym miejscu w ogólnym zestawieniu.
- **Wszechstronność:** Model nie tylko generuje tekst, ale natywnie rozumie obrazy i oferuje wiodącą w swojej klasie obsługę języków innych niż angielski i chiński.

Każdy z nich dostępny jest w trzech wariantach: podstawowym (*base*), instruktażowym (*instruct*) oraz wnioskującym (*reasoning*).

#### Ministral 3 – „kieszonkowa” inteligencja o wielkich możliwościach

Równie ciekawie jest na drugim biegunie skali.

Obok najpotężniejszego modelu Large, zadebiutowała seria Ministral 3, dedykowana rozwiązaniom *edge computing*. Termin ten oznacza przetwarzanie danych bezpośrednio na urządzeniu (np. na laptopie czy w lokalnej infrastrukturze), zamiast przesyłania ich do zewnętrznych serwerów. W dobie obaw o prywatność danych, możliwość uruchomienia zaawansowanego AI lokalnie staje się kluczowa. Seria obejmuje trzy rozmiary:

- 3 miliardy parametrów (3B),
- 8 miliardów parametrów (8B),
- 14 miliardów parametrów (14B).

Szczególną uwagę warto zwrócić na warianty nastawione na wnioskowanie (reasoning). W sytuacjach wymagających żelaznej logiki modele te potrafią „pomyśleć” dłużej przed udzieleniem odpowiedzi. Przekłada się to na imponujące wyniki – wariant 14B osiągnął aż 85% skuteczności w teście matematycznym AIME ’25.

Co więcej, modele Ministral są niezwykle oszczędne w słowach. Dzięki optymalizacji często generują o rząd wielkości mniej tokenów niż konkurencja, zachowując tę samą jakość merytoryczną. Dla biznesu oznacza to konkretną oszczędność kosztów obliczeniowych.

#### Sojusz technologiczny: NVIDIA, Red Hat i vLLM

Wdrożenie Mistral 3 to także popis optymalizacji sprzętowej, osiągnięty dzięki ścisłej współpracy z firmą NVIDIA. Wszystkie modele trenowano na architekturze Hopper, wykorzystując przepustowość pamięci HBM3e.

Aby zapewnić, że otwartość modeli przełoży się na ich praktyczną użyteczność, zespół inżynierów skupił się na usunięciu barier sprzętowych. Udostępniono checkpointy w nowym formacie NVFP4, zbudowane przy użyciu narzędzia llm-compressor.

- **Dla serwerowni:** Umożliwia to wydajne uruchamianie giganta Mistral Large 3 nawet na pojedynczym węźle 8×A100 lub 8×H100 przy użyciu vLLM.
- **Dla urządzeń osobistych:** Mniejsze modele zoptymalizowano pod kątem działania na popularnych kartach RTX, laptopach oraz platformach Jetson. To otwiera drogę do implementacji zaawansowanego AI w robotyce, dronach czy domowych asystentach bez konieczności łączenia się z chmurą.

#### Dostępność i otwarta licencja

Zgodnie z filozofią firmy, kod i wagi modeli z rodziny Mistral 3 trafiły do sieci na permisywnej licencji Apache 2.0. To zaproszenie dla firm i deweloperów do budowania własnych rozwiązań na solidnym fundamencie, bez obaw o prawny „vendor lock-in”.

Modele są już dostępne na wiodących platformach: Mistral AI Studio, Hugging Face, Amazon Bedrock, Azure Foundry, IBM WatsonX oraz OpenRouter. Wkrótce dołączą do nich usługi NVIDIA NIM i AWS SageMaker. Organizacje o specyficznych potrzebach mogą również skorzystać z usług dedykowanego fine-tuningu do własnych danych.