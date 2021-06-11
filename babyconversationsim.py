#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:59:58 2021

@author: user
"""

#number = 1

#while number <= 10:
    #print(number)
    #number = number + 1
   
#L = []

#while len(L) <3:
    #new_name = input("Please add a new name: ").strip().capitalize()
    #L.append(new_name)
    #print("Sorry list is full")
from random import choice 

  
questions = ["Why is the sky blue?, Why is there 10 fingers?: ", 
             "Where is Abraham buried? "]    

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
    
    print("Oh...Okay")
    