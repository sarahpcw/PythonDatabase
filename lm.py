# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:18:14 2021
"""

def myfunction (x):
    a = x/2
    return a

a = myfunction(1)

a = lambda x:x/2
print ('the remainder of  1 divided by 2 :', a(1))
print ('the remainder of  2 divided by 2 :' , a(2))
print ('the remainder of  3 divided by 2 :' , a(3))









#
#
#
#
result = lambda x, y : (x,y,x+y)   
print (result(2,3))  # use result with input parameters 2 and 3 , show the input and the output
print (result(3,4))
print (result(4,5))
# 
#example
Celcius = [27,24,26,28]
Fahrenheit = map ( lambda x : (x  *  9/5 ) + 32   , Celcius ) 
for each in Fahrenheit: 
    print ('Fah',each) 
#example
#
#print ('\n')
#Celsius = [2, 4, 6, 8]
#Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
#for each in Fahrenheit:
#print (each, end= " ")
#
#exercise
#Ask the end-user for the number of adults, number of children, number of pensioners who want to go to the movies. Create a lambda function that will return the full ticketPrice where a single adult ticket is 10 pounds, children pay half and pensioners pay 30%
#
movieprice = lambda pr,a,c,p :  pr * a + pr/2*c + pr/3*p 
a = float(input ("how many adults?"))
c = float(input ("how many children?"))
p = float(input ("how many pensioners?"))
print (movieprice(10,a,c,p))
#
#
#@author: u
#"""
#
