from random import randint
import sys
import argparse

chars='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ000111222333444555666777888999__..--@@##$$!!&%&**%'

def pword_gen(length):
    global pword
    pword=''
    while len(pword)<length:
        if specials=='y'and numbers=='y':
            pword+=chars[randint(0,101)]
        elif specials!='y' and numbers=='y':
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
    parser.add_argument("-a", "--amount", help="the amount of passwords you wish to generate", action='store')
    parser.add_argument("-l", "--length", help="the length of the password", action='store')
    parser.add_argument("-f", "--filename", help="the name of the output file", action='store')
    parser.add_argument("-n", "--numbers", help="your password requires numbers", action='store_true')
    parser.add_argument("-s", "--specials", help="your password requires special characters", action='store_true')
    
    args=parser.parse_args()
    print(args.length)
    length = int(args.length)
    amount = int(args.amount)
    filename = str(args.filename)
    if True == args.specials:
        specials = 'y'
    if True == args.numbers:
        numbers = 'y'
    
    print(multi_pass(filename, amount, length))
 
if __name__=='__main__':
    main()
    
