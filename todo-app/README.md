# Python Todo App

A lightweight todo application built entirely with Python's standard library.

It includes both a command-line interface and a browser-based UI, with tasks
persisted locally in tasks.json. No external Python packages or frameworks
are required.

## Usage

```bash
python3 todo.py add "buy milk"     # Added task 1: buy milk
python3 todo.py list               # [ ] 1: buy milk
python3 todo.py done 1             # Done: buy milk
python3 todo.py delete 1           # Deleted task 1: buy milk
```

`list` output uses `[x]` for done tasks and `[ ]` for open ones.

## Web UI

See the same tasks in a browser:

```bash
python3 web.py                 # serves http://127.0.0.1:8000/ and opens a browser
python3 web.py --port 8080     # pick another port
python3 web.py --no-open       # don't launch a browser
```

`web.py` is standard library only (no Flask, no dependencies) and reads/writes the
same `tasks.json` as the CLI, so changes show up in both places.

The page is styled after the provided design (`UI design of a todo list app(2).jpeg`):
greeting header with a live date, search field, a "Today's tasks" card with a
completion ring, colored task tags with times, an add bar, and a tab bar. Tasks are
split into **Pending** and **Completed** sections with counts, and check-offs move
between them.

Two styling layers sit on top of that design:

- **Luxury typography background** — oversized serif words (*Élégance*, *LUXURY*,
  *Timeless*, *SOPHISTICATION*, *Maison*, *L'art de vivre*) watermark the page behind
  the app, filled and outlined at low opacity. They use Playfair Display (loaded from
  Google Fonts) and fall back to system serifs (Didot/Bodoni/Georgia) when offline,
  so the page still works with no network.
- **Neumorphic controls** — every button is raised out of its surface with paired
  light/dark shadows and presses in on `:active`: the view pill, the in-app theme
  button, search, add, task checkboxes (well when unchecked, raised coral when done),
  task menus, the add bar, and the tab bar. Inputs are inset wells. Shadows and accent
  colors re-derive from CSS variables, so both themes stay consistent.

Use the **Phone view** button (top right) — or open `/#phone` directly — to see the
same UI inside a phone frame, centered on the page. In **Desktop view** (the default)
and on a real phone the app fills the whole viewport: full-bleed surface with the
typography watermark behind a centered content column, no frame.

Every button does something:

- **Profile avatar** (or clicking the greeting) opens an inline field to set your
  name — `Hey, <name>` — saved to `localStorage`. The same field lives in Settings.
- **Tab bar** — *Home* (full dashboard), *Lists* (list only, no Today card),
  *Calendar* (month grid with today highlighted, coral dots on days that have tasks,
  prev/next navigation, and an agenda that shows the tasks dated for the selected
  day plus an "No date" group for the rest), *Settings* (name, dark/light, phone/
  desktop view, and *Clear completed (n)*). The center button opens the add form.
  Tabs deep-link too: `/#lists`, `/#calendar`, `/#settings`.
- Search, add, check off, `···` delete, theme and view toggles all keep working.
The **Light/Dark mode** button lives inside the todo list itself, in the header next
to the profile avatar (so it stays reachable on phones, where the corner pill is
hidden). It switches themes and remembers the choice in `localStorage`; `/#light` or
`/#dark` force a theme from the URL (these combine, e.g. `/#phone#light`).

The add form takes an optional time (e.g. `8:00AM - 8:30AM`), stored as a `time`
field on the task, an optional date (stored as `date`, ISO `YYYY-MM-DD` — invalid
dates are rejected server-side), and an optional **note** section for writing a
random note (stored as `note`, capped at 500 chars). Tasks without a date show just
the time, and without either show `Anytime`. Task colors are derived from the task
id, so no extra field is needed.

On the task card the date shows as `Today` / `Tomorrow` / `Wed 8 Oct` before the
time, and the note appears under the title with a coral rule — clamped to three
lines, click it to expand. **Cancel** in the add form discards everything you
typed and closes the form; **Add** submits it.

Clicking the **time bar** opens a scrollable wheel — **Date** (the next 28 days:
Today, Tomorrow, then weekday + day), hour, minute (5-minute steps) and AM/PM
columns, all with snap-to-selection and a highlighted centre band. Scroll a column
or tap a value and the matching field is filled in (`2026-10-12`, `8:00AM`); **Set**
closes the wheel, and clicking elsewhere or pressing Esc dismisses it. The date
field is also a native date input, so either way works and both stay in sync with
the wheel. The time field stays a normal editable text box, so you can still type a
range like `8:00AM - 8:30AM` — the wheel only takes over the value when the field
holds a single time, so reopening it never clobbers what you typed.

Endpoints, if you want to script against them:

| Method | Path | Body | Result |
| --- | --- | --- | --- |
| `GET` | `/` | — | the HTML page (current tasks embedded) |
| `GET` | `/api/tasks` | — | JSON task list |
| `POST` | `/api/tasks` | `{"title": "...", "time": "...", "date": "YYYY-MM-DD", "note": "..."}` | add a task (201); all but `title` optional |
| `POST` | `/api/tasks/<id>/toggle` | — | flip done state |
| `POST` | `/api/tasks/<id>/delete` | — | delete the task |

Errors come back as `{"error": "..."}` with a 4xx/5xx status — the same messages
the CLI prints.

## Behavior notes

- **Missing `tasks.json`** — treated as an empty list; no error.
- **Corrupt `tasks.json`** — prints `error: Could not read tasks.json: ...` and exits with status 1 instead of a traceback.
- **Unknown or non-numeric IDs** — `done`/`delete` print `error: Task with id N not found.` (or `Invalid ID ...`) and exit with status 1 without modifying the file.
- IDs are never reused: the next ID is always `max(existing) + 1`.
