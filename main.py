from random import randint
import sys
import getopt

def multi_pass(amount,length):
    global pwordlist
    pwordlist=[['Website','Username','Password']]
    count=0
    pwordfile=open('Passwords.csv', 'w')    
    while count<amount:
        pword2=''
        getPurpose()
        getUserName()
        pword2+=purpose+','+uName+','
        pword_gen(length)
        pword2+=pword
        pwordlist.append(pword2.split(','))
        count+=1
    writer=csv.writer(pwordfile, dialect='pDialect')
    for row in pwordlist:
        writer.writerow(row)
    pwordfile.close()
    return "Passwords have been generated, check the file labeled Passwords.csv"

def multi_key(amount,length):
    keylist=[['Purpose', 'Key']]
    count=0
    keyfile=open('Keys.csv', 'w')
    while count<amount:
        key2=''
        getPurpose()
        key2+=purpose+','
        kgen(length)
        key2+=key
        keylist.append(key2.split(','))
        count += 1
    writer=csv.writer(keyfile, dialect='pDialect')            
    for row in keylist:
        writer.writerow(row)
    keyfile.close()
    return "Your keys have been generated, check the file labeled Keylist.txt"


    
def main(argv):
    
