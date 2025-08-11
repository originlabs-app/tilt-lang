# TILT Runtime Architecture (v0.1)

This document describes the runtime architecture for TILT v0.1.

## High-level Diagram
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

## Components
- Lexer: deterministic tokens, `// /* */` comments.
- Parser: follows `spec/grammar.ebnf`, produces AST (see `docs/ast.md`).
- Type check (lite): `fn` signatures, cast `as { ... }`, primitive types.
- Interpreter: executes functions/guards/routes, resolves stdlib.
- Stdlib: `http`, `db` (SQLite), `ui` (SSR), `auth`, `validate`, `policy`.

## Execution Loop
1. Load → AST
2. Register: tables, indexes, routes, UI
3. Start server (FastAPI/Starlette) + SQLite migrations
4. Request: guards → handler → JSON/HTML response

## CLI (MVP)
- `tilt serve app.tilt` — dev server + basic hot reload
- `tilt run app.tilt` — utility execution
- `tilt fmt app.tilt` — canonical formatting v0.1
- `tilt test` — placeholder (TILT tests TBD)

## Observability & Errors
- JSON logs: `{request_id, route, duration_ms, db_queries, error?}`
- HTTP ↔ TILT error codes: see `spec/errors.md`

## Limitations v0.1
- SQLite only, no user async
- No named parameters, no `?:`/`or` operators
- UI SSR (minimal hydration via actions)
