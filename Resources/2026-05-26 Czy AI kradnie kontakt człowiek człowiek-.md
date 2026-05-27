---
categories:
  - "Emails"
published: 2026-05-26
created: 2026-05-27
labels:
  - "Mirek Burnejko"
relevance: wysoka
tags:
  - "prompt-engineering"
  - "strategia-AI"
  - "narzędzia-AI"
---

# Czy AI kradnie kontakt człowiek człowiek?

Newsletter Mirka Burnejki z [[AI Biznes Lab]] porusza trzy tematy: metodologię budowania efektywnych promptów, model zarządzania firmą oparty na agentach AI z dostępem do kontekstu i narzędzi, oraz pytanie o przyszłość komunikacji człowiek-człowiek w zautomatyzowanych miejscach pracy. Burnejko argumentuje, że AI nie zastępuje kontaktu między ludźmi, lecz eliminuje komunikację o niskiej wartości — statusy, lokalizację pliku, odtwarzanie kontekstu. Kluczowe jest budowanie pamięci agenta poprzez akumulowanie reguł, przykładów i decyzji firmowych, co z czasem pozwala na automatyzację powtarzalnych spraw.

## Frameworki i metody

### 6-krokowy proces tworzenia skutecznego promptu
- **Krok 1: Znajdź działający prompt** — zbierasz prompty z sieci, wybierasz taki który pasuje do Twojego zadania, firmy i stylu pracy
- **Krok 2: Poproś AI o dopasowanie** — wrzucasz prompt do [[ChatGPT]] lub [[Claude]] z konkretnym celem (nie ogólnym „ulepsz"); pomocny jest długi wywód głosowy np. przez [[SuperWhisper]]
- **Krok 3: Testuj** — sprawdzasz w kilku scenariuszach; jeśli nie działa — wracasz do kroku 2 z feedbackiem
- **Krok 4: Zrób research** — prosisz AI o pytania do Deep Research, sprawdzasz dokumentację dostawców AI i wiedzę domenową; wykonujesz research w ChatGPT Deep Research, Claude Research lub Gemini Deep Research
- **Krok 5: Wróć z wynikami** — łączysz przetestowany prompt z wynikami researchu i prosisz AI o nową wersję
- **Krok 6: Testuj drugi raz** — jeśli nowa wersja przewyższa poprzednią, masz gotowy prompt

### Model pracy agentowej w firmie
- **Warstwa 1: Automatyzacja zadań** — agent zbiera kontekst i przygotowuje opcje + rekomendację; sam wykonuje zadanie jeśli mieści się w zdefiniowanych granicach
- **Warstwa 2: Komunikacja agent–agent** — agenty różnych pracowników wymieniają się kontekstem; decyzja człowieka potrzebna tylko przy potwierdzeniu kluczowego kontekstu
- **Warstwa 3: Interfejs pracy zespołowej** — dwie osoby w [[Claude Code]] lub Codex ze wspólnym kontekstem; kolejny etap to integracja ze [[Slack]], CRM i bazą wiedzy

## Wnioski
- [[Prompt engineering]] to nie posiadanie „magicznego prompta" — to iteracyjny proces łączący testowanie z Deep Research i dostosowaniem do konkretnego kontekstu pracy
- Agenty AI z dostępem do narzędzi i kontekstu zmieniają charakter pracy zespołowej — eliminują komunikację o niskiej wartości, nie relacje między ludźmi
- Wdrożenie modelu agentowego warto zacząć od jednej relacji 1:1, dając obu agentom dostęp do wspólnego kontekstu, a dopiero potem skalować na całą organizację

## Cytat
> Prompt nie jest produktem. Produktem jest proces poprawiania pracy.

## Zastosowanie
6-krokowy proces promptowania to gotowy framework do przekazania organizacjom w ramach szkoleń — szczególnie krok 4 (research z AI) i krok 2 (głosowy kontekst przez [[SuperWhisper]]) mogą być przystępne dla mniej technicznych odbiorców w NGO. Model pracy agentowej opisany przez Burnejkę to praktyczna inspiracja do projektowania automatyzacji dla klientów [[dobryai.pl]], szczególnie w małych firmach — warto testować ten schemat w ramach własnej pracy z [[Claude Code]] i [[Make.com]].
