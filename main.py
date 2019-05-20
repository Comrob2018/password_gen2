from random import randint
import sys
import getopt
csv.register_dialect('pDialect', delimiter='|')

def multi_pass(amount,length):
    global pwordlist
    pwordlist=[[]]
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

  
def main(argv):
    
