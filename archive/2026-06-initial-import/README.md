# Archive: initial import working files (2026-06-17)

Artifacts from the one-off session that built the tracker's first dataset:

- `novels_page.html` — HTML wrapper embedding the original novel-list photo
- `novels_full/enhanced/final/view/image.png`, `novels_hq/query/small.jpg` — the
  source photo and processing passes (upscale, contrast, invert)
- `novels_row_*.png`, `novels_col*.png`, `novels_reg_*.png`,
  `novels_hdr_*.png`, `novels_top_*/bot-*/mid-*.png` — crops of individual
  rows/columns/regions used for manual transcription

The transcription result lives in `data.json` at the repo root. These files are
kept for provenance only — nothing here is used by the app.
