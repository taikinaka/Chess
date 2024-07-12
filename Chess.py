import pygame
import random
pygame.init()

# Set up the drawing window
scrnSize=600
scrn = pygame.display.set_mode([scrnSize, scrnSize])

pygame.display.set_caption('Game')
 
# create a surface object, image is drawn on it.
B_Pawn = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\B_Pawn.png").convert_alpha()
B_King = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\B_King.png").convert_alpha()
B_Queen = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\B_Queen.png").convert_alpha()
B_Knight = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\B_Knight.png").convert_alpha()
B_Bishop = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\B_Bishop.png").convert_alpha()
B_Rook = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\B_Rook.png").convert_alpha()

W_Pawn = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\W_Pawn.png").convert_alpha()
W_Bishop = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\W_Bishop.png").convert_alpha()
W_King = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\W_King.png").convert_alpha()
W_Knight = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\W_Knight.png").convert_alpha()
W_Queen = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\W_Queen.png").convert_alpha()
W_Rook = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\W_Rook.png").convert_alpha()

B_win = pygame.transform.scale(B_King, (96, 153))
B_King = pygame.transform.scale(B_King, (96/2, 153/2))
B_Pawn = pygame.transform.scale(B_Pawn, (96/2, 153/2))
B_Queen = pygame.transform.scale(B_Queen, (96/2, 153/2))
B_Knight = pygame.transform.scale(B_Knight, (96/2, 153/2))
B_Bishop = pygame.transform.scale(B_Bishop, (96/2, 153/2))
B_Rook = pygame.transform.scale(B_Rook, (96/2, 153/2))

W_win = pygame.transform.scale(W_King, (96, 153))
W_Pawn = pygame.transform.scale(W_Pawn, (96/2, 153/2))
W_Bishop = pygame.transform.scale(W_Bishop, (96/2, 153/2))
W_King = pygame.transform.scale(W_King, (96/2, 153/2))
W_Knight = pygame.transform.scale(W_Knight, (96/2, 153/2))
W_Queen = pygame.transform.scale(W_Queen, (96/2, 153/2))
W_Rook = pygame.transform.scale(W_Rook, (96/2, 153/2))

#Nothing = pygame.image.load("C:\\Users\\taiki\\Desktop\\Python\\Project1\\ChessPieces\\Nothing.png").convert_alpha()


B_background = pygame.transform.rotate(B_Pawn, 45)
W_background = pygame.transform.rotate(W_Pawn, 360-45)
boardSurface=[[B_Rook,B_Knight,B_Bishop,B_Queen,B_King,B_Bishop,B_Knight,B_Rook],[B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn],
           [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn],
           [W_Rook,W_Knight,W_Bishop,W_Queen,W_King,W_Bishop,W_Knight,W_Rook]]
board=[["B_Rook","B_Knight","B_Bishop","B_Queen","B_King","B_Bishop","B_Knight","B_Rook"],["B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn"],
           ["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn"],
           ["W_Rook","W_Knight","W_Bishop","W_Queen","W_King","W_Bishop","W_Knight","W_Rook"]]
boardTake=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
movingPieceX=0
movingPieceY=0
movingPiece=""
startGame=False
turnedOn=False
turnWhite=True
Bwin=False
Wwin=False
blueBoxY,blueBoxX=0,0
redBoxY,redBoxX=7,7
bKingMoved=False
wKingMoved=False
bRookrMoved=False
bRooklMoved=False
wRookrMoved=False
wRooklMoved=False




def moveBPawn(board,boardTake,posy,posx,movingPieceY,movingPieceX):
    turnedOn=False
    try:
        if(board[movingPieceY+1][movingPieceX]=="0"):
            turnedOn=True
            boardTake[posy+1][posx]=1
        
    except IndexError:
        pass
    try:
        if(board[posy+1][posx-1]!="0" and posx!=0 and board[posy+1][posx-1][0]!=board[posy][posx][0]):
            turnedOn=True
            boardTake[posy+1][posx-1]=1
    except IndexError:
        pass
    try:
        if(board[posy+1][posx+1]!="0" and board[posy+1][posx+1][0]!=board[posy][posx][0]):
            turnedOn=True
            boardTake[posy+1][posx+1]=1
    except IndexError:
        pass

    try:
        if(board[posy+1][posx]=="0" and board[posy+2][posx]=="0" and posy==1):
            boardTake[posy+2][posx]=1
    except IndexError:
        pass
    
    return turnedOn
def moveWPawn(board,boardTake,posy,posx,movingPieceY,movingPieceX):
    turnedOn=False
    try:
        if(board[movingPieceY-1][movingPieceX]=="0"):
            turnedOn=True
            boardTake[posy-1][posx]=1
        
    except IndexError:
        pass
    try:
        if(board[posy-1][posx-1]!="0" and posx!=0 and board[posy-1][posx-1][0]!=board[posy][posx][0]):
            turnedOn=True
            boardTake[posy-1][posx-1]=1
    except IndexError:
        pass
    try:
        if(board[posy-1][posx+1]!="0" and board[posy-1][posx+1][0]!=board[posy][posx][0]):
            turnedOn=True
            boardTake[posy-1][posx+1]=1
    except IndexError:
        pass

    try:
        if(board[posy-1][posx]=="0" and board[posy-2][posx]=="0" and posy==6):
            boardTake[posy-2][posx]=1
    except IndexError:
        pass
    return turnedOn
def moveBRook(board,boardTake,posy,posx,color):
    turnedOn=False
    for xa in range(posy+1,8):
        boardTake[xa][posx]=1
        turnedOn=True
        if(board[xa][posx]!="0"):
            if(board[xa][posx][0]==color):
                boardTake[xa][posx]=0
            break
    for xa in range(posx+1,8):
        boardTake[posy][xa]=1
        turnedOn=True
        if(board[posy][xa]!="0"):
            if(board[posy][xa][0]==color):
                boardTake[posy][xa]=0
            break
    for xa in range(posy-1,-1,-1):
        boardTake[xa][posx]=1
        turnedOn=True
        if(board[xa][posx]!="0"):
            if(board[xa][posx][0]==color):
                boardTake[xa][posx]=0
            break
    for xa in range(posx-1,-1,-1):
        boardTake[posy][xa]=1
        turnedOn=True
        if(board[posy][xa]!="0"):
            if(board[posy][xa][0]==color):
                boardTake[posy][xa]=0
            break
    return turnedOn
def moveBBishop(board,boardTake,posy,posx,color):
    turnedOn=False
    a=0
    #TO RIGHT BOTTOM
    for xa in range(0,7,1):
        if(posy+a<7 and posx+a<7):
            a+=1
            boardTake[posy+a][posx+a]=1
            turnedOn=True
            if(board[posy+a][posx+a]!="0"):
                if(board[posy+a][posx+a][0]==color):
                    boardTake[posy+a][posx+a]=0
                break
    a=0
    for xa in range(0,7,1):
        if(posy+a<7 and 0<posx-a):
            a+=1
            boardTake[posy+a][posx-a]=1
            turnedOn=True
            if(board[posy+a][posx-a]!="0"):
                if(board[posy+a][posx-a][0]==color):
                    boardTake[posy+a][posx-a]=0
                break
    a=0
    for xa in range(0,7,1):
        if(-0<posy-a and 0<posx-a):
            a+=1
            boardTake[posy-a][posx-a]=1
            turnedOn=True
            if(board[posy-a][posx-a]!="0"):
                if(board[posy-a][posx-a][0]==color):
                    boardTake[posy-a][posx-a]=0
                break
    a=0
    for xa in range(0,7,1):
        if(0<posy-a and posx+a<7):
            a+=1
            boardTake[posy-a][posx+a]=1
            turnedOn=True
            if(board[posy-a][posx+a]!="0"):
                if(board[posy-a][posx+a][0]==color):
                    boardTake[posy-a][posx+a]=0
                break
    return turnedOn
def moveBKnight(board,boardTake,posy,posx,color):
    turnedOn=False
    if(-1<posy-2<8 and -1<posx+1<8):
        if(board[posy-2][posx+1][0]!=color):
            boardTake[posy-2][posx+1]=1
            turnedOn=True
    if(-1<posy+2<8 and -1<posx+1<8):
        if(board[posy+2][posx+1][0]!=color):
            boardTake[posy+2][posx+1]=1
            turnedOn=True
    if(-1<posy+2<8 and -1<posx-1<8):
        if(board[posy+2][posx-1][0]!=color):
            boardTake[posy+2][posx-1]=1
            turnedOn=True
    if(-1<posy-2<8 and -1<posx-1<8):
        if(board[posy-2][posx-1][0]!=color):
            boardTake[posy-2][posx-1]=1
            turnedOn=True
    if(-1<posy+1<8 and -1<posx+2<8):
        if(board[posy+1][posx+2][0]!=color):
            boardTake[posy+1][posx+2]=1
            turnedOn=True
    if(-1<posy+1<8 and -1<posx-2<8):
        if(board[posy+1][posx-2][0]!=color):
            boardTake[posy+1][posx-2]=1
            turnedOn=True
    if(-1<posy-1<8 and -1<posx+2<8):
        if(board[posy-1][posx+2][0]!=color):
            boardTake[posy-1][posx+2]=1
            turnedOn=True
    if(-1<posy-1<8 and -1<posx-2<8):
        if(board[posy-1][posx-2][0]!=color):
            boardTake[posy-1][posx-2]=1
            turnedOn=True
    

    return turnedOn
def moveBQueen(board,boardTake,posy,posx,color):
    turnedOn=False
    a=0
    for xa in range(posy+1,8):
        boardTake[xa][posx]=1
        turnedOn=True
        if(board[xa][posx]!="0"):
            if(board[xa][posx][0]==color):
                boardTake[xa][posx]=0
            break
    for xa in range(posx+1,8):
        boardTake[posy][xa]=1
        turnedOn=True
        if(board[posy][xa]!="0"):
            if(board[posy][xa][0]==color):
                boardTake[posy][xa]=0
            break
    for xa in range(posy-1,-1,-1):
        boardTake[xa][posx]=1
        turnedOn=True
        if(board[xa][posx]!="0"):
            if(board[xa][posx][0]==color):
                boardTake[xa][posx]=0
            break
    for xa in range(posx-1,-1,-1):
        boardTake[posy][xa]=1
        turnedOn=True
        if(board[posy][xa]!="0"):
            if(board[posy][xa][0]==color):
                boardTake[posy][xa]=0
            break
    a=0
    #TO RIGHT BOTTOM
    for xa in range(0,7,1):
        if(posy+a<7 and posx+a<7):
            a+=1
            boardTake[posy+a][posx+a]=1
            turnedOn=True
            if(board[posy+a][posx+a]!="0"):
                if(board[posy+a][posx+a][0]==color):
                    boardTake[posy+a][posx+a]=0
                break
    a=0
    for xa in range(0,7,1):
        if(posy+a<7 and 0<posx-a):
            a+=1
            boardTake[posy+a][posx-a]=1
            turnedOn=True
            if(board[posy+a][posx-a]!="0"):
                if(board[posy+a][posx-a][0]==color):
                    boardTake[posy+a][posx-a]=0
                break
    a=0
    for xa in range(0,7,1):
        if(0<posy-a and 0<posx-a):
            a+=1
            boardTake[posy-a][posx-a]=1
            turnedOn=True
            if(board[posy-a][posx-a]!="0"):
                if(board[posy-a][posx-a][0]==color):
                    boardTake[posy-a][posx-a]=0
                break
    a=0
    for xa in range(0,7,1):
        if(0<posy-a and posx+a<7):
            a+=1
            boardTake[posy-a][posx+a]=1
            turnedOn=True
            if(board[posy-a][posx+a]!="0"):
                if(board[posy-a][posx+a][0]==color):
                    boardTake[posy-a][posx+a]=0
                break
    return turnedOn
def moveBKing(board,boardTake,posy,posx,color,kingMoved,rookrMoved,rooklMoved):
    turnedOn=False
    if(kingMoved==False):
        for xa in range(-1,2,1):
            for ya in range(-1,2,1):
                if(-1<posy+xa<8 and -1<posx+ya<8):
                    if(board[posy+xa][posx+ya][0]!=color):
                        if(not (xa==0 and ya==0)):
                            boardTake[posy+xa][posx+ya]=1
                            turnedOn=True
        if(board[posy][posx+2]=="0" and board[posy][posx+1]=="0" and not(rookrMoved)):
            boardTake[posy][posx+2]=1
            turnedOn=True
        if(board[posy][posx-2]=="0" and board[posy][posx-3]=="0" and board[posy][posx-1]=="0" and not(rooklMoved)):
            boardTake[posy][posx-2]=1
            turnedOn=True
    else:
        for xa in range(-1,2,1):
            for ya in range(-1,2,1):
                if(-1<posy+xa<8 and -1<posx+ya<8):
                    if(board[posy+xa][posx+ya][0]!=color):
                        if(not (xa==0 and ya==0)):
                            boardTake[posy+xa][posx+ya]=1
                            turnedOn=True


    return turnedOn
l=[]
# Run until the user asks to quit
running = True
while running:
    scrn.fill((0, 100, 0))
    if not(startGame):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey=pygame.mouse.get_pos()
                if(230<=mousex<=230+150 and 250<=mousey<=310):
                    startGame=True



        title_font = pygame.font.SysFont("Comic Sans", 62)
        font=pygame.font.SysFont("Comic Sans", 30)
        title = title_font.render("Chess Game", True, (0,0,0))
        scrn.blit(title,(10,50))
        
        scrn.blit(W_background, (390,40))
        scrn.blit(B_background, (420, 50)) 



        play_button = font.render("PLAY", True, (0,0,0))

        mousex,mousey=pygame.mouse.get_pos()
        if(230<=mousex<=230+150 and 250<=mousey<=310):
            pygame.draw.rect(scrn, (85,155,185), pygame.Rect(230, 250, 150, 60))
            
        else:
            pygame.draw.rect(scrn, (55,125,155), pygame.Rect(230, 250, 150, 60))
        
        
        scrn.blit(play_button,(265,260))


###############################################################################################
###############################################################################################
#######################                       GAME START                   ####################
###############################################################################################
###############################################################################################



    else:
        if(Bwin==False and Wwin==False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False     
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and redBoxX>=1:
                        redBoxX-=1
                    if event.key == pygame.K_RIGHT and redBoxX<=6:
                        redBoxX+=1
                    if event.key == pygame.K_UP and redBoxY>=1:
                        redBoxY-=1
                    if event.key == pygame.K_DOWN and redBoxY<=6:
                        redBoxY+=1

                    if event.key == pygame.K_a and blueBoxX>=1:
                        blueBoxX-=1
                    if event.key == pygame.K_d and blueBoxX<=6:
                        blueBoxX+=1
                    if event.key == pygame.K_w and blueBoxY>=1:
                        blueBoxY-=1
                    if event.key == pygame.K_s and blueBoxY<=6:
                        blueBoxY+=1
                    if (event.key == pygame.K_SPACE and not turnWhite) or ((event.key == pygame.K_RCTRL or event.key == pygame.KSCAN_KP_ENTER) and turnWhite):
                        if(not turnWhite):
                            posx=blueBoxX
                            posy=blueBoxY
                        else:
                            posx=redBoxX
                            posy=redBoxY
                        if(not turnedOn):
                            if(board[posy][posx]!="0"):
                                movingPiece=board[posy][posx]
                                movingPieceY=posy
                                movingPieceX=posx
                                if(not turnWhite):
                                    if board[movingPieceY][movingPieceX]=="B_Pawn":
                                        turnedOn = moveBPawn(board,boardTake,posy,posx,movingPieceY,movingPieceX)
                                    elif board[movingPieceY][movingPieceX]=="B_Rook":
                                        turnedOn = moveBRook(board,boardTake,posy,posx,"B")
                                    elif board[movingPieceY][movingPieceX]=="B_Bishop":
                                        turnedOn = moveBBishop(board,boardTake,posy,posx,"B")
                                    elif board[movingPieceY][movingPieceX]=="B_Knight":
                                        turnedOn = moveBKnight(board,boardTake,posy,posx,"B")
                                    elif board[movingPieceY][movingPieceX]=="B_Queen":
                                        turnedOn = moveBQueen(board,boardTake,posy,posx,"B")
                                    elif board[movingPieceY][movingPieceX]=="B_King":
                                        turnedOn = moveBKing(board,boardTake,posy,posx,"B",bKingMoved,bRookrMoved,bRooklMoved)
                                else:
                                    if board[movingPieceY][movingPieceX]=="W_Pawn":
                                        turnedOn = moveWPawn(board,boardTake,posy,posx,movingPieceY,movingPieceX)
                                    elif board[movingPieceY][movingPieceX]=="W_Rook":
                                        turnedOn = moveBRook(board,boardTake,posy,posx,"W")
                                    elif board[movingPieceY][movingPieceX]=="W_Bishop":
                                        turnedOn = moveBBishop(board,boardTake,posy,posx,"W")
                                    elif board[movingPieceY][movingPieceX]=="W_Knight":
                                        turnedOn = moveBKnight(board,boardTake,posy,posx,"W")
                                    elif board[movingPieceY][movingPieceX]=="W_Queen":
                                        turnedOn = moveBQueen(board,boardTake,posy,posx,"W")
                                    elif board[movingPieceY][movingPieceX]=="W_King":
                                        turnedOn = moveBKing(board,boardTake,posy,posx,"W",wKingMoved,wRookrMoved,wRooklMoved)

                        elif (turnedOn):
                            for x in range(0,8):
                                for y in range(0,8):
                                    if(boardTake[y][x]!=0 and y==posy and x==posx):
                                        #Win screen W.I.P
                                        if(board[y][x]=="B_King"):
                                            Wwin=True
                                        if(board[y][x]=="W_King"):
                                            Bwin=True
                                        if(wRookrMoved==False and movingPieceY==7 and movingPieceX==7):
                                            wRookrMoved=True
                                        if(wRooklMoved==False and movingPieceY==7 and movingPieceX==0):
                                            wRooklMoved=True
                                        if(bRookrMoved==False and movingPieceY==0 and movingPieceX==7):
                                            bRookrMoved=True
                                        if(bRooklMoved==False and movingPieceY==0 and movingPieceX==0):
                                            bRooklMoved=True
                                        if(board[movingPieceY][movingPieceX][5]=="g" and x-movingPieceX==2 and wKingMoved==False and wRookrMoved==False):
                                            board[y][x]=board[movingPieceY][movingPieceX]
                                            board[movingPieceY][movingPieceX]="0"
                                            board[y][x-1]=board[movingPieceY][movingPieceX+3]
                                            board[movingPieceY][movingPieceX+3]="0"
                                            boardSurface[y][x]=boardSurface[movingPieceY][movingPieceX]
                                            boardSurface[movingPieceY][movingPieceX]=0
                                            boardSurface[y][x-1]=boardSurface[movingPieceY][movingPieceX+3]
                                            boardSurface[movingPieceY][movingPieceX+3]=0
                                            wKingMoved=True
                                            wRookrMoved=True
                                        elif(board[movingPieceY][movingPieceX][5]=="g" and x-movingPieceX==2 and bKingMoved==False and bRookrMoved==False):
                                            board[y][x]=board[movingPieceY][movingPieceX]
                                            board[movingPieceY][movingPieceX]="0"
                                            board[y][x-1]=board[movingPieceY][movingPieceX+3]
                                            board[movingPieceY][movingPieceX+3]="0"
                                            boardSurface[y][x]=boardSurface[movingPieceY][movingPieceX]
                                            boardSurface[movingPieceY][movingPieceX]=0
                                            boardSurface[y][x-1]=boardSurface[movingPieceY][movingPieceX+3]
                                            boardSurface[movingPieceY][movingPieceX+3]=0
                                            bKingMoved=True
                                            bRookrMoved=True
                                        elif(board[movingPieceY][movingPieceX][5]=="g" and movingPieceX-x==2 and wKingMoved==False and wRooklMoved==False):
                                            board[y][x]=board[movingPieceY][movingPieceX]
                                            board[movingPieceY][movingPieceX]="0"
                                            board[y][x+1]=board[movingPieceY][movingPieceX-4]
                                            board[movingPieceY][movingPieceX-4]="0"
                                            boardSurface[y][x]=boardSurface[movingPieceY][movingPieceX]
                                            boardSurface[movingPieceY][movingPieceX]=0
                                            boardSurface[y][x+1]=boardSurface[movingPieceY][movingPieceX-4]
                                            boardSurface[movingPieceY][movingPieceX-4]=0
                                            wKingMoved=True
                                            wRookrMoved=True
                                        elif(board[movingPieceY][movingPieceX][5]=="g" and movingPieceX-x==2 and bKingMoved==False and bRooklMoved==False):
                                            board[y][x]=board[movingPieceY][movingPieceX]
                                            board[movingPieceY][movingPieceX]="0"
                                            board[y][x+1]=board[movingPieceY][movingPieceX-4]
                                            board[movingPieceY][movingPieceX-4]="0"
                                            boardSurface[y][x]=boardSurface[movingPieceY][movingPieceX]
                                            boardSurface[movingPieceY][movingPieceX]=0
                                            boardSurface[y][x+1]=boardSurface[movingPieceY][movingPieceX-4]
                                            boardSurface[movingPieceY][movingPieceX-4]=0
                                            bKingMoved=True
                                            bRookrMoved=True
                                        else:
                                            board[y][x]=board[movingPieceY][movingPieceX]
                                            board[movingPieceY][movingPieceX]="0"
                                            boardSurface[y][x]=boardSurface[movingPieceY][movingPieceX]
                                            boardSurface[movingPieceY][movingPieceX]=0
                                        turnWhite= not(turnWhite)
                                        
                                        for xa in range(0,8):
                                            if(board[7][xa]=="B_Pawn"):
                                                board[7][xa]="B_Queen"
                                            if(board[0][xa]=="W_Pawn"):
                                                board[0][xa]="W_Queen"
                                        for A in range(0,8):
                                            for B in range(0,8):
                                                boardTake[A][B]=0
                                        turnedOn=False
                            #defaults every thing out if player presses its self or blank spot
                            turnedOn=False
                            for A in range(0,8):
                                for B in range(0,8):
                                    boardTake[A][B]=0
                            if((not (movingPieceY==posy and movingPieceX==posx)) and  not((board[posy][posx]=="0")) and not(turnedOn==False)):
                                movingPiece=board[posy][posx]
                                movingPieceY=posy
                                movingPieceX=posx
                                turnedOn = moveBPawn(board,boardTake,posy,posx,movingPieceY,movingPieceX)
                    
            #Creates Background 8x8
            for x in range (0,8):
                for y in range(0,4):
                    if(x%2==1):
                        pygame.draw.rect(scrn, (237, 194, 114), pygame.Rect(x*75, 2*(y+0.5)*75, 75, 75))
                    else:
                        pygame.draw.rect(scrn, (237, 194, 114), pygame.Rect(x*75, 2*y*75, 75, 75))
            #Load in Chess Pieces
            for y in range(0,8):
                for x in range(0,8):
                    if(board[x][y]!="0"):
                        scrn.blit(boardSurface[x][y], (y*75+15,x*75))
            #Available circles placed
            if(turnedOn):
                for y in range(0,8):
                    for x in range(0,8):
                        if(boardTake[x][y]!=0):
                            pygame.draw.circle(scrn, (235, 235, 180), (y*75+37,x*75+37), 17,100)
            #box to show where player is looking at
            if(blueBoxX!=redBoxX or blueBoxY!=redBoxY):
                pygame.draw.rect(scrn, (0, 100, 255), (blueBoxX*75, blueBoxY*75, 75, 75), 3)
                pygame.draw.rect(scrn, (255, 100, 0), (redBoxX*75, redBoxY*75, 75, 75), 3)
            else:
                x, y = blueBoxX, blueBoxY
                l1 = [(x*75+1, y*75 + 75), (x*75+1, y*75), (x*75 + 75, y*75)]
                l2 = [(x*75, y*75 + 75-1), (x*75 + 75, y*75 + 75-1), (x*75 + 75, y*75-1)]
                pygame.draw.lines(scrn, (0, 100, 255), False, l1, 3)
                pygame.draw.lines(scrn, (255, 100, 0), False, l2, 3)
                
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    boardSurface=[[B_Rook,B_Knight,B_Bishop,B_Queen,B_King,B_Bishop,B_Knight,B_Rook],[B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn,B_Pawn],
                                  [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn,W_Pawn],
                                  [W_Rook,W_Knight,W_Bishop,W_Queen,W_King,W_Bishop,W_Knight,W_Rook]]
                    board=[["B_Rook","B_Knight","B_Bishop","B_Queen","B_King","B_Bishop","B_Knight","B_Rook"],["B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn","B_Pawn"],
                            ["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],
                            ["W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn","W_Pawn"],["W_Rook","W_Knight","W_Bishop","W_Queen","W_King","W_Bishop","W_Knight","W_Rook"]]
                    boardTake=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
                    movingPieceX=0
                    movingPieceY=0
                    movingPiece=""
                    startGame=False
                    turnedOn=False
                    turnWhite=True
                    Bwin=False
                    Wwin=False
                    bKingMoved=False
                    wKingMoved=False
                    bRookrMoved=False
                    bRooklMoved=False
                    wRookrMoved=False
                    wRooklMoved=False






            win_font = pygame.font.SysFont("Comic Sans", 62)
            small_font = pygame.font.SysFont("Comic Sans", 20)
            
            if(Bwin):
                bWinTitle = win_font.render("Black Win!", True, (0,0,0))
                scrn.blit(B_win, (250,20))
                scrn.blit(bWinTitle,(150,207))
            if(Wwin):
                wWinTitle = win_font.render("White Win!", True, (0,0,0))
                scrn.blit(W_win, (260,20))
                scrn.blit(wWinTitle,(140,207))
            scrn.blit(small_font.render("Click anywhere to return", True, (0,0,0)),(190,350))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()