#!/usr/bin/env python3

import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")
    
    op = ops[operation]
    if len(spells) == 0:
        if operation == "add":
            return 0
        if operation == "multiply":
            return 1
        return 0

    return functools.reduce(op, spells)

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment, power=50, element="fire"),
        'ice_enchant': functools.partial(base_enchantment, power=50, element="ice"),
        'lightning_enchant': functools.partial(base_enchantment, power=50, element="lightning")
    }

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatcher(arg):
        return "Unknown spell type"
    @dispatcher.register(int)
    def _(arg):
        return f"Dealing {arg} damage"
    @dispatcher.register(str)
    def _(arg):
        return f"Enchanting with {arg}"
    @dispatcher.register(list)
    def _(arg):
        return f"Casting multiple spells: {len(arg)} spells"
    return dispatcher

def main() -> None:
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([20, 30, 40, 10], 'multiply')}")
    print(f"Max: {spell_reducer([10, 20, 40, 30], 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    
    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(100))
    print(dispatch("Invisibility"))
    print(dispatch(["Fireball", "Frostbolt"]))

if __name__ == "__main__":
    main()
