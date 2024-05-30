from termcolor import cprint

import os
import time
os.system("cls")
print("nama : andri adrian")
print("nim  : 2310432043")
print("sift : 4")
def lilin():
    api= ("           *  *  *")
    cprint(api, "red")
    lilin= ("           |  |  |")
    cprint(lilin, "white")
lilin()
def kue_ultah():
    for i in range (1):
        print(" "*9, end=" ")
        lapisan_1 = ("~"*8)
        cprint(lapisan_1, "black", "on_magenta")
        print(" "*7, end= " ")
        lapisan_2 =("()"*6)
        cprint (lapisan_2, "black", "on_light_blue")
        print(" "*5, end=" ")
        lapisan_3 = ("~"*16)
        cprint(lapisan_3, "black", "on_magenta") 
        print(" "*3, end=" ")
        lapisan_4 = ("()"*10)
        cprint(lapisan_4, "black", "on_light_blue")
        print(" "*1, end=" ")
        lapisan_5 = ("@"*24)
        cprint(lapisan_5, "black", "on_magenta")
        print()
        time.sleep(1)
        print(" "*5, end= " ")
        kata= ("HAPPY BIRTHDAY !!")
        cprint(kata, "red")
        print()
        print()
kue_ultah()
