
greeting = "Samyak Bambole"
#indexes:   01234

print( len(greeting) ) # Length of the string
print("")
print( greeting[0] ) #Accessing the index
print("")
print( greeting[-1] ) #This is the negative index position
print("")
print( greeting.find("yak") )# This will find the string given in the variable
print("")
print( greeting.find("z") )
print("")
print( greeting[2:] )
print("")
print( greeting[2:3] )
print("")
print ("Samyak \" Bambole\" ") # Use this to print a double-quotation mark in the string
print("")
print(greeting.lower()) # This will output everything in the lower case
print("")
print(greeting.upper())# This will output everything in the upper case
print("")
print(greeting.isupper()) # This will return a boolean value. it will say true if all of the characters are upper case.
print("")
print(greeting.islower())
print("")
print(greeting.upper().isupper()) # I made it upper case and now it will return true
print("")
print(greeting.index("k")) # This will return the  index value of k
print("")
print(greeting.replace("Samyak", "Elephant")) # This will replave samyak with elephant
