def primeChecker(num, printPrime = False):
    isPrime = True
    factors = [1]
    for x in range(2,(num-1)):
        if num % x == 0:
            factors.append(x)
            isPrime = False
    factors.append(num)
    if printPrime == True:
        if isPrime == True:
            print(str(num) + ' is Prime!!!')
            print(factors)
            return True
        elif isPrime == False:
            print(str(num) + ' is Not Prime')
            print(factors)
            return False
    elif printPrime == False:
        if isPrime == True:
            return True
        elif isPrime == False:
            return False
    

for x in range(2,num):
    if primeChecker(x,True) == True:
        print(x)
factors = [1]
for x in range(2,(num-1)):
    if num % x == 0:
        factors.append(x)
factors.append(num)

if isEven(len(factors)) == True:
    pass
elif isEven(len(factors)) == False:
    factors.append(statistics.median(factors))
    factors = sorted(factors)

factors = list(chunks(factors,(int(len(factors)/2))))

fac1 = factors[0]
fac2 = list(reversed(factors[1]))

mulFac = dict(zip(fac1,fac2))

pprint.pprint(mulFac)
