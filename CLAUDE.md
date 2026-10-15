# Audiobook Tracker — rules and context

Achyut calls this the **"novel tracker"**. Same thing. It is a single-page,
local-only web app that tracks audiobook series, which books are downloaded
and which are read. Repo: `~/workspace/clawd/Audiobook-Tracker`
(symlinked as `~/.openclaw/workspace/audiobook-tracker`), remote
`rastogiachyut/audiobook-tracker` on GitHub, branch `master`.

## Files

| File | Role |
|---|---|
| `data.json` | Source of truth. Edit this. 2-space indent, no trailing newline. |
| `source-data.js` | **Generated** from `data.json`. Never hand-edit. Regenerate after every data change (see below). |
| `index.html` | The whole app: CSS, markup and JS. Loads `source-data.js`, keeps user edits in `localStorage`. |
| `server.py` | Optional save server on port 8420 (`/api/save` writes both data files). Usually not running. |
| `fetch_books.py`, `populate_books.py`, `apply_books.py`, `raw_books.json` | One-off enrichment scripts from the first import. Historical, not part of the workflow. |

## Data model

Series: `title, author, booksRead (legacy, ignore), status, myRating (S–F),
myReview, goodreads{rating,description,url}, books[]`.
Book: `title, releaseDate (year string), rating, url, doneReading,
downloaded, description`.

Status values: `reading`, `planned`, `complete`, `waiting`, `lost-interest`,
`dropped`. New series go in as `planned`.

## Invariants (enforced in `index.html`, keep data consistent with them)

1. **A read book is always downloaded.** `doneReading` ⇒ `downloaded`.
   Un-downloading a read book un-reads it.
2. **Complete means every book read.** A series with any unread book is not
   `complete`. Do not auto-promote fully-read series to complete: many are
   ongoing (All the Skills, Noobtown…). The UI asks via a confirm when the
   last book is ticked. A series with an empty `books` list keeps whatever
   status it has (System Apocalypse).
3. Each series row shows three counts: Books, Read, DL.

## Sync workflow: new downloads → tracker

Downloads land in `~/Downloads/Audio Novels/<series or book folder>/…`.
When asked to "mark downloads", "sync downloads" or similar:

1. List the folder. One audio file (`.m4b`/`.mp3`) or one folder of numbered
   `.mp3`s = one book. Omnibus files cover several books.
2. Read tags with `ffprobe -show_entries format_tags=title,album,artist,date,description,comment`.
   **Trust the file tags over existing tracker data** for author and titles;
   several entries were auto-populated wrong in the past (Bog Standard
   Isekai, Hell Difficulty Tutorial, Syl, Unbound were all fixed this way).
3. Existing series: set `downloaded: true` on the matching book; fill empty
   `description`/`releaseDate` from tags. Add missing later volumes.
4. Unknown series: create it (`status: planned`), list the full series if it
   is known, flag only the downloaded ones. Pull descriptions from tags,
   strip HTML, cut to ~220 chars.
5. Nonfiction single books get a series entry with one book (precedent:
   The Let Them Theory, The Mountain Is You).
6. Report what was marked, what was created and anything unconfirmed
   (e.g. a book title taken from a web listing).

## After any change to `data.json`

```bash
python3 -c "import json,pathlib; d=json.load(open('data.json')); pathlib.Path('source-data.js').write_text('// Auto-generated — DO NOT EDIT\nwindow.SOURCE_DATA = '+json.dumps(d,ensure_ascii=False)+';\n')"
```
Then **bump `DATA_VERSION`** in `index.html`, otherwise browsers keep the
stale copy in `localStorage`. Then commit all three files together.

## Git

- Commit after each logical change with a descriptive message.
- **Do not push unless Achyut asks.** Say how many commits are ahead.

## Verifying UI changes

`new Function(script)` parse check, then headless render:
```bash
google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir=/tmp/x --virtual-time-budget=3000 --screenshot=/tmp/shot.png --window-size=1400,900 file://$PWD/index.html
```

## Known quirks / open items

- `Adventures on Brad` has no status set (UI treats it as reading).
- Ultimate Level 1 book 1 (Shattered Dreams) and 11 (Divine Conflict) are not
  downloaded; the book-11 title came from a web listing, unconfirmed.
- A Thousand Li volumes 4–7 follow series numbering, not publication order.
- Seven fully-read series sit at `reading` on purpose (ongoing or undecided).
