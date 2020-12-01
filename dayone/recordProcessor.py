import io

myFile = open("helpfulName.txt" , "r")

intArr = []

for line in myFile:
    intArr.append(int(line))


resultOne = -1
resultTwo = -1

counter = 0;
while(counter < len(intArr)):

  myNum = counter
  while(myNum < len(intArr)):
    
    if intArr[counter] + intArr[myNum] == 2020:
      resultOne = counter
      resultTwo = myNum
      break
    else:
      myNum += 1
   
  counter += 1


if resultOne == -1 or resultTwo == -1:
  print("we fucked up")
else:
  print("num 1 = ", intArr[resultOne], " num 2 = ", intArr[resultTwo])




	