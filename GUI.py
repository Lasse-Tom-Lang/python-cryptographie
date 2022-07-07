import PySimpleGUI as sg

backgroundColor = "#323232"
highlightColor = "#404040"
textColor = "white"

def window(key):
    layout = [
        [
            sg.Column(
                [
                    [
                        sg.FileBrowse(
                            "Choose Image",
                            enable_events=True,
                            key="-IMAGECHOOSED1-",
                            button_color = (textColor, highlightColor),
                            font = "Arial 14", target= "-FILEINPUTTARGET-"
                        ),
                        sg.Button(
                            "Convert",
                            key="-CONVERTTOIMAGE-",
                            font = "Arial 14",
                            button_color = (textColor, highlightColor),
                            expand_x=True
                        ),
                        sg.SaveAs(
                            "Save",
                            key="-SAVEIMAGEBUTTON-",
                            default_extension = ".png",
                            target="-SAVEIMAGE-",
                            disabled = True,
                            button_color = (textColor, highlightColor),
                            font = "Arial 14"
                        ),
                        sg.In(
                            f"Key: {key}",
                            key = "-OUTPUTKEY-",
                            border_width= 0,
                            disabled = True,
                            font = "Arial 14",
                            size=(10, 1),
                            text_color = textColor,
                            disabled_readonly_background_color = backgroundColor
                        ),
                        sg.In(
                            key="-FILEINPUTTARGET-",
                            font = "Arial 14",
                            size=(1, 1),
                            visible = False,
                            change_submits=True
                        ),
                        sg.In(
                            key="-SAVEIMAGE-",
                            font = "Arial 14",
                            size=(1, 1),
                            visible = False
                        )
                    ],
                    [
                        sg.Multiline(
                            background_color = highlightColor,
                            text_color = textColor,
                            size=(40, 10),
                            font = "Arial 14",
                            key="-TEXTINPUT-",
                            sbar_arrow_color=textColor,
                            sbar_background_color=backgroundColor,
                            sbar_trough_color=backgroundColor,
                            expand_x=True,
                            expand_y=True
                        )
                    ],
                    [
                        sg.Image(
                            "",
                            key="-INPUTIMAGE-",
                            expand_x = True,
                            expand_y = True,
                            background_color=backgroundColor
                        )
                    ]
                ],
                background_color=backgroundColor,
                expand_x=True,
                expand_y=True
            ),
            sg.VSeperator(
                color=textColor
            ),
            sg.Column(
                [
                    [
                        sg.In(
                            key = "-INPUTKEY-",
                            font = "Arial 14",
                            size=(10, 1),
                            text_color = textColor,
                            background_color = highlightColor,
                            expand_x=True
                        ),
                        sg.FileBrowse(
                            "Choose Image",
                            button_color = (textColor, highlightColor),
                            font = "Arial 14",
                            target= "-FILEINPUTTARGET2-"
                        ),
                        sg.Button(
                            "Convert",
                            key="-CONVERTTOTEXT-",
                            font = "Arial 14",
                            button_color = (textColor, highlightColor),
                            expand_x=True
                        ),
                        sg.In(
                            key="-FILEINPUTTARGET2-",
                            font = "Arial 14",
                            size=(1, 1),
                            visible = False,
                            change_submits=True
                        )
                    ],
                    [
                        sg.Multiline(
                            background_color = highlightColor,
                            text_color = textColor,
                            size=(40, 10),
                            font = "Arial 14",
                            key="-TEXTOUTPUT-",
                            sbar_arrow_color=textColor,
                            sbar_background_color=backgroundColor,
                            sbar_trough_color=backgroundColor,
                            expand_x=True,
                            expand_y=True
                        )
                    ],
                    [
                        sg.Image(
                            "",
                            key="-OUTPUTIMAGE-",
                            expand_x = True,
                            expand_y = True,
                            background_color=backgroundColor
                        )
                    ]
                ],
                background_color=backgroundColor,
                expand_x=True,
                expand_y=True
            )
        ]
    ]
    return sg.Window(
        "Converter",
        layout,
        background_color=backgroundColor,
        size=(740, 440),
        resizable=True
    )

def errorPopup(message):
    return sg.PopupError(
        message,
        background_color=backgroundColor,
        text_color=textColor,
        button_color=(textColor, "red")
    )