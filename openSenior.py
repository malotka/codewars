def openOrSenior(data):

    return ["Senior" if i[0] >= 55 and i[1] > 7 else "Open" for i in data]

if __name__ == '__main__':

    openOrSenior([[3, 12], [55, 1], [91, -2], [54, 23]])
   