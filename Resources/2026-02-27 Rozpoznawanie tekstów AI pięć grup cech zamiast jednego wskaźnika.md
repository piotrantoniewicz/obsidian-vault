---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2026/02/rozpoznawanie-tekstow-ai-piec-grup-cech-zamiast-jednego-wskaznika"
source: "[[Archives/2026-02-27 Rozpoznawanie tekstów AI pięć grup cech zamiast jednego wskaźnika|2026-02-27 Rozpoznawanie tekstów AI pięć grup cech zamiast jednego wskaźnika]]"
published: 2026-02-27
created: 2026-06-14
relevance: niska
tags:
  - "LLM"
  - "narzędzia-AI"
  - "ghostwriting"
---

# Rozpoznawanie tekstów AI pięć grup cech zamiast jednego wskaźnika

[[Marcin Wilkowski]] omawia pracę Georgiosa Georgiou, który po analizie 40 badań naukowych zaproponował pięć grup wskaźników do rozpoznawania tekstów generowanych przez AI — zamiast jednego uniwersalnego detektora. Główna teza: nie istnieje i nie powstanie jeden skuteczny, powszechny sposób identyfikacji tekstów maszynowych, bo tekst jest zbyt złożonym, gatunkowo zróżnicowanym zjawiskiem. Automatyczne detektory są zawodne i dyskryminujące, a każda analiza powinna być wielowarstwowa i skrojona pod konkretny cel. Artykuł daje praktyczny szkielet do budowania własnych filtrów.

## Frameworki i metody

**5 grup wskaźników Georgiou (cue families):**

1. **Cechy powierzchniowe** — rozkład leksykalny i składniowy, statystyki stylometryczne, wskaźniki czytelności; narzędzie dla języka polskiego: [jasnopis.pl](https://jasnopis.pl)
2. **Cechy dyskursywne i pragmatyczne** — konstrukcja tekstu, organizacja retoryczna, postawa autora; teksty AI powielają szablony gatunkowe, ale inaczej niż ludzie konstruują wypowiedź
3. **Cechy epistemiczne i treściowe** — ugruntowanie w faktach, obecność halucynacji, wiarygodność odwołań do własnych doświadczeń, jakość dowodów
4. **Cechy przewidywalności i probabilistyczne** — statystyczna regularność doboru kolejnych słów (niska entropia); wymaga oprogramowania, sens głównie w dłuższych tekstach
5. **Cechy pochodzenia** — znaki wodne zapisane we wzorcu doboru słów (np. [[SynthID]] od [[Google Gemini]])

## Wnioski

- Brak jednego "podpisu AI" — skuteczność wykrywania zależy od gatunku tekstu, jego długości i tego, czy autor aktywnie próbuje obejść detekcję (parafrazowanie, instrukcje stylu)
- Analiza powinna być profilowana: każda z pięciu grup ma inne ograniczenia, np. stylometria działa na krótkich tekstach, probabilistyczna wymaga długich
- Detektory komercyjne fałszywie klasyfikują teksty nienatywnych użytkowników języka jako generowane przez AI — szkoda dla osób ocenianych na tej podstawie

## Cytat

> Nie istnieje pojedynczy, stabilny "podpis AI" — możliwość wykrycia tekstów generowanych maszynowo wynika z warstwowych grup wskazówek, których przydatność zależy od ograniczeń gatunkowych, procesu rewizji oraz warunków adwersarialnych.

## Zastosowanie

W szkoleniach z AI dla NGO artykuł dobrze ilustruje, dlaczego nie warto polegać na automatycznych detektorach i jak zamiast nich budować własne kryteria oceny jakości treści. Dla ghostwritera — pięć grup wskaźników to lista kontrolna przy redakcji tekstów pisanych z pomocą AI, szczególnie grupy 1 (powierzchniowe) i 3 (epistemiczne). Potencjalnie przydatne przy tworzeniu wewnętrznych standardów jakości treści dla NGO-klientów.
