def is_prime(n, divisor=2):
    """Check if a number is prime."""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % divisor == 0:
        return False
    elif divisor * divisor > n:
        return True
    else:
        return is_prime(n, divisor + 1)

def generate_primes(start, end):
    """Generate all prime numbers within a given range [start, end]."""
    if start > end:
        return []
    elif is_prime(start):
        return [start] + generate_primes(start + 1, end)
    else:
        return generate_primes(start + 1, end)

# Example usage:
start_range = 2
end_range = 50

print("Prime numbers between", start_range, "and", end_range, "are:")
print(generate_primes(start_range, end_range))
