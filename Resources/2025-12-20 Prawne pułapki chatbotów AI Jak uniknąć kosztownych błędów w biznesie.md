---
categories: Clippings
authors: ["[[Kasia Krzywicka]]"]
url: https://www.youtube.com/watch?v=csZ0K42vkkA
source: "[[Archives/2025-12-20 Prawne pułapki chatbotów AI Jak uniknąć kosztownych błędów w biznesie|2025-12-20 Prawne pułapki chatbotów AI Jak uniknąć kosztownych błędów w biznesie]]"
published: 2025-12-20
created: 2026-04-22
relevance: średnia
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "automatyzacja"
---

# Prawne pułapki chatbotów AI Jak uniknąć kosztownych błędów w biznesie?

[[Kasia Krzywicka]], adwokat specjalizująca się w prawie AI i nowych technologii, omawia ryzyka prawne związane z wdrożeniem chatbotów w firmach i organizacjach. Główna teza: chatbot to nie wtyczka do zainstalowania w piątek południe — każde wdrożenie wymaga analizy RODO, [[AI Act]], prawa cywilnego i ograniczeń samej technologii. Szczególnie istotne jest to, że halucynacje [[LLM]] nie są błędem do wyeliminowania przez prompt ani [[RAG]] — to immanentna cecha architektury modeli językowych. Wdrażający chatboty odpowiadają prawnie za skutki ich działań, w tym za umowy zawarte przez AI w imieniu firmy.

## Frameworki i metody

Trzy rodzaje rozwiązań chatbotowych i ich ryzyka:

- **No-code SaaS** (np. [[Botpress]], [[Voiceflow]]) — gotowe platformy, szybkie wdrożenie, mała kontrola nad systemem; ryzyko RODO zależy od dostawcy i wymaga weryfikacji umów powierzenia
- **Low-code** — hybrydowe rozwiązania z automatyzacjami i logiką warunkową; średnie ryzyko RODO, ograniczona kontrola nad danymi
- **Custom code** — pełna kontrola nad logiką, danymi i bezpieczeństwem; najwyższy koszt i czas wdrożenia, najniższe ryzyko prawne przy właściwej implementacji

Trzy typy halucynacji [[LLM]] (za badaniem ACL 2025 "Fantastic LLMs and Where to Find Them"):

- **Typ A** — model miał dostęp do prawdziwego faktu, ale i tak podał błędną odpowiedź
- **Typ B** — model powtórzył błędne lub wyrwane z kontekstu informacje dostarczone przez użytkownika
- **Typ C** — model sam wymyślił informację, której nie było w bazie (najczęstszy typ)

## Kluczowe dane

- Badanie ACL (2025): nawet najnowsze modele generują wysoki odsetek nieprawdziwych faktów, szczególnie w tematach specjalistycznych (prawo, medycyna, technika)
- Kanadyjskie linie lotnicze przegrały sprawę sądową — chatbot poinformował klienta o nieistniejącej zniżce; sąd uznał to za wiążące zobowiązanie firmy

## Wnioski

- Halucynacje są cechą architektury [[LLM]], a nie błędem — żaden prompt ani baza [[RAG]] nie eliminuje ich całkowicie, co ma bezpośrednie konsekwencje prawne dla właściciela chatbota
- [[AI Act]] wymaga poinformowania użytkownika, że rozmawia z AI, najpóźniej przy pierwszej interakcji — nie wystarczy wzmianka w regulaminie małym drukiem
- Chatbot może skutecznie zawrzeć umowę w imieniu firmy na mocy prawa cywilnego — "disclaimery" wyłączające odpowiedzialność mogą nie mieć mocy prawnej w relacjach B2C

## Cytat

> Chatboty wymagają weryfikacji cały czas, sprawdzania, testowania — i naprawdę takiego zastanowienia się, zrobienia kroku w tył, zanim zrobimy kolejne kroki do przodu.

## Zastosowanie

Przy doradzaniu NGO i firmom w zakresie wdrożeń AI warto aktywnie poruszać kwestie prawne — szczególnie RODO, transparentność AI Act i odpowiedzialność za działania chatbotów. Temat halucynacji i odpowiedzialności prawnej to gotowy moduł dydaktyczny do kursu "Fundraising z AI" lub szkoleń dla organizacji. Przed rekomendowaniem narzędzi chatbotowych klientom dobrze mieć własną checklistę weryfikacyjną opartą o te ryzyka.
