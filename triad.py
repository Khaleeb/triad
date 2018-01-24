#!/usr/bin/python
# A script to show all the major, minor, and diminished triads on a fretboard


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


pboard()
