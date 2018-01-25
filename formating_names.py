def namelist(names):
    
    """step 1: for po zakresie calej listy names i append do listy
       step 2: if przedostatnie imie w liscie dodaj " & " po imieniu w stringu
       step 3: elif ostatnie imie - nie dodawaj przecinka po imieniu
       step 4: else: dodaj imie do stringa + ', '"""

    # dictionaries:
    # names[0] = {'name': 'Bart'} - dictionary
    # names[0]['name'] = 'Bart' - how to get to value

    l = []

    for i in range(len(names)):
       l.append(names[i]['name'])

    str = ''

    for j in range(len(l)):

        if j == len(l) - 1:
            str = str + l[j]
        elif j == len(l) - 2:
            str = str + l[j] + " & "
        else:
            str = str + l[j] + ", "


    print(str)
    return str


    #for j in range(len(l)):


if __name__ == '__main__':

    names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]

    namelist(names)