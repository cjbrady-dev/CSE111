#input
from datetime import datetime
import math
#width of the tire in millimeters
w = int(input("Width: "))
# the aspect ratio of the tire.
a = int(input("Aspect ratio: "))
# the diameter of the wheel in inches.
d = int(input("Diameter: "))
# volumes file variable
volumes_txt = "volumes.txt"


#processing
current_date_and_time = datetime.now()

radicul = (w * a) + (2540 * d)
v = (math.pi * (w**2)) * (a * radicul)/ 10000000000



#output
print(f"The approximate volume is {v:.2f} liters")

#files
with open("volumes.txt", "at") as volumes_txt:
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}", file=volumes_txt)