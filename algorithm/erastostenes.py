import sys

def prime_list(n) :
    cnt = 0
    pri_list = [True] * n
    for x in range(2,int(n**0.5+1)) :
        if pri_list[x] == True :
            for y in range(x*2,n,x) :
                pri_list[y] = False
                
    for x in pri_list :
        if x == True :
            cnt += 1
    return cnt

while True :
    a = int(input())
    if a==0 :
        sys.exit()
    
    else :
        print(prime_list(2*a+1)-prime_list(a+1))