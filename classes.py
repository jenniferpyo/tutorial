from cmu_graphics import *
from PIL import Image
import os, pathlib
import random
# pepperoni: http://www.clker.com/clipart-pepperoni-1.html
# bacon: https://www.vecteezy.com/free-png/bacon 
# mushroom: https://in.pinterest.com/pin/png-clip-art--393853929905365183/ 

# customerList = [cs1, cs2, cs3, cs4, cs5]


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
    app.orderToppings = []
    app.currentToppings = []
    app.size = ['small', 'medium', 'large']
    app.type = ['marinara', 'alfredo', 'pesto']
    app.customer = ['A', 'B', 'C', 'D', 'E']
    app.orderDone = False 
    app.currOrder,app.currPizza = randomOrder(app)
    app.move = None
    app.currTopping = None

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

# def countScore(app):
#     if app.size == 'small':



def onMousePress(app, mouseX, mouseY):
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


def drawToppingSelection(app):
    if app.currPizza != None:
        drawCircle(app.currPizza.cx,app.currPizza.cy,app.currPizza.r,fill=app.currPizza.color)
    for topping in app.toppings:
        drawCircle(topping.cx,topping.cy,topping.r,fill = topping.color)

def redrawAll(app):
    drawRect(0,0, 450, app.height, fill = 'lightYellow')
    drawLabel('Toppings', 225, 50, size = 20)
    drawToppingSelection(app)
    drawRect(50, 400, 350, 350, border = 'black', fill = 'white')
    drawLabel(f'Type: {app.currOrder.type}', 100, 100)
    drawLabel(f'Size: {app.currOrder.size}', 200, 200)
    drawLabel(f'Customer Name: {app.currOrder.customer}', 300, 300)
    if app.currOrder.customer == 'A':
        newWidth, newHeight = app.cs1Width//3, app.cs1Height//3
        drawImage(app.cs1, 100, 600, width = newWidth, height = newHeight)


    # elif app.currOrder.customer == 'B':
    #     drawRect(x, y, width, height)
    # elif app.currOrder.customer == 'C':
    #     drawRect(x, y, width, height)
    # elif app.currOrder.customer == 'D':
    #     drawRect(x, y, width, height)
    # elif app.currOrder.customer == 'E':
    #     drawRect(x, y, width, height)
    

   



def play():
    runApp(width = 1200, height = 800)

def main():
    play()

main()
    

        