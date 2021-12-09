import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png" , confidence=.6)
x = position1[0]
y = position1[1]


#GET MESSAGE
def get_message():
    global x,y

    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png" , confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 30, y - 80, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Recieved : " + whatsapp_message)

    return whatsapp_message

# Posts
def post_response(message):
    global x,y

    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x +200 , y + 20 , duration =.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n" ,interval=.01)



# Processes response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any Question! I am a Bot."

    else:
        if random_no == 0:
            return "That's cool! I am a Bot"
        elif random_no == 1:
            return "Vijayasuriyan is on work!"
        else:
            return "I am a Bot."


#Check for new messages
def check_for_new_messages():
    pt.moveTo(x+50,y-35, duration=.5)

    while True:
        #Continuously checks for green dot and new messages
        try:
            position=pt.locateOnScreen("whatsapp/green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new other users with new messages located")

        if pt.pixelMatchesColor(int(x + 50), int(y - 35) ,(38,45,49), tolerance =10):
            print("is_Dark")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet ")
        sleep(.5)













check_for_new_messages()
#processed_message = process_response(get_message())
#post_response(processed_message)

