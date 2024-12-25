n, m, s = map(int, input().split())

chairList = list(i for i in range(1, n+1))

charRearrages = chairList[s-1:] + chairList[:s-1]

lastOne = m%n - 1

print(chairList)
print(charRearrages)
print(charRearrages[lastOne])