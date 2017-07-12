name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#program for inches to centimeters and pounds to kg
inches = 12
centimeters = 2.54 * inches
pounds = 12
kg = pounds * 0.453592
print(f"{inches} inches is {centimeters} in centimeters")
print(f"{pounds} pounds is {kg} in kg")
