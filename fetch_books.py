#!/usr/bin/env python3
"""
Fetch all books in each series from Amazon search results.
Uses the OpenClaw browser tool via exec calls.
"""

import json
import subprocess
import sys
import time
import os

DATA_FILE = "/home/achyut/workspace/clawd/Audiobook-Tracker/data.json"
BROWSER_CTL = "openclaw"  # We'll use direct Chrome DevTools instead

# Series to look up, with Amazon search query
# Skipping duplicates (idx 10, 51-54)
SERIES = [
    (0, "Return of the Runebound Professor", "Actus"),
    (1, "Millennial Mage", "J.L. Mullins"),
    (2, "Portal to Nova Roma", "J.R. Mathews"),
    (3, "The Primal Hunter", "Zogarth"),
    (4, "The Path of Ascension", "C.M. Rosens"),
    (5, "The Mark of the Fool", "J.M. Clarke"),
    (6, "System Universe", "Clyve R. A."),
    (7, "Unintended Cultivator", "Eric Dontigney"),
    (8, "Salvos", "V.A. Lewis"),
    (9, "Warformed Stormweave", "Bryce O'Connor"),
    # 10: Primul Hunter - DUP of The Primal Hunter
    (11, "Vainqueur the Dragon", "Maxime J. Durvaux"),
    (12, "Reborn as a Demonic Tree", "Spicy Zero"),
    (13, "Rise of the Devourer", "Harrison Frye"),
    (14, "My Best Friend is an Eldritch Horror", "Actus"),
    (15, "All the Skills", "Honor Rae"),
    (16, "Arcane Ascension", "Andrew Rowe"),
    (17, "Azarinth Healer", "Rhaegar"),
    (18, "Battle Mage Farmer", "Michael Gallagher"),
    (19, "Beneath the Dragoneye Moons", "Selkie Myth"),
    (20, "Beware of Chicken", "Casualfarmer"),
    (21, "Bog Standard Isekai", "Mecanimus"),
    (22, "Chrysalis", "RinoZ"),
    (23, "Cradle", "Will Wight"),
    (24, "The Fatemarked Epic", "David Estes"),
    (25, "Defiance of the Fall", "JF Brink"),
    (26, "Dungeon Crawler Carl", "Matt Dinniman"),
    (27, "Eight", "C.M. McGuire"),
    (28, "Elydes", "Drew Wells"),
    (29, "Full Murderhobo", "Dakota Krout"),
    (30, "Hell Difficulty Tutorial", "David Petry"),
    (31, "He Who Fights with Monsters", "Shirtaloon"),
    (32, "Immortal Great Souls", "M.H. Cadmus"),
    (33, "Keiran: The Eternal Mage", "C.M. Rosens"),
    (34, "Kerberos: A Summoner Awakens", "S.F. Baumgartner"),
    (35, "Legends and Lattes", "Travis Baldree"),
    (36, "Mage Errant", "John Bierce"),
    (37, "Master Hunter K", "K.S.A. Weld"),
    (38, "Noobtown", "Ryan Rimmel"),
    (39, "Nova Terra", "Seth Ring"),
    (40, "Qi=MC²", "KrazeKode"),
    (41, "Realm of the Elderlings", "Robin Hobb"),
    (42, "The Rage of Dragons", "Evan Winter"),
    (43, "The Hedge Wizard", "K.M. Stormer"),
    (44, "The Infinite World", "J.R. Morrill"),
    (45, "The Ripple System", "Kyle Kirrin"),
    (46, "The Subtle Art of Not Giving a Fuck", "Mark Manson"),
    (47, "The Let Them Theory", "Mel Robbins"),
    (48, "The Wraith's Haunt", "Hugo Huesca"),
    (49, "Unbound", "Nic G. D. Orr"),
    (50, "Traveler's Gate", "Will Wight"),
]

# Mark duplicates with their parent
DUP_MAP = {
    10: 3,   # Primul Hunter -> The Primal Hunter
    51: 43,  # Alex Maher -> The Hedge Wizard
    52: 5,   # J.M. Clarke -> The Mark of the Fool
    53: 38,  # Ryan Rimmel -> Noobtown
    54: 15,  # A.F. Kay -> All the Skills (actually Shade's First Rule)
}

print(f"Will look up {len(SERIES)} series, {len(DUP_MAP)} duplicates to mirror")
print(f"Total: {len(SERIES) + len(DUP_MAP)}")
