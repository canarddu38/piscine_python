#!/usr/bin/env python3

def ft_count_harvest_recursive(days=None, current=1):
    if days is None:
        days = int(input("Days until harvest: "))

    if current > days:
        print("Harvest time!")
        return

    print(f"Day {current}")
    ft_count_harvest_recursive(days, current + 1)
