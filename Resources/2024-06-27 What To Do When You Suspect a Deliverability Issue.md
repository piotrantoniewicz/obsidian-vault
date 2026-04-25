---
categories: Clippings
authors: ["[[Lauren Meyer]]"]
url: https://send-it-right.com/blog/what-to-do-with-deliverability-issues
published: 2024-06-27
created: 2026-04-24
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "content-marketing"
source: "[[Archives/2024-06-27 What To Do When You Suspect a Deliverability Issue|2024-06-27 What To Do When You Suspect a Deliverability Issue]]"
---

# What To Do When You Suspect a Deliverability Issue

[[Lauren Meyer]] prowadzi przez pełny proces diagnozowania i naprawy problemów z dostarczalnością maili — od rozpoznania symptomów, przez identyfikację przyczyny, po konkretne działania naprawcze. Artykuł podkreśla kluczową różnicę między *delivery rate* a *deliverability rate*: wiele organizacji przez długi czas nie wie, że ich maile lądują w spamie, bo metryki „dostarczenia" wyglądają normalnie. Główne przyczyny problemów to niska jakość listy, nieodpowiednia autentykacja domeny (SPF, DKIM, DMARC) i brak właściwego ocieplania nowych domen i IP. Meyer jasno wskazuje, że reputacja nadawcy jest coraz mocniej powiązana z domeną, a nie IP — co oznacza, że nie można uciec od złej reputacji przez zmianę ESP czy adresu IP.

## Frameworki i metody

**Diagnoza problemu deliverability — kolejność kroków:**

1. **Oceń zasięg problemu** — czy problem dotyczy jednego dostawcy poczty (np. Hotmail) czy wszystkich? Czy to pojedynczy zgłoszony przypadek czy fala skarg?
2. **Zidentyfikuj przyczynę** — gdzie się pojawia (który mailbox provider), kiedy się zaczęło (szukaj punktu infleksji w danych), czy można go odtworzyć, co się zmieniło przed pojawieniem się problemu
3. **Działaj** — napraw konkretną przyczynę zamiast zmieniać dostawcę; skontaktuj się z ESP po własnej analizie; jeśli potrzeba — złóż zgłoszenie do mailbox providera lub operatora bloklisty

**Najczęstsze przyczyny problemów:**
- Niska jakość listy (nieoczekiwane maile, stare listy)
- Słabe zarządzanie subskrybentami
- Skupienie tylko na otwarciach i kliknięciach bez uwzględnienia konwersji
- Przestarzałe praktyki zbierania zgód
- Brak autentykacji domeny (SPF, DKIM, DMARC)

## Wnioski

- Autentykacja domeny (SPF, DKIM, DMARC) to dziś wymóg Google i Yahoo, nie opcja — brak jej konfiguracji skutkuje problemami z dotarciem do skrzynek odbiorców
- Reputacja nadawcy jest coraz mocniej przypisana do domeny, co oznacza, że złe praktyki mailowe NGO odbiją się na całej komunikacji organizacji, nie tylko na kampaniach email
- Problemy z dostarczalnością mogą przez długi czas pozostawać niezauważone — warto aktywnie monitorować metryki zaangażowania (kliknięcia, konwersje), a nie tylko open rate

## Zastosowanie

Przy prowadzeniu kampanii fundraisingowych i email-to-target dla NGO znajomość tych zasad pozwala wcześniej wychwycić problemy i edukować klientów, zanim wpadną w spiralę spadającej reputacji. Warto włączyć temat autentykacji i zarządzania listą do oferty konsultingowej jako element audytu przed większymi kampaniami. Artykuł może służyć jako materiał roboczy przy kursie mailowym dla organizacji — szczególnie sekcja o najczęstszych przyczynach problemów i kolejności kroków diagnostycznych.
