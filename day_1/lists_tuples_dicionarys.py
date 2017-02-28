#Getting User Input
value = raw_input("Enter Value : ")
print value
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


#Dictonarys
month_dictonary={'jan':31,'feb':28,'mar':30,'apr':31,'may':30,'jun':31,'july':30,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
inp=raw_input("enter month name :")
inp=int(inp)
print month_dictonary['key']
for m in month_dictonary:
    print (month_dictonary)


#Inbuilt Functions
list_num=[1,2,3]
print max(list_num)
print min(list_num)
print len(list_num)
