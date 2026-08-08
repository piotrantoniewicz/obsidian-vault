---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2026/06/relacja-ma-znaczenie-od-firtha-do-wektorowych-reprezentacji-jezyka?utm_source=newsletter"
published: 2026-06-16
created: 2026-08-05
tags:
  - "LLM"
  - "narzędzia-AI"
  - "prompt-engineering"
---


Aktywny sprzeciw wobec hype'u AI nie powinien prowadzić do dyskredytowania technicznych podstaw działania narzędzi sztucznej inteligencji, którym niektórzy nieostrożnie przypisują większe niż się powinno znaczenie. Dobrym przykładem jest tu reprezentacja wektorowa i modele językowe: zamiast zastanawiać się, czy zabiorą pracę, czy mogą myśleć albo czy mają świadomość, lepiej eksperymentować z wykorzystaniem ich do badań nad przemianami języka.

W 1957 roku brytyjski lingwista John Rupert Firth zaproponował sposób wyznaczania znaczenia słów na podstawie ich sąsiedztwa, co streszcza jego słynny cytat:

> You shall know a word by the company it keeps

Semantyka dystrybucyjna jest podstawą albo przynajmniej jedną ze składowych procesu wyznaczania znaczenia w modelach językowych. Trzymanie słów w wektorach, między którymi oblicza się relacje (np. podobieństwo), jest bardzo skuteczne i pozwala na generowanie spójnych i logicznych wypowiedzi w języku naturalnym, co jest osią takich usług jak ChatGPT. Oczywiście nie trzeba używać modeli językowych wyłącznie do maszynowego wytwarzania tekstów (niektóre z tych modeli [niespecjalnie się nawet do tego nadają](https://blog.humanistyka.dev/2025/07/poezja-bez-ryzyka-to-tylko-skladnia-dlaczego-chatgpt-nie-sprawdzi-sie-w-tworzeniu-poezji)) - sprawdzą się też jako reprezentacje języka, za pomocą których możemy zbadać zmiany znaczenia interesujących nas pojęć (to zadania z zakresu *lexical semantic change*, LSC).

**Co to znaczy δείκνυμι?**

Żeby przeprowadzić takie badanie nie potrzebujemy nawet dużych modeli, wystarczy dostęp do wektorowej reprezentacji słów. Oto w pracy *Lexical semantic change detection for Ancient Greek: dataset creation and evaluation of a word-embedding-based technique* (URI: [clinjournal.org/clinj/article/view/209](https://www.clinjournal.org/clinj/article/view/209), 2024) skorzystano z modeli [word2vec](https://en.wikipedia.org/wiki/Word2vec) do analizy zmian w języku starogreckim. W badaniu skorzystano z korpusu Diorisis Ancient Greek Corpus ([DOI: 10.1163/24523666-01000013](https://doi.org/10.1163/24523666-01000013), 2018), który zawiera ponad 820 tekstów literackich (ok. 10 mln tokenów) w języku greckim i obejmuje różne okresy historyczne (od archaicznego do późnorzymskiego).

Starogrecki korpus podzielono na pięć części, odpowiadających określonym okresom historycznym. Wszystkie słowa zlematyzowano (sprowadzono do form podstawowych) i następnie poddano przetworzeniu na wektory o rozmiarze 30 elementów (co oznacza po prostu 30 cech), z uwzględnieniem ich kontekstu (sąsiedztwa). Porównując ze sobą wektory wybranych słów - co było niczym innym jak działaniem matematycznym! - zanalizowano zmiany semantyczne, dokumentujące np. rozwój języka refleksji filozoficznej czy wpływ chrześcijaństwa.

Przykładowo, w korpusie ponad 4.5 tys. razy występuje słowo δείκνυμι (*deiknymi*), oznaczające pierwotnie *pokazywać*, *wyświetlać* czy *dowodzić*. Obliczono najpierw, że wektory reprezentujące to słowo w subkorpusach odpowiadających kolejnym epokom historycznym dość mocno się zmieniają, dlatego uznano, że warto mu się przyjrzeć. Okazało się, że w ciągu stuleci pojęcie to, odnoszące się najpierw do konkretnych czynności i percepcji wzrokowej, stało się (w epoce klasycznej) elementem języka retorycznego i filozofii, aby ostatecznie w okresie hellenistycznym i późnorzymskim wrócić do ogólnego, mniej technicznego znaczenia.

Analiza ta nie opierała się oczywiście wyłącznie na przeliczaniach wektorów i innych operacjach matematycznych - bez odpowiedniej wiedzy kontekstowej (historia kultury, historia języka) taka interpretacja nie mogłaby powstać. W takich badaniach niezbędne jest też - co podkreślają autorzy - bezpośrednie sięgnięcie do tekstów z korpusu. Reprezentacja wektorowa okazuje się wartościowym wsparciem klasycznych metod filologicznych (close reading), ale w żadnym wypadku ich nie unieważnia.

**Prompt: oceń zmianę semantyczną słowa**

Nieco inne podejście zaprezentowali autorzy i autorki opracowania *(Chat)GPT v BERT: Dawn of Justice for Semantic Change Detection* (DOI: [10.48550/arXiv.2401.14040](https://doi.org/10.48550/arXiv.2401.14040), 2024). Tutaj użyte zostały już duże modele językowe o różnej konstrukcji: BERT i Chat GPT 3.5. W momencie badania, BERT ([google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased)) był modelem *state of the art* w zadaniach analizy zmian semantycznych. Celem badania było sprawdzenie, czy do takich zadań da się wykorzystać ogólnodostępny model GPT (bezpośrednio w ramach konwersacji na stronie oraz za pomocą wysyłania żądań do API).

Oba modele różnią [istotne szczegóły konstrukcyjne](https://www.geeksforgeeks.org/nlp/gpt-vs-bert/) oraz zlecane nim standardowo zadania. Mocno upraszczając, BERT pozwala na głębokie uchwycenie (reprezentację) kontekstu danego słowa, GPT natomiast to model generatywny, zoptymalizowany pod kątem pragmatyki językowej: generowania płynnych wypowiedzi. Działanie BERT pozwala na uwzględnienie kontekstu tych słów, które poprzedzają, ale też pojawiają się po analizowanym na bieżąco słowie, GPT to model autoregresyjny, który pracuje wyłącznie na słowach poprzedzających. Warto dodać, że użycie ChatGPT w badaniu motywowane było jego szeroką dostępnością, m.in. tym, że można z niego korzystać w infrastrukturze chmurowej, bez konieczności przygotowania własnego środowiska i zapewnienia odpowiedniej mocy obliczeniowej. Co również ważne, BERT jest deterministyczny, ChatGPT - niedeterministyczny, co mocno komplikuje porównywanie wyników i reprodukowanie badań.

Efektywność BERT i ChatGPT w zadaniach LCS sprawdzano na kilka sposobów. Udostępniono modelom korpus tweetów z zadaniem wskazania, czy dane słowo zmieniło swoje znaczenie w czasie (klasyfikacja binarna w *Temporal Word-in-Context*). W zadaniu *Historical Word-in-Context* zwiększono dystans czasowy między analizowanymi tekstami (nawet do stuleci). Ostatecznie zbudowano też ranking zmian semantycznych - modele miały wyrazić za pomocą skali od 0 do 1, jak bardzo zmieniło się znaczenie wybranych słów między XIX a XX-XXI w. We wszystkich zadaniach BERT osiągnął lepsze wyniki, co można było ocenić dzięki temu, że zlecone modelom zadania zostały wcześniej wykonane przez ludzi, dostępny był więc punkt odniesienia.

```json
{
  "role": "user",
  "content": "Consider the following two time periods and target word. How much has the meaning of the target word changed between the two periods? Rate the lexical semantic change on a scale from 0 to 1. Provide only a score.\nTarget: attack\n\nTime period 1: 1810–1860\nTime period 2: 1960–2010"
},
{
  "role": "assistant",
  "content": "0.8"
},
{
  "role": "user",
  "content": "Consider the following two time periods and target word. How much has the meaning of the target word changed between the two periods? Rate the lexical semantic change on a scale from 0 to 1. Provide only a score.\nTarget: bag\n\nTime period 1: 1810–1860\nTime period 2: 1960–2010"
},
{
  "role": "assistant",
  "content": "0.8"
}
```

Fragment zestawu promptów wysyłanych do API ChatGPT z poleceniem wyznaczenia poziomu zmiany semantycznej w wybranych słowach. Źródło: [github.com/FrancescoPeriti/ChatGPTvBERT](https://github.com/FrancescoPeriti/ChatGPTvBERT)

Badanie pokazało też, jak duże znaczenie ma sposób, w jaki korzysta się z modeli w zadaniach LCS. Z modelu BERT pozyskano bezpośrednio wektory analizowanych słów i następnie je ze sobą porównywano, mierząc odległość kosinusową. Z ChatGPT skorzystano za pomocą promptów wpisywanych bezpośrednio w aplikacji webowej oraz promptów wysyłanych do interfejsu API. O ile w żądaniach API można było ustawić temperaturę modelu, w aplikacji webowej nie było już takiej opcji - to ważne, ponieważ manipulacja temperaturą może prowadzić do mniej lub bardziej zróżnicowanych odpowiedzi. Wyniki pracy z ChatGPT różniły się także w różnych stylach promptowania: zero-shot (bez przykładów), few-shot (kilka przykładów) i many-shot.

Kiedy myślę o potencjale dużych modeli językowych, możliwości generowania tekstów nie mają dla mnie większego znaczenia. Bardziej interesujące jest traktowanie ich jako reprezentacji języka, za pomocą których badać można jego cechy i ewolucję. Niekiedy propozycje odnoszące się do tej możliwości idą [bardzo daleko](https://blog.humanistyka.dev/2026/05/nie-fotografie-ale-portrety-algorytmiczne-fikcje-literackie), możliwość manipulowania datą odcięcia (zasięgiem wiedzy modelu) pozwala jednak [planować ciekawe eksperymenty](https://blog.humanistyka.dev/2026/05/vintage-large-language-models-nowe-narzedzia-badania-historii-intelektualnej). Omówione wyżej porównanie BERT z ChatGPT w kontekście analizy zmian semantycznych pokazuje też, że nie zawsze najdroższe, ogólne modele są skuteczniejsze w zadaniach językowych niż te odpowiednio sprofilowane.

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).