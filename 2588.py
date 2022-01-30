num1 = int(input())
num2 = input()
 
for i in range(0, 3):
    result = num1*int(num2[2-i])
    print(result)
 
print(num1*int(num2))
