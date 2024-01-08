from math import sqrt


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_n_primes(number):
    primes = []
    i = 2
    while len(primes) < number:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


def main():
    pass


if __name__ == '__main__':
    main()
