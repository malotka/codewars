def is_prime(num):
    """Checks if given number is prime
    Args: num: given number
    Return: True/False
    """
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


def primes(count):
    """Lazily Generates given number of prime numbers
    Args:
        count: how many prime numbers we want
    Returns:
        Yield: next prime number until count is reached
    """
    number = 0
    counter = 0
    while counter <= count:
        if is_prime(number):
            yield number
            counter += 1
        number += 1


if __name__ == '__main__':

    d = sum(primes(1000))
    print(d)
