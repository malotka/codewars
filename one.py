def wypelnij_liste_for(s):
    l = []
    for letter in s:
        l.append(letter)
    print(l)

def wypelnij_liste_comprahention(s):
    l = [letter for letter in s]
    print(l)

def kalk_cels_faht(c):
    print("celcius to fahrenheit")

    fahrenheit = (c * 1.8 + 32)
    print(c, "Celsius is ", fahrenheit, " Fahrenheit")

if __name__ == '__main__':
    print("Hello, World!")

    #wypełnienie listy:
    wypelnij_liste_for("hello world")

    #lepszy sposób - list comprahention:
    wypelnij_liste_comprahention("Franciszek")

    #kalk celcius to fahrenheit
    kalk_cels_faht(0)


    print("Use for, split(), and if to create a Statement that will print out words that start with 's':")
    st = 'Print only the words that start with s in this sentence'

    for word in st.split(" "):
        if word.capitalize().startswith("S"):
            print(word)

    print("Use range() to print all the even numbers from 0 to 10.")
    for x in range(0,11,2):
        print(x)

    print("Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.")
    xyz = [num for num in range(1, 51) if num % 3 == 0]
    print(xyz)

    print("Go through the string below and if the length of a word is even print 'even!'")
    str = 'Print every word in this sentence that has an even number of letters'
    for x in str.split(" "):
        if (len(x) % 2 == 0):
            print(x, "even!")

    print("Write a program that prints the integers from 1 to 100. But for multiples of three print 'Fizz' instead of the number, and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'.")

    for num in [num for num in range(1, 101)]:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

    print("Use List Comprehension to create a list of the first letters of every word in the string below")
    stri = 'Create a list of the first letters of every word in this string'

    print([letter[0][:1] for letter in stri.split(" ")])

