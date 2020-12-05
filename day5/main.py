

def getRow(code, low, high):
  #length of the list is 2**length of code

  if len(code) == 1 and code == code[0] in ["F", "L"]:
      return low

  if len(code) == 1 and code == code[0] in ["B", "R"]:
      return high

  if code[0] in ["F", "L"]:
    return getRow(code[1:], low, (low + high) // 2)
  else: 
    return getRow(code[1:], ((low + high) // 2) + 1, high)


def getSeatId(ticketCode):
  rowCode = ticketCode[:7]
  columnCode = ticketCode[-3:]

  row = getRow(rowCode, 0, 127)
  column = getRow(columnCode, 0, 7)

  return (row * 8) + column


seatIds = []
f = open("data.txt", "rt")
lines = list(f.readlines())
highest = 0
for line in lines:
  seatId = getSeatId(line.rstrip())
  seatIds.append(seatId)

  
f.close()
seatIds = sorted(seatIds)
myList = seatIds[1:len(seatIds)-1]
 
print(len(seatIds))
print(len(myList))

# loop through all numbers 
for index in range(len(myList)):
  if not (index in myList):
    print (index)









