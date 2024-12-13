#activity 2
number = int(input("Enter a number"))
 
if number%3==0 and number%5==0:
    print("busfizz")
elif number%3==0:
    print("bus")
elif number%5==0:
    print("fizz")
else:
    print("Notvalid")