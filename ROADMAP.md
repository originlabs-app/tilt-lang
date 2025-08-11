# TILT Language — Roadmap (v0.1 → v0.2)

## Overview

Goal: ship a credible, minimal, open-source language with clear docs, working examples, and a lightweight toolchain. Keep the grammar simple and the path to a parser/runtime realistic.

Timeframe: ~12 weeks in 4 phases. Adjust pragmatically as we learn.

Current status:
- Legal and repo basics in place (LICENSE, NOTICE.md, TRADEMARK.md, README, CI)
- Docs skeleton present (docs/ast.md, docs/runtime-arch.md, docs/benchmark.md)
- Examples available under `exemples/`
- CI runs lint and optional tests

---

## Phase 1 — Repo Hygiene + Syntax Decision (Weeks 1–2)

- Decide MVP syntax path: Align examples (A) vs Extend EBNF (B)
- If A (recommended): refactor `exemples/*.tilt` to MVP
  - Replace `?:`, `or`, named args, `on click`/`on submit`, `when` in UI
  - Add a script to verify MVP conformance (grep-based for now)
- If B: update `spec/grammar.ebnf`, whitepaper, and examples to match
- Make CI parse-check examples once the parser exists; keep optional until then
- Clean README sections and fix example links (done)

Deliverables:
- Issue and decision recorded; corresponding PR merged
- CI stays green on push

---

## Phase 2 — Grammar Freeze + Lexer/Parser + Formatter (Weeks 3–6)

- Freeze EBNF for v0.1 (post A/B decision)
- Implement lexer with deterministic tokens and clear errors
- Implement parser that builds the AST structures documented in docs/ast.md
- Implement a minimal `tilt fmt` (canonical whitespace and attribute style)
- Add targeted unit tests (no need for full coverage yet)

Deliverables:
- `tilt parse` and `tilt fmt` usable on `exemples/*.tilt`
- CI job to run parsing/formatting check on examples

---

## Phase 3 — Minimal Runtime/Interpreter Prototype (Weeks 7–9)

- Implement a tiny interpreter for a subset needed by examples
  - Routing stub: register `route` and call functions
  - DB stub: in-memory or SQLite with a tiny wrapper
  - UI SSR placeholder: render minimal markup for `ui.page` trees
- Expose `tilt serve` for local dev loop; hot reload optional

Deliverables:
- `tilt serve exemples/todo.tilt` serves a minimal working app
- One end-to-end example verified

---

## Phase 4 — Bench Harness + Docs (Weeks 10–12)

- Ship a reproducible benchmark skeleton (`bench/`, `requirements-bench.txt`)
- Add 1–2 sample tasks under `tasks/` and a basic runner/report
- Expand docs: Quickstart, CLI reference, and update runtime architecture

Deliverables:
- Public, reproducible benchmark skeleton
- Docs sufficient for early contributors to succeed

---

## Success Metrics

- Parser/formatter handle all examples deterministically
- One example app serves end-to-end via CLI
- 10+ community stars and first external issue/PR
- CI green on main for formatting and example parsing

---

## Risks & Mitigations

- Scope creep: Keep MVP surface small; defer ergonomics
- Parser complexity: Favor explicit grammar; add tests per construct
- Runtime effort: Start with stubs; expand only for examples
- Adoption: Publish clear docs and a simple demo; iterate in public

---

## Immediate Next Actions

1. Push current repo state to GitHub (main)
2. Open “MVP syntax — Align examples (A) vs extend EBNF (B)” discussion
3. Implement Option A refactor PR (or B spec update) based on decision

—

Last updated: 2025-08-08
Owner: Pierre Beunardeau (Origin Labs)
Contact: tilt@originlabs.app
