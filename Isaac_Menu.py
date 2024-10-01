import random

def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice "))
        if user == 1:
            PrintRectangle(3.55, 2.54)
        if user == 2:
            UiRectangle()
        if user == 3:
            GolfChart(int(input("what hole are you on?")), int(input("what is the par for the hole?")), int(input("how manny strokes did it take?")))
        if user == 4:
            Loops(int(input("what is the starting number?")), int(input("what is the ending number?")))
        if user == 5:
            Dice(int(input("How mant times do you want to roll the dice?")))
        if user == 6:
            isPalindrome(input("What word do you think is palindrome?"))
        if user == 7:
            totalPalindrome(int(input("what is the starting int?")),int(input("what is the ending int?")))
        if user == 8:
            print("thank you for using the menu")


def printMenu():
    print("1. printRectangle")
    print("2. printRectangle")
    print("3. golfChart")
    print("4. loops")
    print("5. Dice")
    print("6. reverseString")
    print("7. totalPalindrome")
    print("8. exit")

def PrintRectangle(x,y):
    print("A rectangle with the height of:", x, " and a width of:", y," has an area of:", x*y, "and a perimeter of:", (x*2)+(y*2))
def UiRectangle():
    hite = int(input("what is the hight of it?"))
    length = int(input("what is the with of it?"))
    printRectangle(hite, length)
def GolfChart(hole,par,hits):
    slang = ""
    temp = hits - par

    if temp <= -5:
        slang += "Ostrich"
    elif temp == -4:
        slang += "Condor"
    elif temp == -3:
        slang += "Albatross"
    elif temp == -2:
        slang += "Eagle"
    elif temp == -1:
        slang += "Birdie"
    elif temp == 0:
        slang += "Even Par"
    elif temp == 1:
        slang += "Bogey"
    elif temp == 2:
        slang += "Double Bogey"
    elif temp == 3:
        slang += "Triple Bogey"
    elif temp == 4:
        slang += "4 over par"
    elif temp >= 5:
        slang += temp +" over par"

    if hits == 1:
        slang += ", Hole in One!"
    elif hits == 4:
        slang += ", Sailboat"
    elif hits == 8:
        slang += ", SnowMan"
    elif hits == 10:
        slang += ", Bo Derek!"

    if hits == par*2:
        slang += ", with a Beagle"

    print("On hole #", hole, "a par of ", par, " you shot a", slang)

def Loops(start, end):
    if start >= end:
        start = int(input("what is the starting number?"))
        end = int(input("what is the ending number?"))
    total = 0
    for x in range(start, end):
        if x % 3 != 0 and x % 4 != 0 and x % 5 != 0:
            total += x
    print("Starting number: ", start)
    print("Ending number: ", end)
    print("Total: ", total)

def Dice(x):
    two = 0
    three = 0
    fore = 0
    five = 0
    six = 0
    seven = 0
    eate = 0
    nine = 0
    ten = 0
    elevin = 0
    twelve = 0
    doubles = 0
    for ben in range(1,x+1):
        tea = (random.randint(1,6))
        bag = (random.randint(1,6))
        if tea == bag:
            doubles += 1
        tea += bag
        if tea == 2:
            two += 1
        if tea == 3:
            three += 1
        if tea == 4:
            fore += 1
        if tea == 5:
            five += 1
        if tea == 6:
            six += 1
        if tea == 7:
            seven += 1
        if tea == 8:
            eate += 1
        if tea == 9:
            nine += 1
        if tea == 10:
            ten += 1
        if tea == 11:
            elevin += 1
        if tea == 12:
            twelve += 1
    print("2 -", two,"- ", (two/x)*100, "%")
    print("3 -", three,"- ", (three/x)*100, "%")
    print("4 -", fore,"- ", (fore/x)*100, "%")
    print("5 -", five, "- ", (five/x)*100, "%")
    print("6 -", six,"- ", (six/x)*100, "%")
    print("7 -", seven,"- ", (seven/x)*100, "%")
    print("8 -", eate,"- ", (eate/x)*100, "%")
    print("9 -", nine,"- ", (nine/x)*100, "%")
    print("10 -", ten,"- ", (ten/x)*100, "%")
    print("11 -", elevin,"- ", (elevin/x)*100, "%")
    print("12 -", twelve,"- ", (twelve/x)*100, "%")
    print("doubles -", doubles ,"-", (doubles/x)*100, "%")


def reverseString(word):
    temp = ""

    for x in range(len(word)-1,-1,-1):
        temp += word[x]
    return temp

def isPalindrome(word):
    if word == reverseString(word):
        return True
    else:
        return False

def isNumberPalindrome(num):
    x = str(num)
    if isPalindrome(x) == True:
        return True
    else:
        return False


def totalPalindrome(start, end):
    count = 0
    while start < end+1:
        if isNumberPalindrome(start) == True:
            count += start
        start += 1
    print(count)


def main():
    menu()

if __name__ == '__main__':
    main()
