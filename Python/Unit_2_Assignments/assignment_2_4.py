# -*- coding: utf-8 -*-
"""Assignment_2.4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/PetvyLi/data_analytics_2/blob/main/Assignment_2_4.ipynb
"""

#Create a list that holds 5 data variables. 
animals = ["lion", "tiger", "zebra", "elephant", "dog"]

#Print out those variables by using a for loop.
for x in animals:
    print(x)

#Modify your for loop to add a message to your for loop.
for x in animals:
    print("This is an animal:", x)

#Use a for loop to print even numbers from 1-20.
for number in range(2,21,2):
    print(number)

#Sort your list in alphabetic order.
animals.sort()

#Print out the first three elements of your list.
for i in range(3):
    print(animals[i])

#Create a loop to print the last 2 elements of your list.
for i in range(3,5):
    print(animals[i])