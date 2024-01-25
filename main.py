x= int(input("entrer une 1ère valeur:"))
y= int(input("entrer une 2ème valeur:"))
z= int(input("entrer une 3ème valeur:"))
if (x>y) & (x>z):
    print("la plus grande valeur est:",x)
elif (z>y) & (z>x):
    print("la plus grande valeur est:",z)
else:
    print("la plus grande valeur est:",y)


