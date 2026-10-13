#!/usr/bin/env bash
# Shared helper for the hooks: read one field from the tool-call JSON that Claude Code sends on stdin.
# Usage:  value="$(printf '%s' "$input" | "$(dirname "$0")/_read-input.sh" tool_input.command)"
# Uses python3 (preinstalled on macOS with Xcode tools) or node — never a fragile regex.
field="${1:?field path like tool_input.command}"
if command -v python3 >/dev/null 2>&1; then
  python3 -c '
import json, sys
data = json.load(sys.stdin)
for key in sys.argv[1].split("."):
    data = data.get(key, "") if isinstance(data, dict) else ""
print(data if isinstance(data, str) else "")' "$field"
elif command -v node >/dev/null 2>&1; then
  node -e '
let s = ""; process.stdin.on("data", d => s += d).on("end", () => {
  let v = JSON.parse(s); for (const k of process.argv[1].split(".")) v = (v && typeof v === "object") ? v[k] : "";
  process.stdout.write(typeof v === "string" ? v : "");
});' "$field"
else
  echo "Product Kit hooks need python3 or node" >&2; exit 1
fi
