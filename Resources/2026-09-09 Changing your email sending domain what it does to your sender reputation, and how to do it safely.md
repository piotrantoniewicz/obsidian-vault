---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/changing-your-email-sending-domain-what-it-does-to-your-sender-reputation-and-how-to-do-it-safely?utm_medium=email&_hsenc=p2ANqtz-9KIFr353MSvtW-CRWZsrI0gyif2gfnVm_5v7eK-t4cXyBQTUJgJ_LId0lrTQTBkWXAPfpSIXAxIemEdltI2MI6DT1NfqpFGAJ-RHeeCI9jJauyvNI&_hsmi=145370304&utm_content=145358476&utm_source=hs_email"
source: "[[Archives/2026-09-09 Changing your email sending domain what it does to your sender reputation, and how to do it safely|2026-09-09 Changing your email sending domain what it does to your sender reputation, and how to do it safely]]"
published: 2026-09-09
created: 2026-09-10
relevance: średnia
tags:
  - "digital-campaigning"
  - "narzędzia-AI"
---

# Changing your email sending domain: what it does to your sender reputation, and how to do it safely

Artykuł [[Beth O'Malley]] tłumaczy, dlaczego zmiana domeny wysyłkowej to jedna z najbardziej ryzykownych decyzji w programie e-mailowym — reputacja domeny buduje się latami, a nowa domena zaczyna od zera, co filtry providerów odczytują jako sygnał spamowy. Autorka rozróżnia sytuacje, w których zmiana domeny jest uzasadniona (rebranding, fuzja, rozdzielenie strumieni wysyłki) od tych, w których nie jest (ucieczka od nierozwiązanego problemu reputacyjnego, chęć krótszej nazwy). Druga część artykułu to szczegółowy playbook migracji: kolejność działań, warming domeny przez tygodnie/miesiące i utrzymanie starej domeny jako fallbacku. Tekst ma wartość praktyczną dla każdego, kto zarządza wysyłką e-mail w imieniu organizacji lub klienta.

## Frameworki i metody

**Struktura domen wysyłkowych:**
- Domena główna/organizacyjna — obsługuje stronę, pocztę korporacyjną, faktury; powinna być chroniona przed wysyłką masową
- Subdomena — buduje własną reputację, ale dziedziczy politykę DMARC z domeny głównej i jest częściowo zależna od jej kondycji na starcie
- Adres from vs return path — reputacja jest oceniana na obu, dlatego liczy się ich spójność (alignment)

**9-krokowa sekwencja bezpiecznej migracji domeny:**
1. Skonfiguruj i zweryfikuj autentykację (SPF, DKIM, DMARC) na nowej domenie
2. Ustal strukturę (które strumienie gdzie) przed pierwszą wysyłką
3. Zostaw starą domenę aktywną jako fallback
4. Zacznij od najbardziej zaangażowanych odbiorców, w małym wolumenie
5. Zwiększaj wolumen stopniowo przez tygodnie, monitorując codziennie
6. Dziel wolumen między starą i nową domenę w trakcie przejścia
7. Poinformuj odbiorców o zmianie adresu z poziomu starej domeny
8. Zaktualizuj wszystkie formularze, linki i automatyzacje odwołujące się do starego adresu
9. Wygaś starą domenę dopiero po pełnym ugruntowaniu nowej — rekordy DNS zostaw aktywne

**Timeline migracji wstecz od daty cutover:** 3-6 miesięcy przed = struktura i autentykacja; 8-12 tygodni = start warmingu; 4-8 tygodni = wysyłka równoległa; 2-4 tygodnie = komunikat do odbiorców; cutover = większość wolumenu na nowej domenie; 3 miesiące po = dopiero wtedy rozważ wygaszenie starej.

## Wnioski

- Zmiana domeny nie naprawia problemu z wysyłką, tylko go przenosi — ten sam zły nawyk wysyłkowy zniszczy nową domenę szybciej, bo nie ma ona zgromadzonej historii dobrego zachowania.
- Warming to nie formalność wykonywana przez narzędzie, tylko tygodnie konsekwentnego, stopniowego budowania zaufania u wielu providerów jednocześnie — automatyczne narzędzia do warmingu uczą filtry złych wzorców.
- Nigdy nie przeprowadzaj migracji domeny w okresie szczytowej wysyłki (peak) — to najgorszy możliwy moment na budowanie reputacji od zera.

## Zastosowanie

Praktyczny materiał referencyjny przy doradztwie klientom NGO planującym rebranding lub konsolidację wysyłki e-mail — checklistę migracji (9 kroków + timeline) można wykorzystać bezpośrednio jako punkt wyjścia do audytu lub planu wdrożenia.
