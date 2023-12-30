#!/usr/bin/env python3
# coding: utf-8
import random

# Defining character sets  
basic_lowercase = 'abcdefghijklmnopqrstuvwxyz'
special_char='!@#$%^&*()_+'
digits= '0123456789'
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
#adding the various inclusions to  make the password
#this is based on the users input. Defaul is false
def password_combinations(upper, numbers, specialChr):
    combo = basic_lowercase
    if numbers:
        print('numbers= ', numbers)
        combo += digits
    if specialChr:
        print('specialChar= ', special_char)
        combo += special_char
    if upper:
        print('upper= ', upper)
        combo += upper_case
    return combo

#using randomchoice based on the length of the password
def generate_password(length=20, upper= False, num =False, specialC = False ):
    password=[]
    combo_p = password_combinations(upper, num, specialC)
    for l in range(length):
        pword = random.choice(combo_p) #choosing characters from the combined set
        password.append(pword) 
    return ''.join(password)

#Prompting the users with the following questions about how the password should be
def password_gen_questions():
    while True:
        try:
            p_len = int(input('Provide password length: Minimum of 8:   '))
            if p_len < 8: 
                print("Password length not long enough, try again: ")
            else:
                user_upper_letter = input('Use uppercase letters? (y/n): ').lower().strip() =='y'
                user_digits=  input('Use digits? (y/n): ').lower().strip()=='y'
                user_special_chr = input('Use special characters? (y/n): ').lower().strip()=='y'
                gen_password= generate_password(p_len,  user_upper_letter,  user_digits,  user_special_chr)
                print('\n', 'Generated Password', gen_password , '\n')
                break
        except:
            print("Not a valid response")

##Main menu runs indefinitely until user exits by entering "2"
def mainmenu():
    while True:
        print('---- Password generator --\n', 'Choose Option:')
        print(' 1 to generate pasword\n', '2 to exit the program')
        user_input = input('Your choice: ')
        if user_input == '2':
            print('Bye!')
            break
        elif user_input == '1':
            password_gen_questions()
        else:
            print('Please enter a correct value, either 1 0r 2')
    
if __name__ == "__main__":
    mainmenu()


