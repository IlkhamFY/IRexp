# Follow-ups left out of the Sci Data hard-error pass

These items were reviewed and are **not** in `scientific_data.tex`. Do not treat this note as manuscript text.

- Fig. 2B arithmetic (+13) still needs a recompute against the locked figure.
- Duplicate-integer band counts still need a corpus re-run before any manuscript number is added or changed.
- Listing 1 was not replaced. No existing SI or example file in this repo carries a different real row with `ir_shared_in_paper` / `ir_table_flatten_suspect` plus licence fields. The published example still sets `id` to an InChIKey for that resolved row. The manuscript states that `id` is a unique stable internal record identifier, that this listing equality is a convenience for that row, and that InChIKey (`inchikey`) is not unique (57,646 structure-linked records; 54,985 InChIKeys).
- `train_no_bench` was not rebuilt.
- A second human rater was not added.
- A new recall human set was not collected.
