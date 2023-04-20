from cmu_graphics import *
from PIL import Image
import os, pathlib
# import classes

# start page 
# app level: 1
# start button
# instructions button 
# JP'S PIZZERIA logo 
# pizza image 

def onAppStart(app):
   # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.citypng.com%2Fsearch%3Fq%3Dclipart%2Bpizza%2Bno%2Bbackground&psig=AOvVaw0MB-621WdXPKJb6RODU8b1&ust=1681761138154000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLiwuc6Wr_4CFQAAAAAdAAAAABAQ
   app.image = Image.open(os.path.join(pathlib.Path(__file__).parent,"pizza1.jpg"))
   app.image = CMUImage(app.image)
   app.imageWidth, app.imageHeight = app.image.image.width, app.image.image.height
   app.screen = 'homepage'
   app.screen = 'instructions'

   app.x = 0
   app.y = 0


def homepage_redrawAll(app): 
   # background
   drawRect(0, 0, app.width, app.height, fill = 'beige')

   # pizza1
   newWidth, newHeight = (app.imageWidth//3 ,app.imageHeight//3)
   drawImage(app.image, app.width/2, app.height/2, width = newWidth, height = newHeight, align = 'center')

   # JP'S PIZZERIA logo 
   drawLabel("JP'S PIZZERIA", app.width/2, app.height/2 - 200, 
             size = 70, border = 'black', fill = 'brown')

   # start button
   drawRect(500, 600, 200, 50, border = 'black', fill = 'yellow')
   drawLabel('Start', 600, 625, size = 20)

   # start button pressed
   if ((app.x > 500 and app.x < 700) and (app.y > 600 and app.y < 650)):
      setActiveScreen('instructions')
      # initializeBuildScreen(app)
      

def homepage_onMousePress(app, mouseX, mouseY):
   # if click on start button 
   if ((mouseX > 500 and mouseX < 700) and (mouseY > 600 and mouseY < 650)):
      app.x = mouseX
      app.y = mouseY

def instructions_redrawAll(app):
   drawRect(100, 100, 1000, 600, border = 'black', fill = 'white')
   # close button
   drawRect(120, 120, 20, 20, border = 'black', fill = 'red')
   # start - given order button
   drawRect(450, 600, 100, 50, border = 'black', fill = 'yellow')
   drawLabel('Start(easy)', 500, 625)
   # start - random order button
   drawRect(650, 600, 100, 50, border = 'black', fill = 'yellow')
   drawLabel('Start(random)', 700, 625)

   drawLabel('INSERT INSTRUCTIONS', 600, 400)


def instructions_onMousePress(app, mouseX, mouseY):
   if ((mouseX > 120 and mouseX < 140) and (mouseY > 120 and mouseY < 140)):
      setActiveScreen('homepage')



def main():
   runAppWithScreens(initialScreen = 'homepage', width = 1200, height = 800)

main()

