
print "===Prime Numbers Without Definations==="
count = 0
a = int(raw_input("Enter starting number :"))
b = int(raw_input("Enter ending number :"))

for i in range(a,b +1):
    
    if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           count+=1
           print(i)
print "Total numr of Primes are :",count
