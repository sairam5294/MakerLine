#!/usr/bin/env python3
"""Convenience entry point for the distributable product opportunity review script."""
import pathlib
import runpy

TARGET = pathlib.Path(__file__).resolve().parent.parent / "plugin/skills/product-opportunity-review/scripts/opportunity_review.py"
runpy.run_path(str(TARGET), run_name="__main__")
