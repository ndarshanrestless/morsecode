#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import ipdb
import sys

# for developer additional tracing 
debug = False
english_to_morse_lookup_table ={
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '0':'-----',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    ' ':'/'
}
morse_to_english_lookup_table = {v: k for k, v in english_to_morse_lookup_table.items()}


# Meat of the conversion logic is here
def convert_to_english(input_morse_code=None):
    """
    Abstract: Converts the input morse-code to english string
             (prints and returns the converted string)
    input: more encode string
    Returns: None
    Error: If one of the the input morse code does not match to a valid lookup
           of the morse to english lookup dictionary then that will be error
    """
    outlist = []
    try:
        for each in input_morse_code.split():
            english_alphabet = morse_to_english_lookup_table.get(each, None)
            if english_alphabet is None:
                assert False, ("At the index:{} the alphabet:{} is not a"
                               " valid english alphabet".format(each))
            else:
                outlist.append(english_alphabet)
    except Exception as err:
        print "Invalid morse input:{}".format(input_morse_code)
        if debug is True:
            print "Error: {}".format(err)
        return

    ret_english_string = ''.join(outlist)
    print "The Equivalent english is:{}".format(ret_english_string)
    return ret_english_string


if __name__ == '__main__':
    # enforce the program is used the way it is intended t0
    if len(sys.argv) != 2:
        print("Error below is a example of how to use this:\n"
              "python morse_to_english.py \".. / .-.. --- ...- . /"
              ".. -. -.. .. .- -... --- ..- .-.. . ...- .- .-. -..\" "
              "\n Note that letters are seperated by space and words by /")
    else:
        # If arguments check passed let's extract input & call helper func
        input_morse_code = sys.argv[1]
        convert_to_english(input_morse_code)


'''
Tests todo: 
Need unit tests with soem of these and more scenarios
-> +ve test: valid morse code
-> empty morse code
-> Only '/' in the code
-> invalid morse code
-> single string with both invalid and valid morse code
-> alphabet in teh morse code
-> really huge input morse code which when read one shot into the program memoory can 
   cause bad things(OOM, hang, swapping and tracshing etc), so to avoid that one
   simple fix is to have a upper limit of how
   big the input can be. However a fancier solution is to read parts of the files 
   off disk and write output to disk.
'''
