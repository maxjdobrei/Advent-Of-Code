#Author: Max Dobrei
#Objective: A working solution to the first & second challenge of day three for Advent of Code 2020
#Purpose: Take in a 2d representation of a map and determine how many obstacles would be encountered by travelling
#in a straight line for a given slope

import io

def findPath(down, right):
    
    tobogganPATH = open("input.txt", "r")

    currX = 0
    currY = 0
    numObj = 0

    for line in tobogganPATH:
        line = line.strip()

        if currY % down == 0:
            #check things
            if line[currX] == "#":
                numObj += 1
            currX = (currX + right) % (len(line))
             
        currY += 1
      
    print("num of obstacles = ", numObj)

#part 1
findPath(1,3)

#part 2
findPath(1,1)
findPath(1,5)
findPath(1,7)
findPath(2,1)