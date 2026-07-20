# 🌌 Galaxy Dashboard

Samowystarczalny dashboard vaultu — jeden plik HTML (offline, bez internetu),
który pokazuje statystyki i galaktyczny graf połączeń notatek.

## Co zawiera

- **Liczba notatek w każdym folderze** (Resources, Galaxy, Projects, Areas, Inbox…)
- **Top 10 labels**, **Top 10 authors**, **Top 10 wikilinks**
- **Graf „galaxy"** — węzły to notatki (jak gwiazdy), krawędzie to wikilinki
  notatka→notatka. Tytuł każdego **rodzaju notatki** ma inny kolor:
  Clippings, Emails, Reports, LinkedIn, Concept (Galaxy), Project, Area, Inne.

Węzły pomijane: `Archives/` i `Attachments/` (duplikaty / nie-notatki) oraz
pliki-katalogi (`index.md`, `CLAUDE.md`) — łączą się ze wszystkim i psuły graf.

## Odświeżenie (aktualizacja danych)

```bash
python3 Dashboard/galaxy-dashboard.py
```

Skanuje aktualny stan vaultu i nadpisuje `Dashboard/Galaxy Dashboard.html`.
Otwórz ten plik w przeglądarce (Finder → prawy przycisk → Otwórz w…).

Plik HTML jest wykluczony z gita (`.gitignore`) — regeneruje się z jednej
komendy, więc nie trzymamy 900 KB w historii.

## Automatyczna aktualizacja (opcjonalnie)

Żeby dashboard odświeżał się po każdej sesji Claude w vaultcie, można dopisać
regenerację do istniejącego hooka `Stop` w `.claude/settings.json`:

```
python3 /Users/piotr_air/Obsidian/Piotr/Dashboard/galaxy-dashboard.py
```

Albo uruchamiać ręcznie komendą powyżej, kiedy chcesz świeży obraz.

## Sterowanie w grafie

- **kółko myszy** — zoom, **przeciąganie tła** — przesuwanie, **przeciąganie węzła** — układanie
- **najechanie** — podświetla sąsiadów + tooltip (rodzaj, folder, liczba połączeń)
- **legenda** (lewy dół) — klik ukrywa/pokazuje dany rodzaj notatki
- **szukaj** — wyróżnia notatki po tytule
- **ukryj samotne** — chowa notatki bez połączeń (skup się na rdzeniu galaktyki)
- **pauza** — zatrzymuje symulację
