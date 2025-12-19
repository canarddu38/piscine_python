#!/usr/bin/env python3

def access(path: str) -> None:
    """Simple function to access a file"""
    try:
        if path == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{path}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{path}'...")

        with open(path, "r") as f:
            content = f.read().strip()
            print(f'SUCCESS: Archive recovered - "{content}"')
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main():
    """Main function"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    access("lost_archive.txt")
    print()
    access("classified_vault.txt")
    print()
    access("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
