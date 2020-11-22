mainList = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
answer = ' '

# Printing Board
def printBoard(mylist):
    print(mylist[1]+"|"+mylist[2]+"|"+mylist[3])
    print("-|-|-")
    print(mylist[4]+"|"+mylist[5]+"|"+mylist[6])
    print("-|-|-")
    print(mylist[7]+"|"+mylist[8]+"|"+mylist[9])
# PrintBoard End


# Main Function
def func():
    count = 0
    while count<=9:

        print('Choose a position to place your marker')
        printBoard(mainList)

        ans = int(input('Enter position number'))
        if count%2==0:
            mainList[ans] = player1
        else:
            mainList[ans] = player2

        if check(player1):
            printBoard(mainList)
            print(f"The winner is",player1)
            break

        if check(player2):
            printBoard(mainList)
            print(f"The winner is ", player2)
            break

        count = count + 1

# Main Func end

#Checking Winner

def check(marker):
    if mainList[1]== marker and mainList[2] == marker and mainList[3] == marker:
        return True
    if mainList[4] == marker and mainList[5] == marker and mainList[6] == marker:
        return True
    if mainList[7] == marker and mainList[8] == marker and mainList[9] == marker:
        return True
    if mainList[1] == marker and mainList[4] == marker and mainList[7] == marker:
        return True
    if mainList[2] == marker and mainList[5] == marker and mainList[8] == marker:
        return True
    if mainList[3] == marker and mainList[6] == marker and mainList[9] == marker:
        return True
    if mainList[1] == marker and mainList[5] == marker and mainList[9] == marker:
        return True
    if mainList[3] == marker and mainList[5] == marker and mainList[7] == marker:
        return True


######################################################################################################

while (answer != 'N' or answer != 'n'):

    mainList = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1 = input('Choose X or O')
    if player1 == 'x' or player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    func()

    answer = input("Press N if you want to quit or anything else to PLAY AGAIN")















