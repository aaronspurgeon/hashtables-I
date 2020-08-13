import re
from functools import reduce


def no_dups(s):
    # Your code here
    new_arr = re.sub("[^\w]", " ",  s).split()
    hash_table = {}

    for i in new_arr:
        if i not in hash_table:
            hash_table[i] = 1

    return ' '.join(list(hash_table))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
