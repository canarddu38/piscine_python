#!/usr/bin/env python3

import site
import sys
import os


def in_virtualenv() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
        or "VIRTUAL_ENV" in os.environ
    )


def print_env_info() -> None:
    print("Current Python:", sys.executable)
    print("Virtual Environment:",
          os.environ.get("VIRTUAL_ENV", "None detected")
          .split("/bin/python")[0].split("/")[-1])
    if os.environ.get("VIRTUAL_ENV", None):
        print("Environment Path:", os.environ.get("VIRTUAL_ENV"))
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:", site.getsitepackages()[0])
    else:
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print(".\\matrix_env\\Scripts\\activate   # On Windows")
        print()
        print("Then run this program again")


def main() -> None:
    print("\nMATRIX STATUS: ", end='')
    if in_virtualenv():
        print("Welcome to the construct")
    else:
        print("You're still plugged in\n")

    print_env_info()


if __name__ == "__main__":
    main()
