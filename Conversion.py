#!/usr/bin/env python

"""
Name: Brock Glatman
Date: 12/1/2017
Description:
This file will create conversion tables for the encrypt and decrypt methods of the Virgenere cipher method.
"""

# print __doc__

char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             " ", ".", ",", "!", "?",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
             ":", "/"]

def encrypt():
    """This function will create an encryption-conversion dictionary for the Virgenere cipher method."""
    # print encrypt.__doc__
    enc_dict = {}
    for letter in char_list:
        enc_dict[letter] = {}
    for key in enc_dict.keys():
        for i in range(len(char_list)):
            shift = ((i + char_list.index(key))%len(char_list))
            enc_dict[key][char_list[i]] = char_list[shift]
    return enc_dict

def decrypt():
    """This function will create an decryption-conversion dictionary for the Virgenere cipher method."""
    # print decrypt.__doc__
    dec_dict = {}
    for letter in char_list:
        dec_dict[letter] = {}
    for key in dec_dict.keys():
        for i in range(len(char_list)):
            shift = ((i - char_list.index(key))%len(char_list))
            dec_dict[key][char_list[i]] = char_list[shift]
    return dec_dict
