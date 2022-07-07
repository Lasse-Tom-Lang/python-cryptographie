import verschluessler as verschl
import GUI
import PySimpleGUI as sg
import cv2
import shutil
import os

def main():
  verschluessler = verschl.Verschluessler()
  window = GUI.window(verschluessler.generateKey())
  while True:
    event, values = window.read(1000)
    if event == sg.WIN_CLOSED:
      break
    if values["-SAVEIMAGE-"] != "":
      try:
        shutil.move("output.png", values["-SAVEIMAGE-"])
        window["-SAVEIMAGE-"].update("")
      except:
        GUI.errorPopup("There was an error while saving the image.")
    if event == "-CONVERTTOIMAGE-" and values["-FILEINPUTTARGET-"] != "" and values["-TEXTINPUT-"] != "":
      try:
        verschlText = verschluessler.verschluesseln(values["-TEXTINPUT-"], key)
        verschlText += "§"
        with open("test.txt", "w") as file:
          file.write(verschlText)
        verschluessler.writeImage(values["-FILEINPUTTARGET-"])
        os.remove("test.txt")
        window["-SAVEIMAGEBUTTON-"].update(disabled = False)
      except:
        GUI.errorPopup("There was an error encrypting the message.")
    if event == "-CONVERTTOTEXT-" and values["-FILEINPUTTARGET2-"] != "" and values["-INPUTKEY-"] != "":
      try:
        key = int(values["-INPUTKEY-"])
        verschluessler.readImage(values["-FILEINPUTTARGET2-"])
        with open("out.txt", "r") as file:
          text = file.read().split("§")[0]
        os.remove("out.txt")
        output = verschluessler.entschluesseln(text, key)
        window["-TEXTOUTPUT-"].update(output)
      except:
        GUI.errorPopup("There was an error decrypting the message.")
    if event == "-FILEINPUTTARGET-":
      try:
        subsample = cv2.imread(values["-FILEINPUTTARGET-"]).shape[1] // 280
        window["-INPUTIMAGE-"].update(values["-FILEINPUTTARGET-"], subsample = subsample)
      except:
        GUI.errorPopup("Could not load image.")
    if event == "-FILEINPUTTARGET2-":
      try:
        subsample = cv2.imread(values["-FILEINPUTTARGET2-"]).shape[1] // 280
        window["-OUTPUTIMAGE-"].update(values["-FILEINPUTTARGET2-"], subsample = subsample)
      except:
        GUI.errorPopup("Could not load image.")
    
  window.close()
  
if __name__ == "__main__":
  main()
