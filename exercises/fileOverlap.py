
file1 = "primeNumbers.txt"
file2 = "happyNumbers.txt"

primes = []
happies = []

with open(file1, "r") as primeNumbers:
    prime = primeNumbers.readline()
    while prime:
        primes.append(int(prime))
        prime = primeNumbers.readline()
    with open(file2, "r") as happyNumbers:
        happy = happyNumbers.readline()
        while happy:
            happies.append(int(happy))
            happy = happyNumbers.readline()
print([x for x in primes if x in happies])
