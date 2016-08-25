import string
def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    letterMapping = {}
    #letters = string.ascii_lowercase + string.ascii_uppercase
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    lowercase_mapping = ''
    #for letter in letters:
    #    letterMapping[letter] = letters[letters.index(letter)-52+shift]
    for letter in lowercase:
        letterMapping[letter] = lowercase[lowercase.index(letter)-26+shift]
    for letter in uppercase:
        letterMapping[letter] = uppercase[uppercase.index(letter)-26+shift]
    return letterMapping
    '''
    abcdefghijklmnopqrstuvwxyz
    cdefghijklmnopqrstuvwxyzab
    '''
def apply_shift(message, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    letterMapping = build_shift_dict(shift)
    shifted_message = ''
    for char in message:
        if char == ' ' or char in string.digits:
            shifted_message += char
        else:
            shifted_message += letterMapping[char]
    return shifted_message



print build_shift_dict(2)
#print apply_shift('hello', 2)
#print string.digits