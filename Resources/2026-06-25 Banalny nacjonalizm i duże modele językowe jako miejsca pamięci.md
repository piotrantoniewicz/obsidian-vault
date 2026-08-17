---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2026/06/banalny-nacjonalizm-i-duze-modele-jezykowe-jako-miejsca-pamieci?utm_source=newsletter"
source: "[[Archives/2026-06-25 Banalny nacjonalizm i duże modele językowe jako miejsca pamięci|2026-06-25 Banalny nacjonalizm i duże modele językowe jako miejsca pamięci]]"
published: 2026-06-25
created: 2026-08-05
relevance: średnia
tags:
  - "LLM"
  - "framing"
  - "trendy-AI"
---

# Banalny nacjonalizm i duże modele językowe jako miejsca pamięci

Marcin Wilkowski omawia preprint *Same question, different history: language, national identity, and credit in large language models*, który bada, jak duże modele językowe odpowiadają na pytania o autorstwo wynalazków w zależności od języka zapytania. Autorzy pokazują, że modele wykazują „wewnątrzjęzykową przewagę" — częściej przypisują wynalazek postaci narodowej, gdy pytanie zadane jest w jej rodzimym języku, co traktują jako przejaw narodowych „miejsc pamięci" w rozumieniu [[Pierre Nora]]. Zjawisko koreluje ze „śladem instytucjonalnym" danej postaci w jej kraju (pomniki, banknoty, święta), a autorzy łączą je z koncepcją banalnego nacjonalizmu [[Michael Billig]] — modele nieświadomie powielają narodowe uprzedzenia zawarte w danych treningowych. To ważne, bo pokazuje, że stronniczość LLM-ów nie jest tylko błędem do naprawienia, ale też źródłem wiedzy o tym, jak kultury narodowe konstruują pamięć i znaczenie.

## Kluczowe dane
- Pytanie o wynalazcę ruchomej czcionki po chińsku: 98% odpowiedzi wskazuje Bi Shenga vs 79% w innych językach (różnica 19 p.p.)
- Aleksandr Popow jako wynalazca radia: 85% wskazań po rosyjsku vs 48% w innych językach
- Badanie objęło 11 modeli (m.in. [[GPT-4o]], [[Claude AI|Claude]], [[Gemini]], [[DeepSeek]], [[Qwen]], [[Mistral]]) z trzech regionów (USA, Chiny, Europa), 21 wynalazków i 12 języków

## Wnioski
- Stronniczość językowa LLM-ów nie jest przypadkowa — odzwierciedla nierównomierną obecność postaci historycznych w tekstach narodowych, co można wykorzystać jako wskaźnik kulturowej pamięci, a nie tylko jako wadę do usunięcia.
- Postaci o uniwersalnym statusie (np. Newton, bracia Wright) są przywoływane niezależnie od języka promptu, podczas gdy postaci mniej znane globalnie ujawniają silną zależność od języka zapytania — to ma znaczenie przy projektowaniu treści wielojęzycznych i ocenie, czyj punkt widzenia model faktycznie reprezentuje.
- Modele językowe, trenowane na tekstach narodowych, współkształtują banalny nacjonalizm [[Michael Billig]] poprzez rutynowe, niezauważalne przypisywanie atrybucji zgodnie z perspektywą narodową.

## Cytat
> Postaci o niższym statusie, nieanglojęzyczni są wymieniani wyraźnie częściej w powiązanym z nimi języku, podczas gdy globalnie rozpoznawane w zachodniej kulturze postaci wymieniane są z częstością na poziomie bliskim maksimum niezależnie od języka.

## Zastosowanie
Przydatne jako materiał do szkoleń o ograniczeniach i stronniczości AI — dobry przykład na to, że odpowiedzi modelu zależą od języka zapytania, co ma znaczenie przy tworzeniu treści wielojęzycznych dla organizacji społecznych i przy ocenie, na czyją narrację/framing model się domyślnie „przechyla".
