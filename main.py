#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entrypoint: writes the entry picture to /output/entry.png (a JPEG by content, per the rules)."""
import os, shutil
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
shutil.copyfile(src, os.path.join(out, "entry.png"))
print("entry written:", os.path.join(out, "entry.png"))
