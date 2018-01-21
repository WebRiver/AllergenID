# AllergenID by Jordan Reichgut 2018
# run function modified from 15-112 class notes

import string
import querying
from tkinter import *

def init(data):
    data.homeScreen = True
    data.allergyScreen = False
    data.resultsScreen = False
    data.finalScreen = False

    # HOME SCREEN 
    data.allergies = []
    data.entry = ''
    data.entryFill = 'white'
    data.allergyBarFill = 'white'

    # ALLERGY SCREEN
    data.allergens = ['Corn', 'Dairy', 'Gluten', 'Wheat', 'Eggs', 'Fish',
                      'Shellfish', 'Peanuts', 'Tree Nuts', 'Soy', '$trawberries']

    data.cornFill = 'black'
    data.dairyFill = 'black'
    data.glutenFill = 'black'
    data.wheatFill = 'black'
    data.eggsFill = 'black'
    data.fishFill = 'black'
    data.shellfishFill = 'black'
    data.peanutsFill = 'black'
    data.treeNutsFill = 'black'
    data.soyFill = 'black'
    data.strawberriesFill = 'black'

    data.allergyFills = [data.cornFill, data.dairyFill, data.glutenFill, 
                         data.wheatFill, data.eggsFill, data.fishFill,
                         data.shellfishFill, data.peanutsFill, data.treeNutsFill,
                         data.soyFill, data.strawberriesFill]

    # RESULTS SCREEN
    data.results = []

def between(x, a, b):
    return a <= x and x <= b

def mousePressed(event, data):
    if data.homeScreen:
        # 'Select Your Allergies' is clicked
        if (data.width/2-150 <= event.x and event.x <= data.width/2+150 and
            data.height/4+25 <= event.y and event.y <= data.height/4+75):
            data.homeScreen = False
            data.allergyScreen = True
            data.allergies = []
        # 'Enter a Food Product' is clicked
        if (data.width/2-150 <= event.x and event.x <= data.width/2+150 and
            3*data.height/4-100 <= event.y and event.y <= 3*data.height/4-50):
            if data.entryFill == 'white': data.entryFill = 'lightBlue'
            else: data.entryFill = 'white'

    if data.allergyScreen:

        if (between(event.x, 9*data.width/10-100, 9*data.width/10) and
            between(event.y, 5*data.height/10, 5*data.height/10+40)):
            data.allergyScreen = False
            data.homeScreen = True

        if (between(event.x, data.width/4, data.width/2) and
            between(event.y, data.height/8+50, 2*data.height/8+50)):
            if data.cornFill == 'black':
                data.cornFill = 'red'
                data.allergies.append('CORN')
            else:
                data.cornFill = 'black'
                data.allergies.remove('CORN')

        if (between(event.x, data.width/4, data.width/2) and
            between(event.y, 2*data.height/8+51, 3*data.height/8+50)):
            if data.dairyFill == 'black':
                data.dairyFill = 'red'
                data.allergies.append('DAIRY')
            else:
                data.dairyFill = 'black'
                data.allergies.remove('DAIRY')

        if (between(event.x, data.width/4, data.width/2) and
            between(event.y, 3*data.height/8+51, 4*data.height/8+50)):
            if data.glutenFill == 'black':
                data.glutenFill = 'red'
                data.allergies.append('GLUTEN')
            else:
                data.glutenFill = 'black'
                data.allergies.remove('GLUTEN')

        if (between(event.x, data.width/4, data.width/2) and
            between(event.y, 4*data.height/8+51, 5*data.height/8+50)):
            if data.wheatFill == 'black':
                data.wheatFill = 'red'
                data.allergies.append('WHEAT')
            else:
                data.wheatFill = 'black'
                data.allergies.remove('WHEAT')

        if (between(event.x, data.width/4, data.width/2) and
            between(event.y, 5*data.height/8+51, 6*data.height/8+50)):
            if data.eggsFill == 'black':
                data.eggsFill = 'red'
                data.allergies.append('EGGS')
            else:
                data.eggsFill = 'black'
                data.allergies.remove('EGGS')

        if (between(event.x, data.width/2, 3*data.width/4) and
            between(event.y, data.height/8+50, 2*data.height/8+50)):
            if data.fishFill == 'black':
                data.fishFill = 'red'
                data.allergies.append('FISH')
            else:
                data.fishFill = 'black'
                data.allergies.remove('FISH')

        if (between(event.x, data.width/2, 3*data.width/4) and
            between(event.y, 2*data.height/8+51, 3*data.height/8+50)):
            if data.shellfishFill == 'black':
                data.shellfishFill = 'red'
                data.allergies.append('SHELLFISH')
            else:
                data.shellfishFill = 'black'
                data.allergies.remove('SHELLFISH')

        if (between(event.x, data.width/2, 3*data.width/4) and
            between(event.y, 3*data.height/8+51, 4*data.height/8+50)):
            if data.peanutsFill == 'black':
                data.peanutsFill = 'red'
                data.allergies.append('PEANUTS')
            else:
                data.peanutsFill = 'black'
                data.allergies.remove('PEANUTS')

        if (between(event.x, data.width/2, 3*data.width/4) and
            between(event.y, 4*data.height/8+51, 5*data.height/8+50)):
            if data.treeNutsFill == 'black':
                data.treeNutsFill = 'red'
                data.allergies.append('TREE NUTS')
            else:
                data.treeNutsFill = 'black'
                data.allergies.remove('TREE NUTS')

        if (between(event.x, data.width/2, 3*data.width/4) and
            between(event.y, 5*data.height/8+51, 6*data.height/8+50)):
            if data.soyFill == 'black':
                data.soyFill = 'red'
                data.allergies.append('SOY')
            else:
                data.soyFill = 'black'
                data.allergies.remove('SOY')

        if (between(event.x, data.width/4, 3*data.width/4) and
            between(event.y, 6*data.height/8+51, 7*data.height/8+50)):
            if data.strawberriesFill == 'black':
                data.strawberriesFill = 'red'
                data.allergies.append('$TRAWBERRIES')
            else:
                data.strawberriesFill = 'black'
                data.allergies.remove('$TRAWBERRIES')

   # if data.resultsScreen:
   #      if(between(event.y) ) 

def keyPressed(event, data):
    # use event.char and event.keysym
    if data.homeScreen:
        if data.entryFill == 'lightBlue':
            if event.keysym == 'BackSpace' and data.entry != '':
                data.entry = data.entry[:-1]
                if data.entry == '': data.entryFill = 'white'
            if event.keysym == 'Return':
                data.resultsScreen = True
                data.homeScreen = False
            elif event.keysym in string.printable:
                data.entry += event.keysym
            elif event.keysym == 'space':
                data.entry += ' '

def timerFired(data):
    pass

def write(arr):
    # assumes arr is an array of strings
    res = ''
    for c in arr:
        res += c + ', '

    return res[:-2] # exclude last comma

def drawResultsScreen(canvas, data):
    canvas.create_text(data.width/2, data.height/8, text='Search Results',
                       font='Athelas 50')
    y = data.height/8+50
    c = 0.875*data.height
    for i in range(len(data.results)):
        canvas.create_text(data.width/2, i*40 + 200, text=data.results[i],
                           font='Helvetica 20')

def drawHomeScreen(canvas, data):
    canvas.create_text(data.width/2, data.height/8, text='AllergenID',
                       font='Athelas 100')
    canvas.create_rectangle(data.width/2-150, data.height/4+25, data.width/2+150,
                            data.height/4+75, fill=data.allergyBarFill)
    canvas.create_text(data.width/2-250, data.height/4+50, text='STEP 1',
                       font='Athelas 30')
    canvas.create_text(data.width/2, data.height/4+50, text='Select Your Allergies...',
                       font='Helvetica 20')
    if data.allergies != []:
        data.allergyBarFill = 'green'
        canvas.create_text(data.width/2, data.height/4+100, text='Allergies: ' + write(data.allergies),
                           font='Helvetica 15 italic')
    if data.allergyBarFill == 'green' and data.allergies == []: data.allergyBarFill = 'white'
    canvas.create_rectangle(data.width/2-150, 3*data.height/4-100, data.width/2+150,
                            3*data.height/4-50, fill=data.entryFill)
    canvas.create_text(data.width/2-250, 3*data.height/4-75, text='STEP 2',
                       font='Athelas 30')
    canvas.create_text(data.width/2, 3*data.height/4-25, text='Press Enter to Search',
                           font='Helvetica 15 italic')
    if data.entryFill == 'white':
        canvas.create_text(data.width/2, 3*data.height/4-75, text='Enter a Food Product...',
                       font='Helvetica 20')
    else:
        canvas.create_text(data.width/2, 3*data.height/4-75, text=data.entry,
                       font='Helvetica 20')
        
def drawAllergyScreen(canvas, data):
    canvas.create_text(data.width/2, data.height/8, text='Select Your Allergies',
                       font='Athelas 50')
    canvas.create_rectangle(data.width/4, data.height/8+50, 3*data.width/4, 7*data.height/8+50)
    canvas.create_line(data.width/2, data.height/8+50, data.width/2, 6*data.height/8+50)
    y = 2*data.height/8+50
    c = data.height/8
    for i in range(6):
        canvas.create_line(data.width/4, y + i*c, 3*data.width/4, y + i*c)
        if i < 5: 
            canvas.create_text(3*data.width/8, y + i*c - data.height/16, text=data.allergens[i],
                               fill=data.allergyFills[i], font='Helvetica 20')
            canvas.create_text(5*data.width/8, y + i*c - data.height/16, text=data.allergens[i+5],
                               fill=data.allergyFills[i+5], font='Helvetica 20')
    canvas.create_text(data.width/2, y + 5*c - data.height/16, text=data.allergens[-1],
                               fill=data.allergyFills[-1], font='Helvetica 20 italic')
    if data.allergies != []:
        canvas.create_text(data.width/2, 7*data.height/8+75, text='Allergies: ' + str(data.allergies),
                           font='Helvetica 15')
    canvas.create_rectangle(9*data.width/10, 5*data.height/10, 9*data.width/10-100, 5*data.height/10+40)
    canvas.create_text(9*data.width/10-50, 5*data.height/10+20, text='NEXT', font='Helvetica 15')
    

def redrawAll(canvas, data):
    if data.homeScreen: drawHomeScreen(canvas, data)
    elif data.allergyScreen: drawAllergyScreen(canvas, data)
    elif data.resultsScreen: drawResultsScreen(canvas, data)

################################################################################
################################################################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    root.title('AllergenID')
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)