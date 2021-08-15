import string
import random

def generate():
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
    str1 += ''.join((random.choice(string.digits) for x in range(10)))

    sam_list = list(str1)  # it converts the string to list.
    random.shuffle(sam_list)  # It uses a random.shuffle() function to shuffle the string.
    final_string = ''.join(sam_list)

    return final_string