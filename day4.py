import hashlib

def has_leading_zeroes(h, zeroes):
    return h[:zeroes] == zeroes * '0'


def mine(secret_key, zeroes = 5):
    mine_coin = True
    num = 1
    while mine_coin == True:
        string = "{0}{1}".format(secret_key, num)
        print "Hashing {0}...".format(string)
        h = hashlib.md5(string).hexdigest()
        if has_leading_zeroes(h, zeroes):
            print "Lowest number is {0} for hash {1}".format(num, h)
            mine_coin = False
        num += 1

secret_key= 'yzbqklnj'
mine(secret_key, 5)
mine(secret_key, 6)
