#Simple if
# write a program to accept any digit and check that it is positive, negative or zero

# num = int(input("Enter any digit: "))

# if num > 0:
#     print("Positive")

# if num < 0:
#     print("Negative")

# if num == 0:
#     print("Zero")


 #Write a program to accept days and check the working days and weekends

# days = input("Enter the day: ")

# if days == "Saturday" or days == "Sunday":
#     print("Weekend")
# else:
#     print("Working day")


# Write a program to accept three paper marks and calculate total, percentage and if percentage is greater then equal to 60 then
# he/ she is eligible for placement

# m1=int(input("Enter the first paper marks:"))
# m2=int(input("Enter the second paper marks:"))
# m3=int(input("Enter the third paper marks:"))
# total=(m1+m2+m3)
# print("Total:",total)
# percentage= total/300*100
# print("Percentage", percentage)
# if percentage>=60:
#     print("Eligible for placement.")
# else:
#     print("Not eligible for placement.")


# write a program to accept 5 diff value in 5 different var and check max value and print by using "simple if statement"
n1=int(input("Enter the first number :"))
n2=int(input("Enter the second number :"))
n3=int(input("Enter the third number :"))
n4=int(input("Enter the fourth number :"))
n5=int(input("Enter the fifth number :"))
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print("First  number is greatest")
if n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print("First  number is greatest")
if n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print("First  number is greatest")
if n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print("First  number is greatest")
if n5>n1 and n5>n2 and n5>n3 and n5>n4:
    print("First  number is greatest")