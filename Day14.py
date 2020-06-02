# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 14 : 4-06-2020
# Day 14 | IG : https://www.instagram.com/benjivrik/
# Subject : Module - Matplotlib.pyplot
#----------------------------------------------------
# what would be the output of this program ?

'''

    It is possible to graphically vizualise any set 
    of data ('graphically vizualizable') in your program.

    The module matplotlib.pyplot allows you to vizualize your data 
    through plot.

    Let's collect five delays in our program as previously shown in 
    Day 13 and plot the value with collect.

'''

import matplotlib.pyplot as plt
import time



your_I_to_II = int(time.time()*1000)

print("BLOCK I_to_II")
print("Adding a random line.")

your_II_to_III = int(time.time()*1000)

print("BLOCK II_to_III")
print("Adding a random line.")
print("Adding a random line.")
print("Adding a random line.")

your_III_to_IV = int(time.time()*1000)

print("BLOCK III_to_IV")
print("Adding a random line.")
print("Adding a random line.")

your_IV = int(time.time()*1000)


print(
    "\n> Delay block I to II : {} ms".format(your_II_to_III - your_I_to_II),
    "\n> Delay block II to III : {} ms".format(your_III_to_IV - your_II_to_III),
    "\n> Delay block III to IV : {} ms".format(your_IV - your_III_to_IV)
)

data = list()
data.append(your_II_to_III - your_I_to_II)
data.append(your_III_to_IV - your_II_to_III)
data.append(your_IV - your_III_to_IV)
print(data)

plt.plot(data, 'b--')
plt.ylabel('Time (ms)')
plt.axis([0,3,0,48])
plt.title('Block I-II, II-III, III-IV')
plt.show()
