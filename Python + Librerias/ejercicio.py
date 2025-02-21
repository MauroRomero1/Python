num1 = 3
num2 = 4
num3 = 5

for i in range(50):
    num1 = num2
    num2 = num3
    num3 = num1+num2+num3
    
    print(num1, " - ", num2," - ",  num3)

    if(num3 == 8188013234823360):
        print(i)
        break

print(num3)
