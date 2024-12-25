n = int(input())
marks = list(map(int, input().split(" ")))

result = []

for i in range(n):
    mark = marks[i]
    count = 0
    for j in marks[i:]:
        if mark > j:
            count +=1
    print(marks[i:], count, mark)
    result.append(count)
    
print(*result)