'''
PROJECT 1 - SIMPLE GAME
Programmer: Jonathan Camacho Ortega
ID: 117820
'''

from graphics import *
from random import *
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def drawEnemy(center, size, color, win): #all of the dimensions are dependent on it's center and size
    face = Circle(center, size)
    face.setFill(color)
    face.setOutline("white")

    #give him black eyes
    leftEye = Circle(Point(center.getX() - (size * 0.3), center.getY() + (size * 0.3)), size/10)
    leftEye.setFill("black")

    rightEye = Circle(Point(center.getX() + (size * 0.3), center.getY() + (size * 0.3)), size/10)
    rightEye.setFill("black")
    
    if color == "red": #swap his smile from a frown
        smile = Polygon(Point(center.getX(), center.getY() - (size * 0.3)), Point(center.getX() - (size * 0.4), center.getY() - (size * 0.7)), Point(center.getX() + (size * 0.4), center.getY() - (size * 0.7)))
        smile.setFill("white")
    else: #draw a normal smile
        smile = Polygon(Point(center.getX(), center.getY() - (size * 0.7)), Point(center.getX() - (size * 0.4), center.getY() - (size * 0.3)), Point(center.getX() + (size * 0.4), center.getY() - (size * 0.3)))
        smile.setFill("white")
    
    #give him brows
    leftBrow = Line(Point(center.getX() - 0.5, center.getY() + (size * 0.3)), Point(center.getX() - size, center.getY() + (size)))
    rightBrow = Line(Point(center.getX() + 0.5, center.getY() + (size * 0.3)), Point(center.getX() + size, center.getY() + (size)))
    
    #The function returns a list of the graphic objects used for the face, to be able to draw, undraw them and even customize the face.
    graphicObjects = [face, leftEye, rightEye, smile, leftBrow, rightBrow]
    return graphicObjects #Keep this list in mind
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hit(graphicObjects, leftEye, rightEye, win): #Changes the enemy's face to look like he got hit
    #Switches the eyes for the brows
    leftEye = graphicObjects[4]
    leftEye.draw(win)
    rightEye = graphicObjects[5]
    rightEye.draw(win)
    leftEye = graphicObjects[1]
    leftEye.undraw()
    rightEye = graphicObjects[2]
    rightEye.undraw()
    
    print("\n\tYou hit the opponent and he lost 20 health points!")
    print("\tClick anywhere to continue...")
    win.getMouse()
    
    #Switches the brows for the eyes
    leftEye = graphicObjects[4]
    leftEye.undraw()
    rightEye = graphicObjects[5]
    rightEye.undraw()
    leftEye = graphicObjects[1]
    leftEye.draw(win)
    rightEye = graphicObjects[2]
    rightEye.draw(win)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def userAttack(graphicObjects, leftEye, rightEye, win): #Creates a line simulating an attack
    attack = Line(Point(10, 20), Point(30, 30))
    attack.setFill("light blue")
    attack.draw(win)
    
    hit(graphicObjects, leftEye, rightEye, win)
    
    attack.undraw()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def enemyAttack(win): #Creates a line simulating an attack
    attack = Line(Point(25, 30), Point(10, 20))
    attack.setFill("purple")
    attack.draw(win)
    
    print("\n\tYou got hit and lost 20 health points!")
    print("\tClick anywhere to continue...")
    win.getMouse()
    
    attack.undraw()

def drawUser(username, color, win):
    user = Circle(Point(10, 20), 5)
    user.setFill(color)
    user.setOutline("white")
    user.draw(win)
    name = Text(Point(10, 20), username) #prints the user's name onto the graphic
    name.setSize(10)
    name.draw(win)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------  
def welcome_screen(win):
    welcome_message = Text(Point(20, 26), "Welcome to Simple Game!")
    welcome_message.setTextColor("white")
    welcome_message.setStyle("bold")
    welcome_message.setSize(14)
    welcome_message.draw(win)
    
    inst_message = Text(Point(20, 22), "Enter your name to start playing.")
    inst_message.setTextColor("white")
    inst_message.draw(win)
    
    inputBox = Entry(Point(20, 18), 10)
    inputBox.setSize(10)
    inputBox.setTextColor("white")
    inputBox.draw(win)
    
    start_button = Rectangle(Point(15, 13), Point(25, 16))
    start_button.setFill("light gray")
    start_button.setOutline("white")
    start_button.draw(win)
    
    start_message = Text(Point(20, 14.5), "START")
    start_message.setTextColor("white")
    start_message.setStyle("bold")
    start_message.draw(win)
    
    #draws an enemy face in the welcome screen; every component is assigned to a variable
    graphicObjects = drawEnemy(Point(20, 5), 3, "gold", win)
    face = graphicObjects[0]
    face.draw(win)
    leftEye = graphicObjects[1]
    leftEye.draw(win)
    rightEye = graphicObjects[2]
    rightEye.draw(win)
    smile = graphicObjects[3]
    smile.draw(win)
    
    #Get the user's name as input in the inputBox Entry
    username = ""
    while True:
        pt = win.checkMouse()
        if str(type(pt)) == "<class 'NoneType'>": #if the user does not click, it continues the loop
            continue
        elif 15 < pt.getX() < 25 and 13 < pt.getY() < 16: #if the point is within the start_button dimensions, it gets the text within the Entry box
            username = inputBox.getText()
            break;
    
    #undraw the welcome screen after the user presses START
    welcome_message.undraw()
    inst_message.undraw()
    inputBox.undraw()
    start_button.undraw()
    start_message.undraw()
    face.undraw()
    leftEye.undraw()
    rightEye.undraw()
    smile.undraw()
    
    #returns the user's name
    return username

def option_board(win):
    #draw the option board
    options = Rectangle(Point(1, 1), Point(39, 10))
    options.setFill("white")
    options.draw(win)
    
    attack_button = Rectangle(Point(3, 3), Point(13, 8))
    attack_button.setFill("light gray")
    attack_button.draw(win)
    attack_message = Text(Point(8, 5.5), "ATTACK")
    attack_message.setStyle("bold")
    attack_message.draw(win)
    
    block_button = Rectangle(Point(15, 3), Point(25, 8))
    block_button.setFill("light gray")
    block_button.draw(win)
    block_message = Text(Point(20, 5.5), "BLOCK")
    block_message.setStyle("bold")
    block_message.draw(win)
    
    rest_button = Rectangle(Point(27, 3), Point(37, 8))
    rest_button.setFill("light gray")
    rest_button.draw(win)
    rest_message = Text(Point(32, 5.5), "REST")
    rest_message.setStyle("bold")
    rest_message.draw(win)





















#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    win = GraphWin("Simple Game", 400, 400)
    win.setCoords(0.0, 0.0, 40.0, 40.0)
    win.setBackground("lightblue")
    
    username = welcome_screen(win) #calls the welcome_screen function and gets the user's name
    print("\n---------------------------------THE SIMPLE GAME--------------------------------------")
    print("Welcome, " + username + "!\n")
    print("This yellow face is your opponent.")
    
    win.setBackground("beige")
    
    #draw the user
    drawUser(username, "light blue", win)
    
    #draw the initial enemy
    graphicObjects = drawEnemy(Point(30, 30), 5, "gold", win) 
    face = graphicObjects[0]
    face.draw(win)
    leftEye = graphicObjects[1]
    leftEye.draw(win)
    rightEye = graphicObjects[2]
    rightEye.draw(win)
    smile = graphicObjects[3]
    smile.draw(win)
    
    #calls the function and draws the option board
    option_board(win)
    
    #variables
    user_health = 100
    enemy_health = 100
    #resting heals 5 health
    #attacking deals 10 health damage
    #blocking nullifies damage
    numOfRounds = 0
    score = 0
    
    #opponent random options
    enemy_options = ["attack", "block", "rest"]
    
    #the Simple Game
    print("\nThis is a (load, shoot, shield)-style game.")
    print("Predicting your opponent's next move leads to victory!")
    print("Choose your first move!")
    while True:
        #Check for user clicks
        pt = win.checkMouse()
        if str(type(pt)) == "<class 'NoneType'>": #if the user does not click, it continues the loop
            continue
        else:
            #Plays the game
            numOfRounds += 1
            print("\nStart of round--------------------------------------------------------------")
            print("\t\tRound " + str(numOfRounds) + ":")
            print("User health: " + str(user_health) + "    Enemy health: " + str(enemy_health))
        
            #a random option from the opponent
            rand = randint(0, 2)
            enemy_choice = enemy_options[rand]
            
            #See if the click-point was inside the buttons
            attack_condition = 3 <= pt.getX() <= 13 and 3 <= pt.getY() <= 8
            block_condition = 15 <= pt.getX() <= 25 and 3 <= pt.getY() <= 8
            rest_condition = 27 <= pt.getX() <= 37 and 3 <= pt.getY() <= 8
            enemy_turn = False
            
            #If the user clicks somewhere other than the buttons
            if attack_condition == 0 and block_condition == 0 and rest_condition == 0:
                print("\n\tYou must click one of the option buttons.")
                numOfRounds -= 1
            
            #User conditions
            if attack_condition: #if the user chose ATTACK
                if enemy_choice == "block": #if the opponent chose BLOCK
                    print("\n\tThe opponent blocked your attack!") #enemy block output covered
                else: #if the opponent did not choose BLOCK; the opponent gets hit
                    userAttack(graphicObjects, leftEye, rightEye, win)
                    enemy_health -= 20 #opponent loses 20 health points
                    score += 100 #adds 100 to the score
                if enemy_health > 0: #just in case the opponent rests while on 0 health
                    enemy_turn = True
            elif block_condition: #if the user chose BLOCK
                if enemy_choice == "attack": #if the opponent chose ATTACK
                    print("\n\tYou blocked the opponent's attack!")
                    score += 50 #adds 50 to the score
                else: 
                    print("\n\tYou tried to block.")
                enemy_turn = True
            elif rest_condition:#if the user chose REST
                print("\n\tYou rested and gained 10 health points.")
                user_health += 10 #user gains 10 health points
                score += 20 #adds 20 to the score
                if enemy_choice == "block":
                    print("\n\tThe opponent tried to block.")
                enemy_turn = True
            
            #Opponent conditions
            if enemy_turn:
                if enemy_choice == "attack": #if the enemy chose ATTACK
                    if block_condition == False: #if the user did not choose BLOCK; he gets hit
                        enemyAttack(win)
                        user_health -= 20 #user loses 20 health points
                        score -= 30
            #the block scenario was covered in the user conditions above ^
                if enemy_choice == "rest":
                    print("\n\tThe opponent rested and gained 10 health points.")
                    enemy_health += 10
            
            #Specific scenario
            if block_condition and enemy_choice == "block":
                print("\n\tBoth blocked; it's a stand-off!")
                
                
            #Dictates the end of a round
            print("\nEnd of round---------------------------------------------------------------")
            print("User health: " + str(user_health) + "    Enemy health: " + str(enemy_health))
            print("Choose your option...")
            print("-----------------------------------------------------------------------------")
            
            #Conditions to change the appearance of the opponent
            if 25 < enemy_health <= 50:
                #undraw the previous face
                face.undraw()
                leftEye.undraw()
                rightEye.undraw()
                smile.undraw()
                #make the opponent orange and have permanent brows
                graphicObjects = drawEnemy(Point(30, 30), 5, "orange", win) 
                face = graphicObjects[0]
                face.draw(win)
                leftEye = graphicObjects[1]
                leftEye.draw(win)
                rightEye = graphicObjects[2]
                rightEye.draw(win)
                smile = graphicObjects[3]
                smile.draw(win) 
                #make the opponent orange
            elif enemy_health <= 25:
                #undraw the previous face
                face.undraw()
                leftEye.undraw()
                rightEye.undraw()
                smile.undraw()
                #make the opponent red, have permanent brows, and a switched smile
                graphicObjects = drawEnemy(Point(30, 30), 5, "red", win) 
                face = graphicObjects[0]
                face.draw(win)
                leftEye = graphicObjects[1]
                leftEye.draw(win)
                rightEye = graphicObjects[2]
                rightEye.draw(win)
                smile = graphicObjects[3]
                smile.draw(win)
                #make the opponent red
                
            #Conditions to exit the game
            if enemy_health <= 0 and user_health <= 0:
                print("\n\tWow! It's a tie!")
                print("\nThere are no winners here. Try again :)")
                break
            elif enemy_health <= 0:
                print("\n\tThe opponent fainted!")
                face.undraw()
                leftEye.undraw()
                rightEye.undraw()
                smile.undraw()
                #fainted silouhette
                fainted = Oval(Point(25, 25), Point(35, 30))
                fainted.setFill("gray")
                fainted.draw(win)
                #victory message
                victory = Text(Point(20, 38), username + " WINS!")
                victory.setStyle("bold")
                victory.draw(win)
                break
            elif user_health <= 0:
                print("\n\tYou fainted!")
                #fainted silouhette
                drawUser("fainted", "gray", win)
                #failure message
                failure = Text(Point(20, 38), username + " fainted.")
                failure.setStyle("bold")
                failure.draw(win)
                #make sure that the enemy has a smile when victorious
                smile.undraw()
                graphicObjects = drawEnemy(Point(30, 30), 5, "orange", win)
                smile = graphicObjects[3]
                smile.draw(win)
                break
#----------------------------------------RESULTS---------------------------------------------------
    print("\nYour score is: " + str(score))
    
    outfile = open("projectScore.txt", "a")
    #add the new user and score
    print(str(score) + " " + username, file=outfile)
    outfile.close()
    
    infile = open("projectScore.txt", "r")
    standings = infile.read().splitlines()
    standings = sorted(standings)
    
    print("\n\n-----------------------------------------------------------------------------------------")
    print("\t\tLEADERBOARDS")
    print("-----------------------------------------------------------------------------------------")
    for i in range(len(standings)):
        print(standings[-(i + 1)])
        
    print("\n\nClick anywhere to exit...")
    win.getMouse()
                
main()