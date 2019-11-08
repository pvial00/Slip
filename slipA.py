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

def slip_demo(size):
    print "Generating Alice and Bob's keys"
    skA, nA, MA = keygen(size)
    skB, nB, MB = keygen(size)
    print skA, nA, MA
    print skB, nB, MB
    print "Exchanging the umbrella and generating secret umbrellas"
    U = nA * nB
    S = MA * U
    SB = MB * U
    print U
    print S, SB
    print "Each choose a number in secret umbrellas"
    y = number.getRandomRange(1, (S - 1))
    yB = number.getRandomRange(1, (SB - 1))
    print y, yB
    print "Each choose a temporary key in the umbrella"
    TkA = number.getRandomRange(1, (U - 1))
    TkB = number.getRandomRange(1, (U - 1))
    print TkA, TkB
    print "Exchange phase1"
    p1 = pow(y, TkA, S)
    p1B = pow(y, TkB, S)
    print p1, p1B
    print "Arrive at the secret modulus phase2"
    p2 = pow(p1B, TkA, U)
    p2B = pow(p1, TkB, U)
    print p2, p2B
    print "Exchange phase3"
    p3 = pow(yB, skA, p2)
    p3B = pow(yB, skB, p2B)
    print p3, p3B
    print "Arrive at the shared key phase4"
    p4 = pow(p3B, skA, p2)
    p4B = pow(p3, skB, p2B)
    print p4, p4B

slip_demo(16)
