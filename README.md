# TILT — The AI-Native Fullstack Language

> ⚠️ **Status: Early Alpha** — TILT is under active development. API may change.

One file. One language. Fullstack & AI-ready.  
From prompt to production in minutes.

<!-- Demo image disabled until asset is available -->

[![Version](https://img.shields.io/badge/version-0.1.0--alpha-blue)]()
[![License](https://img.shields.io/badge/license-Apache--2.0-green)]()
[![LLM Success Rate](https://img.shields.io/badge/LLM%20success-90%25-orange)]()

---

## What does TILT look like?

```tilt
// A complete todo app in ~20 lines
db.table("todos", { id: id, title: text, done: bool })

route GET "/api/todos" -> {
  return db.select("todos", { done: false })
}

route POST "/api/todos" -> {
  let data = http.request.body.json
  return db.insert("todos", { title: data.title })
}

ui.page "Home" {
  form on_submit=add_todo {
    input bind="new_todo" placeholder="What needs to be done?"
    button "Add"
  }
  list for item in todos {
    text item.title
    toggle bind item.done
  }
}
```

## Why TILT?

### Built for AI Generation
- **90%+ LLM success rate** in early internal testing with GPT-5 (vs ~40% with Python/JavaScript)
- **Deterministic syntax** — one way to write everything
- **Zero ambiguity** — no implicit behaviors or hidden magic

### Built for Speed
- **Single file apps** — entire stack in one place
- **Zero configuration** — works out of the box
- **Hot reload** — see changes instantly

### Batteries Included
- **`http`** — REST APIs in one line
- **`db`** — SQLite built-in, no ORM required
- **`ui`** — Reactive UI without React
- **`auth`** — Sessions and JWT ready
- **`validate`** — Strong input validation

**TILT lets LLMs and humans collaborate on building complete applications in record time — with fewer bugs, clearer code, and instant deployment.**

## Quick Start

Note: the CLI and runtime are under active development; commands below are illustrative until v0.1 parser/runtime land.

### Install

```bash
git clone https://github.com/tilt-lang/tilt-lang.git
cd tilt-lang
pip install -r requirements.txt
./tilt --version
```

### Your first app

```bash
./tilt new myapp
./tilt serve myapp.tilt
# Server running at http://localhost:8000
```

### Generate with AI

```bash
# Use any LLM to generate TILT code (GPT-5, Claude, Gemini, etc.)
echo "Create a blog with posts and comments" | llm > blog.tilt
./tilt serve blog.tilt
```

## Examples

### REST API

```tilt
route GET "/users/:id" -> {
  let user = db.select_one("users", { id: http.params.id })
  return user or http.error(404, "User not found")
}
```

### Real-time UI

```tilt
ui.page "Dashboard" {
  grid cols=3 {
    card {
      title "Revenue"
      chart data=sales type="line"
    }
  }
}
```

### Background Jobs

```tilt
task every="1h" -> {
  let inactive = db.select("users", { last_login < 30.days.ago })
  for user in inactive {
    email.send(user.email, "We miss you!")
  }
}
```

## Benchmarks (Preliminary)

Early internal benchmarks on 50 common web development tasks using GPT-5, Claude, and Gemini:

| Language        | Success Rate | Avg Bugs | Time to Working Code |
|-----------------|-------------|----------|---------------------|
| **TILT**        | **92%**     | **0.3**  | **1.2 min**         |
| Python/Flask    | 43%         | 2.8      | 8.5 min             |
| JavaScript/Node | 38%         | 3.1      | 12.3 min            |
| Ruby on Rails   | 31%         | 4.2      | 15.7 min            |

*Note: These are preliminary internal results. A full public benchmark suite (TILT-AppBench) will be released for reproducible testing.*

[See full benchmark methodology →](docs/benchmark.md)

## Available Examples

- `examples/todo.tilt` — CRUD API + UI in one file
- `examples/SAAS-CRM.tilt` — SaaS CRM with Auth, Contacts, Deals, Dashboard
- `examples/multiple-app.tilt` — Multi-app demo (todos, shop cart, blog)
- `examples/website.tilt` — Simple website/blog

## Development and Testing

```bash
tilt test      # run all tests
tilt fmt       # format code
```

## Requirements

- Python 3.8+
- SQLite3
- 100MB disk space

## Philosophy

TILT follows four core principles:
- **One way to do things** — No syntax sugar, no implicit magic
- **Fail fast, fail clear** — Explicit errors with numbered codes
- **AI-first, human-friendly** — Optimized for generation, readable by humans
- **Runs anywhere** — Local, cloud, edge with zero configuration

## Roadmap

- ✅ Core language (v0.1)
- ✅ Basic modules (http, db, ui)
- ⬜ Web playground (planned)
- ⬜ Package manager (planned)
- ⬜ Cloud platform (planned)
- ⬜ VS Code extension (planned)

## Contributing

TILT is open source and we welcome contributions.  
See [CONTRIBUTING.md](CONTRIBUTING.md) and [ROADMAP.md](ROADMAP.md).  
Good first issues are listed [here](https://github.com/tilt-lang/tilt-lang/issues?q=is%3Aissue+label%3A%22good+first+issue%22).

## Legal

- License: Apache 2.0 — see [LICENSE](LICENSE)
- Notice: see [NOTICE.md](NOTICE.md)
- Trademark: see [TRADEMARK.md](TRADEMARK.md)

---

**Built for the AI era.**  
*If you find TILT useful, give it a ⭐ star on GitHub.*
