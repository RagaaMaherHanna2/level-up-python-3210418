
def get_prime_factor(num):
    prime_factors = []
    primes = [2, 3, 5, 7]
    while num > 1:
        for prime in primes:
            if num % prime == 0:
                prime_factors.append(prime)
                num = num / prime
                break

    return prime_factors


if __name__ == '__main__':
    print(get_prime_factor(60))