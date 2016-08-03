#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import ipdb
import sys

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


def convert_to_english(input_morse_code=None):
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
    
    print "The Equivalent english is:{}".format(''.join(outlist))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error below is a example of how to use this:\n"
              "python morse_to_english.py \".. / .-.. --- ...- . /"
              ".. -. -.. .. .- -... --- ..- .-.. . ...- .- .-. -..\" "
              "\n Note that letters are seperated by space and words by /")
    else:
        input_morse_code = sys.argv[1]
        convert_to_english(input_morse_code)


'''
Tests todo:
-> +ve test: valid morse code
-> empty morse code
-> Only '/' in the code
-> invalid morse code
-> single string with both invalid and valid morse code
-> alphabet int eh morse code
'''
