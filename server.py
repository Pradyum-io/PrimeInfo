#!/usr/bin/env python3
"""
PrimeCoreInfo Contact Form Backend Server Launcher.
Run with: python3 server.py
"""
import sys
from pathlib import Path

# Ensure root directory is in sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.server import run_server

if __name__ == "__main__":
    run_server()
