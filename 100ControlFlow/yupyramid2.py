stacks = int(input("How tall should the pyramid be? (1-8) "))
import random

if 0 < stacks < 9:
    for i in range(stacks):
        for j in range(stacks-i):
            print(" ", end="")
        for j in range(i+1):
            print("#", end="")
        print("\n")
elif stacks == 420:
    print("Nice.")
elif stacks == 20:
    print("Critical Roll!")
elif stacks == F:
    print("You have paid your respects.")
elif stacks == 66:
    print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
else:
    print("The number inputted is out of range. Bye Felica")
