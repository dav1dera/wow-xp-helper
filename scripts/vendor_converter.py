#!/usr/bin/env python3
"""Build GitHub Pages by vendoring the open-source Polestar conversion engine.
No RestedXP guide data, BattleTags, account files, or personal content are fetched or published.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path, PurePosixPath
import io
import json
import shutil
import time
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
UPSTREAM = "https://aronjanosch.github.io/polestar-convert/"
SOURCE = "https://github.com/aronjanosch/polestar-convert/archive/refs/heads/main.zip"

def fetch(url):
    last_error = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "wow-xp-helper/1.0"})
            with urllib.request.urlopen(req, timeout=90) as response:
                return response.read()
        except Exception as exc:
            last_error = exc
            time.sleep(attempt + 1)
    raise RuntimeError(f"Could not fetch {url}: {last_error}")

def write(path, payload):
    p = PurePosixPath(path)
    if p.is_absolute() or ".." in p.parts or not p.parts:
        raise ValueError("Invalid asset path: " + path)
    dest = OUT / "converter" / str(p)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(payload)

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    for name in ("index.html", "compile-worker.mjs", ".nojekyll", "LICENSE"):
        shutil.copyfile(ROOT / name, OUT / name)

    archive = zipfile.ZipFile(io.BytesIO(fetch(SOURCE)))
    scripts = 0
    for item in archive.infolist():
        if item.is_dir() or not item.filename.endswith(".mjs"):
            continue
        parts = PurePosixPath(item.filename).parts
        if len(parts) >= 3 and parts[1] == "src":
            write("/".join(parts[1:]), archive.read(item))
            scripts += 1
    if scripts < 15:
        raise RuntimeError("Missing converter source modules")
    print(f"Bundled {scripts} converter modules", flush=True)

    manifest_raw = fetch(UPSTREAM + "polestar-data/manifest.json")
    manifest = json.loads(manifest_raw)
    paths = manifest.get("files", [])
    if not isinstance(paths, list) or not paths:
        raise RuntimeError("Empty game-data manifest")
    write("polestar-data/manifest.json", manifest_raw)
    assets = ["forge/polestar_convert_wasm.js", "forge/polestar_convert_wasm_bg.wasm"]
    assets += ["polestar-data/" + p for p in paths]
    def download(path):
        return path, fetch(UPSTREAM + path)
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(download, path): path for path in assets}
        for i, future in enumerate(as_completed(futures), 1):
            path, payload = future.result()
            write(path, payload)
            if i % 50 == 0 or i == len(assets):
                print(f"Fetched {i}/{len(assets)} assets", flush=True)
    print("GitHub Pages package ready", flush=True)

if __name__ == "__main__":
    main()
