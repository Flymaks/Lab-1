import math
import os
import time
RED = '\u001b[41m'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK= '\u001b[40m'
END = '\u001b[0m'
#Flag of Lithuania
def flag():
    print("Flag of Lithuania") 
    for i in range(6):
        if i < 2:
            print(f"{YELLOW}{' ' * 24}{END}")
        elif i < 4:
            print(f"{GREEN}{' ' * 24}{END}")
        else:
            print(f"{RED}{' ' * 24}{END}")
# pattern e
def drawlines(offset, line):
    of =  ' ' * offset
    st = ' ' * line
    mid = ' ' * (line *(line - 1))
    for width in range(2):
        print(f"{WHITE}{of}{BLACK}{st}{WHITE}{mid}{BLACK}{st}{WHITE}{of}{END}",end="")
    print()
def pattern():
    print("Pattern e")
    for height in range(5):
            offset = 0
            for i in range(6):
                drawlines(offset, 6 - i)
                offset += 6 - i
# y = |x|in a first quater ->y = x
def function():
    print("y = |x|in a first quater")
    print(f"{BLACK}{'^'}{END}")
    for i in range(8):
        print(f"{BLACK}{'|'}{WHITE}{' ' * ((2 *(8 - i))-1)}{BLACK}{'*'}{END}")
    print(f"{BLACK}{'*------------------>'}{END}")
    print()
#The modulo average of the numbers in even and odd positions
def file():
    print("The modulo average of the numbers in even and odd positions in file sequence")
    file = open('sequence.txt', 'r')
    list1 = []
    for number in file:
        list1.append(float(number))
    len_list = len(list1)
    even = 0
    odd = 0
    for i in range(len_list):
        if i % 2 == 0:
            even += abs(list1[i])
        else:
            odd += abs(list1[i])
    even = round(even / math.ceil(len_list / 2), 1)
    odd = round(odd / (len_list // 2), 1)
    file.close()
    s = ""
    for i in range(11):
        s += str(i)
        if i < 10:
            s += "-" * 9
    print(f"{BLACK}{s}{END}")
    print(f"{RED}{" " * ((int(10 * even))- len(str(even)))}{str(even)}{END}")
    print(f"{BLUE}{" " * ((int(10 * odd))- len(str(odd)))}{str(odd)}{END}")
    print(f"{RED}even pos{WHITE}     {BLUE}odd pos{END}")
#ДОП
def heart(off1, off2):
    print(f"{WHITE}{" " * off1}{BLACK}{"<3"}{WHITE}{" " * off2}", end= "")
    print(f"{BLACK}{"<3"}{WHITE}{" " * (60 - off1 - off2 - 4)}{END}")
def anim():
    for i in range(100):
        print(f"{WHITE}{" " * 20}{BLACK}{"<3" * 11}{WHITE}{" " * 18}{END}")
        for i in range(10):
            print(f"{WHITE}{" " * 29}{BLACK}{"<3" * 2}{WHITE}{" " * 27}{END}")
        print(f"{WHITE}{" " * 20}{BLACK}{"<3" * 11}{WHITE}{" " * 18}{END}")   
        time.sleep(1)
        os.system("cls")
        print(f"{WHITE}{" " * 60}")
        print(f"{WHITE}{" " * 30}{BLACK}{"<3"}{WHITE}{" " * 28}{END}")
        coordinates = [(28, 2),(26, 6),(24, 6),(22, 6),(24, 6),(26, 6),(28, 2)]
        for i, j in coordinates:
            heart(i, j)
        print(f"{WHITE}{" " * 30}{BLACK}{"<3"}{WHITE}{" " * 28}{END}")
        print(f"{WHITE}{" " * 60}")
        time.sleep(1)
        os.system("cls")
        print(f"{WHITE}{" " * 24}{BLACK}{"<3"}{WHITE}{" " * 9}{BLACK}{"<3"}{END}")
        for i in range(7):
            print(f"{WHITE}{" " * 24}{BLACK}{"<3"}{WHITE}{" " * (7-i)}",end ="")
            print(f"{BLACK}{"<3"}{WHITE}{" " * (i +1)}{BLACK}{"<3"}{END}")
        print(f"{WHITE}{" " * 25}{BLACK}{"<3"}{WHITE}{" " * 9}{BLACK}{"<3"}{END}")
        time.sleep(1)
        os.system("cls")

if __name__ == "__main__":
    flag()
    pattern()
    function()
    file()
    #anim()
