num1,num2 = 0,1
count = 0
term = int(input("Enter the number :"))
while count < term:
    nth  = num1 + num2
    print(num1)
    num1 = num2
    num2 = nth
    count+=1

n1,n2 = 0,1
count = 0
# nterm = 5
while count < 5 :
    nth = n1 + n2
    print(n1)
    n1 = n2
    n2  = nth
    count += 1