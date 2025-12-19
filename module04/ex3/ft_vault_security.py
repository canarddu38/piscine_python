#!/usr/bin/env python3

def main():
    """Main function"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    with open("./classified_data.txt", "r") as f:
        print("SECURE EXTRACTION:")
        while (chr := f.read(1)):
            if (chr == '[' or chr == ']'):
                print("{"+chr+"}", end='')
            else:
                print(chr, end='')
    print("\n")

    print("SECURE PRESERVATION:")
    with open("./log.txt", "w") as f:
        line = "{[}CLASSIFIED{]} New security protocols archived"
        f.write(line)
        print(line)
        print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
