---
categories: Clippings
authors: ["[[Lauren Meyer]]"]
url: https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/
source: "[[Archives/2023-12-15 New Google and Yahoo Email Standards Your First 2024 Priority|2023-12-15 New Google and Yahoo Email Standards Your First 2024 Priority]]"
published: 2023-12-15
created: 2026-05-04
relevance: średnia
tags:
  - "digital-campaigning"
  - "fundraising"
---

# New Google and Yahoo Email Standards Your First 2024 Priority

Od lutego 2024 roku Google i Yahoo wymagają od nadawców masowych wiadomości spełnienia nowego zestawu standardów uwierzytelniania (SPF, DKIM, DMARC) oraz wdrożenia jednoklknięciowego wypisywania się z list. Wymogi są odpowiedzią na rosnące koszty przechowywania spamu i ryzyko nadużyć domen w kampaniach phishingowych. Dla organizacji nadal wysyłających z adresów @gmail.com zmiana jest pilna — muszą przejść na własną domenę lub subdomenę powiązaną z marką, inaczej ich wiadomości trafią do spamu. Autorka podkreśla, że spełnienie wymogów to jedynie minimum wejścia — prawdziwym celem jest budowanie zaufania nadawcy przez dostarczanie wartościowych, oczekiwanych wiadomości.

## Frameworki i metody

- **Uwierzytelnienie (trójca email)** — SPF + DKIM + DMARC muszą być skonfigurowane; DMARC może być ustawiony na p=none, ale rekord musi być obecny; dla bulk senderów (>5000 dziennie) wymagane jest pełne wyrównanie domeny
- **Progi skarg spam** — cel <0,1%, absolutne maksimum 0,3%; monitorowane przez [[Google Postmaster Tools]]; przekroczenie grozi degradacją reputacji IP i domenowej
- **One-click list-unsubscribe** — wymagany w nagłówkach wiadomości (nie tylko link w treści); umożliwia natychmiastowe wypisanie jednym kliknięciem; organizacja musi honorować w ciągu 2 dni (wcześniej CAN-SPAM dawał 10 dni)
- **PTR records (forward/reverse DNS)** — wymagane dla wszystkich domen i adresów IP wysyłających pocztę; weryfikują autentyczność serwera nadawcy

## Wnioski

- Wysyłanie z @gmail.com po lutym 2024 skutkuje trafieniem do spamu — przejście na własną domenę lub subdomenę to konieczność dla każdej organizacji prowadzącej kampanie emailowe
- [[DMARC]] to nowy baseline email marketingu — organizacje bez tego rekordu stają się łatwym celem phishingu i tracą reputację domeny nawet jeśli same nie wysyłają spamu
- Ułatwienie wypisywania się paradoksalnie zmniejsza skargi spam — warto wyjaśniać tę logikę klientom NGO, którzy boją się, że jeden klik spowoduje masowy odpływ subskrybentów

## Zastosowanie

Piotr prowadzi kampanie email-to-target i fundraisingowe dla NGO — znajomość tych wymogów jest niezbędna przy doradzaniu organizacjom w kwestii infrastruktury emailowej. Kurs "Fundraising z AI" powinien zawierać moduł o technikaliach dostarczalności jako fundament skutecznych kampanii. Warto rutynowo sprawdzać, czy organizacje partnerskie mają prawidłowo skonfigurowane rekordy SPF/DKIM/DMARC przed uruchomieniem jakiejkolwiek kampanii.
