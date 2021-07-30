number=int(input("Enter a number"))
if number%4==0:
    print("It is divisible by 4")
    print("It is even")
elif number%2==0:
    print("It is even")
elif number%2==1:
    print("It is odd")

num=int(input("Enter a number"))
check=int(input("Enter another number"))
if num%check==0:
    print("Second number divides evenly into first")
else:
    print("Second number does not divide evenly into first")
