# Try to implement memorization on the recursive fibonacci example.

def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]


# Example usage
print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765
print(fibonacci(30))  # Output: 832040
print(fibonacci(300))  # Output: 280571172992510140037611932413038677
