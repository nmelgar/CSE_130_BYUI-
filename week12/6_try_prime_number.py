# A simple Python code to implement the Sieve of Eratosthenes

def apply_sieve(n):
    # n is the size of the sieve
    # Key Idea:
    #  If a[i] == 0, then number i has been "crossed out",
    #  if a[i] == 1, then the number i is not (yet) crossed out. 
    a = [1]*(n+1)  # Start with a list of 1s, of length (n+1). 
    a[0] = 0  # set to zero, as
    a[1] = 0  # neither 0 nor 1 are primes
    p = 2     # 2 is the first prime
    pmax = int(round(n**0.5)) + 1  # we only need to sieve up to square root of n.
    while p < pmax:
        while a[p] == 0:
            p += 1
        j = 2*p
        while j < n:
            a[j] = 0
            j += p
        p += 1
    return [p for p in range(n+1) if a[p] == 1]  # return the list of primes, which are the numbers we have NOT crossed out.

N = 10000  # Look for primes in the first ten thousand numbers.
primes = apply_sieve(N)
print ("The first 100 primes:")
print (primes[:100])