#Password generator that accepts command line input. Developed by Robert Hendrickson.
from random import randint
import sys
import argparse

chars='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ000111222333444555666777888999__..--@@##$$!!&%&**%'
keychars='ABCDEFGHIJKLMNOPQRSTUVWXYZ00112233445566778899__..--@@##$$!!&%&**%'
lowchars='abcdefghijklmnopqrstuvwxyz00112233445566778899__..--@@$$##!!&%&**%'

def pword_gen(length, complexity):
    pword = ''
    while len(pword) < length:
        if complexity == '1111': #all
            pword += chars[randint(0,101)]
        elif complexity == '0111': #numbers lowers and uppers
            pword += chars[randint(0,81)]
        elif complexity =='1101': #specials numbers and uppers
            pword += keychars[randint(0,65)]
        elif complexity == '1110': #specials numbers and lowers
            pword += lowchars[randint(0,65)]
        elif complexity == '0101': #numbers and uppers
            pword += keychars[randint(0,45)]
        elif complexity == '0110': #numbers and lowers
            pword += lowchars[randint(0,45)]
        else:
            print("Error: You have not selected any password complexity requirements.")
            sys.exit()
    return pword

def multi_pass(filename, amount, length, complexity):
    pwordlist = []
    count = 0
    while count < amount:
        pword = pword_gen(length, complexity)
        pwordlist.append(pword)
        count += 1
    pwordfile = open(filename, 'w')
    pwordfile.write(str(pwordlist))
    pwordfile.close()
    return "Passwords have been generated, check the file labeled " + filename

def multi_key(filename, amount, length):
    keylist=[]
    count=0
    while count<amount:
        key=''
        while len(key) < length:
            key+=keychars[randint(0,45)]
        keylist.append(key)
        count+=1
    keyfile=open(filename, 'w')
    keyfile.write(str(keylist))
    keyfile.close()
    return "Code keys have been generated, check the file labeled "+filename

def multi_pin(filename, amount, length):
    pinlist=[]
    count=0
    while count<amount:
        pin=''
        while len(pin) < length:
            pin+=str(randint(0,9))
        pinlist.append(pin)
        count+=1
    pinfile=open(filename, 'w')
    pinfile.write(str(pinlist))
    pinfile.close()
    return "PINs have been generated, check the file labeled "+filename    
    
def main():    

    parser = argparse.ArgumentParser()
    ReqArgs = parser.add_argument_group('required arguments')
    ReqArgs.add_argument("-A", "--Amount", help="Amount of passwords/code keys/PINs to generate.", action='store', required=True)
    ReqArgs.add_argument("-L", "--Length", help="Length of each password/code key/PIN generated.", action='store', required=True)
    ReqArgs.add_argument("-F", "--Filename", help="Name of the output file.", action='store', required=True)
    SecCodeType = parser.add_argument_group('type of security code')
    SecCodeType.add_argument("-P", "--Password", help="Generate a password", action='store_true')
    SecCodeType.add_argument("-K", "--CodeKey", help="Generate a code key", action='store_true')
    SecCodeType.add_argument("-PIN", "--PIN", help="Generate a numeric pin", action='store_true')
    PwordReqs = parser.add_argument_group('requirements for password complexity')
    PwordReqs.add_argument("-n", "--numbers", help="Password requires numbers", action='store_true')
    PwordReqs.add_argument("-s", "--specials", help="Password requires special characters", action='store_true')
    PwordReqs.add_argument("-l", "--lowercase", help="Password requires lowercase characters", action="store_true")
    PwordReqs.add_argument("-u", "--uppercase", help="Password requires uppercase characters", action="store_true")
    
    args=parser.parse_args()
    length = int(args.Length)
    amount = int(args.Amount)
    filename = str(args.Filename)
    specials = bool(args.specials)
    numbers = bool(args.numbers)
    uppers = bool(args.uppercase)
    lowers = bool(args.lowercase)
    Password = bool(args.Password)
    CodeKey = bool(args.CodeKey)
    PIN = bool(args.PIN)
    complexity = ''
    
    if specials == True:
        complexity += '1'
    else:
        complexity += '0'
    if numbers == True:
        complexity += '1'
    else:
        complexity += '0'
    if lowers == True:    
        complexity += '1'
    else:
        complexity += '0'
    if uppers == True:
        complexity += '1'
    else:
        complexity += '0'
    
    if Password and not CodeKey and not PIN:
        print(multi_pass(filename, amount, length, complexity))
    elif CodeKey and not Password and not PIN:
        print(multi_key(filename, amount, length))
    elif PIN and not Password and not CodeKey:
        print(multi_pin(filename, amount, length))
    else:
        print('Error: You must use one -P, -K, or -PIN option. Only one option will be accepted.')
        
if __name__=='__main__':
    main()
