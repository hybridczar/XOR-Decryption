#Authors: Dustin Matt & Dakota Fuller
#Date: 6/18/2012
'''This program xors a hex formated string in a \x00\x11\x22 format and shifts it against itself and keeps xoring'''
crypt = input("Input xor encryption: ")
#def shifter(crypt):
result =[]

crypt = crypt.replace('n','xA')
crypt = crypt.replace('r','xD')
crypt = crypt.replace('t','x9')
    
result = crypt.split('\\x')

q= round(len(result)/2)
a=1
z=0


first=[]
second=[]
while a<= (len(result)-1):
        first.append(result[a])
        second.append(result[a])
        a+=1
       
while z<= len(first)-1:
        result = []
        temp=[]
        out=''
        n=0
        I=0
        
        j=0

        
        while n <= len(first)-1:
                result.append(chr((int(first[n],16))^(int(second[n],16))))
                n+=1
                

        while I <= len(result)-1:
                #print(result[I],'',end='')
                out+= (result[I])
                I+=1
        print ("The correspondant of that key or password is: shifted (",z,") times",out)
        
        
        while j <= len(second)-2:
                temp.append(second[j])
                j+=1
                                
        temp.insert(0,(second[len(second)-1]))
        second=temp               
        z+=1