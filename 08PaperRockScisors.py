#Player1
#Player2
while True:
    p1points=0
    p2points=0

    while p1points<3 and p2points<3:
        print("""Chose:
        1. Paper
        2. Rock
        3. Scisors""")
        print("Player 1:")
        p1 = int(input())
        print("Player 2:")
        p2 = int(input())
        if p1 == 1 and p2 == 2:
            p1points +=1
            print(p1points)
            print(p2points)
        elif p1 == 1 and p2 == 3:
            p2points += 1
            print(p1points)
            print(p2points)
        elif p1 == 2 and p2 == 1:
            p2points += 1
            print(p1points)
            print(p2points)
        elif p1 == 2 and p2 == 3:
            p1points += 1
            print(p1points)
            print(p2points)
        elif p1 == 3 and p2 == 1:
            p1points += 1
            print(p1points)
            print(p2points)
        elif p1 == 3 and p2 == 2:
            p2points += 1
            print(p1points)
            print(p2points)
        else:
            print("remis")
    if p1points > p2points:
        print("Player 1 WINS!!!")
    else:
        print("Player 2 WINS!!!")

    print("Do you want to play again? (Y/N)")
    a = str(input())
    if a == 'Y' or a == 'y':
        print("Lets play again")
    else:
        print("bye")
        exit()