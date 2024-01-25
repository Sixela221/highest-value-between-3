x= int(input("enter a first value:"))
y= int(input("enter a second value:"))
z= int(input("enter a third value:"))
if (x>y) & (x>z):
    print("The highest value is:",x)
elif (z>y) & (z>x):
    print("The highest value is:",z)
else:
    print("The highest value is:",y)
