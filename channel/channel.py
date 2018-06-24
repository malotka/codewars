import re
import zipfile
import string

if __name__ == '__main__':

    pattern = re.compile("Next nothing is (\d+)")
    """
    with open('channel\\readme.txt') as readme:
        whattodo = readme.read()
        print(whattodo)
    """
    num = '90052'

    result = ''
    while True:

        with open('channel\\{}.txt'.format(num)) as numbers:
            data = numbers.read()
            print(data)
            match = pattern.search(data)

            if match is None:
                break
            num = match.group(1)

    zf = zipfile.ZipFile('channel.zip')
    for info in zf.infolist():
        print(info)
        print(info.comment)
        print(info.filename)

    print(result)




