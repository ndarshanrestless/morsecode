#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import ipdb
import sys

morse_look_up_table ={
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
    ' ':' '} # just keep space as space


def convert_to_morse(input_string=None):
    outlist = [] 
    for index, each in enumerate(input_string):
        thecode = morse_look_up_table.get(each, None)
        if thecode is None:
            ipdb.set_trace()
            assert False, ("At the index:{} the alphabet:{} is not a"
                           " valid english alphabet".format(index, each))
        else:
            outlist.append(thecode)

    retstr = ''
    for each in outlist:
        retstr = retstr + ' ' + each
    # todo remove the trailing and startign spaces
    
    print "The Equivalent morse code is {} ".format(' '.join(outlist))
    return outlist


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error below is a example of how to use this:\n"
              "python morse_to_english.py \"India Boulevard\" ")
    else:
        input_string = sys.argv[1]
        converted_morse_code = convert_to_morse(input_string.upper())



        
'''
Todo: 
Unit and functional testing:
--> Postitive test: case of valid english sentence and numbers
--> Negative test: 
--> empty string as a input
--> Non English test
--> multiple spaces in the string
--> extremeley long string where it can be memory intensive and swap to disk!. 
Solution is to have limit on input string 
--> mixed characters of upper and lower case and number in between the string

some more fixes: 
--> If you want a two way function to get back the original string with case
    then we can achive that by keeping the casee of each character as a metadata, 
     which will be dictionary of triple 
'''
