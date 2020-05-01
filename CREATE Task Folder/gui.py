
from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image
class mainMenu():
    def __init__(self, rpg):
        #LoadButton Settings
        self.loadButton = Button(rpg, "Load")
        self.loadButton.startDefault(rpg, 75, 0)
        
        #OuterBorder
        self.borderSquare = square(rpg)
        self.borderSquare.width = rpg.settings.screen_width
        self.borderSquare.height = rpg.settings.screen_height
        self.borderSquare.top = 0
        self.borderSquare.left = 0
        self.borderSquare.color = (255, 255, 255)
        self.borderSquare.border = 1
        self.borderSquare.prep()
        
        #New game button
        self.newGameButton = Button(rpg, "New Game")
        self.newGameButton.startDefault(rpg, 0 , 0)
        
        #Quit Button
        self.quitButton = Button(rpg, "Quit")
        self.quitButton.startDefault(rpg, 150, 0)

        #Project Logo
        self.logo = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\ProjectLogo.png')#pylint: disable = anomalous-backslash-in-string
        self.logo.top = (rpg.settings.screen_height*.5) - (self.logo.height/2) - 200
        self.logo.left = (rpg.settings.screen_width*.5) - (self.logo.width/2)

    def mainMenuDraw(self):
        self.loadButton.update()
        self.loadButton.draw_button()

        self.newGameButton.update()
        self.newGameButton.draw_button()

        self.quitButton.update()
        self.quitButton.draw_button()

        self.logo.update()
        self.logo.blitme()

        self.borderSquare.prep()
        self.borderSquare.drawSquare()

def createChoiceButton(rpg):
    rpg.choice1.choiceDefault(rpg, -375, 0)
    rpg.choice2.choiceDefault(rpg, -300, 0)
    rpg.choice3.choiceDefault(rpg, -225, 0)
    rpg.choice4.choiceDefault(rpg, -150, 0)
    rpg.choice5.choiceDefault(rpg, -75, 0)
    rpg.choice6.choiceDefault(rpg, 0, 0)