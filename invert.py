def invert(lst):
    """ Given a set of numbers, return the additive inverse of each.
    Each positive becomes negatives, and the negatives become positives. """
    inverted = [0 - x for x in lst]
    print(inverted)
    return inverted

if __name__ == '__main__':

    invert([1, -2, 3, -4, 5])
