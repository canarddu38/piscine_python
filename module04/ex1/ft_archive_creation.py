#!/usr/bin/env python3

def write_line(f, text: str) -> None:
    """Write data to a file and print it"""
    f.write(text)
    print(text, end='')


def main():
    """Main function"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    path = "./new_discovery.txt"
    data = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]
    print(f"Initializing new storage unit: {path}")
    try:
        with open(path, "w") as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            i = 1
            for line in data:
                write_line(f, f"{{[}}ENTRY 00{i}{{]}} {line}\n")
                i += 1

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{path}' ready for long-term preservation.")
    except Exception as e:
        print(f"ERROR: {e.args[0]}")


if __name__ == "__main__":
    main()
