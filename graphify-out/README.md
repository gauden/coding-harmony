# Graph snapshot

This graph maps the generated book scaffold immediately before the 2026-08-18
parallel first-draft pass. It is useful for curriculum dependencies and planned
concept progression; it does not claim to reflect prose added later in the same
session.

The build contains 325 nodes and 270 edges across 72 labelled communities.
Graph diagnostics reported five dangling-endpoint edges, with no missing
endpoints or collapsed edges. See `GRAPH_REPORT.md` for the audit report and
`graph.html` for the interactive view.

The report's semantic token counters are zero because the coordinating runtime
did not expose subagent usage numbers to the graph build. Zero means unavailable
here; it is not a claim that semantic extraction consumed no tokens.
