#!/usr/bin/env python3

def write_line(f, i: int, text: str) -> None:
    f.write(text)
    print(text, end='')


print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

path = "./new_discovery.txt"
data = [
    "New quantum algorithm discovered",
    
]
print(f"Initializing new storage unit: {path}")
try:
    with open(path, "w") as f:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        write_line(f, "{[}ENTRY 001{]} \n")
        write_line(f, "{[}ENTRY 002{]} Efficiency increased by 347%\n")
        write_line(f, "{[}ENTRY 003{]} Archived by Data Archivist trainee\n")

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{path}' ready for long-term preservation.")
except Exception as e:
    print(f"ERROR: {e.args[0]}")
