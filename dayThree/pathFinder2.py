#Author: Max Dobrei
#Objective: A working solution to the second challenge of day three for Advent of Code 2020
#Purpose: Take in a 2d representation of a map and determine how many obstacles would be encountered by travelling
#in a straight line for a given slope

#this was a pretty dirty script, got the job done but not so  nice to look at. I ended up changing my solution to part 1 to be generalized, allowing me to use it to confirm the
#answers I got from this solution

import io

tobogganPATH = open("input.txt", "r")

currX = 0
currY = 0

numObjA = 0
numObjB = 0
numObjC = 0
numObjD = 0


for line in tobogganPATH:
    line = line.strip()

    if currY % 2 == 0:
        currX = currY / 2
        currX = currX % len(line)
        currX = int(currX)
        if line[currX] == "#":
            numObjD += 1
    
    currX = currY
    currX = currX % len(line)
    currX = int(currX)

    if line[currX] == "#":
        numObjA += 1


    currX = 5 * currY
    currX = currX % len(line)
    currX = int(currX)

    if line[currX] == "#":
        numObjB += 1
    
    currX = 7 * currY
    currX = currX % len(line)
    currX = int(currX)

    if line[currX] == "#":
        numObjC += 1

    currY += 1
    currX = int(currX)
    
print("num of obstacles for line 1 = ", numObjA) 
print("num of obstacles for line 2 = ", numObjB) 
print("num of obstacles for line 3 = ", numObjC) 
print("num of obstacles for line 4 = ", numObjD) 