p = list(map(int, input().split(" ")))

string = ""

for i in p:
    string += chr(96 + i)
    
print(string)