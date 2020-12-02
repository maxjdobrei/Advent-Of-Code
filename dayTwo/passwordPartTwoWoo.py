#Author: Max Dobrei
#Objective: A working solution to the second challenge of day to for Advent of Code 2020
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
        
    char = firstHalf[1].strip()            #get the char we need to look for in the password
    
    secondHalf = arr[1].strip()       #cleanup any whitespace that is not part of the actual password

    #all that changes for part two is how we use the parsed info to determine validity
    if (pairONums[0]-1 < len(secondHalf) and char == secondHalf[pairONums[0]-1]) and not (pairONums[1]-1 < len(secondHalf) and char == secondHalf[pairONums[1]-1]): 
        count += 1 
    elif (pairONums[1]-1 < len(secondHalf) and char == secondHalf[pairONums[1]-1]) and not (pairONums[0]-1 < len(secondHalf) and char == secondHalf[pairONums[0]-1]):
        count += 1
    
print("num of valid passwords = ", count)