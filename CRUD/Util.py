import random
import string

def random_string(panjang:int)->str:
    '''Fungsi untuk generate random string'''
    hasil_string = "".join(random.choice(string.ascii_letters)for i in range(panjang))
    return hasil_string