def reverse_words(str):
    print(str)
    #using indexing - slicing method, not what we want, we want WORDS reversed not entire sentence:
    #print(str[::-1])


    new_str = ""
    new_str = "".join([new_str + word + " " for word in [word[::-1] for word in str.split(" ")]]).rstrip(" ")
    print(new_str)
    return new_str

if __name__ == '__main__':
    reverse_words('This  is an example!')