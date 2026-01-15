#!/usr/bin/env python3

import sys
import importlib
import os

REQUIRED_PACKAGES = ["pandas", "requests", "matplotlib", "numpy"]


def check_dependencies() -> tuple[list, dict]:
    print("Checking dependencies:")
    missing = []
    versions = {}

    for pkg in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            versions[pkg] = version
            print(f"\033[32m[OK]\033[0m      {pkg} ({version}) - Ready")
        except ImportError:
            print(f"\033[31m[MISSING]\033[0m {pkg}")
            missing.append(pkg)
    return missing, versions


def installation_help(missing):
    print("\nMissing dependencies detected.")
    print("You can install them using:\n")
    print("With pip:")
    print("  pip install -r requirements.txt\n")
    print("With Poetry:")
    print("  poetry install\n")
    print("Missing packages:", ", ".join(missing))


def environment_info():
    print("\nEnvironment detection:")
    if os.environ.get("POETRY_ACTIVE") == "1":
        print("Running inside a Poetry environment")
    elif hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix:
        print("Running inside a virtual environment (pip/venv)")
    else:
        print("Running in global Python environment")


def analyze_data():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    data_points = 1000
    print(f"Processing {data_points} data points...")

    df = pd.DataFrame({
        "signal": np.random.randn(data_points).cumsum(),
        "time": np.arange(data_points)
    })

    plt.figure()
    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Generating visualization...")
    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main():
    print("\nLOADING STATUS: Loading programs...\n")

    missing, versions = check_dependencies()
    environment_info()

    if missing:
        installation_help(missing)
        sys.exit(1)

    analyze_data()


if __name__ == "__main__":
    main()
