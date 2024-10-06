#finds the cycle length sums of a sum
#isPrime takes in 2 values and calculates if value a is relatively prime to b and returns if true or false
def relativelyPrime(a, b):
  if (a == 0):
    return b
  return relativelyPrime(b % a, a)
#eulersPhi calculates the Euler's Phi number of a value and returns it
def eulersPhi(divisor):
  result = 1
  for i in range(2, divisor):
    if (relativelyPrime(i, divisor) == 1):
      result+=1
  return result
#sumCycles takes two lists, adds an element from the first list the amount of times the correspoding element from the second list is to total sum
def sumCycles(divisors, cycleAmnt):
  numsToAdd = []
  result = 0
  for element, count in zip(divisors, cycleAmnt):
      numsToAdd.extend([element] * count)
  for num in numsToAdd:
    result += num
  print(result)
#main call for input and cycles through each input to find the cycle length sum of each value 
n = int(input())
for _ in range(n):
  p = int(input())
  d = p - 1
  divisors = []
  for j in range(1, d + 1):
    if d % j == 0:
      divisors.append(j)
  cycleAmnt = []
  for divisor in divisors:
    phi = eulersPhi(divisor)
    cycleAmnt.append(phi)
  sumCycles(divisors, cycleAmnt)
