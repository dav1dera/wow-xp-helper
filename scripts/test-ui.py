#!/usr/bin/env python3
"""Smoke-test the beginner UI: the essential steps cannot be hidden in accordions."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys

class UI(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.ids = []
        self.hidden_essentials = []
        self.button_ids = set()
        self.labels = {}
        self.links = []
    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if tag == "details":
            self.depth += 1
        item_id = props.get("id")
        if item_id:
            self.ids.append(item_id)
            if item_id in ("cache", "folder", "manual", "guideReady", "wowClosed", "alreadyReady") and self.depth:
                self.hidden_essentials.append(item_id)
            if tag == "button":
                self.button_ids.add(item_id)
        if tag == "label" and props.get("for"):
            self.labels[props["for"]] = True
        if tag == "a" and props.get("href"):
            self.links.append(props["href"])
    def handle_endtag(self, tag):
        if tag == "details":
            self.depth -= 1
            assert self.depth >= 0

source = Path(sys.argv[1]).read_text(encoding="utf-8")
ui = UI()
ui.feed(source)
assert ui.depth == 0, "Unclosed details"
duplicates = [k for k, n in Counter(ui.ids).items() if n > 1]
assert not duplicates, f"Duplicate DOM ids: {duplicates}"
assert not ui.hidden_essentials, f"Essential controls hidden inside an expandable section: {ui.hidden_essentials}"
for item in ("step0", "step1", "step2", "step3", "guideReady", "wowClosed", "cache", "folder", "manual", "auto", "result", "status", "installedFolders", "checkedInGame", "installChecklistStatus", "wowPath", "accountPath", "rxpPath", "addonsPath", "copyAccountPath", "copyRxpPath", "copyAddonsPath"):
    assert item in ui.ids, f"Missing UI component: {item}"
for item in ("cache", "folder", "guideReady", "wowClosed", "installedFolders", "checkedInGame"):
    assert item in ui.labels, f"Missing explicit label for: {item}"
for item in ("alreadyReady", "manual", "auto"):
    assert item in ui.button_ids, f"Missing actionable button: {item}"
for term in ("WowUp", "Get Addons", "Install from URL", "RestedXP Guides", "Polestar Guides", "Purge", "Exit Game", "Suggest guides from", "RXPGuides.lua", "disattiva", "copyAccountPath", "copyRxpPath", "copyAddonsPath", "by Katra Mundo", "C:\\Program Files (x86)\\World of Warcraft\\_forever_"):
    assert term in source, f"Missing important quick-start instruction: {term}"
# Each essential action is visible: optional automated import and settings may be folded.
assert source.index('id="step0"') < source.index('id="step1"') < source.index('id="step2"') < source.index('id="step3"')
assert source.index('id="compat"') < source.index('id="manual"')
assert source.index('id="cache"') < source.index('id="manual"')
for phrase in ("Polestar 0.4.3", "22 cartelle", "PolestarPack_*", "non basta", "Copy report", "/polestar packs"):
    assert phrase in source, f"Missing Polestar 0.4.3 migration guidance: {phrase}"
assert 'id="polestar043"' in source, "Missing Polestar 0.4.3 release note"
assert source.count('<div class="stepnum">') == 4
for item in ("inariaaFreshness", "foreverFreshness", "inariaaDetails", "foreverDetails", "sourceComparison"):
    assert item in ui.ids, f"Missing guide source freshness indicator: {item}"
assert 'guide-sources.json' in source, "Guide freshness JSON is not loaded"
assert "src/rxp/saved.mjs" in source, "Updated RestedXP cache reader is not used"
assert 'non pubblica una data verificabile' in source, "Source date uncertainty warning missing"
for crawler in ("robots", "googlebot", "bingbot"):
    tag = f'<meta name="{crawler}" content="noindex, nofollow, noarchive, noimageindex">'
    assert tag in source.split("</head>", 1)[0], f"Missing noindex meta for {crawler}"
assert source.count("</body>") == 1 and source.count("</html>") == 1, "Invalid end document"
print("Beginner UI smoke checks passed:",len(ui.ids),"IDs")
