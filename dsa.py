import random as rn
from random import randrange
import hashlib

ch=False
def check(p,q):
    for i in range(2,p):
        if (p % i) == 0:
            print(p," is not a prime number!")
            return False
    for i in range(2,q):
        if (q % i) == 0:
            print(q," is not a prime number!")
            return False
    return True

#n=rn.randint(1,160) #we use 160 because the output of SHA-1 is 160
while(ch==False):
    p=input('Enter p:')
    q=input('Enter q:')
    ch = check(p,q)


h = 1
g = 1
for h in range(1,p-1):
    if ( (h**( (p-1)/q ))%p > 1):
        g =  (h**( (p-1)/q ))%p
        break

	
#private_key = 1

private_key = rn.randint(1,q)

public_key = (g**private_key )%p

print "Public Key = { ",g,",", public_key, " }"
print "Private Key = { ",g,",", private_key, " }"

#Generate Signature

m = hashlib.sha1()	#create a SHA1 hash object
m.update("Hello")	#Update the hash object with the string "Hello"
hashm = int(m.hexdigest(),16)	#hexdigest() : the digest is returned as a string of double length, containing only hexadecimal digits.
print "Hashed Message : ",hashm


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

r = 0
s = 0
k = 0
while r == 0 or s == 0:# or modinv(k,q) == None:
    k = rn.randint(1,q)
    r = ((g**k)%p)%q
    val = modinv(k,q)
    if val != None:	
        s =  modinv(k,q) * int((( hashm + private_key*r ) )%q)
	
print "Digital Signature : ( ",r,",",s,")"

