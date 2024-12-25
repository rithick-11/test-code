s , t = map(int, input().split(" "))

cont = 0

for i in range(s+1):
    for j in range(s+1-i):
        for k in range(s+1-i-j):
            if((i*j*k) <= t):
                cont += 1

print(cont)