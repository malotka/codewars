def is_prime(num):

    if num <= 1:
        return False
    elif num <= 3:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True