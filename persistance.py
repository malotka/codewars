def persistence(n):
    c = 0
    list = [int(i) for i in str(n)]
    if n:
        while len(list) > 1:
            multiplied = 1
            for y in list:
                multiplied *= y
            list = [int(i) for i in str(multiplied)]
            c += 1
    return c



if __name__ == "__main__":
    persistence(23445)