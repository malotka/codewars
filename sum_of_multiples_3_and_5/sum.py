def find_sum(n):
    result = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result

#refactored:
def better_sum(n):
    return sum(n for n in range(1, n) if n % 3 == 0 or n % 5 == 0)

if __name__ == "__main__":

 find_sum(5)
 better_sum(5)