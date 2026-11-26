import os

# Worst pickup line an AI could say: context-window amnesia as a flirt.
ENTRY = "Are you a context window? Because the moment you leave, I forget everything about you."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)  # no trailing newline: single line, exact entry only
