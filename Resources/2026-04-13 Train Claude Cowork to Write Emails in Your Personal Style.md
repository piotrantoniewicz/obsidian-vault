---
categories: Clippings
authors: ["[[ChatPRD]]"]
url: https://www.chatprd.ai/how-i-ai/workflows/train-claude-cowork-to-write-emails-in-your-personal-style
source: "[[Archives/2026-04-13 Train Claude Cowork to Write Emails in Your Personal Style|2026-04-13 Train Claude Cowork to Write Emails in Your Personal Style]]"
published: 2026-04-13
created: 2026-04-13
relevance: wysoka
tags:
  - "automatyzacja"
  - "prompt-engineering"
  - "ghostwriting"
---

# Train Claude Cowork to Write Emails in Your Personal Style

Krótki, praktyczny przewodnik [[ChatPRD]] pokazuje jak w trzech krokach nauczyć [[Claude Cowork]] pisać maile w swoim osobistym stylu — poprzez podłączenie Gmaila jako konektora, analizę wysłanych wiadomości z ostatnich 30 dni i automatyczne wygenerowanie "writing skill" zachowującego styl pisania właściciela. Kluczową zasadą bezpieczeństwa jest globalna instrukcja zabraniająca Coworkowi samodzielnego wysyłania maili — narzędzie tworzy wyłącznie szkice do akceptacji. Workflow pokazuje jak przekształcić własne dane (archiwum maili) w spersonalizowane narzędzie AI, które nie naśladuje generycznego stylu, ale faktycznie uczy się indywidualnego tonu komunikacji.

## Frameworki i metody

- **Workflow: email style skill w 3 krokach**:
  1. Podłącz Gmail connector w [[Claude Cowork]] z uprawnieniami do odczytu wysłanych wiadomości
  2. Wydaj polecenie analizy maili z ostatnich 30 dni i stworzenia writing skill na podstawie własnego stylu — przykładowy prompt: *"Analyze my Gmail specifically the emails that I have sent in the last 30 days, and use this to create a writing skill specifically for emails"*
  3. Cowork generuje style guide i voice profile zapisany jako skill; dodaj globalną instrukcję: *"Never send emails on my behalf. Only write them as drafts for me to review"*

## Wnioski

- Własne archiwum maili to gotowy dataset treningowy dla personalizowanego [[ghostwriting]]owego asystenta AI — nie potrzeba żadnego dodatkowego przygotowania danych
- Instrukcja "tylko szkice, nigdy wysyłaj" to wzorzec bezpiecznego wdrażania AI do komunikacji, który warto stosować domyślnie i propagować wśród NGO wdrażających AI
- [[Claude Cowork]] Skills to mechanizm, który zamienia jednorazową analizę w trwałe, wielokrotnie używalne zachowanie narzędzia — to fundamentalnie różni go od jednorazowych promptów

## Zastosowanie

Workflow można zastosować natychmiast — podłączyć Gmail i stworzyć writing skill dla własnych maili, co przyspieszy komunikację i zachowa spójność tonu. To dobry przykład do pokazania uczestnikom szkoleń [[dobryai.pl]] jak używać własnych danych do personalizacji AI bez wiedzy technicznej. Warto też przetestować ten mechanizm jako element oferty dla klientów konsultingowych — pomoc w stworzeniu spersonalizowanego asystenta mailowego jako szybka wygrana na start współpracy.
