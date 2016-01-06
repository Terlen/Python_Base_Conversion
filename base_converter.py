num = input('Enter the base 10 number: ')
base = input('Enter the desired base: ')
tempNum = num
convertedVal = []
while tempNum != 0:
    currentPlace = (tempNum % base)
    convertedVal.append(currentPlace)
    tempNum = tempNum / base
    print(tempNum)
convertedVal.reverse()
for x in range(len(convertedVal)):
    print convertedVal[x],
