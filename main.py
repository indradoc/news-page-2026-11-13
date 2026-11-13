#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Writes the entry picture to /output/entry.png."""
import os, shutil
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"), os.path.join(out, "entry.png"))
