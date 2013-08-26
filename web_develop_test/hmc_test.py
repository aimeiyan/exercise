__author__ = 'nancy'

import hmac

SECRET = 'imsosecret'


def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val


x = make_secure_val("test!!")
print check_secure_val(x)
