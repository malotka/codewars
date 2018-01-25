def add_binary(a, b):
    #done without method bin
    result = a + b
    l = []
    while result > 0:
        mod = result % 2
        l.append(mod)
        result = result // 2

    l.reverse()
    value = ''.join(str(el) for el in l)
    print(value)
    return value

def add_binary_method(a, b):
    print(bin(a + b)[2:])
    return bin(a + b)[2:]

if __name__ == '__main__':

    add_binary(1,1)
    add_binary_method(1,1)