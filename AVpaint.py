#Aleksa Vucak's Paint Project
#November 19th, 2021

#Allows the user to unleash their inner basketball player and create pieces of art with an NBA theme

from pygame import *  #pygame imports needed
from math import *  #used for making each tool work
from random import *  #random dots for spraycan 
import os
from tkinter import *  
from tkinter import filedialog  #used for load/save tool
import pygame  #from template

root=Tk()
root.withdraw()  #hides the little tk window

RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

###############################################################################
##MUSIC##


#init()
#mixer.music.load("paint/tools/nbaEspnsong.mp3")  #importing ESPN song
#mixer.music.play(-1)  #replays the song after it finishes

###############################################################################
##WHERE THE WINDOW OPENS##

init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,100'  #running the code on a different computer/screen size might cut off some of the screen 

###############################################################################             
##STUFF FOR BACKGROUND##

size=width,height=(1450,800)
screen=display.set_mode(size)

##back=image.load("paint/tools/zbball.png")  #loading background image
##back=transform.scale(back,(1214,800))  #scaling
##screen.blit(back,(0,0))  #top left corner x and y coordinates

##screen.fill(BLACK)
##screen.blit(back,(0,0))

t="paint/tools/"  #setting picture path as a variable so i dont need to retype this over and over again
s="paint/stamps/"

draw.line(screen,WHITE,(1220,0),(1220,800),12)  #seperation line

##woodcourt=image.load(t+"woodcourt.jpg")  #loading background image
##woodcourt=transform.scale(woodcourt,(224,800))  #scaling
##screen.blit(woodcourt,(1226,0))  #top left corner corrdinates

draw.line(screen,WHITE,(1220,267),(1450,267),12)  #drawing seperation lines
draw.line(screen,WHITE,(1220,533),(1450,533),12)

###############################################################################
##RECTANGLES FOR EACH TOOL##

canvasRect=Rect(40,75,900,550)  #top left corner coordinates and length of all the white rectangles 
draw.rect(screen,(255,255,255),canvasRect,0)  #drawing the rectangle and setting a variable for it 
pencilRect=Rect(950,75,65,65)
draw.rect(screen,(255,255,255),pencilRect,0)
eraserRect=Rect(1025,75,65,65)
draw.rect(screen,(255,255,255),eraserRect,0)
sprayRect=Rect(1100,75,65,65)
draw.rect(screen,(255,255,255),sprayRect,0)
brushRect=Rect(950,150,65,65)
draw.rect(screen,(255,255,255),brushRect,0)
lineRect=Rect(1025,150,65,65)
draw.rect(screen,(255,255,255),lineRect,0)
mjRect=Rect(40,635,100,150)
draw.rect(screen,(255,255,255),mjRect,0)
redoRect=Rect(1075,10,50,50)
draw.rect(screen,(255,255,255),redoRect,0)
undoRect=Rect(1015,10,50,50)
draw.rect(screen,(255,255,255),undoRect,0)
clearRect=Rect(1135,10,50,50)
draw.rect(screen,(255,255,255),clearRect,0)
beardRect=Rect(155,635,100,150)
draw.rect(screen,(255,255,255),beardRect,0)
aiRect=Rect(270,635,100,150)
draw.rect(screen,(255,255,255),aiRect,0)
lameloRect=Rect(385,635,100,150)
draw.rect(screen,(255,255,255),lameloRect,0)
browRect=Rect(500,635,100,150)
draw.rect(screen,(255,255,255),browRect,0)
jokarRect=Rect(615,635,100,150)
draw.rect(screen,(255,255,255),jokarRect,0)
chocRect=Rect(730,635,100,150)
draw.rect(screen,(255,255,255),chocRect,0)
zionRect=Rect(845,635,100,150)
draw.rect(screen,(255,255,255),zionRect,0)
kyrieRect=Rect(960,635,100,150)
draw.rect(screen,(255,255,255),kyrieRect,0)
shaqRect=Rect(1075,635,100,150)
draw.rect(screen,(255,255,255),shaqRect,0)
rectRect=Rect(1100,150,65,65)
draw.rect(screen,(255,255,255),rectRect,0)
airRect=Rect(1025,225,65,65)
draw.rect(screen,(255,255,255),airRect,0)
saveRect=Rect(10,10,50,50)
draw.rect(screen,(255,255,255),saveRect,0)
loadRect=Rect(70,10,50,50)
draw.rect(screen,(255,255,255),loadRect,0)
ellipseRect=Rect(950,225,65,65)
draw.rect(screen,(255,255,255),ellipseRect,0)
fillRect=Rect(1100,225,65,65)
draw.rect(screen,(255,255,255),fillRect,0)
markerRect=Rect(950,300,65,65)
draw.rect(screen,(255,255,255),markerRect,0)
textRect=Rect(950,375,180,95)
draw.rect(screen,(100,100,100),textRect,0)
mouseRect=(780,45,160,25)  #mouse tracker box
draw.rect(screen,(255,255,255),mouseRect,0)
bg1Rect=Rect(1236,10,204,241)
draw.rect(screen,(255,255,255),bg1Rect,0)
bg2Rect=Rect(1236,283,204,236)
draw.rect(screen,(255,255,255),bg2Rect,0)
bg3Rect=Rect(1236,550,204,241)
draw.rect(screen,(255,255,255),bg3Rect,0)

###############################################################################
###IMAGES###

t="paint/tools/"  #setting variables so i dont need to type the path of the pictures every time
s="paint/stamps/"

pencil=image.load(t+"pencil.png")  #loading image
pencil=transform.scale(pencil,(65,65))  #scaling the image
screen.blit(pencil,(950,75))  #coordinates of the image
eraser=image.load(t+"eraser.png")
eraser=transform.scale(eraser,(65,65))
screen.blit(eraser,(1025,75))
spray=image.load(t+"spray.png")
spray=transform.scale(spray,(65,65))
screen.blit(spray,(1100,75))
brush=image.load(t+"brush.png")
brush=transform.scale(brush,(65,65))
screen.blit(brush,(950,150))
line=image.load(t+"line.png")
line=transform.scale(line,(65,65))
screen.blit(line,(1025,150))
spec=image.load(t+"spec.png")
spec=transform.scale(spec,(215,150))
specblit=screen.blit(spec,(950,475))
specball=image.load(t+"ballspec.png")
specball=transform.scale(specball,(65,60))
screen.blit(specball,(1130,410))
mj=image.load(s+"jordancry.png")
mj=transform.scale(mj,(100,150))
screen.blit(mj,(40,635))
undo=image.load(t+"undo.png")
undo=transform.scale(undo,(50,50))
screen.blit(undo,(1015,10))
redo=image.load(t+"redo.png")
redo=transform.scale(redo,(50,50))
screen.blit(redo,(1075,10))
beard=image.load(s+"beard.png")
beard=transform.scale(beard,(110,140))
screen.blit(beard,(150,635))
ai=image.load(s+"ai.png")
ai=transform.scale(ai,(140,170))
screen.blit(ai,(250,622))
lamelo=image.load(s+"lameloball.png")
lamelo=transform.scale(lamelo,(100,160))
screen.blit(lamelo,(385,635))
brow=image.load(s+"brow.png")
brow=transform.scale(brow,(110,145))
screen.blit(brow,(495,640))
jokar=image.load(s+"jok.png")
jokar=transform.scale(jokar,(105,135))
screen.blit(jokar,(610,640))
choc=image.load(s+"whitechoc.png")
choc=transform.scale(choc,(90,180))
screen.blit(choc,(735,620))
zion=image.load(s+"zwill.png")
zion=transform.scale(zion,(120,170))
screen.blit(zion,(835,630))
kyrie=image.load(s+"kyrie.png")
kyrie=transform.scale(kyrie,(90,150))
screen.blit(kyrie,(965,635))
shaq=image.load(s+"shaqattaq.png")
shaq=transform.scale(shaq,(125,170))
screen.blit(shaq,(1060,627))
nba=image.load(s+"nba.png")
nba=transform.scale(nba,(500,100))
screen.blit(nba,(230,-10))
save=image.load(t+"save.png")
save=transform.scale(save,(50,50))
screen.blit(save,(10,10))
rec=image.load(t+"rec.png")
rec=transform.scale(rec,(65,65))
screen.blit(rec,(1100,150))
ellipse=image.load(t+"ellipse.png")
ellipse=transform.scale(ellipse,(65,65))
screen.blit(ellipse,(950,225))
clear=image.load(t+"clear.png")
clear=transform.scale(clear,(50,50))
screen.blit(clear,(1135,10))
load=image.load(t+"load.png")
load=transform.scale(load,(50,50))
screen.blit(load,(70,10))
fill=image.load(t+"fill.png")
fill=transform.scale(fill,(65,65))
screen.blit(fill,(1100,225))
air=image.load(t+"airbrush.png")
air=transform.scale(air,(65,65))
screen.blit(air,(1025,225))
marker=image.load(t+"marker.png")
marker=transform.scale(marker,(65,65))
screen.blit(marker,(950,300))
##bg1=image.load(t+"remotebball.png")
##sbg1=transform.scale(bg1,(194,231))  #values are prime due to the fact that I wanted to leave a 5 pixel ap on each side of the background selection
##screen.blit(sbg1,(1241,15))
##bg2=image.load(t+"venicebeach.jpeg")
##sbg2=transform.scale(bg2,(194,226))  #values are prime due to the fact that I wanted to leave a 5 pixel ap on each side of the background selection
##screen.blit(sbg2,(1241,288))
##bg3=image.load(t+"glowinadark.jpeg")
##sbg3=transform.scale(bg3,(194,231))  #values are prime due to the fact that I wanted to leave a 5 pixel ap on each side of the background selection
##screen.blit(sbg3,(1241,555))

############################################################################
###IMAGES FOR DESCRIPTION BOX###

#description boxes for each tool were typed out and screenshotted, loading them as a picture is the easiest way to go about this idea
despencil=image.load(t+"pencildes.png")  #loading description box for all tools
despencil=transform.scale(despencil,(175,90))  #how big the des box is going to be 
deseraser=image.load(t+"eraserdes.png")
deseraser=transform.scale(deseraser,(175,90))
desspray=image.load(t+"spraydes.png")
desspray=transform.scale(desspray,(175,90))
desbrush=image.load(t+"brushdes.png")
desbrush=transform.scale(desbrush,(175,90))
desline=image.load(t+"linedes.png")
desline=transform.scale(desline,(175,90))
desrec=image.load(t+"recdes.png")
desrec=transform.scale(desrec,(175,90))
desellipse=image.load(t+"ellipsedes.png")
desellipse=transform.scale(desellipse,(175,90))
desair=image.load(t+"airdes.png")
desair=transform.scale(desair,(175,90))
desfill=image.load(t+"filldes.png")
desfill=transform.scale(desfill,(175,90))
dessave=image.load(t+"savedes.png")
dessave=transform.scale(dessave,(175,90))
desload=image.load(t+"loaddes.png")
desload=transform.scale(desload,(175,90))
desmarker=image.load(t+"markerdes.png")
desmarker=transform.scale(desmarker,(175,90))
dessticker=image.load(t+"stickerdes.png")
dessticker=transform.scale(dessticker,(175,90))
desclear=image.load(t+"cleardes.png")
desclear=transform.scale(desclear,(175,90))
desundo=image.load(t+"undodes.png")
desundo=transform.scale(desundo,(175,90))
desredo=image.load(t+"redodes.png")
desredo=transform.scale(desredo,(175,90))
##desbacks=image.load(t+"backdes.png")
##desbacks=transform.scale(desbacks,(175,90))

###############################################################################
##VARIABLES##

oldmx=0  #old x coordinates are 0
oldmy=0  #old y coordinates are 0
mx,my=0,0
drawColour = (0,0,0)
size=6  #default size also used to set minimum size of tools
stampsize=6  #variable used to set minimum size of stamps
pencilsize=1  #setting minimum pencil size

################################################################################
##HOVERING/CLICKING HIGHLIGHTER LISTS##

#putting all tolls in a list to minimize the amount of code for the hovering and clicking highlighter
tools=["pencil","eraser","spray","brush","line","mj","beard","ai","lamelo","brow","jokar","choc","zion","kyrie","shaq","clear","rect","ellipse","save","load","air","marker","fill","undo","redo","bg1","bg2","bg3"]
tRects=[pencilRect,eraserRect,sprayRect,brushRect,lineRect,mjRect,beardRect,aiRect,lameloRect,browRect,jokarRect,chocRect,zionRect,kyrieRect,shaqRect,clearRect,rectRect,ellipseRect,saveRect,loadRect,airRect,markerRect,fillRect,undoRect,redoRect,bg1Rect,bg2Rect,bg3Rect]

###############################################################################   
##MORE COMPLEX VARIABLES##
    
tool=""  
redo=False
a=0  #keeps count of screenshots taken
undoredolist=[]  #undo/redo list
screenshot=screen.subsurface(canvasRect).copy()  #picture used for undo/redo list
undoredolist.append(screenshot)  #adds picture to undo/redo list

##############################################################################
##FONT##

pygame.init()
font=pygame.font.SysFont("Britannic Bold",33)

###############################################################################
##WHILE LOOP##

running=True
while running:
    buttondown=False
    buttonup=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            buttondown=True
            if evt.button==1:
                screenPic=screen.copy()  #takes a picture of the screen
            sx,sy=evt.pos  #position of line tool
            if evt.button==4:  #4 is scroll up
                size=size+2   #increase size of brush
                stampsize=stampsize+2
                pencilsize=pencilsize+1
                if pencilsize>3:  #limiting pencil size
                        pencilsize=3
            if evt.button==5:  #5 is scrolling down
                size=size-2  #decrease size of brush
                stampsize=stampsize-2
                pencilsize=pencilsize-1
                if size<=1 and pencilsize<=1:
                    size=1  #the size cannot get smaller then 1 making the tool always show
                    pencilsize=1
                
        if evt.type==MOUSEBUTTONUP and clearRect.collidepoint(mx,my):  #so screenshots will add to undo/redo list when clear button is used 
            a+=1
        if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
            buttonup=True     
            screenshot=screen.subsurface(canvasRect).copy()  #picture used for undo redo list
            undoredolist.append(screenshot)  #adds picture to redo list
            a+=1  #adds to count list
    brushHead=Surface((size*2,size*2),SRCALPHA)  #surface for alpha brush
    draw.circle(brushHead,(drawColour[0],drawColour[1],drawColour[2],10),(size,size),size)  #brush in a loop so it doesnt stop until the user stops left clicking on the canvas
        
    mx,my=mouse.get_pos()
    mb= mouse.get_pressed()

    for i in range(len(tools)):  #searches tools list
        draw.rect(screen,(255,255,255),tRects[i],3)
    for i in range(len(tools)):  #searches my tools list
        if tRects[i].collidepoint(mx,my):  #hovering highlighter
                draw.rect(screen,RED,tRects[i],3)  #chose blue because it is one of the main colours of the NBA
    for i in range(len(tools)):  #searches tools list
        if tool==tools[i]:  #clicking highlighter
            draw.rect(screen,BLUE,tRects[i],3)  #chose red because it is one of the main colours of the NBA

###################################################################################
##MOUSE TRACKER##
    
    if canvasRect.collidepoint(mx,my):
        xy=str(mx-40)  #subtracting 40 from mx beacuse the x coordinate of the top left corner of the canvas is 40
        xy2=str(my-75)  #subtracting 40 from mx beacuse the y coordinate of the top left corner of the canvas is 75
        x1=font.render(xy,True,(0,0,200))
        y1=font.render(xy2,True,(0,0,200))
        x2=font.render("X:",True,(0,0,200))  #printing x coordinate on the screen in blue
        y2=font.render("Y:",True,(0,0,200))  #printing y coordinate on the screen in blue
        draw.rect(screen,(255,255,255),mouseRect,0)  #so the new x and y coordinates do not blit on top of the old x and y 
        screen.blit(x1,(847-x1.get_width(),47)) 
        screen.blit(y1,(929-y1.get_width(),47))
        screen.blit(x2,(785,47))
        screen.blit(y2,(867,47))
        
###################################################################################        
##UNDO##
        
    if undoRect.collidepoint(mx,my):
        if evt.type==MOUSEBUTTONDOWN:
            draw.rect(screen,(0,0,200),undoRect,3)
            draw.rect(screen,(100,100,100),textRect,0)
            screen.blit(desundo,(950,375))  #stuff for icon borders and icon pics
            if a<1:
                screen.blit(undoredolist[a],(40,75))  #blits the canvas only
                a=0
            else:
                screen.blit(undoredolist[a-1],(40,75))  #current screen is the one before in the list
                a-=1
            time.wait(200)  #goes through list too fast
      
##################################################################################
##REDO##
            
    if redoRect.collidepoint (mx,my):
       if evt.type==MOUSEBUTTONDOWN:
            draw.rect(screen,(0,0,200),redoRect,3)
            draw.rect(screen,(100,100,100),textRect,0)
            screen.blit(desredo,(950,375))  #stuff for icon borders and icon pics
            if a<len(undoredolist)-1:  #if there is no last postion in list
                screen.blit(undoredolist[a+1],(40,75))
                a+=1  #list increases
            time.wait(200)  #goes through list too fast

################################################################################
##WHEN USER CLICKS ON ICONS##
            
    if pencilRect.collidepoint(mx,my) and mb[0]==1:  #when user clicks on tool
        draw.rect(screen,(0,0,200),pencilRect,3)  #selecting highlighter
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(despencil,(950,375))  #stuff for icon borders and icon pics
        tool="pencil"  #naming the selected tool
    if eraserRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),eraserRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(deseraser,(950,375))
        tool="eraser"
    if sprayRect.collidepoint(mx,my)and mb[0]==1:
        draw.rect(screen,(0,0,200),sprayRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desspray,(950,375))
        tool="spray"
    if brushRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),brushRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desbrush,(950,375))
        tool="brush"
    if lineRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),lineRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desline,(950,375))
        screen
        tool="line"
    if mjRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),mjRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="mj"
    if beardRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),beardRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="beard"
    if aiRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),aiRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="ai"
    if lameloRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),lameloRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="lamelo"
    if browRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),browRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="brow"
    if jokarRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),jokarRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="jokar"
    if chocRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),chocRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="choc"
    if zionRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),zionRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="zion"
    if kyrieRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),kyrieRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="kyrie"
    if shaqRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),shaqRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessticker,(950,375))
        tool="shaq"
    if clearRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),clearRect,3)
        draw.rect(screen,(255,255,255),canvasRect,0)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desclear,(950,375))
        tool="clear"
    if rectRect.collidepoint(mx,my) and mb[2]==1:  #when left click something else happens
        draw.rect(screen,(0,0,200),rectRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desrec,(950,375))
        tool="rect"
    if rectRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),rectRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desrec,(950,375))
        tool="rec"
    if ellipseRect.collidepoint(mx,my) and mb[2]==1:  #when left click something else happens
        draw.rect(screen,(0,0,200),ellipseRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desellipse,(950,375))
        tool="ellipse"
    if ellipseRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),ellipseRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desellipse,(950,375))
        tool="ellip"
    if specblit.collidepoint(mx,my) and mb[0]==1:
        drawColour=screen.get_at((mx,my))
        draw.circle(screen,drawColour,(1165,440),28)
        screen.blit(specball,(1130,410))
    if saveRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),saveRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(dessave,(950,375))
        fname=filedialog.asksaveasfilename(defaultextension=".png")
        screencopy=screen.subsurface(canvasRect).copy()
        if fname!="":
            image.save(screencopy,fname)
    if loadRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),loadRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desload,(950,375))
        fname=filedialog.askopenfilename(filetypes=[("Images","*png;*.bmp;*.jpg;*.jpeg")])
        if fname!="":
            fname=image.load(fname)
            screen.blit(fname,canvasRect)
    if airRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),airRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desair,(950,375))
        tool="air"
    if markerRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),markerRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desmarker,(950,375))
        tool="marker" 
    if fillRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),fillRect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desfill,(950,375))
        tool="fill"
    if bg1Rect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),bg1Rect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desbacks,(950,375))
        tool="bg1"
        bg1=transform.scale(bg1,(900,550))  #making the background the whole canvas
        screen.blit(bg1,(40,75))
    if bg2Rect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),bg2Rect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desbacks,(950,375))
        tool="bg2"
        bg2=transform.scale(bg2,(900,550))  #making the background the whole canvas
        screen.blit(bg2,(40,75))
    if bg3Rect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,0,200),bg3Rect,3)
        draw.rect(screen,(100,100,100),textRect,0)
        screen.blit(desbacks,(950,375))
        tool="bg3"
        bg3=transform.scale(bg3,(900,550))  #making the background the entire canvas
        screen.blit(bg3,(40,75))

################################################################################
##HOW TOOLS ACTUALLY WORK##
            
    if canvasRect.collidepoint(mx,my)and mb[0]==1:
        screen.set_clip(canvasRect)
        if tool=="pencil": 
            dist=hypot(mx-oldmx,my-oldmy)
            dist=max(1,dist)
            sx=(oldmx-mx)/dist
            sy=(oldmy-my)/dist
            dots=int(dist)
            for i in range(dots):  #draws in every pixel
                draw.circle(screen,(drawColour),(int(mx+sx*i),int(my+sy*i)),pencilsize)
        if tool=="eraser":
            dx=mx-oldmx  #finds length of x
            dy=my-oldmy  #finds length of y 
            dist=int(sqrt((dx)**2+(dy)**2))
            for i in range(dist):
                dotX=i*dx/dist+oldmx
                dotY=i*dy/dist+oldmy
                draw.circle(screen,(255,255,255),(int(dotX),int(dotY)),size)  #draws circle
        if size<=5:  #the smallest a tool can be
            size=5
        if size>=75:  #the biggest a tool can be
            size=75
        if tool=="spray":
            for i in range(size*2):  #draws more dots
                ax=randint(mx-size,mx+size)  #draws dots in random places
                ay=randint(my-size,my+size)
                dist=hypot(mx-ax,my-ay)
                if dist<=size:  #draws only in the radius making it a circle instead of a square
                    draw.circle(screen,drawColour,(ax,ay),1)
        if tool=="brush": 
            dist=hypot(mx-oldmx,my-oldmy)
            dist=max(1,dist)
            sx=(oldmx-mx)/dist
            sy=(oldmy-my)/dist
            dots=int(dist)
            for i in range(dots):  #draws in every pixel in a set radius
                draw.circle(screen,(drawColour),(int(mx+sx*i),int(my+sy*i)),size)
        if tool=="line":
            screen.blit(screenPic,(0,0))  #doesn't draw wherever the mouse is
            draw.line(screen,(drawColour),(sx,sy),(mx,my),3)
        if stampsize<=8:  #the smallest a sticker can be
            stampsize=8
        if stampsize>=50:  #the biggest a sticker can be
            stampsize=50
        #so stickers aren't too pixelated
        if tool=="mj":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            mjTmp = transform.scale(mj,(int(100*stampsize/10),int(200*stampsize/10)))  #changes size
            screen.blit(mjTmp,(mx-mjTmp.get_width()//2,my-mjTmp.get_height()//2))  #where the mouse is positioned when user clicks
        if tool=="beard":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            beardTmp = transform.scale(beard,(int(200*stampsize/10),int(200*stampsize/10)))
            screen.blit(beardTmp,(mx-beardTmp.get_width()//2,my-beardTmp.get_height()//2))
        if tool=="ai":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            aiTmp = transform.scale(ai,(int(100*stampsize/10),int(200*stampsize/10)))
            screen.blit(aiTmp,(mx-aiTmp.get_width()//2,my-aiTmp.get_height()//2))
        if tool=="lamelo":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            lameloTmp = transform.scale(lamelo,(int(125*stampsize/10),int(200*stampsize/10)))
            screen.blit(lameloTmp,(mx-lameloTmp.get_width()//2,my-lameloTmp.get_height()//2))
        if tool=="brow":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            browTmp = transform.scale(brow,(int(150*stampsize/10),int(200*stampsize/10)))
            screen.blit(browTmp,(mx-browTmp.get_width()//2,my-browTmp.get_height()//2))
        if tool=="jokar":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            jokarTmp = transform.scale(jokar,(int(125*stampsize/10),int(200*stampsize/10)))
            screen.blit(jokarTmp,(mx-jokarTmp.get_width()//2,my-jokarTmp.get_height()//2))
        if tool=="choc":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            chocTmp = transform.scale(choc,(int(100*stampsize/10),int(200*stampsize/10)))
            screen.blit(chocTmp,(mx-chocTmp.get_width()//2,my-chocTmp.get_height()//2))
        if tool=="zion":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            zionTmp = transform.scale(zion,(int(100*stampsize/10),int(200*stampsize/10)))
            screen.blit(zionTmp,(mx-zionTmp.get_width()//2,my-zionTmp.get_height()//2))
        if tool=="kyrie":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            kyrieTmp = transform.scale(kyrie,(int(150*stampsize/10),int(200*stampsize/10)))
            screen.blit(kyrieTmp,(mx-kyrieTmp.get_width()//2,my-kyrieTmp.get_height()//2))
        if tool=="shaq":
            screen.blit(screenPic,(0,0))  #no trail is left behind when you move the sticker around
            shaqTmp = transform.scale(shaq,(int(100*stampsize/10),int(200*stampsize/10)))
            screen.blit(shaqTmp,(mx-shaqTmp.get_width()//2,my-shaqTmp.get_height()//2))
        if tool=="rect":  #unfilled rectangle
            screen.blit(screenPic,(0,0))
            draw.rect(screen,(drawColour),(sx,sy,mx-sx,my-sy),size)
        if tool=="rec":  #filled rectangle
            screen.blit(screenPic,(0,0))
            draw.rect(screen,(drawColour),(sx,sy,mx-sx,my-sy))
        if tool=="ellipse":  #filled ellipse
            screen.blit(screenPic,(0,0))
            ERect=Rect(sx,sy,mx-sx,my-sy)  #surface for the circle to be drawn on
            draw.ellipse(screen,(drawColour),(ERect))
        if tool=="ellip":  #unfilled ellipse
            screen.blit(screenPic,(0,0))
            ERect=Rect(sx,sy,mx-sx,my-sy)
            draw.rect(screen,(0,0,200),ellipseRect,3)
            if ERect.width<4*2 or ERect.height<4*2:  #draws a filled circle the size of the radius
                draw.ellipse(screen,(drawColour),(ERect))
            else:
                draw.ellipse(screen,drawColour,(ERect),size)  #when the surface is big enough and stops crashing draw unfilled
        if tool=="air":
            draw.circle(brushHead,(drawColour[0],drawColour[1],drawColour[2],1),(size,size),size)
            if mx!=oldmx or my!=oldmy:  #stops dark circles from being drawn when mouse doesn't move
                dist=hypot(oldmx-mx,oldmy-my)
                dist=max(1,dist)
                sx=(mx-oldmx)/dist
                sy=(my-oldmy)/dist
                dots=int(dist)
                for i in range(dots):  #draws on every pixel
                    screen.blit(brushHead,(mx+sx*i-size,my+sy*i-size))
        if tool=="fill":
                fillColour=screen.get_at((mx,my))  #checks for colour that needs to be replaced
                spots=[(mx,my)]  #starts where you click
                while len(spots)>0:
                    newSpots=[]  #list for the spots
                    for fx,fy in spots:
                        if 0<fx<width and 0<fy<height and screen.get_at((fx,fy))==fillColour:
                            screen.set_at((fx,fy),drawColour)
                            newSpots+=[(fx+1,fy),(fx-1,fy),(fx,fy+1),(fx,fy-1)]  #adds pixel in all directions on click
                        spots=newSpots
        if tool=="marker":  #kind of like air brush
            dx=mx-oldmx
            dy=my-oldmy
            dist=hypot(dx,dy)
            screen.blit(brushHead,(mx-5,my-5))
            for i in range(int(dist)):
                dotX=i*dx/dist+oldmx
                dotY=i*dy/dist+oldmy
                screen.blit(brushHead,(int(dotX)-5,int(dotY)-5))
            
        screen.set_clip(None)    
    oldmx,oldmy=mx,my    
    display.flip()
    
  
quit()

            

