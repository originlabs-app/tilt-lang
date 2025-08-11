#+ Open Issues

## Decision: MVP syntax — Align examples (A) or extend EBNF (B)
Tracking issue to decide whether to:
- A) Refactor examples to strictly follow MVP grammar, or
- B) Extend the EBNF to match current examples (ternary `?:`, `or` coalescence, UI `when`, named args).

**Status:** Option A selected — examples will be aligned with the current grammar.

See issue template: .github/ISSUE_TEMPLATE/mvp-syntax-decision.md

Rationale: Keep repo pushable now; finalize direction before enabling strict CI parsing.

