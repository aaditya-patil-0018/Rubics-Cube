import random
import time
from cubemesh import *

x = int(input("Wie oft sollen random Moves auf den Würfel ausgeübt werden?"))


def randomization():
    print("Moves applied: " + str(x) + "x \n")
    time.sleep(2)
    for number in range(x):
        i = random.choice(method_list)
        print(method_list)
        print(i)

    return
randomization()
