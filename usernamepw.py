# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:15:04 2020

@author: u
"""
#
#username ='Sanjeevan'
#password = '123'
#us_nm = ''
#user_pw  = ''
#count =0 
#countpw = 0
#
#us_nm = input ('enter username') 
#    #      if us_nm != username:
#    #          print ( ' We do not recognise the username, try again' )
#while  user_pw != password and countpw < 3 :
#  user_pw = input ('enter password')
#  countpw = countpw + 1
#  
#if us_nm != username :   
#    print (' User name wrong, Please register')
#if user_pw != password : 
#    print ( ' You had give the password incorrectly 3 times and now you are locked' )
#
#if us_nm == username and user_pw == password:
#    print ( 'Login successfull' )
    
# user_pw = input ('enter password')
# print ('Password correct.')



username ='Sanjeevan'
password = '123'
us_nm = ''
user_pw  = ''
us_nm = input ('enter username')
user_pw = input ('enter password')
count = 1
while count < 3 and (us_nm != username or user_pw != password) :
  if us_nm != username:
      us_nm = input ('username incorrect, enter username')
  if us_nm == username and user_pw != password:
      user_pw = input ('password incorrect, enter password')
  count = count + 1
  
  


  
  
  
  
  
  
  