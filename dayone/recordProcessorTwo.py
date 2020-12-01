import io

myFile = open("helpfulName.txt" , "r")

intArr = []

for line in myFile:
    intArr.append(int(line))


for i in range(0, len(intArr)):
    for j in range(i, len(intArr)):
        num = 2020 - intArr[i] - intArr[j]
        if num in intArr:
            print("num 1 = ", intArr[i], " num 2 = ", intArr[j], "num 3 = ", num)
            break
        else:
            continue


print("so did we find anything")
    
   


