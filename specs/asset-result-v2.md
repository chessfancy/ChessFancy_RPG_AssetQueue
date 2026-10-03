# Asset Result v2

`assets/<job-id>/asset.json` records worker output provenance and QC. Worker completion and production approval are separate concepts.

Recommended fields:

```json
{
  "request_id": "...",
  "protocol_version": "2",
  "worker": "muse",
  "generator": "muse",
  "reference_mode": "external_reference_first",
  "canonical_reference": "references/.../canonical.png",
  "request_blob_sha": "...",
  "request_commit_sha": "...",
  "generation_mode": "single_contact_sheet",
  "requested_frames": 8,
  "detected_initial_frames": 8,
  "repaired_frames": [],
  "repair_passes_used": 0,
  "generation_layout": {"cols": 4, "rows": 2},
  "raw_generation": {
    "width": 2240,
    "height": 1120,
    "sha256": "...",
    "snapshot_id": "..."
  },
  "master": {
    "sheet": "master_sheet_rgba.png",
    "cell_width": 607,
    "cell_height": 592,
    "extra_padding_px": 15
  },
  "runtime_cell_size": {"width": 128, "height": 128},
  "background_cleanup": "white_key_if_needed",
  "files": ["master_sheet_rgba.png", "preview.gif", "asset.json"],
  "qc": {
    "frame_count": "pass",
    "identity": "pass",
    "choreography": "pass",
    "crop": "pass",
    "bleed": "pass",
    "background": "pass"
  },
  "created_at": "..."
}
```

Rules:

- Preserve actual values; omit unknown optional values instead of inventing them.
- `repair_passes_used` must never exceed 2.
- `files` lists committed deliverables relative to the bundle directory.
- Raw generation may remain uncommitted if large, but SHA256/snapshot metadata should be retained when available.
- `qc` represents worker-side candidate QC only.
- `status: done` plus all-pass worker QC still does not equal production approval.
- Hermes records runtime/technical QC and promotion separately.
