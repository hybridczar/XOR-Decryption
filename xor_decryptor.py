#Authors: Dustin Matt & Dakota Fuller
#Date: 6/18/2012
'''This program takes a plain text message and xors it against a hex formatted string in a \x00\x11\x22 format'''
run= True
while run == True:
    key = input("Input password or key: ")
    crypt = input("Input xor encryption: ")
    
    result =[]
    asc_key=[]
    out=''
    n=1
    i=0
    p=0
    I=0
    j=0
    
    crypt = crypt.replace('n','xA')
    crypt = crypt.replace('r','xD')
    crypt = crypt.replace('t','x9')
    
    result = crypt.split('\\x')


    while p <= len(key)-1:
        asc_key.append(ord(key[p]))
        p+=1
        
    
    while n <= len(result)-1:
        result[n]= chr((asc_key[i])^(int(result[n],16)))
        n+=1
        if i == (len(key)-1):
            i = 0
        else: i+=1
    while I <= len(result)-1:
        out+= (result[I])
        I+=1    
    print ("The correspondant of that key or password is: ",out)
    run = input("Do you need to run another? (y or n): ")
    if run =="y" or "Y":
        run = True
    else:
        run = False

    
    