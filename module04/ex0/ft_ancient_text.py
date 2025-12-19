#!/usr/bin/env python3

def main():
    """Main function"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    path = "./ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {path}")
        with open(path, "r") as f:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            while (chr := f.read(1)):
                if (chr == '[' or chr == ']'):
                    print("{"+chr+"}", end='')
                else:
                    print(chr, end='')
        print("\n\nData recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
