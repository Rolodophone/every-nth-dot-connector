import gui

BLACK       = color(000)
GREY1       = color(050)
GREY2       = color(100)
GREY3       = color(150)
GREY4       = color(200)
WHITE       = color(255)
RED         = color(255, 000, 000)
DARKRED     = color(100, 000, 000)
GREEN       = color(000, 255, 000)
DARKGREEN   = color(000, 100, 000)
BLUE        = color(000, 000, 255)
DARKBLUE    = color(000, 000, 100)
YELLOW      = color(255, 255, 000)
DARKYELLOW  = color(100, 100, 000)
MAGENTA     = color(255, 000, 255)
DARKMAGENTA = color(100, 000, 100)
CYAN        = color(000, 255, 255)
DARKCYAN    = color(000, 100, 100)
TRANSPARENT = color(255, 255, 255, 000)

traceColour = GREY4
pointColour = RED
lineColour  = GREEN
bgColour    = WHITE

pointDiameter = 8
traceRadius   = 400
traceWidth    = 800
lineWeight    = 2
traceWeight   = 2
numOfPoints   = 100
pointGap      = 40
structure     = "Circle"

selectionList = [4, 6, 8, 5, 7, 7, 7, 1, 1, 1, 1, 1]

inSettings = False

SCREENNUM = 2



def setup():
    global settingsButton, traceColourSelector, pointColourSelector, lineColourSelector, bgColourSelector, pointDiameterSelector, traceRadiusSelector, traceWidthSelector, lineWeightSelector, traceWeightSelector, numOfPointsSelector, pointGapSelector, structureSelector, selectorList
    
    fullScreen(SCREENNUM)
    ellipseMode(RADIUS)
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    
    settingsButton        = gui.IconButton(width - 55, 55, 80, 80, (TRANSPARENT, TRANSPARENT, GREEN, BLACK, DARKGREEN, BLACK), iconFunc)
    traceColourSelector   = gui.ColourSelector(275,         180, 300, 100, 150, 90, 60, 60, (GREY4, WHITE, RED, DARKRED, GREEN, DARKGREEN, BLUE, DARKBLUE, YELLOW, DARKYELLOW, MAGENTA, DARKMAGENTA, CYAN, DARKCYAN, BLACK, GREY1, GREY2, GREY3))
    pointColourSelector   = gui.ColourSelector(625,         180, 300, 100, 150, 90, 60, 60, (RED, DARKRED, GREEN, DARKGREEN, BLUE, DARKBLUE, YELLOW, DARKYELLOW, MAGENTA, DARKMAGENTA, CYAN, DARKCYAN, BLACK, GREY1, GREY2, GREY3, GREY4, WHITE))
    lineColourSelector    = gui.ColourSelector(width - 625, 180, 300, 100, 150, 90, 60, 60, (GREEN, DARKGREEN, BLUE, DARKBLUE, YELLOW, DARKYELLOW, MAGENTA, DARKMAGENTA, CYAN, DARKCYAN, BLACK, GREY1, GREY2, GREY3, GREY4, WHITE, RED, DARKRED))
    bgColourSelector      = gui.ColourSelector(width - 275, 180, 300, 100, 150, 90, 60, 60, (WHITE, RED, DARKRED, GREEN, DARKGREEN, BLUE, DARKBLUE, YELLOW, DARKYELLOW, MAGENTA, DARKMAGENTA, CYAN, DARKCYAN, BLACK, GREY1, GREY2, GREY3, GREY4))
    pointDiameterSelector = gui.TextSelector(275,         430, 300, 100, 150, 90, 60, 60, ("8", "9", "10", "1", "2", "3", "4", "5", "6", "7"                    ), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    traceRadiusSelector   = gui.TextSelector(625,         430, 300, 100, 150, 90, 60, 60, ("400", "450", "500", "50", "100", "150", "200", "250", "300", "350"  ), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    traceWidthSelector    = gui.TextSelector(width - 625, 430, 300, 100, 150, 90, 60, 60, ("800", "900", "1000", "100", "200", "300", "400", "500", "600", "700"), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    lineWeightSelector    = gui.TextSelector(width - 275, 430, 300, 100, 150, 90, 60, 60, ("2", "3", "4", "5", "6", "7", "8", "9", "10", "1"                    ), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    traceWeightSelector   = gui.TextSelector(275,         680, 300, 100, 150, 90, 60, 60, ("2", "3", "4", "5", "6", "7", "8", "9", "10", "1"                    ), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    numOfPointsSelector   = gui.TextSelector(625,         680, 300, 100, 150, 90, 60, 60, ("100", "150", "200", "250", "300", "350", "400", "450", "500", "50"  ), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    pointGapSelector      = gui.TextSelector(width - 625, 680, 300, 100, 150, 90, 60, 60, ("40", "60", "80", "100", "120", "140", "160", "180", "200", "20"     ), (50, 50, 50, 50, 50, 50, 50, 50, 50, 50))
    structureSelector     = gui.TextSelector(width - 275, 680, 300, 100, 150, 90, 60, 60, ("Circle", "Square"))
    
    selectorList = [traceColourSelector, pointColourSelector, lineColourSelector, bgColourSelector, pointDiameterSelector, traceRadiusSelector, traceWidthSelector, lineWeightSelector, traceWeightSelector, numOfPointsSelector, pointGapSelector, structureSelector]
    


def draw():
    global inSettings, traceColour, pointColour, lineColour, bgColour, pointDiameter, traceRadius, traceWidth, lineWeight, traceWeight, numOfPoints, pointGap, structure
    
    background(bgColour)
    noFill()
    
    settingsButton.handle()
    if settingsButton.justReleased:
        if inSettings:
            traceColour   = traceColourSelector.currentColour
            pointColour   = pointColourSelector.currentColour
            lineColour    = lineColourSelector.currentColour
            bgColour      = bgColourSelector.currentColour
            pointDiameter = int(pointDiameterSelector.currentText)
            traceRadius   = int(traceRadiusSelector.currentText)
            traceWidth    = int(traceWidthSelector.currentText)
            lineWeight    = int(lineWeightSelector.currentText)
            traceWeight   = int(traceWeightSelector.currentText)
            numOfPoints   = int(numOfPointsSelector.currentText)
            pointGap      = int(pointGapSelector.currentText)
            structure     = structureSelector.currentText
            
            inSettings = False
        else:
            inSettings = True
    
    
    if inSettings:    
        settingsMenu()
    else:
        translate(width / 2, height / 2)
        strokeWeight(traceWeight)
        stroke(traceColour)
        noFill()
        if structure == "Circle":
            pointList = circle()
        elif structure == "Square":
            pointList = square()
            
        for i in range(numOfPoints):
            stroke(lineColour)
            strokeWeight(lineWeight)
            line(pointList[i][0], pointList[i][1], pointList[(i + pointGap) % numOfPoints][0], pointList[(i + pointGap) % numOfPoints][1])
            
        for i in range(numOfPoints):
            stroke(pointColour)
            strokeWeight(pointDiameter)
            point(pointList[i][0], pointList[i][1])
        
        
        
def iconFunc():
    fill(BLACK)
    noStroke()
    for i in range(4):
        rotate(radians(i * 45))
        rect(0, 0, 13, 55)
    
    fill(WHITE)
    ellipse(0, 0, 12, 12)
    
    
    
def settingsMenu():
    stroke(BLACK)
    fill(GREY4)
    rect(width / 2, height / 2, width - 20, height - 20)
    settingsButton.handle()
    
    fill(BLACK)
    textSize(30)
    
    text("Shape trace colour:", 275,         100, 300, 40)
    text("Point colour:",       625,         100, 300, 40)
    text("Line colour:",        width - 625, 100, 300, 40)
    text("Background colour:",  width - 275, 100, 300, 40)
    text("Point diameter:",     275,         350, 300, 40)
    text("Shape trace radius:", 625,         350, 300, 40)
    text("Shape trace width:",  width - 625, 350, 300, 40)
    text("Line width:",         width - 275, 350, 300, 40)
    text("Trace width:",        275,         600, 300, 40)
    text("Number of points:",   625,         600, 300, 40)
    text("Point gap:",          width - 625, 600, 300, 40)
    text("Shape:",              width - 275, 600, 300, 40)
    
    for selector in selectorList:
        selector.handle()
    


def circle():
    noFill()
    ellipse(0, 0, traceRadius, traceRadius)
    
    pointList = []
    for i in range(numOfPoints): 
        pointX = traceRadius * cos(TAU * i / numOfPoints)
        pointY = traceRadius * sin(TAU * i / numOfPoints)
        pointList.append([pointX, pointY])
    
    return pointList
    


def square():
    noFill()
    rect(0, 0, traceWidth, traceWidth)
    
    sidePoints = numOfPoints / 4.0
    unit = traceWidth / sidePoints
    
    pointList = []
    for i in range(numOfPoints): 
        if i >= 0 and i < sidePoints:
            pointX = (i - (1 * sidePoints / 2)) * unit
            pointY = -(sidePoints / 2) * unit
            
        elif i >= sidePoints and i < (2 * sidePoints):
            pointX = (sidePoints / 2) * unit
            pointY = (i - (3 * sidePoints / 2)) * unit
            
        elif i >= (2 * sidePoints) and i < (3 * sidePoints):
            pointX = (-i + (5 * sidePoints / 2)) * unit
            pointY = (sidePoints / 2) * unit
            
        else:
            pointX = -(sidePoints / 2) * unit
            pointY = (-i + (7 * sidePoints / 2)) * unit
            
        pointList.append([pointX, pointY])

    return pointList
