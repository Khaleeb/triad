#!/usr/bin/python
# A script to show all the major, minor, and diminished triads on a fretboard
import sys


# Fretboard Point Matrix
Points = [[0 for x in range(25)] for y in range(6)]
for s in range(6):
    for f in range(25):
        if(f==3 or f==5 or f==7 or f==9 or f==15 or f==17 or f==19 or f==21):
            Points[s][f] = "*"
        elif(f==12 or f==24):
            Points[s][f] = "|"
        elif(f==0):
            Points[s][f] = "O"
        else:
            Points[s][f] = "-"


def pboard():
    for s in range(6):
        for f in range(25):
            print(Points[s][f], end=" ")
        print("")


Notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]


def Calc(root,ty):
    global first
    global third
    global fifth
    if(ty == 'M'):
        three = 4
        five = 7
    elif(ty == 'm'):
        three = 3
        five = 7
    elif(ty == 'd' or ty == 'D'):
        three = 3
        five = 6
    else:
        print("Input Error")
        sys.exit()


    first = root
    third = root + three
    fifth = root + five
    if(third > 11):
        third = third - 12
    if(fifth > 11):
        fifth = fifth - 12


def Indexer(a,b,c):
    for s in range(6):
        for f in range(25):
            index = (s * 25) + f
            if(s == 0):
                I = (f + 7) % 12
            elif(s == 1):
                I = (f + 2) % 12
            elif(s == 2):
                I = (f + 10) % 12
            elif(s == 3):
                I = (f + 5) % 12
            elif(s == 4):
                I = (f % 12)
            elif(s == 5):
                I = (f + 7) %  12

            if(I == a):
                Points[s][f] = "1"
            elif(I == b):
                Points[s][f] = "3"
            elif(I == c):
                Points[s][f] = "5"


inp = input("Root Note(# only): ")
root = Notes.index(inp)
ty = input("M/m/D: ")
Calc(root,ty)
Indexer(first,third,fifth)
print ("1: %s\n3: %s\n5: %s" % (Notes[first],Notes[third],Notes[fifth]))
print("0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
pboard()
