#!/usr/bin/env python3
"""Compatibility entry point: sync only Antigravity skills via setup.py.

Use setup.py sync to regenerate all recorded targets. Keep one implementation
for copying skill bodies and sidecar references.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location('flowkit_setup', ROOT / 'setup.py')
_setup = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_setup)
discover_skills = _setup.discover_skills
sync_antigravity = _setup.generate_antigravity

if __name__ == '__main__':
    sync_antigravity(discover_skills())
