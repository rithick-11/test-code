base_price = int(input())
rounds = input()

amanda = 0
mary_kom = 0

for round in rounds:
    if(round == "A"):
        amanda += 2
    elif(round == "M"):
        mary_kom += 2
    else:
        amanda +=1
        mary_kom +=1    
    
print(f"Amanda :{amanda} | Mary Kom :{mary_kom} | winner: {round}")
        
if(amanda == mary_kom):
    print(55 * base_price)
elif(mary_kom > amanda):
    print(60 * base_price)
else:
    print(40 * base_price)
        
