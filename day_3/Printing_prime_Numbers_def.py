
print "===Prime Numbers Witmething (an object) back to the call so you can use ith Definations==="
count = 0
def prime(x):
    if x >= 1:

        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

a=int(raw_input("enter starting num :"))	        
b=int(raw_input("enter ending num :"))

for i in range(a,b):
    if prime(i):
        count += 1
        print i

print "Total Prime nums are ",count
