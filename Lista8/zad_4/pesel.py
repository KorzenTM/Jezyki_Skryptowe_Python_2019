def check_control_digit(pesel):
    check_digit_real=int(pesel[10])
    scale=[1,3,7,9,1,3,7,9,1,3]
    out=[]
    for j in range(0,10):
        res = int(pesel[j])*scale[j]
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
        
    if check_digit_real==checkdigit:
        return True
    else:
        return False
  
def date_birth(pesel):
    year="19"+pesel[0]+pesel[1]
    month=pesel[2]+pesel[3]
    day=pesel[4]+pesel[5]
    date=day+"-"+month+"-"+year
    return date

def sex(pesel):
    sex=int(pesel[9])
    if sex%2==0:
        return "Men"
    else:
        return "Woman"