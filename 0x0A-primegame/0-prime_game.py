#!/usr/bin/python3
"""
 0. Prime Game
----------------
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    """

    def sieve(n):
        """
        Generate an array with True (prime) and False (composite)
        up to n using the Sieve of Eratosthenes algorithm.
        """
        prime = [True] * (n + 1)
        # 0 and 1 are not prime numbers
        prime[0] = prime[1] = False

        # Iterate over numbers from 2 to sqrt(n)
        # if n = 16, i = (2, 4) => 2^2= 4, 3^2 = 9, 4^2=16
        # Mark all multiples of i as False (composite)
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):  # Start marking from i^2
                    prime[j] = False
        return prime

    # Handle edge cases where no game can be played
    if not nums or x <= 0:
        return None

    # Precompute primes up to the largest number in nums
    max_n = max(nums)
    primes = sieve(max_n)

    # Prepare a list to count the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        # Add 1 to the count if the current number is prime
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Initialize win counts for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play the game for each number in nums
    # Maria wins if the number of primes is odd; Ben wins if even
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
