#!/usr/bin/env python3
"""Small verification script to run inside the SWAN session.

Run: python test_env.py
It prints Python version, platform, and attempts to import common packages.
"""
import sys
import platform
import importlib


def try_import(name):
    try:
        mod = importlib.import_module(name)
        ver = getattr(mod, "__version__", "unknown")
        return True, ver
    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("Python:", sys.version.splitlines()[0])
    print("Platform:", platform.platform())
    pkgs = ["numpy", "pandas", "matplotlib", "scipy", "sklearn", "requests"]
    for p in pkgs:
        ok, info = try_import(p)
        if ok:
            print(f"OK: imported {p} (version: {info})")
        else:
            print(f"MISSING: {p} -> {info}")

    # quick numeric check if numpy is available
    try:
        import numpy as np
        a = np.arange(6).reshape(2, 3)
        print("Numpy quick check, shape:", a.shape)
    except Exception:
        pass
