#!/usr/bin/env python3

import sys

print("=== Command Quest ===")
if (len(sys.argv) == 1):
    print("No arguments provided!")

i = 0
for arg in sys.argv:
    if i == 0:
        print(f"Program name: {arg}")
    else:
        print(f"Argument {i}: {arg}")
    i += 1
print(f"Total arguments: {i}")
