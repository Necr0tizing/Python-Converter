#All to All Converter
#Author - Martin Zastrow
#Date 15/3/21
print('''
------------------------------------------------------------------
      ,  ,  _, _,,_   _,  ___,___,__, ___,,  ,  _,                
      |\ | /_,/  |_) / \,' | ' |   / ' |  |\ | / _                
      |'\|'\_'\_'| \'\_/   |  _|_,/_  _|_,|'\|'\_|`               
      '  `   `  `'  `'     ' '   '  `'    '  `  _|                
                                               '                  
        _, ,  , ___,  _,,  ,     _, _, ,  ,,   , _,,_  ___,_,,_   
       / \,|  |' |   /  |_/     /  / \,|\ |\  / /_,|_)' | /_,|_)  
      '\_X'\__| _|_,'\_'| \    '\_'\_/ |'\| \/`'\_'| \  |'\_'| \  
          `   `'       `'  `      `'   '  ` '     `'  ` '   `'  `
------------------------------------------------------------------ 
        Author - Martin Zastrow
        Date 15/3/21 
------------------------------------------------------------------                                                                                                                                                      
''')


#Starting withg taking in an int to determine the starting point of the conversion
print('''What starting type do you want to use?
1 = Dec
2 = Hex
3 = Oct
4 = Bin''')
theInputType = int(input(""))

#The switch for the initial input
def theType(i):
        switcher={
                1:'dec',
                2:'hex',
                3:'oct',
                4:'bin',
             }
        return switcher.get(i,"Invalid type use 1, 2, 3 or 4")
choice1 = theType(theInputType)

#------------------------------------------------------------------------------
#Decimal choice start
#------------------------------------------------------------------------------
#The input for the Decimal
if choice1 == 'dec':
    theInputBin = int(input('Decimal: '))
    print('''1 = Bin
2 = Hex
3 = Oct''')
#The input for the X
    theInputType = int(input("What do you want to convert to? "))
    
#Decimal to X switch 
    def theTypeBin(i):
            switcher={
                    1:'bin',
                    2:'hex',
                    3:'oct',
                 }
            return switcher.get(i,"Invalid type use 1, 2 or 3")
    choice = theTypeBin(theInputType)

#Decimal to Bin
    if choice == 'bin':
        a = bin(theInputBin)[2:]
        b = a.zfill(8)
        print(b)
        
#Decimal to Hex        
    elif choice == 'hex':
        a = hex(theInputBin)[2:]
        a = a.upper()
        print(a)
        
#Decimal to Oct
    elif choice == 'oct':
        a = oct(theInputBin)[2:]
        print(a)
        
#------------------------------------------------------------------------------
#Hex choice start
#------------------------------------------------------------------------------
#The input for the Hex
elif choice1 == 'hex':
    theInputBin = input('Hex: ')
    print('''1 = Bin
2 = Dec
3 = Oct''')
#The input for the X
    theInputType = int(input("What do you want to convert to? "))
#Hex to X switch 
    def theTypeBin(i):
            switcher={
                    1:'bin',
                    2:'dec',
                    3:'oct',
                 }
            return switcher.get(i,"Invalid type use 1, 2 or 3")
    choice = theTypeBin(theInputType)

#Hex to Bin
    if choice == 'bin':
        print(bin(int(theInputBin, 16))[2:].zfill(8))
        
#Hex to Dec        
    elif choice == 'dec':
        print(int(theInputBin, 16))
#Hex to Oct
    elif choice == 'oct':
        a = int(theInputBin, 16)
        print(oct(a)[2:])





#------------------------------------------------------------------------------
#Oct choice start
#------------------------------------------------------------------------------
#The input for the Oct
elif choice1 == 'oct':
    theInputBin = input('Oct: ')
    print('''1 = Bin
2 = Dec
3 = Hex''')
#The input for the X
    theInputType = int(input("What do you want to convert to? "))
#Oct to X switch 
    def theTypeBin(i):
            switcher={
                    1:'bin',
                    2:'dec',
                    3:'hex',
                 }
            return switcher.get(i,"Invalid type use 1, 2 or 3")
    choice = theTypeBin(theInputType)

#Oct to Bin
    if choice == 'bin':
        a = int(theInputBin, 8)
        a = bin(a)[2:]
        print(a.zfill(8))
        
#Oct to Dec        
    elif choice == 'dec':
        print(int(theInputBin, 8))
        
#Oct to Hex
    elif choice == 'hex':
        a = int(theInputBin, 8)
        a = hex(a)[2:]
        a = a.upper()
        print(a)


#------------------------------------------------------------------------------
#Bin choice start
#------------------------------------------------------------------------------
elif choice1 == 'bin':

#The input for the Bin
    theInputBin = input('Binary: ')
    print('''1 = Dec
2 = Hex
3 = Oct''')

    theInputType = int(input("What do you want to convert to? "))
#Bin to X switch 
    def theTypeBin(i):
            switcher={
                    1:'int',
                    2:'hex',
                    3:'oct',
                 }
            return switcher.get(i,"Invalid type use 1, 2 or 3")
    choice = theTypeBin(theInputType)

#Bin to Dec
    if choice == 'int':
        print(int(theInputBin, 2))
        
#Bin to Hex        
    elif choice == 'hex':
        a = hex(int(theInputBin, 2))
        a = a.upper()
        print(a[2:])
        
#Bin to Oct
    elif choice == 'oct':
        print(oct(int(theInputBin, 2)))
else:
    print('wrong choice')

input()
#------------------------------------------------------------------------------
#END
#------------------------------------------------------------------------------
