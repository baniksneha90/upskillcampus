import random
import string
def gen_shortcode():
    characters = string.ascii_letters + string.digits
    short_code = ""
    for i in range(6):
        short_code += random.choice(characters)
    return short_code
print(gen_shortcode())