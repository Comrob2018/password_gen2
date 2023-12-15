# Password Generator version 2

## Password generator for python that allows for command line arguments.

Usage: passgen.py -a ## -f someFile.txt -l ## -K/-P/-PIN -n -s

-a amount of passwords/keys/pins you wish to generate

-f output filename, the name of the file that the program will generate with the passwords in it

-l length of passwords/keys/pins you wish to generate

 Only one of the following three will be accepted:
 
 -K generate a code key (i.e. CD key);
 -P generate a password;
 -N generate a numeric PIN

-n your password requires numbers

-s your password requires special characters
