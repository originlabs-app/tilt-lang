---
name: "Decision: MVP grammar alignment (A) vs EBNF extension (B)"
about: Decide whether to refactor examples to MVP grammar or extend the EBNF to match examples
title: "Decision: MVP syntax — Align examples (A) or extend EBNF (B)"
labels: ["discussion", "design", "grammar"]
assignees: []
---

## Context
Examples currently use constructs outside the strict MVP grammar (e.g., UI `when`, ternary `?:`, `or` coalescence, named args like `url:`). We must either refactor examples to MVP or extend the EBNF to include these constructs.

## Options
### A) Align examples to MVP
- Replace `?:` with explicit `if/else`
- Replace `or` coalescence with explicit `if`/defaults
- Convert named args to positional
- Replace UI `when` with standard `if`
- Normalize UI events to `on_click=` / `on_submit=`

Pros: Keeps grammar minimal; easier for parsers/type-checkers; consistent with "one way to do things".

Cons: Refactor examples; slightly more verbose in UI logic.

### B) Extend the EBNF
- Add ternary `?:`
- Add `or` as coalescing operator
- Allow `when` in UI declarations
- Keep named arguments in stdlib calls

Pros: Matches current examples; possibly more ergonomic.

Cons: Increases grammar surface; higher risk for ambiguity; more work for parser/typechecker; weakens MVP simplicity.

## Impacted Files
- exemples/*.tilt (multiple locations)
- spec/grammar.ebnf (keywords and productions)
- spec/whitepaper.md and spec/errors.md (docs alignment)

## Acceptance Criteria
- Decision recorded (A or B)
- If A: PR refactors all examples to MVP and CI passes
- If B: PR updates EBNF/spec, updates parser roadmap, and examples validated

## Additional Notes
Maintainers suggested to push current changes and track this decision as an issue.

