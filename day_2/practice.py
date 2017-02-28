#Dictonarys
mydict = {'name':'gopikrishna','company':'ASM Technologies','role':'SE','age':22}

print mydict.items()
print mydict
print len(mydict)
print "\n"

mydict ['Loc']='Banglore'
print mydict.items()
print len(mydict)
print "\n"







#File Operations
file = open("new.txt", "r")

for line in file:
    print(line)

file.close() 


#Tuple

tup_value=("mon","tue","wed","thu","fri","sat","sun")
inp=raw_input("enter day number  :")
inp=int(inp)
print tup_value[inp]

#Lists

list_month=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
month=raw_input("enter number :")
month=int(month)
end=month*3
start=end-3
print list_month[start:end]

