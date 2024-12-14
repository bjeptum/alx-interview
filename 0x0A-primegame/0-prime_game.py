#!/usr/bin/python3
"""
Find winner module.
"""


def isWinner(x, nums):
    """
    Determines which player wins the most rounds in a game
    """
    if x <= 0:
        return None

    MAX_N = 10000
    sieve = [True] * (MAX_N + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(MAX_N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, MAX_N + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, MAX_N + 1) if sieve[i]]

    maria = 0
    ben = 0

    for n in nums:
        if n <= 1:
            ben += 1
            continue

        nums_set = set(range(1, n + 1))

        # Turn-based game simulation
        turn = 0
        while True:
            prime_found = None
            for prime in primes:
                if prime > n:
                    break
                if prime in nums_set:
                    prime_found = prime
                    break

            if prime_found is None:
                if turn == 0:
                    ben += 1
                else:
                    maria += 1
                break

            nums_set -= set(range(prime_found, n + 1, prime_found))

            # Switch turn
            turn = 1 - turn

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
