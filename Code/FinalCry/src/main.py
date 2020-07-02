# import the library
from appJar import gui

# handle button events
#def press(button):
#    if sdfbutton == "Cancel":
#        app.stop()
#    else:
#        usr = app.getEntry("Username")
#        pwd = app.getEntry("Password")
#        print("User:", usr, "Pass:", pwd)
#        app.addLabel("result", "Your name is: %s." % usr)
#        app.emptyCurrentContainer()

def createGUI():
    # create a GUI variable called app
    app = gui("NBA2k20 hacking tool", "600x700")
    app.setBg("grey")
    app.setFont(18)

    # add image
    app.addImage("thumbnail", "game.png")
    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "NBA2k20 gameplay editor")
    app.setLabelFg("title", "white")

    app.check("max speed")
    app.check("max vertical")
    app.check("unlimited stamina")
    app.check("green shot")
    app.check("100% shot success")

    # link the buttons to the function called press
    #app.addButtons(["Submit", "Cancel"], press)


    # start the GUI
    app.go()