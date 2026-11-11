"""Buduje stronę z src/lista.html i zdjęć z images/ (wstawionych jako data URI).

- index.html     pełny dokument HTML dla GitHub Pages (zaznaczenia w Firestore)
- artifact.html  fragment strony dla claude.ai (nagłówek dokumentu dodaje claude.ai)
"""
import base64, json, pathlib

root = pathlib.Path(__file__).parent
imgs = {
    p.stem: "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
    for p in sorted((root / "images").glob("*.jpg"))
}
body = (root / "src" / "lista.html").read_text(encoding="utf-8").replace("/*IMAGES*/{}", json.dumps(imgs))

(root / "artifact.html").write_text(body, encoding="utf-8")

head = (
    "<!doctype html>\n<html lang=\"pl\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
)
# Move <title>, <meta>, <link> and <style> from the top of the fragment into <head>.
split = body.index("<div class=\"wrap\">")
(root / "index.html").write_text(
    head + body[:split] + "</head>\n<body>\n" + body[split:] + "\n</body>\n</html>\n", encoding="utf-8"
)
print(f"index.html + artifact.html: {len(imgs)} zdjęć")
