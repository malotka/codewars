if __name__ == '__main__':

    """You have an array of numbers
    Your task is to sort ascending odd numbers but even numbers must be on their places.
    Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it."""

    n = [5, 3, 2, 8, 1, 4]
    print("list to sort: ", n)
    #save odd numbers and sort then ascending
    odd_num = sorted([num for num in n if num % 2 != 0])
    print("list of odd numbers: ", odd_num)

    #in n change %2!=0 for nums from odd_num
    init = 0
    for i in range(len(n)):
        if n[i] % 2 != 0:
            n[i] = odd_num[init]
            init += 1

    print("Sorted: ", n)
