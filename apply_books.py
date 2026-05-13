#!/usr/bin/env python3
"""Apply fetched book data to the JSON from raw browser output strings."""
import json, sys, re

DATA = "/home/achyut/workspace/clawd/Audiobook-Tracker/data.json"

def parse_books(raw_str, series_title):
    """Parse browser-extracted books and filter to series-relevant ones."""
    try:
        books = json.loads(raw_str)
    except:
        return []
    
    if not books:
        return []
    
    # Filter to series-relevant books
    series_words = [w.lower() for w in series_title.split() if len(w) > 3]
    # Add common series abbreviations
    word_map = {
        "cradle": ["cradle"],
        "primal": ["primal"],
        "hunter": ["hunter"],
        "salvos": ["salvos"],
        "mark": ["mark", "fool"],
        "fool": ["mark", "fool"],
        "warformed": ["warformed", "stormweav"],
        "stormweave": ["warformed", "stormweav"],
        "chrysalis": ["chrysalis", "antventur"],
        "defiance": ["defiance"],
        "dungeon": ["dungeon", "crawler", "carl"],
        "mage": ["mage errant"],
        "errant": ["mage errant"],
        "noobtown": ["noobtown", "mayor"],
        "beware": ["beware", "chicken"],
        "chicken": ["beware", "chicken"],
        "battle": ["battle mage"],
        "azarinth": ["azarinth"],
        "nova": ["nova terra"],
        "terra": ["nova terra"],
        "hedge": ["hedge wizard"],
        "wizard": ["hedge wizard"],
        "he who": ["he who fights"],
        "fights": ["he who fights"],
        "monsters": ["he who fights"],
        "unintended": ["unintended"],
        "cultivator": ["unintended"],
        "vainqueur": ["vainqueur"],
        "dragon": ["vainqueur"],
        "portal": ["portal to nova"],
        "roma": ["portal to nova"],
        "arcane": ["arcane ascension", "sufficiently"],
        "ascension": ["path of ascension", "arcane"],
        "path": ["path of ascension"],
        "keiran": ["keiran"],
        "kerberos": ["kerberos"],
        "full": ["full murderhobo"],
        "murderhobo": ["full murderhobo"],
        "elydes": ["elydes"],
        "qi": ["qi=mc", "cultivation"],
        "mc": ["qi=mc", "cultivation"],
        "rage": ["rage of dragons"],
        "dragons": ["rage of dragons"],
        "infinite": ["infinite world"],
        "ripple": ["ripple system"],
        "shadeslinger": ["ripple system"],
        "fatemarked": ["fatemarked"],
        "wraith": ["wraith", "dungeon lord"],
        "unbound": ["unbound"],
        "traveler": ["traveler", "house of blades"],
        "gate": ["traveler", "house of blades"],
        "hugo": ["wraith", "hugo huesca"],
        "eight": ["law of the jungle", "eight"],
        "system": ["system universe", "system clash"],
        "universe": ["system universe", "system clash"],
        "reborn": ["reborn", "demonic tree"],
        "demonic": ["reborn", "demonic tree"],
        "tree": ["reborn", "demonic tree"],
        "hell": ["hell difficulty"],
        "difficulty": ["hell difficulty"],
        "tutorial": ["hell difficulty"],
        "rise": ["rise of the devourer"],
        "devourer": ["rise of the devourer"],
        "eldritch": ["eldritch horror"],
        "horror": ["eldritch horror"],
        "skills": ["all the skills"],
        "bog": ["bog standard", "scarred"],
        "standard": ["bog standard"],
        "isekai": ["bog standard"],
        "master": ["master hunter"],
        "immortal": ["immortal great souls"],
        "great": ["immortal great souls"],
        "souls": ["immortal great souls"],
        "runebound": ["runebound professor"],
        "professor": ["runebound professor"],
        "millennial": ["millennial mage"],
        "mageling": ["millennial mage"],
        "all": ["all the skills"],
    }
    
    expanded_words = []
    for w in series_words:
        expanded_words.append(w)
        if w in word_map:
            expanded_words.extend(word_map[w])
    
    filtered = []
    for b in books:
        bt = b["title"].lower()
        match_count = sum(1 for w in expanded_words if w in bt)
        if match_count >= 1:
            filtered.append({
                "title": b["title"],
                "releaseDate": None,
                "rating": b.get("rating"),
                "url": b.get("url"),
                "doneReading": False
            })
    
    return filtered if filtered else [{"title": b["title"], "releaseDate": None, "rating": b.get("rating"), "url": b.get("url"), "doneReading": False} for b in books[:8]]

# Read current data
with open(DATA) as f:
    data = json.load(f)

# This script will be called with: python apply_books.py IDX RAW_JSON
idx = int(sys.argv[1])
raw = sys.argv[2]

if idx < len(data):
    books = parse_books(raw, data[idx]["title"])
    data[idx]["books"] = books
    
    with open(DATA, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"[{idx}] {data[idx]['title']}: {len(books)} books")
else:
    print(f"ERROR: idx {idx} out of range")
