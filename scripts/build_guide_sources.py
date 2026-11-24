#!/usr/bin/env python3
"""Create public, non-sensitive freshness metadata for the two external guide generators.

Never equate website deployments, HTTP Last-Modified, or addon releases with guide data
updates. GitHub file commits can verify Inariaa's guide.txt change date. The other
generator currently has no independently verifiable guide-file change feed: report
the version visible on its public website when recognizable, and mark date unknown.
Failures are non-fatal and must never be shown as a definitive "old" version.
"""
import datetime as dt
import html
import json
from pathlib import Path
import re
import urllib.request

OUT=Path(__file__).resolve().parents[1] / "_site" / "guide-sources.json"
UA={"User-Agent":"WoW-XP-Helper-freshness/1.0 (+https://github.com/dav1dera/wow-xp-helper)","Accept":"application/json,text/html;q=0.9"}

def fetch(url,timeout=12):
    request=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(request,timeout=timeout) as res:
        return res.read(1_500_000).decode("utf-8","replace")

def inariaa():
    payload=json.loads(fetch("https://api.github.com/repos/Inariaa/rxp_decrypter/commits?path=guide.txt&per_page=1"))
    latest=payload[0]
    date=latest["commit"]["committer"]["date"]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",date):
        raise ValueError("Invalid GitHub guide date")
    return {"guideUpdatedAt":date,"kind":"guide-file-commit","version":None,
            "sourceUrl":"https://github.com/Inariaa/rxp_decrypter/commits/main/guide.txt",
            "notes":"Ultima modifica del file guide.txt inglese, non garanzia che ogni capitolo sia nuovo."}

def forever():
    page=fetch("https://forever-free-rxp.online/en/")
    # Match a *clearly labelled* RestedXP version (not just unrelated numbers).
    versions=re.findall(r"(?:Rested\s*XP|RestedXP|RXP)\s*(?:version\s*)?v?(\d+\.\d+\.\d+)",html.unescape(page),flags=re.I)
    version=sorted(set(versions),key=lambda x:tuple(map(int,x.split("."))))[-1] if versions else None
    # The page exposes guide versions but no reliable per-guide publication timestamp.
    # Do not derive a guide date from HTML build date, response headers or git pushes.
    return {"guideUpdatedAt":None,"kind":"published-version","version":version,
            "sourceUrl":"https://forever-free-rxp.online/en/",
            "notes":"Il sito pubblica versioni, ma non una data verificabile di aggiornamento dei file delle guide."}

def main():
    now=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00","Z")
    data={"checkedAt":now,"inariaa":None,"forever":None}
    for key,task in [("inariaa",inariaa),("forever",forever)]:
        try:
            data[key]=task()
            print(f"Guide source {key}: {data[key]}",flush=True)
        except Exception as exc:
            data[key]={"guideUpdatedAt":None,"version":None,"kind":"unavailable","sourceUrl":(
                "https://github.com/Inariaa/rxp_decrypter/commits/main/guide.txt" if key=="inariaa"
                else "https://forever-free-rxp.online/en/"),
                "notes":"Fonte temporaneamente non verificabile."}
            print(f"Guide source {key}: unavailable ({type(exc).__name__}: {exc})",flush=True)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Wrote {OUT}",flush=True)

if __name__=="__main__":
    main()
