#Authors: Dustin Matt & Dakota Fuller
#Date: 6/18/2012
def compare (first,second):
    x=0
    y=0

    result=[]

    
    while x <= len(second)-1:
        #This iterates through the second list, and compares one item of the second list to the entirety of the first list. Then if it finds itself in the first list it is then saved.
        two = False
        y=0
        while y <= len(first)-1:
            one = False
 
            z=0
            while z <= 1:
               
                if (second[x][z]) == (first[y][0]):

                    one = True
                    two = True
                    break

                elif second[x][z] == first[y][1]:

                    one = True
                    two = True
                    break
                z+=1
            if (one == True) and not(first[y] in result):
                result.append(first[y])
            y+=1
        if two == True and not(second[x] in result):
            result.append(second[x])        
        x+=1
    return (result)
