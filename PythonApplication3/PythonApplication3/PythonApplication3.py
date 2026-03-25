

H1 = ["H1", "Bob Miller special", 195, "191,300", 5600, 4, 2000, 6]
E2 = ["E2", "Polo 39",          197, "190,300", 5700, 6, 1800, 6]
C3 = ["C3", "Ford Dandoff",     205, "201,300", 5650, 4, 2200, 5]
F1 = ["F1", "Escort 46",        190, "205,300", 5300, 2, 1600, 6]
K2 = ["K2", "GTI",              201, "197,300", 5800, 2, 2000, 3]
B2 = ["B2", "VW 9012",          207, "196,300", 5750, 4, 2000, 6]
A4 = ["A4", "WRC Pop",          192, "193,300", 5400, 4, 1800, 2]
C5 = ["C5", "Cane RRC",         195, "201,300", 5600, 6, 2000, 6]

cars = [H1, E2, C3, F1, K2, B2, A4, C5]

def print_car(c):
    print("|" + c[0] + " Car Model: " + c[1] + "|")
    print("Top Speed: " + str(c[2]) + " km/h      RPM: " + str(c[4]))
    print("Hp: " + str(c[3]) + "          0-60: " + str(c[5]))
    print("CCs: " + str(c[6]) + "        Cylinders: " + str(c[7]))
    print()  


print("Cars:")
i = 1
for car in cars:
    print(i, car[1])
    i = i + 1

print()  
choice = input("Enter car number: ")


if choice.isdigit():
    index = int(choice) - 1  
    if index >= 0 and index < len(cars):
        print()
        print_car(cars[index])
    else:
        print("That car number does not exist.")
else:
    print("You must type a number.")
