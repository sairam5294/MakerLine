#!/usr/bin/env python3
"""Convenience entry point for the handoff skill's shared-context checker (see its references/shared-context.md)."""
import pathlib
import runpy

TARGET = pathlib.Path(__file__).resolve().parent.parent / "plugin/skills/handoff/scripts/context_check.py"
runpy.run_path(str(TARGET), run_name="__main__")
