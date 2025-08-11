# Contributing to TILT

Thanks for your interest! This guide covers the environment, rules, and contribution flow.

## Prerequisites
- Python 3.11+
- SQLite3

## Dev Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt || true
```

## Lint & Tests
```bash
ruff . || true
black --check . || true
pytest -q || true
```

## Rules
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`, ...)
- Branches: `feature/<slug>`, `fix/<slug>`
- PRs: clear description + checklist + docs updated
- Logs: prefer structured JSON logs

## PR Process
1. Fork + branch
2. Code + tests
3. Lint/CI green
4. Open PR and link issues

## CLA
Signing `CLA.md` is required on the first PR.

## v0.1 Priorities
- Runtime (lexer, parser, interpreter)
- Minimal stdlib (`http`, `db`, `ui`, `auth`, `validate`, `policy`)
- `tilt fmt`
- Benchmarks (`docs/benchmark.md`)
