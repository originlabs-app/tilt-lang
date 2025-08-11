# Contribuer à TILT

Merci pour votre intérêt ! Ce guide couvre l'environnement, les règles et le flux de contribution.

## Prérequis
- Python 3.11+
- SQLite3

## Installation (dev)
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

## Règles
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`, ...)
- Branches: `feature/<slug>`, `fix/<slug>`
- PR: description claire + checklist + docs mises à jour
- Logs: privilégier logs JSON structurés

## Processus PR
1. Fork + branche
2. Code + tests
3. Lint/CI verts
4. Ouvrir PR et lier aux issues

## CLA
Signer le `CLA.md` est requis lors de la première PR.

## Priorités v0.1
- Runtime (lexer, parser, interpréteur)
- Stdlib minimale (`http`, `db`, `ui`, `auth`, `validate`, `policy`)
- `tilt fmt`
- Benchmarks (`docs/benchmark.md`)
