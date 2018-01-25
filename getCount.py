def getCount(inputStr):
    num_vowels = 0

    #casefold makes string case insensitive ;)
    inputStr = inputStr.casefold()

    #add 1 each time u find vowel in inputStr
    num_vowels = sum(1 for let in inputStr if let in "aeiou")

    print(num_vowels)
    return num_vowels

if __name__ == '__main__':
    getCount("aabracadabraii")