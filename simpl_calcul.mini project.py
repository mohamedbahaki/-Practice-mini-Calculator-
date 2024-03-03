# practis calculatris 
print ("*" * 12) 
number_1 = float (input ("inter your number 1 :")).split() # --> split() for remove spaces and float for add any type number 
print ("*" * 12)
number_2 = float (input ("inter your number 2 :")).split() 
print ("*" * 12)
relation = input ("inter your relation :") # relation + or - or ..

# relation

if relation == "+" :
    print (number_1 + number_2)
elif relation == "-" :
    print (number_1 - number_2)
elif relation == "*" :
    print (number_1 * number_1 )
else :
    print ("inter your relation !!")    