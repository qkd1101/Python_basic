# test_n = int(input())

# for _ in range(test_n) :

def make_pg(k,n,N) :
    tmp_k = k
    tmp_n = n-1
    y = []
    for _ in range(3) :
        tmp_n = n-1
        for __ in range(3) :
            if tmp_k < 0 :
                break
            if tmp_n < 0:
                tmp_n += 1
                continue
            if tmp_n >= N :
                break
            if(li[tmp_k][tmp_n] == 'o') :
                if tmp_k == k and tmp_n == n :
                    tmp_n += 1
                    continue
                y.append([tmp_k,tmp_n])
                tmp_n += 1
                continue
            else :
                tmp_n += 1
                continue
        tmp_k += 1

    return y   

def next(k,n,ta,li,coli,N) :
    global stack
    stack += 1
    for tik,tin in ta :
        tmp_k = k - tik
        tmp_n = n - tin
        coli[tik][tin] = 1
        while True :
            stack += 1
            if(0 <= tik+tmp_k <= N and 0 <= tin+tmp_n <= N and \
                li[tik+tmp_k][tin+tmp_n] == 'o') :
                stack += 1
                tik += tmp_k
                tin += tmp_n
            else :
                stack = 0
                return 0





N = int(input())
li = []
coli = []
pg = []
y2 = []
stack = 0

for _ in range(N) :
    a = list(input())
    li.append(a)

coli = [[0 for col in range(N)] for row in range(N)]
pg = [[0 for col in range(3)] for row in range(3)]

print(li)
for k in range(N) :
    for n in range(N) :
        if(li[k][n] == 'o') :
            y2 = make_pg(k,n,N)
            coli[k][n] = 1
            next(k,n,y2,li,coli,N)
            break
    break 

print(stack)
print(li)