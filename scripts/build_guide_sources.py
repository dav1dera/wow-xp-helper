#!/usr/bin/env python3
"""Publish independently sourced update metadata for WoW Forever RXP import generators.

Do not mistake a repository push/site build for an update of the guide text.
All fetched data is public; no user's guide files or BattleTag are transmitted.
Missing sources remain 'unverified' instead of being silently ranked as older.
"""
import datetime as dt
import html
import json
from pathlib import Path
import re
import urllib.request

OUT=Path(__file__).resolve().parents[1] / "_site" / "guide-sources.json"
UA={"User-Agent":"WoW-XP-Helper-sources/1.1 (+https://github.com/dav1dera/wow-xp-helper)",
    "Accept":"application/json,text/html;q=0.9"}
SOURCE_URLS={
    "inariaa":"https://inariaa.github.io/rxp_decrypter/",
    "forever":"https://forever-free-rxp.online/en/",
    "avery":"https://averyp-git.github.io/rested-exp-free/",
    "kostya":"https://rxp.kostya.sexy/",
}

def fetch(url,timeout=15):
    with urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout) as response:
        return response.read(2_100_000).decode("utf-8","replace")

def valid_iso(value):
    if not isinstance(value,str) or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ",value):
        raise ValueError("Invalid ISO timestamp")
    dt.datetime.fromisoformat(value.replace("Z","+00:00"))
    return value

def gh_commit(url):
    rows=json.loads(fetch(url))
    if not isinstance(rows,list) or not rows:
        raise ValueError("No GitHub commits available")
    return valid_iso(rows[0]["commit"]["committer"]["date"])

def extract_version(page,pattern):
    candidates=re.findall(pattern,html.unescape(page),re.I)
    if not candidates:return None
    vals=list(set(candidates))
    return sorted(vals,key=lambda v:tuple(map(int,re.findall(r"\d+",v))))[-1]

def meta(key,kind="unavailable",version=None,**kwargs):
    return {"kind":kind,"guideUpdatedAt":None,"siteUpdatedAt":None,
            "declaredGuideDate":None,"declaredSiteDate":None,"guideReleaseDate":None,
            "version":version,"sourceUrl":SOURCE_URLS[key],
            "notes":"Versione o data delle guide non verificabile.",**kwargs}

def inariaa():
    date=gh_commit("https://api.github.com/repos/Inariaa/rxp_decrypter/commits?path=guide.txt&per_page=1")
    return meta("inariaa",kind="guide-file-commit",
        guideUpdatedAt=date,
        sourceUrl="https://github.com/Inariaa/rxp_decrypter/commits/main/guide.txt",
        notes="Data del commit del file inglese guide.txt. Non garantisce che tutti i capitoli siano nuovi.")

def forever():
    page=fetch(SOURCE_URLS["forever"])
    version=extract_version(page,r"(?:Rested\s*XP|RestedXP|RXP)\s*(?:version\s*)?v?(\d+\.\d+\.\d+)")
    # The visible 'Updated: DD.MM.YYYY' is a site claim, not a verified guide-file commit.
    plain=re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",html.unescape(page)))
    match=re.search(r"\bUpdated\s*:\s*(\d{1,2})[./-](\d{1,2})[./-](20\d{2})",plain,re.I)
    declared=None
    if match:
        try:
            declared=dt.date(int(match.group(3)),int(match.group(2)),int(match.group(1))).isoformat()
        except ValueError:
            pass
    return meta("forever",kind="published-version",version=version,declaredSiteDate=declared,
        notes="Versione RestedXP dichiarata sul sito. Il campo 'Updated' riguarda il sito e non viene usato per datare le guide.")

def avery():
    # Read the generator's *embedded addon version* from the page footer metadata,
    # not its GitHub commit or build timestamp. Current format:
    # const meta = {"built":"...","addon":{"version":"v4.11.35","released":"2026-11-08",...}};
    page=fetch("https://raw.githubusercontent.com/averyp-git/rested-exp-free/main/index.html")
    match=re.search(r"\bconst\s+meta\s*=\s*(\{[^\r\n;]+\})\s*;",page)
    if not match:
        raise ValueError("Avery addon metadata not present")
    addon=json.loads(match.group(1)).get("addon") or {}
    version=str(addon.get("version","")).strip()
    if not re.fullmatch(r"v?\d+\.\d+\.\d+",version):
        raise ValueError("Avery addon version missing or invalid")
    version=version.lstrip("v")
    released=addon.get("released")
    release_date=None
    if isinstance(released,str):
        try:
            release_date=dt.date.fromisoformat(released).isoformat()
        except ValueError:
            pass
    return meta("avery",kind="embedded-guide-version",version=version,
        guideReleaseDate=release_date,
        notes="Versione RXPGuides dichiarata nei metadati della pagina Avery; data 'released' del pacchetto inclusa, non data di creazione del sito né conferma indipendente dei contenuti.")

def kostya():
    page=fetch(SOURCE_URLS["kostya"])
    version=extract_version(page,r"\bv(4\.11\.\d{1,4})\b")
    # Read a date only when explicitly displayed next to an RXP guide version.
    # This is a claim of the site, not an independently verified guide-file timestamp.
    text=html.unescape(page)
    plain=re.sub(r"<[^>]+>"," ",text)
    plain=re.sub(r"\s+"," ",plain)
    # The site uses e.g. '20.11.2026 · v4.11.37' (day.month.year).
    match=re.search(r"(?<!\d)(\d{2})[./-](\d{2})[./-](20\d{2}).{0,220}?\bv4\.11\.\d{1,4}\b",plain)
    claimed=None
    if match:
        try:
            claimed=dt.date(int(match.group(3)),int(match.group(2)),int(match.group(1))).isoformat()
        except ValueError:
            pass
    return meta("kostya",kind="site-declared-guide-date",
        version=version,declaredGuideDate=claimed,
        notes="Versione e data della guida ufficiale 1-60 dichiarate sulla pagina Forever RXP; non verificate su un file separato.")

TASKS={"inariaa":inariaa,"forever":forever,"avery":avery,"kostya":kostya}

def main():
    checked_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00","Z")
    output={"checkedAt":checked_at,"sources":{}}
    for name,task in TASKS.items():
        try:
            item=task()
            output["sources"][name]=item
            print(f"Guide source {name}: {item}",flush=True)
        except Exception as exc:
            output["sources"][name]=meta(name,notes="Fonte temporaneamente non verificabile; nessun dato recente confermato.")
            print(f"Guide source {name}: unavailable ({type(exc).__name__}: {exc})",flush=True)
    # Compatibility with old UI readers; removed after all clients refresh.
    output.update({name:output["sources"][name] for name in ("inariaa","forever")})
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Wrote {OUT}",flush=True)

if __name__=="__main__":
    main()
