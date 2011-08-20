def printl(list):
    print "["
    for elet in list:
        print "\t" + str(elet)
    print "]"

row = [-2] * 10
board = [row] * 20
printl(board)

pieces = [0,0,0]
pieces[0] = [[0,0,0,0]]
pieces[1] = [[1,1,1], [-2,-2,1]]
pieces[2] = [[2,2], [2,2]]
printl(pieces)


