name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#program to convert inches to centimeters and pounds to kilogram
inches_to_centimeters = 2.54
pounds_to_kg = 0.453592

print "4 cm in inches is %f inches"  % (4 / inches_to_centimeters)
print "10 kilograms in pound is %f pounds" %(10 / pounds_to_kg)