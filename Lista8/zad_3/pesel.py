import random


def calc_check_digit(pesel):
    scale=[1,3,7,9,1,3,7,9,1,3]
    out=[]
    for j in range(0,10):
        res = pesel[j]*scale[j]
        if res>9:
            temp=str(res)
            res=temp[1]
            out.append(int(res))
        else:
            out.append(res)
    sum=0
    for k in out:
        sum=sum+k
    if sum>9:
        temp=str(sum)
        sum=int(temp[1])
        checkdigit=10-sum
    else:
        checkdigit=10-sum
    return checkdigit
            
    
def generate():
    pesel=[]
    for i in range(0,11):
        if i==0 or i==1:
            pesel.append(random.randint(0,9))
        elif i==2:
            pesel.append(random.randint(0,1))
        elif i==3:
            if pesel[i-1]==0:
                pesel.append(random.randint(1,9))
            else:
                pesel.append(random.randint(0,2))
        elif i==4:
            pesel.append(random.randint(0,3))
            if pesel[i-2]==2:
                pesel.append(random.randint(0,2))
        elif i==5:
            if pesel[i-3]==2:
                if pesel[i-4]%2==0:
                    pesel.append(random.randint(0,9))
                else:
                    pesel.append(random.randint(0,8))
            elif pesel[i-1]==3:
                if pesel[i-3]==0:
                    if pesel[i-2]==1:
                        pesel.append(random.randint(0,1))
                    elif pesel[i-2]==3:
                        pesel.append(random.randint(0,1))
                    elif pesel[i-2]==4:
                        pesel.append(0)
                    elif pesel[i-2]==5:
                        pesel.append(random.randint(0,1))
                    elif pesel[i-2]==6:
                        pesel.append(0)
                    elif pesel[i-2]==7:
                        pesel.append(random.randint(0,1))
                    elif pesel[i-2]==8:
                        pesel.append(random.randint(0,1))
                    elif pesel[i-2]==9:
                        pesel.append(0)
                elif pesel[i-3]==1:
                    if pesel[i-2]==0:
                        pesel.append(random.randint(0,1))
                    elif pesel[i-2]==1:
                        pesel.append(0)
                    elif pesel[i-2]==2:
                        pesel.append(random.randint(0,1))
            else:
                pesel.append(random.randint(0,9))
        elif i==6 or i==7 or i==8 or i==9:
            pesel.append(random.randint(0,9))
        elif i==10:
             pesel.append(calc_check_digit(pesel) )                    
    
    temp=""                
    for j in pesel:
        temp=temp+str(j)
    
    return temp
    