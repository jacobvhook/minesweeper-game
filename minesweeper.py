from minefield import MineField

def main():
    width = 10
    height = 10
    num_mines = 5

    lost = False

    minefield = MineField(width,height,num_mines)
    minefield.displayminefield()

    while not lost:
        xguess = int(input("Pick x coordinate "))
        yguess = int(input("Pick y coordinate "))

        lost = minefield.guessspot(xguess,yguess)
        minefield.displayminefield()

    print('Sorry you lost!')
    minefield.displaywholeminefield()

if __name__ == '__main__':
    main()