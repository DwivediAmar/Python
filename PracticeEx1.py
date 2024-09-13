
# 1 write a program to take details from a student for ID-card and then print it in different lines.

Name = input("Enter Your Full Name : ")
dep = input("Enter Your Depertment : ")
program = input("Enter Your Program Name : ")
batch = input("Enter Your Batch Number : ")
BOD = input("Enter Your Birth Date : ")

print(Name,"//",dep,"//",program,"//",batch,"//",BOD )


# 2 write a program to take an user input as integer then convert to flaot

number  = int(input("Enter Any Random Number :"))
print("Before coversion",type(number))
number = float(number)
print("After converstion value is :",number)
print("After converstion", type(number))

#conditional statement
#if the Statement

marks = 70
if marks >= 90:
    print("you will get mobile phone")
print("thank you")

#if else statement

marks = 70
if marks >= 90:
    print("you will get new mobile phone")
else:
    print("Better luck next time")

#If - elif - else statement
marks = 50
if marks >= 40:
    print("You pass Exam")
elif marks >= 90:
    print("You have top the Exam")    
else:
    print("Need to work hard")
