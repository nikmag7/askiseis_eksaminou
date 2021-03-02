print "Kalispera"
n=input("Give Fibonacci Sequence Term   ")
terms=[1,1]
for i in range (1,n-1):
    p=terms[-1]+terms[-2]
    terms.append(p)
p=terms[-1]
print p
import random
prwtos=1
for i in range (20):
    a=random.randint(1,1000000)
    print a%p
    print a**p
    if a**p == a%p:
        print "kalispera"
        prwtos=prwtos+1
if prwtos==20:
    print ("O arithmos einai prvtos")
else:
    print ("O arithmos den einai prwtos")
