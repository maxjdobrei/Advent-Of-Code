#Author: Max Dobrei
#Objective: A working solution to the first challenge of day to for Advent of Code 2020
#Purpose: Take in "passwords" and a validation code that specifies what policy was issued at the time of the passwords creation
#using these two details we can determine if the given passwords are valid given the policy in place when they were created
#the goal is to count how many valid passwords there are

import io

passwords = open("passwords.txt", "r")

count = 0


for line in passwords:
    
    arr = line.split(":")            #parse out the two things we care abt; the validation codes on the left and the passwords themselves on the right
    firstHalf = arr[0].split(" ")    #seperate the numerical range from the specified character
    
    pairOStr = firstHalf[0].split("-")  #pair of nums that create a range
    pairONums = []        
    for string in pairOStr:   
        pairONums.append(int(string))  #parse out the numerical values from the str
        
    char = firstHalf[1]               #get the char we need to look for in the password
    
    secondHalf = arr[1].strip()       #cleanup any whitespace that is not part of the actual password

    if secondHalf.count(char) >= pairONums[0] and secondHalf.count(char) <= pairONums[1]:
        count += 1


print("num of valid passwords = ", count)


    
    