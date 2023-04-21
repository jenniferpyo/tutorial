from cmu_graphics import *
from PIL import Image
import os, pathlib
import random
import copy 
# pepperoni: http://www.clker.com/clipart-pepperoni-1.html
# bacon: https://www.vecteezy.com/free-png/bacon 
# mushroom: https://in.pinterest.com/pin/png-clip-art--393853929905365183/ 

class Order: 
    def __init__(self, size, type, customer, diffToppings, eachToppings):
        self.size = size
        self.type = type
        self.customer = customer
        self.diffToppings = []
        self.eachToppings = [] 

class Pizza(object):
    def __init__(self, cx, cy, r, color, name):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color
        self.name = name
        self.toppings = []

class Topping(object):
    def __init__(self, cx, cy, r, color):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color

pepperoni = Topping(125, 125, 25, 'red')
chicken = Topping(225, 125, 25, 'brown')
pork = Topping(325, 125, 25, 'pink')
beef = Topping(125, 225, 25, 'saddleBrown')
shrimp = Topping(225, 225, 25, 'peachPuff')
olives = Topping(325, 225, 25, 'darkKhaki')
potato = Topping(125, 325, 25, 'orange')
bacon = Topping(225, 325, 25, 'salmon')
mushroom = Topping(325, 325, 25, 'tan')

# toppingsList = [pepperoni, chicken, pork, beef, shrimp, olives, potato, bacon, mushroom]

def onAppStart(app):
# def initializeBuildScreen(app):
    app.score = 0
    app.toppings = []
    app.toppings.append(pepperoni)
    app.toppings.append(chicken)
    app.toppings.append(pork)
    app.toppings.append(beef)
    app.toppings.append(shrimp)
    app.toppings.append(olives)
    app.toppings.append(potato)
    app.toppings.append(bacon)
    app.toppings.append(mushroom)
    app.options = ['pepperoni', 'chicken', 'pork', 'beef', 'shrimp', 'olives', 'potato', 'bacon', 'mushroom']
    app.orderToppings = []
    app.currentToppings = []
    app.size = ['small', 'medium', 'large']
    app.type = ['marinara', 'alfredo', 'pesto']
    app.customer = ['A', 'B', 'C', 'D', 'E']
    app.orderDone = False 
    app.currOrder,app.currPizza = randomOrder(app)
    app.move = None
    app.toppingsOnPizza = []
    app.currTopping = None
    app.coordinates = [(125, 125), (225, 125), (325, 125), 
                       (125, 225), (225, 225), (325, 225), 
                       (125, 325), (225, 325), (325, 325)]
    app.cx = 0
    app.cy = 0

    # customer pictures all from https://creazilla.com/ 
    # customer 1
    app.cs1 = Image.open(os.path.join(pathlib.Path(__file__).parent,"customer1.jpg"))
    app.cs1 = CMUImage(app.cs1)
    app.cs1Width, app.cs1Height = app.cs1.image.width, app.cs1.image.height

    # customer 2
    app.cs2 = Image.open(os.path.join(pathlib.Path(__file__).parent,"customer2.jpg"))
    app.cs2 = CMUImage(app.cs2)
    app.cs2Width, app.cs2Height = app.cs2.image.width, app.cs2.image.height

    # customer 3
    app.cs3 = Image.open(os.path.join(pathlib.Path(__file__).parent,"customer3.jpg"))
    app.cs3 = CMUImage(app.cs3)
    app.cs3Width, app.cs3Height = app.cs3.image.width, app.cs3.image.height

    # customer 4
    app.cs4 = Image.open(os.path.join(pathlib.Path(__file__).parent,"customer4.jpg"))
    app.cs4 = CMUImage(app.cs4)
    app.cs4Width, app.cs4Height = app.cs4.image.width, app.cs4.image.height

    # customer 5
    app.cs5 = Image.open(os.path.join(pathlib.Path(__file__).parent,"customer5.jpg"))
    app.cs5 = CMUImage(app.cs5)
    app.cs5Width, app.cs5Height = app.cs5.image.width, app.cs5.image.height


def randomOrder(app):
    type = random.choice(app.type)
    if type == "marinara":
        baseColor = "red"
    elif type == "alfredo":
        baseColor = "yellow"
    elif type == "pesto":
        baseColor = "green"
    
    size = random.choice(app.size)
    pizzaRadius = 0
    if size == 'small':
        numDiffToppings = 3
        numEachTopping = 3
        pizzaRadius = 120
    elif size == 'medium':
        numDiffToppings = 4
        numEachTopping = 4
        pizzaRadius = 150
    elif size == 'large': 
        numDiffToppings = 5
        numEachTopping = 5
        pizzaRadius = 180
    
    customer = random.choice(app.customer)
    
    currOrder = Order(size, type, customer, numDiffToppings, numEachTopping)
    currPizza = Pizza(825 ,500, pizzaRadius, baseColor, customer)
    return currOrder, currPizza


def onMousePress(app, mouseX, mouseY):
    if(mouseX >= 100 and mouseX <= 350) and ((mouseY >= 100 and mouseY <= 350)):
        # pepperoni
        if (mouseX >= 100 and mouseX <= 150) and (mouseY >= 100 and mouseY <= 150):
            app.move = (mouseX, mouseY)
            app.currTopping = 'pepperoni'

        # chicken
        if (mouseX >= 200 and mouseX <= 250) and (mouseY >= 100 and mouseY <= 150):
            app.move = (mouseX, mouseY)
            app.currTopping = 'chicken'

        # pork 
        if (mouseX >= 300 and mouseX <= 350) and (mouseY >= 100 and mouseY <= 150):
            app.move = (mouseX, mouseY)
            app.currTopping = 'pork'

        # beef
        if (mouseX >= 100 and mouseX <= 150) and (mouseY >= 200 and mouseY <= 250):
            app.move = (mouseX, mouseY)
            app.currTopping = 'beef'

        # shrimp
        if (mouseX >= 200 and mouseX <= 250) and (mouseY >= 200 and mouseY <= 250):
            app.move = (mouseX, mouseY)
            app.currTopping = 'shrimp'
        
        # olives
        if (mouseX >= 300 and mouseX <= 350) and (mouseY >= 200 and mouseY <= 250):
            app.move = (mouseX, mouseY)
            app.currTopping = 'olives' 

        # potato 
        if (mouseX >= 100 and mouseX <= 150) and (mouseY >= 300 and mouseY <= 350):
            app.move = (mouseX, mouseY)
            app.currTopping = 'potato'

        # bacon
        if (mouseX >= 200 and mouseX <= 250) and (mouseY >= 300 and mouseY <= 350):
            app.move = (mouseX, mouseY)
            app.currTopping = 'bacon'

        # mushroom
        if (mouseX >= 300 and mouseX <= 350) and (mouseY >= 300 and mouseY <= 350):
            app.move = (mouseX, mouseY)
            app.currTopping = 'mushroom'


def onMouseDrag(app, mouseX, mouseY):
    app.cx = mouseX
    app.cy = mouseY

    if app.currTopping == 'pepperoni':
        app.toppings[0].cx,app.toppings[0].cy = mouseX, mouseY  

    if app.currTopping == 'chicken':
        app.toppings[1].cx, app.toppings[1].cy = mouseX, mouseY

    if app.currTopping == 'pork':
        app.toppings[2].cx, app.toppings[2].cy = mouseX, mouseY

    if app.currTopping == 'beef':
        app.toppings[3].cx, app.toppings[3].cy = mouseX, mouseY
    
    if app.currTopping == 'shrimp':
        app.toppings[4].cx, app.toppings[4].cy = mouseX, mouseY

    if app.currTopping == 'olives':
        app.toppings[5].cx, app.toppings[5].cy = mouseX, mouseY

    if app.currTopping == 'potato':
        app.toppings[6].cx, app.toppings[6].cy = mouseX, mouseY

    if app.currTopping == 'bacon':
        app.toppings[7].cx, app.toppings[7].cy = mouseX, mouseY
    
    if app.currTopping == 'mushroom':
        app.toppings[8].cx, app.toppings[8].cy = mouseX, mouseY


def onMouseRelease(app, mouseX, mouseY):
    if ((mouseX > app.currPizza.cx - app.currPizza.r and mouseX < app.currPizza.cx + app.currPizza.r) and 
        (mouseY > app.currPizza.cy - app.currPizza.r and mouseY < app.currPizza.cy + app.currPizza.r)):
        if app.currTopping != None: 
            index = app.options.index(app.currTopping) 
            newTopping = copy.deepcopy(app.toppings[index])
            app.toppings.append(newTopping)
            app.toppingsOnPizza.append(newTopping) 
        
            app.toppings[len(app.toppings) - 1].cx = app.coordinates[index][0]
            app.toppings[len(app.toppings) - 1].cy = app.coordinates[index][1]
            app.currTopping = None
    
    else:
        index = app.options.index(app.currTopping) 
        app.toppings[index].cx = app.coordinates[index][0]
        app.toppings[index].cy = app.coordinates[index][1]


def drawToppingSelection(app):
    if len(app.toppingsOnPizza) > 0:
        for i in range(len(app.toppingsOnPizza)):
         drawCircle(app.toppingsOnPizza[i].cx, app.toppingsOnPizza[i].cy, app.toppingsOnPizza[i].r, fill=app.toppingsOnPizza[i].color)
    if app.currPizza != None:
        drawCircle(app.currPizza.cx, app.currPizza.cy, app.currPizza.r, fill=app.currPizza.color)
    for topping in app.toppings:
        drawCircle(topping.cx, topping.cy, topping.r, fill = topping.color)


def redrawAll(app):
    drawRect(0,0, 450, app.height, fill = 'lightYellow')
    drawLabel('Toppings', 225, 50, size = 20)
    drawToppingSelection(app)
    drawRect(50, 400, 350, 350, border = 'black', fill = 'white')
    drawLabel(f'Customer Name: {app.currOrder.customer}', 70, 430, align = 'left', size = 15)
    drawLabel(f'Type: {app.currOrder.type}', 70, 480, align = 'left', size = 15)
    drawLabel(f'Size: {app.currOrder.size}', 70, 530, align = 'left', size = 15)
    
    if app.currOrder.customer == 'A':
        newWidth, newHeight = app.cs1Width//5, app.cs1Height//5
        drawImage(app.cs1, 235, 580, width = newWidth, height = newHeight)

    elif app.currOrder.customer == 'B':
        newWidth, newHeight = app.cs2Width//12, app.cs2Height//12
        drawImage(app.cs2, 235, 580, width = newWidth, height = newHeight)

    elif app.currOrder.customer == 'C':
        newWidth, newHeight = app.cs3Width//5, app.cs3Height//5
        drawImage(app.cs3, 235, 580, width = newWidth, height = newHeight)
    
    elif app.currOrder.customer == 'D':
        newWidth, newHeight = app.cs4Width//5, app.cs4Height//5
        drawImage(app.cs4, 235, 580, width = newWidth, height = newHeight)

    elif app.currOrder.customer == 'E':
        newWidth, newHeight = app.cs5Width//5, app.cs5Height//5
        drawImage(app.cs5, 235, 580, width = newWidth, height = newHeight)


   



def play():
    runApp(width = 1200, height = 800)

def main():
    play()

main()
    

        
