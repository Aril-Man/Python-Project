import random

dadu = random.randrange(1,6)

rool_again = "yes"

while rool_again == "yes" or rool_again == "y":
    print("Rolling the dices...")
    print("The value are....")
    print(dadu)
    print(dadu)

    rool_again = input("Mau coba lagi? ")