import random
import time
from cubemesh import *

x = int(input("Wie oft sollen random Moves auf den Würfel ausgeübt werden?"))


def randomization():
    print("Moves applied: " + str(x) + "x \n")
    time.sleep(2)
    for number in range(x):
        i = random.choice(method_list)
        ml = []
        for method in method_list:
            ml.append(str(method))
        print(ml)
        i()
        print(str(i))

    return
randomization()
