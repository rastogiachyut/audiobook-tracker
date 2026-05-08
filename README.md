# 📚 Audiobook Tracker

A lightweight, self-contained web app to track your audiobook series — ratings, reviews, and reading progress per book.

## Features

- **55 series** with **331 individual books** pre-loaded (LitRPG, Progression Fantasy, and more)
- ✅ Checkbox per book to track reading progress
- ⭐ My rating system (S through F)
- 📊 Goodreads/Amazon ratings auto-populated
- 🔍 Search, filter by status and rating
- 📥 Export/Import JSON data
- 🔒 Fully local — no server needed, data persists in localStorage
- 📱 Responsive design

## Usage

1. Open `index.html` in any browser
2. Click any series row to expand and see all books
3. Click checkboxes to mark books as read
4. Click book titles to see descriptions
5. Use Edit to add your ratings and reviews

## Data Format

Each series entry in `data.json`:

```json
{
  "title": "Cradle",
  "author": "Will Wight",
  "booksRead": 12,
  "status": "complete",
  "myRating": null,
  "myReview": null,
  "goodreads": {
    "rating": "4.14",
    "description": null,
    "url": "https://www.goodreads.com/book/show/30558257-unsouled"
  },
  "books": [
    {
      "title": "Unsouled",
      "releaseDate": null,
      "rating": "4.4",
      "url": null,
      "doneReading": false
    }
  ]
}
```

## License

MIT
