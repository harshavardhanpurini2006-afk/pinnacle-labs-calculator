num1=float(input("enter first number :"))
num2=float(input("enter second number :"))
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=input("choose an operation (1-4):")
if choice=="1":
    result=num1+num2
    print("addition:",result)
elif choice=="2":
    result=num1-num2
    print("subtraction:",result)
elif choice=="3":
    result=num1*num2
    print("multiplication:",result)
elif choice=="4":
    if num2!=0:
        result=num1/num2
        print("division:",result)
    else:
        print("cannot divide by zero")
else:
    print("invalid choice") 