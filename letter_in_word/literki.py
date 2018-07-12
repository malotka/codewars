def contains(word, letter):


    if type(letter) == str:
        word = word.lower()
        letter = letter.lower()
        if len(letter) == 1:
            for i in word:
                if i == letter:
                    return True
                else:
                    return False
        else:
            raise ValueError()
    else:
        raise ValueError()

