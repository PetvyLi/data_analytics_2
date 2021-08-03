#1. What is Python and why is it useful?
#Python is a general purpose, interpreted, interactive, object-oriented high level programming language 
#developed in 1989 by Guido van Rossum. It is useful for many purposes including machine learning, 
#artificial intelligence, data analytics, research, web and app development among others.

#2. 2.	Are the following variable names allowed in python?
#a.	1_message   No
#b.	Greeting_message    Yes
#c.	Message_1   Yes
#d.	First name   No
#e.	Full_name   Yes

#3. Create a variable that holds the string “hello there!”
greeting= “hello there!”

#4. Create a variable for first name, last name and an email extension.  
#Concatenating all three together to form an email address.  For example: firstnamelastname@gmail.com
first_name=”Petvy”
last_name=”Li”
extension=”@gmail.com”
address= first_name + last_name + extension

#5.	Store someone you know name in a variable called name.  Print their name in lower and uppercase using a method.
name=”John Smith”
print(name.lower())
print(name.upper())

#6.	Using a variable, ask your friend if they want to hang out on the 15th of the month.  For example, 
#“Do you want to hang out on the 15th of this month?”  You should have to convert the number to a string.
date=15
print(“Do you want to hang out on the “ + str(date) + “th of this month?”)
------------------------------------------------------------------------------------------------------------
