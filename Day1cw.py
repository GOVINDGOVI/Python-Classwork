apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

totalvolume_sold = apple_juice + orange_juice + grape_juice

print("Total volume of juice sold:", totalvolume_sold)

totalvolume_int = int(totalvolume_sold)
print("Total volume of juice sold (as integer):", totalvolume_int)

totalvolume_str = str(totalvolume_sold)
print("Total volume of juice sold (as string):", totalvolume_str)

import random
bonus_liters = random.randint(5, 10)
final_total = totalvolume_int + bonus_liters

print("Final total volume after bonus liters:", final_total)