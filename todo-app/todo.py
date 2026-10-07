#!/usr/bin/env python3
"""A small command-line todo app backed by a local JSON file."""

import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Return the task list, tolerating a missing file.

    Raises ValueError if the file exists but cannot be parsed.
    """
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError(f"Could not read {DATA_FILE.name}: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError(f"{DATA_FILE.name} has an unexpected format (expected a list).")
    return data


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2) + "\n", encoding="utf-8")


def parse_id(raw):
    """Convert a CLI id argument to a positive int, or exit gracefully."""
    try:
        task_id = int(raw)
    except ValueError:
        fail(f"Invalid ID {raw!r}: expected a number.")
    if task_id < 1:
        fail(f"Invalid ID {raw!r}: expected a positive number.")
    return task_id


def find_task(tasks, task_id):
    """Return the task with the given id, or exit gracefully if absent."""
    for task in tasks:
        if task.get("id") == task_id:
            return task
    fail(f"Task with id {task_id} not found.")


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def cmd_add(args):
    tasks = load_tasks()
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": args.text, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task {next_id}: {args.text}")


def cmd_list(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks. Add one with: todo.py add \"...\"")
        return
    for task in tasks:
        marker = "x" if task.get("done") else " "
        print(f"[{marker}] {task['id']}: {task['title']}")


def cmd_done(args):
    task_id = parse_id(args.id)
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task.get("done"):
        print(f"Task {task_id} is already done: {task['title']}")
        return
    task["done"] = True
    save_tasks(tasks)
    print(f"Done: {task['title']}")


def cmd_delete(args):
    task_id = parse_id(args.id)
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Deleted task {task_id}: {task['title']}")


def build_parser():
    parser = argparse.ArgumentParser(prog="todo.py", description="A small local todo app.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("text", help="task description")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list all tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("id", help="task id")
    p_done.set_defaults(func=cmd_done)

    p_delete = sub.add_parser("delete", help="delete a task")
    p_delete.add_argument("id", help="task id")
    p_delete.set_defaults(func=cmd_delete)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except ValueError as exc:
        fail(str(exc))
    except OSError as exc:
        fail(f"Could not write {DATA_FILE.name}: {exc}")


if __name__ == "__main__":
    main()
