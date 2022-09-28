#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:29:00 2022

@author: milouchev
"""

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
letters_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=.,/|\<>{}[]~:;"
letters_numbers_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=.,/|\<>{}[]~:;"


while 1:
    try:
        length_fixed = int(input("Enter the character length of your desired password: "))
    except:
        print("\nPlease enter the length as an integer.")
        length_fixed = int(input("Enter the character length of your desired password: "))
    numbers = str(input("Do you want to include numbers? If yes, enter 'yes'. If no, enter 'no':  "))
    symbols = str(input("Do you want to include symbols? If yes, enter 'yes'. If no, enter 'no':  "))
    password = ""
    if numbers == 'yes' and symbols == 'yes':
        for i in range(0,length_fixed):
            password_characters = random.choice(letters_numbers_symbols)
            password = password + password_characters
        print("\nHere is your randomly generated password: ", password, "\n")
    elif numbers == 'yes' and symbols == 'no':
        for i in range(0,length_fixed):
            password_characters = random.choice(letters_numbers)
            password = password + password_characters
        print("\nHere is your randomly generated password: ", password, "\n")
    elif numbers == 'no' and symbols == 'yes':
        for i in range(0,length_fixed):
            password_character = random.choice(letters_symbols)
            password = password + password_character
        print("\nHere is your randomly generated password: ", password, "\n")    
    elif numbers == 'no' and symbols == 'no':
        for i in range(0,length_fixed):
            password_character = random.choice(letters)
            password = password + password_character
        print("\nHere is your randomly generated password: ", password, "\n")
    else:
        print("\nError in selection for numbers and/or symbols. Enter 'yes' or 'no' to answer. Please try again.")