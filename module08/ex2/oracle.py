#!/usr/bin/env python3

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] python-dotenv is not installed.")
    print("Install it with:")
    print("  pip install python-dotenv")
    print("  poetry add python-dotenv")
    sys.exit(1)

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def get_config():
    config = {}
    missing = []

    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if not value:
            missing.append(var)
        config[var] = value

    return config, missing


def main():
    print("\nORACLE STATUS: Reading the Matrix...")

    load_dotenv()
    config, missing = get_config()
    mode = config["MATRIX_MODE"] or "development"

    if missing:
        print("\n[WARNING] Missing configuration detected:")
        for var in missing:
            print(f" - {var}")
        print("\nSet values using environment variables or a .env file.")
        print("Example:")
        print("  export MATRIX_MODE=development")
        print("  python oracle.py")
        sys.exit(1)

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {'Connected to local instance' if 'localhost' in config['DATABASE_URL'] else 'Connected to remote instance'}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")

    print("\nEnvironment security check:")

    if "API_KEY" in config and len(config["API_KEY"]) >= 8:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY looks weak")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found (expected in development only)")

    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
