# Prezenty Zojki

Lista prezentów Zojki do Mikołaja. Rodzina może na niej zaznaczać, co już zostało kupione.

- `src/lista.html`: źródło strony (lista prezentów, wygląd, logika).
- `images/`: zdjęcia prezentów (`g01.jpg` … `g25.jpg`, numery jak `id` w `src/lista.html`).
- `index.html`: gotowa strona ze zdjęciami wbudowanymi w plik. Generuje ją `python3 build.py`.

Zaznaczanie zakupionych prezentów korzysta ze współdzielonej bazy danych artefaktu na claude.ai,
więc działa tylko w opublikowanej wersji na claude.ai. Otwarta z innego miejsca (np. GitHub Pages)
strona pokaże listę, zdjęcia i linki, ale bez zaznaczania.
