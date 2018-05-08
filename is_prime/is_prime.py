def is_prime(num):
    if type(num) == int:

        if num <= 1:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            else:
                return True
    else:
        return False
