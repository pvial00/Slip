# Python3 program to calculate  
# discrete logarithm  
import math; 
  
# Iterative Function to calculate  
# (x ^ y)%p in O(log y)  
def powmod(x, y, p):  
  
    res = 1; # Initialize result  
  
    x = x % p; # Update x if it is more  
               # than or equal to p  
  
    while (y > 0):  
          
        # If y is odd, multiply x with result  
        if (y & 1):  
            res = (res * x) % p;  
  
        # y must be even now  
        y = y >> 1; # y = y/2  
        x = (x * x) % p;  
    return res;  
  
# Function to calculate k for given a, b, m  
def discreteLogarithm(a, b, m):  
    n = int(math.sqrt(m) + 1);  
  
    value = [0] * m;  
  
    # Store all values of a^(n*i) of LHS  
    for i in range(n, 0, -1):  
        value[ powmod (a, i * n, m) ] = i;  
  
    for j in range(n):  
          
        # Calculate (a ^ j) * b and check  
        # for collision  
        cur = (powmod (a, j, m) * b) % m;  
  
        # If collision occurs i.e., LHS = RHS  
        if (value[cur]):  
            ans = value[cur] * n - j;  
              
            # Check whether ans lies below m or not  
            if (ans < m):  
                return ans;  
      
    return -1;  
  
from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B

def keygen(size):
    N, M = genBase(size)
    sk = number.getRandomRange(1, (N - 1))
    return sk, N, M

size = 16
print("Generating Alice and Bob's keys")
skA, nA, MA = keygen(size)
skB, nB, MB = keygen(size)

print("Alice keys")
print skA, nA, MA
print("Bob keys")
print(skB, nB, MB)
U = nA * nB
S = U * MA
SB = U * MB
print("Generating ephemeral public keys")
y = number.getRandomRange(1, (S - 1))
yB = number.getRandomRange(1, (SB - 1))
TkA = number.getRandomRange(1, (U - 1))
TkB = number.getRandomRange(1, (U - 1))

print(y, yB)
p1 = pow(y, TkA, S)
p1B = pow(y, TkB, SB)
print("p1", p1, p1B)
p2 = pow(p1B, TkA, U)
p2B = pow(p1, TkB, U)
print(p2, p2B)
p3 = pow(yB, skA, p2)
p3B = pow(yB, skB, p2B)
print(p3, p3B)
p4 = pow(p3B, skA, p2)
p4B = pow(p3, skB, p2B)
print(p4, p4B)
#Osk = discreteLogarithm(y, p1, U)
#print Osk
#o1 = pow(p1B, Osk, U)
#print o1
#o2 = pow(yB, Osk, o1)
#print o2
