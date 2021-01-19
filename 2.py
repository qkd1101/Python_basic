# test_n = int(input())

# for _ in range(test_n) :

def make_pg(k,n,N) :
    tmp_k = k-1
    tmp_n = n-1
    key_k = 0
    key_n = 0
    for _ in range(3) :
        tmp_n = n-1
        key_n = 0
        for __ in range(3) :
            if tmp_k < 0 :
                # print("spot1")
                pg[key_k][0] = -1
                pg[key_k][1] = -1
                pg[key_k][2] = -1
                break
            if tmp_n < 0:
                # print("spot2")
                pg[key_k][key_n] = -1
                tmp_n += 1
                key_n += 1
                continue
            if tmp_n >= N :
                # print("spot3")
                pg[key_k][key_n] = -1
                break
            if(li[tmp_k][tmp_n] == 'o') :
                if tmp_k == k & tmp_n == n :
                    # print("spot4-1")
                    continue
                print("spot4-2",tmp_k,tmp_n,key_k,key_n)
                pg[key_k][key_n] = 1
                tmp_n += 1
                key_n += 1
                continue
            else :
                # print("spot5")
                pg[key_k][key_n] = -1
                tmp_n += 1
                key_n += 1
                continue
        tmp_k += 1
        key_k += 1

def next(k,n,N) :
    stack += 1
    

N = int(input())
li = []
coli = []
pg = []
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
            make_pg(k,n,N)
            li[k][n] = 1

            break
    break 

for a in pg :
    print(a)
        