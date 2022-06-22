import verschluessler as verschl
import GUI
import PySimpleGUI as sg
import cv2
import shutil
import os

def run():
  verschluessler = verschl.Verschluessler()
  key = verschluessler.generateKey()
  ui = GUI.UI
  window = ui.Window
  window.read(timeout = 1)
  window["-OUTPUTKEY-"].update("Key: " + str(key))
  while True:
    event, values = window.read(1000)
    if event == sg.WIN_CLOSED:
      break
    if values["-SAVEIMAGE-"] != "":
      try:
        shutil.move("output.png", values["-SAVEIMAGE-"])
        window["-SAVEIMAGE-"].update("")
      except:
        sg.popup_error("There was an error while saving the image.")
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
        sg.popup_error("There was an error encrypting the message.")
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
        sg.popup_error("There was an error decrypting the message.")
    if values["-FILEINPUTTARGET-"] != "":
      try:
        subsample = cv2.imread(values["-FILEINPUTTARGET-"]).shape[1] // 280
        window["-INPUTIMAGE-"].update(values["-FILEINPUTTARGET-"], subsample = subsample)
      except:
        sg.popup_error("There was an error loading the image on the left.")
    if values["-FILEINPUTTARGET2-"] != "":
      try:
        subsample = cv2.imread(values["-FILEINPUTTARGET2-"]).shape[1] // 280
        window["-OUTPUTIMAGE-"].update(values["-FILEINPUTTARGET2-"], subsample = subsample)
      except:
        sg.popup_error("There was an error loading the image on the right.")
    
  window.close()
  os.remove("__pycache__/GUI.cpython-310.pyc")
  os.remove("__pycache__/ImageConvertor.cpython-310.pyc")
  os.remove("__pycache__/verschluessler.cpython-310.pyc")
  os.rmdir("__pycache__")
  
if __name__ == "__main__":
  run()
