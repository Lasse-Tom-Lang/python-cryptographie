import PySimpleGUI as sg

class UI():
    backgroundColor = "#323232"
    highlightColor = "#404040"
    textColor = "white"
    layout_left = [
        [
            sg.FileBrowse("Choose Image", enable_events=True, key="-IMAGECHOOSED1-", button_color = (textColor, highlightColor), font = "Arial 14", target= "-FILEINPUTTARGET-"),sg.Button("Convert", key="-CONVERTTOIMAGE-", font = "Arial 14", button_color = (textColor, highlightColor)), sg.SaveAs("Save", key="-SAVEIMAGEBUTTON-", default_extension = ".png", target="-SAVEIMAGE-", disabled = True, button_color = (textColor, highlightColor), font = "Arial 14"),sg.In(key = "-OUTPUTKEY-", border_width= 0, disabled = True, font = "Arial 14", size=(10, 1), text_color = textColor, disabled_readonly_background_color = backgroundColor),sg.In(key="-FILEINPUTTARGET-", font = "Arial 14", size=(1, 1), visible = False),sg.In(key="-SAVEIMAGE-", font = "Arial 14", size=(1, 1), visible = False)
        ],
        [
            sg.Multiline(background_color = highlightColor, text_color = textColor, size=(40, 10), font = "Arial 14", key="-TEXTINPUT-", sbar_arrow_color=textColor, sbar_background_color=backgroundColor, sbar_trough_color=backgroundColor)
        ],
        [
            sg.Image("", key="-INPUTIMAGE-", expand_x = False, expand_y = False, subsample = 4, background_color=backgroundColor)
        ]
    ]
    layout_right = [
        [sg.In(key = "-INPUTKEY-", font = "Arial 14", size=(10, 1), text_color = textColor, background_color = highlightColor), sg.FileBrowse("Choose Image", button_color = (textColor, highlightColor), font = "Arial 14", target= "-FILEINPUTTARGET2-"), sg.Button("Convert", key="-CONVERTTOTEXT-", font = "Arial 14", button_color = (textColor, highlightColor)), sg.In(key="-FILEINPUTTARGET2-", font = "Arial 14", size=(1, 1), visible = False)],
        [
            sg.Multiline(background_color = highlightColor, text_color = textColor, size=(40, 10), font = "Arial 14", key="-TEXTOUTPUT-", sbar_arrow_color=textColor, sbar_background_color=backgroundColor, sbar_trough_color=backgroundColor)
        ],
        [
            sg.Image("", key="-OUTPUTIMAGE-", expand_x = False, expand_y = False, subsample = 4, background_color=backgroundColor)
        ]
    ]
    layout = [
        [
            sg.Column(layout_left, background_color=backgroundColor, vertical_alignment="top"),
            sg.VSeperator(color=textColor),
            sg.Column(layout_right, background_color=backgroundColor, vertical_alignment="top")
        ]
    ]
    Window = sg.Window("Converter", layout, background_color = backgroundColor, size=(740, 440))
