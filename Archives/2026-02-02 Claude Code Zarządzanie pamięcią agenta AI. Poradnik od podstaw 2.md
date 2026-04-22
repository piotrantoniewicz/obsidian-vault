---
type: Web
authors: '[[Krzysztof Bohaczyk]]'
url: 'https://www.youtube.com/watch?v=PIvJnLkquVc'
published: 2026-02-02T00:00:00.000Z
created: 2026-04-19T00:00:00.000Z
tags:
  - narzędzia-AI
  - szkolenia-AI
  - strategia-AI
---


![](https://www.youtube.com/watch?v=PIvJnLkquVc)

Drugi odcinek poradnika dla początkujących pracy z Claude Code. Pokażę Ci, jak zarządzać pamięcią CLAUDE.md i rozpocząć pracę z własnym projektem w Claude Code.  
  
Poprzedni odcinek pokazał instalację - teraz czas na prawdziwą magię. Dowiesz się jak sprawić, by Claude Code znał Twój projekt od podszewki, pamiętał Twoje preferencje i pracował dokładnie tak, jak tego potrzebujesz.  
  
CLAUDE.md to plik, który zmienia wszystko. Dzięki niemu Claude Code nie zaczyna od zera przy każdej sesji - pamięta strukturę projektu, Twoje zasady i styl pracy.  
  
W tym odcinku zobaczysz:  
  
✓ Czym jest plik CLAUDE.md i dlaczego jest kluczowy  
✓ Komenda /init - automatyczna analiza projektu  
✓ Hierarchia pamięci (globalny, projektowy, lokalny)  
✓ Jak dodawać reguły w trakcie rozmowy  
✓ Praktyczny przykład: system do zarządzania treściami  
✓ Wskazówki dla projektów nietechnicznych  
  
To nie jest tylko dla programistów! Pokazuję projekt do content marketingu - bez linijki kodu.  
  
Kluczowe komendy z odcinka:  
→ /init - inicjalizacja projektu  
→ /memory - podgląd plików pamięci  
→ # - szybkie dodawanie reguł  
  
Obejrzyj część 1 jeśli jeszcze nie masz zainstalowanego Claude Code!  
  
👍 ZOSTAW LAJKA, jeśli seria Ci się podoba!  
🔔 SUBSKRYBUJ, by nie przegapić części 3!  
💬 Napisz w komentarzu - jaki projekt chciałbyś skonfigurować z Claude Code?  
  
🔗 Przydatne linki:  
👉 Oficjalna dokumentacja: https://docs.anthropic.com/en/docs/claude-code  
👉 Projekt z odcinka (GitHub): https://github.com/simplybychris/content-os  
📧 Newsletter Detechtive: https://www.detechtive.pl  
  
Rozdziały:  
0:00 - Wprowadzenie  
1:42 - Eksperyment z pamięcią sesji  
2:50 - Czym jest CLAUDE.md  
4:30 - Komenda /init w akcji  
6:00 - Praca z ClAUDE.md  
11:20 - Hierarchia pamięci (globalny/projektowy/local)  
12:35 - Komenda /memory  
12:30 - Szybkie dodawanie reguł (#)  
14:00 - Podsumowanie  

## Transcript

### Wprowadzenie

**0:00** · Cześć. \[muzyka\] W poprzednim odcinku zainstalowaliśmy Cloud Code i poznaliśmy podstawowe komendy. A dzisiaj chciałbym ci pokazać jak rozpocząć pracę nad własnym projektem i jak \[muzyka\] zarządzać pamięcią w Cloud Cod, która jest bardzo kluczowa i ważna do efektywnej pracy z tym narzędziem. Także zaczynajmy. Popatrz, ja jestem w swoim projekcie Content OS. Jeśli zapytasz, co to jest za projekt, to już ci mówię, jest to system do zarządzania treściami.

**0:24** · Polega on na tym, że w tym projekcie będę mógł przygotowywać moje wpisy od pomysłu do publikacji. I struktura wygląda następująco. Mamy główny folder content tutaj po lewej stronie, który zawiera folder ideas, czyli pomysły na treści. Jest też folder do szkiców na pewne publikacje. Publish, czyli moje opublikowane artykuły. Repurpost, czyli adaptacje na inne platformy.

**0:49** · Również mamy templates, czyli szablony, które możemy sobie określić na konkretne social media, czyli na przykład inny styl do pisania naie, inny styl napisania na LinkedInie czy też inny chociażby na nasz blog. I również ważny folder reset, czyli przed każdą publikacją będziemy sobie przygotowywać materiały źródłowe na dany temat.

**1:11** · Oczywiście to jest mój pomysł na projekt. Ty możesz zacząć z jakimkolwiek innym projektem. Może być to strona, blog czy też może właśnie narzędzie podobne jak to, które ci pokazuję. Ten projekt jest przygotowany stricte pod kurs, natomiast coś bardzo podobnego używam również dla siebie właśnie do produkcji kontentu, także będziesz mógł to zaczerpnąć również do siebie. Ten projekt będziesz mógł pobrać w opisie, z którego będziesz mógł prosto skopiować link i nawet powiedzieć Clodowi o tym, żeby skopiował ten projekt lokalnie do ciebie, żebyś mógł z nim działać również ze mną.

**1:40** · No dobra, ale jeszcze zanim zaczniemy z naszym projektem, chciałem tobie pokazać pewien eksperyment.

### Eksperyment z pamięcią sesji

**1:46** · Włączmy sobie cloud i powiedzmy, że chciałbym, żeby cloud za przy każdym powitaniu mówił do mnie kapitanie. Tak więc przy każdym powitaniu zwracaj się do mnie.

**2:00** · kapitanie.

**2:02** · Dobra i dajmy mu taką regułę. Zaraz ci powiem o co dokładnie chodzi. No i zobacz. Rozumiem kapitanie. Teraz będę się do ciebie zwracał przy powitaniach.

**2:10** · Cześć Klot.

**2:12** · No jest. Cześć kapitanie. No wygląda rewelacyjnie. No i powiesz Krzysiek, ale do czego ma to służyć? Jak wyjdziemy teraz z tego cloda komendą exit i włączymy go sobie na nowo i przywitamy się z nim, czyli znowu cześć, to zauważ, że już nie zwraca się do nas per kapitan. Czemu? No bo te z reguły, zasady, które narzuciliśmy mu w poprzedniej sesji zostają w poprzedniej sesji. Clod nie ma narzędzia, by przetrzymywać te informacje pomiędzy sesjami. I tu właśnie pojawia się temat Cloud MD.

**2:43** · Cloud MD jest to plik, który możemy sobie utworzyć tutaj po lewej stronie.

**2:46** · Wpisujemy cloud. MD. Jest to plik Markdown, który zawiera właśnie najważniejsze informacje o naszym projekcie dla Cloda. Powiedzmy, że przychodzi do ciebie nowy stażysta, no i też musi w jakiś sposób zapoznać się z waszym projektem, z funkcjonowaniem firmy i też musi zrozumieć organizację i właśnie do tego jest cloud. Czyli jak zaczynamy nową instancję Cloda, to on może sobie zaczytać do pamięci właśnie ten plik wraz z najważniejszymi informacjami. Czyli możemy mu tutaj napisać zwracaj się do mnie per kapitanie. Tak.

### Czym jest CLAUDE.md

**3:19** · I zapisujemy sobie taką linijkę. I zauważ, że jak teraz otworzymy sobie nowy terminal, piszemy cloud i napiszemy cześć, czyli to co robiliśmy wcześniej, to zobacz, nie musiałem mu nadawać żadnego polecenia jak ma się do mnie zwracać. Natomiast zaraz Clotisze: "Cześć kapitanie, jak mogę ci pomóc?" Czyli to co chcę ci pokazać to właśnie takie proste zrozumienie jak działa właściwie clot.

**3:44** · Clot to jest taki plik, który będzie się dołączał do naszego prompta systemowego.

**3:49** · Tak? Czyli jak mamy kontekst, wejdziemy sobie z powrotem na kontekst, o tym mówiliśmy jeszcze poprzednio. No i zauważ, że mamy coś takiego jak memory files, pliki z pamięcią. To jest właśnie clodem MD. Mam nadzieję, że to już się troszeczkę rozjaśniło, więc wracając jeszcze do tego pliku, oczywiście wyczyścimy sobie tą regułę, bo nie potrzebuję, żeby zwracał się do mnie per kapitan. No ale chciałbym ci pokazać, że mamy ten nasz katalog wraz z różnymi plikami, folderami oraz jakimiś dokumentami. I fajnie jakby Clot przy każdej sesji zdawał sobie sprawę z czym pracuje. I mamy taką komendę init.

**4:18** · Jest to komenda, która zainicjalizuje nam nowy plik clodem D. Czyli możemy sobie usunąć ten nasz plik. delete. Zauważ, że już tego nie ma w naszym projekcie. I mogę wpisać init. I co robi właśnie Cloud Code? To on sam analizuje nasz projekt, wyciąga najważniejsze informacje i później na bazie tego naszego repozytorium przygotowuje taką spójną instrukcję krok po kroku dla Cloda, dla kolejnych sesji, żeby wiedział co się znajduje w tym projekcie. I poczekajmy chwilkę.

### Komenda /init w akcji

**4:48** · Tutaj widzisz, że iteruje, sprawdza różne pliki i katalogi. Możemy sobie kliknąć ctrol o i dokładnie podglądnąć, co właśnie myśli. Oczywiście standardowe pytanie, czy chcemy zezwolić na wykonywanie tej komendy. Clot często przy różnych akcjach będzie się pytał, czy chcesz wykonać tą komendę. Jeśli chcesz, żeby to było jednorazowo, dajesz jest.

**5:13** · Jeśli chcesz, żeby to już było zapisane również w konfiguracji, to możesz dać drugie, czyli żeby zapisał to już nie pytał cię ponownie o to konkretne narzędzie. Także dajemy enter.

**5:24** · Dobra, teraz możemy sobie przejść.

**5:26** · Jeszcze chwileczkę tutaj myśli. Okej, utworzyłem plik clodem D. Zawiera opis projektu, workflow, struktura katalogów, format plików, informacje o języku. Plik jest zwięzły i skupia się na tym, co jest specyficzne dla tego projektu.

**5:40** · Super. Przejdźmy od razu do tego pliku i zobaczmy jak on wygląda. Oczywiście plik markdowny jest zapisany w takim formacie właśnie chociażby z takimi hashztagami co oznacza nagłówek i też mogą się pojawiać pogrubienia. Wtedy robimy to gwiazdkami, ale możemy go otworzyć open preview i wtedy mamy ładnie sformatowany taki czytelny dla nas. Więc mamy tutaj instrukcję po angielsku. Nawet tutaj Cloud dodał sobie informację na starcie, że jest to instrukcja dla cloud coda.

### Praca z ClAUDE.md

**6:07** · Pracując właśnie z tym kodem, z tym repozytorium naszym, tak? I jest project overview, czyli taki krótki opis.

**6:13** · Content OS jest to właśnie takim content management system do zarządzania pisanym contentem od pomysłów poprzez drafty do publikacji. Content workflow, czyli on tutaj sam wywnioskował na podstawie tych naszych folderów jaki będzie przepływ pracy. Czyli mamy pomysły, później mamy drafty i konkretnie zauważ, że też podał content drafts content ideas, czyli tą naszą strukturę, którą mamy tutaj w folderach.

**6:38** · A następnie jest strzałka jeszcze do repst, czyli później tworzenie na bazie tego naszego opublikowanego wpisu content na inne social media. Mamy opis również katalogów, czyli co znajduje się w jakim folderze. Po to, że jak zaczniemy nową sesję z cloud codem, to on będzie wiedział jak wygląda struktura projektu bez skanowania całego projektu na nowo.

**7:00** · Mamy również formaty plików, no i też język, czyli cały kontent i dokumentacja jest w języku polskim. Co prawda ten kod jest w języku angielskim, możemy to dostosować również, powiedzieć mu, żeby zrobił ją w języku polskim. Także tutaj też możemy śmiało iterować. Ta komenda ini to jest oczywiście fajna komenda na start, natomiast możemy doprecyzować popraw cloudd był cały w języku polskim,

**7:26** · czyli zauważ, że mogę też normalnie napisać mu zwrócić uwagę o jaki plik mi chodzi, czy też nawet małpą zaznaczyć ten plik. Ja tego tutaj nie zrobiłem, ale on już sobie łatwo wyłapał ten plik i go edytuje. Zaraz będziemy mieć poprawioną wersję. Super, mamy różnicę pomiędzy dwoma wersjami i zapisał gotowe. Także jak sobie to zwiniemy, to mamy ładny opis po polsku. I teraz, żeby było jasne, my pracujemy przy projekcie, który jest dla osób również nietchnicznych. Nie musimy tutaj działać z poziomu kodu.

**7:58** · W naszym przypadku my mamy opis naszego narzędzia, też język preferowany. Tu możemy dodać też ton jaki ma być naszych publikacji czy też naszą personę. Natomiast w przypadku chociażby projektu takiego technicznego, jeśli masz aplikację, stronę, możesz tutaj śmiało dać też taki opis swojej aplikacji, tekstach, czyli jakie technologie wykorzystujesz, jakie bazy danych, jak uruchomić ten projekt. To jest też bardzo ważne, żeby Cloud mógł łatwo sobie ten projekt zbudować i też uruchomić. To zależy od twojego projektu.

**8:28** · Także my mamy taki projekt nietchniczny, dlatego nie mamy tutaj żadnej zmiance o kodzie. Co jest jak najbardziej poprawne. Cloud MD dostosowujesz do swojego projektu. Jeśli masz stronę, wypiszę ci technologię.

**8:41** · Jeśli masz bloga, możesz wypisać właśnie styl pisania, masz aplikację, wpisz jak ją uruchomić i staraj się również, żeby ten cały plik cloudem dłzły na temat.

**8:51** · Nie chcemy wrzucać tutaj wszystkich informacji o każdym pliku. Nie o to w tym chodzi. Ma być to mały zrzut. Staraj się, żeby ten plik był do 300, ma 500 linijek. Myśl o tym jako takiej dokumentacji dla twojego projektu. Także bardzo ważne jest, by ona była update z tym, co budujesz. I co ważne, jest coś takiego jak hierarchia pamięci, czyli możemy tego Cloud MD zapisać na różnych poziomach. Zauważ tutaj mam wypisaną tą hierarchię.

**9:15** · Ja ci powiem o takich najważniejszych, a mianowicie jest coś takiego jak poziom globalny, czyli on jest zapisany w twoim folderze domowym i wtedy ten cloud MD będzie dotyczył wszystkich projektów, które masz u siebie na komputerze. Także tutaj możesz napisać takie ogólne instrukcje. To są rzeczy, które dotyczą ciebie, twój styl pisania, twój język, twoje preferencje.

**9:37** · Możesz też dodać jakieś swoje ulubione technologie, z którymi pracujesz, tak żeby CLCode mógł je również wziąć pod uwagę przy nowych projektach. I pamiętaj, działa to we wszystkich projektach, także też jest ważne, żeby nie zapychać tego pliku. Druga rzecz to cloud MD projektowy, czyli w naszym projekcie Content OS występuje plik clod MD i on będzie dotyczył tylko tego repozytorium. To jest fajne, jeśli pracujesz w parę osób nad jednym projektem.

**10:03** · Możesz takiego Cloudem D skomitować, wrzucić na GitHub, czyli na repozytorium kodu i wymieniać się z również z innymi pracownikami czy też znajomymi będą mogli mieć ten sam kontekst dzięki temu wspólnemu pliku.

**10:15** · Oczywiście ten plik, zależnie od jakiego narzędzia będziesz używać, może troszeczkę inaczej się nazywać.

**10:20** · Przykładowo dla Codexa i copilota jest taki plik zapisany jako agents. Jeśli działasz z Gemini, no to mamy gemini.m.

**10:30** · A cloud ma cloud MD, także każdy może mieć troszeczkę inny sposób zapisu.

**10:34** · Natomiast sama reguła, zasada jest podobna we wszystkich. Także ten, te rzeczy, które się tutaj nauczysz, będziesz mógł zastosować w innych narzędziach. Czyli krótko mówiąc, globalne dotyczą ciebie, projektowe dotyczą tego konkretnego projektu, z którym działasz. I mamy jeszcze taką jedną strukturę jak clot local MD. To co tutaj masz zwrócone, twoje prywatne ustawienia dla projektu. I nad czym polega różnica pomiędzy cloudem D a cloud local MD? To to, że local MD nie będzie komitowany, wrzucany na twoje repozytorium.

**11:05** · Tutaj możesz zapisać jakieś narzędzia, y, schematy, które ty wykorzystujesz, a nie muszą być konkretnie upublicznione w całym projekcie dla reszty zespołu. Także ja sobie utworzę właśnie taki local MD i dam tutaj ten zapis. Zwracaj się do mnie per capitan. I teraz tylko clot code do mnie będzie się zwracał per capitan z tego powodu, że ten plik nie będzie udostępniany przy komicie, przy wrzucaniu komitu do GitHuauba. Po prostu clot code będzie go pomijał. Także to jest ta największa różnica. Możemy sobie zrobić jeszcze taką komendę jak memory.

### Hierarchia pamięci (globalny/projektowy/local)

**11:37** · No i mamy te nasze pliki. Jest user memory, czyli ten główny plik cloud MD, który występuje w katalogu domowym. Mamy cloud local MD, czyli ten, który utworzyliśmy sobie przed chwilką. I mamy też project memory, czyli właśnie ten, który będzie publikowany jako nowa wersja na przykład w naszym repozytorium. Jeśli będziesz ustalał coś ważnego podczas rozmowy właśnie z Cloud Codem, to możesz powiedzieć Cloudowi, żeby zapisał tą konwersację właśnie w Cloudm MD. Tak, możesz sobie poprzez małpę dodać zwrot do tego naszego pliku.

**12:09** · O, tak, jak widzisz, tak jak ja to robię właśnie teraz. Ale możesz też zrobić to w inny sprytniejszy sposób. A mamy mianowicie taką komendę jak hashtag, czyli szybkie dodawanie do pamięci.

**12:19** · Możesz dodać regułę, na przykład używaj tonu profesjonalnego, ale przystępnego dla mojej widowni. I mogę kliknąć enter i zobacz jak się zachowa cloud code, jak dam mu tą kratkę z przodu. Zobaczmy sobie co robi. Czyta nasz plik clod MD, czyli to co robi hashag to on z automatu można powiedzieć wysyła w prompcie to, żeby zaktualizował plik clodem D. No i mamy dodałem wytyczną o tonę do sekcji język i ton klodem D. Jak przejdziemy do naszego pliku, zjedźmy niżej jest język ton.

### Komenda /memory

**12:50** · Wszystkie treści dokumentacja są po polsku. To mieliśmy wcześniej, natomiast używaj tonu profesjonalnego, ale przystępnego.

**12:58** · Treści są kierowane do szerokiej widowni. To jest to, co dodaliśmy przed chwilką, stosując tego hashtaga. Jest to na pewno pomocne, gdy chcesz szybko podsumować jakąś rozmowę, którą robię z Cloud Codem. Czy zauważysz w trakcie, że na przykład robi coś niepoprawnie, możesz mu powiedzieć, żeby wyciągnął z tego wnioski i właśnie podsumował to krótko w Cloud MD. W ten sposób będziesz mógł jeszcze lepiej przekazać Cloud Codowi, jak ma profesjonalnie pracować z twoim projektem.
