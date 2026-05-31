---
type: "Web"
authors: "[[Przemek Jurgiel-Zyla]]"
url: "https://www.linkedin.com/pulse/18-podstawyai-czyli-uruchom-bielika-na-swoim-manual-jurgiel-zyla-ob8vf/"
published: 2025-06-17
created: 2026-05-31
tags:
  - "narzędzia-AI"
  - "LLM"
  - "szkolenia-AI"
---


### Dzisiaj chciałbym Cię zaprosić do uruchomienia razem ze mną najlepszego polskiego modelu językowego, czyli Bielika - i tak, imho każdy będzie potrafił to zrobić!

> ale zanim zaczniemy - zaobserwuj mnie - codziennie pisze o AI, inwestycjach VC oraz technologiach / a jeśli interesuje Cię szkolenie z #podstawyAI, to zapraszam na [**https://podstawy.ai**](https://podstawy.ai/), gdzie można się zapisać na listę oczekujących (kolejna edycja wkrótce)

**I druga uwaga: nie wklejam klinków -> w manualu jest opis krok po kroku co trzeba zrobić i w sumie tylko raz wystarczy skorzystać z google.**

### Dlaczego Bielik?

No jak to dlaczego? bo to jeden z dwóch naszych "narodowych" modeli językowych (obok PLLuM). Rozwijany przez [SpeakLeash | Spichlerz](https://www.linkedin.com/company/speakleash/) i całą zgraję wolontariuszy i ludzi dobrej woli. Niedawno wyszły nowe wersje Bielika, więc tym bardziej warto się zainteresować.

### Co potrafi Bielik i czym się charakteryzuje?

Bielik 4.5B v3 to nowoczesny, lekki model językowy o 4,5 miliarda parametrów, zoptymalizowany pod kątem generowania i rozumienia tekstu po polsku. Jest zbudowany na architekturze „decoder‑only”, z dedykowanym tokenizatorem polskojęzycznym, co pozwala mu efektywnie operować na strukturach specyficznych dla polszczyzny (fleksja, odmiana, składnia).

**Co potrafi:**

- Generować spójne zdania, akapity i proste opisy.
- Uzupełniać tekst, tłumaczyć lub tworzyć zarys treści (np. e‑maila, notatki, podsumowanie).
- Służyć jako chatbot do pytań ogólnych, wsparcia twórczości, podstawowych konsultacji.

**Czego nie potrafi:**

- Nie zastąpi eksperta – może się mylić, generować nieprecyzyjne lub nieprawdziwe informacje.
- Nie jest wyposażony w wbudowane narzędzia do weryfikacji faktów czy moderacji treści.

**Dla kogo i gdzie się sprawdzi:**

- Dla początkujących i średnio zaawansowanych użytkowników – np. do prototypów, edukacji, lekkich zastosowań biznesowych.
- Świetny do lokalnego użycia bez chmury – można go uruchomić na komputerach osobistych (CPU/GPU), bez potrzeby dostępu do internetu.

### Instalujemy - pierwszy krok, czyli "studio LM" - wyszukaj w google i zainstaluj

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQEp2sQTzKZhiw/article-inline_image-shrink_1000_1488/B56Zd6sbD4HUAQ-/0/1750110155822?e=1781740800&v=beta&t=5M-YUvbw3tc570hTPCfiaufvsYxX3cFnRCAGAivLS5E)

Treść artykułu

Przy pierwszym uruchomieniu będzie trzeba nacisnąć zielony przycisk, ale w kolejnym oknie skip, żeby zamknąć okno.

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQFH6B0vzyfIMA/article-inline_image-shrink_1000_1488/B56Zd6wDPtH8AU-/0/1750111106728?e=1781740800&v=beta&t=elydZqzeX1vhyj-KyMPByuL6lX-uZq6kbizxd0Jm-oA)

Treść artykułu

Narzędzie StudioLM jest środowiskiem uruchomieniowym dla wielu otwartych modeli - w zależności od "mocy" komputera mozna wybierać modele z większą liczbą parametrów. U mnie od strzała zadziałał model z 4.5b parametrów (4,5 miliarda). Niemniej w Twoim przypadku (jeśli nie będzie się chciał uruchomić, to rekomenduję wybranie takiego, który ma mniej parametrów).

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQGvIcD1eFUECA/article-inline_image-shrink_1000_1488/B56Zd6vlisGoAQ-/0/1750110985060?e=1781740800&v=beta&t=0ILuRutJLbs2Cgj6FXpPuslNxl2PH56b5jJKA9olALY)

Treść artykułu

Następnie wybieramy DISCOVER i szukamy modelu, który nas interesuje. Polecam wpisać 'bielik 4 v3' - to powinno wystarczyć do znalezienia właściwego.

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQGfq5n6UEALbw/article-inline_image-shrink_1500_2232/B56Zd6v8H5HQBg-/0/1750111077603?e=1781740800&v=beta&t=NUFjMUeKNQLUSWXgdpOif0-XWeQy4-qIN490PP48e2A)

Treść artykułu

Ważne, żeby wybrać model z rozszerzeniem GGUF, który powinien od ręki się uruchomić. No i klikamy DOWNLOAD w prawym dolnym rogu (oczywiście z założeniem, ze mamy minimum 5-6gb miejsca na dysku).

Gdy model się pobierze wystarczy go uruchomić. Naprawdę. W większości przypadków nic więcej nie trzeba ustawiać.

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQHCz_6o10X_1w/article-inline_image-shrink_1500_2232/B56Zd6w6gfH8AY-/0/1750111332934?e=1781740800&v=beta&t=amDquykO9sZ8tOQerUrXNCf_HegNfB513Dc4l5ENqls)

Treść artykułu

Klikamy w górnym oknie "WYBIERZ MODEL DO ZAŁADOWANIA" lub anglojęzyczną wersję tego komunikatu.

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQG7TKV1tDu48A/article-inline_image-shrink_400_744/B56Zd6xovgGQAc-/0/1750111522347?e=1781740800&v=beta&t=3uzXnFs1q6f0PWAratIUTP_ljlvfq7rH-cSTIdnl_Ek)

Treść artykułu

Na końcu ZAŁADUJ MODEL i voila. W czacie możemy juz rozmawiać z modelem. Na powyższym oknie widać podstawowe parametry, które (w zależności od mocy komputera) możemy zmienić na wyższe i/lub po wybraniu opcji advenced (lewy dolny róg tego okna) pojawi się więcej ustawień.

![Treść artykułu](https://media.licdn.com/dms/image/v2/D5612AQEt54vpobQyUw/article-inline_image-shrink_1500_2232/B56Zd6yNyvG0AY-/0/1750111674299?e=1781740800&v=beta&t=ervPS1JglR5slyNuzLGUCvABufLmJ6ZHztgNkmJeikc)

Treść artykułu

Ostatnie na co warto zwrócić uwagę, to w głównym oknie apliacji i po uruchomieniu modelu można kliknąć w prawym górnym rogu w ikonkę fiolki/kolby stożkowej, która rozwinie nam ustawienia modelu typu temperatura, etc. Zachęcam do czatowania z modelem i dopytywania co znaczą te ustawienia.

### I to wszystko? po co?

Odpowiem krótko - bo można. Ile znasz osób, które uruchamiały instancję modelu językowego u siebie na komputerze? No własnie, ja też niewiele. Dlatego czasem warto coś zrobić dla własnej satysfakcji i/lub, żeby przyznać Jurgiel-Żyle, że to wcale nie jest takie trudne:)

Dobrego wtorku!