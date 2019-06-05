#Password generator that accepts command line input. Developed by Robert Hendrickson.
from random import randint
import sys
import argparse
import textwrap

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

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    ReqArgs = parser.add_argument_group('required arguments')
    ReqArgs.add_argument("-A", "--Amount", help="Amount of passwords/code keys/PINs to generate.", action='store', required=True)
    ReqArgs.add_argument("-L", "--Length", help="Length of each password/code key/PIN generated.", action='store', required=True)
    ReqArgs.add_argument("-F", "--Filename", help="Name of the output file.", action='store', required=True)
    ReqArgs.add_argument("-T ", "--Type", choices=['P', 'K', 'PIN'], help='''\
    P to generate a Password, 
    K to generate a Code Key, 
    PIN to generate a PIN.
    ''', action='store')
    PwordReqs = parser.add_argument_group('password complexity requirements')
    PwordReqs.add_argument("-n", "--numbers", help="Password requires numbers", action='store_true')
    PwordReqs.add_argument("-s", "--specials", help="Password requires special characters", action='store_true')
    PwordReqs.add_argument("-l", "--lowercase", help="Password requires lowercase characters", action="store_true")
    PwordReqs.add_argument("-u", "--uppercase", help="Password requires uppercase characters", action="store_true")
    
    args=parser.parse_args()
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
    
    if str(args.Type) == 'P':
        print(multi_pass(args.Filename, int(args.Amount), int(args.Length), complexity))
    elif str(args.Type) == "K":    
        print(multi_key(args.Filename, int(args.Amount), int(args.Length)))
    elif str(args.Type) == "PIN":
        print(multi_pin(args.Filename, int(args.Amount), int(args.Length)))
    else:
        print('Error: You must use -T with one P, K, or PIN option.')
        
if __name__=='__main__':
    main()
