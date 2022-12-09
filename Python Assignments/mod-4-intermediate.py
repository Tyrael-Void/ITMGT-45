'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
       # declare list
    ltr_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    if letter in ltr_list:  # conditional to evaluate if input ⊆ list
        idx = ltr_list.index(letter)  # contain index

        # position letter as first element in list
        x = 0
        while x < idx:
            ltr_list.insert(len(ltr_list), ltr_list.pop(0))
            x += 1

        # shift letter in list
        y = 0
        while y < shift:
            ltr_list.insert(len(ltr_list), ltr_list.pop(0))
            y += 1

        return ltr_list[0]

    if letter == " ":  # conditional if " " is the input
        return " "

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def caesar_cipher(message, shift):
    msg_list = [ch for ch in (message * 2)]  # list comprehension to generate list
    
    # apply rules for shifting letters in list
    x = 0
    while x < shift:
        msg_list.insert(0, msg_list.pop())
        x += 1

    return msg_list

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == ' ':
        return (chr(32))
    elif ord(letter) + (ord(letter_shift)-65) >=90:
        return (chr((ord(letter_shift)-65) + (ord(letter)-65)%26+65))
    else:
        return (chr(ord(letter)+(ord(letter_shift)-65)))

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    finalMessage = ""
    numberShift = 0
    if len(key) % len(message) == 0:
        VKey = key * (len(message)//len(key))
    else:
        VKey = key * (len(message)//len(key)) + key[:(len(message) % len(key))]
        
    for letter in message:
        if letter != " ":
            finalLetter = ord(letter) + (ord(VKey[numberShift]) - 65)
            if finalLetter > 90:
                finalLetter -= 26
        else:
            finalLetter = ord(letter)
        space = chr(finalLetter)
        finalMessage += space
        numberShift += 1
    return(finalMessage)
