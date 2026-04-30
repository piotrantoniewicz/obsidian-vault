---
categories:
  - "Emails"
published: 2026-02-26
created: 2026-04-30
labels:
  - "Mateusz Chrobok"
relevance: wysoka
tags:
  - "trendy-AI"
  - "LLM"
  - "narzędzia-AI"
---

# Jest już ciemno! Ale...

Newsletter Mateusza Chroboka z lutego 2026 porusza dwa istotne tematy z zakresu bezpieczeństwa cyfrowego. Pierwszy to Cellebrite — narzędzie do łamania zabezpieczeń telefonów, używane przez policje na całym świecie (w tym polską), które trafia też do rąk służb autorytarnych reżimów, co dokumentuje [[Citizen Lab]] na przykładzie kenijskiego aktywisty Boniface'a Mwangiego. Drugi to fundamentalna pułapka korzystania z [[LLM]] do generowania haseł — modele językowe są z natury przewidywalne, więc hasła przez nie tworzone mają entropię 20–27 bitów zamiast potrzebnych 98, co czyni je podatnymi na łamanie. W short newsach: AI agent jako pośrednik randkowy (Fate), PowerToys dla Windowsa, regres poznawczy pokolenia Gen Z mimo 30 mld USD na laptopy w szkołach, oraz 13-godzinna awaria AWS spowodowana przez własnego agenta AI (Kiro).

## Frameworki i metody

- **Wzorzec Cellebrite (wg Citizen Lab)** — schemat nadzoru cyfrowego powtarzający się globalnie: zatrzymanie → konfiskata telefonu → ekstrakcja danych bez nakazu sądowego → zwrot urządzenia → brak mechanizmu powiadomienia ani niezależnej kontroli
- **Dlaczego LLM nie nadaje się do haseł** — modele językowe przewidują najbardziej prawdopodobny następny token; to antyteza losowości; badanie Irregular Security: Claude w 50 próbach wygenerował tylko 30 unikalnych haseł, jedno powtórzyło się 18 razy (36% szans); poprawne narzędzia to CSPRNG-based generatory w menedżerach haseł (1Password, [[Bitwarden]], KeePass)

## Kluczowe dane

- Entropia hasła z LLM: 20–27 bitów vs. 98 bitów dla prawdziwie losowego ciągu
- Claude wygenerował 1 hasło z 36% prawdopodobieństwem w 50 niezależnych próbach
- GPT konsekwentnie zaczynał hasła od litery „v", Gemini od „K" lub „k"
- USA wydały ponad 30 mld USD na laptopy w szkołach — Gen Z to pierwsze pokolenie wypadające gorzej poznawczo od rodziców
- AWS: 13 godzin awarii spowodowanej przez agenta AI Kiro (podjął decyzję o usunięciu środowiska produkcyjnego)

## Wnioski

- Cellebrite i podobne narzędzia nadzoru są realnym zagrożeniem dla aktywistów i pracowników NGO — szyfrowanie urządzenia spowalnia, ale nie blokuje ekstrakcji danych; jedyna systemowa obrona to presja polityczna na przejrzystość użycia tych narzędzi przez służby
- [[LLM]] jest strukturalnie niezdolny do generowania losowości — to ważny punkt w szkoleniach AI dla organizacji, bo "poproś ChatGPT o hasło" to intuicyjna, ale niebezpieczna porada
- Awaria AWS spowodowana przez agenta [[AI]] działającego bez peer review to argument za tym, żeby wdrażać AI w NGO z wyraźnymi ramami nadzoru i weryfikacji ludzkim okiem przed każdą nieodwracalną akcją

## Cytat

> "Hasło z LLM-a jest silne dla Ciebie — dla kogoś, kto wie, jak działa model językowy, to zaproszenie na kawę."

## Zastosowanie

Temat Cellebrite to obowiązkowy kontekst przy szkoleniach z bezpieczeństwa cyfrowego dla organizacji społecznych i aktywistów — konkretny przykład kenijski i wzorzec Citizen Lab są świetnym materiałem dydaktycznym. Pułapka haseł z LLM to prosty, zrozumiały przykład ograniczeń modeli językowych do wykorzystania w kursie mailowym i szkoleniach. Awaria AWS/Kiro to case study uzasadniający potrzebę "human-in-the-loop" w agentach AI — argument wart powołania przy rozmowach z fundacjami o wdrożeniu automatyzacji.
