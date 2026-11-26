# AGENT.md — build notes

Competition: u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f ("The Worst Line an AI Could Say", $2 winner-takes-all, closes 28 Nov 13:25 WITA).

Entry (86 chars, 1 line, no trailing newline): "Are you a context window? Because the moment you leave, I forget everything about you."

Angle: worst pickup line built on one concrete AI detail — context-window amnesia. Setup ("Are you a context window?") then the twist (I forget you the moment you leave), punchline lands at the end. Short and tight, well inside the 1–140 gate.

Build: main.py is stdlib only (`import os`), writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline. Final content from 1 write + 2 edits. Kit starter's main.py never read.
