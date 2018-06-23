import pickle

if __name__ == '__main__':
    with open('banner.p', 'rb') as pickle_file:
        content = pickle.load(pickle_file)


        print(content)

