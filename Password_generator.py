""" 
A lot of improvements can be done for examples we can check whether the input is a number or not, so we can use try and except.
"""


import string
import random


alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
number = []
for i in range(0,10):
    number.append(str(i))

symbols = ['!','@','#','$','%','^','&','*','(',')']





def user_input():
    alphabet_total= int(input("How many alphabets do you want? "))
    while True:
        alpha_lower=int(input("How many alphabets do you want in lowercase"))
        if alpha_lower>alphabet_total:
            raise Exception("Lowercase alphabet is more than the total alphabet")
        else:
            break
    
    alpha_upper= alphabet_total-alpha_lower
    password_num= int(input("How many numbers do you want it ?"))
    password_symbols= int(input("How many symbols do you want it ?"))

    return alpha_lower, alpha_upper, password_num, password_symbols


def welcome_page():
    print(''' 

 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒      ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░             ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
                                                                 ░                                                                                       

    
    ''')


def computation( alpha_lower, alpha_upper, password_num, password_symbols):
    password= ""
    if alpha_lower>0:
        for _ in range(alpha_lower):
            t=random.choice(alphabet_lower)
            password +=t
    if alpha_upper>0:
        for _ in range(alpha_upper):
            t=random.choice(alphabet_upper)
            password +=t
    if password_symbols>0:
        for _ in range(password_symbols):
            t=random.choice(symbols)
            password +=t
    if password_num>0:
        for _ in range(password_num):
            t=random.choice(number)
            password +=t
    return password

def shuffling_password(password):
    password= random.sample(password,len(password))

    final_password=""
    
    for i in password:
        final_password +=i
    print(final_password)
    


def main():
    welcome_page()
    alpha_lower, alpha_upper, password_num, password_symbols=  user_input()
    password= computation(alpha_lower, alpha_upper, password_num, password_symbols)
    shuffling_password(password)
    
    
   
        

main()