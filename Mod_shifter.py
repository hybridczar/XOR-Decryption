#Authors: Dustin Matt & Dakota Fuller
#Date: 6/18/2012
from comparison import*

dictionary={
1:[['c','b'],['d','e'],['f','g'],['h','i'],['j','k'],['l','m'],['n','o'],['p','q'],['r','s'],['t','u'],['v','w'],['x','y']],
2:[['a','c'],['d','f'],['e','g'],['h','j'],['i','k'],['l','n'],['m','o'],['p','r'],['q','s'],['t','v'],['u','w'],['x','z']],
3:[['a','b'],['e','f'],['d','g'],['h','k'],['i','j'],['l','o'],['m','n'],['p','s'],['q','r'],['t','w'],['u','v'],['y','z']],
4:[['a','e'],['b','f'],['c','g'],['h','l'],['i','m'],['j','n'],['k','o'],['p','t'],['q','u'],['r','v'],['s','w']],
5:[['a','d'],['c','f'],['b','g'],['h','m'],['i','l'],['j','o'],['k','n'],['p','u'],['q','t'],['r','w'],['s','v']],
6:[['b','d'],['c','e'],['g','a'],['h','n'],['i','o'],['j','l'],['k','m'],['p','v'],['q','w'],['r','t'],['s','u']],
7:[['c','d'],['b','e'],['a','f'],['h','o'],['i','n'],['j','m'],['k','l'],['p','w'],['q','v'],['r','u'],['s','t']],
8:[['a','i'],['b','j'],['c','k'],['d','l'],['e','m'],['f','n'],['g','o'],['p','x'],['q','y'],['r','z']],
9:[['a','h'],['b','k'],['c','j'],['d','m'],['e','l'],['f','o'],['g','n'],['p','y'],['q','x'],['s','z']],
10:[['b','h'],['c','i'],['a','k'],['d','n'],['e','o'],['f','l'],['g','m'],['p','z'],['r','x'],['s','y']],
11:[['c','h'],['b','i'],['a','j'],['d','o'],['e','n'],['f','m'],['g','l'],['q','z'],['r','y'],['s','x']],
12:[['d','h'],['e','i'],['a','m'],['b','n'],['c','o'],['f','j'],['g','k'],['t','x'],['u','y'],['v','z']],
13:[['e','h'],['d','i'],['a','l'],['b','o'],['l','n'],['f','k'],['g','j'],['t','y'],['u','x'],['w','z']],
14:[['f','h'],['g','i'],['a','o'],['b','l'],['c','m'],['d','j'],['e','k'],['t','z'],['v','x'],['w','y']],
15:[['g','h'],['f','i'],['a','n'],['b','m'],['c','l'],['d','k'],['e','j'],['u','z'],['v','y'],['w','x']],
16:[['a','q'],['b','r'],['c','s'],['d','t'],['e','u'],['f','v'],['g','w'],['h','x'],['i','y'],['j','x']],
17:[['a','p'],['b','s'],['c','r'],['d','u'],['e','t'],['f','w'],['g','v'],['h','y'],['i','y'],['j','k']],
18:[['a','s'],['b','p'],['c','q'],['d','v'],['e','w'],['f','t'],['g','u'],['h','z'],['j','z'],['k','y']],
19:[['a','r'],['b','q'],['c','p'],['d','w'],['e','v'],['f','u'],['g','t'],['i','z'],['k','x']],
20:[['a','u'],['b','v'],['c','w'],['d','p'],['e','q'],['f','r'],['g','s'],['l','x'],['m','y'],['n','z']],
21:[['a','t'],['b','w'],['c','v'],['d','q'],['e','p'],['f','s'],['g','r'],['l','y'],['m','x'],['o','z']],
22:[['a','w'],['b','t'],['c','u'],['d','r'],['e','s'],['f','p'],['g','q'],['l','z'],['n','x'],['o','y']],
23:[['a','v'],['b','u'],['c','t'],['d','s'],['e','r'],['f','q'],['g','p'],['m','z'],['n','y'],['o','x']],
24:[['a','y'],['b','z'],['h','p'],['i','q'],['j','r'],['k','s'],['l','t'],['m','u'],['n','v'],['o','w']],
25:[['a','x'],['c','z'],['h','q'],['i','p'],['j','s'],['k','r'],['l','u'],['m','t'],['n','w'],['o','v']],
26:[['b','x'],['c','y'],['h','r'],['i','s'],['j','p'],['k','q'],['l','v'],['m','w'],['n','t'],['o','u']],
27:[['a','z'],['b','y'],['c','x'],['h','s'],['i','r'],['j','q'],['k','p'],['l','w'],['m','v'],['n','u'],['o','t']],
28:[['d','x'],['e','y'],['f','z'],['h','t'],['i','u'],['k','w'],['l','p'],['m','q'],['n','r'],['o','s']],
29:[['d','y'],['e','x'],['g','z'],['h','u'],['i','t'],['k','v'],['l','q'],['m','p'],['n','s'],['o','r']],
30:[['d','z'],['f','x'],['g','y'],['h','v'],['i','w'],['j','t'],['k','u'],['k','u'],['l','r'],['m','s'],['n','p'],['o','q']],
31:[['e','z'],['f','y'],['g','x'],['h','w'],['i','v'],['j','u'],['k','t'],['l','s'],['m','r'],['n','q'],['o','p']]
}



x=0 #Iterates through printing Gspot.
y=0 #Controls index of shiftList and reference to Gspot.
z=0 #Controls index of baseList

crypt = input("Input xor encryption: ")
keyLength= int(input("Input key length: "))

crypt = crypt.replace('n','xA')
crypt = crypt.replace('r','xD')
crypt = crypt.replace('t','x9')
result =[]   
result = crypt.split('\\x')

temp = [0]
baseList=[]
shiftList=[]
Gspot = []

baseList =(result[keyLength+1:])
shiftList=(result[1:-keyLength])
while y <= keyLength-1:#len(shiftList)-1:
        xor = None
        z=y #should fix indexing errors where it xor's incorrectly //see notes
        while z<= len(baseList)-1:

                
                
                # If this is the first time an element has been xor'ed, put it right into a new index of the resultinf list.
                if xor == None: 
                        
                        xor =((int(baseList[z],16))^(int(shiftList[y],16)))
                        if xor in dictionary:
                                Gspot.append(dictionary[xor])
                        else:
                                print('Result not in dictionary at index', z, 'of letter',y)
                        
                
                #Otherwise put the xor'ed results into a temporary list to compare the like terms and overwrite the previous results input for this letter with the new list.
                else:
                        xor = (int(baseList[z],16))^(int(shiftList[y],16))  
                        if xor in dictionary:
                                temp[0] = dictionary[xor]
                                Gspot[y] = compare(Gspot[y],temp[0])
                                
                        else:
                                print('Result not in dictionary at index', z, 'of letter',y)
                                        

                z+=keyLength
        
        y+=1
        


while x <= len(Gspot)-1:
        print("Result for index: ", x,'\n',Gspot[x])
        x+=1
