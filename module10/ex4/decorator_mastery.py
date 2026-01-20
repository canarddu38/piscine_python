#!/usr/bin/env python3
import functools
import time
import inspect

def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = None
            sig = inspect.signature(func)
            try:
                bound = sig.bind(*args, **kwargs)
                bound.apply_defaults()
                if 'power' in bound.arguments:
                    power = bound.arguments['power']
                elif len(args) > 0 and isinstance(args[0], int):
                     power = args[0]
            except:
                pass
            
            if power is None and args:
                 if isinstance(args[0], int):
                     power = args[0]
                 elif isinstance(args[-1], int):
                     power = args[-1]

            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not name or not isinstance(name, str):
            return False
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"

def main() -> None:
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"
    
    print(fireball())
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Frost", 5))

    print("\nTesting retry_spell...")
    @retry_spell(max_attempts=3)
    def broken_spell():
        raise ValueError("Fizzle")
    
    print(broken_spell())

if __name__ == "__main__":
    main()
