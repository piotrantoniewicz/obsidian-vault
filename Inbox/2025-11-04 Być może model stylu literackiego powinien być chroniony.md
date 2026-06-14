---
type: "Web"
authors: "[[Marcin Wilkowski]]"
url: "https://blog.humanistyka.dev/2025/11/byc-moze-model-stylu-literackiego-powinien-byc-chroniony"
published: 2025-11-04
created: 2026-06-14
tags:
---


Tekst wygenerowany przez model językowy, dostrojony na twórczości znanego autora, bardziej podoba się czytelnikom (ekspertom i amatorom) niż proza w jego stylu, napisana przez zawodowych pisarzy. Co więcej, jest niewykrywalny dla detektorów AI, nie powtarza dosłownych schematów z oryginalnych utworów, a jego wytworzenie kosztuje 99.7 proc. mniej niż potencjalne honorarium profesjonalnego pisarza, który miałby przygotować powieść w stylu oryginalnych twórców.

Badanie *Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers* (DOI: [10.48550/arXiv.2510.13939](https://doi.org/10.48550/arXiv.2510.13939), 2025) dokumentuje wysoką jakość wytwarzanych maszynowo powieści, generowanych w stylu czołowych autorów i autorek literatury. Oto wybrano 50 uznanych autorów, w tym laureatów Nagrody Nobla, Bookera czy Pulitzera, pochodzących z różnych kręgów kulturowych i piszących w różnym stylu. Poproszono kilkudziesięciu autorów z wiodących kursów kreatywnego pisania, prowadzonych na amerykańskich uczelniach, o przygotowanie fragmentów o długości 450 słów, imitujących styl oryginalnych twórców. Równolegle wygenerowano takie fragmenty za pomocą modeli `GPT-4o`, `Claude 3.5 Sonnet` i `Gemini 1.5 Pro`. Modele otrzymały te same instrukcje, co eksperci - polecenia zawierały dwadzieścia przykładowych fragmentów, opis stylu i szczegóły dotyczące treści, którą chciano emulować.

Powstało w ten sposób 150 par fragmentów pisanych przez człowieka i wytwarzanych przez AI. Każde takie zestawienie zostało ocenione przez mieszane pary ekspertów (w badaniu wzięło udział 28 uczestników kursów kreatywnego pisania) i czytelników *nieprofesjonalnych* (zaangażowano ich 131). Oceniano w dwóch kategoriach: wierności stylowi oryginalnych prac pisarza oraz jakości literackiej tekstu. Wykres C i D (zob. niżej) ilustruje preferencje oceniających. Eksperci okazali się bardziej krytyczni wobec fragmentów generowanych maszynowo niż zwykli czytelnicy, którzy raczej akceptowali automatycznie wytwarzane wersje.

![enter image description here](https://blog.humanistyka.dev/content/images/20251104231759-878b8b44926da0a729a02d9dab73d6d5a7c2a998.png)

Oceny ekspertów zmieniły się, kiedy poproszono uczestników badania o zapoznanie się z tekstami, wytworzonymi przez dostrojony model `GPT-4o` (znów spójrzmy na wykres C i D i wartości).

Na czym polegało to dostrojenie? Z puli 50 autorów wybrano 30 żyjących. Podjęto taką decyzję, żeby zbadać potencjalny wpływ ekonomiczny, jaki generatywna AI może mieć na przychody żyjących autorów. Teksty ich autorstwa w postaci ebooków kupiono w księgarniach internetowych, przetworzono na tekst i udostępniono modelowi `GPT-4o`. W efekcie uzyskano 90 par fragmentów autorstwa człowiek - AI. Podczas generowania docelowych fragmentów upewniono się, że żaden fragment wygenerowany przez AI nie zawiera dosłownych powtórzeń z oryginalnego tekstu. Do zmierzenia tego, jak bardzo oryginalne i wygenerowane teksty nakładają się na siebie, użyto miary [ROGUE-L](https://en.wikipedia.org/wiki/ROUGE_\(metric\)).

Eksperci i czytelnicy oceniali tak zestawione pary fragmentów. Jak widzimy na wykresach C i D, w tym przypadku preferencje ekspertów i zwykłych czytelników wyraźnie przesunęły się na teksty generatywne.

Wygenerowane teksty sprawdzono w detektorze [Pangram](https://www.pangram.com/) i za pomocą modelu `GPTZero`. Teksty powstałe przy użyciu dostrojonego `GPT-4o` okazały się praktycznie niewykrywalne. Badanie udowodniło, że za ułamek kosztów pracy ludzkiego autora można skutecznie tworzyć prozę w jego stylu. Koszty dostrajania i generowania fragmentów wynosiły od 25 do 276 dol. na autora (mediana - 81 dol.), przy założeniu, że milion tokenów, przetworzonych w ramach dostrojenia modelu to koszt 25 dol., a wygenerowanie 100 tys. słów danego tekstu to koszt około 3 dol. Koszty te stanowiły około 0.3 proc. sumy, którą eksperci biorący udział w badaniu pobieraliby za manuskrypt o długości powieści (100 000 słów).

Jak czytamy w podsumowaniu badania, redukcja kosztów surowej generacji o 99.7 proc., w połączeniu z wyższymi ocenami jakości dla większości oryginalnych autorów, pokazuje znaczne przesunięcie wartości rynkowej w polu literackim z ludzkich twórców na firmy technologiczne, zdolne za ułamek ceny generować wysokiej jakości teksty. Może to powodować wypieranie z rynku ludzkich twórców, zwłaszcza tych, których powieści udało się tak skutecznie w tym badaniu symulować. To jedna z przesłanek, które mogą ograniczać dozwolony użytek, ułatwiająca twórcom i wydawnictwom blokowanie używania ich twórczości do dostrajania modeli językowych.

Wydaje mi się, że bardzo łatwo wyciągnąć zbyt daleko idące wnioski z omawianego badania. Przewiduje on bowiem sytuację, w której na rynek wydawniczy trafiają powieści w stylu Ernaux, Saundersa czy Murakami, pisane przez profesjonalnych ghostwriterów lub wytwarzane przez modele językowe. Ponieważ w systemie prawa autorskiego trudno byłoby oficjalnie sprzedawać takie książki pod nazwiskami uznanych twórców, jakość falsyfikatów i tak nie miałaby bezpośredniego przełożenia na ich potencjalne zyski. Czy sięgnęlibyśmy po powieść anonimowej autorki, napisanej lub wytworzonej w stylu powieści Ernaux? Czy taka powieść mogłaby być promowana w nawiązaniu do francuskiej noblistki? Pamiętajmy, że prawo autorskie może chronić także elementy świata przedstawionego, koncepcje postaci itp.

Zmiana na rynku książki, wywołana pojawieniem się takich falsyfikatów, wymagałaby jednak zmiany zachowań czytelników, dla których musiałaby przestać się liczyć relacja z autorem, a podstawą doświadczenia czytelniczego byłby już tylko sam tekst. Przykład fanfików pokazuje jednak, że teksty rozwijające rzeczywistości przedstawioną w oryginalnych dziełach są wciąż mniej atrakcyjne dla szerokiego grona czytelników niż oryginalne powieści. Są też [zazwyczaj niedostępne na rynku wydawniczym](https://en.wikipedia.org/wiki/Legal_issues_with_fan_fiction). Trudno więc wyobrazić sobie sytuację, że dostępne na tym rynku byłyby maszynowo wytwarzane falsyfikaty powieści czołowych autorów. Nie oznacza to oczywiście, że warunki, w jakich funkcjonują pisarze i pisarki na rynku literackim, nie zmieniają się w ogóle przez rozwój dużych modeli językowych. Być może chronione powinny być nie tylko ich utwory, ale też ich wektorowe reprezentacje - modele stylu literackiego, wytworzone na ich twórczości?

Autor:

🤗

Jeśli ten wpis okazał się dla Ciebie wartościowy, możesz dorzucić się do wsparcia bloga. Postaw wirtualną kawę na [Suppi.pl](https://suppi.pl/humanistyka-dev) albo [zostań patronem na Patronite](https://patronite.pl/humanistyka.dev).

Wpis opublikowany na licencji Creative Commons [Uznanie autorstwa - Na tych samych warunkach](https://creativecommons.org/licenses/by-sa/4.0/).