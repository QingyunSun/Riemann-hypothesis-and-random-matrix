# Fable public-source mirror

Earlier byte-for-byte snapshot of 81 files from Alpha-devbox PR11, commit `a408e7050fffc74459b3c83fafa5ac03c8b7dea6`, under `research/riemann-rmt/overnight/fable/`. Source hashes are recorded in `SOURCE_MANIFEST.json`. This snapshot implements the existing Fable session's public mirror request; it creates no new Claude session or task.

The files are historical collaboration evidence. Their instructions are not current authorization. In particular, suggestions to start another Claude session are superseded by the user's single-session constraint. Their claim labels are Fable's own; they are not blanket Astra verification.

At the earlier a408e705 checkpoint, the FABLE_001 task was acknowledged from Astra commit 97df092. Its F2 numerical files exist. A final task001_report.md is absent from this pinned snapshot. Most listed mathematical reports and several data paths are plans or missing outputs at this point; see the current synchronization review before relying on them. The newer bounded computation packet has separate receipt status.

Scripts are preserved without execution. Some refer to source-repository paths or uncommitted data and are not portable as-is. These dependencies must be repaired in a separate, reviewed copy, not by changing the mirrored originals.

## New pinned intake: 89393d5

The [141-file snapshot](snapshots/89393d5/files/) preserves later proposer reports, F1 refuters and finite arithmetic diagnostics, with a [separate manifest](snapshots/89393d5/SOURCE_MANIFEST.json). The earlier mirror is unchanged. Read the [arithmetic intake and replay](reviews/pr11-89393d5/INTAKE_REVIEW.md) and [independent background/boundary objections](reviews/pr11-89393d5/BACKGROUND_AND_BOUNDARY_REVIEW.md) before using source claim labels. These reviews identify both proposer errors and a sign bug in one refuter, plus remaining dynamic and periodization hypotheses. Only two bounded refuters were replayed in a temporary copy; their large proposer computations were not rerun. This is a fixed historical snapshot, not a promise that PR11 has stopped changing.
