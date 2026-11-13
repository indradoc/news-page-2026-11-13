#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Writes the entry picture to /output/entry.png (a JPEG by content, per the rules)."""
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
