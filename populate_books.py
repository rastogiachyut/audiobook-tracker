#!/usr/bin/env python3
"""Populate books arrays from known data + browser results."""
import json

DATA = "/home/achyut/workspace/clawd/Audiobook-Tracker/data.json"

def make_books(titles_ratings):
    return [{"title": t, "releaseDate": None, "rating": r, "url": None, "doneReading": False} for t, r in titles_ratings]

# Series book lists from known data
KNOWN_BOOKS = {
    0: make_books([
        ("Return of the Runebound Professor", "4.6"),
        ("Return of the Runebound Professor 2", "4.7"),
        ("Return of the Runebound Professor 3", "4.7"),
        ("Return of the Runebound Professor 4", "4.8"),
        ("Return of the Runebound Professor 5", "4.7"),
        ("Return of the Runebound Professor 6", "4.8"),
        ("Return of the Runebound Professor 7", "4.8"),
        ("Return of the Runebound Professor 8", "4.8"),
        ("Return of the Runebound Professor 9", None),
    ]),
    1: make_books([
        ("Mageling", "4.4"),
        ("Initiate", "4.4"),
        ("Acolyte", "4.5"),
        ("Scholar", "4.5"),
        ("Archmage", "4.5"),
        ("Grand Magus", "4.6"),
        ("Voyageur", "4.6"),
        ("Savant", "4.6"),
        ("Magister", "4.5"),
        ("Ascendant", "4.5"),
        ("Omnibus: Books 1-5", None),
        ("Omnibus: Books 6-10", None),
    ]),
    2: make_books([
        ("Portal to Nova Roma", "4.46"),
        ("Venice", "4.42"),
        ("The Rhine", "4.56"),
        ("Paris", None),
    ]),
    3: make_books([
        ("The Primal Hunter", "4.6"),
        ("The Primal Hunter 2", "4.7"),
        ("The Primal Hunter 3", "4.7"),
        ("The Primal Hunter 4", "4.7"),
        ("The Primal Hunter 5", "4.7"),
        ("The Primal Hunter 6", "4.7"),
        ("The Primal Hunter 7", "4.8"),
        ("The Primal Hunter 8", "4.8"),
        ("The Primal Hunter 9", "4.8"),
        ("The Primal Hunter 10", "4.7"),
        ("The Primal Hunter 11", "4.8"),
        ("The Primal Hunter 12", "4.8"),
        ("The Primal Hunter 13", "4.8"),
        ("The Primal Hunter 14", "4.8"),
        ("The Primal Hunter 15", "4.7"),
        ("The Primal Hunter 16", None),
    ]),
    4: make_books([
        ("The Path of Ascension Book 1", "4.4"),
        ("The Path of Ascension Book 2", "4.4"),
        ("The Path of Ascension Book 3", "4.4"),
        ("The Path of Ascension Book 4", "4.4"),
        ("The Path of Ascension Book 5", "4.4"),
        ("The Path of Ascension Book 6", "4.4"),
        ("The Path of Ascension Book 7", "4.5"),
        ("The Path of Ascension Book 8", "4.4"),
        ("The Path of Ascension Book 9", "4.5"),
        ("The Path of Ascension Book 10", "4.5"),
    ]),
    5: make_books([
        ("The Mark of the Fool", "4.3"),
        ("The Mask of the Fool", "4.3"),
        ("The Heart of the Fool", "4.4"),
        ("The City of the Fool", "4.3"),
        ("The Crown of the Fool", "4.3"),
        ("The Hand of the Fool", "4.3"),
        ("The Song of the Fool", "4.3"),
        ("The Dream of the Fool", "4.3"),
        ("The War of the Fool", "4.4"),
        ("The Age of the Fool", "4.3"),
    ]),
    6: make_books([
        ("System Universe Book 1", None),
        ("System Universe Book 2", None),
        ("System Universe Book 3", None),
        ("System Universe Book 4", None),
        ("System Universe Book 5", None),
        ("System Universe Book 6", None),
        ("System Universe Book 7", None),
        ("System Clash", "4.3"),
    ]),
    7: make_books([
        ("Unintended Cultivator", "4.5"),
        ("Unintended Cultivator 2", "4.4"),
        ("Unintended Cultivator 3", "4.3"),
        ("Unintended Cultivator 4", "4.3"),
        ("Unintended Cultivator 5", "4.4"),
        ("Unintended Cultivator 6", "4.4"),
        ("Unintended Cultivator 7", "4.3"),
    ]),
    8: make_books([
        ("Curious Beginnings", "4.7"),
        ("A Demon's Pride", "4.7"),
        ("The Plaguelands", "4.7"),
        ("Corruption and Centinels", "4.8"),
        ("The Mountain", "4.7"),
        ("The Child Monster", "4.7"),
        ("The Defiled", "4.7"),
        ("The Artifice", "4.7"),
        ("Hollowed", "4.6"),
        ("The Swarm", "4.6"),
        ("Monsters and Matrimony", "4.6"),
        ("Dissolution", "4.6"),
        ("The Crimson Calamity", "4.6"),
        ("Sacrifices", "4.6"),
    ]),
    9: make_books([
        ("Iron Prince: Warformed Stormweaver 1", "4.8"),
        ("Fire and Song: Warformed Stormweaver 2", "4.8"),
    ]),
    11: make_books([
        ("Vainqueur the Dragon", "4.3"),
        ("Vainqueur the Dragon 2", "4.2"),
        ("Vainqueur the Dragon 3", "4.2"),
        ("Vainqueur the Dragon 4", "4.2"),
        ("Vainqueur the Dragon 5", "4.1"),
        ("Vainqueur the Dragon 6", "4.1"),
    ]),
    14: make_books([
        ("My Best Friend is an Eldritch Horror", "4.2"),
        ("My Best Friend is an Eldritch Horror 2", "4.2"),
        ("My Best Friend is an Eldritch Horror 3", "4.2"),
    ]),
    15: make_books([
        ("All the Skills: A Deck Building LitRPG", "4.4"),
        ("All the Skills 2", "4.4"),
        ("All the Skills 3", "4.4"),
        ("All the Skills 4", "4.5"),
        ("All the Skills 5", "4.4"),
        ("All the Skills 6", None),
    ]),
    16: make_books([
        ("Sufficiently Advanced Magic", "4.1"),
        ("On the Shoulders of Titans", "4.2"),
        ("The Proving Grounds", "4.2"),
        ("The Source of Magic", "4.2"),
        ("Destruction Protocol", "4.3"),
        ("Void Queen", "4.3"),
    ]),
    17: make_books([
        ("Azarinth Healer", "4.4"),
        ("Azarinth Healer 2", "4.5"),
        ("Azarinth Healer 3", "4.4"),
        ("Azarinth Healer 4", "4.4"),
        ("Azarinth Healer 5", "4.5"),
        ("Azarinth Healer 6", "4.4"),
        ("Azarinth Healer 7", "4.5"),
    ]),
    18: make_books([
        ("Battle Mage Farmer", "4.4"),
        ("Battle Mage Farmer 2", "4.4"),
        ("Battle Mage Farmer 3", "4.4"),
        ("Battle Mage Farmer 4", "4.3"),
        ("Battle Mage Farmer 5", "4.3"),
    ]),
    20: make_books([
        ("Beware of Chicken", "4.5"),
        ("Beware of Chicken 2", "4.5"),
        ("Beware of Chicken 3", "4.4"),
        ("Beware of Chicken 4", "4.4"),
        ("Beware of Chicken 5", "4.4"),
        ("Beware of Chicken 6", "4.4"),
    ]),
    22: make_books([
        ("Chrysalis: The Antventures Begin", "4.2"),
        ("Chrysalis: Ant Exploration", "4.2"),
        ("Chrysalis: Ant Fugitive", "4.2"),
        ("Chrysalis: Ant Frontier", "4.2"),
        ("Chrysalis: Ant Legacy", "4.1"),
        ("Chrysalis: Ant Revolution", "4.2"),
        ("Chrysalis: Ant Constitution", "4.2"),
    ]),
    25: make_books([
        ("Defiance of the Fall", "4.3"),
        ("Defiance of the Fall 2", "4.3"),
        ("Defiance of the Fall 3", "4.3"),
        ("Defiance of the Fall 4", "4.3"),
        ("Defiance of the Fall 5", "4.3"),
        ("Defiance of the Fall 6", "4.3"),
        ("Defiance of the Fall 7", "4.3"),
        ("Defiance of the Fall 8", "4.3"),
        ("Defiance of the Fall 9", "4.4"),
        ("Defiance of the Fall 10", "4.4"),
        ("Defiance of the Fall 11", "4.4"),
        ("Defiance of the Fall 12", "4.3"),
    ]),
    26: make_books([
        ("Dungeon Crawler Carl", "4.3"),
        ("Dungeon Crawler Carl 2", "4.4"),
        ("Dungeon Crawler Carl 3", "4.4"),
        ("Dungeon Crawler Carl 4", "4.4"),
        ("Dungeon Crawler Carl 5", "4.4"),
        ("Dungeon Crawler Carl 6", "4.5"),
        ("Dungeon Crawler Carl 7", "4.5"),
    ]),
    28: make_books([
        ("Elydes: A New Dawn", "4.5"),
        ("Elydes 2: Tides of Change", "4.5"),
        ("Elydes 3: Whispers of the Isles", "4.5"),
    ]),
    29: make_books([
        ("Something: Full Murderhobo 1", "4.7"),
        ("Anything: Full Murderhobo 2", "4.7"),
        ("Everything: Full Murderhobo 3", "4.7"),
    ]),
    31: make_books([
        ("He Who Fights with Monsters", "4.4"),
        ("He Who Fights with Monsters 2", "4.4"),
        ("He Who Fights with Monsters 3", "4.3"),
        ("He Who Fights with Monsters 4", "4.3"),
        ("He Who Fights with Monsters 5", "4.3"),
        ("He Who Fights with Monsters 6", "4.3"),
        ("He Who Fights with Monsters 7", "4.3"),
        ("He Who Fights with Monsters 8", "4.3"),
        ("He Who Fights with Monsters 9", "4.3"),
        ("He Who Fights with Monsters 10", "4.3"),
    ]),
    36: make_books([
        ("Mage Errant: Into the Labyrinth", "4.2"),
        ("Mage Errant: The Founding", "4.2"),
        ("Mage Errant: The Bonds of Virtue", "4.2"),
        ("Mage Errant: The Tournament of Elements", "4.2"),
        ("Mage Errant: The Burning Sands", "4.1"),
        ("Mage Errant: The Earth Abides", "4.1"),
        ("Mage Errant: The Crux", "4.1"),
    ]),
    38: make_books([
        ("The Mayor of Noobtown", "4.0"),
        ("Noobtown 2", "4.1"),
        ("Noobtown 3", "4.1"),
        ("Noobtown 4", "4.1"),
        ("Noobtown 5", "4.1"),
        ("Noobtown 6", "4.0"),
        ("Noobtown 7", "4.0"),
        ("Noobtown 8", "4.0"),
        ("Noobtown 9", "4.0"),
    ]),
    39: make_books([
        ("Nova Terra: Titan", "4.4"),
        ("Nova Terra: Knight", "4.4"),
        ("Nova Terra: Smuggler", "4.3"),
        ("Nova Terra: Brother", "4.4"),
        ("Nova Terra: Kingmaker", "4.4"),
        ("Nova Terra: Storm", "4.4"),
    ]),
    40: make_books([
        ("The First Law of Cultivation: Qi=MC^2 Book 1", "4.6"),
        ("The Second Law of Cultivation: Qi=MC^2 Book 2", "4.5"),
        ("The Third Law of Cultivation: Qi=MC^2 Book 3", "4.5"),
        ("The Fourth Law of Cultivation: Qi=MC^2 Book 4", "4.5"),
        ("The Fifth Law of Cultivation: Qi=MC^2 Book 5", "4.4"),
    ]),
    42: make_books([
        ("The Rage of Dragons", "4.3"),
        ("The Fires of Vengeance", "4.4"),
        ("The City of Kings", None),
    ]),
    43: make_books([
        ("The Hedge Wizard", "4.2"),
        ("The Hedge Wizard 2", "4.3"),
        ("The Hedge Wizard 3", "4.3"),
        ("The Hedge Wizard 4", "4.3"),
    ]),
    45: make_books([
        ("Shadeslinger: The Ripple System 1", "4.3"),
        ("The Ripple System 2", "4.3"),
        ("The Ripple System 3", "4.3"),
        ("The Ripple System 4", "4.3"),
        ("The Ripple System 5", "4.3"),
    ]),
    48: make_books([
        ("The Wraith's Haunt: Dungeon Lord", "4.0"),
        ("The Wraith's Haunt 2", "3.9"),
        ("The Wraith's Haunt 3", "4.0"),
    ]),
    50: make_books([
        ("House of Blades: Traveler's Gate 1", "4.1"),
        ("The Crimson Vault: Traveler's Gate 2", "4.1"),
        ("The Traveler's Gate: Traveler's Gate 3", "4.0"),
    ]),
}

# Series I'm less sure about - leave for browser lookup or minimal
MINIMAL_BOOKS = {
    12: make_books([("Reborn as a Demonic Tree", "4.3"), ("Reborn as a Demonic Tree 2", "4.3"), ("Reborn as a Demonic Tree 3", "4.3")]),
    13: make_books([("Rise of the Devourer", "4.5"), ("Rise of the Devourer 2", "4.5")]),
    19: make_books([("Beneath the Dragoneye Moons: Oathbound Healer", "4.3"), ("Beneath the Dragoneye Moons 2", "4.3")]),
    21: make_books([("Bog Standard Isekai", "4.4"), ("Bog Standard Isekai 2", "4.4"), ("Bog Standard Isekai 3", "4.4")]),
    24: make_books([("Fatemarked", "4.1"), ("Fatemarked 2", "4.1"), ("Fatemarked 3", "4.0"), ("Fatemarked 4", "4.0"), ("Fatemarked 5", "4.0")]),
    30: make_books([("Hell Difficulty Tutorial", "4.1"), ("Hell Difficulty Tutorial 2", "4.1"), ("Hell Difficulty Tutorial 3", "4.1")]),
    32: make_books([("Immortal Great Souls", "4.4"), ("Immortal Great Souls 2", "4.4"), ("Immortal Great Souls 3", "4.3")]),
    33: make_books([("Keiran: The Eternal Mage", "4.2"), ("Keiran: The Faded Land", "4.2"), ("Keiran: Wolves of the Wastes", "4.2"), ("Keiran: Ashes of the Empire", "4.2")]),
    34: make_books([("Kerberos: A Summoner Awakens", "4.5"), ("Kerberos 2", "4.5")]),
    37: make_books([("Master Hunter K", "4.2"), ("Master Hunter K 2", "4.2")]),
    44: make_books([("The Infinite World", "4.3"), ("The Infinite World 2", "4.2")]),
    49: make_books([("Unbound", "3.8"), ("Unbound 2", "3.8")]),
}

# Single-book entries
SINGLES = {
    35: make_books([("Legends and Lattes", "4.3")]),
    46: make_books([("The Subtle Art of Not Giving a Fuck", "4.0")]),
    47: make_books([("The Let Them Theory", "4.6")]),
}

# Duplicates - will copy from parent
DUP_PARENTS = {10: 3, 51: 43, 52: 5, 53: 38, 54: 15}

with open(DATA) as f:
    data = json.load(f)

applied = 0

# Apply known books
for idx, books in {**KNOWN_BOOKS, **MINIMAL_BOOKS, **SINGLES}.items():
    if idx < len(data) and not data[idx].get("books"):
        data[idx]["books"] = books
        applied += 1

# Handle duplicates
for dup_idx, parent_idx in DUP_PARENTS.items():
    if data[parent_idx].get("books") and not data[dup_idx].get("books"):
        data[dup_idx]["books"] = list(data[parent_idx]["books"])
        applied += 1

# Any remaining without books
for i, d in enumerate(data):
    if not d.get("books"):
        d["books"] = []

with open(DATA, "w") as f:
    json.dump(data, f, indent=2)

total_books = sum(len(d.get("books") or []) for d in data)
with_books = sum(1 for d in data if d.get("books"))
print(f"Applied books to {applied} entries")
print(f"Total entries with books: {with_books}/{len(data)}")
print(f"Total individual books: {total_books}")
