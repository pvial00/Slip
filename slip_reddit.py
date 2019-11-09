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
nA = 45667
nB = 61559
U = nA * nB
y = 36371949254935
yB = 61102435573150

print "Alice keys"
print  nA, y
print "Bob keys"
print nB, yB
U = nA * nB
p1A = 64411339244032
p1B = 95801938861458
p3A = 724057700
p3B = 770567088
Osk = discreteLogarithm(y, p1A, U)
print Osk
o1 = pow(p1B, Osk, U)
print o1
o2 = pow(yB, Osk, o1)
#print o2
