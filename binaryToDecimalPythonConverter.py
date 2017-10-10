#Bin-Dec
#
#This program converts numbers decimal to binary and binary to decimal;
#Originally ideated by
#
#<francesco iulio>
#<fri0039@my.londonmet.ac.uk>
#10th October 2017
#

import os
import platform
import time
import sys
platform = platform.system()
print 'Serving',platform

def dec2bin():
    #Converts any prompted decimal number to binary
    decimal = input('Insert a decimal number:')
    binary = [""]
    counter = 0
    while decimal != 0:
        counter = counter+1
        remainder = decimal%2        
        decimal = decimal/2
        binary.append(remainder)
    for i in  binary:
        print binary[counter],
        counter = counter-1
    print

def bin2dec():
    #Converts any prompted binary number to decimal
    result = 0
    binary = raw_input('Insert a binary number:')
    length = len(binary)
    for digit in binary:
        if (digit == '0' or digit == '1'):
            weight = 2**(length-1)   
            position = (int(digit)*weight)
            result = result + position
            length = length-1
        else:
            print 'not a binary number'
            result = 'result not valid'
            break
    print result
        
    
    
    
    
    
#Main part of the conversion program

def main():   
    banner();
    print '|',
    time.sleep(0.5)
    for i in xrange(35):
        time.sleep(0.07)
        print '>',
    print ' LOADED!'
    print
    time.sleep(0.9)    
    Choice = 'Y'
    while Choice == 'Y':
        Select = input('Select:\n  1-- binary to decimal;\n  2-- decimal to binary;\n  3-- exit\n:> ')
        if Select == 1:
            if platform == 'Windows':
                os.system('cls')  # clears the screen if windows   ...         
                bin2dec();
            elif platform == 'Linux':
                os.system('clear')  # ...    or Linux            
                bin2dec();    
            else:
                bin2dec();
                print
        elif Select ==2:
            if platform == 'Windows':
                os.system('cls')            
                dec2bin(); 
            elif platform == 'Linux':
                os.system('clear')           
                dec2bin(); 
            else:
                dec2bin(); 
                print   
        elif Select ==3:
            banner();
            exit();
        else:
            print 'wrong selection...\n'
        yourChoice = raw_input('Do you want to continue? [Y/n]')
        if (yourChoice == 'N' or yourChoice == 'n'):
            print 'Exiting...'
            print '\n'*10
            banner();
            Choice = ''
        else:
            Choice = 'Y'
#Function that clears the screen and show just the banner for 2 seconds.
def banner():
    if platform == 'Windows':
        time.sleep(2)
        os.system('cls')           
    elif platform == 'Linux':
        time.sleep(2)
        os.system('clear')         
    else:
        print
        
    print' _________ _________     __         __       ____    ______  _____  '
    print'|___   ___|    |    \   |  |>>>>>  /<<\ <<<<|    \  |      |/_ ___|  '
    print'|___   ___|    |     \  |  |>>>>  />>>>\ <<<|     \ |   ___|__/    '
    print'|____ ___/|    |      \_|  |>>>  /<<<<<<\ <<|      \|  |__/__/'
    print'|___   _/ |    |           |>>  |>>>>>>>>| <|       |   __|__\    '
    print'|___   _\ |    |    |\     |>>>  \<<<<<</ <<|      /|  |___\__\___'
    print'|____ ___\|    |    | \    |>>>>  \>>>>/ <<<|     / |      |\_____|'
    print'|________/|____|____|  \___|>>>>>  \==/ <<<<|____/  |______| \____| '   
    print
    time.sleep(2)

    


main();