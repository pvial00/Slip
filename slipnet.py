from os import urandom
from slip import keygen
from Crypto.Util import number
import hashlib

def negdh_client(s):
    sk, n, M = keygen(512)
    P0 = s.recv(8192)
    nB = long(P0)
    s.send(str(n))
    P1Y = s.recv(8192)
    yB = long(P1Y.split('X')[0])
    p1B = long(P1Y.split('X')[1])
    U = n * nB
    S = M * U
    y = number.getRandomRange(1, (S - 1))
    Tk = number.getRandomRange(1, (U - 1))
    myp1 = pow(yB, Tk, S)
    p1string = str(myp1)
    ystring = str(y)
    s.send(p1string+"X"+ystring)
    p2 = pow(p1B, Tk, U)
    myp3 = pow(y, sk, p2)
    s.send(str(myp3))
    P3 = s.recv(8192)
    p3 = long(P3)
    p4 = pow(p3, sk, p2)
    k = number.long_to_bytes(p4)
    key = hashlib.sha256(k).digest()
    return key

def negdh_server(s):
    sk, n, M = keygen(512)
    s.send(str(n))
    nBtmp = s.recv(8192)
    nB = long(nBtmp)
    U = n * nB
    S = M * U
    y = number.getRandomRange(1, (S - 1))
    Tk = number.getRandomRange(1, (U - 1))
    p1 = pow(y, Tk, S)
    s.send(str(y)+"X"+str(p1))
    P1Y = s.recv(8192)
    yB = long(P1Y.split('X')[1])
    p1B = long(P1Y.split('X')[0])
    p2 = pow(p1B, Tk, U)
    p3 = pow(yB, sk, p2)
    P3 = s.recv(8192)
    s.send(str(p3))
    p3B = long(P3)
    p4 = pow(p3B, sk, p2)
    k = number.long_to_bytes(p4)
    key = hashlib.sha256(k).digest()
    return key
