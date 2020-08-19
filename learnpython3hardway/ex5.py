name = 'Zed A. Shaw'
age = 35 # not a lie
height_inch = 74 # inches
height_cm = height_inch * 2.54 # cms
weight_lbs = 180 # lbs
weight_kgs = round(weight_lbs * 0.453592) # kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inch} inches tall, or {height_cm} cms tall.")
print(f"He's {weight_lbs} pounds heavy or {weight_kgs} kiligrams heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_inch + weight_lbs
print(f"If I add {age}, {height_inch}, and {weight_lbs} I get {total}.")
