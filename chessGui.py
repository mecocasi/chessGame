#chess game
#grid based GUI
#grid() and pack() CANNOT be mixed

#imports
#PIL is pillow
import tkinter as tkin
from PIL import ImageTk,Image

#master root and window
root = tkin.Tk()
root.title("Louise's 2D Chess")
root.geometry("1300x1000")

#title
header = tkin.Label(root,text="2D Chess",)
header.config(font=("courier",20))
header.grid(column=0,row=0)

def roundLabel(moveNo):
        roundText = tkin.Label(root,text="MOVE")
        roundNo = tkin.Label(root,text=moveNo)
        roundText.grid(column=0,row=9,sticky="w")
        roundNo = roundNo.grid(column=0,row=9)

        return roundNo

def playerLabel(playerGo):
        playerText = tkin.Label(root,text=playerGo)
        playerText.grid(column=10,row=0)

        return playerGo

def labelTop():
        #putting letter labels at top of board
        topLabels = ["A","B","C","D","E","F","G","H"]
        count=1
        for letter in topLabels:
                letter = tkin.Label(root,text=letter)
                letter.grid(column=count,row=0,sticky="S")
                count+=1

def labelSide():
        #putting numbers in labels at side of board
        sideLabels = []
        sideLabels+= range(8,0,-1)
        count=1
        for num in sideLabels:
                num = tkin.Label(root,text=num)
                num.grid(column=0,row=count,sticky="E")
                count+=1

def padding():        
        #left padding #####################
        lLabel = tkin.Label(root)
        lLabel.grid(column=0,ipadx=50)

def makeBoardCanvases():
        '''Gets and stores the square images needed to make the board'''
        #because ImageTk garbage collects after function is finished
        #you must make your image variables global
        #global b
        #global w
        #b = Image.open("mats/blackSquare.jpg")
        #w = Image.open("mats/whiteSquare.jpg")
        #global bImg
        #global wImg
        #bImg = ImageTk.PhotoImage(b)
        #wImg = ImageTk.PhotoImage(w)

        global blackSquares
        global whiteSquares
        #black squares
        blackSquares = []
        blackSquares+=range(0,32)

        #white squares
        whiteSquares = []
        whiteSquares+=range(0,32)

        #assigning images to the variables inside square lists using their indexes
        #USING CANVASES instead
        #images of the pieces can be pasted inside canvases with coloured backgrounds
        #this preserves transparency and makes it easier
        for var in blackSquares:
            ind = blackSquares.index(var)
            blackSquares[ind] = tkin.Canvas(root, width=110,height=110,border=0,bg="brown",cursor="hand2")
            #blackSquares[ind].create_image(50,50,image=)
            
        for var in whiteSquares:
            ind = whiteSquares.index(var)
            whiteSquares[ind] = tkin.Canvas(root, width=110,height=110,border=0,bg="white",cursor="hand2")
            #whiteSquares[ind].create_image(50,50,image=)
            
        return blackSquares,whiteSquares
        

def positionBoardCanvases(blackSquares,whiteSquares):
        '''Positions the square images into grid columns and rows'''
        #Below uses indexes to pick & position square image objects into a grid
        #the ranges change because the indexes contain different objects
        ################change this to be valid with
        #each chunk is one row
        bCol = 0
        wCol = -1
        for num in range(0,4):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=1)
            whiteSquares[num].grid(column=wCol,row=1)

        bCol = -1
        wCol = 0
        for num in range(4,8):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=2)
            whiteSquares[num].grid(column=wCol,row=2)

        bCol = 0
        wCol = -1
        for num in range(8,12):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=3)
            whiteSquares[num].grid(column=wCol,row=3)

        bCol = -1
        wCol = 0
        for num in range(12,16):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=4)
            whiteSquares[num].grid(column=wCol,row=4)

        bCol = 0
        wCol = -1
        for num in range(16,20):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=5)
            whiteSquares[num].grid(column=wCol,row=5)

        bCol = -1
        wCol = 0
        for num in range(20,24):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=6)
            whiteSquares[num].grid(column=wCol,row=6)

        bCol = 0
        wCol = -1
        for num in range(24,28):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=7)
            whiteSquares[num].grid(column=wCol,row=7)

        bCol = -1
        wCol = 0
        for num in range(28,32):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=8)
            whiteSquares[num].grid(column=wCol,row=8)

        return blackSquares,whiteSquares

def boardSpaces(blackSquares,whiteSquares):
        #BOARD SPACES LIST
        #Merging blackSquares and whiteSquares together in an accurate index representation
        #63 total index spaces with a 0
        #32 black squares and 32 white squares
        #Because each row swaps square colour patterns from white black to black white the algorithm has to do this too
        #Leave this unindented otherwise the index spaces will mess up going downwards in 2 columns
        board = []
        for num in range(0,4):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(4,8):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(8,12):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(12,16):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(16,20):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(20,24):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(24,28):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(28,32):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        return board


#boardobjectspaces will store objects in the index that matches their position on the board
#one can then access their color through object.color
#IMPORTANT
# example = [bpawn1,wqueen,bpawn2]
boardObjectSpaces = []
for num in range(0,64):
        boardObjectSpaces.append("")


#SETS
#global variables
#stores pieces which are objects
wSet = []
bSet = []

class Piece(object):
        def __init__(self,color,mySet):
                #things that never change after initialisation
                #color of the piece
                self.color = color
                #once object is created append it into its set
                self.mySet = mySet.append(self)
        
        #properties
        alive = True
        squareInd = 0
        #####move below outside of class
        #if self.color == "b":
                #square = board[squareInd].create_image(55,55,image=self.bImage)
        #elif self.color == "w":
                #square = board[squareInd].create_image(55,55,image=self.wImage)


        # these globals represent rows and columns on the board
        # they are used for the moves() method in each piece subclass to determine where
        # a piece can move depending on where they are on the board
        global row1
        global row2
        global row3
        global row4
        global row5
        global row6
        global row7
        global row8

        global col1
        global col2
        global col3
        global col4
        global col5
        global col6
        global col7
        global col8

        row1 = range(0, 8)
        row2 = range(8, 16)
        row3 = range(16, 24)
        row4 = range(24, 32)
        row5 = range(32, 40)
        row6 = range(40, 48)
        row7 = range(48, 56)
        row8 = range(56, 64)

        col1 = range(0, 57, +8)
        col2 = range(1, 58, +8)
        col3 = range(2, 59, +8)
        col4 = range(3, 60, +8)
        col5 = range(4, 61, +8)
        col6 = range(5, 62, +8)
        col7 = range(6, 63, +8)
        col8 = range(7, 64, +8)

def doMove(event):
        event = event.widget
        print("MOVE")
        
                
class Pawn(Piece):
        #properties
        bOpen= Image.open("mats/bPawn.png")
        bImage= ImageTk.PhotoImage(bOpen)
        wOpen= Image.open("mats/wPawn.png")
        wImage= ImageTk.PhotoImage(wOpen)


        def moves(self,squareIndex):
                print("PAWN MOVE")
                #index of current square in boardSquares
                print(squareIndex,"\n")

                #plug base movements into list
                left = squareIndex - 1
                right = squareIndex + 1
                up = squareIndex - 8
                down = squareIndex + 8
                possibleSpaces = [left,right,up,down]

                #make sure the piece isn't on row ends
                #if it is then remove appropriate move from list of moves
                if squareIndex in range(0,56,+8):
                        #can't go left
                        possibleSpaces.remove(left)
                if squareIndex in range(7,63,+8):
                        #can't go right
                        possibleSpaces.remove(right)

                if squareIndex in range(0,8):
                        #can't go up
                        possibleSpaces.remove(up)

                if squareIndex in range(56,63):
                        #can't go down
                        possibleSpaces.remove(down)
                else:
                        #not at any row ends
                        pass


                #highlighting possible spaces in light purple
                for var in possibleSpaces:
                        print(var)
                        posSpace = board[var]
                        posSpace.config(bg="mediumpurple4")

                origSquare = board[squareIndex]
                print(origSquare)

                #EVENT
                #move on click
                posSpace.bind("<Button-1>",lambda event: doMove(event,origSquare = origSquare))


                #EVENT
                #deselect on right click
                #lambda is necessary so arguments can be accepted inside the function inside bind()
                origSquare.bind("<Button-3>",lambda event: deselect(event,possibleSpaces = possibleSpaces))


class Knight(Piece):
        #properties
        bOpen= Image.open("mats/bKnight.png")
        bImage= ImageTk.PhotoImage(bOpen)
        wOpen= Image.open("mats/wKnight.png")
        wImage= ImageTk.PhotoImage(wOpen)


        def moves(self,squareIndex):

                #left,right,up,down
                ul = squareIndex - 17
                ur = squareIndex - 15
                lu = squareIndex - 10
                ld = squareIndex + 6
                ru = squareIndex - 6
                rd = squareIndex + 10
                dl = squareIndex + 15
                dr = squareIndex + 17


                possibleSpaces = [ul,ur,lu,ld,ru,rd,dl,dr]

                #remove moves if at row ends
                #2 sets of ranges as the move covers 2 columns
                if squareIndex in range(0,57,+8):
                        #end left row
                        #can't go left
                        possibleSpaces.remove(ul)
                        possibleSpaces.remove(dl)
                        possibleSpaces.remove(ld)
                        possibleSpaces.remove(lu)

                elif squareIndex in range(1,58,+8):
                        #+1 to end of range because it doesn't count the last number
                        #second left row from end
                        #can't go too far left
                        if ld in possibleSpaces:
                                possibleSpaces.remove(ld)
                        if lu in possibleSpaces:
                                possibleSpaces.remove(lu)

                else:
                        pass

                if squareIndex in range(7,64,+8):
                        #can't go right
                        possibleSpaces.remove(ur)
                        possibleSpaces.remove(ru)
                        possibleSpaces.remove(rd)
                        possibleSpaces.remove(dr)

                elif squareIndex in range(6,63,+8):
                        #second right row from end
                        #can't go too far right
                        if ru in possibleSpaces:
                                possibleSpaces.remove(ru)
                        if rd in possibleSpaces:
                                possibleSpaces.remove(rd)
                else:
                        pass


                if squareIndex in range(0,9):
                        #can't go up
                        if ul in possibleSpaces:
                                possibleSpaces.remove(ul)
                        if ur in possibleSpaces:
                                possibleSpaces.remove(ur)
                        if lu in possibleSpaces:
                                possibleSpaces.remove(lu)
                        if ru in possibleSpaces:
                                possibleSpaces.remove(ru)

                elif squareIndex in range(1,10):
                        #can't go too far up
                        if ul in possibleSpaces:
                                possibleSpaces.remove(ul)
                        if ur in possibleSpaces:
                                possibleSpaces.remove(ur)
                else:
                        pass

                if squareIndex in range(56,64):
                        #can't go down
                        if ld in possibleSpaces:
                                possibleSpaces.remove(ld)
                        if rd in possibleSpaces:
                                possibleSpaces.remove(rd)
                        if dl in possibleSpaces:
                                possibleSpaces.remove(dl)
                        if dr in possibleSpaces:
                                possibleSpaces.remove(dr)

                elif squareIndex in range(55,63):
                        #can't go too far down
                        possibleSpaces.remove(dl)
                        possibleSpaces.remove(dr)
                else:
                        #not at any row ends
                        pass

                print("POSS SPACES")
                print(possibleSpaces)
                copyPossibleSpaces = possibleSpaces


                # highlighting possible spaces in light purple
                for var in copyPossibleSpaces:
                        posSpace = board[var]
                        posSpace.config(bg="mediumpurple4")

                origSquare = board[squareIndex]
                #print(origSquare)

                #print(possibleSpaces)
                # EVENT
                # move on click
                posSpace.bind("<Button-1>", lambda event: doMove(event, origSquare=origSquare))

                # EVENT
                # deselect on right click
                # lambda is necessary so arguments can be accepted inside the function inside bind()
                origSquare.bind("<Button-3>", lambda event: deselect(event, possibleSpaces=possibleSpaces))


class Rook(Piece):
        #properties
        bOpen= Image.open("mats/bRook.png")
        bImage= ImageTk.PhotoImage(bOpen)
        wOpen= Image.open("mats/wRook.png")
        wImage= ImageTk.PhotoImage(wOpen)

        def moves(self,squareIndex):

                #left,right,up,down
                #each variable represents a square

                #LEFT
                left = squareIndex - 1
                l2 = left-1
                l3 = l2-1
                l4 = l3-1
                l5 = l4-1
                l6 = l5-1
                l7 = l6-1
                #l8 = l7-1

                leftBunch = [left,l2,l3,l4,l5,l6,l7]

                #RIGHT
                right = squareIndex + 1
                r2 = right+1
                r3 = r2+1
                r4 = r3+1
                r5 = r4+1
                r6 = r5+1
                r7 = r6+1
                #r8 = r7+1

                rightBunch = [right,r2,r3,r4,r5,r6,r7]

                #UP
                up = squareIndex - 8
                u2 = up-8
                u3 = u2-8
                u4 = u3-8
                u5 = u4-8
                u6 = u5-8
                u7 = u6-8
                #u8 = u7-8

                upBunch = [up,u2,u3,u4,u5,u6,u7]

                #DOWN
                down = squareIndex + 8
                d2 = down+8
                d3 = d2+8
                d4 = d3+8
                d5 = d4+8
                d6 = d5+8
                d7 = d6+8
                #d8 = d7+8

                downBunch = [down,d2,d3,d4,d5,d6,d7]

                #got rid of 8s because we also count the piece's square

                #possibleSpaces = [left,right,up,down]
                possibleSpaces = []
                upSpaces = []
                downSpaces = []

                rows = [row1,row2,row3,row4,row5,row6,row7,row8]
                cols = [col1,col2,col3,col4,col5,col6,col7,col8]

                upCount = 0
                downCount = 7

                #up and down
                for row in rows:
                        if squareIndex in row:
                                for num in range(0,downCount):
                                        possibleSpaces.append(downBunch[num])

                                for num in range(0,upCount):
                                        possibleSpaces.append(upBunch[num])
                        else:
                                upCount += 1
                                downCount -= 1
                                continue

                #left and right
                leftCount = 0
                rightCount = 7

                for col in cols:
                        if squareIndex in col:
                                for num in range(0, leftCount):
                                        possibleSpaces.append(leftBunch[num])

                                for num in range(0, rightCount):
                                        possibleSpaces.append(rightBunch[num])
                        else:
                                leftCount += 1
                                rightCount -= 1
                                continue


                copyPossibleSpaces = possibleSpaces

                print(copyPossibleSpaces)

                # highlighting possible spaces in light purple
                for var in copyPossibleSpaces:
                        posSpace = board[var]
                        posSpace.config(bg="mediumpurple4")

                origSquare = board[squareIndex]
                #print(origSquare)

                #print(possibleSpaces)
                # EVENT
                # move on click
                posSpace.bind("<Button-1>", lambda event: doMove(event, origSquare=origSquare))

                # EVENT
                # deselect on right click
                # lambda is necessary so arguments can be accepted inside the function inside bind()
                origSquare.bind("<Button-3>", lambda event: deselect(event, possibleSpaces=possibleSpaces))


class Bishop(Piece):
        #properties
        bOpen= Image.open("mats/bBishop.png")
        bImage= ImageTk.PhotoImage(bOpen)
        wOpen= Image.open("mats/wBishop.png")
        wImage= ImageTk.PhotoImage(wOpen)

        def endBreaker(self):
                pass


        def moves(self,squareIndex):

                # bishop moves diagonally
                # north west
                nw = squareIndex - 9
                nw2 = nw - 9
                nw3 = nw2 - 9
                nw4 = nw3 - 9
                nw5 = nw4 - 9
                nw6 = nw5 - 9
                nw7 = nw6 - 9

                nwBunch = [nw, nw2, nw3, nw4, nw5, nw6, nw7]

                # north east
                ne = squareIndex - 7
                ne2 = ne - 7
                ne3 = ne2 - 7
                ne4 = ne3 - 7
                ne5 = ne4 - 7
                ne6 = ne5 - 7
                ne7 = ne6 - 7

                neBunch = [ne, ne2, ne3, ne4, ne5, ne6, ne7]

                # south west
                sw = squareIndex + 7
                sw2 = sw + 7
                sw3 = sw2 + 7
                sw4 = sw3 + 7
                sw5 = sw4 + 7
                sw6 = sw5 + 7
                sw7 = sw6 + 7

                swBunch = [sw, sw2, sw3, sw4, sw5, sw6, sw7]

                # south east
                se = squareIndex + 9
                se2 = se + 9
                se3 = se2 + 9
                se4 = se3 + 9
                se5 = se4 + 9
                se6 = se5 + 9
                se7 = se6 + 9

                seBunch = [se, se2, se3, se4, se5, se6, se7]

                possibleSpaces = []


                #rows = [row1, row2, row3, row4, row5, row6, row7, row8]
                #cols = [col1, col2, col3, col4, col5, col6, col7, col8]

                #ENDS used to determine the end of board
                end1 = range(0,8)
                end2 = range(0,57,8)
                end3 = range(56,64)
                end4 = range(7,57,8)

                ends = [end1,end2,end3,end4]
                endsIndexes = []

                #this is needed to convert the endsIndexes to numbers as the ends only holds ranges
                #meaning I would have to do a double loop break further on
                for ranges in ends:
                        for numbs in ranges:
                                endsIndexes.append(numbs)

                #calculate possible spaces using movement bunches and end numbers
                #if one of the nums in the bunches hits an end then the loop stops and moves onto the next direction loop
                if squareIndex:
                        for num in nwBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        possibleSpaces.append(num)

                        for num in neBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        print(num)
                                        possibleSpaces.append(num)

                        for num in seBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        possibleSpaces.append(num)

                        for num in swBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        possibleSpaces.append(num)


                print(possibleSpaces)

                copyPossibleSpaces = possibleSpaces

                # print(copyPossibleSpaces)

                # highlighting possible spaces in light purple
                for var in copyPossibleSpaces:
                        posSpace = board[var]
                        posSpace.config(bg="mediumpurple4")

                origSquare = board[squareIndex]
                # print(origSquare)

                # print(possibleSpaces)
                # EVENT
                # move on click
                posSpace.bind("<Button-1>", lambda event: doMove(event, origSquare=origSquare))

                # EVENT
                # deselect on right click
                # lambda is necessary so arguments can be accepted inside the function inside bind()
                origSquare.bind("<Button-3>", lambda event: deselect(event, possibleSpaces=copyPossibleSpaces))



        
class Queen(Piece):
        #properties
        bOpen= Image.open("mats/bQueen.png")
        bImage= ImageTk.PhotoImage(bOpen)
        wOpen= Image.open("mats/wQueen.png")
        wImage= ImageTk.PhotoImage(wOpen)

        def moves(self,squareIndex):


                # DIAGONALS
                # north west
                nw = squareIndex - 9
                nw2 = nw - 9
                nw3 = nw2 - 9
                nw4 = nw3 - 9
                nw5 = nw4 - 9
                nw6 = nw5 - 9
                nw7 = nw6 - 9

                nwBunch = [nw, nw2, nw3, nw4, nw5, nw6, nw7]

                # north east
                ne = squareIndex - 7
                ne2 = ne - 7
                ne3 = ne2 - 7
                ne4 = ne3 - 7
                ne5 = ne4 - 7
                ne6 = ne5 - 7
                ne7 = ne6 - 7

                neBunch = [ne, ne2, ne3, ne4, ne5, ne6, ne7]

                # south west
                sw = squareIndex + 7
                sw2 = sw + 7
                sw3 = sw2 + 7
                sw4 = sw3 + 7
                sw5 = sw4 + 7
                sw6 = sw5 + 7
                sw7 = sw6 + 7

                swBunch = [sw, sw2, sw3, sw4, sw5, sw6, sw7]

                # south east
                se = squareIndex + 9
                se2 = se + 9
                se3 = se2 + 9
                se4 = se3 + 9
                se5 = se4 + 9
                se6 = se5 + 9
                se7 = se6 + 9

                seBunch = [se, se2, se3, se4, se5, se6, se7]

                possibleSpaces = []

                # rows = [row1, row2, row3, row4, row5, row6, row7, row8]
                # cols = [col1, col2, col3, col4, col5, col6, col7, col8]

                # ENDS used to determine the end of board
                end1 = range(0, 8)
                end2 = range(0, 57, 8)
                end3 = range(56, 64)
                end4 = range(7, 57, 8)

                ends = [end1, end2, end3, end4]
                endsIndexes = []

                # this is needed to convert the endsIndexes to numbers as the ends only holds ranges
                # meaning I would have to do a double loop break further on
                for ranges in ends:
                        for numbs in ranges:
                                endsIndexes.append(numbs)

                # calculate possible spaces using movement bunches and end numbers
                # if one of the nums in the bunches hits an end then the loop stops and moves onto the next direction loop
                if squareIndex:
                        for num in nwBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        possibleSpaces.append(num)

                        for num in neBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        print(num)
                                        possibleSpaces.append(num)

                        for num in seBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        possibleSpaces.append(num)

                        for num in swBunch:
                                if num in endsIndexes:
                                        possibleSpaces.append(num)
                                        break
                                elif num < 0 or num > 63:
                                        break
                                else:
                                        possibleSpaces.append(num)

                # STRAIGHTS
                # left,right,up,down
                # each variable represents a square

                # LEFT
                left = squareIndex - 1
                l2 = left - 1
                l3 = l2 - 1
                l4 = l3 - 1
                l5 = l4 - 1
                l6 = l5 - 1
                l7 = l6 - 1
                # l8 = l7-1

                leftBunch = [left, l2, l3, l4, l5, l6, l7]

                # RIGHT
                right = squareIndex + 1
                r2 = right + 1
                r3 = r2 + 1
                r4 = r3 + 1
                r5 = r4 + 1
                r6 = r5 + 1
                r7 = r6 + 1
                # r8 = r7+1

                rightBunch = [right, r2, r3, r4, r5, r6, r7]

                # UP
                up = squareIndex - 8
                u2 = up - 8
                u3 = u2 - 8
                u4 = u3 - 8
                u5 = u4 - 8
                u6 = u5 - 8
                u7 = u6 - 8
                # u8 = u7-8

                upBunch = [up, u2, u3, u4, u5, u6, u7]

                # DOWN
                down = squareIndex + 8
                d2 = down + 8
                d3 = d2 + 8
                d4 = d3 + 8
                d5 = d4 + 8
                d6 = d5 + 8
                d7 = d6 + 8
                # d8 = d7+8

                downBunch = [down, d2, d3, d4, d5, d6, d7]

                # got rid of 8s because we also count the piece's square

                # possibleSpaces = [left,right,up,down]
                # possibleSpaces = []
                upSpaces = []
                downSpaces = []

                rows = [row1, row2, row3, row4, row5, row6, row7, row8]
                cols = [col1, col2, col3, col4, col5, col6, col7, col8]

                upCount = 0
                downCount = 7

                # up and down
                for row in rows:
                        if squareIndex in row:
                                for num in range(0, downCount):
                                        possibleSpaces.append(downBunch[num])

                                for num in range(0, upCount):
                                        possibleSpaces.append(upBunch[num])
                        else:
                                upCount += 1
                                downCount -= 1
                                continue

                # left and right
                leftCount = 0
                rightCount = 7

                for col in cols:
                        if squareIndex in col:
                                for num in range(0, leftCount):
                                        possibleSpaces.append(leftBunch[num])

                                for num in range(0, rightCount):
                                        possibleSpaces.append(rightBunch[num])
                        else:
                                leftCount += 1
                                rightCount -= 1
                                continue

                copyPossibleSpaces = possibleSpaces

                # print(copyPossibleSpaces)

                # highlighting possible spaces in light purple
                for var in copyPossibleSpaces:
                        posSpace = board[var]
                        posSpace.config(bg="mediumpurple4")

                origSquare = board[squareIndex]
                # print(origSquare)

                # print(possibleSpaces)
                # EVENT
                # move on click
                posSpace.bind("<Button-1>", lambda event: doMove(event, origSquare=origSquare))

                # EVENT
                # deselect on right click
                # lambda is necessary so arguments can be accepted inside the function inside bind()
                origSquare.bind("<Button-3>", lambda event: deselect(event, possibleSpaces=copyPossibleSpaces))


class King(Piece):
        #properties
        bOpen= Image.open("mats/bKing.png")
        bImage= ImageTk.PhotoImage(bOpen)
        wOpen= Image.open("mats/wKing.png")
        wImage= ImageTk.PhotoImage(wOpen)

        def moves(self,squareIndex):
                #King moves 1 square horizontally,vertically, or diagonally
                pass

#############           

def setStartPosition(bSet,wSet,board,boardObjectSpaces):
        #starting positions
        #sets hold the objects
        #black
        for num in range(0,16):
                piece = bSet[num]
                boardObjectSpaces[num] = piece
                display = bSet[num].bImage
                place = board[num].create_image(55,55,image=display)
                ########this is making a one when it should be storing an object
                bPlaces[num] = piece

        #white
        setCounter = 0
        for num in range(63,47,-1):
                piece = wSet[setCounter]
                boardObjectSpaces[num] = piece
                display = wSet[setCounter].wImage
                place = board[num].create_image(55,55,image=display)
                wPlaces[num] = piece
                setCounter+=1

        return bSet,wSet,board,bPlaces,wPlaces,boardObjectSpaces


def pickPiece(setMove):
        #change cursor to plus on player's own pieces they can select
        if setMove == "w":
                places = wPlaces
        elif setMove == "b":
                places = bPlaces
                
        for piece in places:
                if piece != "":
                        pIndex = places.index(piece)
                        fullCanvas = board[pIndex]
                        fullCanvas.config(cursor="plus")
                        fullCanvas.bind("<Button-1>",playerSelect)
        return places

def playerSelect(event):
        #ON CLICK EVENT
        #get caller/widget that called
        caller = event.widget
        #change background color
        caller.config(bg="mediumpurple1")
        squareIndex = board.index(caller)
        piece = boardObjectSpaces[squareIndex]

        for counter in places:
                if counter != "" or places[squareIndex]:
                        pIndex = places.index(counter)
                        fullCanvas = board[pIndex]
                        fullCanvas.config(cursor="plus")
                        fullCanvas.bind("<Button-1>",unbind)

        #deselect with the right mouse button


        possibleMoves(piece,squareIndex)
        ############################unbind so that we can only select one piece
        ##########unbind selected piece if rigght click and allow others to be selected

def unbind(event):
        pass

def deselect(event,possibleSpaces):
        print("DESELECT")
        event = event.widget
        #make sure the background color returns to its original color
        #original square dehighlight
        if event in whiteSquares:
                bgcol = "white"
        elif event in blackSquares:
                bgcol = "brown"

        event.config(bg=bgcol)

        #since possibleSquares contains the indexes we use them to get the canvas widget objects
        selCanvases = []
        #print(possibleSpaces)
        for index in possibleSpaces:
                selCanvas = board[index]
                selCanvases.append(selCanvas)

        #possible squares to move to dehighlight
        for canvas in selCanvases:
                if canvas in whiteSquares:
                        canvas.config(bg="white")
                elif canvas in blackSquares:
                        canvas.config(bg="brown")



        #be able to select pieces again. Jump back to start.
        pickPiece(setMove)

def possibleMoves(piece,squareIndex):
        #piece = piece
        #index = index
        #piece is the object
        #index is the board canvas
        #because the moves will be different for different piece types we access the move method of the piece object
        print("POSMOVE")
        piece.moves(squareIndex)


def playerMove(event,active,board,boardObjectSpaces):
        print("move")
        active.calculateMove(board,boardObjectSpaces)
        


#OBJECTS
#16 total in each set
#laid out in their starting order so they are instaniated that way inside their set and boardObjectSpaces
#black objects
bRook1 = Rook("b",bSet)
bKnight1 = Knight("b",bSet)
bBishop1 = Bishop("b",bSet)
bQueen = Queen("b",bSet)
bKing = King("b",bSet)
bBishop2 = Bishop("b",bSet)
bKnight2 = Knight("b",bSet)
bRook2 = Rook("b",bSet)
bPawn1 = Pawn("b",bSet)
bPawn2 = Pawn("b",bSet)
bPawn3 = Pawn("b",bSet)
bPawn4 = Pawn("b",bSet)
bPawn5 = Pawn("b",bSet)
bPawn6 = Pawn("b",bSet)
bPawn7 = Pawn("b",bSet)
bPawn8 = Pawn("b",bSet)

#white objects
wRook1 = Rook("w",wSet)
wKnight1 = Knight("w",wSet)
wBishop1 = Bishop("w",wSet)
wKing = King("w",wSet)
wQueen = Queen("w",wSet)
wBishop2 = Bishop("w",wSet)
wKnight2 = Knight("w",wSet)
wRook2 = Rook("w",wSet)
wPawn1 = Pawn("w",wSet)
wPawn2 = Pawn("w",wSet)
wPawn3 = Pawn("w",wSet)
wPawn4 = Pawn("w",wSet)
wPawn5 = Pawn("w",wSet)
wPawn6 = Pawn("w",wSet)
wPawn7 = Pawn("w",wSet)
wPawn8 = Pawn("w",wSet)

#print(wSet)

def fillPlaces(wPlaces,bPlaces):
        '''fills the places trackers with num of spaces on board so positions of pieces can be tracked
                for black and white pieces seperately'''
        for num in range(0,64):
                wPlaces.append("")
                bPlaces.append("")

        return wPlaces,bPlaces

def turn(setMove):
        if setMove == "w":
                for space in wPlaces:
                        if space != "":
                                spaceIndex = wPlaces.index(space)
                                board[spaceIndex]
        
        
#TRACKERS        
moveNo = 0
playerGo = "It's white's move"
setMove = "w"
wPlaces = []
bPlaces = []

#FUNCTIONS
wPlaces,bPlaces = fillPlaces(wPlaces,bPlaces)
labelTop()
labelSide()
roundNo = roundLabel(moveNo)
playerGo = playerLabel(playerGo)
blackSquares,whiteSquares = makeBoardCanvases()
blackSquares,whiteSquares = positionBoardCanvases(blackSquares,whiteSquares)
board = boardSpaces(blackSquares,whiteSquares)
bSet,wSet,board,bPlaces,wPlaces,boardObjectSpaces = setStartPosition(bSet,wSet,board,boardObjectSpaces)
places = pickPiece(setMove)

#print(bPlaces)
#print("\n")
#print(wPlaces)
#print("\n")
#print(boardObjectSpaces)

#EVENTS
#need to select a square and then move
#when canvas clicked run function
#board is full of canvases




#for canvas in board:
        #canvas.bind("<Button-1>",playerSelect)

        

#print(blackSquares)
#print(whiteSquares)
    
#board = blackSquares + whiteSquares
#print(board)


#####EXAMPLE
#bPawnOpen = Image.open("mats/wKing.png")
#bPawnImg = ImageTk.PhotoImage(bPawnOpen)
#board[10].create_image(55,55,image=bPawnImg)

#bPawnOpen = Image.open("mats/wKing.png")
#bPawnImg = ImageTk.PhotoImage(bPawnOpen)
#whiteSquares[2].create_image(55,55,image=bPawnImg)

#starting positions
#bPawnOpen = Image.open("mats/bPawn.png")
#bPawnImg = ImageTk.PhotoImage(bPawnOpen)
#for num in range(4,8):
        #blackSquares[num].create_image(55,55,image=bPawnImg)
        #whiteSquares[num].create_image(55,55,image=bPawnImg)

        #event driven

######## Labels don't support transparency........convert everything to a canvas!!

#use whiteSquares and blackSquares as indexes
#if someone picks 1A then
#or make new data struct with
#["w","b","w","b"]
#then if someone picks black correspond to another struct
#[1,2,3,4,5]

#square = board[squareInd].create_image(55,55,image=self.bImage)

#or just
#[["w",1],["b",1],]

#main
root.mainloop()        


                
                
                



