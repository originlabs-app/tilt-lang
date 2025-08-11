# TILT — Error Codes (v0.1-alpha)

TILT standardise des erreurs **courtes, numérotées et stables** pour faciliter
la lecture humaine, l'automatisation et l'auto-fix par LLM.

Chaque erreur suit un format JSON :

```json
{
  "code": "E101",
  "message": "Type mismatch: expected int, got text",
  "hint": "Cast input as { qty:int } or update schema.",
  "span": { "file": "examples/crm.tilt", "line": 42, "col": 15 },
  "details": { "expected": "int", "found": "text", "path": "body.qty" }
}
```

## Index des familles

* **E0xx — Lexing / Parsing**

  * E001: Unexpected token
  * E002: Unterminated string literal
  * E003: Invalid number literal
  * E004: Unknown keyword or reserved identifier
  * E005: Duplicate declaration (symbol redefined)
  * E006: Unexpected end-of-file (missing `}` or `)`)
  * E007: Invalid UI attribute syntax
  * E008: Invalid route declaration
  * E009: Invalid enum/ref declaration

* **E1xx — Typage / Validation statique**

  * E100: Unknown identifier
  * E101: Type mismatch (expected X, got Y)
  * E102: Invalid call arguments (arity or types)
  * E103: Incompatible assignment
  * E104: Invalid cast shape (`as { ... }`)
  * E105: Field not found on type
  * E106: Non-boolean condition in `if`/`match`
  * E107: Return type mismatch
  * E108: Unreachable or fallthrough not allowed
  * E109: Enum value not allowed
  * E110: Foreign ref invalid (unknown table)
  * E111: Duplicate field name
  * E112: Constant requires literal value

* **E2xx — Exécution / Runtime**

  * E200: Null/Option value where non-optional required
  * E201: Division by zero
  * E202: Pattern match failed
  * E203: Index out of bounds
  * E204: Timeout exceeded
  * E205: Serialization error (JSON)
  * E206: Permission denied (guard failed)
  * E207: Not found
  * E208: Rate limit exceeded
  * E209: Resource unavailable (pool exhausted)

* **E3xx — Modules système (HTTP/DB/UI)**

  * E300: HTTP request failed
  * E301: HTTP invalid status
  * E302: CORS blocked
  * E310: DB connection failed
  * E311: DB constraint violation (unique/foreign key)
  * E312: DB query error / syntax
  * E313: DB migration missing
  * E320: UI render error (invalid node)
  * E321: UI unsafe HTML rejected (CSP)
  * E322: UI component props mismatch

* **E4xx — Auth / Validation**

  * E400: Authentication required
  * E401: Invalid credentials
  * E402: Session expired
  * E403: CSRF validation failed
  * E404: Token invalid or revoked
  * E410: Validation failed (see `details.errors`)
  * E411: Missing required field
  * E412: Invalid email/format

* **E5xx — I/O / Sécurité / Sandbox**

  * E500: File access denied
  * E501: Network access denied (not allowlisted)
  * E502: Secret not found
  * E503: Quota exceeded (CPU/Mem/DB)
  * E504: Sandbox violation
  * E505: Unsupported operation in this environment

* **E9xx — Interne**

  * E900: Internal error
  * E901: Not implemented
  * E902: Invariant violated
  * E903: Panic guard

---

## Détails par catégorie

### E0xx — Parsing

**E001 Unexpected token**
*Message*: `Unexpected token '}' (expected identifier)`
*Hint*: Check for a stray `}` or missing comma.
*Span*: precise location.

**E006 Unexpected end-of-file**
*Message*: `EOF while parsing ui.page block`
*Hint*: Close the `{ ... }` block.

### E1xx — Typage

**E101 Type mismatch**
*Details*: `{ "expected": "int", "found": "text", "path": "body.qty" }`
*Hint*: `let b = http.request.body.json as { qty:int }`

**E104 Invalid cast shape**
*Message*: `Cast as { name:text, age:int? } incompatible with value`
*Hint*: Ensure all required fields are present.

**E110 Foreign ref invalid**
*Message*: `ref("contacts") points to unknown table`
*Hint*: Declare `db.table("contacts", ...)` first.

### E2xx — Runtime

**E206 Permission denied**
*Message*: `Guard 'require_auth' failed`
*Hint*: Attach correct guards: `route POST "/x" use [require_auth] -> ...`

**E208 Rate limit exceeded**
*Details*: `{ "limit": "100 r/min", "scope": "ip:/api/x" }`

### E3xx — HTTP/DB/UI

**E311 DB constraint violation**
*Details*: `{ "constraint": "unique_email" }`

**E320 UI render error**
*Message*: `Unknown UI node 'grdi' (did you mean 'grid'?)`

### E4xx — Auth/Validation

**E410 Validation failed**
*Details*:

```json
{
  "errors": [
    {"path": "email", "rule": "email", "message": "Invalid email"},
    {"path": "name", "rule": "min", "expected": 2}
  ]
}
```

### E5xx — I/O/Sandbox

**E501 Network access denied**
*Hint*: Add domain to allowlist: `http.allow("api.stripe.com")`.

### E9xx — Interne

**E901 Not implemented**
*Message*: `Feature 'ui.chart' not implemented in this build`

---

## Recommandations d'UX erreur

* **Courtes & actionnables** : message ≤ 100 chars, `hint` concret.
* **Stables** : les codes ne changent pas entre versions mineures.
* **Corrélables** : inclure `span` (file/line/col) pour IDE & LLM.
* **Sécurité** : ne pas exposer de secrets dans `message`/`details`.

---

## Exemples d'erreurs générées par stdlib

```json
{
  "code": "E410",
  "message": "Validation failed",
  "hint": "Fix invalid fields and retry.",
  "span": {"file": "examples/marketplace.tilt", "line": 73, "col": 9},
  "details": {
    "errors": [
      {"path": "price_cents", "rule": "int", "message": "Expected integer"},
      {"path": "email", "rule": "email", "message": "Invalid email"}
    ]
  }
}
```

```json
{
  "code": "E320",
  "message": "UI render error: unknown node 'crad'",
  "hint": "Did you mean 'card'?",
  "span": {"file": "examples/crm.tilt", "line": 112, "col": 7}
}
```

---

## Mapping HTTP ↔︎ Codes TILT (serveur)

| HTTP Status | Code TILT | Usage                            |
| ----------- | --------- | -------------------------------- |
| 400         | E410      | Validation failed                |
| 401         | E400      | Authentication required          |
| 403         | E206      | Permission denied (guard/policy) |
| 404         | E207      | Not found                        |
| 409         | E311      | DB constraint violation          |
| 429         | E208      | Rate limit exceeded              |
| 500         | E900      | Internal error                   |

---

## Conventions d'émission

* Les routes API renvoient `{"ok":false, "error":{...}}` ou `{"ok":true, ...}`.
* Le runtime sérialise les exceptions en payload conforme (`code`, `message`, `span`, `details`).
* Les erreurs UI sont également loguées côté serveur avec un `request_id` pour corrélation.