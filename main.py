from random import randint
import sys
import getopt
csv.register_dialect('pDialect', delimiter='|')

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

def multi_pass(amount,length):
    pwordlist=[]
    count=0
    pwordfile=open(filename, 'w')    
    while count<amount:
        pword_gen(length)
        pwordlist.append(pword)
        count+=1
    pwordfile.write(str(pwordlist))
    pwordfile.close()
    return "Passwords have been generated, check the file labeled" + filename
  
def main(argv):
    global length
    length = ''
    global amount
    amount = ''
    global numbers
    numbers = ''
    global specials
    specials = ''
    global filename
    filename = ''
    
    try:
        opts, args = getopt.getopt(argv, "ha:f:l:ns, ["amount=","filename=","length=","numbers","specials"])
    except getopt.GetoptError:
        print('''passgen.py -a ## <amount of passwords to generate> 
                            -f <output filename> 
                            -h <help message> 
                            -l ## <character length of password> 
                            -n <password requires numbers> 
                            -s <password requires special characters>''')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('''passgen.py -a ## <amount of passwords to generate> 
                                -f <output filename> 
                                -h <help message> 
                                -l ## <character length of password> 
                                -n <password requires numbers> 
                                -s <password requires special characters>''')
            sys.exit()
        elif opt in ('-a', '--amount'):
            amount = int(arg)
        elif opt in ('-f', '--filename'):
            filename = arg
        elif opt in ('-l', '--length'):
            length = int(arg)
        elif opt in ('-n', '--numbers'):
            numbers = 'y'
        elif opt in ('s', '--specials'):
            specials = 'y'
                                   
    print(multi_pass(amount,length))
                                   
if __name__=='__main__':
    main(sys.argv[1:])
    
