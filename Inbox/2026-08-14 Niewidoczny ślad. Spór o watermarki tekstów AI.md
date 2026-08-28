---
type: "Web"
authors: "[[Redakcja]]"
url: "https://haimagazine.com/pl/ai_branza/prawo_etyka/watermarki-tekstow-ai/?utm_source=ActiveCampaign&utm_medium=email&utm_content=Zg%C5%82o%C5%9B%20si%C4%99%2C%20do%C5%82%C4%85cz%2C%20tw%C3%B3rz%20-%20mamy%20dla%20Ciebie%20bilety&utm_campaign=Zg%C5%82o%C5%9B%20si%C4%99%2C%20do%C5%82%C4%85cz%2C%20tw%C3%B3rz%20-%20mamy%20dla%20Ciebie%20bilety"
published: 2026-08-14
created: 2026-08-28
tags:
---


Anthropic poinformował, że modele Claude wprowadzane od 2 sierpnia 2026 roku mają obsługiwać niewidoczne watermarki tekstowe już od chwili premiery. Firma pracuje również nad dodaniem oznaczeń do modeli wydanych wcześniej. Nie oznacza to więc, że każdy tekst generowany obecnie przez dowolną wersję Claude musi już zawierać taki ślad.

W przypadku obsługiwanych modeli oznaczenie ma być stosowane globalnie, niezależnie od tego, czy użytkownik korzysta z aplikacji Claude, API, Claude Code czy usług chmurowych partnerów. Watermark zostanie wpleciony bezpośrednio w tekst, dzięki czemu ma przetrwać kopiowanie, wklejanie oraz część późniejszych zmian. [==Anthropic nie opublikował jednak jeszcze szczegółów technicznych ani narzędzia==](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content), którym użytkownicy mogliby samodzielnie sprawdzić obecność oznaczenia. Firma zapowiada dopiero udostępnienie odpowiedniej dokumentacji i mechanizmu detekcji.

To nie jest pierwsze takie rozwiązanie. Google już w maju 2024 roku rozszerzył SynthID na teksty generowane w aplikacji i internetowej wersji Gemini. System nie dopisuje ukrytych znaków do pliku. Wpływa na prawdopodobieństwo wyboru kolejnych tokenów, tworząc statystyczny wzór możliwy do rozpoznania przez detektor. ==[Google od początku zastrzegał jednak, że nie jest to metoda niezawodna](https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/).==

Skąd więc tak silna reakcja na decyzję Anthropic? Problem nie dotyczy wyłącznie osób, które przedstawiają wygenerowane teksty jako własne. Spór koncentruje się na tym, co właściwie potwierdza niewidoczny znak i jak zostanie wykorzystany przez uczelnie, pracodawców, wydawców oraz platformy internetowe.

#### Ślad ukryty słowach

Watermarkowanie tekstu różni się od znaku wodnego umieszczanego na obrazie. Czytelnik nie widzi logo, symbolu ani komunikatu. Sygnał jest zakodowany w statystycznych właściwościach wygenerowanej wypowiedzi.

Jednym z pierwszych badaczy, którzy publicznie opisywali ten mechanizm, był [==Scott Aaronson==](https://scottaaronson.blog/?p=6823), informatyk i były badacz OpenAI, który pracował nad teoretycznymi podstawami watermarkowania tekstów generowanych przez modele językowe. Model nie wybiera każdego kolejnego słowa w sposób całkowicie zdeterminowany. Dysponuje zbiorem możliwych tokenów oraz przypisanym im prawdopodobieństwem. System watermarkowania może delikatnie preferować niektóre z dopuszczalnych opcji, nie zmieniając zauważalnie znaczenia tekstu.

Po odpowiednio długim fragmencie powstaje wzór, który dla czytelnika wygląda jak zwykły tekst, ale może zostać wykryty przez narzędzie znające zastosowaną metodę. Aaronson wskazywał, że takie rozwiązanie mogłoby utrudnić przedstawianie wygenerowanych materiałów jako pracy człowieka. Później [==określił teoretyczne podstawy watermarkowania modeli językowych==](https://scottaaronson.blog/?p=9333) jako jeden z najważniejszych rezultatów swojej pracy nad bezpieczeństwem AI.

Podobnie swoje rozwiązanie przedstawia Google. SynthID ma dostarczać odbiorcom informacji o pochodzeniu treści bez wpływania na jej czytelność, dokładność czy tempo generowania. Firma nie nazywa go jednak rozwiązaniem ostatecznym. Traktuje watermark jako jeden z elementów szerszego systemu identyfikowania materiałów syntetycznych.

W tym punkcie zwolennicy oznaczeń są zgodni: wraz ze wzrostem liczby treści generowanych przez modele potrzebne są narzędzia, które pozwolą przynajmniej częściowo ustalić ich pochodzenie. Nie oznacza to jednak zgody co do tego, jak należy interpretować znaleziony ślad.

#### Kto właściwie to napisał?

Anthropic sam przyznaje, że wykrycie watermarka nie musi oznaczać, iż Claude jest autorem całego materiału. Model mógł jedynie poprawić gramatykę, przetłumaczyć tekst, przygotować streszczenie albo zmienić format dokumentu. Idee, dane i pierwotne sformułowania mogły pochodzić od człowieka.

Na różnicę między pełnym generowaniem a redakcją tekstu zwraca uwagę [==William Allen==](https://www.linkedin.com/posts/williamallen2050_i-started-the-content-authenticity-initiative-activity-7492934617881006080-kroU), współtwórca Content Authenticity Initiative i uczestnik prac nad standardem C2PA dotyczącym pochodzenia cyfrowych treści. Jego zdaniem watermarkowanie wszystkich tekstów sprowadza złożony proces ich powstawania do binarnego oznaczenia.

Allen wskazuje na różnicę między użyciem modelu jako odpowiednika korektora a wygenerowaniem całego materiału jednym poleceniem. Watermark może sygnalizować udział AI, ale nie pokazuje jego zakresu. Zamiast prostego podziału na tekst ludzki i wygenerowany proponuje historię pochodzenia dokumentu, która informowałaby o kolejnych etapach edycji oraz wprowadzonych zmianach.

Podobną wątpliwość opisują [==Federico Germani i Giovanni Spitale==](https://arxiv.org/abs/2607.13082), badacze etyki informacji i wpływu AI na obieg treści. Ich zdaniem informacja o pochodzeniu tekstu nie mówi niczego pewnego o jego prawdziwości, jakości ani intencji autora. Materiał oznaczony jako wygenerowany przez AI może być rzetelny, a tekst bez oznaczenia może zawierać manipulacje lub nieprawdziwe informacje.

Badacze ostrzegają, że prosta etykieta może stygmatyzować zgodne z zasadami wykorzystanie narzędzi, a jednocześnie budować nieuzasadnione zaufanie do treści nieoznaczonych. W ich ujęciu większe znaczenie ma transparentność całego procesu niż pojedynczy sygnał o udziale modelu.

#### Watermark nie jest niezawodny?

Druga część sporu dotyczy skuteczności. Anthropic deklaruje, że znak może przetrwać kopiowanie i część edycji, ale jednocześnie wymienia sytuacje, w których może zniknąć lub stać się niewykrywalny. Dotyczy to między innymi intensywnego przeredagowania, parafrazowania, tłumaczenia, połączenia z innymi tekstami oraz bardzo krótkich fragmentów.

Nie jest to problem charakterystyczny wyłącznie dla Claude. [==Google podaje, że SynthID najlepiej działa w dłuższych i bardziej zróżnicowanych wypowiedziach==](https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/). Kilka zmian lub łagodna parafraza nie muszą usuwać sygnału, ale pełne przepisanie albo tłumaczenie tekstu znacząco obniża pewność detekcji.

System ma też mniejsze możliwości w przypadku odpowiedzi na pytania faktograficzne. Gdy model odpowiada na pytanie o stolicę państwa albo przytacza konkretny utwór, liczba poprawnych wariantów kolejnych słów jest ograniczona. Pozostaje więc mniej miejsca na wybory, w których można zakodować dodatkowy wzór.

[==Alex Cui==](https://x.com/alexcdot/status/2087078010524406137), współzałożyciel i dyrektor technologiczny GPTZero, firmy tworzącej narzędzia do wykrywania tekstów generowanych przez AI, przypuszcza, że rozwiązanie Anthropic może być oparte na podobnym wpływaniu na rozkład tokenów. Anthropic nie potwierdził jednak tej hipotezy, dlatego nie można przedstawiać jej jako opisu rzeczywistej konstrukcji systemu.

Cui zwraca uwagę na bardziej ogólny problem. Publiczny detektor jest potrzebny, aby użytkownicy nie musieli polegać wyłącznie na deklaracji Anthropic. Z drugiej strony takie narzędzie może pomóc w testowaniu kolejnych wersji tekstu aż do momentu, gdy watermark przestanie być wykrywany. Powstaje więc klasyczny wyścig między oznaczaniem a jego obchodzeniem.

#### Jak to sprawdzać?

Samo istnienie niedoskonałego oznaczenia nie musi być szczególnie niebezpieczne. Znacznie ważniejsze jest to, jakie konsekwencje zostaną przypisane wynikowi detekcji.

[==Alexander Nemecek, Yuzhou Jiang i Erman Ayday==](https://arxiv.org/abs/2505.23814), badacze zajmujący się technicznymi i regulacyjnymi aspektami watermarkowania treści AI, przekonują, że oznaczenia bez wspólnych standardów mogą stać się jedynie symbolem kontroli. Analizują nie tylko skuteczność samych znaków, lecz także warunki, które muszą zostać spełnione, aby ich wykrycie można było wiarygodnie wykorzystywać w praktyce.

Ich zdaniem skuteczny system wymaga trzech warstw: określonych standardów technicznych, niezależnej infrastruktury audytowej oraz mechanizmów odpowiedzialności i egzekwowania zasad.

Bez nich dostawca może sam ustalać sposób znakowania, progi wykrywania i sposób interpretowania wyniku. Zewnętrzny obserwator nie będzie natomiast w stanie ocenić, czy system działa zgodnie z deklaracjami ani jak często się myli.

[==Zespół badawczy z udziałem Nemeceka i Aydaya==](https://arxiv.org/abs/2604.13776) zwraca uwagę na jeszcze jeden element. Siła watermarka zależy od statystycznych właściwości treści, a te różnią się między językami i grupami użytkowników. W przeglądzie najważniejszych benchmarków autorzy stwierdzili, że niemal żaden nie raportuje wyników z uwzględnieniem różnic językowych, kulturowych lub demograficznych.

Nie dowodzi to, że system Claude będzie gorzej działał po polsku. Pokazuje jednak, dlaczego przed wykorzystaniem wyniku wobec studenta lub pracownika potrzebne są testy obejmujące różne języki.

#### Sędzia we własnej sprawie

Znany inwestor technologiczny [==Bill Gurley==](https://x.com/bgurley/status/2087335941216272548) zauważa, że oznaczenie będzie rozpoznawalne przede wszystkim dla Anthropic. Firma staje się wówczas, jak napisał, „sędzią, ławą przysięgłych i oskarżycielem”. Anthropic pracuje nad bezpłatnym API, które pozwoli użytkownikom i podmiotom zewnętrznym sprawdzać obecność watermarka. Na razie nie opublikował jednak progów wykrywania, wyników testów ani informacji o odsetku błędnych wskazań. Nie wiadomo także, czy zewnętrzne instytucje będą mogły niezależnie audytować system.

Brakuje również odpowiedzi na pytanie o procedurę odwoławczą. Co ma zrobić student, pracownik lub autor, którego tekst zostanie oznaczony jako przetworzony przez Claude? Czy otrzyma jedynie wynik pozytywny, czy także informację o sile sygnału? Jak odróżnić pełne wygenerowanie dokumentu od korekty kilku akapitów?

Są to szczegóły, których Anthropic jeszcze nie ujawnił. Ich znaczenie będzie jednak rosło wraz z każdą instytucją, która spróbuje potraktować watermark jako dowód naruszenia zasad.

#### Sygnał, nie werdykt

[==Europejski AI Act==](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) wymaga od dostawców generatywnych systemów dodawania maszynowo odczytywalnych oznaczeń umożliwiających wykrywanie treści wygenerowanych lub zmodyfikowanych przez AI. Reakcje na decyzję Anthropic pokazują, że spełnienie obowiązku technicznego nie kończy dyskusji. Dla jednych watermark jest narzędziem, które może utrudnić ukrywanie pochodzenia tekstu. Dla drugich pojedynczy znak nie wystarcza, ponieważ nie pokazuje historii pracy nad dokumentem ani rzeczywistego zakresu pomocy AI. Jeszcze inni podkreślają, że oznaczenia nabiorą znaczenia dopiero wtedy, gdy będą oparte na wspólnych standardach i poddawane niezależnemu audytowi.

Rynek nie spiera się już o to, czy treści tworzone przez AI należy oznaczać. Spór dotyczy przede wszystkim tego, co takie oznaczenie rzeczywiście mówi o tekście.