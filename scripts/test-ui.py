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
            if item_id in ("cache", "folder", "manual", "auto", "guideReady", "wowClosed", "alreadyReady") and self.depth:
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
for item in ("step1", "step2", "step3", "guideReady", "wowClosed", "cache", "folder", "manual", "auto", "result", "status"):
    assert item in ui.ids, f"Missing UI component: {item}"
for item in ("cache", "folder", "guideReady", "wowClosed"):
    assert item in ui.labels, f"Missing explicit label for: {item}"
for item in ("alreadyReady", "manual", "auto"):
    assert item in ui.button_ids, f"Missing actionable button: {item}"
for term in ("Purge", "Reload", "Exit Game", "Interface\\AddOns", "Polestar", "RXPGuides.lua"):
    assert term in source, f"Missing essential instruction: {term}"
assert source.count("</body>") == 1 and source.count("</html>") == 1, "Invalid end document"
print("Beginner UI smoke checks passed:",len(ui.ids),"IDs")
