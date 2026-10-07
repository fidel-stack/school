#!/usr/bin/env python3
"""A small web UI for todo.py, using only the standard library."""

import argparse
import datetime
import json
import re
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

from todo import DATA_FILE, fail, load_tasks, save_tasks

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>todo.py</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<style>
  :root {
    color-scheme: dark;
    --bg: #1d1922;
    --screen1: #312c3c;
    --screen2: #292433;
    --card: #3a3446;
    --card-dark: #221e2c;
    --card-hover: #443d51;
    --coral: #ef6d6d;
    --purple: #b06ae8;
    --text: #f4f1f8;
    --muted: #9a93a6;
    --faint: #6f6879;
    --title: #e8e4ee;
    --screen-shadow: 0 30px 70px rgba(0,0,0,.5);
    --serif: "Playfair Display", "Didot", "Bodoni MT", "Cormorant Garamond", Georgia, "Times New Roman", serif;
    --typo-fill: rgba(244,241,248,.05);
    --typo-stroke: rgba(244,241,248,.12);
    --neu-bg: #2e2939;
    --neu-shadow: rgba(0,0,0,.6);
    --neu-hi: rgba(255,255,255,.055);
    --neu-out: 6px 6px 14px var(--neu-shadow), -6px -6px 14px var(--neu-hi);
    --neu-out-sm: 3px 3px 7px var(--neu-shadow), -3px -3px 7px var(--neu-hi);
    --neu-in: inset 5px 5px 11px var(--neu-shadow), inset -5px -5px 11px var(--neu-hi);
    --neu-in-sm: inset 3px 3px 6px var(--neu-shadow), inset -3px -3px 6px var(--neu-hi);
    --neu-accent-shadow: rgba(120,35,35,.55);
    --neu-accent-hi: rgba(255,165,165,.22);
    --neu-accent-out: 6px 6px 14px var(--neu-accent-shadow), -6px -6px 14px var(--neu-accent-hi);
    --neu-accent-out-sm: 3px 3px 7px var(--neu-accent-shadow), -3px -3px 7px var(--neu-accent-hi);
    --neu-accent-in: inset 4px 4px 9px var(--neu-accent-shadow), inset -4px -4px 9px var(--neu-accent-hi);
    --ring-track: #4a4356;
    --ring-fg: #f4f1f8;
    --tabbar-bg: rgba(0,0,0,.14);
    --hairline: rgba(255,255,255,.06);
    --menu-border: rgba(255,255,255,.14);
    --error-bg: rgba(239,109,109,.16);
    --error-fg: #ff9b9b;
    --home-ind: rgba(255,255,255,.4);
    --bezel: #0c0a0f;
    --bezel-edge: #2b2833;
    --hint: #6f6879;
    --radius: 12px;
  }
  body.light {
    color-scheme: light;
    --bg: #f1eff5;
    --screen1: #ffffff;
    --screen2: #f7f5fb;
    --card: #f2eff7;
    --card-dark: #e8e4f2;
    --card-hover: #e2dced;
    --purple: #9d4edd;
    --text: #26212f;
    --muted: #6d6679;
    --faint: #a49db6;
    --title: #2b2536;
    --screen-shadow: 0 24px 60px rgba(70,55,95,.18);
    --typo-fill: rgba(38,33,47,.055);
    --typo-stroke: rgba(38,33,47,.14);
    --neu-bg: #f4f2f9;
    --neu-shadow: rgba(163,157,183,.5);
    --neu-hi: rgba(255,255,255,.95);
    --neu-accent-shadow: rgba(190,95,95,.4);
    --neu-accent-hi: rgba(255,255,255,.9);
    --ring-track: #ddd8e6;
    --ring-fg: #26212f;
    --tabbar-bg: rgba(0,0,0,.035);
    --hairline: rgba(0,0,0,.08);
    --menu-border: rgba(0,0,0,.14);
    --error-bg: rgba(239,109,109,.14);
    --error-fg: #cc4444;
    --home-ind: rgba(0,0,0,.25);
    --bezel: #e7e3ef;
    --bezel-edge: rgba(0,0,0,.14);
    --hint: #7d7689;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    min-height: 100vh;
  }
  [hidden] { display: none !important; }

  /* ---- luxury typography background ---- */
  .type-bg {
    position: fixed; inset: 0; overflow: hidden;
    pointer-events: none; z-index: 0; user-select: none;
    font-family: var(--serif);
  }
  .type-bg span {
    position: absolute; white-space: nowrap; line-height: 1;
    color: var(--typo-fill); font-weight: 700;
  }
  .type-bg .outline { color: transparent; -webkit-text-stroke: 1.5px var(--typo-stroke); }
  .type-bg .w1 { top: 5%; left: -2%; font-size: 132px; font-style: italic; font-weight: 500; }
  .type-bg .w2 { top: 22%; right: -3%; font-size: 88px; letter-spacing: .16em; transform: rotate(-4deg); }
  .type-bg .w3 { top: 45%; left: -4%; font-size: 150px; font-style: italic; font-weight: 400; }
  .type-bg .w4 { top: 63%; right: -5%; font-size: 62px; letter-spacing: .28em; }
  .type-bg .w5 { bottom: 6%; left: 2%; font-size: 116px; letter-spacing: .08em; transform: rotate(-3deg); }
  .type-bg .w6 { bottom: 14%; right: 6%; font-size: 30px; letter-spacing: .42em; font-style: italic; font-weight: 400; }

  .stage {
    position: relative; z-index: 1;
    display: flex; justify-content: center; align-items: flex-start;
    padding: 52px 16px 40px;
  }

  /* ---- neumorphic buttons ---- */
  button { transition: box-shadow .18s ease, background .18s ease, color .18s ease, border-color .18s ease; }
  .view-toggle {
    position: fixed; top: 16px; right: 16px; z-index: 5;
    display: inline-flex; align-items: center; gap: 7px;
    padding: 10px 16px; font-size: 13px; font-weight: 600; cursor: pointer;
    color: var(--text); background: var(--neu-bg);
    border: none; border-radius: 999px;
    box-shadow: var(--neu-out);
  }
  .view-toggle:hover { color: var(--coral); }
  .view-toggle:active { box-shadow: var(--neu-in); }
  .header-actions { display: flex; align-items: center; gap: 9px; }
  .theme-btn {
    width: 34px; height: 34px; flex: none; padding: 0;
    display: grid; place-items: center; cursor: pointer;
    color: var(--muted); background: var(--neu-bg);
    border: none; border-radius: 50%;
    box-shadow: var(--neu-out-sm);
  }
  .theme-btn:hover { color: var(--coral); }
  .theme-btn:active { box-shadow: var(--neu-in-sm); }

  /* ---- device / screen ---- */
  .device { position: relative; width: 312px; }
  .notch { display: none; }
  .statusbar { display: none; }
  .screen {
    display: flex; flex-direction: column; overflow: hidden;
    background: linear-gradient(180deg, var(--screen1), var(--screen2));
    border-radius: 10px;
    box-shadow: var(--screen-shadow);
  }
  .app { flex: 1; min-height: 0; display: flex; flex-direction: column; }

  /* ---- desktop view fills the page; phone view uses the frame ---- */
  body:not(.phone) { background: linear-gradient(180deg, var(--screen1), var(--screen2)); }
  body:not(.phone) .stage {
    padding: 0; align-items: stretch;
    min-height: 100vh; min-height: 100dvh;
  }
  body:not(.phone) .device { width: 100%; }
  body:not(.phone) .screen {
    width: 100%; height: 100vh; height: 100dvh;
    border-radius: 0; box-shadow: none; background: transparent;
  }
  body:not(.phone) .scroll,
  body:not(.phone) .tabbar { width: 100%; max-width: 860px; margin-inline: auto; }
  body:not(.phone) .scroll { padding-top: 58px; }
  body:not(.phone) .hint { display: none; }
  body.phone .stage {
    align-items: center; min-height: calc(100vh - 46px); padding: 20px 16px;
  }

  body.phone .device {
    width: 390px; padding: 12px; background: var(--bezel);
    border-radius: 50px;
    box-shadow: 0 40px 90px rgba(0,0,0,.65), inset 0 0 0 2px var(--bezel-edge);
  }
  body.phone .screen { border-radius: 38px; box-shadow: none; height: 820px; }
  body.phone .notch {
    display: block; position: absolute; z-index: 3;
    top: 21px; left: 50%; transform: translateX(-50%);
    width: 112px; height: 26px; background: #0c0a0f; border-radius: 14px;
  }
  body.phone .statusbar {
    flex: none; display: flex; justify-content: space-between; align-items: center;
    height: 44px; padding: 4px 26px 0; font-size: 13px; font-weight: 600;
    color: var(--text);
  }
  .sb-icons { display: inline-flex; align-items: center; gap: 6px; }
  .home-ind { display: none; }
  body.phone .home-ind {
    flex: none; width: 118px; height: 5px; margin: 2px auto 8px;
    background: var(--home-ind); border-radius: 3px;
  }

  /* ---- scroll area ---- */
  .scroll {
    flex: 1; min-height: 0; overflow-y: auto;
    display: flex; flex-direction: column; gap: 14px;
    padding: 22px 16px 16px;
    scrollbar-width: thin; scrollbar-color: var(--ring-track) transparent;
  }
  .scroll::-webkit-scrollbar { width: 6px; }
  .scroll::-webkit-scrollbar-thumb { background: var(--ring-track); border-radius: 3px; }

  /* ---- header ---- */
  .app-header { display: flex; justify-content: space-between; align-items: flex-start; }
  .app-header h1 { margin: 0; font-size: 22px; font-weight: 800; letter-spacing: .2px; color: var(--text); }
  .date { margin: 7px 0 0; font-size: 11.5px; color: var(--muted); display: flex; gap: 14px; }
  .avatar {
    width: 34px; height: 34px; border: none; border-radius: 50%; cursor: pointer;
    background: linear-gradient(135deg, #c07af2, #8b4fe0);
    display: grid; place-items: center; color: #fff; flex: none;
    box-shadow: var(--neu-out-sm);
  }
  .avatar:active { box-shadow: var(--neu-in-sm); }

  /* ---- search ---- */
  .search { display: flex; gap: 8px; }
  .search input {
    flex: 1; min-width: 0; padding: 11px 13px; font-size: 12.5px;
    color: var(--text); background: var(--neu-bg);
    border: 1px solid transparent; border-radius: 10px; outline: none;
    box-shadow: var(--neu-in-sm);
  }
  .search input::placeholder { color: var(--muted); }
  .search input:focus { border-color: rgba(239,109,109,.65); }
  .search-btn {
    width: 40px; height: 40px; flex: none; border: none; border-radius: 10px;
    cursor: pointer; background: linear-gradient(145deg, #f58080, #e35f5f); color: #fff;
    display: grid; place-items: center;
    box-shadow: var(--neu-accent-out);
  }
  .search-btn:hover { box-shadow: var(--neu-accent-out), 0 0 0 2px rgba(239,109,109,.35); }
  .search-btn:active { box-shadow: var(--neu-accent-in); }
  .error {
    margin: 0; padding: 6px 10px; border-radius: 8px; font-size: 11.5px;
    background: var(--error-bg); color: var(--error-fg);
  }

  /* ---- today's tasks card ---- */
  .today {
    display: flex; align-items: center; justify-content: space-between; gap: 10px;
    background: var(--card-dark); border-radius: var(--radius); padding: 13px 14px;
  }
  .today h2 { margin: 0; font-size: 14.5px; font-weight: 700; color: var(--text); }
  .today-actions { display: flex; align-items: center; gap: 11px; }
  .ring { position: relative; width: 36px; height: 36px; flex: none; }
  .ring svg { display: block; transform: rotate(-90deg); }
  .ring .track { stroke: var(--ring-track); }
  .ring .fg { stroke: var(--ring-fg); }
  .ring span {
    position: absolute; inset: 0; display: grid; place-items: center;
    font-size: 8.5px; font-weight: 700; color: var(--text);
  }
  .icon-btn {
    width: 30px; height: 30px; flex: none; padding: 0;
    border: none; border-radius: 50%;
    background: var(--neu-bg); color: var(--coral); cursor: pointer;
    display: grid; place-items: center;
    box-shadow: var(--neu-out-sm);
  }
  .today .icon-btn { background: var(--card-dark); }
  .icon-btn:hover { color: var(--text); }
  .icon-btn:active { box-shadow: var(--neu-in-sm); }

  /* ---- add panel ---- */
  .add-panel {
    display: flex; flex-direction: column; gap: 8px;
    background: var(--card-dark); border-radius: var(--radius); padding: 10px;
  }
  .ap-row { display: flex; gap: 8px; }
  .ap-row input {
    min-width: 0; padding: 9px 11px; font-size: 12.5px;
    color: var(--text); background: var(--card-dark);
    border: 1px solid transparent; border-radius: 9px; outline: none;
    box-shadow: var(--neu-in-sm);
  }
  .ap-row input::placeholder { color: var(--muted); }
  .ap-row input:focus { border-color: rgba(239,109,109,.65); }
  .ap-row textarea {
    width: 100%; min-width: 0; padding: 8px 11px; font-family: inherit;
    font-size: 12.5px; line-height: 1.45; color: var(--text);
    background: var(--card-dark); border: 1px solid transparent;
    border-radius: 9px; outline: none; box-shadow: var(--neu-in-sm);
    resize: vertical;
  }
  .ap-row textarea::placeholder { color: var(--muted); }
  .ap-row textarea:focus { border-color: rgba(239,109,109,.65); }
  #new-title { flex: 1; }
  #new-time { flex: 1.4; }
  #new-date { flex: 1; }
  .add-panel button {
    flex: none; padding: 0 16px; font-size: 12.5px; font-weight: 700;
    color: #fff; background: linear-gradient(145deg, #f58080, #e35f5f);
    border: none; border-radius: 9px; cursor: pointer;
    box-shadow: var(--neu-accent-out);
  }
  .add-panel button:active { box-shadow: var(--neu-accent-in); }
  .add-panel .ap-cancel {
    padding: 0 13px; color: var(--muted);
    background: var(--card); box-shadow: var(--neu-out-sm);
  }
  .add-panel .ap-cancel:hover { color: var(--coral); }
  .add-panel .ap-cancel:active { box-shadow: var(--neu-in-sm); }

  /* ---- scrollable time picker (wheel) ---- */
  .time-picker {
    display: flex; align-items: flex-end; gap: 8px;
    background: var(--card-dark); border-radius: var(--radius); padding: 12px;
  }
  .tp-cols { display: flex; flex: 1; min-width: 0; gap: 6px; }
  .tp-slot { position: relative; flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px; }
  .tp-slot.tp-date { flex: 1.35; }
  .tp-label {
    height: 12px; line-height: 12px; text-align: center;
    font-size: 9.5px; font-weight: 700; letter-spacing: .1em;
    text-transform: uppercase; color: var(--muted);
  }
  .tp-col {
    position: relative; height: 130px; overflow-y: auto;
    scroll-snap-type: y mandatory; padding: 52px 0;
    background: var(--neu-bg); border-radius: 10px;
    box-shadow: var(--neu-in-sm); scrollbar-width: none;
  }
  .tp-col::-webkit-scrollbar { width: 0; height: 0; }
  .tp-slot::after {
    content: ""; position: absolute; left: 4px; right: 4px; top: 69px; height: 26px;
    border-radius: 8px; background: rgba(239,109,109,.12);
    border: 1px solid rgba(239,109,109,.35); pointer-events: none;
  }
  .tp-item {
    display: block; width: 100%; height: 26px; padding: 0;
    border: none; background: transparent; cursor: pointer;
    color: var(--muted); font-family: inherit; font-size: 13px; font-weight: 600;
    scroll-snap-align: center;
  }
  .tp-item.on { color: var(--coral); font-weight: 800; }
  .tp-date .tp-item { font-size: 11.5px; }
  .time-picker #tp-done { align-self: flex-end; }

  /* ---- task sections: pending / completed ---- */
  .task-section { display: flex; flex-direction: column; gap: 10px; }
  .section-head { display: flex; align-items: center; gap: 8px; }
  .section-head h3 {
    margin: 0; font-size: 11px; font-weight: 700; letter-spacing: .1em;
    text-transform: uppercase; color: var(--muted);
  }
  .count {
    min-width: 20px; padding: 1px 7px; text-align: center;
    font-size: 10.5px; font-weight: 700; color: var(--muted);
    background: var(--card); border-radius: 999px;
  }
  .tasks { display: flex; flex-direction: column; gap: 12px; }
  .task { position: relative; background: var(--card); border-radius: var(--radius); padding: 11px 12px 10px; }
  .task .top { display: flex; align-items: center; justify-content: space-between; }
  .tag { display: block; width: 42px; height: 7px; border-radius: 4px; flex: none; }
  .dots {
    padding: 4px 6px; border: none; background: var(--card);
    color: var(--muted); cursor: pointer; line-height: 0; border-radius: 999px;
    box-shadow: var(--neu-out-sm);
  }
  .dots:hover { color: var(--text); }
  .dots:active { box-shadow: var(--neu-in-sm); }
  .task .title { margin: 9px 0 10px; font-size: 12.5px; line-height: 1.4; color: var(--title); }
  .task.done .title { text-decoration: line-through; color: var(--muted); }
  .task .note {
    margin: -4px 0 10px; padding-left: 8px; border-left: 2px solid var(--coral);
    font-size: 11.5px; line-height: 1.45; color: var(--muted); white-space: pre-wrap;
    cursor: pointer;
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .task .note.open { display: block; -webkit-line-clamp: unset; overflow: visible; }
  .task .note:hover { color: var(--title); }
  .task .bottom { display: flex; align-items: center; gap: 8px; }
  .task .meta { flex: 1; min-width: 0; display: flex; align-items: center; gap: 8px; font-size: 10.5px; color: var(--muted); }
  .task .meta svg { flex: none; opacity: .8; }
  .task .time { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .check {
    width: 20px; height: 20px; flex: none; padding: 0;
    border: none; border-radius: 6px;
    background: var(--card); color: transparent; cursor: pointer;
    display: grid; place-items: center;
    box-shadow: var(--neu-in-sm);
  }
  .check[aria-checked="true"] {
    background: linear-gradient(145deg, #f58080, #e35f5f);
    color: #fff;
    box-shadow: var(--neu-accent-out-sm);
  }
  .check:hover { color: rgba(239,109,109,.7); }
  .check[aria-checked="true"]:hover { color: #fff; }
  .menu {
    position: absolute; top: 32px; right: 10px; z-index: 4; overflow: hidden;
    background: var(--card-dark); border: 1px solid var(--menu-border);
    border-radius: 10px; box-shadow: var(--neu-out);
  }
  .menu button {
    display: block; width: 100%; padding: 7px 16px;
    font-size: 12px; text-align: left;
    border: none; background: transparent; color: #e85f5f; cursor: pointer;
  }
  .menu button:hover { background: rgba(239,109,109,.12); }

  /* ---- empty states ---- */
  .empty { margin: 2px 0; font-size: 12px; text-align: center; color: var(--muted); font-style: italic; }

  /* ---- add bar ---- */
  .add-bar {
    display: grid; place-items: center; width: 100%; padding: 9px;
    background: var(--neu-bg); border: none; border-radius: 12px; cursor: pointer;
    box-shadow: var(--neu-out);
  }
  .add-bar .icon-btn { background: transparent; box-shadow: none; }
  .add-bar:hover .icon-btn { color: var(--text); }
  .add-bar:active { box-shadow: var(--neu-in); }

  /* ---- tab bar ---- */
  .tabbar {
    flex: none; display: flex; justify-content: space-around; align-items: center;
    padding: 11px 10px;
    background: var(--tabbar-bg);
    border-top: 1px solid var(--hairline);
  }
  .tab {
    width: 34px; height: 34px; padding: 0; border: none;
    background: var(--neu-bg); border-radius: 50%;
    color: var(--purple); cursor: pointer; display: grid; place-items: center;
    box-shadow: var(--neu-out-sm);
  }
  .tab:hover { color: var(--coral); }
  .tab.active { color: var(--coral); box-shadow: var(--neu-in-sm); }

  /* ---- inline name editing ---- */
  #greeting { cursor: pointer; }
  .name-input {
    padding: 7px 11px; font-size: 12.5px; color: var(--text);
    background: var(--neu-bg); border: 1px solid transparent;
    border-radius: 9px; outline: none; box-shadow: var(--neu-in-sm);
  }
  .name-input:focus { border-color: rgba(239,109,109,.65); }
  #name-input { width: 170px; font-size: 19px; font-weight: 800; padding: 5px 10px; }
  #set-name { width: 110px; background: var(--card); }

  /* ---- calendar + settings panels ---- */
  .panel {
    display: flex; flex-direction: column; gap: 13px;
    background: var(--card-dark); border-radius: var(--radius); padding: 15px 14px;
  }
  .panel-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
  .panel-head h2 {
    margin: 0; font-family: var(--serif); font-size: 17px; font-weight: 700;
    letter-spacing: .3px; color: var(--text);
  }
  .cal-nav { display: flex; gap: 8px; }
  .cal-nav .icon-btn { width: 26px; height: 26px; font-size: 16px; line-height: 1; }
  .cal-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; }
  .cal-dow {
    text-align: center; padding: 3px 0; font-size: 9.5px; font-weight: 700;
    letter-spacing: .08em; text-transform: uppercase; color: var(--muted);
  }
  .cal-day {
    position: relative;
    aspect-ratio: 1; min-height: 26px; border: none; border-radius: 8px;
    background: var(--card-dark); color: var(--text); cursor: pointer;
    font-size: 11.5px; font-weight: 600; box-shadow: var(--neu-out-sm);
  }
  .cal-day:hover { color: var(--coral); }
  .cal-day:active { box-shadow: var(--neu-in-sm); }
  .cal-day.selected:not(.today) { box-shadow: var(--neu-in-sm); color: var(--coral); }
  .cal-day.today {
    background: linear-gradient(145deg, #f58080, #e35f5f); color: #fff;
    box-shadow: var(--neu-accent-out-sm);
  }
  .cal-day.has::after {
    content: ""; position: absolute; bottom: 4px; left: 50%; transform: translateX(-50%);
    width: 4px; height: 4px; border-radius: 50%; background: var(--coral);
  }
  .cal-day.today.has::after { background: #fff; }
  .cal-agenda h3 {
    margin: 0; font-size: 11px; font-weight: 700; letter-spacing: .1em;
    text-transform: uppercase; color: var(--muted);
  }
  .cal-list { list-style: none; margin: 9px 0 0; padding: 0; display: flex; flex-direction: column; gap: 8px; }
  .cal-list li {
    display: flex; align-items: center; gap: 9px;
    background: var(--card); border-radius: 10px; padding: 9px 11px;
    font-size: 12.5px; color: var(--title);
  }
  .cal-list li.done { color: var(--muted); text-decoration: line-through; }
  .cal-list li.cal-empty { justify-content: center; color: var(--muted); font-style: italic; }
  .cal-list li.cal-sub {
    background: transparent; padding: 4px 4px 0; text-decoration: none;
    font-size: 10px; font-weight: 700; letter-spacing: .1em;
    text-transform: uppercase; color: var(--muted);
  }
  .cal-list .cal-dot { width: 8px; height: 8px; flex: none; border-radius: 50%; background: var(--coral); }
  .cal-list .cal-title { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .cal-list .cal-time { font-size: 10.5px; color: var(--muted); white-space: nowrap; }
  .setting-row {
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 9px; background: var(--card); border-radius: 10px; padding: 11px 12px;
  }
  .setting-row label { font-size: 12.5px; font-weight: 600; color: var(--title); }
  .setting-control { display: flex; align-items: center; gap: 8px; }
  .pill-btn {
    padding: 7px 13px; font-size: 11.5px; font-weight: 700; border: none;
    border-radius: 999px; cursor: pointer; color: var(--muted);
    background: var(--card); box-shadow: var(--neu-out-sm);
  }
  .pill-btn:hover { color: var(--coral); }
  .pill-btn:active { box-shadow: var(--neu-in-sm); }
  .pill-btn.on { box-shadow: var(--neu-in-sm); color: var(--coral); }
  .pill-btn.danger { color: var(--error-fg); }
  .pill-btn:disabled { opacity: .45; cursor: default; box-shadow: var(--neu-in-sm); }

  .hint { position: relative; z-index: 1; margin: 18px 0 0; font-size: 11.5px; text-align: center; color: var(--hint); }
  .hint code { font-family: ui-monospace, monospace; }

  /* ---- real phone screens: fill the viewport ---- */
  @media (max-width: 480px) {
    .view-toggle, .type-bg, .hint { display: none; }
    .stage { padding: 0; }
    body.phone .device, .device { width: 100%; padding: 0; background: none; border-radius: 0; box-shadow: none; }
    body.phone .notch, .notch,
    body.phone .statusbar, .statusbar,
    body.phone .home-ind, .home-ind { display: none; }
    body.phone .screen, body:not(.phone) .screen, .screen { height: auto; border-radius: 0; box-shadow: none; }
    body:not(.phone) .scroll, .scroll { padding-top: 18px; }
  }
</style>
</head>
<body>
<div class="type-bg" aria-hidden="true">
  <span class="w1">Élégance</span>
  <span class="w2 outline">LUXURY</span>
  <span class="w3">Timeless</span>
  <span class="w4 outline">SOPHISTICATION</span>
  <span class="w5">Maison</span>
  <span class="w6">L'art de vivre</span>
</div>

<button class="view-toggle" id="view-toggle" type="button"></button>

<div class="stage">
  <div class="device" id="device">
    <div class="notch" aria-hidden="true"></div>
    <div class="screen">
      <div class="statusbar" aria-hidden="true">
        <span id="sb-time">12:00</span>
        <span class="sb-icons">
          <svg width="17" height="11" viewBox="0 0 17 11" fill="currentColor" aria-hidden="true">
            <rect x="0" y="7" width="3" height="4" rx="1"/>
            <rect x="4.5" y="4.7" width="3" height="6.3" rx="1"/>
            <rect x="9" y="2.3" width="3" height="8.7" rx="1"/>
            <rect x="13.5" width="3" height="11" rx="1" opacity=".45"/>
          </svg>
          <svg width="25" height="12" viewBox="0 0 25 12" aria-hidden="true">
            <rect x=".5" y=".5" width="21" height="11" rx="3.5" fill="none" stroke="currentColor" opacity=".5"/>
            <rect x="2.5" y="2.5" width="14" height="7" rx="2" fill="currentColor"/>
            <rect x="22.7" y="4" width="2.3" height="4" rx="1.2" fill="currentColor" opacity=".5"/>
          </svg>
        </span>
      </div>

      <div class="app">
        <div class="scroll">
          <header class="app-header">
            <div>
              <h1 id="greeting" title="Click to set your name">Hey, <span id="name-text">Steve</span></h1>
              <input id="name-input" class="name-input" type="text" maxlength="24" autocomplete="off" hidden aria-label="Your name">
              <p class="date"><span id="today">21 sep 2022</span><span id="now">12:00pm</span></p>
            </div>
            <div class="header-actions">
              <button class="theme-btn" id="theme-toggle" type="button"
                      title="Light mode" aria-label="Switch to light mode">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.2 5.2 7 7M17 17l1.8 1.8M18.8 5.2 17 7M7 17l-1.8 1.8"/></svg>
              </button>
              <button class="avatar" id="avatar-btn" type="button" title="Set your name" aria-label="Set your name">
                <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M12 12a4.2 4.2 0 1 0 0-8.4 4.2 4.2 0 0 0 0 8.4Zm0 2.2c-4.3 0-7.6 2.3-7.6 5.1V21.5h15.2v-2.2c0-2.8-3.3-5.1-7.6-5.1Z"/>
                </svg>
              </button>
            </div>
          </header>

          <div class="search" id="search-row">
            <input id="search" type="text" placeholder="Search your Lists" autocomplete="off" aria-label="Search your lists">
            <button class="search-btn" id="search-btn" type="button" aria-label="Search">
              <svg width="17" height="17" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
                <circle cx="9" cy="9" r="5.5"/>
                <path d="M13.4 13.4 18 18"/>
              </svg>
            </button>
          </div>

          <p class="error" id="error" hidden></p>

          <section class="today" id="today-card">
            <h2>Today's tasks</h2>
            <div class="today-actions">
              <div class="ring" aria-hidden="true">
                <svg width="36" height="36" viewBox="0 0 36 36">
                  <circle class="track" cx="18" cy="18" r="15" fill="none" stroke-width="3"/>
                  <circle class="fg" id="ring-progress" cx="18" cy="18" r="15" fill="none"
                          stroke-width="3" stroke-linecap="round" stroke-dasharray="0 94.3"/>
                </svg>
                <span id="pct">0%</span>
              </div>
              <button class="icon-btn" id="add-toggle-1" type="button" aria-label="Add task">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </section>

          <form class="add-panel" id="add-form" hidden>
            <div class="ap-row">
              <input id="new-title" type="text" placeholder="New task" autocomplete="off" aria-label="Task name">
              <button type="submit">Add</button>
              <button class="ap-cancel" id="add-cancel" type="button">Cancel</button>
            </div>
            <div class="ap-row">
              <input id="new-time" type="text" placeholder="8:00AM - 8:30AM" autocomplete="off" aria-label="Task time">
              <input id="new-date" type="date" aria-label="Task date">
            </div>
            <div class="ap-row">
              <textarea id="new-note" rows="2" placeholder="Add a random note (optional)" aria-label="Task note"></textarea>
            </div>
          </form>

          <div class="time-picker" id="time-picker" hidden>
            <div class="tp-cols">
              <div class="tp-slot tp-date">
                <span class="tp-label">Date</span>
                <div class="tp-col" id="tp-date" aria-label="Date"></div>
              </div>
              <div class="tp-slot">
                <span class="tp-label">Hour</span>
                <div class="tp-col" id="tp-hour" aria-label="Hour"></div>
              </div>
              <div class="tp-slot">
                <span class="tp-label">Min</span>
                <div class="tp-col" id="tp-minute" aria-label="Minute"></div>
              </div>
              <div class="tp-slot">
                <span class="tp-label">AM/PM</span>
                <div class="tp-col" id="tp-meridiem" aria-label="AM or PM"></div>
              </div>
            </div>
            <button class="pill-btn" id="tp-done" type="button">Set</button>
          </div>

          <section class="task-section" id="pending-section">
            <div class="section-head">
              <h3>Pending</h3>
              <span class="count" id="pending-count">0</span>
            </div>
            <div class="tasks" id="pending-tasks"></div>
            <p class="empty" id="pending-empty" hidden></p>
          </section>

          <section class="task-section" id="completed-section">
            <div class="section-head">
              <h3>Completed</h3>
              <span class="count" id="completed-count">0</span>
            </div>
            <div class="tasks" id="completed-tasks"></div>
            <p class="empty" id="completed-empty" hidden></p>
          </section>

          <section class="panel" id="calendar-panel" hidden>
            <div class="panel-head">
              <h2 id="cal-title">Month</h2>
              <div class="cal-nav">
                <button class="icon-btn" id="cal-prev" type="button" aria-label="Previous month">&#8249;</button>
                <button class="icon-btn" id="cal-next" type="button" aria-label="Next month">&#8250;</button>
              </div>
            </div>
            <div class="cal-grid" id="cal-grid"></div>
            <div class="cal-agenda">
              <h3 id="cal-day-label">Today</h3>
              <ul class="cal-list" id="cal-list"></ul>
            </div>
          </section>

          <section class="panel" id="settings-panel" hidden>
            <div class="panel-head"><h2>Settings</h2></div>
            <div class="setting-row">
              <label for="set-name">Your name</label>
              <div class="setting-control">
                <input id="set-name" class="name-input" type="text" maxlength="24" autocomplete="off">
                <button class="pill-btn" id="set-name-save" type="button">Save</button>
              </div>
            </div>
            <div class="setting-row">
              <label>Appearance</label>
              <div class="setting-control">
                <button class="pill-btn" id="set-dark" type="button">Dark</button>
                <button class="pill-btn" id="set-light" type="button">Light</button>
              </div>
            </div>
            <div class="setting-row">
              <label>View</label>
              <div class="setting-control">
                <button class="pill-btn" id="set-desktop" type="button">Desktop</button>
                <button class="pill-btn" id="set-phone" type="button">Phone</button>
              </div>
            </div>
            <div class="setting-row">
              <label>Tasks</label>
              <div class="setting-control">
                <button class="pill-btn danger" id="set-clear" type="button">Clear completed</button>
              </div>
            </div>
          </section>

          <button class="add-bar" id="add-toggle-2" type="button" aria-label="Add task">
            <span class="icon-btn" aria-hidden="true">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
                <path d="M12 5v14M5 12h14"/>
              </svg>
            </span>
          </button>
        </div>

        <nav class="tabbar" aria-label="Main">
          <button class="tab active" type="button" data-view="home" title="Home" aria-label="Home">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true">
              <path d="M4 10.5 12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5H15V15H9v5.5H5.5A1.5 1.5 0 0 1 4 19z"/>
            </svg>
          </button>
          <button class="tab" type="button" data-view="lists" title="Lists" aria-label="Lists">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true">
              <rect x="4" y="4" width="16" height="16" rx="2.5"/>
              <path d="M8 4v16M11 9h6M11 13h6"/>
            </svg>
          </button>
          <button class="tab" id="tab-add" type="button" title="Add task" aria-label="Add task">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true">
              <rect x="3.5" y="3.5" width="17" height="17" rx="4"/>
              <path d="M12 8.5v7M8.5 12h7"/>
            </svg>
          </button>
          <button class="tab" type="button" data-view="calendar" title="Calendar" aria-label="Calendar">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true">
              <rect x="3.5" y="5" width="17" height="15.5" rx="3"/>
              <path d="M3.5 9.5h17M8 3v4M16 3v4M8.5 13.5h2M13.5 13.5h2M8.5 17h2M13.5 17h2"/>
            </svg>
          </button>
          <button class="tab" type="button" data-view="settings" title="Settings" aria-label="Settings">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M19.14 12.94c.04-.3.06-.61.06-.94s-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.49.49 0 0 0-.59-.22l-2.39.96a7.05 7.05 0 0 0-1.62-.94l-.36-2.54a.48.48 0 0 0-.48-.41h-3.84a.48.48 0 0 0-.48.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96a.49.49 0 0 0-.59.22L2.74 8.87a.48.48 0 0 0 .12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.48-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32a.49.49 0 0 0-.12-.61l-2.01-1.58ZM12 15.6A3.6 3.6 0 1 1 12 8.4a3.6 3.6 0 0 1 0 7.2Z"/>
            </svg>
          </button>
        </nav>
        <div class="home-ind" aria-hidden="true"></div>
      </div>
    </div>
  </div>
</div>

<p class="hint">Backed by <code>tasks.json</code> — shared with the <code>todo.py</code> CLI. Use <code>#phone</code> / <code>#light</code> / <code>#calendar</code> / <code>#settings</code> in the URL to preselect a view.</p>

<script>
  const INITIAL = __TASKS__;

  const TAGS = ["#f2a7c3", "#ee7f70", "#5fd3d3", "#b07af0", "#f0c674"];
  const ICON_PHONE = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/></svg>';
  const ICON_DESKTOP = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg>';
  const ICON_SUN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.2 5.2 7 7M17 17l1.8 1.8M18.8 5.2 17 7M7 17l-1.8 1.8"/></svg>';
  const ICON_MOON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.4 14.6A8.6 8.6 0 0 1 9.4 3.6a8.9 8.9 0 1 0 11 11Z"/></svg>';
  const ICON_DOTS = '<svg width="16" height="5" viewBox="0 0 20 6" fill="currentColor" aria-hidden="true"><circle cx="3" cy="3" r="1.7"/><circle cx="10" cy="3" r="1.7"/><circle cx="17" cy="3" r="1.7"/></svg>';
  const ICON_CHECK = '<svg width="12" height="12" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 7.4 5.6 10.5 11.5 4"/></svg>';
  const ICON_LIST = '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M2 4.5h12M2 8h12M2 11.5h7.5"/></svg>';

  const $ = (id) => document.getElementById(id);
  let tasks = INITIAL;
  let filter = "";

  function api(path, opts) {
    return fetch(path, opts).then(async (res) => {
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || res.statusText);
      return data;
    });
  }

  function showError(err) {
    $("error").textContent = "error: " + err.message;
    $("error").hidden = false;
  }

  function clearError() {
    $("error").hidden = true;
  }

  /* ---------- clock ---------- */
  const MONTHS = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];
  function tick() {
    const d = new Date();
    $("today").textContent = d.getDate() + " " + MONTHS[d.getMonth()] + " " + d.getFullYear();
    let h = d.getHours();
    const m = String(d.getMinutes()).padStart(2, "0");
    const ampm = h >= 12 ? "pm" : "am";
    h = h % 12 || 12;
    $("now").textContent = h + ":" + m + ampm;
    $("sb-time").textContent = String(d.getHours()).padStart(2, "0") + ":" + m;
  }

  /* ---------- rendering ---------- */
  function visibleTasks() {
    if (!filter) return tasks;
    return tasks.filter((t) => t.title.toLowerCase().includes(filter));
  }

  function closeMenus(except) {
    document.querySelectorAll(".menu").forEach((m) => {
      if (m !== except) m.hidden = true;
    });
  }

  function taskCard(t) {
    const card = document.createElement("article");
    card.className = "task" + (t.done ? " done" : "");

    const top = document.createElement("div");
    top.className = "top";
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.style.background = TAGS[((t.id - 1) % TAGS.length + TAGS.length) % TAGS.length];
    const dots = document.createElement("button");
    dots.className = "dots";
    dots.type = "button";
    dots.title = "Task options";
    dots.setAttribute("aria-label", "Options for " + t.title);
    dots.innerHTML = ICON_DOTS;
    dots.addEventListener("click", (event) => {
      event.stopPropagation();
      const willOpen = menu.hidden;
      closeMenus();
      menu.hidden = !willOpen;
    });
    top.append(tag, dots);

    const title = document.createElement("p");
    title.className = "title";
    title.textContent = t.title;

    const bottom = document.createElement("div");
    bottom.className = "bottom";
    const meta = document.createElement("div");
    meta.className = "meta";
    meta.innerHTML = ICON_LIST;
    const time = document.createElement("span");
    time.className = "time";
    time.textContent = (t.date ? dateLabel(t.date) + " \u00b7 " : "") + (t.time || "Anytime");
    meta.append(time);
    const check = document.createElement("button");
    check.className = "check";
    check.type = "button";
    check.setAttribute("role", "checkbox");
    check.setAttribute("aria-checked", String(!!t.done));
    check.setAttribute("aria-label", (t.done ? "Mark not done: " : "Mark done: ") + t.title);
    check.innerHTML = ICON_CHECK;
    check.addEventListener("click", () => act("/api/tasks/" + t.id + "/toggle"));
    bottom.append(meta, check);

    const menu = document.createElement("div");
    menu.className = "menu";
    menu.hidden = true;
    const del = document.createElement("button");
    del.type = "button";
    del.textContent = "Delete";
    del.addEventListener("click", (event) => {
      event.stopPropagation();
      menu.hidden = true;
      act("/api/tasks/" + t.id + "/delete");
    });
    menu.append(del);

    const note = t.note ? document.createElement("p") : null;
    if (note) {
      note.className = "note";
      note.textContent = t.note;
      note.title = "Click to expand the note";
      note.addEventListener("click", () => note.classList.toggle("open"));
    }
    card.append(top, title);
    if (note) card.append(note);
    card.append(bottom, menu);
    return card;
  }

  function fill(list, items) {
    list.textContent = "";
    items.forEach((t) => list.append(taskCard(t)));
  }

  function render() {
    const shown = visibleTasks();
    const pending = shown.filter((t) => !t.done);
    const completed = shown.filter((t) => t.done);

    fill($("pending-tasks"), pending);
    fill($("completed-tasks"), completed);

    $("pending-count").textContent = pending.length;
    $("completed-count").textContent = completed.length;

    $("pending-empty").hidden = pending.length > 0;
    $("pending-empty").textContent = filter
      ? "No pending tasks match your search."
      : tasks.length
        ? "Nothing pending — enjoy your day."
        : "No tasks yet — tap + to add one.";

    $("completed-empty").hidden = completed.length > 0 || tasks.length === 0;
    $("completed-empty").textContent = filter
      ? "No completed tasks match your search."
      : "No completed tasks yet.";

    const done = tasks.filter((t) => t.done).length;
    const pct = tasks.length ? Math.round((done / tasks.length) * 100) : 0;
    $("pct").textContent = pct + "%";
    const C = 2 * Math.PI * 15;
    $("ring-progress").setAttribute(
      "stroke-dasharray",
      ((C * pct) / 100).toFixed(1) + " " + C.toFixed(1)
    );
    syncSettings();
    if (view === "calendar") renderCalendar();
  }

  async function act(path) {
    try {
      const data = await api(path, { method: "POST" });
      clearError();
      tasks = data.tasks;
      render();
    } catch (err) {
      showError(err);
      refresh();
    }
  }

  async function refresh() {
    try {
      tasks = await api("/api/tasks");
      clearError();
      render();
    } catch (err) {
      showError(err);
    }
  }

  /* ---------- add form ---------- */
  function toggleAdd() {
    const panel = $("add-form");
    panel.hidden = !panel.hidden;
    if (!panel.hidden) $("new-title").focus();
    else hideTimePicker();
  }

  function resetAddForm() {
    $("new-title").value = "";
    $("new-time").value = "";
    $("new-date").value = "";
    $("new-note").value = "";
  }

  function cancelAdd() {
    resetAddForm();
    $("add-form").hidden = true;
    hideTimePicker();
  }

  async function submitAdd() {
    const title = $("new-title").value.trim();
    if (!title) {
      $("new-title").focus();
      return;
    }
    const time = $("new-time").value.trim();
    const date = $("new-date").value.trim();
    const note = $("new-note").value.trim();
    try {
      const data = await api("/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, time, date, note }),
      });
      tasks = data.tasks;
      resetAddForm();
      $("add-form").hidden = true;
      hideTimePicker();
      clearError();
      render();
    } catch (err) {
      showError(err);
    }
  }

  /* ---------- phone view ---------- */
  const smallScreen = window.matchMedia("(max-width: 480px)");
  function setPhone(on) {
    document.body.classList.toggle("phone", on && !smallScreen.matches);
    const btn = $("view-toggle");
    const isPhone = document.body.classList.contains("phone");
    btn.innerHTML = isPhone ? ICON_DESKTOP + " Desktop view" : ICON_PHONE + " Phone view";
    btn.setAttribute("aria-label", isPhone ? "Switch to desktop view" : "Switch to phone view");
    syncSettings();
  }

  /* ---------- dark / light mode ---------- */
  function setTheme(mode) {
    const light = mode === "light";
    document.body.classList.toggle("light", light);
    document.documentElement.style.colorScheme = light ? "light" : "dark";
    const btn = $("theme-toggle");
    btn.innerHTML = light ? ICON_MOON : ICON_SUN;
    btn.title = light ? "Dark mode" : "Light mode";
    btn.setAttribute("aria-label", light ? "Switch to dark mode" : "Switch to light mode");
    try {
      localStorage.setItem("todo-theme", light ? "light" : "dark");
    } catch (err) {
      /* storage unavailable (e.g. private mode) — theme just won't persist */
    }
    syncSettings();
  }

  function initialTheme() {
    let saved = null;
    try {
      saved = localStorage.getItem("todo-theme");
    } catch (err) {
      /* ignore */
    }
    if (window.location.hash.includes("#light")) return "light";
    if (window.location.hash.includes("#dark")) return "dark";
    return saved === "light" ? "light" : "dark";
  }

  /* ---------- scrollable time picker (wheel) ---------- */
  const TP_ITEM = 26; // must match the .tp-item height in the CSS
  const TP_HOURS = Array.from({ length: 12 }, (_, i) => String(i + 1));
  const TP_MINUTES = Array.from({ length: 12 }, (_, i) => String(i * 5).padStart(2, "0"));
  const TP_MERIDIEM = ["AM", "PM"];
  let TP_DATES = [];
  let tpDate = "";
  let tpHour = new Date().getHours() % 12 || 12;
  let tpMinute = Math.round(new Date().getMinutes() / 5) * 5 % 60;
  let tpMeridiem = new Date().getHours() >= 12 ? "PM" : "AM";

  function markColumn(el, index) {
    el.dataset.index = String(index);
    Array.from(el.children).forEach((child, i) => child.classList.toggle("on", i === index));
  }

  function positionColumn(el, index) {
    const i = Math.max(0, index);
    el.scrollTop = i * TP_ITEM;
    markColumn(el, i);
  }

  function buildColumn(el, items, apply) {
    el.textContent = "";
    items.forEach((label, i) => {
      const item = document.createElement("button");
      item.type = "button";
      item.className = "tp-item";
      item.textContent = label;
      item.addEventListener("click", () => {
        positionColumn(el, i);
        apply(i);
      });
      el.append(item);
    });
    let timer = 0;
    el.addEventListener("scroll", () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        const i = Math.max(0, Math.min(items.length - 1, Math.round(el.scrollTop / TP_ITEM)));
        // Only write the field when the selection actually changed — this keeps a
        // typed value/range intact when the wheel merely snaps into place.
        const changed = Number(el.dataset.index) !== i;
        markColumn(el, i);
        if (changed) apply(i);
      }, 90);
    });
  }

  function writeTimeField() {
    $("new-time").value = tpHour + ":" + String(tpMinute).padStart(2, "0") + tpMeridiem;
  }

  function writeDateField() {
    $("new-date").value = tpDate;
  }

  function isoOf(d) {
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") +
      "-" + String(d.getDate()).padStart(2, "0");
  }

  function seedTimePicker() {
    // Only take over the field when it holds exactly one time (e.g. "8:00AM");
    // free text and ranges like "8:00AM - 9:30AM" keep the wheel's own state.
    const m = $("new-time").value.trim().match(/^(\\d{1,2})\\s*:\\s*(\\d{2})\\s*(am|pm)?$/i);
    if (!m) return;
    tpHour = Number(m[1]) % 12 || 12;
    tpMinute = Math.round(Number(m[2]) / 5) * 5 % 60;
    if (m[3]) tpMeridiem = m[3].toUpperCase();
    const day = $("new-date").value.trim();
    if (day) tpDate = day;
  }

  function openTimePicker() {
    seedTimePicker();
    $("time-picker").hidden = false;
    positionColumn($("tp-date"), Math.max(0, TP_DATES.findIndex((x) => x.iso === tpDate)));
    positionColumn($("tp-hour"), TP_HOURS.indexOf(String(tpHour)));
    positionColumn($("tp-minute"), TP_MINUTES.indexOf(String(tpMinute).padStart(2, "0")));
    positionColumn($("tp-meridiem"), tpMeridiem === "PM" ? 1 : 0);
  }

  function hideTimePicker() {
    $("time-picker").hidden = true;
  }

  function buildTimePicker() {
    TP_DATES = Array.from({ length: 28 }, (_, i) => {
      const day = new Date();
      day.setDate(day.getDate() + i);
      return {
        iso: isoOf(day),
        label: i === 0 ? "Today"
          : i === 1 ? "Tomorrow"
            : DOW[(day.getDay() + 6) % 7] + " " + day.getDate(),
      };
    });
    tpDate = TP_DATES[0].iso;
    buildColumn($("tp-date"), TP_DATES.map((x) => x.label), (i) => {
      tpDate = TP_DATES[i].iso;
      writeDateField();
    });
    buildColumn($("tp-hour"), TP_HOURS, (i) => {
      tpHour = Number(TP_HOURS[i]);
      writeTimeField();
    });
    buildColumn($("tp-minute"), TP_MINUTES, (i) => {
      tpMinute = Number(TP_MINUTES[i]);
      writeTimeField();
    });
    buildColumn($("tp-meridiem"), TP_MERIDIEM, (i) => {
      tpMeridiem = TP_MERIDIEM[i];
      writeTimeField();
    });
  }

  /* ---------- views: home / lists / calendar / settings ---------- */
  let view = "home";

  function setView(next) {
    view = next;
    const home = next === "home";
    const listing = home || next === "lists";
    $("search-row").hidden = !home;
    $("today-card").hidden = !home;
    $("pending-section").hidden = !listing;
    $("completed-section").hidden = !listing;
    $("add-toggle-2").hidden = !listing;
    $("calendar-panel").hidden = next !== "calendar";
    $("settings-panel").hidden = next !== "settings";
    if (!listing) {
      $("add-form").hidden = true;
      hideTimePicker();
    }
    document.querySelectorAll(".tab[data-view]").forEach((tab) => {
      tab.classList.toggle("active", tab.dataset.view === next);
    });
    document.querySelector(".scroll").scrollTop = 0;
    if (next === "calendar") renderCalendar();
    if (next === "settings") syncSettings();
  }

  /* ---------- display name ---------- */
  let userName = "Steve";

  function applyName() {
    $("name-text").textContent = userName;
    const field = $("set-name");
    if (field) field.value = userName;
  }

  function loadName() {
    try {
      const saved = localStorage.getItem("todo-name");
      if (saved) userName = saved;
    } catch (err) {
      /* storage unavailable — name just won't persist */
    }
    applyName();
  }

  function setName(value) {
    userName = (value || "").trim().slice(0, 24) || "Steve";
    try {
      localStorage.setItem("todo-name", userName);
    } catch (err) {
      /* ignore */
    }
    applyName();
  }

  function startNameEdit() {
    const input = $("name-input");
    if (!input.hidden) return;
    input.value = userName;
    input.hidden = false;
    $("greeting").hidden = true;
    input.focus();
    input.select();
  }

  function endNameEdit(save) {
    const input = $("name-input");
    if (input.hidden) return;
    if (save) setName(input.value);
    input.hidden = true;
    $("greeting").hidden = false;
  }

  /* ---------- calendar ---------- */
  const MONTHS_LONG = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"];
  const DOW = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  let calMonth = new Date();
  let calSelected = new Date();

  const startOfDay = (d) => new Date(d.getFullYear(), d.getMonth(), d.getDate());
  const sameDay = (a, b) => startOfDay(a).getTime() === startOfDay(b).getTime();

  function renderCalendar() {
    const grid = $("cal-grid");
    grid.textContent = "";
    const year = calMonth.getFullYear();
    const month = calMonth.getMonth();
    $("cal-title").textContent = MONTHS_LONG[month] + " " + year;
    DOW.forEach((day) => {
      const head = document.createElement("span");
      head.className = "cal-dow";
      head.textContent = day;
      grid.append(head);
    });
    const offset = (new Date(year, month, 1).getDay() + 6) % 7; // weeks start Monday
    const days = new Date(year, month + 1, 0).getDate();
    const today = new Date();
    for (let i = 0; i < offset; i += 1) grid.append(document.createElement("span"));
    for (let day = 1; day <= days; day += 1) {
      const date = new Date(year, month, day);
      const cell = document.createElement("button");
      cell.type = "button";
      cell.className = "cal-day";
      cell.textContent = day;
      cell.setAttribute("aria-label", MONTHS_LONG[month] + " " + day);
      if (sameDay(date, today)) cell.classList.add("today");
      if (sameDay(date, calSelected)) cell.classList.add("selected");
      if (tasks.some((t) => t.date === isoOf(date))) cell.classList.add("has");
      cell.addEventListener("click", () => {
        calSelected = date;
        if (date.getMonth() !== calMonth.getMonth() || date.getFullYear() !== calMonth.getFullYear()) {
          calMonth = new Date(date.getFullYear(), date.getMonth(), 1);
        }
        renderCalendar();
      });
      grid.append(cell);
    }
    renderAgenda();
  }

  function agendaItem(t) {
    const item = document.createElement("li");
    if (t.done) item.classList.add("done");
    const dot = document.createElement("span");
    dot.className = "cal-dot";
    const title = document.createElement("span");
    title.className = "cal-title";
    title.textContent = t.title;
    const time = document.createElement("span");
    time.className = "cal-time";
    time.textContent = t.time || "Anytime";
    item.append(dot, title, time);
    return item;
  }

  function renderAgenda() {
    const iso = isoOf(calSelected);
    const isToday = sameDay(calSelected, new Date());
    const weekday = DOW[(calSelected.getDay() + 6) % 7];
    $("cal-day-label").textContent = (isToday ? "Today — " : "") + weekday + " " +
      calSelected.getDate() + " " + MONTHS_LONG[calSelected.getMonth()];
    const list = $("cal-list");
    list.textContent = "";
    const byTime = (a, b) => (a.time || "zz").localeCompare(b.time || "zz");
    const onDay = tasks.filter((t) => t.date === iso).sort(byTime);
    const undated = tasks.filter((t) => !t.date).sort(byTime);
    if (!onDay.length && !undated.length) {
      const empty = document.createElement("li");
      empty.className = "cal-empty";
      empty.textContent = tasks.length
        ? "Nothing scheduled for this day."
        : "No tasks yet — add one from the Home tab.";
      list.append(empty);
      return;
    }
    onDay.forEach((t) => list.append(agendaItem(t)));
    if (undated.length) {
      const sub = document.createElement("li");
      sub.className = "cal-sub";
      sub.textContent = onDay.length ? "No date" : "Without a date";
      list.append(sub);
      undated.forEach((t) => list.append(agendaItem(t)));
    }
  }

  function dateLabel(iso) {
    if (!/^\\d{4}-\\d{2}-\\d{2}$/.test(iso || "")) return iso;
    const now = new Date();
    if (iso === isoOf(now)) return "Today";
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    if (iso === isoOf(tomorrow)) return "Tomorrow";
    const p = iso.split("-");
    const d = new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]));
    return DOW[(d.getDay() + 6) % 7] + " " + d.getDate() + " " +
      MONTHS_LONG[d.getMonth()].slice(0, 3);
  }

  /* ---------- settings ---------- */
  function syncSettings() {
    const light = document.body.classList.contains("light");
    const phone = document.body.classList.contains("phone");
    const mark = (id, on) => {
      const el = $(id);
      if (el) el.classList.toggle("on", on);
    };
    mark("set-dark", !light);
    mark("set-light", light);
    mark("set-phone", phone);
    mark("set-desktop", !phone);
    const clear = $("set-clear");
    if (clear) {
      const done = tasks.filter((t) => t.done).length;
      clear.textContent = done ? "Clear completed (" + done + ")" : "Clear completed";
      clear.disabled = done === 0;
    }
  }

  async function clearCompleted() {
    const done = tasks.filter((t) => t.done).map((t) => t.id);
    if (!done.length) return;
    try {
      for (const id of done) {
        await api("/api/tasks/" + id + "/delete", { method: "POST" });
      }
      clearError();
      await refresh();
    } catch (err) {
      showError(err);
      refresh();
    }
  }

  /* ---------- wire up ---------- */
  $("view-toggle").addEventListener("click", () =>
    setPhone(!document.body.classList.contains("phone"))
  );
  $("theme-toggle").addEventListener("click", () =>
    setTheme(document.body.classList.contains("light") ? "dark" : "light")
  );
  $("add-toggle-1").addEventListener("click", toggleAdd);
  $("add-toggle-2").addEventListener("click", toggleAdd);
  $("add-cancel").addEventListener("click", cancelAdd);
  $("add-form").addEventListener("submit", (event) => {
    event.preventDefault();
    submitAdd();
  });
  $("search").addEventListener("input", (event) => {
    filter = event.target.value.trim().toLowerCase();
    render();
  });
  $("search-btn").addEventListener("click", () => $("search").focus());
  $("avatar-btn").addEventListener("click", startNameEdit);
  $("greeting").addEventListener("click", startNameEdit);
  $("name-input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") endNameEdit(true);
    if (event.key === "Escape") endNameEdit(false);
  });
  $("name-input").addEventListener("blur", () => endNameEdit(true));
  $("set-name-save").addEventListener("click", () => setName($("set-name").value));
  $("set-name").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      setName($("set-name").value);
    }
  });
  $("set-dark").addEventListener("click", () => setTheme("dark"));
  $("set-light").addEventListener("click", () => setTheme("light"));
  $("set-phone").addEventListener("click", () => setPhone(true));
  $("set-desktop").addEventListener("click", () => setPhone(false));
  $("set-clear").addEventListener("click", clearCompleted);
  $("new-time").addEventListener("focus", openTimePicker);
  $("new-time").addEventListener("click", openTimePicker);
  $("tp-done").addEventListener("click", hideTimePicker);
  $("new-date").addEventListener("input", () => {
    const value = $("new-date").value.trim();
    if (!value) return;
    tpDate = value;
    positionColumn($("tp-date"), Math.max(0, TP_DATES.findIndex((x) => x.iso === value)));
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest || !event.target.closest("#time-picker, #new-time")) {
      hideTimePicker();
    }
  });
  $("cal-prev").addEventListener("click", () => {
    calMonth = new Date(calMonth.getFullYear(), calMonth.getMonth() - 1, 1);
    renderCalendar();
  });
  $("cal-next").addEventListener("click", () => {
    calMonth = new Date(calMonth.getFullYear(), calMonth.getMonth() + 1, 1);
    renderCalendar();
  });
  document.querySelectorAll(".tab").forEach((tab) => {
    tab.addEventListener("click", () => {
      const target = tab.dataset.view;
      if (target) {
        setView(target);
        return;
      }
      if (view !== "home" && view !== "lists") setView("home");
      if ($("add-form").hidden) toggleAdd();
      else $("new-title").focus();
    });
  });
  document.addEventListener("click", () => closeMenus());
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenus();
      $("add-form").hidden = true;
      hideTimePicker();
      endNameEdit(false);
    }
  });
  if (smallScreen.addEventListener) {
    smallScreen.addEventListener("change", () => setPhone(false));
  }

  setPhone(window.location.hash.includes("#phone"));
  setTheme(initialTheme());
  loadName();
  buildTimePicker();
  setView("home");
  ["lists", "calendar", "settings"].some((v) => {
    if (!window.location.hash.includes("#" + v)) return false;
    setView(v);
    return true;
  });
  tick();
  setInterval(tick, 30000);
  render();
  refresh();
</script>
</body>
</html>
"""


class TodoHandler(BaseHTTPRequestHandler):
    server_version = "todo.py-web"

    def _reply(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, status, payload):
        self._reply(status, json.dumps(payload).encode("utf-8"),
                    "application/json; charset=utf-8")

    def _html(self, status, text):
        self._reply(status, text.encode("utf-8"),
                    "text/html; charset=utf-8")

    def _error(self, status, message):
        self._json(status, {"error": message})

    def _page(self):
        """Render the page with the current tasks embedded for instant paint."""
        try:
            tasks = load_tasks()
        except ValueError:
            tasks = []
        payload = json.dumps(tasks).replace("<", "\\u003c")
        return PAGE.replace("__TASKS__", payload)

    def _read_body(self):
        """Return the parsed JSON object, {} if empty, or None if invalid."""
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length > 0 else b""
        if not raw:
            return {}
        try:
            data = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None
        return data if isinstance(data, dict) else None

    def _tasks(self):
        """Load tasks, replying with a 500 and returning None on failure."""
        try:
            return load_tasks()
        except ValueError as exc:
            self._error(500, str(exc))
            return None

    def _save(self, tasks):
        """Persist tasks, replying with a 500 and returning False on failure."""
        try:
            save_tasks(tasks)
        except OSError as exc:
            self._error(500, f"Could not write {DATA_FILE.name}: {exc}")
            return False
        return True

    def do_GET(self):
        path = urlsplit(self.path).path
        if path in ("/", "/index.html"):
            self._html(200, self._page())
        elif path == "/api/tasks":
            tasks = self._tasks()
            if tasks is not None:
                self._json(200, tasks)
        else:
            self._error(404, f"Not found: {path}")

    def do_POST(self):
        path = urlsplit(self.path).path
        body = self._read_body()
        if body is None:
            self._error(400, "Expected a JSON object body.")
            return
        tasks = self._tasks()
        if tasks is None:
            return

        if path == "/api/tasks":
            title = str(body.get("title", "")).strip()
            if not title:
                self._error(400, "Task text is required.")
                return
            raw_time = body.get("time")
            time = raw_time.strip()[:60] if isinstance(raw_time, str) else ""
            raw_date = body.get("date")
            date = raw_date.strip() if isinstance(raw_date, str) else ""
            if date:
                try:
                    datetime.date.fromisoformat(date)
                except ValueError:
                    date = ""
            raw_note = body.get("note")
            note = raw_note.strip()[:500] if isinstance(raw_note, str) else ""
            task_id = max((t["id"] for t in tasks), default=0) + 1
            task = {"id": task_id, "title": title, "done": False}
            if time:
                task["time"] = time
            if date:
                task["date"] = date
            if note:
                task["note"] = note
            tasks.append(task)
            if self._save(tasks):
                self._json(201, {"ok": True, "tasks": tasks})
            return

        match = re.fullmatch(r"/api/tasks/(\d+)/(toggle|delete)", path)
        if match is None:
            self._error(404, f"Not found: {path}")
            return
        task_id, action = int(match.group(1)), match.group(2)
        task = next((t for t in tasks if t.get("id") == task_id), None)
        if task is None:
            self._error(404, f"Task with id {task_id} not found.")
            return
        if action == "toggle":
            task["done"] = not task.get("done")
        else:
            tasks.remove(task)
        if self._save(tasks):
            self._json(200, {"ok": True, "tasks": tasks})

    def log_message(self, fmt, *args):
        print(f"[web] {self.address_string()} {fmt % args}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="web.py",
        description="A small web UI for todo.py (standard library only).")
    parser.add_argument("--host", default="127.0.0.1",
                        help="interface to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000,
                        help="port to listen on (default: 8000)")
    parser.add_argument("--no-open", action="store_true",
                        help="don't open a browser automatically")
    args = parser.parse_args(argv)

    try:
        server = ThreadingHTTPServer((args.host, args.port), TodoHandler)
    except OSError as exc:
        fail(f"Could not listen on {args.host}:{args.port}: {exc}")

    host = "127.0.0.1" if args.host in ("0.0.0.0", "::") else args.host
    url = f"http://{host}:{server.server_address[1]}/"
    print(f"Serving todo.py on {url} (Ctrl+C to stop)")
    if not args.no_open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
