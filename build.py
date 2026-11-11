"""Buduje index.html: wstawia zdjęcia z images/ (jako data URI) do src/lista.html."""
import base64, json, pathlib

root = pathlib.Path(__file__).parent
imgs = {
    p.stem: "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
    for p in sorted((root / "images").glob("*.jpg"))
}
html = (root / "src" / "lista.html").read_text(encoding="utf-8")
(root / "index.html").write_text(html.replace("/*IMAGES*/{}", json.dumps(imgs)), encoding="utf-8")
print(f"index.html: {len(imgs)} zdjęć")
