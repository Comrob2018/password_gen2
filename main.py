#Password generator that accepts command line input. Developed by Robert Hendrickson.
from random import randint
import sys
import argparse

chars='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ000111222333444555666777888999__..--@@##$$!!&%&**%'
keychars='ABCDEFGHIJKLMNOPQRSTUVWXYZ00112233445566778899'

def pword_gen(length):
    global pword
    pword=''
    while len(pword)<length:
        if specials and numbers:
            pword+=chars[randint(0,101)]
        elif not specials and numbers:
            pword+=chars[randint(0,81)]
        else:
            pword+=chars[randint(0,51)]
    return pword

def multi_pass(filename, amount, length):
    pwordlist=[]
    count=0
    pwordfile=open(filename, 'w')    
    while count<amount:
        pword_gen(length)
        pwordlist.append(pword)
        count+=1
    pwordfile.write(str(pwordlist))
    pwordfile.close()
    return "Passwords have been generated, check the file labeled " + filename

def multi_key(filename, amount, length):
    keylist=[]
    count=0  
    keyfile=open(filename, 'w')
    while count<=amount:
        key=''    
        while len(key)<=length:
            key+=keychars[randint(0,45)]
        keylist.append(key)
        count+=1
    keyfile.write(str(keylist))    
    keyfile.close()
    return "Your keys have been generated, check the file labeled "+filename

def multi_pin(filename, amount, length):
    pinlist=[]
    count=0
    pinfile=open(filename, 'w')
    while count<amount:
        pin=''
        while len(pin)<=length:
            pin+=str(randint(0,9))
        pinlist.append(pin)
        count+=1
    pinfile.write(str(pinlist))
    pinfile.close()
    return "Your pins have been generated, check the file labeled "+filename
  
def main():
    global length
    global amount
    global numbers
    global specials
    global filename
    length=''
    amount=''
    numbers=''
    specials=''
    filename=''
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--amount", help="Amount of passwords/code keys/PINs you wish to generate", action='store', required=True)
    parser.add_argument("-l", "--length", help="Length of the password/code key/PIN", action='store', required=True)
    parser.add_argument("-f", "--filename", help="Name of the output file", action='store', required=True)
    parser.add_argument("-n", "--numbers", help="Password requires numbers", action='store_true')
    parser.add_argument("-s", "--specials", help="Password requires special characters", action='store_true')
    parser.add_argument("-P", "--Password", help="Generate a password", action='store_true')
    parser.add_argument("-K", "--CodeKey", help="Generate a Code key", action='store_true')
    parser.add_argument("-PIN", "--PIN", help="Generate a numeric pin", action='store_true')
    
    args=parser.parse_args()
    length = int(args.length)
    amount = int(args.amount)
    filename = str(args.filename)
    specials = bool(args.specials)
    numbers = bool(args.numbers)
    
    if True == args.Password:
        print(multi_pass(filename, amount, length))
    elif True == args.CodeKey:
        print(multi_key(filename, amount, length))
    elif True == args.PIN:
        print(multi_pin(filename, amount, length))
    else:
        print('Error: You must include the -P, -K, or -PIN option.')
 
if __name__=='__main__':
    main()
    
