def main():
    myArray = []
    printing_list(zero_to_100(myArray))
    quit_func()
    name_list()
    name_counter()


def zero_to_100(anyArray):
    for x in range(101):
        anyArray.append(x)
    return anyArray


def printing_list(assignedArray):
    for x in assignedArray:
        print(x)


def quit_func():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter anything. Press 'q' to quit: ")


def name_list():
    listNames = ["John", "Paul", "George", "Pete"]
    print(listNames[3])
    listNames[3] = "Ringo"
    print(listNames)
    listNames.append("Yoko")
    print(listNames)


def name_counter():
    namesToCount = ["Kenn", "Erin", "Kenn", "Kenn", "Erin", "Kenn", "Kevin", "Kevin", "Kenn", "Kenn", "Erin", "Erin",
                    "Kevin"]
    kennCount = 0
    erinCount = 0
    kevinCount = 0

    for eachName in namesToCount:
        if eachName == "Kenn":
            kennCount = kennCount + 1
        elif eachName == "Erin":
            erinCount = erinCount + 1
        elif eachName == "Kevin":
            kevinCount = kevinCount + 1
    print(f"In this list, there are {kennCount} Kenns, {erinCount} Erins, and {kevinCount} Kevins.")


main()
