import random
import string

def rdm_char_dig_sym(string_length=6):
    """Generate a random string of letters, digits and
    special characters """

    pass_char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(pass_char) for i in range(string_length))

print("Generating Random String password with letters, digits and special characters")

print("First Random String ", rdm_char_dig_sym())
print("Second Random String ", rdm_char_dig_sym(6))
