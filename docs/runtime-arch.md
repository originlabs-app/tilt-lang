# TILT Runtime Architecture (v0.1)

Ce document décrit l'architecture d'exécution du runtime TILT v0.1.

## Schéma général
```mermaid
flowchart LR
  A[Source .tilt] --> B[Lexer]
  B --> C[Parser]
  C --> D[AST]
  D --> E[Type Check (lite)]
  E --> F[Interpreter]
  F -->|routes| G[HTTP Server]
  F -->|queries| H[(SQLite)]
  F -->|ui tree| I[UI Renderer (SSR)]
  G <--> J[CLI Serve/Watch]
```

## Composants
- Lexer: tokens déterministes, commentaires `// /* */`.
- Parser: conforme à `spec/grammar.ebnf`, produit l'AST (voir `docs/ast.md`).
- Type check (lite): signatures `fn`, cast `as { ... }`, types primitifs.
- Interpreter: exécute fonctions/guards/routes, résout stdlib.
- Stdlib: `http`, `db` (SQLite), `ui` (SSR), `auth`, `validate`, `policy`.

## Boucle d'exécution
1. Chargement → AST
2. Enregistrement: tables, indexes, routes, UI
3. Démarrage serveur (FastAPI/Starlette) + migrations SQLite
4. Requête: guards → handler → réponse JSON/HTML

## CLI (MVP)
- `tilt serve app.tilt` — serveur + hot reload basique
- `tilt run app.tilt` — exécution utilitaire
- `tilt fmt app.tilt` — formatage canonique v0.1
- `tilt test` — placeholder (tests TILT à venir)

## Observabilité & Erreurs
- Logs JSON: `{request_id, route, duration_ms, db_queries, error?}`
- Mapping HTTP ↔ Codes TILT: voir `spec/errors.md`

## Limites v0.1
- SQLite uniquement, pas d'async utilisateur
- Pas de paramètres nommés, pas d'opérateurs `?:`/`or`
- UI SSR (hydratation minimale via actions)

