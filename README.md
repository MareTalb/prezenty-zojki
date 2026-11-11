# Prezenty Zojki

Lista prezentów Zojki do Mikołaja. Rodzina może na niej zaznaczać, co już zostało kupione.

## Pliki

- `src/lista.html`: źródło strony (lista prezentów, wygląd, logika).
- `images/`: zdjęcia prezentów (`g01.jpg` … `g26.jpg`, numery jak `id` w `src/lista.html`).
- `build.py`: buduje gotowe strony ze źródła i zdjęć: `python3 build.py`.
- `index.html`: gotowa strona dla GitHub Pages. Zaznaczenia zapisuje w Firestore (projekt Firebase `prezenty-zojki`).
- `artifact.html`: ta sama strona w wersji dla claude.ai (tam zaznaczenia trafiają do bazy claude.ai).
- `firestore.rules`: reguły bezpieczeństwa Firestore.

## Firebase

1. Konsola Firebase → **Build → Firestore Database → Create database** (lokalizacja `eur3`, production mode).
2. Zakładka **Rules** → wklej zawartość `firestore.rules` → **Publish**.

Reguły pozwalają każdemu tylko odczytać listę i oznaczyć prezent jako kupiony. Żeby cofnąć oznaczenie,
usuń dokument z kolekcji `kupione` w konsoli Firebase (np. `g07`).

## Dodawanie prezentu

1. Dopisz wpis na końcu listy `GIFTS` w `src/lista.html` z kolejnym `id` (np. `g27`).
2. Dodaj zdjęcie `images/g27.jpg` (najlepiej ok. 360 px).
3. Uruchom `python3 build.py` i wypchnij zmiany.
