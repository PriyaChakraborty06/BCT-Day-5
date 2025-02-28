num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
try:
    ans=num1/num2
    print("Result is: ",ans)
except Exception as e:
    print(e)
print("This is the last line")