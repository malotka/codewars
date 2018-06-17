def stx_next(num):
    if type(num) == int or type(num) == float:
        if num % 15 == 0:
            print("STXNext")
        elif num % 3 == 0:
            print("STX")
        elif num % 5 == 0:
            print("Next")
        else:
            print(num)

if __name__ == "__main__":

    for x in range(1,101):
        stx_next(x)


