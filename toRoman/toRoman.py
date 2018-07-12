def to_roman(num):
    result = ''

    roman_dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    if type(num) != int:
        return 'Error'

    if num < 1:
        return 'Less than 1!'

    if num > 3999:
        return 'More than 3999!'

    while num > 0:
        for key in roman_dict:
            if num >= key:
                result = result + roman_dict[key]
                num = num - key

                break

    return result


