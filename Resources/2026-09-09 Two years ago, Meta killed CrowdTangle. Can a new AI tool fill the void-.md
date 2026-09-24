---
authors:
  - '[[Andre Deck]]'
categories:
  - Clippings
created: '2026-09-24'
published: '2026-09-09'
relevance: wysoka
source: >-
  [[Archives/2026-09-09 Two years ago, Meta killed CrowdTangle. Can a new AI
  tool fill the void-|2026-09-09 Two years ago, Meta killed CrowdTangle. Can a
  new AI tool fill the void-]]
tags:
  - narzędzia-AI
  - digital-campaigning
  - LLM
url: >-
  https://www.niemanlab.org/2026/09/two-years-ago-meta-killed-crowdtangle-can-a-new-ai-tool-fill-the-void/?utm_campaign=WGIT&utm_medium=email&_hsenc=p2ANqtz--bzAEQKxwBd2vyW1Z3hATTUWpNGGdnnl_KtABcX64qvgnV2PJFIvCbvplzcuQGtgTvG62kbFtHum0eeZtCkmjQc4c7wtrttiBsdGHIm_nUYEovF5k&_hsmi=38096778&utm_content=38096778&utm_source=hs_email
---
# Two years ago, Meta killed CrowdTangle. Can a new AI tool fill the void?

## Synteza
Nieman Lab opisuje Arbiter — narzędzie non-profitu SimPPL, które ma zapełnić lukę po zamkniętym przez Metę CrowdTangle. Arbiter zbiera posty z wielu platform (Facebook, Instagram, X, YouTube, TikTok, Reddit, Bluesky, 4chan) i zamiast opierać się na jednym dużym modelu językowym, łączy osiem do dziesięciu wyspecjalizowanych modeli AI do różnych zadań — od wykrywania słów kluczowych, przez klasteryzację narracji, po mapowanie sieci kont. Kluczowa różnica względem klasycznych narzędzi social listeningu: Arbiter ma wyprzedzać eskalację szkodliwej narracji, a nie tylko alarmować, gdy już „wybuchnie” — co jest kluczowe dla dziennikarzy i fact-checkerów, nie tylko dla PR-u. To dobra ilustracja tego, jak krucha bywa infrastruktura civic-tech zależna od dobrej woli platform, i jak wygląda realistyczna architektura AI do takich zastosowań.

## Frameworki i metody
Stos technologiczny Arbitera nie opiera się na jednym modelu, tylko na wielu wyspecjalizowanych warstwach, między którymi rozkładane jest zadanie:
- kodowanie zapytania użytkownika (żeby wyszukiwanie rozumiało kontekst, a nie tylko dopasowywało słowa),
- dobór właściwych postów do pobrania,
- identyfikacja skoordynowanych sieci kont wewnątrz tych postów,
- podobieństwo semantyczne między treściami,
- mapowanie sieci (kto z kim i jak się łączy).

Część z tych warstw jest niezależna od konkretnego dostawcy modelu — newsroomy mogą wybrać preferowanego dostawcę [[LLM]].

## Kluczowe dane
- Użytkownicy z ponad 100 organizacji zarejestrowali się do testowania Arbitera; wśród pierwszych newsroomów: Deutsche Welle, Chequeado (Argentyna) i Rappler (Filipiny).
- Narzędzie jest obecnie udostępniane redakcjom bezpłatnie — SimPPL dopiero szuka modelu przychodowego, świadomie unikając modelu subskrypcyjnego niedostępnego dla niedofinansowanych redakcji.

## Wnioski
- Zamknięcie [[CrowdTangle]] przez [[Meta]] pokazało, że infrastruktura monitoringu dezinformacji zależna od jednego dostawcy platformowego jest krucha — Arbiter odpowiada na to własnym, wielomodelowym stosem zamiast uzależnienia od jednego dostawcy LLM.
- Zwykłe „wrzucenie” dużego zbioru danych social media do pojedynczego LLM nie działa w praktyce — jak mówi współtwórca Arbitera, ponad 100 tysięcy postów bez odpowiedniej warstwy kontekstowej „blows up your credit card bill and gives you garbage outputs you can't control”.
- Ambicja narzędzia to wyprzedzanie eskalacji szkodliwych narracji, a nie tylko alarmowanie po fakcie — różnica między pracą dziennikarską/fact-checkingową a klasycznym social listeningiem budowanym z myślą o PR i marketingu.

## Cytat
> Każdy, kto miał do czynienia z ponad 100 tysiącami danych, wie, że wrzucenie ich prosto do LLM najpierw wysadza rachunek za API, a potem daje śmieciowe wyniki, których nie da się kontrolować.

## Zastosowanie
Dobry przykład do rozmów z klientami NGO o realistycznych oczekiwaniach wobec wdrożeń AI do monitoringu treści czy dezinformacji — pokazuje, że pojedynczy duży model to za mało i potrzebna jest przemyślana architektura wielu wyspecjalizowanych modeli dopasowanych do etapów procesu.
