firstTerm = 1
secondTerm = 2
lastTerm = firstTerm + secondTerm
finalSum = 2

while(lastTerm < 4000000):
  firstTerm = secondTerm
  secondTerm = lastTerm
  lastTerm = firstTerm + secondTerm
  if(lastTerm % 2 == 0):
    finalSum += lastTerm

print(finalSum)

